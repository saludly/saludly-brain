/**
 * Saludly · Vista para el médico del paciente (Fase 6): GET ?e=<slug> → resumen clínico del informe aprobado.
 *
 * La abre la página app.saludly.online/m/<slug>, sin cuenta: el enlace es la llave (tiene un código aleatorio).
 * Devuelve solo lo clínico: datos del paciente (nombre, edad, sexo, celular, últimos 4 del documento), medidas,
 * todos los resultados, hallazgos y condiciones con sus guías, lo que hay que vigilar, y lo que el paciente
 * respondió sobre alergias, medicamentos y hábitos. Nada de textos internos de Saludly ni frases para el paciente.
 * Se publica con --no-verify-jwt.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, responder } from "../_compartido/whatsapp.ts";

// deno-lint-ignore no-explicit-any
type J = any;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const slug = new URL(req.url).searchParams.get("e") ?? "";
  if (!/^[a-z0-9-]{8,80}$/.test(slug)) return responder(404, { error: "enlace no válido" });

  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: e } = await admin.from("enlaces_medico").select("paciente_id, informe_id, revocado").eq("slug", slug).maybeSingle();
  if (!e || e.revocado) return responder(404, { error: "enlace no válido" });

  const [i, p, c] = await Promise.all([
    admin.from("informes").select("informe, estado, aprobado, orden").eq("id", e.informe_id).maybeSingle(),
    admin.from("pacientes").select("nombre, edad, sexo, celular_whatsapp, tipo_documento, cedula").eq("id", e.paciente_id).maybeSingle(),
    admin.from("cuestionarios").select("alergias, alergias_otras, dieta, medicamentos, medicamentos_otros, fuma, alcohol, antecedentes, embarazo, toma_biotina, nivel_actividad").eq("paciente_id", e.paciente_id).maybeSingle(),
  ]);
  if (!i.data || i.data.estado !== "aprobado" || !p.data) return responder(404, { error: "enlace no válido" });

  const inf: J = i.data.informe;
  const m: J = inf.medico ?? {};
  const med: J = inf.perfil?.medidas_enfermera ?? {};
  const imc = med.peso_kg && med.talla_m ? Math.round((med.peso_kg / (med.talla_m * med.talla_m)) * 10) / 10 : null;
  const activas = Object.values(m.condiciones ?? {}).filter((x: J) => x.estado === "activa");
  const extra = (x: J) =>
    Object.fromEntries(Object.entries(x).filter(([k, v]) => typeof v === "number" && !["escalamiento"].includes(k)));

  return responder(200, {
    paciente: {
      nombre: p.data.nombre,
      edad: inf.perfil?.edad ?? p.data.edad,
      sexo: inf.perfil?.sexo ?? p.data.sexo,
      celular: `+${p.data.celular_whatsapp}`,
      documento: `${p.data.tipo_documento} ···${p.data.cedula.slice(-4)}`,
    },
    informe: { orden: i.data.orden, fecha_toma: inf.fecha_toma, aprobado: i.data.aprobado, ciudad: inf.perfil?.ciudad },
    medidas: { ...med, imc },
    edad_biologica: inf.edad_biologica ?? null,
    hallazgos: (m.hallazgos ?? []).map((h: J) => ({ nombre: h.nombre, tipo: h.tipo, coincidencia: h.coincidencia, escalamiento: h.escalamiento, fuente: h.fuerza ?? null })),
    condiciones: activas.map((x: J) => ({
      nombre: x.nombre,
      coincidencia: x.coincidencia,
      escalamiento: x.escalamiento,
      criterios: x.criterios_cumplidos ?? [],
      guias: x.guias ?? [],
      severidad: x.severidad ?? null,
      nota: x.nota ?? null,
      datos: extra(x),
    })),
    vigilar: (m.vigilar ?? []).map((v: J) => ({ nombre: v.nombre, nota: v.nota })),
    reflejas_pendientes: m.reflejas_pendientes ?? [],
    datos_faltantes: m.datos_faltantes ?? [],
    paciente_reporta: c.data ?? null,
    calculados: inf.trazabilidad?.calculados ?? {},
    resultados: (inf.resultados ?? []).map((r: J) => ({
      nombre: r.nombre,
      valor: r.valor_original ?? r.valor,
      unidad: r.unidad,
      intervalo: r.intervalo,
      clase: r.clase,
      estado: r.estado,
      seccion: r.seccion,
    })),
  });
});
