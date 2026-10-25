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

/**
 * El mismo texto de cada plantilla (como se envió a Meta), para mandarlo como texto libre si la plantilla todavía
 * no está aprobada: Meta lo entrega si el paciente escribió al número en las últimas 24 horas.
 */
const TEXTOS: Record<string, (p: string[]) => string> = {
  registro_completo: ([n]) =>
    `Hola, ${n} 👋 Tu registro en Saludly está completo. En tu app encuentras los datos para el pago de tu paquete. Cuando lo hagas, envíanos por este chat la captura del comprobante y te avisamos apenas lo confirmemos.`,
  pago_confirmado: ([n]) => `¡Listo, ${n}! ✅ Confirmamos tu pago. Ya puedes agendar la visita de la enfermera desde tu app: https://app.saludly.online`,
  cita_agendada: ([n, f]) =>
    `Hola, ${n} 📅 Tu visita con la enfermera de Saludly quedó agendada para el ${f}. Recuerda estar en ayunas. Si necesitas cambiarla, escríbenos por aquí.`,
  resultados_listos: ([n]) => `Hola, ${n} 👋 Tus resultados de Saludly ya están listos y un médico los revisó. Entra a tu app para ver tu informe y tu plan: https://app.saludly.online`,
  enlace_medico: ([n, e]) =>
    `Hola, ${n} 👩‍⚕️ Este es el resumen de tus resultados para tu médico. En tu próxima consulta, muéstrale este enlace: ${e}\nSolo lo puede abrir quien tenga el enlace; no lo compartas con nadie más.`,
  visita_agendar: ([n]) =>
    `¡Hola, ${n}! 👋 Ya tenemos tus respuestas en Saludly. Ahora agendemos la visita de la enfermera para tomar tu muestra: es de lunes a viernes, entre las 7 y las 11 de la mañana, y debes estar en ayunas. Responde este mensaje con el día que te queda mejor.`,
};

/**
 * Plantilla aprobada (la única forma de escribir primero); los parámetros llenan {{1}}, {{2}}… del cuerpo.
 * Si Meta la rechaza (por ejemplo, porque aún está en revisión), intenta el mismo texto como mensaje libre.
 */
export async function enviarPlantilla(a: string, plantilla: string, parametros: string | string[]) {
  const p = [parametros].flat();
  const ok = await enviar({
    to: a,
    type: "template",
    template: { name: plantilla, language: { code: "es" }, components: [{ type: "body", parameters: p.map((text) => ({ type: "text", text })) }] },
  });
  if (ok || !TEXTOS[plantilla]) return ok;
  return enviarTexto(a, TEXTOS[plantilla]!(p));
}

/** Texto libre: solo llega dentro de las 24 horas siguientes al último mensaje del paciente. */
export const enviarTexto = (a: string, texto: string) => enviar({ to: a, type: "text", text: { body: texto } });

/** Texto libre con botones de respuesta rápida (hasta 3, de 20 caracteres); cada id vuelve en el webhook al tocarlo. */
export const enviarBotones = (a: string, texto: string, botones: { id: string; titulo: string }[]) =>
  enviar({
    to: a,
    type: "interactive",
    interactive: { type: "button", body: { text: texto }, action: { buttons: botones.map((b) => ({ type: "reply", reply: { id: b.id, title: b.titulo } })) } },
  });

export const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type" };
export const responder = (estado: number, cuerpo: Record<string, unknown>) =>
  new Response(JSON.stringify(cuerpo), { status: estado, headers: { ...CORS, "Content-Type": "application/json" } });
