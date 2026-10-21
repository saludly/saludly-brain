import { Link, useRouterState } from "@tanstack/react-router";
import { CASOS } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";

export function Marca({ derecha }: { derecha?: string }) {
  return (
    <header className="flex items-center justify-between gap-4">
      <div className="flex items-center gap-2.5">
        <span className="flex h-7 w-7 items-center justify-center rounded-full bg-optimal">
          <span className="h-2 w-2 rounded-full bg-background" />
        </span>
        <span className="text-lg tracking-tight text-ink">Saludly</span>
      </div>
      {derecha && <span className="font-mono text-[11px] uppercase tracking-[0.2em] text-ink-faint">{derecha}</span>}
    </header>
  );
}

/** Rutas que muestran un informe. Por ahora usan los informes de ejemplo. */
export const RUTAS_INFORME = ["/recorrido", "/panel", "/plan"];

const ITEMS: { label: string; to: "/panel" | "/plan"; hash?: string }[] = [
  { label: "INICIO", to: "/panel" },
  { label: "MI PLAN", to: "/plan" },
  { label: "RESULTADOS", to: "/panel", hash: "resultados" },
];

export function NavFlotante() {
  const { pathname, hash } = useRouterState({ select: (s) => s.location });
  if (!RUTAS_INFORME.includes(pathname) || pathname === "/recorrido") return null; // el recorrido y el registro no muestran el menú
  const activo = ITEMS.findIndex((i) => (i.hash ? pathname === "/panel" && hash === i.hash : i.to === pathname && !hash));
  return (
    <div className="pointer-events-none sticky top-3 z-40 flex justify-center px-3 sm:top-4 sm:px-4">
      <nav className="pointer-events-auto flex max-w-full items-center gap-0.5 overflow-x-auto rounded-full bg-ink/95 p-1 shadow-[0_10px_30px_-12px_rgba(0,0,0,0.5)] backdrop-blur sm:gap-1 sm:p-1.5">
        {ITEMS.map((item, idx) => (
          <Link
            key={item.label}
            to={item.to}
            {...(item.hash ? { hash: item.hash } : {})}
            className={`shrink-0 whitespace-nowrap rounded-full px-3 py-1.5 font-mono text-[9px] uppercase tracking-[0.08em] transition-all duration-300 sm:px-4 sm:text-[10px] sm:tracking-[0.16em] ${
              idx === activo ? "bg-background text-ink" : "text-background/60 hover:bg-background/10 hover:text-background"
            }`}
          >
            {item.label}
          </Link>
        ))}
      </nav>
    </div>
  );
}

/** Barra para cambiar de caso de ejemplo. Desaparece cuando el informe venga de la cuenta del paciente. */
export function BarraDemo() {
  const { caso, cambiarCaso, origen, revisar } = useInforme();
  const { pathname } = useRouterState({ select: (s) => s.location });
  if (!RUTAS_INFORME.includes(pathname) || origen === "propio") return null;
  if (origen === "revision")
    return (
      <div className="border-b border-rule bg-attention-soft px-4 py-2">
        <div className="mx-auto flex max-w-7xl flex-wrap items-center gap-3 text-[11px] text-ink">
          <span className="font-mono uppercase tracking-[0.14em]">Vista previa · así lo verá el paciente</span>
          <Link to="/medico" onClick={() => revisar(null)} className="rounded-full border border-ink/20 bg-background px-3 py-1">
            Volver a la revisión
          </Link>
        </div>
      </div>
    );
  return (
    <div className="border-b border-rule bg-surface px-4 py-2">
      <div className="mx-auto flex max-w-7xl flex-wrap items-center gap-2 text-[11px] text-ink-muted">
        <span className="font-mono uppercase tracking-[0.14em] text-ink-faint">Demo · datos sintéticos</span>
        <select
          value={caso}
          onChange={(e) => cambiarCaso(e.target.value)}
          className="rounded-full border border-rule bg-background px-3 py-1 text-[11px] text-ink"
          aria-label="Caso de ejemplo"
        >
          {CASOS.map((c) => (
            <option key={c.id} value={c.id}>
              {c.nombre}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}

export function PieLegal() {
  return (
    <footer className="mt-20 border-t border-rule py-8 text-xs leading-relaxed text-ink-faint">
      Este informe es preventivo y no es un diagnóstico. Un médico de Saludly lo revisó. Ante cualquier duda, consulta con tu médico.
    </footer>
  );
}
