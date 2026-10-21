/**
 * Google Calendar de saludlyco@gmail.com: la cuenta lo autorizó una vez (función google-calendar) y su refresh token
 * vive en la tabla secretos. Aquí se cambia por un token de acceso de una hora para cada llamada.
 */
// deno-lint-ignore no-explicit-any
type Admin = any;

export const CALENDARIO = Deno.env.get("SALUDLY_CALENDARIO") ?? "saludlyco@gmail.com";
export const ZONA = "America/Bogota";

export async function tokenCalendario(admin: Admin) {
  const { data } = await admin.from("secretos").select("valor").eq("clave", "google_calendar_refresh").maybeSingle();
  if (!data) throw new Error("El calendario de Saludly no está conectado");
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: Deno.env.get("GOOGLE_CLIENT_ID")!,
      client_secret: Deno.env.get("GOOGLE_CLIENT_SECRET")!,
      refresh_token: data.valor,
      grant_type: "refresh_token",
    }),
  });
  const j = await r.json();
  if (!j.access_token) throw new Error(`Google no entregó el token: ${j.error ?? r.status}`);
  return j.access_token as string;
}

/** Llamada a la API de Calendar con el token de saludlyco. */
export async function calendar(token: string, ruta: string, metodo = "GET", cuerpo?: unknown) {
  const r = await fetch(`https://www.googleapis.com/calendar/v3/${ruta}`, {
    method: metodo,
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
    body: cuerpo ? JSON.stringify(cuerpo) : undefined,
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(`Calendar respondió ${r.status}: ${JSON.stringify(j).slice(0, 300)}`);
  return j;
}
