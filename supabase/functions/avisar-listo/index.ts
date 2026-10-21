/**
 * Saludly · Aviso por WhatsApp cuando el paciente termina el cuestionario (Fase 6).
 *
 * La app la llama al llegar a "¡Listo!". Con la sesión del paciente revisa que el cuestionario esté completo,
 * que haya aceptado WhatsApp en su autorización y que no se le haya avisado antes; entonces envía la plantilla
 * aprobada por Meta (la empresa solo puede escribir primero con plantilla) y marca cuestionarios.aviso_listo.
 * El token de WhatsApp vive en los secretos de la función (WHATSAPP_TOKEN, WHATSAPP_PHONE_NUMBER_ID); nunca en el navegador.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, enviarPlantilla, responder } from "../_compartido/whatsapp.ts";

const PLANTILLA = Deno.env.get("WHATSAPP_PLANTILLA_LISTO") ?? "visita_agendar";

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });

  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: u } = await admin.auth.getUser((req.headers.get("Authorization") ?? "").replace("Bearer ", ""));
  if (!u.user) return responder(401, { error: "sin sesión" });
  const yo = u.user.id;

  const [p, a, c] = await Promise.all([
    admin.from("pacientes").select("nombre, celular_whatsapp, whatsapp_baja").eq("id", yo).maybeSingle(),
    admin.from("autorizaciones").select("id").eq("paciente_id", yo).eq("acepta_whatsapp", true).limit(1),
    admin.from("cuestionarios").select("completo, aviso_listo").eq("paciente_id", yo).maybeSingle(),
  ]);
  if (!p.data || !c.data?.completo) return responder(409, { error: "falta el registro o el cuestionario" });
  if (c.data.aviso_listo) return responder(200, { estado: "ya_avisado" });
  if (!a.data?.length || p.data.whatsapp_baja) return responder(200, { estado: "no_acepta_whatsapp" });

  const ok = await enviarPlantilla(p.data.celular_whatsapp, PLANTILLA, p.data.nombre.trim().split(/\s+/)[0]);
  if (!ok) return responder(502, { error: "no se pudo enviar el WhatsApp" });
  await admin.from("cuestionarios").update({ aviso_listo: new Date().toISOString() }).eq("paciente_id", yo);
  return responder(200, { estado: "enviado" });
});
