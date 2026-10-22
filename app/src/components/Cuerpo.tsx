import type { CSSProperties } from "react";
import cuerpoHombre from "@/assets/body.png";
import cuerpoMujer from "@/assets/body-female.png";
import { ETIQUETA, PLAZO, PUNTO, SISTEMAS, TEXTO, estadoDe, estadoDeSistema, fechaLarga } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";

export function Cuerpo() {
  const { informe } = useInforme();
  const res = informe.resultados.filter((r) => r.estado !== "no_medido");
  const calculados = res.filter((r) => r.estado === "calculado").length;
  const cuenta = (e: string) => res.filter((r) => estadoDe(r.clase) === e).length;
  const enRango = cuenta("en_rango");
  const fuera = cuenta("fuera");
  const pronto = cuenta("pronto");
  const total = res.length || 1;
  const pct = (n: number) => (n / total) * 100;
  const mujer = informe.perfil.sexo === "mujer"; // la silueta sale del sexo del informe (PDF), sin selector
  const sistemas = SISTEMAS.map((s) => ({ ...s, estado: estadoDeSistema(res, s.secciones) })).filter((s) => s.estado);
  const sistemasEnRango = sistemas.filter((s) => s.estado === "en_rango").length;

  return (
    <section className="relative overflow-hidden pb-8 pt-6">
      <div className="grid items-center gap-10 lg:grid-cols-[1fr_auto_1fr]">
        <div className="rise order-2 lg:order-1">
          <p className="font-mono text-[11px] uppercase tracking-[0.24em] text-optimal">Tu informe · revisado por un médico</p>
          <h1 className="mt-3 text-4xl font-light leading-[1.08] tracking-tight text-ink sm:text-5xl">
            Todo tu cuerpo,
            <br />
            medido.
          </h1>
          <p className="mt-4 max-w-sm text-sm leading-relaxed text-ink-muted">
            {res.length} biomarcadores analizados: {res.length - calculados} de tu laboratorio, cada uno frente a su rango de referencia, y {calculados} calculados por Saludly.
          </p>
          <div className="mt-8 max-w-sm rounded-3xl border border-rule bg-background px-6 py-5 shadow-[0_16px_40px_-32px_rgba(20,30,60,0.55)]">
            <dl className="flex flex-wrap items-start gap-x-8 gap-y-4">
              {[
                { n: res.length, l: "Total", c: "text-ink" },
                { n: enRango, l: ETIQUETA.en_rango, c: TEXTO.en_rango },
                { n: fuera, l: ETIQUETA.fuera, c: TEXTO.fuera },
                ...(pronto ? [{ n: pronto, l: ETIQUETA.pronto, c: TEXTO.pronto }] : []),
              ].map((s) => (
                <div key={s.l}>
                  <dd className={`font-mono text-2xl tabular-nums ${s.c}`}>{s.n}</dd>
                  <dt className="mt-1 text-[12px] text-ink-faint">{s.l}</dt>
                </div>
              ))}
            </dl>
            <div className="mt-5 flex gap-1.5">
              <span className="h-1.5 rounded-full bg-optimal" style={{ width: `${pct(enRango)}%` }} />
              <span className="h-1.5 rounded-full bg-attention" style={{ width: `${pct(fuera)}%` }} />
              {pronto > 0 && <span className="h-1.5 rounded-full bg-critical" style={{ width: `${pct(pronto)}%` }} />}
            </div>
          </div>
        </div>

        <div className="rise order-1 lg:order-2" style={{ "--rise-delay": "0.1s" } as CSSProperties}>
          <div className="relative mx-auto w-[240px] sm:w-[300px]">
            <div className="breathe absolute inset-x-6 bottom-[8%] top-[12%] rounded-full bg-optimal-soft blur-3xl" />
            <img
              src={mujer ? cuerpoMujer : cuerpoHombre}
              alt={`Figura de un cuerpo ${mujer ? "femenino" : "masculino"} con los sistemas analizados`}
              width={768}
              height={1280}
              className="relative w-full select-none"
              draggable={false}
            />
            {sistemas.map((s) => (
              <div
                key={s.nombre}
                className="absolute flex items-center gap-2"
                style={{
                  top: s.top,
                  left: s.left,
                  transform: s.lado === "izq" ? "translate(-100%, -50%)" : "translateY(-50%)",
                  flexDirection: s.lado === "izq" ? "row-reverse" : "row",
                }}
              >
                <span className="relative flex h-2 w-2">
                  {s.estado !== "en_rango" && <span className={`absolute inline-flex h-full w-full animate-ping rounded-full opacity-60 ${PUNTO[s.estado!]}`} />}
                  <span className={`relative inline-flex h-2 w-2 rounded-full ${PUNTO[s.estado!]}`} />
                </span>
                <span className="whitespace-nowrap text-[10px] uppercase tracking-[0.16em] text-ink-faint">{s.nombre}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="rise order-3 hidden lg:block" style={{ "--rise-delay": "0.2s" } as CSSProperties}>
          <div className="ml-auto max-w-[240px] space-y-6 text-right">
            {[
              { k: "Sistemas en rango", v: `${sistemasEnRango} de ${sistemas.length}` },
              { k: "Fecha de la toma", v: fechaLarga(informe.fecha_toma) },
              { k: "Siguiente paso", v: PLAZO[informe.escalamiento_maximo] },
              { k: "Tus metas", v: informe.objetivos.map((o) => o.nombre).join(" · ") || "—" },
            ].map((r) => (
              <div key={r.k}>
                <div className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">{r.k}</div>
                <div className="mt-1 text-sm leading-snug text-ink">{r.v}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
