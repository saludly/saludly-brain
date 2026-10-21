/**
 * Saludly · Aviso por WhatsApp de que los resultados están listos (Fase 6).
 * La llama la vista del médico al aprobar un informe. Solo el equipo puede llamarla. Envía la plantilla
 * resultados_listos si el paciente aceptó WhatsApp y no pidió BAJA, y marca informes.avisado. Nunca envía valores.
 * También crea el enlace para su médico (enlaces_medico) y lo envía con la plantilla enlace_medico.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CORS, enviarPlantilla, responder } from "../_compartido/whatsapp.ts";

const PLANTILLA = Deno.env.get("WHATSAPP_PLANTILLA_RESULTADOS") ?? "resultados_listos";
const APP = "https://app.saludly.online";

/** nombre-apellido-1234-k3f9q: legible para el paciente, imposible de adivinar por el código final. */
function nuevoSlug(nombre: string, cedula: string) {
  const base = nombre.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase().replace(/[^a-z ]/g, "").trim().split(/\s+/).slice(0, 2).join("-") || "paciente";
  const letras = "abcdefghjkmnpqrstuvwxyz23456789";
  const codigo = Array.from(crypto.getRandomValues(new Uint8Array(5)), (b) => letras[b % letras.length]).join("");
  return `${base}-${cedula.slice(-4)}-${codigo}`;
}

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
    admin.from("pacientes").select("nombre, cedula, celular_whatsapp, whatsapp_baja").eq("id", inf.paciente_id).maybeSingle(),
    admin.from("autorizaciones").select("id").eq("paciente_id", inf.paciente_id).eq("acepta_whatsapp", true).limit(1),
  ]);
  // El enlace para el médico se crea aunque el paciente no reciba WhatsApp: también lo ve en su app.
  let { data: enlace } = await admin.from("enlaces_medico").select("slug").eq("informe_id", inf.id).is("revocado", null).maybeSingle();
  if (!enlace && p.data) {
    const slug = nuevoSlug(p.data.nombre, p.data.cedula);
    await admin.from("enlaces_medico").insert({ slug, paciente_id: inf.paciente_id, informe_id: inf.id });
    enlace = { slug };
  }
  if (!p.data || !a.data?.length || p.data.whatsapp_baja) return responder(200, { estado: "no_acepta_whatsapp" });

  const nombre = p.data.nombre.trim().split(/\s+/)[0];
  const ok = await enviarPlantilla(p.data.celular_whatsapp, PLANTILLA, [nombre]);
  if (!ok) return responder(502, { error: "no se pudo enviar el WhatsApp" });
  await admin.from("informes").update({ avisado: new Date().toISOString() }).eq("id", inf.id);
  if (enlace) await enviarPlantilla(p.data.celular_whatsapp, "enlace_medico", [nombre, `${APP}/m/${enlace.slug}`]);
  return responder(200, { estado: "enviado" });
});
