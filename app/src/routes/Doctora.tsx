/**
 * Línea GLP-1 · Panel de la doctora (Fase 6B), con el diseño del demo aprobado (formato iPad).
 * La doctora ve solo a sus pacientes (RLS: es_doctora_de); el equipo de Saludly ve a todas.
 * Por paciente: avance, gráficas por tema, análisis del laboratorio para aprobar, datos del tratamiento para confirmar
 * y la semana de recomendaciones (borrador de codigo/informe/recomendar_peso.py) para editar y publicar.
 */
import { useCallback, useEffect, useMemo, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import "@/peso.css";
import { Anillo, Tooltip } from "@/components/PesoComunes";
import { bullet, constancia, efectos, grafPeso, grafVel, pesas } from "@/lib/graficas";
import { supabase, useSesion } from "@/lib/sesion";
import type { Informe } from "@/lib/informe";
import {
  DIA_TEXTO, RANGO, actual, alertas, fmt, imc, normalizar, normalizarT, rfm, semanaDeTratamiento, serieSemanal,
  type Alerta, type ItemSemana, type Registro, type Semana, type Tratamiento,
} from "@/lib/peso";

interface Pac { id: string; nombre: string; edad: number; sexo: "hombre" | "mujer" }
interface FilaInforme { id: number; paciente_id: string; orden: string; informe: Informe; estado: string; creado: string }
interface Ficha { p: Pac; t: Tratamiento; regs: Registro[]; informes: FilaInforme[]; semana: Semana | null; alertas: Alerta[] }

const SECCION: Record<string, string> = { alta: "Requieren atención", media: "Requieren atención", info: "Para revisar", baja: "Para revisar", ok: "Al día" };
const LABS = ["hba1c", "glucose", "triglycerides", "hdl_c", "ldl_c", "alt", "tsh", "vitamin_b12"];

export function Doctora() {
  const s = useSesion();
  const navigate = useNavigate();
  const [fichas, setFichas] = useState<Ficha[]>([]);
  const [sel, setSel] = useState<string | null>(null);
  const [lim, setLim] = useState({ nombre: "", limite: 1.5, meseta: 4 });
  const [toast, setToast] = useState<string | null>(null);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    if (s.cargando) return;
    if (!s.sesion) void navigate({ to: "/entrar" });
    else if (!s.esDoctora && !s.esEquipo) void navigate({ to: "/" });
  }, [s, navigate]);

  const cargar = useCallback(async () => {
    const [md, tr] = await Promise.all([supabase.rpc("mi_doctora"), supabase.from("tratamientos_peso").select("*")]);
    const d = (md.data as { nombre: string; limite_semanal: number; semanas_meseta: number }[] | null)?.[0];
    const l = { nombre: d?.nombre ?? (s.esEquipo ? "equipo Saludly" : ""), limite: Number(d?.limite_semanal ?? 1.5), meseta: d?.semanas_meseta ?? 4 };
    setLim(l);
    const ts = ((tr.data as Tratamiento[] | null) ?? []).map(normalizarT);
    const ids = ts.map((t) => t.paciente_id);
    if (!ids.length) { setFichas([]); setCargando(false); return; }
    const [ps, rs, is, ss] = await Promise.all([
      supabase.from("pacientes").select("id, nombre, edad, sexo").in("id", ids),
      supabase.from("registros_peso").select("*").in("paciente_id", ids).order("fecha"),
      supabase.from("informes").select("id, paciente_id, orden, informe, estado, creado").in("paciente_id", ids).order("creado", { ascending: false }),
      supabase.from("semanas_peso").select("*").in("paciente_id", ids).order("semana", { ascending: false }),
    ]);
    const lista: Ficha[] = ts.map((t) => {
      const p = ((ps.data as Pac[] | null) ?? []).find((x) => x.id === t.paciente_id) ?? { id: t.paciente_id, nombre: "Paciente", edad: 0, sexo: "mujer" as const };
      const regs = ((rs.data as Registro[] | null) ?? []).filter((r) => r.paciente_id === t.paciente_id).map(normalizar);
      const informes = ((is.data as FilaInforme[] | null) ?? []).filter((x) => x.paciente_id === t.paciente_id);
      const semana = ((ss.data as Semana[] | null) ?? []).find((x) => x.paciente_id === t.paciente_id) ?? null;
      const al = alertas(t, regs, l.limite, l.meseta, informes.some((x) => x.estado === "en_revision"));
      if (semana?.estado === "borrador") al.push({ s: "info", corto: "Semana por publicar", texto: "Las recomendaciones de esta semana esperan su revisión." });
      return { p, t, regs, informes, semana, alertas: al.sort((a, b) => RANGO[a.s] - RANGO[b.s]) };
    });
    setFichas(lista);
    setSel((x) => x ?? lista.sort((a, b) => RANGO[a.alertas[0]?.s ?? "ok"] - RANGO[b.alertas[0]?.s ?? "ok"])[0]?.p.id ?? null);
    setCargando(false);
  }, [s.esEquipo]);
  useEffect(() => {
    if (!s.cargando && s.sesion) void cargar();
  }, [s.cargando, s.sesion, cargar]);

  const avisar = (t: string) => {
    setToast(t);
    setTimeout(() => setToast(null), 2600);
  };

  const orden = useMemo(() => [...fichas].sort((a, b) => RANGO[a.alertas[0]?.s ?? "ok"] - RANGO[b.alertas[0]?.s ?? "ok"]), [fichas]);
  const f = fichas.find((x) => x.p.id === sel) ?? null;
  const registraron = fichas.filter((x) => x.regs.some((r) => Date.now() - new Date(r.fecha + "T12:00:00").getTime() < 7 * 864e5)).length;
  const bajaron5 = fichas.filter((x) => (x.t.peso_inicio - actual(x.t, x.regs).peso) / x.t.peso_inicio >= 0.05).length;
  const atencion = fichas.filter((x) => (x.alertas[0] && RANGO[x.alertas[0].s] <= 1)).length;
  const fecha = new Date().toLocaleDateString("es-CO", { weekday: "long", day: "numeric", month: "long" });

  return (
    <main className="peso-app">
      <Tooltip />
      <div className="doc">
        <div className="d-cab">
          <div>
            <h1 className="d-titulo">Hola{lim.nombre ? `, ${lim.nombre}` : ""}</h1>
            <p className="d-sub" style={{ textTransform: "capitalize" }}>{fecha} · {fichas.length} {fichas.length === 1 ? "paciente" : "pacientes"} en tratamiento</p>
          </div>
          <button type="button" className="btn" onClick={() => void s.salir()}>Salir</button>
        </div>

        {cargando ? <div className="cd"><p className="nota" style={{ margin: 0 }}>Cargando…</p></div> : !fichas.length ? (
          <div className="cd"><h3>Todavía no tiene pacientes</h3><p className="nota" style={{ margin: 0 }}>Cuando una paciente se registre con su código, le aparece aquí.</p></div>
        ) : (
          <>
            <div className="cd">
              <h3>Esta semana</h3>
              <p className="nota">Su consultorio de un vistazo.</p>
              <div className="semana">
                <div className="it"><Anillo clase="mini" f={registraron / fichas.length} grande={`${registraron}/${fichas.length}`} /><div><b className="t">Registraron</b><span className="s">esta semana</span></div></div>
                <div className="it"><Anillo clase="mini" f={bajaron5 / fichas.length} grande={`${bajaron5}/${fichas.length}`} /><div><b className="t">Ya bajaron 5 %</b><span className="s">o más de su peso</span></div></div>
                <div className="it"><Anillo clase="mini" f={fichas.filter((x) => x.t.confirmado).length / fichas.length} grande={`${fichas.filter((x) => x.t.confirmado).length}/${fichas.length}`} /><div><b className="t">Datos confirmados</b><span className="s">por usted</span></div></div>
                <div className="it"><div className="alertas-n">{atencion}</div><div><b className="t">Necesitan atención</b><span className="s">hoy</span></div></div>
              </div>
            </div>
            <div className="d-grid">
              <nav className="cd d-lista" aria-label="Pacientes">
                {orden.map((x, i) => {
                  const a = x.alertas[0], sv = a?.s ?? "ok", sec = SECCION[sv];
                  const previo = i > 0 ? SECCION[orden[i - 1].alertas[0]?.s ?? "ok"] : null;
                  const fr = Math.max(0, Math.min(1, (x.t.peso_inicio - actual(x.t, x.regs).peso) / (x.t.peso_inicio - x.t.peso_meta)));
                  return (
                    <div key={x.p.id}>
                      {sec !== previo && <div className="d-sec">{sec}</div>}
                      <button type="button" className="pac" aria-current={x.p.id === sel} onClick={() => setSel(x.p.id)}>
                        <Anillo clase="mini" f={fr} grande={String(Math.round(fr * 100))} grosor={14} />
                        <span><b className="n">{x.p.nombre}</b><span className="e"><i className={`punto s-${sv}`} />{a?.corto ?? "Al día"}</span></span>
                        <svg viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"><path d="m3.5 1.5 3.5 3.5-3.5 3.5" /></svg>
                      </button>
                    </div>
                  );
                })}
              </nav>
              {f && <FichaPaciente f={f} lim={lim} correo={s.sesion?.user.email ?? ""} avisar={avisar} recargar={cargar} />}
            </div>
          </>
        )}
      </div>
      {toast && <div className="toast" role="status">{toast}</div>}
    </main>
  );
}

function FichaPaciente({ f, lim, correo, avisar, recargar }: { f: Ficha; lim: { limite: number; meseta: number }; correo: string; avisar: (t: string) => void; recargar: () => Promise<void> }) {
  const { p, t, regs } = f;
  const { peso, cintura } = actual(t, regs);
  const sem = semanaDeTratamiento(t);
  const serie = serieSemanal(t, regs);
  const perdido = t.peso_inicio - peso, total = t.peso_inicio - t.peso_meta;
  const mujer = p.sexo === "mujer";
  const pendiente = f.informes.find((x) => x.estado === "en_revision") ?? null;
  const aprobados = f.informes.filter((x) => x.estado === "aprobado");
  const inf = pendiente?.informe ?? aprobados[0]?.informe ?? null;
  const previo = pendiente ? aprobados[0]?.informe : aprobados[1]?.informe;
  const labs = (inf?.resultados ?? []).filter((r) => LABS.includes(r.biomarker_id) && typeof r.valor === "number").map((r) => {
    const a = previo?.resultados.find((x) => x.biomarker_id === r.biomarker_id);
    return { n: r.nombre.length > 14 ? r.biomarker_id.toUpperCase() : r.nombre, antes: typeof a?.valor === "number" ? a.valor : null, ahora: r.valor as number, u: r.unidad ?? "", ref: null, d: Number(r.valor) < 20 ? 1 : 0 };
  });
  const preguntas = regs.filter((r) => r.pregunta).slice(-3).map((r) => r.pregunta!);
  const a = f.alertas[0];

  const aprobar = async () => {
    if (!pendiente) return;
    const { error } = await supabase.from("informes").update({ estado: "aprobado", aprobado: new Date().toISOString(), aprobado_por: correo }).eq("id", pendiente.id);
    avisar(error ? "No se pudo aprobar. Intente de nuevo." : `Aprobado: ${p.nombre.split(" ")[0]} ya ve su análisis.`);
    await recargar();
  };
  const confirmar = async () => {
    const { error } = await supabase.from("tratamientos_peso").update({ confirmado: new Date().toISOString(), confirmado_por: correo }).eq("paciente_id", t.paciente_id);
    avisar(error ? "No se pudo confirmar." : "Datos del tratamiento confirmados.");
    await recargar();
  };

  return (
    <div className="d-ficha">
      <div className="cd f-cab">
        <div className="f-id">
          <div className="avatar">{p.nombre.split(" ").map((x) => x[0]).join("").slice(0, 2)}</div>
          <div><h2>{p.nombre}</h2><p>{p.edad} años · {fmt(t.talla_m, 2)} m · semana {sem} de tratamiento</p></div>
        </div>
      </div>
      {a && a.s !== "ok" && <div className={`aviso-d ${a.s}`}><i className={`punto s-${a.s}`} /><span>{a.texto}</span></div>}

      <div className="cd f-hero">
        <Anillo f={total > 0 ? perdido / total : 0} grande={fmt(Math.max(0, perdido))} chico={`de ${fmt(total, 0)} kg`} />
        <div className="f-hero-txt">
          <h3 style={{ margin: 0 }}>Avance a la meta</h3>
          <p>Bajó <b>{fmt(Math.max(0, perdido))} kg (−{fmt(Math.max(0, (perdido / t.peso_inicio) * 100))} %)</b> en {sem} semanas. Le faltan <b>{fmt(Math.max(0, peso - t.peso_meta))} kg</b> para la meta de {fmt(t.peso_meta, 0)} kg.</p>
          <div className="stats">
            <div className="stat"><b>{fmt(peso)} kg</b><span>Peso hoy</span></div>
            <div className="stat"><b>{fmt(imc(peso, t.talla_m))}</b><span>IMC</span></div>
            <div className="stat"><b>{cintura != null ? `${fmt(rfm(cintura, t.talla_m, mujer))} %` : "—"}</b><span>Grasa estimada (RFM)</span></div>
          </div>
        </div>
      </div>

      <div className="graficas">
        <div className="cd"><h3>Peso</h3><p className="nota">Semanal, desde el inicio del tratamiento</p><div dangerouslySetInnerHTML={{ __html: grafPeso(serie, t.peso_meta) }} /></div>
        <div className="cd"><h3>Velocidad de pérdida</h3><p className="nota">Porcentaje del peso que bajó cada semana</p><div dangerouslySetInnerHTML={{ __html: grafVel(serie, lim.limite) }} /></div>
        <div className="cd"><h3>Cintura y grasa estimada</h3><p className="nota">Del inicio a la meta</p>
          {t.cintura_inicio != null && t.cintura_meta != null && cintura != null ? (
            <div dangerouslySetInnerHTML={{ __html: bullet([
              { n: "Cintura", ini: t.cintura_inicio, hoy: cintura, meta: t.cintura_meta, u: "cm", d: 0 },
              { n: "Grasa (RFM)", ini: rfm(t.cintura_inicio, t.talla_m, mujer), hoy: rfm(cintura, t.talla_m, mujer), meta: rfm(t.cintura_meta, t.talla_m, mujer), u: "%", d: 1 },
            ]) }} />
          ) : <p className="nota" style={{ margin: 0 }}>Falta la cintura al inicio, hoy o la meta.</p>}
        </div>
        <div className="cd"><h3>Laboratorios</h3><p className="nota">{previo ? "Antes y ahora" : "Último resultado"}</p>
          {labs.length ? <div dangerouslySetInnerHTML={{ __html: pesas(labs) }} /> : <p className="nota" style={{ margin: 0 }}>Sin resultados todavía.</p>}
        </div>
        <div className="cd"><h3>Constancia</h3><p className="nota">Cada cuadro es una semana</p><div dangerouslySetInnerHTML={{ __html: constancia(t, regs, sem) }} /></div>
        <div className="cd"><h3>Efectos reportados</h3><p className="nota">Lo que la paciente marcó cada semana</p><div dangerouslySetInnerHTML={{ __html: efectos(t, regs, sem) }} /></div>
      </div>

      <div className="f-dos">
        <div className="cd"><h3>Tratamiento</h3><p className="nota">{t.confirmado ? "Confirmado por usted" : "Lo escribió la paciente · por confirmar"}</p>
          <p style={{ color: "var(--ios-label)" }}>{[t.medicamento, t.dosis, t.dia_aplicacion && DIA_TEXTO[t.dia_aplicacion]].filter(Boolean).join(" · ") || "Sin medicamento registrado"}</p>
          <p>Inicio {new Date(t.fecha_inicio + "T12:00:00").toLocaleDateString("es-CO", { day: "numeric", month: "long", year: "numeric" })} · {fmt(t.peso_inicio)} kg → meta {fmt(t.peso_meta)} kg</p>
          {!t.confirmado && <div className="acciones" style={{ marginTop: 12 }}><button type="button" className="btn pri" onClick={() => void confirmar()}>Confirmar datos</button></div>}
        </div>
        <div className="cd"><h3>Preguntas para el control</h3><p className="nota">Las dejó la paciente en la app</p>
          {preguntas.length ? <ul>{preguntas.map((q, i) => <li key={i}>“{q}”</li>)}</ul> : <p>Ninguna.</p>}
        </div>
      </div>

      <div className="cd">
        <h3>Análisis del laboratorio</h3>
        {!inf ? <p className="nota" style={{ margin: 0 }}>La paciente todavía no ha subido resultados.</p> : (
          <>
            <p className="nota">{pendiente ? "Espera su revisión: la paciente lo ve cuando usted lo apruebe." : "Aprobado: la paciente ya lo ve."} · Orden {pendiente?.orden ?? aprobados[0]?.orden}</p>
            {inf.paciente.lo_que_merece_atencion.length ? inf.paciente.lo_que_merece_atencion.map((h) => (
              <div key={h.hallazgo_id} className="hallazgo"><b>{h.titulo}</b><p>{h.nivel_lenguaje ?? ""}{h.escalamiento >= 2 ? " · consulta sugerida" : ""} · {h.por_que.join(" ")}</p></div>
            )) : <p className="nota">Sin hallazgos que merezcan atención.</p>}
            {inf.resultados.filter((r) => r.clase && !["en_rango", "calculado"].includes(r.clase) && r.estado !== "no_medido").length > 0 && (
              <p className="nota" style={{ marginTop: 10 }}>Fuera de rango: {inf.resultados.filter((r) => r.clase && !["en_rango", "calculado"].includes(r.clase) && r.estado !== "no_medido").map((r) => `${r.nombre} ${r.valor_original ?? r.valor} ${r.unidad ?? ""}`).join(" · ")}</p>
            )}
            {pendiente && <div className="acciones" style={{ marginTop: 12 }}><button type="button" className="btn pri" onClick={() => void aprobar()}>Aprobar lo que ve la paciente</button></div>}
          </>
        )}
      </div>

      <SemanaCard f={f} correo={correo} avisar={avisar} recargar={recargar} />
    </div>
  );
}

function SemanaCard({ f, correo, avisar, recargar }: { f: Ficha; correo: string; avisar: (t: string) => void; recargar: () => Promise<void> }) {
  const sm = f.semana;
  const [quitar, setQuitar] = useState<Set<string>>(new Set());
  const [mensaje, setMensaje] = useState(sm?.mensaje_doctora ?? "");
  useEffect(() => {
    setQuitar(new Set());
    setMensaje(f.semana?.mensaje_doctora ?? "");
  }, [f.semana?.id, f.semana?.mensaje_doctora]);
  if (!sm) return <div className="cd"><h3>Recomendaciones de la semana</h3><p className="nota" style={{ margin: 0 }}>La lista de la semana se arma el domingo con sus registros y sus exámenes.</p></div>;
  const publicar = async () => {
    const items: ItemSemana[] = sm.items.filter((x) => !quitar.has(x.id));
    const { error } = await supabase.from("semanas_peso").update({ items, mensaje_doctora: mensaje.trim() || null, estado: "publicada", revisado_por: correo, publicada: new Date().toISOString() }).eq("id", sm.id);
    avisar(error ? "No se pudo publicar." : "Publicada: la paciente ya la ve en Para ti.");
    await recargar();
  };
  return (
    <div className="cd">
      <h3>Recomendaciones de la semana</h3>
      <p className="nota">Semana del {new Date(sm.semana + "T12:00:00").toLocaleDateString("es-CO", { day: "numeric", month: "long" })} · {sm.estado === "publicada" ? "publicada" : "borrador para revisar"}</p>
      {sm.items.map((it) => (
        <div key={it.id} className="item-semana">
          <div style={{ opacity: quitar.has(it.id) ? 0.4 : 1 }}><b>{it.titulo}</b><p>{it.texto}</p><p>{it.por_que}</p></div>
          {sm.estado === "borrador" && (
            <button type="button" className="btn" onClick={() => setQuitar((q) => { const n = new Set(q); if (n.has(it.id)) n.delete(it.id); else n.add(it.id); return n; })}>{quitar.has(it.id) ? "Volver a poner" : "Quitar"}</button>
          )}
        </div>
      ))}
      {sm.estado === "borrador" ? (
        <>
          <div className="campo" style={{ marginTop: 12 }}>
            <label htmlFor="msj">Su mensaje para la paciente (opcional)</label>
            <textarea id="msj" rows={3} maxLength={600} value={mensaje} onChange={(e) => setMensaje(e.target.value)} placeholder="Por ejemplo: Vas muy bien, Laura. Nos vemos el jueves." />
          </div>
          <div className="acciones" style={{ marginTop: 12 }}><button type="button" className="btn pri" onClick={() => void publicar()}>Publicar la semana</button></div>
        </>
      ) : sm.mensaje_doctora ? <p className="nota" style={{ marginTop: 10 }}>Su mensaje: “{sm.mensaje_doctora}”</p> : null}
    </div>
  );
}
