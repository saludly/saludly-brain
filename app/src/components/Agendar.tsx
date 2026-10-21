import { useEffect, useState } from "react";
import { CalendarCheck } from "lucide-react";
import { supabase } from "@/lib/sesion";

/**
 * Agenda de la visita (pantalla Listo, con el pago confirmado). Los días libres los da la función agenda:
 * lunes a viernes, una visita por día, de 7 a 11 a. m. Al confirmar, la cita queda en el Google Calendar de
 * Saludly y en el del paciente (le llega la invitación) y sale el WhatsApp de cita agendada.
 */
interface Dia {
  fecha: string;
  horas: string[];
}

const largo = (f: string) => new Date(`${f}T12:00:00Z`).toLocaleDateString("es-CO", { weekday: "long", day: "numeric", month: "long", timeZone: "UTC" });
const corto = (f: string) => new Date(`${f}T12:00:00Z`).toLocaleDateString("es-CO", { weekday: "short", day: "numeric", timeZone: "UTC" });
const hora = (h: string) => `${Number(h.slice(0, 2))}:00 a. m.`;

export function Agendar() {
  const [cita, setCita] = useState<{ inicio: string; dia: string } | null>(null);
  const [dias, setDias] = useState<Dia[] | null>(null);
  const [fecha, setFecha] = useState<string | null>(null);
  const [h, setH] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const cargar = async () => {
    const { data, error } = await supabase.functions.invoke("agenda", { method: "GET" });
    if (error) {
      const cuerpo = await (error as { context?: Response }).context?.json?.().catch(() => null);
      return setError(cuerpo?.error ?? "La agenda no está disponible en este momento.");
    }
    if (data.cita) setCita(data.cita);
    else setDias(data.dias);
  };
  useEffect(() => {
    void cargar();
  }, []);

  const confirmar = async () => {
    if (!fecha || !h) return;
    setOcupado(true);
    setError(null);
    const { data, error } = await supabase.functions.invoke("agenda", { body: { fecha, hora: h } });
    setOcupado(false);
    if (error) {
      const cuerpo = await (error as { context?: Response }).context?.json?.().catch(() => null);
      setError(cuerpo?.error ?? "No pudimos agendar. Intenta de nuevo.");
      setFecha(null);
      setH(null);
      return void cargar();
    }
    setCita(data.cita);
  };

  if (cita)
    return (
      <div className="mt-8 flex gap-4 rounded-2xl bg-optimal-soft p-5">
        <CalendarCheck className="h-6 w-6 shrink-0 text-optimal" strokeWidth={1.6} />
        <div>
          <h2 className="text-base text-ink">Tu visita quedó agendada</h2>
          <p className="mt-1 text-sm leading-relaxed text-ink-muted">
            {largo(cita.dia)} a las {hora(new Date(cita.inicio).toLocaleTimeString("en-GB", { timeZone: "America/Bogota" }).slice(0, 5))}. Te llegó la invitación a tu
            correo y quedó en tu calendario. Recuerda estar en ayunas.
          </p>
        </div>
      </div>
    );

  return (
    <div className="mt-8 rounded-3xl border border-rule p-5">
      <h2 className="text-base text-ink">Agenda la visita de la enfermera</h2>
      <p className="mt-1 text-sm text-ink-muted">Elige el día y la hora. Va a tu casa en ayunas, de lunes a viernes.</p>
      {error && <p className="mt-3 text-sm text-attention">{error}</p>}
      {dias === null && !error && <p className="mt-4 text-sm text-ink-faint">Buscando días libres…</p>}
      {dias && dias.length === 0 && <p className="mt-4 text-sm text-ink-muted">No hay días libres en las próximas dos semanas. Te escribimos por WhatsApp para acordar uno.</p>}
      {dias && dias.length > 0 && (
        <>
          <div className="mt-4 flex flex-wrap gap-2">
            {dias.map((d) => (
              <button
                key={d.fecha}
                type="button"
                onClick={() => {
                  setFecha(d.fecha);
                  setH(null);
                }}
                className={`rounded-full border px-4 py-2 text-sm capitalize ${fecha === d.fecha ? "border-optimal bg-optimal text-primary-foreground" : "border-rule text-ink"}`}
              >
                {corto(d.fecha)}
              </button>
            ))}
          </div>
          {fecha && (
            <div className="mt-4 flex flex-wrap gap-2">
              {dias.find((d) => d.fecha === fecha)?.horas.map((x) => (
                <button key={x} type="button" onClick={() => setH(x)} className={`rounded-full border px-4 py-2 text-sm ${h === x ? "border-optimal bg-optimal text-primary-foreground" : "border-rule text-ink"}`}>
                  {hora(x)}
                </button>
              ))}
            </div>
          )}
          <button type="button" disabled={!fecha || !h || ocupado} onClick={() => void confirmar()} className="mt-5 w-full rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground disabled:opacity-40">
            {ocupado ? "Agendando…" : fecha && h ? `Agendar el ${largo(fecha)} a las ${hora(h)}` : "Elige día y hora"}
          </button>
        </>
      )}
    </div>
  );
}
