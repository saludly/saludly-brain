/**
 * Línea GLP-1 · App de la paciente (Fase 6B), con el lenguaje de iOS del demo aprobado.
 * Hoy (nivel y reto en anillos, registro, aplicación, metas y síntomas), Progreso (silueta con capa y peso),
 * Logros, Exámenes (subir el PDF y ver el análisis aprobado por la doctora) y Para ti (semana publicada).
 * Los síntomas de alarma muestran el mensaje de seguridad en el momento y le aparecen a la doctora primero.
 */
import { useCallback, useEffect, useMemo, useState, type ReactNode } from "react";
import { useNavigate } from "@tanstack/react-router";
import "@/peso.css";
import { Anillo, Notificacion, Silueta, useContador } from "@/components/PesoComunes";
import { DatosTratamiento } from "@/components/DatosTratamiento";
import { grafPeso } from "@/lib/graficas";
import { supabase, useSesion } from "@/lib/sesion";
import {
  DIA_TEXTO, SINTOMAS, actual, avance, cargarPaciente, esAlarma, fmt, hoyISO, logros, marcarLineaPeso, nivel, nivelSinBajar, retoActual, serieSemanal,
  type Registro, type Semana, type Tratamiento,
} from "@/lib/peso";
import type { Resultado } from "@/lib/informe";

type Tab = "hoy" | "progreso" | "logros" | "examenes" | "parati";
const METAS = ["Caminar 30 minutos", "Proteína en el desayuno", "8 vasos de agua"];

const ICONOS: Record<Tab, ReactNode> = {
  hoy: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8"><circle cx="12" cy="12" r="8.5" /><circle cx="12" cy="12" r="4" /></svg>,
  progreso: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M4 18 9 12l4 3 7-8" /><path d="M15 7h5v5" /></svg>,
  logros: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round"><circle cx="12" cy="9" r="6" /><path d="m8.5 13.5-1.5 7 5-2.5 5 2.5-1.5-7" /></svg>,
  examenes: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"><path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3" /><path d="M7.5 15h9" /></svg>,
  parati: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z" /></svg>,
};
const NOMBRE_TAB: Record<Tab, string> = { hoy: "Hoy", progreso: "Progreso", logros: "Logros", examenes: "Exámenes", parati: "Para ti" };

export function Peso() {
  const s = useSesion();
  const navigate = useNavigate();
  const [tab, setTab] = useState<Tab>("hoy");
  const [t, setT] = useState<Tratamiento | null>(null);
  const [regs, setRegs] = useState<Registro[]>([]);
  const [semana, setSemana] = useState<Semana | null>(null);
  const [aviso, setAviso] = useState<{ m: string; t: string; s: string; id: number } | null>(null);
  const [hoja, setHoja] = useState(false);
  const [momento, setMomento] = useState<"inicio" | "hoy" | "meta">("hoy");

  useEffect(() => {
    marcarLineaPeso();
    if (s.cargando) return;
    if (!s.sesion) void navigate({ to: "/entrar" });
    else if (!s.tienePeso) void navigate({ to: "/peso/empezar" });
  }, [s, navigate]);

  const yo = s.sesion?.user.id;
  const recargar = useCallback(async () => {
    if (!yo) return;
    const d = await cargarPaciente(yo);
    setT(d.tratamiento);
    setRegs(d.registros);
    setSemana(d.semana);
  }, [yo]);
  // Al abrir, al volver a la app y cada 30 segundos: así se ve lo que registre o corrija la doctora.
  useEffect(() => {
    void recargar();
    const id = setInterval(() => void recargar(), 30000);
    const alVolver = () => document.visibilityState === "visible" && void recargar();
    document.addEventListener("visibilitychange", alVolver);
    return () => { clearInterval(id); document.removeEventListener("visibilitychange", alVolver); };
  }, [recargar]);
  useEffect(() => {
    window.scrollTo({ top: 0 }); // con llaves: lo que devuelva scrollTo no debe llegar a React
  }, [tab]);

  const hoy = regs.find((r) => r.fecha === hoyISO());
  const guardarHoy = async (campos: Partial<Registro>) => {
    if (!yo) return;
    const { error } = await supabase.from("registros_peso").upsert({ paciente_id: yo, fecha: hoyISO(), ...campos }, { onConflict: "paciente_id,fecha" });
    if (error) setAviso({ m: "!", t: "No se guardó", s: "Revisa tu conexión e intenta de nuevo.", id: Date.now() });
    await recargar();
  };

  if (!t || !yo) return <main className="peso-app" />;

  const examenOk = !!s.informe;
  const { peso, cintura } = actual(t, regs);
  const nv = nivelSinBajar(yo, nivel(t, regs, examenOk));
  const reto = retoActual(t, peso);
  const av = avance(t, peso, cintura);
  const grosor = momento === "inicio" ? 1 : momento === "meta" ? 0 : 1 - av;

  return (
    <main className="peso-app">
      <Notificacion aviso={aviso} />
      <div className="pa-col">
        <div className="vista-in" key={tab}>
          {tab === "hoy" && <Hoy t={t} regs={regs} hoy={hoy} nivel={nv} reto={reto} nombre={s.paciente?.nombre.split(" ")[0] ?? ""} abrir={() => setHoja(true)} guardar={guardarHoy} />}
          {tab === "progreso" && (
            <>
              <h1 className="titulo-grande">Progreso</h1>
              <div className="card" style={{ display: "grid", gap: 12 }}>
                <Silueta grosor={grosor} />
                <div className="seg-ios" role="group" aria-label="Momento">
                  {(["inicio", "hoy", "meta"] as const).map((m) => <button key={m} type="button" aria-pressed={momento === m} onClick={() => setMomento(m)}>{m === "inicio" ? "Inicio" : m === "hoy" ? "Hoy" : "Meta"}</button>)}
                </div>
                <p className="camino">Llevas el <b>{Math.round(av * 100)} %</b> del camino a tu meta</p>
              </div>
              <div className="dos">
                <div className="card dato"><b>−{fmt(Math.max(0, t.peso_inicio - peso))} kg</b><span>desde que empezaste</span></div>
                <div className="card dato"><b>{t.cintura_inicio != null && cintura != null ? `−${fmt(Math.max(0, t.cintura_inicio - cintura), 0)} cm` : "—"}</b><span>de cintura</span></div>
              </div>
              <div className="card"><h3>Tu peso</h3><div className="grafica" dangerouslySetInnerHTML={{ __html: grafPeso(serieSemanal(t, regs), t.peso_meta) }} /></div>
              <MisDatos t={t} alGuardar={(m) => { setAviso({ m: "✓", t: "Datos guardados", s: m, id: Date.now() }); void recargar(); }} />
            </>
          )}
          {tab === "logros" && <Logros t={t} regs={regs} examenOk={examenOk} nivel={nv} peso={peso} />}
          {tab === "examenes" && <Examenes onAviso={setAviso} />}
          {tab === "parati" && <ParaTi semana={semana} />}
        </div>
      </div>

      <nav className="tabbar" aria-label="Secciones">
        <div>
          {(Object.keys(NOMBRE_TAB) as Tab[]).map((k) => (
            <button key={k} type="button" aria-current={tab === k ? "page" : undefined} onClick={() => setTab(k)}>{ICONOS[k]}{NOMBRE_TAB[k]}</button>
          ))}
        </div>
      </nav>

      <HojaRegistro
        abierta={hoja}
        peso={peso}
        cintura={cintura}
        cerrar={() => setHoja(false)}
        guardar={async (p, c) => {
          const antes = new Set(logros(t, regs, examenOk).filter((l) => l.ok).map((l) => l.id));
          setHoja(false);
          const { error } = await supabase.from("registros_peso").upsert({ paciente_id: yo, fecha: hoyISO(), peso: p, cintura: c }, { onConflict: "paciente_id,fecha" });
          if (error) return setAviso({ m: "!", t: "No se guardó", s: "Revisa tu conexión e intenta de nuevo.", id: Date.now() });
          const d = await cargarPaciente(yo);
          setRegs(d.registros);
          const nuevos = logros(t, d.registros, examenOk).filter((l) => l.ok && !antes.has(l.id));
          const n2 = nivelSinBajar(yo, nivel(t, d.registros, examenOk));
          setAviso(nuevos.length
            ? { m: nuevos[0].m, t: "Logro: " + nuevos[0].t, s: nuevos.length > 1 ? `y ${nuevos.length - 1} más. Tu nivel subió a ${n2}.` : `Tu nivel subió a ${n2}.`, id: Date.now() }
            : { m: String(n2), t: "Registro guardado", s: "Tu silueta ya cambió en Progreso.", id: Date.now() });
        }}
      />
    </main>
  );
}

function MisDatos({ t, alGuardar }: { t: Tratamiento; alGuardar: (m: string) => void }) {
  const [editar, setEditar] = useState(false);
  const fecha = new Date(t.fecha_inicio + "T12:00:00").toLocaleDateString("es-CO", { day: "numeric", month: "long", year: "numeric" });
  return (
    <div className="card">
      <h3>Mis datos</h3>
      {editar ? (
        <DatosTratamiento t={t} quien="paciente" alGuardar={(m) => { setEditar(false); alGuardar(m); }} alCancelar={() => setEditar(false)} />
      ) : (
        <div style={{ display: "grid", gap: 6, fontSize: 15 }}>
          <div className="fila"><span style={{ color: "var(--ios-2)" }}>Empezaste</span><b>{fecha} · {fmt(t.peso_inicio)} kg</b></div>
          <div className="fila"><span style={{ color: "var(--ios-2)" }}>Tu meta</span><b>{fmt(t.peso_meta)} kg</b></div>
          {t.cintura_inicio != null && <div className="fila"><span style={{ color: "var(--ios-2)" }}>Cintura</span><b>{fmt(t.cintura_inicio, 0)} → {t.cintura_meta != null ? fmt(t.cintura_meta, 0) : "—"} cm</b></div>}
          <div className="fila"><span style={{ color: "var(--ios-2)" }}>Estado</span><b>{t.confirmado ? "Confirmado por tu doctora" : "Por confirmar con tu doctora"}</b></div>
          <button type="button" className="boton sec" style={{ marginTop: 8 }} onClick={() => setEditar(true)}>Corregir mis datos</button>
        </div>
      )}
    </div>
  );
}

function Hoy({ t, regs, hoy, nivel: nv, reto, nombre, abrir, guardar }: {
  t: Tratamiento; regs: Registro[]; hoy?: Registro; nivel: number; reto: ReturnType<typeof retoActual>; nombre: string; abrir: () => void; guardar: (c: Partial<Registro>) => Promise<void>;
}) {
  const n = useContador(nv);
  const [sint, setSint] = useState<string[]>(hoy?.sintomas ?? []);
  const [metas, setMetas] = useState<boolean[]>(() => METAS.map((_, i) => i < (hoy?.metas_cumplidas ?? 0)));
  useEffect(() => {
    setSint(hoy?.sintomas ?? []);
  }, [hoy?.sintomas]);
  const alarma = sint.some(esAlarma);
  const fecha = new Date().toLocaleDateString("es-CO", { weekday: "long", day: "numeric", month: "long" });
  const tocarSintoma = (id: string) => {
    // "Bien" excluye los demás síntomas, y marcar un síntoma quita "Bien".
    const nuevo = sint.includes(id) ? sint.filter((x) => x !== id) : id === "bien" ? ["bien"] : [...sint.filter((x) => x !== "bien"), id];
    setSint(nuevo);
    void guardar({ sintomas: nuevo });
  };
  const tocarMeta = (i: number) => {
    const nuevo = metas.map((m, k) => (k === i ? !m : m));
    setMetas(nuevo);
    void guardar({ metas_cumplidas: nuevo.filter(Boolean).length, metas_total: METAS.length });
  };
  const ultimaAplicada = [...regs].reverse().find((r) => r.aplicada)?.fecha;
  const aplicadaEstaSemana = !!ultimaAplicada && Date.now() - new Date(ultimaAplicada + "T12:00:00").getTime() < 6 * 864e5;
  return (
    <>
      <h1 className="titulo-grande">Hola, {nombre}</h1>
      <p className="sub" style={{ textTransform: "capitalize" }}>{fecha}</p>
      <div className="card">
        <div className="dos-anillos">
          <div className="an"><Anillo f={nv / 100} grande={String(n)} chico="de 100" /><small>Tu nivel</small></div>
          <div className="an">
            {reto ? <Anillo clase="anillo reto" f={reto.bajo / reto.obj} grande={fmt(reto.bajo)} chico={`de ${fmt(reto.obj, 0)} kg`} color="var(--ios-green)" /> : <Anillo clase="anillo reto" f={1} grande="✓" chico="meta" color="var(--ios-green)" />}
            <small>{reto ? `Reto ${fmt(reto.obj, 0)} kg` : "Tu meta"}</small>
          </div>
        </div>
        <div className="siguiente">
          {reto ? <><b>Reto: {reto.t}</b><span>Te faltan {fmt(reto.falta)} kg. Vas muy bien.</span></> : <><b>¡Llegaste a tu meta!</b><span>Ahora el reto es mantenerla.</span></>}
        </div>
      </div>
      <button type="button" className="boton" onClick={abrir}>Registrar peso y cintura</button>
      {(t.dosis || t.dia_aplicacion) && (
        <div className="card">
          <h3>Tu aplicación semanal</h3>
          <div className="med">
            <div className="med-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"><rect x="3" y="5" width="18" height="16" rx="3" /><path d="M3 10h18M8 3v4M16 3v4" /></svg></div>
            <div><b>{[t.dia_aplicacion && DIA_TEXTO[t.dia_aplicacion], t.dosis].filter(Boolean).join(" · ")}</b><small>Como indicó tu doctora</small></div>
            <button type="button" className={`pill-btn${aplicadaEstaSemana ? " hecho" : ""}`} onClick={() => !aplicadaEstaSemana && void guardar({ aplicada: true })}>{aplicadaEstaSemana ? "Aplicada ✓" : "Ya la apliqué"}</button>
          </div>
        </div>
      )}
      <div className="card">
        <h3>Metas de hoy</h3>
        <div className="lista">
          {METAS.map((m, i) => (
            <div key={m}>
              <button type="button" className="check" role="checkbox" aria-checked={metas[i]} aria-label={m} onClick={() => tocarMeta(i)}>
                <svg viewBox="0 0 14 14" fill="none" stroke="#fff" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="m3 7.5 2.6 2.5L11 4" /></svg>
              </button>
              <div className="meta-txt">{m}</div>
            </div>
          ))}
        </div>
      </div>
      <div className="card">
        <h3>¿Cómo te sientes esta semana?</h3>
        <div className="chips">
          {SINTOMAS.map((x) => <button key={x.id} type="button" className={`chip${x.alarma ? " alarma" : ""}`} aria-pressed={sint.includes(x.id)} onClick={() => tocarSintoma(x.id)}>{x.texto}</button>)}
        </div>
        {alarma && <div className="aviso-alarma">Si el dolor abdominal es fuerte y no se quita, o el vómito no para, llama a tu doctora o ve a urgencias. Ya le avisamos a tu doctora en su panel.</div>}
      </div>
    </>
  );
}

function HojaRegistro({ abierta, peso, cintura, cerrar, guardar }: { abierta: boolean; peso: number; cintura: number | null; cerrar: () => void; guardar: (p: number, c: number | null) => void }) {
  const [p, setP] = useState(peso);
  const [c, setC] = useState<number | null>(cintura);
  useEffect(() => {
    if (abierta) { setP(peso); setC(cintura); }
  }, [abierta, peso, cintura]);
  const r = (x: number) => Math.round(x * 10) / 10;
  return (
    <>
      <div className={`velo${abierta ? " on" : ""}`} onClick={cerrar} />
      <div className={`hoja${abierta ? " on" : ""}`} role="dialog" aria-modal="true" aria-labelledby="hoja-t" aria-hidden={!abierta}>
        <div>
          <div className="agarre" />
          <div className="hoja-cab"><button type="button" onClick={cerrar}>Cancelar</button><b id="hoja-t">Registrar</b><button type="button" style={{ fontWeight: 600 }} onClick={() => guardar(p, c)}>Guardar</button></div>
          <div className="card"><h3>Peso de hoy</h3>
            <div className="paso">
              <button type="button" aria-label="Bajar 100 gramos" onClick={() => setP(r(Math.max(30, p - 0.1)))}>−</button>
              <div className="v">{fmt(p)} <small>kg</small></div>
              <button type="button" aria-label="Subir 100 gramos" onClick={() => setP(r(Math.min(300, p + 0.1)))}>+</button>
            </div>
          </div>
          <div className="card"><h3>Cintura (cada 2 semanas)</h3>
            {c == null ? (
              <button type="button" className="boton sec" onClick={() => setC(90)}>Agregar cintura</button>
            ) : (
              <div className="paso">
                <button type="button" aria-label="Bajar medio centímetro" onClick={() => setC(r(Math.max(40, c - 0.5)))}>−</button>
                <div className="v">{fmt(c)} <small>cm</small></div>
                <button type="button" aria-label="Subir medio centímetro" onClick={() => setC(r(Math.min(200, c + 0.5)))}>+</button>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}

function Logros({ t, regs, examenOk, nivel: nv, peso }: { t: Tratamiento; regs: Registro[]; examenOk: boolean; nivel: number; peso: number }) {
  const ls = logros(t, regs, examenOk);
  const reto = retoActual(t, peso);
  return (
    <>
      <h1 className="titulo-grande">Logros</h1>
      <div className="card">
        <div className="fila"><b style={{ fontSize: 17 }}>Nivel {nv}</b><span style={{ color: "var(--ios-2)", fontSize: 14 }}>{ls.filter((l) => l.ok).length} de {ls.length} logros</span></div>
        <div className="barra"><i style={{ width: nv + "%" }} /></div>
      </div>
      <div className="card">
        <div className="medallas">
          {ls.map((l) => (
            <div key={l.id} className={`medalla${l.ok ? "" : " bloq"}`}>
              <div className="m">{l.m}</div>
              <b>{l.t}</b>
              <small>{l.ok ? l.s || "Logrado" : reto && reto.id === l.id ? `Te faltan ${fmt(reto.falta)} kg` : "Por ganar"}</small>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

const ETIQUETA_CLASE: Record<string, [string, string]> = {
  en_rango: ["bien", "En tu rango"], bajo: ["hablar", "Para hablar con tu doctora"], alto: ["hablar", "Para hablar con tu doctora"],
  limitrofe: ["hablar", "Para hablar con tu doctora"], critico: ["hablar", "Para hablar con tu doctora"], alterado: ["hablar", "Para hablar con tu doctora"],
};

function Examenes({ onAviso }: { onAviso: (a: { m: string; t: string; s: string; id: number }) => void }) {
  const s = useSesion();
  const [abierto, setAbierto] = useState(false);
  const [subiendo, setSubiendo] = useState(false);
  const [estado, setEstado] = useState<string | null>(null);
  const inf = s.informe;
  const res = useMemo(() => (inf?.resultados ?? []).filter((r: Resultado) => r.estado !== "no_medido" && r.clase !== "calculado" && r.valor != null), [inf]);

  const subir = async (f: File) => {
    if (f.type !== "application/pdf") return setEstado("El archivo tiene que ser el PDF del laboratorio.");
    if (f.size > 3 * 1024 * 1024) return setEstado("El PDF pesa más de 3 MB.");
    setSubiendo(true);
    setEstado(null);
    const bytes = new Uint8Array(await f.arrayBuffer());
    let bin = "";
    for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
    try {
      const r = await fetch("/api/procesar", {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${s.sesion?.access_token}` },
        body: JSON.stringify({ pdf_base64: btoa(bin) }),
      });
      const d = (await r.json().catch(() => ({}))) as { error?: string };
      if (!r.ok) setEstado(d.error ?? "No pudimos leer el PDF. Intenta de nuevo.");
      else {
        setEstado("Recibimos tu resultado. Tu doctora lo revisa y aquí te aparece el análisis cuando lo apruebe.");
        onAviso({ m: "Lab", t: "Resultado recibido", s: "Tu doctora lo revisa antes de que lo veas.", id: Date.now() });
      }
    } catch {
      setEstado("No hubo conexión. Intenta de nuevo.");
    }
    setSubiendo(false);
  };

  return (
    <>
      <h1 className="titulo-grande">Exámenes</h1>
      {inf ? (
        <>
          <p className="sub">Revisados por tu doctora{inf.fecha_toma ? ` · tomados el ${new Date(inf.fecha_toma + "T12:00:00").toLocaleDateString("es-CO", { day: "numeric", month: "long" })}` : ""}</p>
          {inf.paciente.lo_que_merece_atencion.length > 0 && (
            <div className="card">
              <h3>Lo que vio Saludly</h3>
              {inf.paciente.lo_que_merece_atencion.map((h) => (
                <div key={h.hallazgo_id} className="examen"><b style={{ fontSize: 16 }}>{h.titulo}</b><small>{h.por_que[0] ?? h.que_es}</small></div>
              ))}
            </div>
          )}
          <div className="card">
            {res.map((r) => {
              const [cl, tx] = ETIQUETA_CLASE[r.clase ?? ""] ?? ["", ""];
              return (
                <div key={r.biomarker_id} className="examen">
                  <div className="fila"><b>{r.nombre}</b>{tx && <span className={`tag ${cl}`}>{tx}</span>}</div>
                  <div className="fila"><small>{r.intervalo ? `Referencia del laboratorio: ${r.intervalo}` : ""}</small><span className="valor">{String(r.valor_original ?? r.valor)} {r.unidad ?? ""}</span></div>
                </div>
              );
            })}
          </div>
          <p className="pie-legal">Esto no es un diagnóstico. Tu doctora revisó estos resultados y los habla contigo en el control.</p>
        </>
      ) : (
        <div className="card"><p style={{ margin: 0, fontSize: 15 }}>Cuando subas el PDF de tu laboratorio, Saludly lo analiza y tu doctora lo revisa. Después te aparece aquí, explicado en simple.</p></div>
      )}

      <div className="card" style={{ display: "grid", gap: 10 }}>
        <h3>Subir tu resultado</h3>
        <label className="boton sec" style={{ cursor: "pointer" }}>
          {subiendo ? "Analizando…" : "Elegir el PDF del laboratorio"}
          <input type="file" accept="application/pdf" hidden disabled={subiendo} onChange={(e) => { const f = e.target.files?.[0]; if (f) void subir(f); e.target.value = ""; }} />
        </label>
        {estado && <p style={{ margin: 0, fontSize: 14, color: "var(--ios-2)" }}>{estado}</p>}
        <small style={{ fontSize: 12, color: "var(--ios-2)" }}>El PDF no se guarda: se lee y se borra.</small>
      </div>

      <button type="button" className="sutil" aria-expanded={abierto} onClick={() => setAbierto(!abierto)}>
        <span>¿Te toca repetir tus exámenes?<small>Te los tomamos en casa</small></span>
        <svg viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m5 2.5 4.5 4.5L5 11.5" /></svg>
      </button>
      {abierto && (
        <div className="card" style={{ display: "grid", gap: 8 }}>
          <b style={{ fontSize: 17 }}>Exámenes en casa con Saludly</b>
          <p style={{ margin: 0, fontSize: 15, color: "var(--ios-2)" }}>Una enfermera va a tu casa con la orden de tu doctora; vas en ayunas. También puedes hacerlos en el laboratorio que prefieras.</p>
          <a className="boton sec" href="https://wa.me/573011307944?text=Hola%2C%20quiero%20agendar%20mis%20ex%C3%A1menes%20en%20casa" target="_blank" rel="noopener">Agendar por WhatsApp</a>
          <p style={{ margin: 0, fontSize: 13, color: "var(--ios-2)" }}>WhatsApp de Saludly: <span className="numero">+57 301 130 7944</span></p>
        </div>
      )}
    </>
  );
}

function ParaTi({ semana }: { semana: Semana | null }) {
  const s = useSesion();
  const recos = s.informe?.paciente.que_puedes_hacer.slice(0, 2) ?? [];
  return (
    <>
      <h1 className="titulo-grande">Para ti</h1>
      {semana?.mensaje_doctora && (
        <div className="card reco"><small>Mensaje de tu doctora</small><p style={{ color: "var(--ios-label)" }}>{semana.mensaje_doctora}</p></div>
      )}
      {semana?.items.map((it) => (
        <div key={it.id} className="card reco">
          <small>{it.fuente === "examenes" ? "Por tus exámenes" : it.fuente === "objetivos" ? "Para tus objetivos" : "Esta semana"}</small>
          <b>{it.titulo}</b>
          <p>{it.texto}</p>
          {it.por_que && <p className="porque">{it.por_que}</p>}
        </div>
      ))}
      {!semana && recos.map((r) => (
        <div key={r.recomendacion_id} className="card reco"><small>Por tus exámenes</small><b>{r.titulo}</b><p>{r.texto}</p></div>
      ))}
      {!semana && <div className="card"><p style={{ margin: 0, fontSize: 15, color: "var(--ios-2)" }}>Cada lunes te llegan aquí las recomendaciones de tu semana, revisadas por tu doctora.</p></div>}
      <div className="card reco">
        <small>Receta del día</small>
        <b>¿Quieres una receta cada día?</b>
        <p>Te llega por WhatsApp, pensada para tus objetivos. Solo si tú nos escribes.</p>
        <a className="boton verde" style={{ marginTop: 10 }} href="https://wa.me/573011307944?text=Hola%2C%20quiero%20la%20receta%20del%20d%C3%ADa" target="_blank" rel="noopener">Recibir la receta por WhatsApp</a>
        <p style={{ fontSize: 13, marginTop: 6 }}>WhatsApp de Saludly: <span className="numero">+57 301 130 7944</span></p>
      </div>
    </>
  );
}
