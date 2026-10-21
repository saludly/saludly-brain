/**
 * Saludly · Agenda de la visita de la enfermera desde la PWA (Fase 6). Con la sesión del paciente.
 *
 * GET  → { cita } si ya tiene una; si no, los días libres: lunes a viernes, desde 2 días después de hoy,
 *        las próximas 2 semanas hábiles, una visita por día, a las 7, 8, 9 o 10 a. m. (hora de Bogotá).
 *        Un día se ocupa si ya hay una cita de Saludly o si el Google Calendar de saludlyco tiene algo entre 7 y 11.
 * POST {fecha, hora} → crea el evento en el calendario de saludlyco con el paciente invitado (Google le manda la
 *        invitación y queda en los dos calendarios), guarda la cita y envía la plantilla cita_agendada por WhatsApp.
 * Solo con el pago confirmado.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, enviarPlantilla, responder } from "../_compartido/whatsapp.ts";
import { CALENDARIO, ZONA, calendar, tokenCalendario } from "../_compartido/calendario.ts";

const HORAS = ["07:00", "08:00", "09:00", "10:00"];
const DIAS_HABILES = 10;

/** Fecha AAAA-MM-DD en Bogotá (UTC-5, sin horario de verano). */
const hoyBogota = () => new Date(Date.now() - 5 * 3600e3).toISOString().slice(0, 10);
const masDias = (f: string, n: number) => new Date(Date.parse(`${f}T12:00:00Z`) + n * 864e5).toISOString().slice(0, 10);
const diaSemana = (f: string) => new Date(`${f}T12:00:00Z`).getUTCDay();

function candidatos() {
  const dias: string[] = [];
  let f = masDias(hoyBogota(), 2);
  while (dias.length < DIAS_HABILES) {
    if (diaSemana(f) >= 1 && diaSemana(f) <= 5) dias.push(f);
    f = masDias(f, 1);
  }
  return dias;
}

const FECHA_LARGA = (f: string, h: string) =>
  `${new Date(`${f}T12:00:00Z`).toLocaleDateString("es-CO", { weekday: "long", day: "numeric", month: "long", timeZone: "UTC" })} a las ${Number(h.slice(0, 2))}:00 a. m.`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: u } = await admin.auth.getUser((req.headers.get("Authorization") ?? "").replace("Bearer ", ""));
  if (!u.user) return responder(401, { error: "sin sesión" });
  const yo = u.user.id;

  const [{ data: cita }, { data: pago }] = await Promise.all([
    admin.from("citas").select("inicio, dia").eq("paciente_id", yo).eq("estado", "agendada").maybeSingle(),
    admin.from("pagos").select("estado").eq("paciente_id", yo).maybeSingle(),
  ]);
  if (cita) return responder(200, { cita });
  if (pago?.estado !== "confirmado") return responder(409, { error: "El pago todavía no está confirmado." });

  // Días ocupados: citas de Saludly + cualquier cosa en el calendario de saludlyco entre 7 y 11 a. m.
  const dias = candidatos();
  let token: string;
  try {
    token = await tokenCalendario(admin);
  } catch (e) {
    console.error(String(e));
    return responder(503, { error: "La agenda no está disponible en este momento. Te escribimos por WhatsApp." });
  }
  const { data: tomadas } = await admin.from("citas").select("dia").eq("estado", "agendada").in("dia", dias);
  const ocupados = new Set((tomadas ?? []).map((x) => x.dia as string));
  const fb = await calendar(token, "freeBusy", "POST", {
    timeMin: `${dias[0]}T07:00:00-05:00`,
    timeMax: `${dias[dias.length - 1]}T11:00:00-05:00`,
    timeZone: ZONA,
    items: [{ id: "primary" }],
  });
  for (const b of fb.calendars?.primary?.busy ?? []) {
    for (const d of dias) {
      const ini = Date.parse(`${d}T07:00:00-05:00`), fin = Date.parse(`${d}T11:00:00-05:00`);
      if (Date.parse(b.start) < fin && Date.parse(b.end) > ini) ocupados.add(d);
    }
  }
  const libres = dias.filter((d) => !ocupados.has(d));

  if (req.method === "GET") return responder(200, { dias: libres.map((fecha) => ({ fecha, horas: HORAS })) });

  const { fecha, hora } = await req.json().catch(() => ({}));
  if (!libres.includes(fecha) || !HORAS.includes(hora)) return responder(409, { error: "Ese horario ya no está disponible. Elige otro." });

  const { data: p } = await admin.from("pacientes").select("nombre, direccion, celular_whatsapp, whatsapp_baja").eq("id", yo).single();
  const inicio = `${fecha}T${hora}:00-05:00`;
  const fin = new Date(Date.parse(inicio) + 3600e3).toISOString();

  // Primero la cita (el índice único evita dos visitas el mismo día); después el evento.
  const { data: nueva, error } = await admin.from("citas").insert({ paciente_id: yo, inicio, dia: fecha }).select("id").single();
  if (error) return responder(409, { error: "Ese día se acaba de ocupar. Elige otro." });
  try {
    const ev = await calendar(token, "calendars/primary/events?sendUpdates=all", "POST", {
      summary: `Visita Saludly · ${p.nombre}`,
      location: p.direccion,
      description: `Toma de muestra de sangre (en ayunas) y medidas con la enfermera de Saludly.\nPaciente: ${p.nombre}\nWhatsApp: +${p.celular_whatsapp}\nDirección: ${p.direccion}`,
      start: { dateTime: inicio, timeZone: ZONA },
      end: { dateTime: fin, timeZone: ZONA },
      attendees: u.user.email ? [{ email: u.user.email, displayName: p.nombre }] : [],
      reminders: { useDefault: false, overrides: [{ method: "popup", minutes: 12 * 60 }, { method: "popup", minutes: 60 }] },
    });
    await admin.from("citas").update({ evento_id: ev.id }).eq("id", nueva.id);
  } catch (e) {
    await admin.from("citas").delete().eq("id", nueva.id);
    console.error(String(e));
    return responder(502, { error: "No pudimos crear la cita en el calendario. Intenta de nuevo." });
  }

  const { data: a } = await admin.from("autorizaciones").select("id").eq("paciente_id", yo).eq("acepta_whatsapp", true).limit(1);
  if (a?.length && !p.whatsapp_baja) await enviarPlantilla(p.celular_whatsapp, "cita_agendada", [p.nombre.trim().split(/\s+/)[0], FECHA_LARGA(fecha, hora)]);
  return responder(200, { cita: { inicio, dia: fecha }, calendario: CALENDARIO });
});
