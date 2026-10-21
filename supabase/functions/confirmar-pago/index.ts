/**
 * Saludly · Confirmar o rechazar un pago desde el panel (Fase 6). Solo el equipo.
 * POST {paciente_id, confirmar: true|false, nota?}. Al confirmar, envía la plantilla pago_confirmado con el link de la app;
 * al rechazar, el paciente vuelve a ver la pantalla de pago con la nota.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, enviarPlantilla, responder } from "../_compartido/whatsapp.ts";

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: u } = await admin.auth.getUser((req.headers.get("Authorization") ?? "").replace("Bearer ", ""));
  const correo = u.user?.email?.toLowerCase();
  if (!correo || !(await admin.from("equipo").select("correo").eq("correo", correo).maybeSingle()).data) return responder(403, { error: "solo el equipo" });

  const { paciente_id, confirmar, nota } = await req.json().catch(() => ({}));
  const cambio = confirmar
    ? { estado: "confirmado", confirmado: new Date().toISOString(), confirmado_por: correo, nota: null }
    : { estado: "rechazado", nota: (nota ?? "").slice(0, 300) || null };
  const { data: pago } = await admin.from("pagos").update(cambio).eq("paciente_id", paciente_id).select("estado").maybeSingle();
  if (!pago) return responder(404, { error: "no hay pago para ese paciente" });
  if (!confirmar) return responder(200, { estado: "rechazado" });

  const [p, a] = await Promise.all([
    admin.from("pacientes").select("nombre, celular_whatsapp, whatsapp_baja").eq("id", paciente_id).maybeSingle(),
    admin.from("autorizaciones").select("id").eq("paciente_id", paciente_id).eq("acepta_whatsapp", true).limit(1),
  ]);
  if (!p.data || !a.data?.length || p.data.whatsapp_baja) return responder(200, { estado: "confirmado", whatsapp: "no_acepta" });
  const ok = await enviarPlantilla(p.data.celular_whatsapp, "pago_confirmado", [p.data.nombre.trim().split(/\s+/)[0]]);
  return responder(200, { estado: "confirmado", whatsapp: ok ? "enviado" : "fallo" });
});
