/**
 * Saludly · Programador de la semana de prueba (preventa). Lo llama pg_cron cada 5 minutos
 * (migración 20261025000000_semana_prueba_envios.sql) con la llave SEMANA_CRON_SECRET en el encabezado x-semana-cron.
 * 1. Manda a cada persona lo que ya le toca de su semana (_compartido/semana_envios.ts > entregar).
 * 2. Un día después del pre-registro, si todavía no escribió hola, le manda la plantilla bienvenida_semana
 *    (una sola vez, entre las 9 a. m. y las 7 p. m. de Bogotá).
 * Se publica sin verificación de sesión (--no-verify-jwt): la protege la llave propia.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { fechaBogota, primerNombre } from "../_compartido/semana.ts";
import { CAMPOS, entregar, type Pre } from "../_compartido/semana_envios.ts";
import { enviarPlantilla, responder } from "../_compartido/whatsapp.ts";

Deno.serve(async (req) => {
  const llave = Deno.env.get("SEMANA_CRON_SECRET");
  if (!llave || req.headers.get("x-semana-cron") !== llave) return responder(401, { error: "sin llave" });
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const ahora = new Date();

  // 1. Envíos que ya tocan
  const { data: toca } = await admin.from("semana_envios").select("preregistro_id").eq("estado", "pendiente").lte("programado", ahora.toISOString());
  const ids = [...new Set((toca ?? []).map((f) => f.preregistro_id as string))];
  let enviados = 0;
  if (ids.length) {
    const { data: personas } = await admin.from("preregistros").select(CAMPOS).in("id", ids);
    for (const p of (personas ?? []) as Pre[]) {
      if (p.estado !== "registrado") {
        await admin.from("semana_envios").update({ estado: "cancelado" }).eq("preregistro_id", p.id).in("estado", ["pendiente", "esperando"]);
        continue;
      }
      enviados += await entregar(admin, p, ahora);
    }
  }

  // 2. Bienvenida a quien se pre-registró ayer o antes y no ha escrito (máximo 14 días después)
  let bienvenidas = 0;
  const horaBogota = (ahora.getUTCHours() + 19) % 24;
  if (horaBogota >= 9 && horaBogota < 19) {
    const hoyBogota = new Date(ahora.getTime() - 5 * 3600_000);
    hoyBogota.setUTCHours(5, 0, 0, 0); // las 00:00 de hoy en Bogotá
    const { data: nuevas } = await admin.from("preregistros").select(CAMPOS)
      .eq("estado", "registrado").eq("quiere_prueba", true).is("prueba_inicio", null).is("bienvenida_enviada", null)
      .lt("creado", hoyBogota.toISOString()).gt("creado", new Date(ahora.getTime() - 14 * 86400_000).toISOString()).limit(50);
    for (const p of (nuevas ?? []) as Pre[]) {
      const ok = await enviarPlantilla(p.celular_whatsapp, "bienvenida_semana", [primerNombre(p.nombre)]);
      if (!ok) continue;
      await admin.from("preregistros").update({ bienvenida_enviada: ahora.toISOString(), ultima_plantilla: fechaBogota(ahora) }).eq("id", p.id);
      bienvenidas++;
    }
  }
  return responder(200, { enviados, personas: ids.length, bienvenidas });
});
