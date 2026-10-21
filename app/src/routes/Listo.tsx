import { useEffect } from "react";
import { useNavigate } from "@tanstack/react-router";
import { CalendarClock, MessageCircle, Stethoscope } from "lucide-react";
import { Marca } from "@/components/Comunes";
import { Espera } from "@/components/Espera";
import { siguientePaso, useSesion } from "@/lib/sesion";
import C from "@/lib/contenido.json";

/**
 * Después del cuestionario. Muestra si el pago ya está confirmado; la agenda en la app (Google Calendar) viene después.
 * Mientras tanto, Carlos coordina la visita por WhatsApp (1 por día, lunes a viernes, de 7 a 11 a. m.).
 */
export function Listo() {
  const s = useSesion();
  const navigate = useNavigate();
  useEffect(() => {
    if (s.cargando) return;
    const ir = siguientePaso(s);
    if (ir !== "/listo") void navigate({ to: ir });
  }, [s, navigate]);

  const pagoConfirmado = s.pago?.estado === "confirmado";
  const nombre = s.paciente?.nombre.split(" ")[0];
  // Ya pasó la enfermera: solo queda esperar el laboratorio.
  if (s.visita) return <Espera />;

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-xl flex-col px-6 py-8">
        <Marca />
        <section className="rise mt-14">
          <h1 className="text-3xl font-light tracking-tight text-ink">¡Listo{nombre ? `, ${nombre}` : ""}! Ya tenemos tus respuestas.</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">Ahora necesitamos tomar tu muestra y algunas medidas en una visita corta de la enfermera.</p>
          <div className="mt-8 space-y-3">
            {[
              pagoConfirmado
                ? { icono: CalendarClock, t: "Tu pago está confirmado", d: "Agendamos tu visita de lunes a viernes, entre las 7 y las 11 de la mañana. Te escribimos por WhatsApp para confirmar el día." }
                : { icono: CalendarClock, t: "Estamos confirmando tu pago", d: "Apenas lo confirmemos te avisamos por WhatsApp para agendar la visita de la enfermera." },
              { icono: Stethoscope, t: "Ve en ayunas", d: C.ayuno.aviso },
              { icono: MessageCircle, t: "Te avisamos por WhatsApp", d: "Cuando estén tus resultados y un médico los revise, te enviamos un mensaje para que los veas aquí." },
            ].map((x) => (
              <article key={x.t} className="flex gap-4 rounded-2xl border border-rule p-5">
                <span className="grid h-10 w-10 shrink-0 place-items-center rounded-2xl bg-optimal-soft text-optimal">
                  <x.icono className="h-5 w-5" strokeWidth={1.6} />
                </span>
                <div>
                  <h2 className="text-base text-ink">{x.t}</h2>
                  <p className="mt-1 text-sm leading-relaxed text-ink-muted">{x.d}</p>
                </div>
              </article>
            ))}
          </div>
          {s.visita ? (
            <p className="mt-8 rounded-2xl bg-optimal-soft p-4 text-sm leading-relaxed text-ink">
              ✓ La enfermera ya tomó tus medidas. Ahora esperamos los resultados del laboratorio.
            </p>
          ) : (
            <button
              type="button"
              onClick={() => void navigate({ to: "/visita" })}
              className="mt-8 w-full rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground"
            >
              Mi enfermera está aquí
            </button>
          )}
          <button type="button" onClick={() => void s.salir()} className="mt-10 text-sm text-ink-faint underline-offset-4 hover:underline">
            Cerrar sesión
          </button>
        </section>
      </div>
    </main>
  );
}
