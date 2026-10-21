/**
 * Saludly · Conectar el Google Calendar de saludlyco@gmail.com (se hace una sola vez).
 *
 * GET sin parámetros → lleva a Google para autorizar (ver y crear eventos, y consultar disponibilidad).
 * GET ?code=… → Google vuelve aquí; se cambia el código por un refresh token y se guarda en la tabla secretos,
 * solo si la cuenta que autorizó es la de Saludly (si autoriza otra cuenta, se rechaza).
 * Se publica con --no-verify-jwt: Google no manda sesión de Supabase.
 */
import { createClient } from "npm:@supabase/supabase-js@2";
import { CALENDARIO } from "../_compartido/calendario.ts";

const AQUI = `${Deno.env.get("SUPABASE_URL")}/functions/v1/google-calendar`;
const ALCANCES = ["openid", "email", "https://www.googleapis.com/auth/calendar.events", "https://www.googleapis.com/auth/calendar.freebusy"];

const pagina = (titulo: string, texto: string, estado = 200) =>
  new Response(
    `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Saludly</title>` +
      `<body style="font-family:system-ui;max-width:520px;margin:15vh auto;padding:0 24px;color:#1d2433">` +
      `<h1 style="font-weight:300">${titulo}</h1><p style="color:#555;line-height:1.5">${texto}</p></body>`,
    { status: estado, headers: { "Content-Type": "text/html; charset=utf-8" } },
  );

Deno.serve(async (req) => {
  const url = new URL(req.url);
  const code = url.searchParams.get("code");
  if (!code) {
    const destino = new URL("https://accounts.google.com/o/oauth2/v2/auth");
    destino.search = new URLSearchParams({
      client_id: Deno.env.get("GOOGLE_CLIENT_ID")!,
      redirect_uri: AQUI,
      response_type: "code",
      scope: ALCANCES.join(" "),
      access_type: "offline",
      prompt: "consent",
      login_hint: CALENDARIO,
    }).toString();
    return Response.redirect(destino.toString(), 302);
  }

  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      code,
      client_id: Deno.env.get("GOOGLE_CLIENT_ID")!,
      client_secret: Deno.env.get("GOOGLE_CLIENT_SECRET")!,
      redirect_uri: AQUI,
      grant_type: "authorization_code",
    }),
  });
  const j = await r.json();
  if (!j.refresh_token || !j.id_token) return pagina("No se pudo conectar", "Google no entregó el permiso. Vuelve a intentarlo desde el enlace.", 400);

  // El correo de la cuenta que autorizó viene en el id_token (firmado por Google y recibido directo de Google).
  const correo = JSON.parse(atob(j.id_token.split(".")[1].replace(/-/g, "+").replace(/_/g, "/"))).email?.toLowerCase();
  if (correo !== CALENDARIO) return pagina("Cuenta equivocada", `Autorizaste con ${correo}. Hay que hacerlo con ${CALENDARIO}.`, 403);

  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  await admin.from("secretos").upsert({ clave: "google_calendar_refresh", valor: j.refresh_token, actualizado: new Date().toISOString() });
  return pagina("¡Calendario conectado! ✅", `Las visitas que agenden los pacientes aparecerán en el Google Calendar de ${CALENDARIO}. Ya puedes cerrar esta pestaña.`);
});
