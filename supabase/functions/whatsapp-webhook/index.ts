/**
 * Saludly · Webhook de WhatsApp: respuestas automáticas fijas (sin IA) a lo que escribe el paciente (Fase 6).
 *
 * Meta llama aquí con cada mensaje que recibe el número de Saludly.
 * - GET: verificación del webhook (hub.verify_token = WHATSAPP_VERIFY_TOKEN).
 * - POST: guarda el mensaje en whatsapp_mensajes y responde con un texto fijo según lo que escribió:
 *   1 agendar · 2 resultados · 3 hablar con una persona · BAJA dejar de recibir mensajes · cualquier otra cosa, el menú.
 * Las respuestas no dan valores ni interpretan resultados: eso solo lo ve el paciente en la app.
 * Se publica sin verificación de sesión (--no-verify-jwt): Meta no manda token de Supabase. La firma de Meta
 * se revisa con WHATSAPP_APP_SECRET cuando está configurado.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { enviarTexto } from "../_compartido/whatsapp.ts";

const APP = "https://app.saludly.online";
const MENU =
  "Escribe el número de lo que necesitas:\n1️⃣ Agendar o cambiar la visita de la enfermera\n2️⃣ Ver mis resultados\n3️⃣ Hablar con una persona de Saludly\n\nSi no quieres recibir más mensajes, escribe BAJA.";

const RESPUESTAS: Record<string, (nombre: string) => string> = {
  hola: (n) => `¡Hola${n ? `, ${n}` : ""}! 👋 Soy el asistente de Saludly.\n\n${MENU}`,
  otro: (n) => `Recibimos tu mensaje${n ? `, ${n}` : ""} 🙌 Una persona del equipo de Saludly te responde muy pronto.\n\n${MENU}`,
  "1": () =>
    "📅 Las visitas son de lunes a viernes, entre las 7 y las 11 de la mañana, y debes estar en ayunas. Escríbenos el día y la hora que te quedan mejor y te confirmamos hoy mismo.",
  "2": () => `🔎 Tus resultados aparecen en tu app cuando un médico los revisa: ${APP}\nSi todavía no están, te escribimos apenas estén listos.`,
  "3": () => "🙋 Listo, una persona del equipo de Saludly te va a escribir pronto por este chat.",
  baja: () => "Listo, no te enviaremos más mensajes por WhatsApp. Si cambias de opinión, escribe ALTA.",
  alta: (n) => `¡Bienvenido de nuevo${n ? `, ${n}` : ""}! Volverás a recibir los avisos de Saludly por WhatsApp.`,
};

function clave(texto: string) {
  const t = texto.trim().toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  if (/^1\b|agendar|visita|cita/.test(t)) return "1";
  if (/^2\b|resultado/.test(t)) return "2";
  if (/^3\b|persona|asesor|humano/.test(t)) return "3";
  if (/^baja\b|^stop\b|^no mas\b/.test(t)) return "baja";
  if (/^alta\b/.test(t)) return "alta";
  if (!t || /^(hola|buenas|buenos|buen dia|hi|hello|menu|inicio|ayuda)\b/.test(t)) return "hola";
  return "otro"; // una pregunta libre: la responde una persona (queda en whatsapp_mensajes)
}

/** Baja el archivo de Meta (dos pasos: la URL y luego el contenido) y lo sube al bucket privado "comprobantes". */
// deno-lint-ignore no-explicit-any
async function guardarComprobante(admin: any, pacienteId: string, mediaId: string) {
  const token = Deno.env.get("WHATSAPP_TOKEN");
  const info = await (await fetch(`https://graph.facebook.com/v25.0/${mediaId}`, { headers: { Authorization: `Bearer ${token}` } })).json();
  const contenido = await (await fetch(info.url, { headers: { Authorization: `Bearer ${token}` } })).arrayBuffer();
  const tipo: string = info.mime_type ?? "image/jpeg";
  const ext = tipo.includes("pdf") ? "pdf" : tipo.includes("png") ? "png" : "jpg";
  const ruta = `${pacienteId}/${Date.now()}.${ext}`;
  const { error } = await admin.storage.from("comprobantes").upload(ruta, contenido, { contentType: tipo });
  if (error) console.error("no se guardó el comprobante", error.message);
  return ruta;
}

async function firmaValida(req: Request, cuerpo: string) {
  const secreto = Deno.env.get("WHATSAPP_APP_SECRET");
  if (!secreto) return true;
  const firma = req.headers.get("x-hub-signature-256")?.replace("sha256=", "") ?? "";
  const llave = await crypto.subtle.importKey("raw", new TextEncoder().encode(secreto), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const mac = new Uint8Array(await crypto.subtle.sign("HMAC", llave, new TextEncoder().encode(cuerpo)));
  return [...mac].map((b) => b.toString(16).padStart(2, "0")).join("") === firma;
}

Deno.serve(async (req) => {
  const url = new URL(req.url);
  if (req.method === "GET") {
    const ok = url.searchParams.get("hub.mode") === "subscribe" && url.searchParams.get("hub.verify_token") === Deno.env.get("WHATSAPP_VERIFY_TOKEN");
    return ok ? new Response(url.searchParams.get("hub.challenge") ?? "") : new Response("prohibido", { status: 403 });
  }
  const cuerpo = await req.text();
  if (!(await firmaValida(req, cuerpo))) return new Response("firma inválida", { status: 401 });

  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const datos = JSON.parse(cuerpo || "{}");
  for (const entrada of datos.entry ?? []) {
    for (const cambio of entrada.changes ?? []) {
      for (const m of cambio.value?.messages ?? []) {
        const de: string = m.from;
        const texto: string = m.text?.body ?? m.button?.text ?? m.interactive?.button_reply?.title ?? "";
        const { data: p } = await admin.from("pacientes").select("id, nombre").eq("celular_whatsapp", de).order("creado", { ascending: false }).limit(1).maybeSingle();
        const nombre = p?.nombre?.trim().split(/\s+/)[0] ?? "";

        // Una imagen o un PDF es el comprobante de pago: se guarda en privado y Carlos lo confirma en el panel.
        const archivo = m.image ?? m.document;
        if (archivo?.id) {
          await admin.from("whatsapp_mensajes").insert({ paciente_id: p?.id ?? null, celular: de, texto: m.image ? "[imagen]" : "[documento]", opcion: "comprobante" });
          if (!p) {
            await enviarTexto(de, `Recibimos tu archivo. Para que podamos asociarlo a tu pago, primero crea tu cuenta en ${APP} con este mismo número de WhatsApp.`);
            continue;
          }
          const ruta = await guardarComprobante(admin, p.id, archivo.id);
          const { data: pago } = await admin.from("pagos").select("estado").eq("paciente_id", p.id).maybeSingle();
          if (pago?.estado === "confirmado") {
            await enviarTexto(de, `Tu pago ya estaba confirmado${nombre ? `, ${nombre}` : ""} ✅ Guardamos este archivo por si acaso.`);
            continue;
          }
          await admin.from("pagos").upsert({ paciente_id: p.id, estado: "comprobante", comprobante: ruta, comprobante_recibido: new Date().toISOString() });
          await enviarTexto(de, `¡Recibimos tu comprobante${nombre ? `, ${nombre}` : ""}! ✅ Lo revisamos hoy y te avisamos por aquí. Mientras tanto, puedes responder tus preguntas de salud en ${APP}`);
          continue;
        }

        const k = clave(texto);
        await admin.from("whatsapp_mensajes").insert({ paciente_id: p?.id ?? null, celular: de, texto: texto.slice(0, 1000), opcion: k });
        if (p && (k === "baja" || k === "alta")) {
          await admin.from("pacientes").update({ whatsapp_baja: k === "baja" ? new Date().toISOString() : null }).eq("id", p.id);
        }
        await enviarTexto(de, RESPUESTAS[k]!(nombre));
      }
    }
  }
  return new Response("ok");
});
