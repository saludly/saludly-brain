/**
 * Saludly · Aviso por WhatsApp de que los resultados están listos (Fase 6).
 * La llama la vista del médico al aprobar un informe. Solo el equipo puede llamarla. Envía la plantilla
 * resultados_listos si el paciente aceptó WhatsApp y no pidió BAJA, y marca informes.avisado. Nunca envía valores.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, enviarPlantilla, responder } from "../_compartido/whatsapp.ts";

const PLANTILLA = Deno.env.get("WHATSAPP_PLANTILLA_RESULTADOS") ?? "resultados_listos";

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: u } = await admin.auth.getUser((req.headers.get("Authorization") ?? "").replace("Bearer ", ""));
  const correo = u.user?.email?.toLowerCase();
  if (!correo || !(await admin.from("equipo").select("correo").eq("correo", correo).maybeSingle()).data) return responder(403, { error: "solo el equipo" });

  const { informe_id } = await req.json().catch(() => ({}));
  const { data: inf } = await admin.from("informes").select("id, paciente_id, estado, avisado").eq("id", informe_id).maybeSingle();
  if (!inf || inf.estado !== "aprobado") return responder(409, { error: "el informe no está aprobado" });
  if (inf.avisado) return responder(200, { estado: "ya_avisado" });

  const [p, a] = await Promise.all([
    admin.from("pacientes").select("nombre, celular_whatsapp, whatsapp_baja").eq("id", inf.paciente_id).maybeSingle(),
    admin.from("autorizaciones").select("id").eq("paciente_id", inf.paciente_id).eq("acepta_whatsapp", true).limit(1),
  ]);
  if (!p.data || !a.data?.length || p.data.whatsapp_baja) return responder(200, { estado: "no_acepta_whatsapp" });

  const ok = await enviarPlantilla(p.data.celular_whatsapp, PLANTILLA, p.data.nombre.trim().split(/\s+/)[0]);
  if (!ok) return responder(502, { error: "no se pudo enviar el WhatsApp" });
  await admin.from("informes").update({ avisado: new Date().toISOString() }).eq("id", inf.id);
  return responder(200, { estado: "enviado" });
});
