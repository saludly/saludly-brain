/**
 * Línea GLP-1 · Registro del tratamiento (Fase 6B). La paciente pone a su doctora (código), su tratamiento, su peso
 * al inicio, hoy y su meta, y unas preguntas cortas. Todo queda como "dato de la paciente" hasta que la doctora lo confirma.
 * Guarda: autorización complementaria, cuestionario (objetivos, biotina, embarazo, actividad), tratamiento y el registro de hoy.
 */
import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import "@/peso.css";
import C from "@/lib/contenido.json";
import { supabase, useSesion } from "@/lib/sesion";
import { DIAS, DIA_TEXTO, VERSION_AUTORIZACION_PESO, codigoDraGuardado, hoyISO, marcarLineaPeso } from "@/lib/peso";

const num = (s: string) => {
  const n = Number(s.replace(",", "."));
  return s.trim() && Number.isFinite(n) ? n : null;
};

export function PesoEmpezar() {
  const s = useSesion();
  const navigate = useNavigate();
  const [paso, setPaso] = useState(1);
  const [codigo, setCodigo] = useState(codigoDraGuardado());
  const [doctora, setDoctora] = useState<string | null>(null);
  const [inicio, setInicio] = useState("");
  const [medicamento, setMedicamento] = useState("");
  const [dosis, setDosis] = useState("");
  const [dia, setDia] = useState("");
  const [talla, setTalla] = useState("");
  const [pesoInicio, setPesoInicio] = useState("");
  const [pesoHoy, setPesoHoy] = useState("");
  const [pesoMeta, setPesoMeta] = useState("");
  const [cintInicio, setCintInicio] = useState("");
  const [cintHoy, setCintHoy] = useState("");
  const [cintMeta, setCintMeta] = useState("");
  const [objetivos, setObjetivos] = useState<string[]>(["bajar_peso"]);
  const [actividad, setActividad] = useState("");
  const [biotina, setBiotina] = useState<"" | "si" | "no">("");
  const [embarazo, setEmbarazo] = useState("");
  const [aceptaDatos, setAceptaDatos] = useState(false);
  const [aceptaComerciales, setAceptaComerciales] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState(false);

  useEffect(() => {
    marcarLineaPeso();
    if (s.cargando) return;
    if (!s.sesion) void navigate({ to: "/entrar" });
    else if (!s.paciente || !s.autorizado) void navigate({ to: "/registro" });
    else if (s.tienePeso) void navigate({ to: "/peso" });
    if (s.cuestionario?.talla_m && !talla) setTalla(String(Math.round(Number(s.cuestionario.talla_m) * 100)));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [s, navigate]);

  // Nombre de la doctora del código (sin mostrar su correo).
  useEffect(() => {
    const c = codigo.trim().toUpperCase();
    if (c.length < 3) return void setDoctora(null);
    let vivo = true;
    void supabase.rpc("doctora_por_codigo", { c }).then(({ data }) => vivo && setDoctora((data as string | null) ?? null));
    return () => {
      vivo = false;
    };
  }, [codigo]);

  useEffect(() => {
    window.scrollTo({ top: 0 }); // con llaves: lo que devuelva scrollTo no debe llegar a React
  }, [paso]);

  const tallaM = (num(talla) ?? 0) / 100;
  const pi = num(pesoInicio), ph = num(pesoHoy), pm = num(pesoMeta);
  const validar = (): string | null => {
    if (paso === 1 && codigo.trim() && !doctora) return "No encontramos ese código. Revísalo o déjalo vacío.";
    if (paso === 2 && !inicio) return "Escribe cuándo empezaste el tratamiento.";
    if (paso === 2 && inicio > hoyISO()) return "La fecha de inicio no puede ser después de hoy.";
    if (paso === 3) {
      if (!(tallaM >= 1.2 && tallaM <= 2.2)) return "Escribe tu talla en centímetros, por ejemplo 162.";
      if (!pi || !ph || !pm || [pi, ph, pm].some((x) => x < 30 || x > 300)) return "Escribe tu peso al inicio, hoy y tu meta en kilos.";
      if (pm >= pi) return "Tu meta tiene que ser menor que tu peso al inicio.";
      for (const c of [cintInicio, cintHoy, cintMeta]) if (c.trim() && !((num(c) ?? 0) >= 40 && (num(c) ?? 0) <= 200)) return "Escribe la cintura en centímetros, por ejemplo 92.";
    }
    if (paso === 4 && (!actividad || !biotina || (s.paciente?.sexo === "mujer" && !embarazo))) return "Responde las preguntas para seguir.";
    if (paso === 5 && !aceptaDatos) return "Para usar Saludly con tu doctora necesitamos tu autorización.";
    return null;
  };

  const seguir = async () => {
    const e = validar();
    setError(e);
    if (e) return;
    if (paso < 5) return setPaso(paso + 1);
    setOcupado(true);
    const yo = s.sesion!.user.id;
    const a = await supabase.from("autorizaciones").insert({ version: VERSION_AUTORIZACION_PESO, acepta_datos: true, acepta_whatsapp: aceptaComerciales, acepta_comerciales: aceptaComerciales, agente: navigator.userAgent.slice(0, 200) });
    const c = await supabase.from("cuestionarios").upsert({
      paciente_id: yo, objetivos, peso_kg: ph, talla_m: Number(tallaM.toFixed(2)), nivel_actividad: actividad, toma_biotina: biotina === "si",
      embarazo: s.paciente?.sexo === "mujer" ? embarazo : null, completo: true, actualizado: new Date().toISOString(),
    });
    const t = await supabase.from("tratamientos_peso").insert({
      doctora_codigo: doctora ? codigo.trim().toUpperCase() : null, fecha_inicio: inicio, peso_inicio: pi, peso_meta: pm,
      cintura_inicio: num(cintInicio), cintura_meta: num(cintMeta), talla_m: Number(tallaM.toFixed(2)),
      medicamento: medicamento.trim() || null, dosis: dosis.trim() || null, dia_aplicacion: dia || null,
    });
    const r = t.error ? null : await supabase.from("registros_peso").upsert({ paciente_id: yo, fecha: hoyISO(), peso: ph, cintura: num(cintHoy) }, { onConflict: "paciente_id,fecha" });
    setOcupado(false);
    if (a.error || c.error || t.error || r?.error) return setError("No pudimos guardar tus datos. Revisa tu conexión e intenta de nuevo.");
    await s.recargar();
    void navigate({ to: "/peso" });
  };

  const tog = (id: string) => setObjetivos((o) => (o.includes(id) ? o.filter((x) => x !== id) : o.length >= 3 ? o : [...o, id]));
  const titulos = ["Tu doctora", "Tu tratamiento", "Tu peso y tu meta", "Sobre ti", "Tu autorización"];

  return (
    <main className="peso-app">
      <div className="pa-col" style={{ paddingBottom: 40 }}>
        <div className="pasos-reg" aria-label={`Paso ${paso} de 5`}>{[1, 2, 3, 4, 5].map((i) => <i key={i} className={i <= paso ? "ok" : ""} />)}</div>
        <h1 className="titulo-grande">{titulos[paso - 1]}</h1>

        {paso === 1 && (
          <div className="card" style={{ display: "grid", gap: 12 }}>
            <p style={{ margin: 0, fontSize: 15 }}>Si tu doctora te dio un código, escríbelo para que ella vea tu avance y tus exámenes.</p>
            <div className="campo">
              <label htmlFor="codigo">Código de tu doctora</label>
              <input id="codigo" value={codigo} onChange={(e) => setCodigo(e.target.value.toUpperCase())} autoCapitalize="characters" placeholder="Por ejemplo RIVERA" />
              {doctora ? <small>Te vas a vincular con <b>{doctora}</b>.</small> : <small>Si no lo tienes, déjalo vacío y lo agregas después.</small>}
            </div>
          </div>
        )}

        {paso === 2 && (
          <div className="card" style={{ display: "grid", gap: 14 }}>
            <div className="campo">
              <label htmlFor="inicio">¿Cuándo empezaste el tratamiento?</label>
              <input id="inicio" type="date" max={hoyISO()} value={inicio} onChange={(e) => setInicio(e.target.value)} />
            </div>
            <div className="campo">
              <label htmlFor="med">Medicamento que te indicó tu doctora</label>
              <input id="med" value={medicamento} onChange={(e) => setMedicamento(e.target.value)} maxLength={80} placeholder="Como aparece en tu fórmula" />
            </div>
            <div className="dos-campos">
              <div className="campo">
                <label htmlFor="dosis">Dosis</label>
                <input id="dosis" value={dosis} onChange={(e) => setDosis(e.target.value)} maxLength={40} placeholder="Ej. 0,5 mg" />
              </div>
              <div className="campo">
                <label htmlFor="dia">Día de aplicación</label>
                <select id="dia" value={dia} onChange={(e) => setDia(e.target.value)}>
                  <option value="">Elige</option>
                  {DIAS.map((d) => <option key={d} value={d}>{DIA_TEXTO[d]}</option>)}
                </select>
              </div>
            </div>
            <small style={{ color: "var(--ios-2)", fontSize: 12 }}>Solo lo usamos para recordarte tu aplicación. Saludly nunca cambia tu dosis: eso lo decide tu doctora.</small>
          </div>
        )}

        {paso === 3 && (
          <div className="card" style={{ display: "grid", gap: 14 }}>
            <div className="campo">
              <label htmlFor="talla">Talla (cm)</label>
              <input id="talla" inputMode="numeric" value={talla} onChange={(e) => setTalla(e.target.value)} placeholder="162" />
            </div>
            <div className="dos-campos">
              <div className="campo"><label htmlFor="pi">Peso al empezar (kg)</label><input id="pi" inputMode="decimal" value={pesoInicio} onChange={(e) => setPesoInicio(e.target.value)} placeholder="92" /></div>
              <div className="campo"><label htmlFor="ph">Peso hoy (kg)</label><input id="ph" inputMode="decimal" value={pesoHoy} onChange={(e) => setPesoHoy(e.target.value)} placeholder="85" /></div>
            </div>
            <div className="campo">
              <label htmlFor="pm">Tu meta de peso (kg)</label>
              <input id="pm" inputMode="decimal" value={pesoMeta} onChange={(e) => setPesoMeta(e.target.value)} placeholder="74" />
              <small>La que acordaste con tu doctora. Ella la confirma en su panel.</small>
            </div>
            <div className="campo"><span>Cintura (cm) · si la sabes</span></div>
            <div className="dos-campos" style={{ gridTemplateColumns: "1fr 1fr 1fr" }}>
              <div className="campo"><label htmlFor="ci">Al empezar</label><input id="ci" inputMode="decimal" value={cintInicio} onChange={(e) => setCintInicio(e.target.value)} /></div>
              <div className="campo"><label htmlFor="ch">Hoy</label><input id="ch" inputMode="decimal" value={cintHoy} onChange={(e) => setCintHoy(e.target.value)} /></div>
              <div className="campo"><label htmlFor="cm">Meta</label><input id="cm" inputMode="decimal" value={cintMeta} onChange={(e) => setCintMeta(e.target.value)} /></div>
            </div>
            <small style={{ color: "var(--ios-2)", fontSize: 12 }}>Mide la cintura a la altura del ombligo, sin apretar la cinta.</small>
          </div>
        )}

        {paso === 4 && (
          <>
            <div className="card" style={{ display: "grid", gap: 10 }}>
              <h3>Elige hasta 3 objetivos</h3>
              <div className="chips">
                {C.objetivos.map((o) => <button key={o.id} type="button" className="chip" aria-pressed={objetivos.includes(o.id)} onClick={() => tog(o.id)}>{o.nombre}</button>)}
              </div>
            </div>
            <div className="card" style={{ display: "grid", gap: 10 }}>
              <h3>{C.actividad.texto}</h3>
              <div className="chips">
                {C.actividad.opciones.map((o) => <button key={o.id} type="button" className="chip" aria-pressed={actividad === o.id} onClick={() => setActividad(o.id)}>{o.texto}</button>)}
              </div>
            </div>
            <div className="card" style={{ display: "grid", gap: 10 }}>
              <h3>{C.biotina.texto}</h3>
              <p style={{ margin: 0, fontSize: 13, color: "var(--ios-2)" }}>{C.biotina.ayuda}</p>
              <div className="chips">
                {(["si", "no"] as const).map((v) => <button key={v} type="button" className="chip" aria-pressed={biotina === v} onClick={() => setBiotina(v)}>{v === "si" ? "Sí" : "No"}</button>)}
              </div>
            </div>
            {s.paciente?.sexo === "mujer" && (
              <div className="card" style={{ display: "grid", gap: 10 }}>
                <h3>¿Estás embarazada o lactando?</h3>
                <div className="chips">
                  {C.embarazo.opciones.map((o) => <button key={o.id} type="button" className="chip" aria-pressed={embarazo === o.id} onClick={() => setEmbarazo(o.id)}>{o.texto}</button>)}
                </div>
              </div>
            )}
          </>
        )}

        {paso === 5 && (
          <div className="card" style={{ display: "grid", gap: 16 }}>
            <label className="casilla">
              <input type="checkbox" checked={aceptaDatos} onChange={(e) => setAceptaDatos(e.target.checked)} />
              <span>
                Autorizo a Saludly a tratar los datos de mi tratamiento (medicamento, dosis, peso, cintura, síntomas y resultados de laboratorio), que son datos sensibles de salud,
                para mostrarme mi avance y compartirlos con mi doctora{doctora ? ` (${doctora})` : ""}. Puedo retirar esta autorización cuando quiera. <b>Obligatoria.</b>
              </span>
            </label>
            <label className="casilla">
              <input type="checkbox" checked={aceptaComerciales} onChange={(e) => setAceptaComerciales(e.target.checked)} />
              <span>Acepto que Saludly me escriba por WhatsApp de vez en cuando para ofrecerme sus servicios, como los exámenes de laboratorio a domicilio. <b>Opcional.</b></span>
            </label>
            <small style={{ color: "var(--ios-2)", fontSize: 12 }}>Esto complementa la autorización que firmaste al registrarte (Ley 1581 de 2012). Saludly no diagnostica ni cambia tu tratamiento.</small>
          </div>
        )}

        {error && <p className="error">{error}</p>}
        <button type="button" className="boton" disabled={ocupado} onClick={() => void seguir()}>{ocupado ? "Guardando…" : paso < 5 ? "Seguir" : "Empezar"}</button>
        {paso > 1 && <button type="button" className="boton sec" onClick={() => { setError(null); setPaso(paso - 1); }}>Atrás</button>}
      </div>
    </main>
  );
}
