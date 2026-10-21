/**
 * Saludly · Aviso por WhatsApp cuando el paciente termina el cuestionario (Fase 6).
 *
 * La app la llama al llegar a "¡Listo!". Con la sesión del paciente revisa que el cuestionario esté completo,
 * que haya aceptado WhatsApp en su autorización y que no se le haya avisado antes; entonces envía la plantilla
 * aprobada por Meta (la empresa solo puede escribir primero con plantilla) y marca cuestionarios.aviso_listo.
 * El token de WhatsApp vive en los secretos de la función (WHATSAPP_TOKEN, WHATSAPP_PHONE_NUMBER_ID); nunca en el navegador.
 */
import { createClient } from "npm:@supabase/supabase-js@2";

const PLANTILLA = Deno.env.get("WHATSAPP_PLANTILLA_LISTO") ?? "visita_agendar";
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

const responder = (estado: number, cuerpo: Record<string, unknown>) =>
  new Response(JSON.stringify(cuerpo), { status: estado, headers: { ...CORS, "Content-Type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });

  const url = Deno.env.get("SUPABASE_URL")!;
  const admin = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const jwt = (req.headers.get("Authorization") ?? "").replace("Bearer ", "");
  const { data: u } = await admin.auth.getUser(jwt);
  if (!u.user) return responder(401, { error: "sin sesión" });
  const yo = u.user.id;

  const [p, a, c] = await Promise.all([
    admin.from("pacientes").select("nombre, celular_whatsapp").eq("id", yo).maybeSingle(),
    admin.from("autorizaciones").select("id").eq("paciente_id", yo).eq("acepta_whatsapp", true).limit(1),
    admin.from("cuestionarios").select("completo, aviso_listo").eq("paciente_id", yo).maybeSingle(),
  ]);
  if (!p.data || !c.data?.completo) return responder(409, { error: "falta el registro o el cuestionario" });
  if (c.data.aviso_listo) return responder(200, { estado: "ya_avisado" });
  if (!a.data?.length) return responder(200, { estado: "no_acepta_whatsapp" });

  const nombre = p.data.nombre.trim().split(/\s+/)[0];
  const r = await fetch(`https://graph.facebook.com/v25.0/${Deno.env.get("WHATSAPP_PHONE_NUMBER_ID")}/messages`, {
    method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("WHATSAPP_TOKEN")}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      messaging_product: "whatsapp",
      to: p.data.celular_whatsapp,
      type: "template",
      template: { name: PLANTILLA, language: { code: "es" }, components: [{ type: "body", parameters: [{ type: "text", text: nombre }] }] },
    }),
  });
  if (!r.ok) {
    console.error("Meta respondió", r.status, (await r.text()).slice(0, 400));
    return responder(502, { error: "no se pudo enviar el WhatsApp" });
  }
  await admin.from("cuestionarios").update({ aviso_listo: new Date().toISOString() }).eq("paciente_id", yo);
  return responder(200, { estado: "enviado" });
});
