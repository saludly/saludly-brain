import { useMemo, useState, type CSSProperties } from "react";
import { Cuerpo } from "@/components/Cuerpo";
import { Indicadores } from "@/components/Indicadores";
import { Categoria, DetalleResultado } from "@/components/Resultados";
import { Marca, PieLegal } from "@/components/Comunes";
import { Retenido } from "@/routes/Retenido";
import { estadoDe, fechaLarga, nombreSeccion, type Estado } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";
import type { Resultado } from "@/lib/informe";

type Filtro = "todos" | Estado;
const FILTROS: { k: Filtro; l: string }[] = [
  { k: "todos", l: "Todos" },
  { k: "en_rango", l: "En rango" },
  { k: "fuera", l: "Fuera de rango" },
  { k: "pronto", l: "Atención pronta" },
];

export function Panel() {
  const { informe } = useInforme();
  const [elegido, setElegido] = useState<Resultado | null>(null);
  const [filtro, setFiltro] = useState<Filtro>("todos");

  const grupos = useMemo(() => {
    const lista = informe.resultados.filter((r) => r.estado !== "no_medido" && (filtro === "todos" || estadoDe(r.clase) === filtro));
    const porSeccion = new Map<string, Resultado[]>();
    for (const r of lista) {
      const s = nombreSeccion(r.seccion);
      porSeccion.set(s, [...(porSeccion.get(s) ?? []), r]);
    }
    return [...porSeccion.entries()];
  }, [informe, filtro]);

  if (informe.estado === "retenido_hasta_llamada") return <Retenido />;

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-7xl px-6 py-8 sm:px-10">
        <Marca derecha={`Informe · ${fechaLarga(informe.fecha_toma)}`} />
        <Cuerpo />
        <Indicadores />
        <section id="resultados" className="rise mt-16 scroll-mt-24" style={{ "--rise-delay": "0.3s" } as CSSProperties}>
          <div className="flex flex-wrap items-baseline justify-between gap-4 border-b border-rule pb-4">
            <h2 className="text-2xl font-light tracking-tight text-ink">Todos sus resultados</h2>
            <div className="flex flex-wrap gap-2">
              {FILTROS.map((f) => (
                <button
                  key={f.k}
                  type="button"
                  onClick={() => setFiltro(f.k)}
                  className={`rounded-full border px-3.5 py-1.5 text-[11px] uppercase tracking-[0.12em] transition-colors duration-300 ${
                    filtro === f.k ? "border-optimal bg-optimal text-primary-foreground" : "border-rule text-ink-muted hover:border-ink/20 hover:text-ink"
                  }`}
                >
                  {f.l}
                </button>
              ))}
            </div>
          </div>
          {grupos.map(([nombre, items]) => (
            <Categoria key={nombre} nombre={nombre} items={items} onSelect={setElegido} />
          ))}
          {grupos.length === 0 && <p className="mt-6 text-sm text-ink-muted">No hay resultados en este filtro.</p>}
        </section>
        <PieLegal />
      </div>
      <DetalleResultado r={elegido} onClose={() => setElegido(null)} />
    </main>
  );
}
