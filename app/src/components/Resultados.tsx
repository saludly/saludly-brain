import { useEffect, useState } from "react";
import { X } from "lucide-react";
import { ETIQUETA, PUNTO, SUAVE, TEXTO, barra, estadoDe, valorTexto } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";
import type { Resultado } from "@/lib/informe";

function Barra({ r, grande = false }: { r: Resultado; grande?: boolean }) {
  const b = barra(r);
  if (!b) return null;
  const e = estadoDe(r.clase);
  return (
    <div className={`relative w-full rounded-full bg-rule ${grande ? "h-1.5" : "mt-3 h-1"}`}>
      <div className="absolute inset-y-0 rounded-full bg-optimal-soft" style={{ left: `${b.inicio}%`, width: `${b.ancho}%` }} />
      <div
        className={`absolute top-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full transition-all duration-500 ${PUNTO[e]} ${
          grande ? "h-3.5 w-3.5 ring-4 ring-background" : "h-2.5 w-2.5 ring-2 ring-background"
        }`}
        style={{ left: `${b.posicion}%` }}
      />
    </div>
  );
}

export function TarjetaResultado({ r, onSelect }: { r: Resultado; onSelect: (r: Resultado) => void }) {
  const e = estadoDe(r.clase);
  return (
    <button
      type="button"
      onClick={() => onSelect(r)}
      aria-label={`${r.nombre}: ${valorTexto(r)} ${r.unidad ?? ""}`}
      className="group rounded-2xl border border-rule bg-background px-4 py-4 text-left transition-all duration-300 hover:-translate-y-0.5 hover:border-ink/15 hover:shadow-[0_12px_32px_-20px_rgba(20,30,60,0.45)] focus:outline-none focus-visible:ring-2 focus-visible:ring-ring"
    >
      <div className="flex items-start justify-between gap-3">
        <span className="text-[13px] leading-snug text-ink">{r.nombre}</span>
        <span className={`mt-1 h-2 w-2 shrink-0 rounded-full ${PUNTO[e]}`} />
      </div>
      <div className="mt-3 flex items-baseline gap-1.5">
        <span className={`font-mono text-xl tabular-nums ${TEXTO[e]}`}>{valorTexto(r)}</span>
        <span className="text-[11px] text-ink-faint">{r.unidad}</span>
      </div>
      <Barra r={r} />
    </button>
  );
}

export function Categoria({ nombre, items, onSelect }: { nombre: string; items: Resultado[]; onSelect: (r: Resultado) => void }) {
  const [abierta, setAbierta] = useState(false);
  const porRevisar = items.filter((i) => ["fuera", "pronto"].includes(estadoDe(i.clase))).length;
  const id = nombre.toLowerCase().normalize("NFD").replace(/[^a-z0-9]+/g, "-");
  return (
    <section className="mt-6 scroll-mt-24" id={id}>
      <button
        type="button"
        onClick={() => setAbierta((v) => !v)}
        aria-expanded={abierta}
        aria-controls={`${id}-panel`}
        className="flex w-full items-baseline justify-between gap-4 border-b border-rule pb-3 text-left transition-colors duration-300 hover:border-ink/25 focus:outline-none focus-visible:ring-2 focus-visible:ring-ring"
      >
        <span className="flex items-center gap-3">
          <span aria-hidden className={`inline-block text-ink-faint transition-transform duration-300 ${abierta ? "rotate-90" : ""}`}>
            ›
          </span>
          <h3 className="text-lg font-normal tracking-tight text-ink">{nombre}</h3>
        </span>
        <span className="font-mono text-[11px] tabular-nums text-ink-faint">
          {items.length} resultados
          {porRevisar > 0 && <span className="text-attention"> · {porRevisar} por revisar</span>}
        </span>
      </button>
      <div id={`${id}-panel`} className={`grid transition-all duration-500 ease-out ${abierta ? "mt-4 grid-rows-[1fr] opacity-100" : "grid-rows-[0fr] opacity-0"}`}>
        <div className="overflow-hidden">
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {items.map((r) => (
              <TarjetaResultado key={r.biomarker_id} r={r} onSelect={onSelect} />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

const GUIA = {
  en_rango: "Su resultado está dentro del rango de referencia de su laboratorio. Siga cuidando sus hábitos.",
  fuera: "Su resultado está fuera del rango de referencia. Un solo examen no basta para sacar conclusiones: revise en su informe qué puede significar y qué puede hacer.",
  pronto: "El laboratorio marcó este resultado para revisarlo pronto. Nuestro equipo médico se comunica con usted.",
  sin_lectura: "Este resultado no se pudo interpretar con seguridad. Su médico lo revisa.",
};

export function DetalleResultado({ r, onClose }: { r: Resultado | null; onClose: () => void }) {
  const { informe } = useInforme();
  useEffect(() => {
    if (!r) return;
    const tecla = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", tecla);
    return () => window.removeEventListener("keydown", tecla);
  }, [r, onClose]);
  const abierto = r !== null;
  const e = r ? estadoDe(r.clase) : "en_rango";
  const relacionados = r
    ? informe.paciente.lo_que_merece_atencion.filter((h) => h.por_que.some((p) => p.toLowerCase().includes(r.nombre.toLowerCase())))
    : [];

  return (
    <>
      <div
        onClick={onClose}
        aria-hidden
        className={`fixed inset-0 z-40 bg-scrim backdrop-blur-[2px] transition-opacity duration-300 ${abierto ? "opacity-100" : "pointer-events-none opacity-0"}`}
      />
      <aside
        role="dialog"
        aria-modal="true"
        aria-label={r?.nombre ?? "Detalle del resultado"}
        className={`fixed inset-y-0 right-0 z-50 w-full max-w-md overflow-y-auto bg-background transition-transform duration-500 [transition-timing-function:cubic-bezier(0.22,1,0.36,1)] ${
          abierto ? "translate-x-0" : "translate-x-full"
        }`}
      >
        {r && (
          <div className="px-7 py-8">
            <div className="flex items-start justify-between gap-4">
              <div>
                <span className="font-mono text-[10px] uppercase tracking-[0.2em] text-ink-faint">{r.seccion}</span>
                <h3 className="mt-2 text-2xl font-light tracking-tight text-ink">{r.nombre}</h3>
              </div>
              <button
                type="button"
                onClick={onClose}
                aria-label="Cerrar"
                className="rounded-full border border-rule p-2 text-ink-muted transition-colors hover:bg-secondary hover:text-ink"
              >
                <X className="h-4 w-4" />
              </button>
            </div>
            <div className="mt-7 flex items-end justify-between">
              <div className="flex items-baseline gap-2">
                <span className={`font-mono text-5xl tabular-nums ${TEXTO[e]}`}>{valorTexto(r)}</span>
                <span className="text-sm text-ink-faint">{r.unidad}</span>
              </div>
              <span className={`rounded-full px-3 py-1 text-[10px] uppercase tracking-[0.14em] ${SUAVE[e]}`}>{ETIQUETA[e]}</span>
            </div>
            <div className="mt-8">
              <Barra r={r} grande />
            </div>
            <div className="mt-9 space-y-6">
              <div>
                <h4 className="text-[11px] uppercase tracking-[0.18em] text-ink-faint">Qué significa su resultado</h4>
                <p className="mt-2 text-sm leading-relaxed text-ink-muted">{r.motivo ?? GUIA[e]}</p>
              </div>
              {relacionados.length > 0 && (
                <div>
                  <h4 className="text-[11px] uppercase tracking-[0.18em] text-ink-faint">Aparece en</h4>
                  <ul className="mt-2 space-y-1.5 text-sm text-ink">
                    {relacionados.map((h) => (
                      <li key={h.hallazgo_id}>· {h.titulo}</li>
                    ))}
                  </ul>
                </div>
              )}
              <div className="rounded-2xl bg-surface p-5">
                <h4 className="text-[11px] uppercase tracking-[0.18em] text-ink-faint">Rango de referencia del laboratorio</h4>
                <p className="mt-2 font-mono text-sm tabular-nums text-ink">
                  {r.intervalo ?? "—"} {r.unidad}
                </p>
                <p className="mt-3 text-xs leading-relaxed text-ink-faint">Este informe es preventivo y no es un diagnóstico.</p>
              </div>
            </div>
          </div>
        )}
      </aside>
    </>
  );
}
