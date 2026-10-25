/**
 * Saludly · Semana de prueba de la preventa: los mensajes de cada día para una persona del pre-registro y su hora de envío.
 *
 * Es la misma lógica de codigo/informe/semana_prueba.py (mensajes, reparto de consejos, cortisol y recetas sin alérgenos,
 * con su código como semilla), con el contenido aprobado que exporta codigo/herramientas/exportar_semana.py a semana.json.
 * probar_semana.ts compara lo que arma este archivo con lo que arma el Python: deben salir iguales, letra por letra.
 * Sin examen no hay hallazgos: no se diagnostica nada.
 */
import S from "./semana.json" with { type: "json" };

export const DIAS = 7;
const MAX_OBJETIVOS = 3;
// Espacios de consejos por objetivo: las 7 mañanas y las tardes de los días 1 a 6 (la del día 7 la ocupa el cierre)
const ESPACIOS: [number, string][] = [
  ...Array.from({ length: DIAS }, (_, k) => [k + 1, "manana"] as [number, string]),
  ...Array.from({ length: DIAS - 1 }, (_, k) => [k + 1, "tarde"] as [number, string]),
];
const ALERGIA: Record<string, string> = {
  mani: "maní", frutos_secos: "frutos secos", mariscos: "mariscos", pescado: "pescado", huevo: "huevo",
  leche: "leche", lactosa: "lactosa", gluten: "gluten", soya: "soya", ajonjoli: "ajonjolí",
};
const DEPORTE = ["masa_muscular", "atletico", "rendimiento", "maraton"];
const TIEMPOS = ["almuerzo", "desayuno", "cena", "almuerzo", "merienda", "cena", "desayuno"];

export type Persona = { nombre: string; objetivos: string[]; alergias: string[]; codigo: string };
export type Mensaje = { envio: string; hora: string; texto: string; botones: string[] };
type Consejo = { id: string; turno: string; texto: string };
type Receta = (typeof S.recetas)[number];

// deno-lint-ignore no-explicit-any
const C = S as any;
export const contenido = C;

const formato = (t: string, v: Record<string, string>) => t.replace(/\{(\w+)\}/g, (m, k) => (k in v ? v[k] : m));
export const primerNombre = (n: string) => n.trim().split(/\s+/)[0];

function familia(objetivo: string) {
  return Object.entries(C.familias as Record<string, string[]>).find(([, objs]) => objs.includes(objetivo))![0];
}

/** 'Aumentar mi masa muscular' → 'aumentar tu masa muscular'. */
function objetivoEnTu(nombre: string) {
  const t = nombre[0].toLowerCase() + nombre.slice(1);
  return t.replace(/\bmi\b/g, "tu").replace("que ya tengo", "que ya tienes");
}

function fraseAlergias(alergias: string[]) {
  const n = alergias.map((a) => ALERGIA[a] ?? a);
  if (!n.length) return "";
  const lista = n.length === 1 ? n[0] : n.slice(0, -1).join(", ") + " ni " + n[n.length - 1];
  return ` Ninguna receta lleva ${lista}.`;
}

/** Los que eligió, en su orden y sin "Otro" (hasta 3); si no queda ninguno, salud general. */
export function objetivosPersona(objetivos: string[]) {
  const v = [...new Set((objetivos ?? []).filter((o) => o in C.objetivos))].slice(0, MAX_OBJETIVOS);
  return v.length ? v : ["salud_general"];
}

/** {"día|turno": consejo} de un objetivo: los de turno fijo en su turno y los demás en los espacios libres, en orden. */
function reparto(consejos: Consejo[]) {
  const libres = [...ESPACIOS], asignado = new Map<string, Consejo>();
  for (const turno of ["tarde", "manana"]) {
    for (const c of consejos.filter((c) => c.turno === turno)) {
      const i = libres.findIndex((e) => e[1] === turno);
      asignado.set(libres[i].join("|"), c);
      libres.splice(i, 1);
    }
  }
  libres.sort((a, b) => a[0] - b[0] || (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0));
  for (const c of consejos.filter((c) => c.turno === "cualquiera")) asignado.set(libres.shift()!.join("|"), c);
  return asignado;
}

function listaObjetivos(objs: string[]) {
  const n = objs.map((o) => objetivoEnTu(C.objetivos[o].nombre));
  if (n.length === 1) return `tu objetivo: ${n[0]}`;
  return "tus objetivos: " + n.slice(0, -1).join(", ") + " y " + n[n.length - 1];
}

function cortisolDelDia(objs: string[], dia: number): string | null {
  const k = C.dias_cortisol.indexOf(dia);
  if (k < 0) return null;
  const lista = [...new Set([...objs.map((o) => C.por_objetivo[o].cortisol as string), ...C.cortisol_general])];
  return lista[k];
}

async function azar(texto: string) {
  const h = new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(texto)));
  return parseInt([...h.slice(0, 4)].map((b) => b.toString(16).padStart(2, "0")).join(""), 16) / 0xffffffff;
}

/** Una receta por día, alternando el momento del día, sin repetir y sin sus alérgenos (nutricion.plan_recetas). */
export async function planRecetas(persona: Persona): Promise<Receta[]> {
  const objs = objetivosPersona(persona.objetivos), ale = new Set(persona.alergias ?? []);
  const aptas: Receta[] = C.recetas.filter((r: Receta) => !r.alergenos.some((a: string) => ale.has(a)));
  const pref = new Set<string>();
  if (objs.some((o) => DEPORTE.includes(o))) pref.add("alta_en_proteina");
  if (objs.includes("bajar_peso")) { pref.add("alta_en_fibra"); pref.add("sin_azucar_anadida"); }
  const puntaje = new Map<string, number>();
  for (const r of aptas) puntaje.set(r.id, -(r.etiquetas.filter((e: string) => pref.has(e)).length + (await azar(`${persona.codigo}${r.id}`))));
  const orden = (a: Receta, b: Receta) => puntaje.get(a.id)! - puntaje.get(b.id)!;
  const plan: Receta[] = [], usadas = new Set<string>();
  for (let d = 0; d < DIAS; d++) {
    const t = TIEMPOS[d % TIEMPOS.length];
    let cand = aptas.filter((r) => r.tiempo_comida === t && !usadas.has(r.id)).sort(orden);
    if (!cand.length) cand = aptas.filter((r) => !usadas.has(r.id)).sort(orden);
    if (!cand.length) break;
    plan.push(cand[0]);
    usadas.add(cand[0].id);
  }
  return plan;
}

/** Envíos del día 1 a 7, en orden (semana_prueba.mensajes). */
export function mensajes(persona: Persona, dia: number, recetas: Receta[]): Mensaje[] {
  const objs = objetivosPersona(persona.objetivos), nombre = primerNombre(persona.nombre), h = C.horarios;
  const r = recetas[dia - 1];
  const g = C.ganchos[familia(objs[0])][dia - 1];
  const pr = C.preguntas_receta[String(dia)];
  const repartos = Object.fromEntries(objs.map((o) => [o, reparto(C.por_objetivo[o].consejos)]));

  const consejos = (turno: string, titulo: string) => {
    const partes = objs.filter((o) => repartos[o].has(`${dia}|${turno}`))
      .map((o) => `${C.por_objetivo[o].emoji} *${C.objetivos[o].nombre}*\n${repartos[o].get(`${dia}|${turno}`)!.texto}`);
    return partes.length ? `*Día ${dia} de ${DIAS}* · ${titulo}\n\n` + partes.join("\n\n") : "";
  };
  const horas = dia === 1
    ? { manana: "al escribir hola", receta: "2 horas después", cortisol: `${h.cortisol} o con la receta`, examen: h.examen, tarde: h.tarde }
    : h;
  const out: Mensaje[] = [];
  if (dia === 1) {
    out.push({ envio: "manana", hora: horas.manana, botones: [], texto: formato(C.bienvenida, {
      nombre, objetivos: listaObjetivos(objs), sin_alergias: fraseAlergias(persona.alergias ?? []) }) });
  }
  let t = consejos("manana", "Tus consejos de la mañana");
  if (t) out.push({ envio: "manana", hora: horas.manana, botones: [], texto: t });
  out.push({ envio: "receta", hora: horas.receta, botones: [], texto: r.texto });
  out.push({ envio: "receta", hora: horas.receta, botones: pr.botones, texto: pr.texto });
  const c = cortisolDelDia(objs, dia);
  if (c) out.push({ envio: "cortisol", hora: horas.cortisol, botones: [], texto: `🌿 *Bájale al estrés*\n\n${c}` });
  if (dia < DIAS) {
    out.push({ envio: "examen", hora: horas.examen, botones: g.botones, texto: `🩸 *Solo tu examen lo dice*\n\n${g.texto}\n\n${g.pregunta}` });
    t = consejos("tarde", "Tus consejos de la tarde");
    if (t) out.push({ envio: "tarde", hora: horas.tarde, botones: [], texto: t });
  } else {
    let cierre = formato(C.cierre, { nombre, valor: "$" + C.anticipo_valor.toLocaleString("en-US").replace(/,/g, ".") });
    if (objs.includes("condicion_existente")) cierre += " " + C.aviso_condicion_existente;
    out.push({ envio: "examen", hora: horas.examen, botones: C.cierre_botones, texto: `🩸 *Solo tu examen lo dice*\n\n${g.texto}\n\n${cierre}` });
  }
  return out;
}

// ── Horas de envío (Bogotá, UTC-5 todo el año) ──────────────────────────────────────────────────────────────────────
const BOGOTA = -5 * 3600_000;
const HORA = 3600_000;
/** Fecha de Bogotá (AAAA-MM-DD) de un instante. */
export const fechaBogota = (t: Date) => new Date(t.getTime() + BOGOTA).toISOString().slice(0, 10);
/** El instante de las "HH:MM" de Bogotá, `dias` días después de la fecha de Bogotá de `base`. */
function aLas(base: Date, hhmm: string, dias = 0) {
  const [y, m, d] = fechaBogota(base).split("-").map(Number), [hh, mm] = hhmm.split(":").map(Number);
  return new Date(Date.UTC(y, m - 1, d + dias, hh, mm) - BOGOTA);
}
const max = (a: Date, b: Date) => (a > b ? a : b);

/**
 * Hora de cada envío. Días 2 a 7: los horarios fijos. Día 1 (empieza al escribir hola), según semana_prueba.yaml > dia_1:
 * antes de las 4 p. m., bienvenida y consejos de una vez, receta 2 horas después, cortisol a la 1 p. m. o con la receta,
 * examen a las 6 p. m. y consejos de la tarde a las 7:30; desde las 4 p. m., consejos y receta de una vez y lo demás
 * 2 horas después, y si eso pasa de las 9 p. m., al otro día a las 7 a. m.
 */
export function horaDeEnvio(inicio: Date, dia: number, envio: string): Date {
  const h = C.horarios;
  if (dia > 1) return aLas(inicio, h[envio], dia - 1);
  const despues = new Date(inicio.getTime() + 2 * HORA);
  if (inicio < aLas(inicio, "16:00")) {
    return ({ manana: inicio, receta: despues, cortisol: max(aLas(inicio, h.cortisol), despues), examen: aLas(inicio, h.examen),
      tarde: aLas(inicio, h.tarde) } as Record<string, Date>)[envio];
  }
  if (envio === "manana" || envio === "receta") return inicio;
  return despues > aLas(inicio, "21:00") ? aLas(inicio, h.manana, 1) : despues;
}

/** Todas las filas de semana_envios de una persona, desde que escribió hola. */
export async function semana(persona: Persona, inicio: Date) {
  const recetas = await planRecetas(persona);
  return Array.from({ length: DIAS }, (_, k) => k + 1).flatMap((dia) =>
    mensajes(persona, dia, recetas).map((m, orden) => ({
      dia, orden, envio: m.envio, texto: m.texto, botones: m.botones,
      programado: horaDeEnvio(inicio, dia, m.envio).toISOString(),
      resumen: formato(C.recordatorio_que[m.envio], { receta: recetas[dia - 1].nombre[0].toLowerCase() + recetas[dia - 1].nombre.slice(1) }),
    }))
  );
}

/** Respuesta del bot al tocar un botón de la semana (o de la plantilla cierre_semana). null: no responde, solo entrega lo pendiente. */
export function respuestaBoton(boton: string, dia: number, nombre: string): { texto: string | null; interes: boolean; cupo: boolean } {
  const n = primerNombre(nombre || "");
  const interes = C.botones_interes.includes(boton);
  if (dia === DIAS && boton in C.respuestas_cierre) {
    return { texto: formato(C.respuestas_cierre[boton], { nombre: n }), interes: boton !== "Ahora no", cupo: boton === "Quiero mi cupo" };
  }
  if (boton === "Quiero saber" && dia === DIAS) return { texto: null, interes: true, cupo: false };
  if (interes) return { texto: C.respuesta_interes, interes, cupo: false };
  return { texto: formato(dia === DIAS ? C.respuesta_boton_dia7 : C.respuesta_boton, { nombre: n }), interes, cupo: false };
}
