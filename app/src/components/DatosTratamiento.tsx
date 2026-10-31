/**
 * Línea GLP-1 · Datos del tratamiento que corrigen la paciente (en su app) y la doctora (en su panel):
 * inicio, meta, talla, cintura, medicamento y día. Si la paciente cambia algo, la doctora lo vuelve a confirmar;
 * si lo guarda la doctora, queda confirmado. El peso y la cintura de hoy se registran aparte (registros_peso).
 */
import { useState } from "react";
import { supabase } from "@/lib/sesion";
import { DIAS, DIA_TEXTO, hoyISO, type Tratamiento } from "@/lib/peso";

const num = (s: string) => {
  const n = Number(s.replace(",", "."));
  return s.trim() && Number.isFinite(n) ? n : null;
};
const txt = (n: number | null | undefined) => (n == null ? "" : String(n).replace(".", ","));

export function DatosTratamiento({ t, quien, correo, alGuardar, alCancelar }: {
  t: Tratamiento; quien: "paciente" | "doctora"; correo?: string; alGuardar: (mensaje: string) => void; alCancelar: () => void;
}) {
  const [inicio, setInicio] = useState(t.fecha_inicio);
  const [pi, setPi] = useState(txt(t.peso_inicio));
  const [pm, setPm] = useState(txt(t.peso_meta));
  const [talla, setTalla] = useState(String(Math.round(t.talla_m * 100)));
  const [ci, setCi] = useState(txt(t.cintura_inicio));
  const [cm, setCm] = useState(txt(t.cintura_meta));
  const [med, setMed] = useState(t.medicamento ?? "");
  const [dosis, setDosis] = useState(t.dosis ?? "");
  const [dia, setDia] = useState(t.dia_aplicacion ?? "");
  const [error, setError] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState(false);

  const guardar = async () => {
    const p0 = num(pi), p1 = num(pm), ta = (num(talla) ?? 0) / 100, c0 = num(ci), c1 = num(cm);
    if (!inicio || inicio > hoyISO()) return setError("Revisa la fecha de inicio.");
    if (!p0 || !p1 || p0 < 30 || p0 > 300 || p1 < 30 || p1 > 300) return setError("Escribe el peso al inicio y la meta en kilos.");
    if (p1 >= p0) return setError("La meta tiene que ser menor que el peso al inicio.");
    if (!(ta >= 1.2 && ta <= 2.2)) return setError("Escribe la talla en centímetros, por ejemplo 162.");
    if ([c0, c1].some((c) => c != null && (c < 40 || c > 200))) return setError("Escribe la cintura en centímetros.");
    setOcupado(true);
    const datos = {
      fecha_inicio: inicio, peso_inicio: p0, peso_meta: p1, talla_m: Number(ta.toFixed(2)), cintura_inicio: c0, cintura_meta: c1,
      medicamento: med.trim() || null, dosis: dosis.trim() || null, dia_aplicacion: dia || null, actualizado: new Date().toISOString(),
      // La doctora confirma al guardar; un cambio de la paciente vuelve a pedir su confirmación.
      ...(quien === "doctora" ? { confirmado: new Date().toISOString(), confirmado_por: correo ?? null } : { confirmado: null, confirmado_por: null }),
    };
    const { error: e } = await supabase.from("tratamientos_peso").update(datos).eq("paciente_id", t.paciente_id);
    setOcupado(false);
    if (e) return setError("No se pudo guardar. Intenta de nuevo.");
    alGuardar(quien === "doctora" ? "Datos guardados y confirmados." : "Listo. Tu doctora ve el cambio en su panel.");
  };

  return (
    <div style={{ display: "grid", gap: 12 }}>
      <div className="campo"><label htmlFor="dt-ini">Inicio del tratamiento</label><input id="dt-ini" type="date" max={hoyISO()} value={inicio} onChange={(e) => setInicio(e.target.value)} /></div>
      <div className="dos-campos">
        <div className="campo"><label htmlFor="dt-pi">Peso al empezar (kg)</label><input id="dt-pi" inputMode="decimal" value={pi} onChange={(e) => setPi(e.target.value)} /></div>
        <div className="campo"><label htmlFor="dt-pm">Meta de peso (kg)</label><input id="dt-pm" inputMode="decimal" value={pm} onChange={(e) => setPm(e.target.value)} /></div>
      </div>
      <div className="dos-campos" style={{ gridTemplateColumns: "1fr 1fr 1fr" }}>
        <div className="campo"><label htmlFor="dt-ta">Talla (cm)</label><input id="dt-ta" inputMode="numeric" value={talla} onChange={(e) => setTalla(e.target.value)} /></div>
        <div className="campo"><label htmlFor="dt-ci">Cintura al empezar</label><input id="dt-ci" inputMode="decimal" value={ci} onChange={(e) => setCi(e.target.value)} /></div>
        <div className="campo"><label htmlFor="dt-cm">Cintura meta</label><input id="dt-cm" inputMode="decimal" value={cm} onChange={(e) => setCm(e.target.value)} /></div>
      </div>
      <div className="campo"><label htmlFor="dt-med">Medicamento</label><input id="dt-med" maxLength={80} value={med} onChange={(e) => setMed(e.target.value)} /></div>
      <div className="dos-campos">
        <div className="campo"><label htmlFor="dt-do">Dosis</label><input id="dt-do" maxLength={40} value={dosis} onChange={(e) => setDosis(e.target.value)} /></div>
        <div className="campo"><label htmlFor="dt-dia">Día de aplicación</label>
          <select id="dt-dia" value={dia} onChange={(e) => setDia(e.target.value)}><option value="">Sin día</option>{DIAS.map((d) => <option key={d} value={d}>{DIA_TEXTO[d]}</option>)}</select>
        </div>
      </div>
      {quien === "paciente" && <small style={{ fontSize: 12, color: "var(--ios-2)" }}>Si cambias algo, tu doctora lo vuelve a confirmar. Tu peso de hoy se registra con el botón "Registrar peso y cintura".</small>}
      {error && <p className="error">{error}</p>}
      <div className="acciones">
        <button type="button" className="btn pri" disabled={ocupado} onClick={() => void guardar()}>{ocupado ? "Guardando…" : "Guardar"}</button>
        <button type="button" className="btn" onClick={alCancelar}>Cancelar</button>
      </div>
    </div>
  );
}

/** La doctora registra el peso y la cintura de hoy (por ejemplo, en la consulta). */
export function RegistroDoctora({ pacienteId, correo, alGuardar }: { pacienteId: string; correo: string; alGuardar: (mensaje: string) => void }) {
  const [peso, setPeso] = useState("");
  const [cint, setCint] = useState("");
  const [error, setError] = useState<string | null>(null);
  const guardar = async () => {
    const p = num(peso), c = num(cint);
    if (p == null && c == null) return setError("Escribe el peso o la cintura.");
    if ((p != null && (p < 30 || p > 300)) || (c != null && (c < 40 || c > 200))) return setError("Revisa los valores.");
    const { error: e } = await supabase.from("registros_peso").upsert(
      { paciente_id: pacienteId, fecha: hoyISO(), ...(p != null ? { peso: p } : {}), ...(c != null ? { cintura: c } : {}), registrado_por: correo },
      { onConflict: "paciente_id,fecha" },
    );
    if (e) return setError("No se pudo guardar.");
    setPeso(""); setCint(""); setError(null);
    alGuardar("Registro de hoy guardado. La paciente lo ve en su app.");
  };
  return (
    <div style={{ display: "grid", gap: 10 }}>
      <div className="dos-campos">
        <div className="campo"><label htmlFor="rd-p">Peso de hoy (kg)</label><input id="rd-p" inputMode="decimal" value={peso} onChange={(e) => setPeso(e.target.value)} /></div>
        <div className="campo"><label htmlFor="rd-c">Cintura de hoy (cm)</label><input id="rd-c" inputMode="decimal" value={cint} onChange={(e) => setCint(e.target.value)} /></div>
      </div>
      {error && <p className="error">{error}</p>}
      <div className="acciones"><button type="button" className="btn pri" onClick={() => void guardar()}>Guardar registro</button></div>
    </div>
  );
}
