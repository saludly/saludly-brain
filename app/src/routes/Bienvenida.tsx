import { useState } from "react";
import { Link, useNavigate } from "@tanstack/react-router";
import { Marca } from "@/components/Comunes";
import { Retenido } from "@/routes/Retenido";
import { PLAZO, SUAVE, TEXTO, estadoDe, estadoDeEscalamiento } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";

/**
 * Recorrido que ve el paciente al abrir su informe por primera vez (mismo formato del recorrido de Lovable).
 * Las preguntas (objetivos, actividad, cuestionario) van en la PWA antes de la visita, no aquí.
 */
const PASOS = ["Tu resumen", "Edad biológica", "Lo que está bien", "Lo que merece atención", "Tu plan"];

export function Bienvenida() {
  const { informe } = useInforme();
  const navigate = useNavigate();
  const [paso, setPaso] = useState(0);
  if (informe.estado === "retenido_hasta_llamada") return <Retenido />;

  const p = informe.paciente;
  // Solo los del laboratorio: los calculados por Saludly no tienen rango, así que no cuentan en "en rango".
  const res = informe.resultados.filter((r) => r.estado !== "no_medido" && r.estado !== "calculado");
  const enRango = res.filter((r) => estadoDe(r.clase) === "en_rango").length;
  const eb = informe.edad_biologica;
  const pasos = PASOS.filter((_, i) => i !== 1 || eb); // sin edad biológica, se salta ese paso
  const titulo = pasos[paso];
  const ultimo = paso === pasos.length - 1;
  const tresRecs = p.que_puedes_hacer.filter((r) => !r.requiere_consulta_previa).slice(0, 3);

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-3xl flex-col px-6 pb-32 pt-8 sm:px-10">
        <Marca derecha={`Paso ${paso + 1} / ${pasos.length}`} />
        <nav aria-label="Progreso" className="mt-8">
          <div className="flex gap-1.5">
            {pasos.map((l, i) => (
              <button
                key={l}
                type="button"
                aria-label={l}
                aria-current={i === paso}
                disabled={i > paso}
                onClick={() => setPaso(i)}
                className={`h-1.5 flex-1 rounded-full transition-colors duration-300 ${i <= paso ? "bg-optimal" : "bg-rule"} ${i > paso ? "cursor-default" : "cursor-pointer"}`}
              />
            ))}
          </div>
          <p className="mt-3 font-mono text-[10px] uppercase tracking-[0.18em] text-ink-faint">{titulo}</p>
        </nav>

        <section key={paso} className="rise mt-10 flex-1">
          {titulo === "Tu resumen" && (
            <div>
              <h1 className="text-3xl font-light tracking-tight text-ink sm:text-4xl">Tus resultados están listos.</h1>
              <p className="mt-4 max-w-xl text-base leading-relaxed text-ink-muted">{p.resumen}</p>
              <div className="mt-8 grid gap-3 sm:grid-cols-2">
                <div className="rounded-2xl bg-optimal p-6 text-primary-foreground">
                  <span className="text-[11px] uppercase tracking-[0.2em] text-primary-foreground/70">Resultados en rango</span>
                  <div className="mt-6 flex items-baseline gap-1">
                    <span className="font-mono text-6xl leading-none tabular-nums">{enRango}</span>
                    <span className="font-mono text-xl text-primary-foreground/60">/{res.length}</span>
                  </div>
                </div>
                <div className="rounded-2xl border border-rule p-6">
                  <span className="text-[11px] uppercase tracking-[0.2em] text-ink-faint">Puntos para atender</span>
                  <div className="mt-6 font-mono text-6xl leading-none tabular-nums text-attention">{p.lo_que_merece_atencion.length}</div>
                </div>
              </div>
            </div>
          )}

          {titulo === "Edad biológica" && eb && (
            <div>
              <h1 className="text-3xl font-light tracking-tight text-ink sm:text-4xl">Tu edad biológica estimada.</h1>
              <p className="mt-3 max-w-xl text-sm leading-relaxed text-ink-muted">
                No es la edad de tu cédula: es una estimación de cómo está funcionando tu cuerpo, calculada con 9 de tus resultados.
              </p>
              <div className="mt-8 rounded-2xl border border-rule p-6">
                <div className="flex items-baseline gap-1.5">
                  <span className="font-mono text-6xl leading-none tabular-nums text-optimal">{eb.phenoage.toLocaleString("es-CO")}</span>
                  <span className="text-xs text-ink-faint">años</span>
                </div>
                <p className="mt-3 text-sm text-ink-muted">
                  {eb.diferencia <= 0
                    ? `${Math.abs(eb.diferencia).toLocaleString("es-CO")} años menos que tu edad (${informe.perfil.edad}).`
                    : `${eb.diferencia.toLocaleString("es-CO")} años más que tu edad (${informe.perfil.edad}).`}
                </p>
              </div>
              <p className="mt-4 text-xs leading-relaxed text-ink-muted">
                Es una estimación, no un diagnóstico. La buena noticia: se mueve con el sueño, la actividad y la alimentación.
              </p>
            </div>
          )}

          {titulo === "Lo que está bien" && (
            <div>
              <h1 className="text-3xl font-light tracking-tight text-ink sm:text-4xl">Lo que está bien.</h1>
              <p className="mt-3 max-w-xl text-sm leading-relaxed text-ink-muted">Estos resultados son tu base. Mantenerlos cuesta mucho menos que recuperarlos.</p>
              <div className="mt-8 space-y-3">
                {p.lo_que_esta_bien.slice(0, 5).map((b) => (
                  <article key={b.grupo} className="rounded-2xl border border-rule bg-optimal-soft p-5">
                    <h2 className={`text-base ${TEXTO.en_rango}`}>{b.nombre ?? b.grupo}</h2>
                    <p className="mt-1.5 text-sm leading-relaxed text-ink-muted">{b.texto}</p>
                  </article>
                ))}
                {p.lo_que_esta_bien.length === 0 && <p className="text-sm text-ink-muted">En este informe no hay grupos completos en rango.</p>}
              </div>
            </div>
          )}

          {titulo === "Lo que merece atención" && (
            <div>
              <h1 className="text-3xl font-light tracking-tight text-ink sm:text-4xl">Lo que merece atención.</h1>
              <p className="mt-3 max-w-xl text-sm leading-relaxed text-ink-muted">
                Ninguno es un diagnóstico. Son señales para cuidar a tiempo, ordenadas de la más importante a la menos.
              </p>
              <div className="mt-8 space-y-3">
                {p.lo_que_merece_atencion.slice(0, 4).map((h) => (
                  <article key={h.hallazgo_id} className="rounded-2xl border border-rule p-5">
                    <span className={`rounded-full px-2 py-0.5 text-[9px] uppercase tracking-[0.12em] ${SUAVE[estadoDeEscalamiento(h.escalamiento)]}`}>{PLAZO[h.escalamiento]}</span>
                    <h2 className="mt-3 text-base text-ink">{h.titulo}</h2>
                    <p className="mt-1.5 text-sm leading-relaxed text-ink-muted">{h.por_que[0]}</p>
                  </article>
                ))}
              </div>
              {p.lo_que_merece_atencion.length > 4 && (
                <p className="mt-4 text-xs text-ink-muted">Y {p.lo_que_merece_atencion.length - 4} más en tu panel.</p>
              )}
            </div>
          )}

          {titulo === "Tu plan" && (
            <div>
              <h1 className="text-3xl font-light tracking-tight text-ink sm:text-4xl">Por dónde empezar.</h1>
              <p className="mt-3 max-w-xl text-sm leading-relaxed text-ink-muted">Tres cambios para esta semana, elegidos según tus resultados y tus metas.</p>
              <div className="mt-8 space-y-3">
                {tresRecs.map((r, i) => (
                  <article key={r.recomendacion_id} className="flex gap-4 rounded-2xl border border-rule p-5">
                    <span className="font-mono text-sm text-ink-faint">0{i + 1}</span>
                    <div>
                      <h2 className="text-base text-ink">{r.titulo}</h2>
                      <p className="mt-1.5 text-sm leading-relaxed text-ink-muted">{r.meta ?? r.texto}</p>
                    </div>
                  </article>
                ))}
              </div>
              <p className="mt-4 text-sm leading-relaxed text-ink-muted">
                Puedes ver tu{" "}
                <Link to="/plan" className="text-optimal underline-offset-4 hover:underline">
                  plan completo
                </Link>{" "}
                cuando entres a tu panel.
              </p>
            </div>
          )}
        </section>

        <p className="mt-10 text-xs text-ink-faint">Este informe es preventivo y no es un diagnóstico. Un médico de Saludly lo revisó.</p>
      </div>

      <div className="fixed inset-x-0 bottom-0 z-30 border-t border-rule bg-background/95 px-6 py-4 backdrop-blur sm:px-10">
        <div className="mx-auto flex max-w-3xl items-center gap-3">
          {paso > 0 && (
            <button
              type="button"
              onClick={() => setPaso((s) => s - 1)}
              className="rounded-full border border-rule px-5 py-4 text-sm text-ink-muted transition-colors hover:border-ink/20 hover:text-ink"
            >
              Atrás
            </button>
          )}
          <button
            type="button"
            onClick={() => (ultimo ? navigate({ to: "/panel" }) : setPaso((s) => s + 1))}
            className="flex-1 rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground transition-opacity duration-300"
          >
            {ultimo ? "Entrar a mi panel" : "Continuar"}
          </button>
        </div>
      </div>
    </main>
  );
}
