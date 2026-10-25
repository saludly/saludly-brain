/**
 * Saludly · Envío de la semana de prueba: arrancarla, mandar lo que ya toca y entregar lo que quedó esperando.
 * Lo usan semana-programador (cada 5 minutos) y whatsapp-webhook (cuando la persona escribe o toca un botón).
 * Cada fila se "toma" con un update atómico (pendiente/esperando → enviando) para que dos llamadas no la manden dos veces.
 */
import { DIAS, fechaBogota, primerNombre, semana } from "./semana.ts";
import { enviarBotones, enviarPlantilla, enviarTexto } from "./whatsapp.ts";

// Margen antes de las 24 horas: pasado esto ya no se arriesga un mensaje libre
const VENTANA = 23.5 * 3600_000;

export type Pre = {
  id: string; nombre: string; celular_whatsapp: string; objetivos: string[]; alergias: string[]; codigo: string;
  estado: string; quiere_prueba: boolean; prueba_inicio: string | null; prueba_dia: number;
  ultimo_mensaje: string | null; ultima_plantilla: string | null; bienvenida_enviada: string | null; creado: string;
};
export const CAMPOS = "id, nombre, celular_whatsapp, objetivos, alergias, codigo, estado, quiere_prueba, prueba_inicio, prueba_dia, ultimo_mensaje, ultima_plantilla, bienvenida_enviada, creado";
type Fila = { id: number; dia: number; orden: number; envio: string; texto: string; botones: string[]; resumen: string; programado: string };

export const ventanaAbierta = (p: Pre, ahora = new Date()) => !!p.ultimo_mensaje && ahora.getTime() - new Date(p.ultimo_mensaje).getTime() < VENTANA;

/** Arma los 7 días desde ahora y los guarda (si ya los tenía, no hace nada). */
// deno-lint-ignore no-explicit-any
export async function arrancar(admin: any, p: Pre, ahora = new Date()) {
  if (p.prueba_inicio) return false;
  const filas = (await semana(p, ahora)).map((f) => ({ ...f, preregistro_id: p.id }));
  const { error } = await admin.from("semana_envios").insert(filas);
  if (error) { console.error("no se guardó la semana", error.message); return false; }
  await admin.from("preregistros").update({ prueba_inicio: ahora.toISOString(), prueba_dia: 1, actualizado: ahora.toISOString() }).eq("id", p.id);
  p.prueba_inicio = ahora.toISOString();
  return true;
}

// deno-lint-ignore no-explicit-any
async function tomar(admin: any, p: Pre, desde: string[], ahora: Date): Promise<Fila[]> {
  const { data } = await admin.from("semana_envios").update({ estado: "enviando" })
    .eq("preregistro_id", p.id).in("estado", desde).lte("programado", ahora.toISOString()).select("id, dia, orden, envio, texto, botones, resumen, programado");
  return ((data ?? []) as Fila[]).sort((a, b) => a.programado.localeCompare(b.programado) || a.dia - b.dia || a.orden - b.orden);
}

/** Manda lo que ya toca. Con la ventana cerrada, una plantilla (máximo una al día) y lo demás queda esperando. */
// deno-lint-ignore no-explicit-any
export async function entregar(admin: any, p: Pre, ahora = new Date()) {
  if (p.estado !== "registrado") return 0;
  const filas = await tomar(admin, p, ventanaAbierta(p, ahora) ? ["pendiente", "esperando"] : ["pendiente"], ahora);
  if (!filas.length) return 0;
  if (!ventanaAbierta(p, ahora)) {
    const hoy = fechaBogota(ahora);
    if (p.ultima_plantilla !== hoy) {
      const nombre = primerNombre(p.nombre), primera = filas[0];
      const cierre = filas.find((f) => f.dia === DIAS && f.envio === "examen");
      const ok = cierre
        ? await enviarPlantilla(p.celular_whatsapp, "cierre_semana", [nombre])
        : await enviarPlantilla(p.celular_whatsapp, "recordatorio_dia", [nombre, primera.resumen]);
      if (ok) {
        await admin.from("preregistros").update({ ultima_plantilla: hoy }).eq("id", p.id);
        p.ultima_plantilla = hoy;
      }
    }
    await admin.from("semana_envios").update({ estado: "esperando" }).in("id", filas.map((f) => f.id));
    return 0;
  }
  let enviados = 0;
  for (const f of filas) {
    const ok = f.botones.length
      ? await enviarBotones(p.celular_whatsapp, f.texto, f.botones.map((b, k) => ({ id: `sp:${f.dia}:${f.orden}:${k}`, titulo: b })))
      : await enviarTexto(p.celular_whatsapp, f.texto);
    await admin.from("semana_envios").update(ok ? { estado: "enviado", enviado: new Date().toISOString() } : { estado: "error" }).eq("id", f.id);
    if (ok) enviados++;
  }
  const dia = Math.max(...filas.map((f) => f.dia));
  if (dia > p.prueba_dia) {
    await admin.from("preregistros").update({ prueba_dia: dia }).eq("id", p.id);
    p.prueba_dia = dia;
  }
  return enviados;
}
