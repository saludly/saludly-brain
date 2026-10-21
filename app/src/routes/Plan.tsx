import { useState } from "react";
import { Dumbbell, Moon, Salad, Stethoscope, UtensilsCrossed } from "lucide-react";
import { Marca, PieLegal } from "@/components/Comunes";
import { Retenido } from "@/routes/Retenido";
import { useInforme } from "@/lib/contexto";
import type { Recomendacion, TipoRecomendacion } from "@/lib/informe";

const PASOS: { id: string; n: string; tab: string; titulo: string; icono: typeof Salad; tipos: TipoRecomendacion[]; intro: string }[] = [
  {
    id: "alimentacion",
    n: "01",
    tab: "Alimentación e hidratación",
    titulo: "Lo que comes y lo que tomas",
    icono: Salad,
    tipos: ["alimentacion", "hidratacion"],
    intro: "Cambios pequeños en tu plato y en tus bebidas, elegidos según tus resultados y tus metas.",
  },
  {
    id: "movimiento",
    n: "02",
    tab: "Movimiento y descanso",
    titulo: "Actividad, sueño y tiempo para ti",
    icono: Moon,
    tipos: ["actividad", "sueno", "actividades_saludables"],
    intro: "Moverse y dormir bien mejoran a la vez el azúcar, el colesterol, la presión y el ánimo.",
  },
  {
    id: "controles",
    n: "03",
    tab: "Controles y hábitos",
    titulo: "Citas, controles y hábitos",
    icono: Stethoscope,
    tipos: ["controles", "habitos", "vitaminas_suplementos", "terapias"],
    intro: "Lo que conviene revisar con tu médico y los hábitos que protegen tus resultados.",
  },
];

function TarjetaRec({ r }: { r: Recomendacion }) {
  return (
    <div className="rounded-2xl border border-rule bg-background p-5 transition-colors duration-300 hover:border-ink/15">
      {r.requiere_consulta_previa && (
        <span className="mb-2 inline-block rounded-full bg-attention-soft px-2 py-0.5 text-[9px] uppercase tracking-[0.12em] text-attention">
          Consulta antes con tu médico
        </span>
      )}
      <p className="text-sm font-normal text-ink">{r.titulo}</p>
      <p className="mt-1.5 text-sm leading-relaxed text-ink-muted">{r.texto}</p>
      {r.meta && (
        <p className="mt-3 border-t border-rule pt-3 text-xs leading-relaxed text-ink">
          <span className="font-mono text-[10px] uppercase tracking-[0.12em] text-optimal">Meta de la semana · </span>
          {r.meta}
        </p>
      )}
    </div>
  );
}

const COMIDA: Record<string, string> = { desayuno: "Desayuno", almuerzo: "Almuerzo", cena: "Cena", merienda: "Merienda" };

export function Plan() {
  const { informe } = useInforme();
  const [activo, setActivo] = useState(0);
  if (informe.estado === "retenido_hasta_llamada") return <Retenido />;
  const recs = informe.paciente.que_puedes_hacer;
  const paso = PASOS[activo] ?? PASOS[0]!;
  const Icono = paso.icono;
  const deEste = recs.filter((r) => paso.tipos.includes(r.tipo));
  const meta = informe.nutricion.meta_diaria;

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-4xl px-4 py-8 sm:px-10">
        <Marca derecha="Mi plan" />
        <p className="mt-10 font-mono text-[10px] uppercase tracking-[0.2em] text-ink-faint">Tu plan en 3 pasos</p>
        <h1 className="mt-2 text-3xl font-light tracking-tight text-ink">Plan Saludly</h1>
        <p className="mt-3 max-w-xl text-sm leading-relaxed text-ink-muted">
          Recomendaciones elegidas según tus resultados y ordenadas según tus metas: {informe.objetivos.map((o) => o.nombre.toLowerCase()).join(", ")}.
        </p>
        {informe.paciente.nota_alimentacion && (
          <p className="mt-4 max-w-2xl rounded-2xl bg-optimal-soft p-4 text-sm leading-relaxed text-ink">{informe.paciente.nota_alimentacion}</p>
        )}

        <div className="mt-8 grid grid-cols-1 gap-2 sm:grid-cols-3">
          {PASOS.map((s, idx) => (
            <button
              key={s.id}
              type="button"
              onClick={() => setActivo(idx)}
              className={`rounded-2xl border p-4 text-left transition-all duration-300 ${
                idx === activo ? "border-ink/20 bg-ink text-background shadow-[0_16px_36px_-18px_rgba(0,0,0,0.45)]" : "border-rule bg-background hover:border-ink/15"
              }`}
            >
              <span className={`font-mono text-[10px] uppercase tracking-[0.16em] ${idx === activo ? "text-background/60" : "text-ink-faint"}`}>Paso {s.n}</span>
              <span className={`mt-1 block text-sm font-light tracking-tight ${idx === activo ? "text-background" : "text-ink"}`}>{s.tab}</span>
            </button>
          ))}
        </div>

        <section className="mt-6 rounded-3xl border border-rule bg-surface p-6 sm:p-8">
          <div className="flex items-center gap-3">
            <span className="grid h-11 w-11 shrink-0 place-items-center rounded-2xl bg-primary/10 text-primary">
              <Icono className="h-5 w-5" strokeWidth={1.6} />
            </span>
            <h2 className="min-w-0 text-xl font-light tracking-tight text-ink">{paso.titulo}</h2>
          </div>
          <p className="mt-4 max-w-2xl text-sm leading-relaxed text-ink-muted">{paso.intro}</p>
          <div className="mt-6 grid gap-2.5 sm:grid-cols-2">
            {deEste.map((r) => (
              <TarjetaRec key={r.recomendacion_id} r={r} />
            ))}
            {deEste.length === 0 && <p className="text-sm text-ink-muted">Por ahora no hay recomendaciones de este tipo para ti.</p>}
          </div>
        </section>

        <section className="mt-12">
          <div className="flex items-baseline justify-between border-b border-rule pb-4">
            <h2 className="text-2xl font-light tracking-tight text-ink">Tus recetas de la semana</h2>
            <UtensilsCrossed className="h-4 w-4 text-ink-faint" />
          </div>
          <p className="mt-4 max-w-2xl text-sm leading-relaxed text-ink-muted">
            Te enviaremos una receta cada día por WhatsApp.
            {meta.personalizada && meta.kcal
              ? ` Tu meta orientativa es de unas ${meta.kcal.toLocaleString("es-CO")} kcal y ${meta.proteina_g} g de proteína al día.`
              : ""}{" "}
            {meta.notas[0]}
          </p>
          <div className="mt-6 grid gap-2.5 sm:grid-cols-2">
            {informe.nutricion.plan.map((d) => (
              <div key={d.dia} className="flex gap-4 rounded-2xl border border-rule bg-background p-5">
                <span className="font-mono text-sm text-ink-faint">{String(d.dia).padStart(2, "0")}</span>
                <div className="min-w-0">
                  <p className="text-[10px] uppercase tracking-[0.14em] text-optimal">{COMIDA[d.tiempo_comida]}</p>
                  <p className="mt-1 text-sm text-ink">{d.nombre}</p>
                  <p className="mt-1 font-mono text-[11px] text-ink-faint">
                    {Math.round(d.nutrientes_porcion.kcal)} kcal · {Math.round(d.nutrientes_porcion.proteina_g)} g proteína · {d.tiempo_min ?? "—"} min
                  </p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="mt-6 grid grid-cols-1 gap-2.5 sm:grid-cols-3">
          {[
            { icono: Dumbbell, l: "Actividad", d: informe.perfil.nivel_actividad.replace(" (supuesto)", "") },
            { icono: Moon, l: "Sueño", d: "7 a 9 horas" },
            { icono: Stethoscope, l: "Siguiente control", d: informe.escalamiento_maximo >= 2 ? "Consulta en 2 a 4 semanas" : "En tu próximo control" },
          ].map((x) => (
            <div key={x.l} className="flex items-center gap-3 rounded-2xl border border-rule bg-background p-5">
              <span className="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-optimal/10 text-optimal">
                <x.icono className="h-4 w-4" strokeWidth={1.8} />
              </span>
              <div className="min-w-0">
                <p className="truncate text-sm font-normal text-ink">{x.l}</p>
                <p className="truncate text-xs capitalize text-ink-muted">{x.d}</p>
              </div>
            </div>
          ))}
        </section>
        <PieLegal />
      </div>
    </main>
  );
}
