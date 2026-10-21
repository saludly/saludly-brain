/** Envío por la API de WhatsApp (Meta). El token vive en los secretos de las funciones; nunca en el navegador. */
const API = () => `https://graph.facebook.com/v25.0/${Deno.env.get("WHATSAPP_PHONE_NUMBER_ID")}/messages`;

async function enviar(cuerpo: Record<string, unknown>) {
  const r = await fetch(API(), {
    method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("WHATSAPP_TOKEN")}`, "Content-Type": "application/json" },
    body: JSON.stringify({ messaging_product: "whatsapp", ...cuerpo }),
  });
  if (!r.ok) console.error("Meta respondió", r.status, (await r.text()).slice(0, 400));
  return r.ok;
}

/** Plantilla aprobada (la única forma de escribir primero); los parámetros llenan {{1}}, {{2}}… del cuerpo. */
export const enviarPlantilla = (a: string, plantilla: string, parametros: string | string[]) =>
  enviar({
    to: a,
    type: "template",
    template: {
      name: plantilla,
      language: { code: "es" },
      components: [{ type: "body", parameters: [parametros].flat().map((text) => ({ type: "text", text })) }],
    },
  });

/** Texto libre: solo llega dentro de las 24 horas siguientes al último mensaje del paciente. */
export const enviarTexto = (a: string, texto: string) => enviar({ to: a, type: "text", text: { body: texto } });

export const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type" };
export const responder = (estado: number, cuerpo: Record<string, unknown>) =>
  new Response(JSON.stringify(cuerpo), { status: estado, headers: { ...CORS, "Content-Type": "application/json" } });
