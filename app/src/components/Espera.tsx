import { Phone } from "lucide-react";
import { GROSOR_Y, TRAZO_Y } from "@/lib/trazo_y";

/**
 * Espera de resultados (después de la visita de la enfermera): la "y" de Saludly se dibuja de punta a punta,
 * plana y sin brillos, como en el video de marca, y debajo el aviso de WhatsApp. Nada más.
 */
export function Espera() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-background px-6">
      <svg viewBox="0 0 981.45 1248.02" className="h-40 w-auto" role="img" aria-label="Saludly está esperando tus resultados">
        <path d={TRAZO_Y} pathLength={1} className="trazo-espera" fill="none" stroke="#2793ff" strokeWidth={GROSOR_Y} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      <p className="rise mt-12 flex max-w-xs items-center gap-3 text-left text-base leading-relaxed text-ink">
        <IconoWhatsApp />
        Te enviaremos un mensaje por WhatsApp cuando estén tus resultados.
      </p>
    </main>
  );
}

/** Burbuja verde de WhatsApp con el teléfono, dibujada aquí (sin archivos externos). */
function IconoWhatsApp() {
  return (
    <span className="relative grid h-11 w-11 shrink-0 place-items-center" aria-hidden>
      <svg viewBox="0 0 24 24" className="absolute inset-0 h-full w-full">
        <path d="M12 1.5a10.5 10.5 0 0 0-9.06 15.8L1.5 22.5l5.33-1.4A10.5 10.5 0 1 0 12 1.5z" fill="#25D366" />
      </svg>
      <Phone className="relative h-5 w-5 text-white" strokeWidth={2.2} fill="currentColor" />
    </span>
  );
}
