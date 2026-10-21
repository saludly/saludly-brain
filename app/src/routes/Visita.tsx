import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Campo, Pantalla, Titulo, claseEntrada } from "@/components/Formulario";
import { siguientePaso, supabase, useSesion } from "@/lib/sesion";

/**
 * "Mi enfermera está aquí": la enfermera llena solo lo técnico en el celular del paciente.
 * Las preguntas ya las respondió el paciente en el cuestionario. Los rangos son de digitación, no clínicos.
 * Peso y estatura ya están en el cuestionario (decisión de Carlos, 22 oct 2026): aquí solo se piden si el paciente los dejó en blanco.
 */
const numero = (v: string, dec = false) => (dec ? v.replace(",", ".").replace(/[^\d.]/g, "") : v.replace(/\D/g, "")).slice(0, 6);

export function Visita() {
  const s = useSesion();
  const navigate = useNavigate();
  const [sist, setSist] = useState("");
  const [diast, setDiast] = useState("");
  const [cintura, setCintura] = useState("");
  const [cadera, setCadera] = useState("");
  const [peso, setPeso] = useState("");
  const [talla, setTalla] = useState("");
  const [enfermera, setEnfermera] = useState("");
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (s.cargando) return;
    const ir = siguientePaso(s);
    if (ir !== "/listo") void navigate({ to: ir });
    else if (s.visita) {
      const v = s.visita;
      setSist(String(v.presion_sistolica ?? ""));
      setDiast(String(v.presion_diastolica ?? ""));
      setCintura(String(v.cintura_cm ?? ""));
      setCadera(String(v.cadera_cm ?? ""));
      setPeso(String(v.peso_kg ?? ""));
      setTalla(v.talla_m ? String(Math.round(v.talla_m * 100)) : "");
      setEnfermera(v.enfermera ?? "");
    }
  }, [s, navigate]);

  const enRango = (v: string, a: number, b: number) => v !== "" && Number(v) >= a && Number(v) <= b;
  const pidePeso = !s.cuestionario?.peso_kg;
  const pideTalla = !s.cuestionario?.talla_m;
  const valido =
    enRango(sist, 60, 260) && enRango(diast, 30, 160) && Number(sist) > Number(diast) && enRango(cintura, 40, 200) &&
    (cadera === "" || enRango(cadera, 40, 220)) && (!pidePeso || enRango(peso, 25, 300)) && (!pideTalla || enRango(talla, 100, 230)) &&
    enfermera.trim().length >= 3;

  const guardar = async () => {
    setError(null);
    setOcupado(true);
    const { error } = await supabase.from("visitas").upsert({
      paciente_id: s.sesion!.user.id,
      presion_sistolica: Number(sist),
      presion_diastolica: Number(diast),
      cintura_cm: Number(cintura),
      cadera_cm: cadera ? Number(cadera) : null,
      peso_kg: pidePeso ? Number(peso) : null,
      talla_m: pideTalla ? Number(talla) / 100 : null,
      enfermera: enfermera.trim(),
      tomada: new Date().toISOString(),
    });
    if (error) {
      setOcupado(false);
      return setError("No pudimos guardar las medidas. Revísalas e intenta de nuevo.");
    }
    await s.recargar();
    setOcupado(false);
    void navigate({ to: "/listo" });
  };

  return (
    <Pantalla etiqueta="Visita" boton="Guardar medidas" puedeSeguir={valido} ocupado={ocupado} onSeguir={guardar} onAtras={() => void navigate({ to: "/listo" })} error={error}>
      <Titulo texto="La enfermera te dicta las medidas y tú las escribes, o ella las escribe en tu celular. Tus preguntas ya las respondiste.">Mi enfermera está aquí.</Titulo>
      <div className="mt-8 space-y-6">
        <div>
          <span className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">Presión arterial (mmHg)</span>
          <p className="mt-1 text-xs text-ink-muted">Sentado, después de 5 minutos de reposo.</p>
          <div className="mt-2 flex items-center gap-2">
            <input inputMode="numeric" aria-label="Sistólica" value={sist} onChange={(e) => setSist(numero(e.target.value))} className={claseEntrada} placeholder="120" />
            <span className="text-xl text-ink-faint">/</span>
            <input inputMode="numeric" aria-label="Diastólica" value={diast} onChange={(e) => setDiast(numero(e.target.value))} className={claseEntrada} placeholder="80" />
          </div>
        </div>
        <div className="grid grid-cols-2 gap-4">
          <Campo etiqueta="Cintura (cm)" ayuda="A la altura del ombligo.">
            <input inputMode="decimal" value={cintura} onChange={(e) => setCintura(numero(e.target.value, true))} className={claseEntrada} placeholder="85" />
          </Campo>
          <Campo etiqueta="Cadera (cm)" ayuda="Opcional.">
            <input inputMode="decimal" value={cadera} onChange={(e) => setCadera(numero(e.target.value, true))} className={claseEntrada} placeholder="98" />
          </Campo>
          {pidePeso && (
            <Campo etiqueta="Peso (kg)" ayuda="No lo diste en el cuestionario.">
              <input inputMode="decimal" value={peso} onChange={(e) => setPeso(numero(e.target.value, true))} className={claseEntrada} placeholder="70" />
            </Campo>
          )}
          {pideTalla && (
            <Campo etiqueta="Estatura (cm)" ayuda="No la diste en el cuestionario.">
              <input inputMode="numeric" value={talla} onChange={(e) => setTalla(numero(e.target.value))} className={claseEntrada} placeholder="165" />
            </Campo>
          )}
        </div>
        <Campo etiqueta="Nombre de la enfermera">
          <input value={enfermera} onChange={(e) => setEnfermera(e.target.value)} className={claseEntrada} />
        </Campo>
      </div>
    </Pantalla>
  );
}
