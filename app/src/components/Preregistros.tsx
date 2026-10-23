import { useCallback, useEffect, useMemo, useState } from "react";
import { supabase } from "@/lib/sesion";
import C from "@/lib/contenido.json";

/**
 * Panel de la preventa (solo el equipo): cuántos se inscribieron, de dónde llegan (?ref=), sus metas y "Otro",
 * la lista completa para el seguimiento por WhatsApp, descarga en CSV y "Pasar a cliente" (sigue el flujo con pago).
 */
interface Fila {
  id: string;
  nombre: string;
  correo: string | null;
  celular_whatsapp: string;
  fecha_nacimiento: string;
  sexo: string | null;
  localidad: string;
  objetivos: string[];
  objetivo_otro: string | null;
  alergias: string[];
  dieta: string | null;
  quiere_prueba: boolean;
  acepta_contacto: boolean;
  fuente: string | null;
  referido_por: string | null;
  codigo: string;
  estado: "registrado" | "cliente" | "baja";
  prueba_dia: number;
  anticipo_estado: string | null;
  creado: string;
}

const META: Record<string, string> = { ...Object.fromEntries(C.objetivos.map((o) => [o.id, o.nombre])), otro: "Otro" };
const ESTADO: Record<string, string> = { registrado: "Pre-registrado", cliente: "Cliente", baja: "De baja" };

function edad(fecha: string) {
  const n = new Date(fecha);
  const h = new Date();
  return h.getFullYear() - n.getFullYear() - (h < new Date(h.getFullYear(), n.getMonth(), n.getDate()) ? 1 : 0);
}

/** Cuenta cuántas veces aparece cada valor, de mayor a menor. */
function contar(valores: string[]) {
  const m = new Map<string, number>();
  for (const v of valores) m.set(v, (m.get(v) ?? 0) + 1);
  return [...m.entries()].sort((a, b) => b[1] - a[1]);
}

function Cifra({ valor, texto }: { valor: number | string; texto: string }) {
  return (
    <div className="rounded-2xl bg-surface p-4">
      <p className="text-3xl font-light text-ink">{valor}</p>
      <p className="mt-1 text-xs text-ink-muted">{texto}</p>
    </div>
  );
}

function Barras({ titulo, datos }: { titulo: string; datos: [string, number][] }) {
  const max = Math.max(1, ...datos.map((d) => d[1]));
  return (
    <div className="rounded-2xl border border-rule p-4">
      <p className="text-sm text-ink">{titulo}</p>
      {datos.length === 0 && <p className="mt-3 text-xs text-ink-faint">Sin datos todavía.</p>}
      <div className="mt-3 space-y-2">
        {datos.slice(0, 12).map(([k, n]) => (
          <div key={k} className="text-xs">
            <div className="flex justify-between gap-3 text-ink-muted">
              <span className="truncate">{k}</span>
              <span className="tabular-nums text-ink">{n}</span>
            </div>
            <div className="mt-1 h-1.5 rounded-full bg-rule">
              <div className="h-1.5 rounded-full bg-optimal" style={{ width: `${(n / max) * 100}%` }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function csv(filas: Fila[]) {
  const cols: [string, (f: Fila) => string | number][] = [
    ["fecha", (f) => f.creado.slice(0, 10)],
    ["nombre", (f) => f.nombre],
    ["celular", (f) => f.celular_whatsapp],
    ["correo", (f) => f.correo ?? ""],
    ["edad", (f) => edad(f.fecha_nacimiento)],
    ["sexo", (f) => f.sexo ?? ""],
    ["localidad", (f) => f.localidad],
    ["metas", (f) => f.objetivos.map((o) => META[o] ?? o).join(" | ")],
    ["otra_meta", (f) => f.objetivo_otro ?? ""],
    ["semana_prueba", (f) => (f.quiere_prueba ? "si" : "no")],
    ["acepta_contacto", (f) => (f.acepta_contacto ? "si" : "no")],
    ["alergias", (f) => f.alergias.join(" | ")],
    ["dieta", (f) => f.dieta ?? ""],
    ["origen", (f) => f.fuente ?? ""],
    ["codigo", (f) => f.codigo],
    ["estado", (f) => f.estado],
    ["anticipo", (f) => f.anticipo_estado ?? ""],
  ];
  const celda = (v: string | number) => `"${String(v).replace(/"/g, '""')}"`;
  const texto = [cols.map((c) => c[0]).join(","), ...filas.map((f) => cols.map((c) => celda(c[1](f))).join(","))].join("\n");
  const url = URL.createObjectURL(new Blob(["﻿" + texto], { type: "text/csv;charset=utf-8" }));
  const a = document.createElement("a");
  a.href = url;
  a.download = `preregistros-saludly-${new Date().toISOString().slice(0, 10)}.csv`;
  a.click();
  URL.revokeObjectURL(url);
}

export function Preregistros() {
  const [filas, setFilas] = useState<Fila[] | null>(null);
  const [buscar, setBuscar] = useState("");
  const [ocupado, setOcupado] = useState<string | null>(null);

  const cargar = useCallback(async () => {
    const { data } = await supabase.from("preregistros").select("*").order("creado", { ascending: false });
    setFilas((data as Fila[] | null) ?? []);
  }, []);
  useEffect(() => void cargar(), [cargar]);

  const r = useMemo(() => {
    const f = filas ?? [];
    const hoy = new Date().toISOString().slice(0, 10);
    const hace7 = Date.now() - 7 * 864e5;
    return {
      total: f.length,
      hoy: f.filter((x) => x.creado.slice(0, 10) === hoy).length,
      semana: f.filter((x) => new Date(x.creado).getTime() >= hace7).length,
      prueba: f.filter((x) => x.quiere_prueba).length,
      anticipos: f.filter((x) => x.anticipo_estado === "pagado").length,
      clientes: f.filter((x) => x.estado === "cliente").length,
      origen: contar(f.map((x) => (x.referido_por ? "Invitado por un amigo" : (x.fuente ?? "Sin origen")))),
      metas: contar(f.flatMap((x) => x.objetivos.map((o) => META[o] ?? o))),
      localidades: contar(f.map((x) => x.localidad)),
      dias: contar(f.map((x) => x.creado.slice(0, 10))).sort((a, b) => b[0].localeCompare(a[0])),
      otros: f.filter((x) => x.objetivo_otro),
    };
  }, [filas]);

  const visibles = (filas ?? []).filter((f) => {
    const q = buscar.trim().toLowerCase();
    return !q || [f.nombre, f.celular_whatsapp, f.correo ?? "", f.localidad, f.fuente ?? ""].some((v) => v.toLowerCase().includes(q));
  });

  const cambiarEstado = async (f: Fila, estado: Fila["estado"]) => {
    if (estado === "cliente" && !window.confirm(`¿Pasar a ${f.nombre} a cliente? Al entrar verá el registro completo con el pago.`)) return;
    setOcupado(f.id);
    await supabase.rpc("preregistro_estado", { p_id: f.id, p_estado: estado });
    setOcupado(null);
    void cargar();
  };

  if (filas === null) return <p className="mt-8 text-sm text-ink-muted">Cargando…</p>;

  return (
    <section className="mt-10">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-3xl font-light tracking-tight text-ink">Pre-registros</h1>
          <p className="mt-2 text-sm text-ink-muted">Personas inscritas en la preventa. Comparte enlaces con ?ref=nombre-del-grupo para saber de dónde llegan.</p>
        </div>
        <button type="button" onClick={() => csv(filas)} disabled={filas.length === 0} className="rounded-full border border-rule px-5 py-2.5 text-sm text-ink disabled:opacity-40">
          Descargar CSV
        </button>
      </div>

      <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
        <Cifra valor={r.total} texto="Inscritos" />
        <Cifra valor={r.hoy} texto="Hoy" />
        <Cifra valor={r.semana} texto="Últimos 7 días" />
        <Cifra valor={r.prueba} texto="Quieren la semana de prueba" />
        <Cifra valor={r.anticipos} texto="Anticipos pagados" />
        <Cifra valor={r.clientes} texto="Pasados a cliente" />
      </div>

      <div className="mt-4 grid gap-3 md:grid-cols-2 lg:grid-cols-4">
        <Barras titulo="De dónde llegan" datos={r.origen} />
        <Barras titulo="Metas más elegidas" datos={r.metas} />
        <Barras titulo="Localidades" datos={r.localidades} />
        <Barras titulo="Inscritos por día" datos={r.dias} />
      </div>

      {r.otros.length > 0 && (
        <div className="mt-4 rounded-2xl border border-rule p-4">
          <p className="text-sm text-ink">Lo que escribieron en «Otro» ({r.otros.length})</p>
          <ul className="mt-2 space-y-1 text-sm text-ink-muted">
            {r.otros.map((f) => (
              <li key={f.id}>
                «{f.objetivo_otro}» <span className="text-xs text-ink-faint">· {f.nombre.split(" ")[0]}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      <input value={buscar} onChange={(e) => setBuscar(e.target.value)} placeholder="Buscar por nombre, celular, correo, localidad u origen" className="mt-6 w-full rounded-2xl border border-rule bg-background px-4 py-3 text-sm text-ink outline-none focus:border-optimal" />

      <div className="mt-3 space-y-2">
        {filas.length === 0 && <p className="text-sm text-ink-muted">Todavía no hay inscritos.</p>}
        {visibles.map((f) => (
          <div key={f.id} className="flex flex-wrap items-start justify-between gap-3 rounded-2xl border border-rule p-4">
            <div className="min-w-0">
              <p className="text-base text-ink">{f.nombre}</p>
              <p className="text-xs text-ink-muted">
                {edad(f.fecha_nacimiento)} años{f.sexo ? ` · ${f.sexo}` : ""} · {f.localidad} ·{" "}
                <a href={`https://wa.me/${f.celular_whatsapp}`} target="_blank" rel="noreferrer" className="text-optimal underline-offset-2 hover:underline">
                  +{f.celular_whatsapp}
                </a>
                {f.correo ? ` · ${f.correo}` : ""}
              </p>
              <p className="mt-1 text-xs text-ink-muted">
                {f.objetivos.map((o) => (o === "otro" ? `Otro: ${f.objetivo_otro}` : META[o] ?? o)).join(" · ")}
              </p>
              <p className="mt-1 font-mono text-[10px] text-ink-faint">
                {new Date(f.creado).toLocaleString("es-CO", { dateStyle: "medium", timeStyle: "short" })} · origen {f.referido_por ? `amigo ${f.referido_por}` : (f.fuente ?? "—")} · código {f.codigo}
                {f.quiere_prueba ? ` · prueba día ${f.prueba_dia}/7` : " · sin prueba"}
                {f.acepta_contacto ? "" : " · NO acepta contacto"}
                {f.anticipo_estado ? ` · anticipo ${f.anticipo_estado}` : ""}
              </p>
            </div>
            <div className="flex items-center gap-2">
              <span className={`rounded-full px-3 py-1 text-xs ${f.estado === "cliente" ? "bg-optimal-soft text-optimal" : "bg-surface text-ink-muted"}`}>{ESTADO[f.estado]}</span>
              {f.estado !== "cliente" && (
                <button type="button" disabled={ocupado === f.id} onClick={() => void cambiarEstado(f, "cliente")} className="rounded-full bg-optimal px-4 py-2 text-xs text-primary-foreground disabled:opacity-40">
                  Pasar a cliente
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
