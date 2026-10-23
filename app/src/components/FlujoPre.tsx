import { useEffect, type ReactNode } from "react";

/**
 * Pantallas del pre-registro al estilo de un onboarding de celular (como Morse), sobre blanco:
 * arriba la flecha de atrás, la barra del flujo y, a la derecha, cambiar de cuenta;
 * título grande alineado a la izquierda, fichas grises con la etiqueta adentro y un botón grande abajo.
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
  derecha,
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
  /** Botón pequeño arriba a la derecha (cambiar de cuenta). */
  derecha?: ReactNode;
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
          <span className="flex justify-end">{derecha}</span>
        </div>
        <section key={paso} className="rise pt-9">
          <h1 className="text-balance text-[32px] font-normal leading-[1.12] tracking-tight text-ink">{titulo}</h1>
          {texto && <p className="mt-3 text-[17px] leading-relaxed text-ink-muted">{texto}</p>}
          <div className="mt-7">{children}</div>
        </section>
      </div>
      <div className="fixed inset-x-0 bottom-0 z-30 bg-white px-6 pb-[max(1.25rem,env(safe-area-inset-bottom))] pt-3">
        <div className="mx-auto max-w-md">
          {error && <p className="mb-3 rounded-xl bg-critical-soft px-4 py-2 text-center text-sm text-critical">{error}</p>}
          {encimaBoton && <div className="mb-3 flex justify-center">{encimaBoton}</div>}
          <button
            type="button"
            onClick={onSeguir}
            disabled={!puedeSeguir || ocupado}
            className="h-14 w-full rounded-full bg-ink text-lg text-white transition-opacity duration-300 disabled:cursor-not-allowed disabled:opacity-30"
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
    <label className={`block rounded-[22px] bg-[#f2f4f7] px-5 pb-3.5 pt-3 transition-shadow focus-within:ring-2 focus-within:ring-ink/15 ${className}`}>
      <span className="block text-[14px] text-ink-muted">{etiqueta}</span>
      <span className="mt-0.5 flex items-center gap-1.5 text-[18px] text-ink">{children}</span>
    </label>
  );
}

export const claseFicha = "w-full min-w-0 appearance-none bg-transparent text-[18px] text-ink outline-none placeholder:text-ink-faint";

/** Botón pequeño gris redondeado (como "Ayuda" en la referencia). */
export function BotonChico({ children, onClick }: { children: ReactNode; onClick: () => void }) {
  return (
    <button type="button" onClick={onClick} className="whitespace-nowrap rounded-full bg-[#f2f4f7] px-3.5 py-2 text-[13px] text-ink">
      {children}
    </button>
  );
}
