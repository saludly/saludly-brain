import { useEffect, useState } from "react";
import { Check, Copy, ExternalLink, Stethoscope } from "lucide-react";
import { useInforme } from "@/lib/contexto";
import { supabase, useSesion } from "@/lib/sesion";

/**
 * Tarjeta del panel con el enlace para el médico (el mismo que llega por WhatsApp). Solo con el informe propio.
 * No muestra la dirección completa (en el celular se partía en muchas líneas): se comparte, se copia o se abre.
 */
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
      setTimeout(() => setCopiado(false), 2500);
    } catch {
      /* sin portapapeles: queda "Ver resumen" para abrirlo y copiarlo desde el navegador */
    }
  };
  const whatsapp = `https://wa.me/?text=${encodeURIComponent(`Doctor(a), este es el resumen de mis resultados de Saludly: ${enlace}`)}`;

  return (
    <section className="rise mt-12 rounded-3xl border border-rule bg-optimal-soft/40 p-6 sm:p-8">
      <div className="flex items-start gap-4">
        <span className="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-background text-optimal">
          <Stethoscope className="h-6 w-6" strokeWidth={1.6} />
        </span>
        <div className="min-w-0">
          <h2 className="text-xl font-light tracking-tight text-ink">Muéstrale esto a tu médico</h2>
          <p className="mt-1 text-sm leading-relaxed text-ink-muted">
            Tu médico ve tu resumen completo, sin crear una cuenta. Es un enlace privado: solo lo abre quien lo tenga.
          </p>
        </div>
      </div>
      <div className="mt-5 grid gap-2 sm:grid-cols-3">
        <a href={whatsapp} target="_blank" rel="noreferrer" className="flex items-center justify-center gap-2 rounded-full bg-[#25D366] px-5 py-3 text-sm text-white">
          Enviar por WhatsApp
        </a>
        <button type="button" onClick={() => void copiar()} className="flex items-center justify-center gap-2 rounded-full border border-rule bg-background px-5 py-3 text-sm text-ink">
          {copiado ? <Check className="h-4 w-4 text-optimal" /> : <Copy className="h-4 w-4" />}
          {copiado ? "Enlace copiado" : "Copiar enlace"}
        </button>
        <a href={enlace} target="_blank" rel="noreferrer" className="flex items-center justify-center gap-2 rounded-full border border-rule bg-background px-5 py-3 text-sm text-ink">
          <ExternalLink className="h-4 w-4" />
          Ver resumen
        </a>
      </div>
    </section>
  );
}
