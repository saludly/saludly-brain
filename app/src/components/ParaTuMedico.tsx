import { useEffect, useState } from "react";
import { Stethoscope } from "lucide-react";
import { useInforme } from "@/lib/contexto";
import { supabase, useSesion } from "@/lib/sesion";

/** Tarjeta del panel con el enlace para el médico (el mismo que llega por WhatsApp). Solo con el informe propio. */
export function ParaTuMedico() {
  const { origen } = useInforme();
  const s = useSesion();
  const [enlace, setEnlace] = useState<string | null>(null);
  const [copiado, setCopiado] = useState(false);

  useEffect(() => {
    if (origen !== "propio" || !s.sesion) return;
    void supabase
      .from("enlaces_medico")
      .select("slug")
      .eq("paciente_id", s.sesion.user.id)
      .is("revocado", null)
      .order("creado", { ascending: false })
      .limit(1)
      .then(({ data }) => setEnlace(data?.[0] ? `${window.location.origin}/m/${data[0].slug}` : null));
  }, [origen, s.sesion]);

  if (!enlace) return null;
  const copiar = async () => {
    try {
      await navigator.clipboard.writeText(enlace);
      setCopiado(true);
    } catch {
      /* sin portapapeles: el enlace queda visible para copiarlo a mano */
    }
  };

  return (
    <section className="rise mt-12 flex flex-wrap items-center gap-4 rounded-3xl border border-rule p-6">
      <span className="grid h-11 w-11 shrink-0 place-items-center rounded-2xl bg-optimal-soft text-optimal">
        <Stethoscope className="h-5 w-5" strokeWidth={1.6} />
      </span>
      <div className="min-w-0 flex-1">
        <h2 className="text-base text-ink">Muéstrale esto a tu médico</h2>
        <p className="mt-1 break-all text-xs text-ink-muted">{enlace}</p>
      </div>
      <div className="flex gap-2">
        <button type="button" onClick={() => void copiar()} className="rounded-full border border-rule px-4 py-2 text-sm text-ink">
          {copiado ? "Copiado" : "Copiar"}
        </button>
        <a href={enlace} target="_blank" rel="noreferrer" className="rounded-full bg-optimal px-4 py-2 text-sm text-primary-foreground">
          Abrir
        </a>
      </div>
    </section>
  );
}
