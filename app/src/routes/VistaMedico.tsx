import { useEffect, useState } from "react";
import { useParams } from "@tanstack/react-router";
import { Marca } from "@/components/Comunes";

/**
 * Lo que ve el médico del paciente al abrir app.saludly.online/m/<enlace> (sin cuenta: el enlace es la llave).
 * Los datos vienen de la función vista-medico de Supabase: solo lo clínico, sin textos internos de Saludly.
 * Primero lo que está fuera de rango y los hallazgos; después todos los resultados por sección.
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type Vista = any;

const FUERA = new Set(["bajo", "alto", "critico", "alterado", "limitrofe"]);
const CLASE: Record<string, string> = { bajo: "Bajo", alto: "Alto", critico: "Crítico", alterado: "Alterado", limitrofe: "Limítrofe", en_rango: "En rango" };
const COINCIDENCIA: Record<string, string> = { alta: "Coincidencia alta", moderada: "Coincidencia moderada", baja: "Coincidencia baja" };

function fecha(iso?: string | null) {
  if (!iso) return "—";
  const d = new Date(iso.length === 10 ? `${iso}T12:00:00` : iso);
  return d.toLocaleDateString("es-CO", { day: "numeric", month: "long", year: "numeric" });
}

function Dato({ k, v }: { k: string; v: React.ReactNode }) {
  return (
    <div>
      <dt className="text-[10px] uppercase tracking-[0.14em] text-ink-faint">{k}</dt>
      <dd className="mt-0.5 text-sm text-ink">{v ?? "—"}</dd>
    </div>
  );
}

function Fila({ r }: { r: Vista }) {
  const fuera = FUERA.has(r.clase);
  return (
    <tr className={`border-b border-rule align-top ${fuera ? "bg-attention-soft" : ""}`}>
      <td className="py-2 pr-3 text-ink">{r.nombre}</td>
      <td className={`py-2 pr-3 tabular-nums ${fuera ? "font-semibold text-attention" : "text-ink"}`}>
        {r.valor ?? "—"} <span className="text-xs font-normal text-ink-faint">{r.unidad}</span>
      </td>
      <td className="py-2 pr-3 text-xs text-ink-muted">{r.intervalo ?? "—"}</td>
      <td className={`py-2 text-xs ${fuera ? "font-medium text-attention" : "text-ink-faint"}`}>{CLASE[r.clase] ?? r.estado}</td>
    </tr>
  );
}

function Tabla({ filas }: { filas: Vista[] }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-[520px] text-left text-sm">
        <thead>
          <tr className="border-b border-rule text-[10px] uppercase tracking-[0.12em] text-ink-faint">
            <th className="py-2 pr-3 font-normal">Prueba</th>
            <th className="py-2 pr-3 font-normal">Resultado</th>
            <th className="py-2 pr-3 font-normal">Intervalo del laboratorio</th>
            <th className="py-2 font-normal">Estado</th>
          </tr>
        </thead>
        <tbody>
          {filas.map((r, i) => (
            <Fila key={i} r={r} />
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Seccion({ titulo, children }: { titulo: string; children: React.ReactNode }) {
  return (
    <section className="mt-10">
      <h2 className="text-[11px] uppercase tracking-[0.18em] text-ink-faint">{titulo}</h2>
      <div className="mt-3">{children}</div>
    </section>
  );
}

const lista = (x: unknown) => (Array.isArray(x) && x.length ? x.join(", ") : null);

export function VistaMedico() {
  const { slug } = useParams({ strict: false }) as { slug: string };
  const [v, setV] = useState<Vista | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_SUPABASE_URL}/functions/v1/vista-medico?e=${encodeURIComponent(slug)}`)
      .then((r) => (r.ok ? r.json() : Promise.reject()))
      .then(setV)
      .catch(() => setError(true));
  }, [slug]);

  if (error)
    return (
      <main className="flex min-h-screen items-center justify-center bg-background px-6 text-center">
        <p className="max-w-sm text-sm text-ink-muted">Este enlace no es válido o ya no está activo. Pídele al paciente uno nuevo desde su app de Saludly.</p>
      </main>
    );
  if (!v) return <main className="min-h-screen bg-background" />;

  const fuera = v.resultados.filter((r: Vista) => FUERA.has(r.clase));
  const secciones = new Map<string, Vista[]>();
  for (const r of v.resultados) secciones.set(r.seccion ?? "Otros", [...(secciones.get(r.seccion ?? "Otros") ?? []), r]);
  const pr = v.paciente_reporta ?? {};
  const med = v.medidas ?? {};

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-4xl px-5 pb-20 pt-8">
        <Marca derecha="Resumen para el médico" />

        <header className="mt-10 rounded-3xl border border-rule p-6">
          <h1 className="text-2xl font-light tracking-tight text-ink">{v.paciente.nombre}</h1>
          <dl className="mt-4 grid grid-cols-2 gap-4 sm:grid-cols-4">
            <Dato k="Edad" v={`${v.paciente.edad} años`} />
            <Dato k="Sexo" v={v.paciente.sexo === "hombre" ? "Masculino" : "Femenino"} />
            <Dato k="Documento" v={v.paciente.documento} />
            <Dato k="Celular" v={v.paciente.celular} />
            <Dato k="Toma de la muestra" v={fecha(v.informe.fecha_toma)} />
            <Dato k="Orden" v={v.informe.orden} />
            <Dato k="Revisado" v={fecha(v.informe.aprobado)} />
            <Dato k="Ciudad" v={v.informe.ciudad} />
          </dl>
        </header>

        <Seccion titulo="Medidas de la visita">
          <dl className="grid grid-cols-2 gap-4 sm:grid-cols-5">
            <Dato k="Presión" v={med.presion_sistolica ? `${med.presion_sistolica}/${med.presion_diastolica} mmHg` : null} />
            <Dato k="Peso" v={med.peso_kg ? `${med.peso_kg} kg` : null} />
            <Dato k="Talla" v={med.talla_m ? `${med.talla_m} m` : null} />
            <Dato k="IMC" v={med.imc} />
            <Dato k="Cintura" v={med.cintura_cm ? `${med.cintura_cm} cm` : null} />
          </dl>
        </Seccion>

        <Seccion titulo={`Fuera de rango (${fuera.length} de ${v.resultados.length})`}>
          {fuera.length ? <Tabla filas={fuera} /> : <p className="text-sm text-ink-muted">Todos los resultados están dentro del intervalo del laboratorio.</p>}
        </Seccion>

        {(v.hallazgos.length > 0 || v.condiciones.length > 0) && (
          <Seccion titulo="Hallazgos y condiciones">
            <div className="space-y-3">
              {v.hallazgos.map((h: Vista, i: number) => (
                <article key={`h${i}`} className="rounded-2xl border border-rule p-4">
                  <p className="text-sm font-medium text-ink">{h.nombre}</p>
                  <p className="mt-1 text-xs text-ink-muted">
                    {COINCIDENCIA[h.coincidencia] ?? "—"}
                    {h.fuente ? ` · ${h.fuente}` : ""}
                  </p>
                </article>
              ))}
              {v.condiciones.map((c: Vista, i: number) => (
                <article key={`c${i}`} className="rounded-2xl border border-rule p-4">
                  <p className="text-sm font-medium text-ink">
                    {c.nombre}
                    {c.severidad ? <span className="font-normal text-ink-muted"> · {c.severidad}</span> : null}
                  </p>
                  <p className="mt-1 text-xs text-ink-muted">
                    {COINCIDENCIA[c.coincidencia] ?? "—"}
                    {c.criterios.length ? ` · Criterios: ${c.criterios.join(", ")}` : ""}
                  </p>
                  {Object.keys(c.datos).length > 0 && (
                    <p className="mt-1 text-xs text-ink-muted">
                      {Object.entries(c.datos)
                        .map(([k, x]) => `${k.replace(/_/g, " ")}: ${x}`)
                        .join(" · ")}
                    </p>
                  )}
                  {c.nota && <p className="mt-1 text-xs text-ink-muted">{c.nota}</p>}
                  {c.guias.length > 0 && <p className="mt-2 text-xs text-ink-faint">Guías: {c.guias.join("; ")}</p>}
                </article>
              ))}
            </div>
          </Seccion>
        )}

        {v.vigilar.length > 0 && (
          <Seccion titulo="Para vigilar">
            <ul className="space-y-1.5 text-sm text-ink">
              {v.vigilar.map((x: Vista, i: number) => (
                <li key={i}>
                  · {x.nombre}
                  {x.nota ? <span className="text-ink-muted"> ({x.nota})</span> : null}
                </li>
              ))}
            </ul>
          </Seccion>
        )}

        <Seccion titulo="Lo que reporta el paciente">
          <dl className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            <Dato k="Alergias" v={[lista(pr.alergias), pr.alergias_otras].filter(Boolean).join(", ") || "Ninguna"} />
            <Dato k="Medicamentos" v={[lista(pr.medicamentos), pr.medicamentos_otros].filter(Boolean).join(", ") || "Ninguno"} />
            <Dato k="Dieta" v={pr.dieta} />
            <Dato k="Tabaco" v={pr.fuma} />
            <Dato k="Alcohol" v={pr.alcohol} />
            <Dato k="Biotina" v={pr.toma_biotina === true ? "Sí" : pr.toma_biotina === false ? "No" : null} />
            <Dato k="Antecedentes familiares" v={lista(pr.antecedentes) ?? "Ninguno"} />
            <Dato k="Actividad física" v={pr.nivel_actividad} />
            {pr.embarazo && <Dato k="Embarazo" v={pr.embarazo} />}
          </dl>
          {v.datos_faltantes.length > 0 && <p className="mt-3 text-xs text-ink-faint">Datos que faltaron para el análisis: {v.datos_faltantes.join(", ")}.</p>}
        </Seccion>

        <Seccion titulo="Todos los resultados">
          <div className="space-y-8">
            {[...secciones].map(([s, filas]) => (
              <div key={s}>
                <h3 className="mb-2 text-sm text-ink">{s}</h3>
                <Tabla filas={filas} />
              </div>
            ))}
          </div>
        </Seccion>

        <p className="mt-12 text-xs leading-relaxed text-ink-faint">
          Resumen preventivo de Saludly a partir del PDF del laboratorio y de las medidas de la visita. No es un diagnóstico: la interpretación
          y las decisiones clínicas son del médico tratante. Los intervalos son los del laboratorio.
        </p>
      </div>
    </main>
  );
}
