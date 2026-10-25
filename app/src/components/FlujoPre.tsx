import { useEffect, type ReactNode } from "react";

/**
 * Pantallas del pre-registro al estilo de un onboarding de celular (como Morse), sobre blanco:
 * arriba la flecha de atrás y la barra del flujo; título grande alineado a la izquierda, fichas grises con la etiqueta
 * adentro y un botón grande abajo. Si el botón no deja seguir, encima dice por qué (motivo). Ver app/DESIGN.md.
 */

export const PASOS_PRE = 6; // quién eres · cumpleaños · dónde vives · objetivo · alergias · términos

export function BarraFlujo({ paso, total = PASOS_PRE }: { paso: number; total?: number }) {
  return (
    <div role="progressbar" aria-valuemin={1} aria-valuemax={total} aria-valuenow={paso} aria-label={`Paso ${paso} de ${total}`} className="flex justify-center gap-1.5">
      {Array.from({ length: total }, (_, i) => (
        <span key={i} className={`h-[5px] rounded-full transition-all duration-500 ${i < paso ? "w-6 bg-ink" : "w-4 bg-rule"}`} />
      ))}
    </div>
  );
}

export function PantallaPre({
  paso,
  titulo,
  texto,
  children,
  boton,
  puedeSeguir = true,
  ocupado = false,
  onSeguir,
  onAtras,
  motivo,
  encimaBoton,
  error,
}: {
  paso: number;
  titulo: ReactNode;
  texto?: ReactNode;
  children: ReactNode;
  boton: string;
  puedeSeguir?: boolean;
  ocupado?: boolean;
  onSeguir: () => void;
  onAtras?: () => void;
  /** Qué falta para seguir; se muestra encima del botón mientras no deja seguir. */
  motivo?: string;
  /** Algo fijo justo encima del botón (la casilla de aceptar en los términos). */
  encimaBoton?: ReactNode;
  error?: string | null;
}) {
  // Cada pantalla nueva empieza arriba. Con llaves: lo que devuelva scrollTo no debe llegar a React.
  useEffect(() => {
    window.scrollTo({ top: 0 });
  }, [paso]);
  return (
    <main className="min-h-screen bg-white">
      <div className="mx-auto flex min-h-screen max-w-md flex-col px-6 pb-36">
        <div className="grid grid-cols-[4rem_1fr_4rem] items-center gap-2 pt-5">
          <span>
            {onAtras && (
              <button type="button" onClick={onAtras} aria-label="Atrás" className="grid h-10 w-10 place-items-center rounded-full text-ink">
                <svg viewBox="0 0 24 24" className="h-6 w-6" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
                  <path d="M19 12H5M12 19l-7-7 7-7" />
                </svg>
              </button>
            )}
          </span>
          <BarraFlujo paso={paso} />
          <span />
        </div>
        <section key={paso} className="rise pt-9">
          <h1 className="text-balance text-[32px] font-normal leading-[1.12] tracking-tight text-ink">{titulo}</h1>
          {texto && <p className="mt-3 text-[17px] leading-relaxed text-ink-muted">{texto}</p>}
          <div className="mt-7">{children}</div>
        </section>
      </div>
      <div className="fixed inset-x-0 bottom-0 z-30 bg-white px-6 pb-[max(1.25rem,env(safe-area-inset-bottom))] pt-3">
        <div className="mx-auto max-w-md">
          {error && <p role="alert" className="mb-3 rounded-xl bg-critical-soft px-4 py-2 text-center text-base text-critical">{error}</p>}
          {encimaBoton && <div className="mb-3 flex justify-center">{encimaBoton}</div>}
          {!puedeSeguir && motivo && (
            <p aria-live="polite" className="mb-3 text-center text-base text-ink-muted">
              {motivo}
            </p>
          )}
          <button
            type="button"
            onClick={onSeguir}
            disabled={!puedeSeguir || ocupado}
            className="h-14 w-full rounded-full bg-ink text-lg text-white transition-opacity duration-300 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-marca/40 disabled:cursor-not-allowed disabled:opacity-30"
          >
            {ocupado ? "Guardando…" : boton}
          </button>
        </div>
      </div>
    </main>
  );
}

/** Ficha gris con la etiqueta adentro, arriba del valor (como en la referencia). */
export function Ficha({ etiqueta, children, className = "" }: { etiqueta: string; children: ReactNode; className?: string }) {
  return (
    <label className={`block rounded-[22px] bg-ficha px-5 pb-3.5 pt-3 transition-shadow focus-within:ring-2 focus-within:ring-marca/50 ${className}`}>
      <span className="block text-base text-ink-muted">{etiqueta}</span>
      <span className="mt-0.5 flex items-center gap-1.5 text-[18px] text-ink">{children}</span>
    </label>
  );
}

export const claseFicha = "w-full min-w-0 appearance-none bg-transparent text-[18px] text-ink outline-none placeholder:text-ink-faint";
