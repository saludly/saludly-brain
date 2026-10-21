import type { ReactNode } from "react";
import { Marca } from "@/components/Comunes";

/** Pantalla de un paso de la PWA: marca, progreso, contenido y botón fijo abajo (mismo formato del recorrido). */
export function Pantalla({
  paso,
  total,
  etiqueta,
  children,
  boton,
  puedeSeguir = true,
  ocupado = false,
  onSeguir,
  onAtras,
  error,
}: {
  paso?: number;
  total?: number;
  etiqueta?: string;
  children: ReactNode;
  boton: string;
  puedeSeguir?: boolean;
  ocupado?: boolean;
  onSeguir: () => void;
  onAtras?: () => void;
  error?: string | null;
}) {
  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-3xl flex-col px-6 pb-36 pt-8 sm:px-10">
        <Marca derecha={paso && total ? `Paso ${paso} / ${total}` : undefined} />
        {paso && total ? (
          <nav aria-label="Progreso" className="mt-8">
            <div className="flex gap-1.5">
              {Array.from({ length: total }, (_, i) => (
                <span key={i} className={`h-1.5 flex-1 rounded-full transition-colors duration-300 ${i < paso ? "bg-optimal" : "bg-rule"}`} />
              ))}
            </div>
            {etiqueta && <p className="mt-3 font-mono text-[10px] uppercase tracking-[0.18em] text-ink-faint">{etiqueta}</p>}
          </nav>
        ) : null}
        <section key={paso} className="rise mt-10 flex-1">
          {children}
        </section>
      </div>
      <div className="fixed inset-x-0 bottom-0 z-30 border-t border-rule bg-background/95 px-6 py-4 backdrop-blur sm:px-10">
        <div className="mx-auto max-w-3xl">
          {error && <p className="mb-3 rounded-xl bg-critical-soft px-4 py-2 text-sm text-critical">{error}</p>}
          <div className="flex items-center gap-3">
            {onAtras && (
              <button
                type="button"
                onClick={onAtras}
                className="rounded-full border border-rule px-5 py-4 text-sm text-ink-muted transition-colors hover:border-ink/20 hover:text-ink"
              >
                Atrás
              </button>
            )}
            <button
              type="button"
              onClick={onSeguir}
              disabled={!puedeSeguir || ocupado}
              className="flex-1 rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground transition-opacity duration-300 disabled:cursor-not-allowed disabled:opacity-40"
            >
              {ocupado ? "Guardando…" : boton}
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}

export function Titulo({ children, texto }: { children: ReactNode; texto?: ReactNode }) {
  return (
    <>
      <h1 className="text-3xl font-light tracking-tight text-ink sm:text-4xl">{children}</h1>
      {texto && <p className="mt-3 max-w-xl text-sm leading-relaxed text-ink-muted">{texto}</p>}
    </>
  );
}

export function Opcion({ activa, onClick, texto, nota, multiple }: { activa: boolean; onClick: () => void; texto: string; nota?: string | null; multiple?: boolean }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-pressed={activa}
      className={`rounded-2xl border p-4 text-left transition-all duration-300 ${activa ? "border-optimal bg-optimal-soft" : "border-rule hover:border-ink/20"}`}
    >
      <span className="flex items-center justify-between gap-3">
        <span className="text-sm text-ink">{texto}</span>
        <span
          className={`flex h-5 w-5 shrink-0 items-center justify-center border text-[10px] ${multiple ? "rounded-md" : "rounded-full"} ${
            activa ? "border-optimal bg-optimal text-primary-foreground" : "border-rule text-transparent"
          }`}
        >
          ✓
        </span>
      </span>
      {nota && <span className="mt-1 block text-xs text-ink-muted">{nota}</span>}
    </button>
  );
}

export function Campo({
  etiqueta,
  ayuda,
  children,
}: {
  etiqueta: string;
  ayuda?: string;
  children: ReactNode;
}) {
  return (
    <label className="block">
      <span className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">{etiqueta}</span>
      <div className="mt-2">{children}</div>
      {ayuda && <span className="mt-1.5 block text-xs text-ink-muted">{ayuda}</span>}
    </label>
  );
}

export const claseEntrada =
  "w-full rounded-2xl border border-rule bg-background px-4 py-3.5 text-base text-ink outline-none transition-colors placeholder:text-ink-faint focus:border-optimal";
