import { useState } from "react";
import { ChevronDown } from "lucide-react";
import { PLAZO, SUAVE, estadoDe, estadoDeEscalamiento } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";
import type { Hallazgo } from "@/lib/informe";

/** Medidor semicircular para la edad biológica. */
function Medidor({ valor, min, max }: { valor: number; min: number; max: number }) {
  const pct = Math.min(1, Math.max(0, (valor - min) / (max - min)));
  const largo = Math.PI * 62;
  return (
    <svg viewBox="0 0 160 92" className="w-full max-w-[220px]" aria-hidden>
      <path d="M 18 80 A 62 62 0 0 1 142 80" fill="none" stroke="currentColor" className="text-rule" strokeWidth="8" strokeLinecap="round" />
      <path
        d="M 18 80 A 62 62 0 0 1 142 80"
        fill="none"
        stroke="currentColor"
        className="text-optimal"
        strokeWidth="8"
        strokeLinecap="round"
        strokeDasharray={`${largo * pct} ${largo}`}
      />
    </svg>
  );
}

function TarjetaHallazgo({ h }: { h: Hallazgo }) {
  const [abierta, setAbierta] = useState(false);
  const estado = estadoDeEscalamiento(h.escalamiento);
  return (
    <article className="rounded-2xl border border-rule bg-background p-5 transition-colors duration-300 hover:border-ink/15">
      <button type="button" onClick={() => setAbierta((v) => !v)} aria-expanded={abierta} className="w-full text-left">
        <div className="flex items-start justify-between gap-3">
          <span className={`rounded-full px-2 py-0.5 text-[9px] uppercase tracking-[0.12em] ${SUAVE[estado]}`}>{PLAZO[h.escalamiento]}</span>
          <ChevronDown className={`h-4 w-4 shrink-0 text-ink-faint transition-transform duration-300 ${abierta ? "rotate-180" : ""}`} />
        </div>
        <h3 className="mt-3 text-base leading-snug text-ink">{h.titulo}</h3>
        <p className="mt-2 text-xs leading-relaxed text-ink-muted">{h.que_es}</p>
      </button>
      {abierta && (
        <div className="mt-4 space-y-3 border-t border-rule pt-4 text-sm leading-relaxed text-ink-muted">
          <ul className="space-y-1.5">
            {h.por_que.map((p) => (
              <li key={p}>· {p}</li>
            ))}
          </ul>
          <p className="rounded-xl bg-surface p-3 text-xs">{h.ejemplo}</p>
        </div>
      )}
    </article>
  );
}

export function Indicadores() {
  const { informe } = useInforme();
  const p = informe.paciente;
  const res = informe.resultados.filter((r) => r.estado !== "no_medido");
  const enRango = res.filter((r) => estadoDe(r.clase) === "en_rango").length;
  const eb = informe.edad_biologica;

  return (
    <section className="mt-16">
      <div className="flex items-baseline justify-between border-b border-rule pb-4">
        <h2 className="text-2xl font-light tracking-tight text-ink">Su resumen</h2>
        <span className="font-mono text-[11px] uppercase tracking-[0.18em] text-ink-faint">Informe preventivo</span>
      </div>

      <p className="mt-6 max-w-3xl text-base leading-relaxed text-ink">{p.resumen}</p>
      {p.nota_alimentacion && <p className="mt-3 max-w-3xl rounded-2xl bg-optimal-soft p-4 text-sm leading-relaxed text-ink">{p.nota_alimentacion}</p>}

      <div className="mt-6 grid gap-3 sm:grid-cols-2 lg:max-w-2xl">
        <div className="flex aspect-[5/4] flex-col justify-between rounded-2xl bg-optimal p-6 text-primary-foreground sm:aspect-square">
          <span className="text-[11px] uppercase tracking-[0.2em] text-primary-foreground/70">Resultados en rango</span>
          <div>
            <div className="flex items-baseline gap-1">
              <span className="font-mono text-6xl leading-none tabular-nums">{enRango}</span>
              <span className="font-mono text-xl text-primary-foreground/60">/{res.length}</span>
            </div>
            <p className="mt-3 text-xs leading-relaxed text-primary-foreground/80">
              Un conteo de sus resultados frente al rango de su laboratorio. No es una calificación de su salud.
            </p>
          </div>
        </div>

        {eb && (
          <div className="relative flex aspect-[5/4] flex-col justify-between overflow-hidden rounded-2xl border border-rule bg-background p-6 sm:aspect-square">
            <div aria-hidden className="pointer-events-none absolute -right-10 -top-10 h-40 w-40 rounded-full bg-optimal-soft blur-2xl" />
            <span className="relative text-[11px] uppercase tracking-[0.2em] text-ink-faint">Edad biológica estimada</span>
            <div className="relative flex flex-col items-center">
              <Medidor valor={eb.phenoage} min={20} max={80} />
              <div className="-mt-10 flex items-baseline gap-1">
                <span className="font-mono text-5xl leading-none tabular-nums text-ink">{eb.phenoage.toLocaleString("es-CO")}</span>
                <span className="text-xs text-ink-faint">años</span>
              </div>
              <p className="mt-2 text-center text-xs text-ink-muted">
                {eb.diferencia <= 0
                  ? `${Math.abs(eb.diferencia).toLocaleString("es-CO")} años menos que su edad.`
                  : `${eb.diferencia.toLocaleString("es-CO")} años más que su edad.`}{" "}
                Es una estimación, no un diagnóstico.
              </p>
            </div>
          </div>
        )}
      </div>

      {p.lo_que_merece_atencion.length > 0 && (
        <>
          <h3 className="mt-12 text-lg font-light tracking-tight text-ink">Lo que merece atención</h3>
          <div className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {p.lo_que_merece_atencion.map((h) => (
              <TarjetaHallazgo key={h.hallazgo_id} h={h} />
            ))}
          </div>
        </>
      )}

      {p.lo_que_esta_bien.length > 0 && (
        <>
          <h3 className="mt-12 text-lg font-light tracking-tight text-ink">Lo que está bien</h3>
          <div className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
            {p.lo_que_esta_bien.map((b) => (
              <article key={b.grupo} className="rounded-2xl border border-rule bg-optimal-soft p-5">
                <span className="text-[11px] uppercase tracking-[0.16em] text-optimal">{b.nombre ?? b.grupo}</span>
                <p className="mt-2 text-xs leading-relaxed text-ink-muted">{b.texto}</p>
              </article>
            ))}
          </div>
        </>
      )}
    </section>
  );
}
