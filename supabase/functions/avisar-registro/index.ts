/**
 * Saludly · WhatsApp de registro completo (Fase 6): la app la llama al abrir la pantalla de pago por primera vez.
 * Con la sesión del paciente, envía una sola vez la plantilla registro_completo (los datos del pago están en la app)
 * si aceptó WhatsApp y no pidió BAJA, y marca pagos.aviso_registro.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, enviarPlantilla, responder } from "../_compartido/whatsapp.ts";

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: u } = await admin.auth.getUser((req.headers.get("Authorization") ?? "").replace("Bearer ", ""));
  if (!u.user) return responder(401, { error: "sin sesión" });
  const yo = u.user.id;

  const [p, a, g] = await Promise.all([
    admin.from("pacientes").select("nombre, celular_whatsapp, whatsapp_baja").eq("id", yo).maybeSingle(),
    admin.from("autorizaciones").select("id").eq("paciente_id", yo).eq("acepta_whatsapp", true).limit(1),
    admin.from("pagos").select("aviso_registro").eq("paciente_id", yo).maybeSingle(),
  ]);
  if (!p.data || !g.data) return responder(409, { error: "falta el registro o el pago" });
  if (g.data.aviso_registro) return responder(200, { estado: "ya_avisado" });
  if (!a.data?.length || p.data.whatsapp_baja) return responder(200, { estado: "no_acepta_whatsapp" });

  const ok = await enviarPlantilla(p.data.celular_whatsapp, "registro_completo", [p.data.nombre.trim().split(/\s+/)[0]]);
  if (!ok) return responder(502, { error: "no se pudo enviar el WhatsApp" });
  await admin.from("pagos").update({ aviso_registro: new Date().toISOString() }).eq("paciente_id", yo);
  return responder(200, { estado: "enviado" });
});
