import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Campo, Opcion, Pantalla, Titulo, claseEntrada } from "@/components/Formulario";
import { CUESTIONARIO_VACIO, siguientePaso, supabase, useSesion, type Cuestionario as Datos } from "@/lib/sesion";
import C from "@/lib/contenido.json";

/**
 * Cuestionario de la PWA, antes de la visita. Las opciones salen del Knowledge Base
 * (objetivos.yaml, filtros.yaml y cuestionario.yaml, exportados con codigo/herramientas/exportar_app.py).
 * Cada paso se guarda al avanzar, así que se puede retomar.
 */
const PASOS = ["Tus metas", "Tu cuerpo", "Tus medicamentos", "Tu alimentación", "Tus hábitos", "Tu familia"];

function alternar(lista: string[], id: string, maximo?: number) {
  if (lista.includes(id)) return lista.filter((x) => x !== id);
  if (maximo && lista.length >= maximo) return lista;
  return [...lista, id];
}

export function Cuestionario() {
  const s = useSesion();
  const navigate = useNavigate();
  const [paso, setPaso] = useState(0);
  const [d, setD] = useState<Datos>(CUESTIONARIO_VACIO);
  const [peso, setPeso] = useState("");
  const [talla, setTalla] = useState("");
  const [sinMedicamentos, setSinMedicamentos] = useState(false);
  const [sinAlergias, setSinAlergias] = useState(false);
  const [sinAntecedentes, setSinAntecedentes] = useState(false);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [listo, setListo] = useState(false);

  useEffect(() => {
    if (s.cargando || listo) return;
    const ir = siguientePaso(s);
    if (ir !== "/cuestionario") return void navigate({ to: ir });
    if (s.cuestionario) {
      setD(s.cuestionario);
      if (s.cuestionario.peso_kg) setPeso(String(s.cuestionario.peso_kg));
      if (s.cuestionario.talla_m) setTalla(String(Math.round(s.cuestionario.talla_m * 100)));
    }
    setListo(true);
  }, [s, navigate, listo]);

  const mujer = s.paciente?.sexo === "mujer";
  const cambiar = (c: Partial<Datos>) => setD((x) => ({ ...x, ...c }));

  const valido = [
    d.objetivos.length === 3,
    d.nivel_actividad !== null && (peso === "" || (Number(peso) >= 25 && Number(peso) <= 300)) && (talla === "" || (Number(talla) >= 100 && Number(talla) <= 230)),
    d.toma_biotina !== null && (sinMedicamentos || d.medicamentos.length > 0 || !!d.medicamentos_otros?.trim()),
    d.dieta !== null && (sinAlergias || d.alergias.length > 0 || !!d.alergias_otras?.trim()),
    d.fuma !== null && d.alcohol !== null,
    (sinAntecedentes || d.antecedentes.length > 0) && (!mujer || d.embarazo !== null),
  ][paso];

  const guardar = async () => {
    setError(null);
    setOcupado(true);
    const ultimo = paso === PASOS.length - 1;
    const fila = {
      ...d,
      paciente_id: s.sesion!.user.id,
      peso_kg: peso ? Number(peso) : null,
      talla_m: talla ? Number(talla) / 100 : null,
      medicamentos_otros: d.medicamentos_otros?.trim() || null,
      alergias_otras: d.alergias_otras?.trim() || null,
      embarazo: mujer ? d.embarazo : null,
      completo: ultimo,
    };
    const { error } = await supabase.from("cuestionarios").upsert(fila);
    setOcupado(false);
    if (error) return setError("No pudimos guardar tus respuestas. Intenta de nuevo.");
    if (ultimo) {
      await s.recargar();
      void navigate({ to: "/listo" });
    } else setPaso(paso + 1);
  };

  return (
    <Pantalla
      paso={paso + 1}
      total={PASOS.length}
      etiqueta={PASOS[paso]}
      boton={paso === PASOS.length - 1 ? "Terminar" : "Continuar"}
      puedeSeguir={!!valido}
      ocupado={ocupado}
      onSeguir={guardar}
      onAtras={paso > 0 ? () => setPaso(paso - 1) : undefined}
      error={error}
    >
      {paso === 0 && (
        <>
          <Titulo texto="Tus metas definen el orden de tus recomendaciones. Nunca cambian tus resultados.">Elige tus 3 metas principales.</Titulo>
          <p className="mt-4 font-mono text-[10px] uppercase tracking-[0.16em] text-ink-faint">{d.objetivos.length} de 3 elegidas</p>
          <div className="mt-5 grid gap-3 sm:grid-cols-2">
            {C.objetivos.map((o) => (
              <Opcion key={o.id} activa={d.objetivos.includes(o.id)} onClick={() => cambiar({ objetivos: alternar(d.objetivos, o.id, 3) })} texto={o.nombre} nota={o.enfoque} />
            ))}
          </div>
        </>
      )}

      {paso === 1 && (
        <>
          <Titulo texto="Si no sabes tu peso o tu estatura, déjalos en blanco: la enfermera los mide en la visita.">Cuéntanos de tu cuerpo.</Titulo>
          <div className="mt-8 grid grid-cols-2 gap-4">
            <Campo etiqueta="Peso (kg)">
              <input inputMode="decimal" value={peso} onChange={(e) => setPeso(e.target.value.replace(",", ".").replace(/[^\d.]/g, ""))} className={claseEntrada} placeholder="70" />
            </Campo>
            <Campo etiqueta="Estatura (cm)">
              <input inputMode="numeric" value={talla} onChange={(e) => setTalla(e.target.value.replace(/\D/g, "").slice(0, 3))} className={claseEntrada} placeholder="165" />
            </Campo>
          </div>
          <p className="mt-8 text-base text-ink">{C.actividad.texto}</p>
          <div className="mt-4 grid gap-3 sm:grid-cols-2">
            {C.actividad.opciones.map((o) => (
              <Opcion key={o.id} activa={d.nivel_actividad === o.id} onClick={() => cambiar({ nivel_actividad: o.id })} texto={o.texto} />
            ))}
          </div>
        </>
      )}

      {paso === 2 && (
        <>
          <Titulo texto={C.biotina.ayuda}>{C.biotina.texto}</Titulo>
          <div className="mt-6 grid grid-cols-2 gap-3">
            <Opcion activa={d.toma_biotina === true} onClick={() => cambiar({ toma_biotina: true })} texto="Sí" />
            <Opcion activa={d.toma_biotina === false} onClick={() => cambiar({ toma_biotina: false })} texto="No" />
          </div>
          <p className="mt-10 text-base text-ink">{C.medicamentos.texto}</p>
          <p className="mt-1 text-xs text-ink-muted">Algunos cambian lo que te podemos recomendar. Puedes elegir varios.</p>
          <div className="mt-4 grid gap-3">
            {C.medicamentos.opciones.map((o) => (
              <Opcion
                key={o.id}
                multiple
                activa={d.medicamentos.includes(o.id)}
                onClick={() => {
                  setSinMedicamentos(false);
                  cambiar({ medicamentos: alternar(d.medicamentos, o.id) });
                }}
                texto={o.texto}
              />
            ))}
            <Opcion
              multiple
              activa={sinMedicamentos}
              onClick={() => {
                setSinMedicamentos(!sinMedicamentos);
                cambiar({ medicamentos: [] });
              }}
              texto="No tomo ninguno de estos"
            />
          </div>
          <div className="mt-5">
            <Campo etiqueta="¿Tomas otros medicamentos?" ayuda="Escríbelos si los recuerdas; se los mostramos a tu médico.">
              <input value={d.medicamentos_otros ?? ""} onChange={(e) => cambiar({ medicamentos_otros: e.target.value })} className={claseEntrada} placeholder="Por ejemplo: losartán, levotiroxina…" />
            </Campo>
          </div>
        </>
      )}

      {paso === 3 && (
        <>
          <Titulo texto="Tus recetas y recomendaciones no incluirán lo que no puedes comer.">{C.alergias.texto}</Titulo>
          <div className="mt-6 grid gap-3 sm:grid-cols-2">
            {C.alergias.opciones.map((o) => (
              <Opcion
                key={o.id}
                multiple
                activa={d.alergias.includes(o.id)}
                onClick={() => {
                  setSinAlergias(false);
                  cambiar({ alergias: alternar(d.alergias, o.id) });
                }}
                texto={o.texto}
              />
            ))}
            <Opcion
              multiple
              activa={sinAlergias}
              onClick={() => {
                setSinAlergias(!sinAlergias);
                cambiar({ alergias: [] });
              }}
              texto="No tengo alergias ni intolerancias"
            />
          </div>
          <div className="mt-5">
            <Campo etiqueta={C.alergias.otra}>
              <input value={d.alergias_otras ?? ""} onChange={(e) => cambiar({ alergias_otras: e.target.value })} className={claseEntrada} />
            </Campo>
          </div>
          <p className="mt-10 text-base text-ink">{C.dieta.texto}</p>
          <div className="mt-4 grid gap-3">
            {C.dieta.opciones.map((o) => (
              <Opcion key={o.id} activa={d.dieta === o.id} onClick={() => cambiar({ dieta: o.id })} texto={o.texto} />
            ))}
          </div>
        </>
      )}

      {paso === 4 && (
        <>
          <Titulo texto="Sin juicios: nos ayuda a leer mejor tus resultados.">{C.fuma.texto}</Titulo>
          <div className="mt-6 grid gap-3">
            {C.fuma.opciones.map((o) => (
              <Opcion key={o.id} activa={d.fuma === o.id} onClick={() => cambiar({ fuma: o.id })} texto={o.texto} />
            ))}
          </div>
          <p className="mt-10 text-base text-ink">{C.alcohol.texto}</p>
          <div className="mt-4 grid gap-3 sm:grid-cols-2">
            {C.alcohol.opciones.map((o) => (
              <Opcion key={o.id} activa={d.alcohol === o.id} onClick={() => cambiar({ alcohol: o.id })} texto={o.texto} />
            ))}
          </div>
        </>
      )}

      {paso === 5 && (
        <>
          <Titulo texto="Algunas condiciones vienen de familia y cambian cómo leemos tus resultados.">{C.antecedentes.texto}</Titulo>
          <div className="mt-6 grid gap-3">
            {C.antecedentes.opciones.map((o) => (
              <Opcion
                key={o.id}
                multiple
                activa={d.antecedentes.includes(o.id)}
                onClick={() => {
                  setSinAntecedentes(false);
                  cambiar({ antecedentes: alternar(d.antecedentes, o.id) });
                }}
                texto={o.texto}
              />
            ))}
            <Opcion
              multiple
              activa={sinAntecedentes}
              onClick={() => {
                setSinAntecedentes(!sinAntecedentes);
                cambiar({ antecedentes: [] });
              }}
              texto="Ninguno, o no lo sé"
            />
          </div>
          {mujer && (
            <>
              <p className="mt-10 text-base text-ink">{C.embarazo.texto}</p>
              <div className="mt-4 grid grid-cols-3 gap-3">
                {C.embarazo.opciones.map((o) => (
                  <Opcion key={o.id} activa={d.embarazo === o.id} onClick={() => cambiar({ embarazo: o.id })} texto={o.texto} />
                ))}
              </div>
            </>
          )}
        </>
      )}
    </Pantalla>
  );
}
