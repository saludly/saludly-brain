import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { MessageCircle, Salad, Share2, Stethoscope } from "lucide-react";
import { BotonGoogle } from "@/components/BotonGoogle";
import { Marca } from "@/components/Comunes";
import { Campo, Opcion, Pantalla, Titulo, claseEntrada } from "@/components/Formulario";
import { leerOrigen } from "@/lib/origen";
import { GROSOR_Y, TRAZO_Y } from "@/lib/trazo_y";
import { VERSION_AUTORIZACION_PRE, siguientePaso, supabase, useSesion } from "@/lib/sesion";
import C from "@/lib/contenido.json";

/**
 * Preventa: pre-registro gratis (tabla preregistros). Sin documento, dirección ni datos clínicos.
 * Sin sesión: qué es Saludly y la semana de prueba, y el botón de Google.
 * Con sesión: datos básicos, 3 metas (con "Otro"), semana de prueba (alergias y dieta para las recetas) y autorización.
 * Al final: escribir "hola" por WhatsApp para empezar la semana de prueba y el enlace para invitar amigos.
 * El anticipo no va aquí: lo pide el WhatsApp al terminar la semana.
 */

const LOCALIDADES = [
  "Usaquén", "Chapinero", "Santa Fe", "San Cristóbal", "Usme", "Tunjuelito", "Bosa", "Kennedy", "Fontibón", "Engativá",
  "Suba", "Barrios Unidos", "Teusaquillo", "Los Mártires", "Antonio Nariño", "Puente Aranda", "La Candelaria",
  "Rafael Uribe Uribe", "Ciudad Bolívar", "Sumapaz", "Municipio cercano a Bogotá", "Fuera de Bogotá",
];

const OTRO = "otro";

function alternar(lista: string[], id: string, maximo?: number) {
  if (lista.includes(id)) return lista.filter((x) => x !== id);
  if (maximo && lista.length >= maximo) return lista;
  return [...lista, id];
}

/** Años cumplidos a hoy. */
function edadDe(fecha: string) {
  const [a, m, d] = fecha.split("-").map(Number);
  if (!a || !m || !d) return NaN;
  const hoy = new Date();
  return hoy.getFullYear() - a - (hoy.getMonth() + 1 < m || (hoy.getMonth() + 1 === m && hoy.getDate() < d) ? 1 : 0);
}

function hoyISO() {
  const h = new Date();
  return `${h.getFullYear()}-${String(h.getMonth() + 1).padStart(2, "0")}-${String(h.getDate()).padStart(2, "0")}`;
}

function Presentacion() {
  const [error, setError] = useState<string | null>(null);
  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-md flex-col px-6 py-8">
        <Marca derecha="Pre-registro" />
        <section className="rise mt-12">
          <h1 className="text-3xl font-light tracking-tight text-ink">Conoce tu salud antes de que te avise.</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">
            Saludly es un estudio preventivo de sangre en Bogotá: más de 100 marcadores, la toma en tu casa y un informe en palabras claras que revisa un médico. No es un diagnóstico.
          </p>
          <div className="mt-8 space-y-3">
            {[
              { icono: Salad, t: "Una semana de recetas y recomendaciones de salud gratis", d: "Durante 7 días te mandamos por WhatsApp una receta saludable y un consejo de salud. Sin tarjeta y sin compromiso." },
              { icono: Stethoscope, t: "Tu lugar en la lista", d: "Cuando abramos los cupos en Bogotá te avisaremos primero, con los beneficios exclusivos para los primeros." },
            ].map(({ icono: Icono, t, d }) => (
              <div key={t} className="flex gap-4 rounded-2xl bg-surface p-4">
                <Icono className="mt-0.5 h-5 w-5 shrink-0 text-optimal" />
                <div>
                  <p className="text-sm text-ink">{t}</p>
                  <p className="mt-1 text-xs leading-relaxed text-ink-muted">{d}</p>
                </div>
              </div>
            ))}
          </div>
          <div className="mt-8">
            <BotonGoogle texto="signup_with" alError={setError} />
          </div>
          {error && <p className="mt-4 rounded-xl bg-critical-soft px-4 py-2 text-sm text-critical">{error}</p>}
          <a href="/entrar" className="mt-4 block text-center text-sm text-optimal underline-offset-4 hover:underline">
            Prefiero usar mi correo
          </a>
          <p className="mt-8 text-center text-xs text-ink-faint">
            Toma 1 minuto. Lee cómo cuidamos tus datos en la{" "}
            <a href="/privacidad" target="_blank" rel="noreferrer" className="underline">
              política de datos
            </a>
            .
          </p>
        </section>
      </div>
    </main>
  );
}

/** Para quien entró con otra cuenta de Google: cierra la sesión y vuelve a la presentación. */
function OtraCuenta() {
  const s = useSesion();
  return (
    <p className="mt-6 text-center text-xs text-ink-faint">
      Entraste como {s.sesion?.user.email}.{" "}
      <button type="button" onClick={() => void s.salir()} className="text-optimal underline-offset-4 hover:underline">
        Usar otra cuenta
      </button>
    </p>
  );
}

function YaInscrito() {
  const s = useSesion();
  const [whatsapp, setWhatsapp] = useState<string | null>(null);
  const [copiado, setCopiado] = useState(false);
  useEffect(() => {
    void supabase
      .from("configuracion")
      .select("valor")
      .eq("clave", "whatsapp_saludly")
      .maybeSingle()
      .then(({ data }) => setWhatsapp(data?.valor ?? null));
  }, []);
  const p = s.preregistro!;
  const nombre = p.nombre.split(" ")[0];
  const mensaje = p.quiere_prueba
    ? `Hola, soy ${p.nombre}. Quiero empezar mi semana de prueba en Saludly. Mi código es ${p.codigo}.`
    : `Hola, soy ${p.nombre}. Ya me pre-registré en Saludly. Mi código es ${p.codigo}.`;
  const enlace = `${window.location.origin}/preregistro?ref=amigo-${p.codigo}`;
  const invitar = async () => {
    const texto = "Me inscribí en Saludly, un estudio preventivo de sangre en Bogotá. Tienen una semana de prueba gratis por WhatsApp:";
    try {
      if (navigator.share) return await navigator.share({ text: texto, url: enlace });
      await navigator.clipboard.writeText(`${texto} ${enlace}`);
      setCopiado(true);
    } catch {
      /* compartir cancelado o sin portapapeles: el enlace queda visible */
    }
  };
  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-md flex-col px-6 py-8">
        <Marca derecha="Pre-registro" />
        <section className="rise mt-10">
          {/* La "y" de Saludly se dibuja de punta a punta, como en la espera de resultados. */}
          <svg viewBox="0 0 981.45 1248.02" className="mx-auto h-28 w-auto" role="img" aria-label="Saludly">
            <path d={TRAZO_Y} pathLength={1} className="trazo-espera" fill="none" stroke="#2793ff" strokeWidth={GROSOR_Y} strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          <h1 className="mt-10 text-3xl font-light tracking-tight text-ink">¡Ya estás en la lista, {nombre}!</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">
            {p.quiere_prueba
              ? "Último paso: escríbenos por WhatsApp para empezar tu semana de prueba. Así sabemos que el número es tuyo y te llega la primera receta."
              : "Te avisaremos por WhatsApp cuando abramos los cupos en Bogotá. Escríbenos para guardar nuestro número."}
          </p>
          {whatsapp && (
            <a
              href={`https://wa.me/${whatsapp}?text=${encodeURIComponent(mensaje)}`}
              target="_blank"
              rel="noreferrer"
              className="mt-8 flex w-full items-center justify-center gap-3 rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground"
            >
              <MessageCircle className="h-5 w-5" />
              {p.quiere_prueba ? "Empezar mi semana por WhatsApp" : "Escribir a Saludly por WhatsApp"}
            </a>
          )}
          <div className="mt-10 rounded-2xl bg-surface p-5">
            <p className="text-sm text-ink">¿Conoces a alguien a quien le sirva?</p>
            <p className="mt-1 text-xs leading-relaxed text-ink-muted">Compártele tu enlace y tendrás mejores beneficios.</p>
            <p className="mt-3 break-all font-mono text-xs text-ink-faint">{enlace}</p>
            <button type="button" onClick={() => void invitar()} className="mt-4 flex items-center gap-2 rounded-full border border-rule px-5 py-2.5 text-sm text-ink">
              <Share2 className="h-4 w-4" />
              {copiado ? "Copiado" : "Invitar"}
            </button>
          </div>
          <OtraCuenta />
        </section>
      </div>
    </main>
  );
}

export function Preregistro() {
  const s = useSesion();
  const navigate = useNavigate();
  const [paso, setPaso] = useState(1);
  const [nombre, setNombre] = useState("");
  const [celular, setCelular] = useState("");
  const [nacimiento, setNacimiento] = useState("");
  const [sexo, setSexo] = useState<"hombre" | "mujer" | "">("");
  const [localidad, setLocalidad] = useState("");
  const [metas, setMetas] = useState<string[]>([]);
  const [otro, setOtro] = useState("");
  const [quierePrueba, setQuierePrueba] = useState<boolean | null>(null);
  const [alergias, setAlergias] = useState<string[]>([]);
  const [sinAlergias, setSinAlergias] = useState(false);
  const [dieta, setDieta] = useState<string | null>(null);
  const [aceptaDatos, setAceptaDatos] = useState(false);
  const [aceptaContacto, setAceptaContacto] = useState(false);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Pacientes, clientes y el equipo siguen su propio flujo.
  useEffect(() => {
    if (s.cargando || !s.sesion) return;
    const ir = siguientePaso(s);
    if (ir !== "/preregistro") void navigate({ to: ir });
  }, [s, navigate]);

  // El nombre sale de la cuenta de Google.
  useEffect(() => {
    const n = s.sesion?.user.user_metadata?.full_name;
    if (typeof n === "string") setNombre((x) => x || n);
  }, [s.sesion]);

  if (s.cargando) return <div className="min-h-screen bg-background" />;
  if (!s.sesion) return <Presentacion />;
  if (s.preregistro) return <YaInscrito />;

  const edad = edadDe(nacimiento);
  const datosValidos = nombre.trim().length >= 3 && /^3\d{9}$/.test(celular) && edad >= 18 && edad <= 110 && localidad !== "";
  const metasValidas = metas.length > 0 && (!metas.includes(OTRO) || otro.trim().length >= 3);
  const pruebaValida = quierePrueba === false || (quierePrueba === true && dieta !== null && (sinAlergias || alergias.length > 0));

  const inscribir = async () => {
    setOcupado(true);
    setError(null);
    const { fuente, referido_por } = leerOrigen();
    const { error } = await supabase.from("preregistros").insert({
      nombre: nombre.trim(),
      correo: s.sesion!.user.email ?? null,
      celular_whatsapp: `57${celular}`,
      fecha_nacimiento: nacimiento,
      sexo: sexo || null,
      localidad,
      objetivos: metas,
      objetivo_otro: metas.includes(OTRO) ? otro.trim() : null,
      alergias: quierePrueba ? alergias : [],
      dieta: quierePrueba ? dieta : null,
      quiere_prueba: quierePrueba === true,
      acepta_datos: true,
      acepta_contacto: aceptaContacto,
      version_autorizacion: VERSION_AUTORIZACION_PRE,
      agente: navigator.userAgent.slice(0, 300),
      fuente,
      referido_por,
    });
    setOcupado(false);
    if (error) return setError("No pudimos guardar tu inscripción. Revisa tu conexión e intenta de nuevo.");
    await s.recargar();
  };

  if (paso === 1)
    return (
      <Pantalla paso={1} total={4} etiqueta="Tus datos" boton="Continuar" puedeSeguir={datosValidos} onSeguir={() => setPaso(2)}>
        <Titulo texto="Solo lo básico. No te pedimos documento ni dirección.">Cuéntanos quién eres.</Titulo>
        <OtraCuenta />
        <div className="mt-8 space-y-5">
          <Campo etiqueta="Nombre">
            <input autoComplete="name" value={nombre} onChange={(e) => setNombre(e.target.value)} className={claseEntrada} />
          </Campo>
          <Campo etiqueta="Celular con WhatsApp" ayuda="Ahí te llega la semana de prueba.">
            <div className="flex gap-2">
              <span className="rounded-2xl border border-rule bg-surface px-4 py-3.5 text-base text-ink-muted">+57</span>
              <input inputMode="tel" autoComplete="tel-national" value={celular} onChange={(e) => setCelular(e.target.value.replace(/\D/g, "").slice(0, 10))} className={claseEntrada} placeholder="300 123 4567" />
            </div>
          </Campo>
          <Campo etiqueta="Fecha de nacimiento" ayuda={nacimiento && !Number.isNaN(edad) ? (edad < 18 ? "Saludly es solo para mayores de 18 años." : `Tienes ${edad} años.`) : undefined}>
            <input type="date" autoComplete="bday" min="1900-01-01" max={hoyISO()} value={nacimiento} onChange={(e) => setNacimiento(e.target.value)} className={claseEntrada} />
          </Campo>
          <Campo etiqueta="Sexo" ayuda="Opcional. Nos ayuda a elegir tus consejos.">
            <select value={sexo} onChange={(e) => setSexo(e.target.value as "hombre" | "mujer" | "")} className={claseEntrada}>
              <option value="">Prefiero no decirlo</option>
              <option value="hombre">Masculino</option>
              <option value="mujer">Femenino</option>
            </select>
          </Campo>
          <Campo etiqueta="¿En qué localidad vives?">
            <select value={localidad} onChange={(e) => setLocalidad(e.target.value)} className={claseEntrada}>
              <option value="" disabled>
                Elige una opción
              </option>
              {LOCALIDADES.map((l) => (
                <option key={l} value={l}>
                  {l}
                </option>
              ))}
            </select>
          </Campo>
        </div>
      </Pantalla>
    );

  if (paso === 2)
    return (
      <Pantalla paso={2} total={4} etiqueta="Tus metas" boton="Continuar" puedeSeguir={metasValidas} onSeguir={() => setPaso(3)} onAtras={() => setPaso(1)}>
        <Titulo texto="Elige hasta 3. Con ellas escogemos tus recetas y consejos.">¿Para qué quieres Saludly?</Titulo>
        <p className="mt-4 font-mono text-[10px] uppercase tracking-[0.16em] text-ink-faint">{metas.length} de 3 elegidas</p>
        <div className="mt-5 grid gap-3 sm:grid-cols-2">
          {C.objetivos.map((o) => (
            <Opcion key={o.id} multiple activa={metas.includes(o.id)} onClick={() => setMetas(alternar(metas, o.id, 3))} texto={o.nombre} />
          ))}
          <Opcion multiple activa={metas.includes(OTRO)} onClick={() => setMetas(alternar(metas, OTRO, 3))} texto="Otro" nota="Escríbelo con tus palabras." />
        </div>
        {metas.includes(OTRO) && (
          <div className="mt-5">
            <Campo etiqueta="¿Cuál es tu otra meta?">
              <input value={otro} maxLength={200} onChange={(e) => setOtro(e.target.value)} className={claseEntrada} placeholder="Por ejemplo: controlar el estrés" />
            </Campo>
          </div>
        )}
      </Pantalla>
    );

  if (paso === 3)
    return (
      <Pantalla paso={3} total={4} etiqueta="Semana de prueba" boton="Continuar" puedeSeguir={pruebaValida} onSeguir={() => setPaso(4)} onAtras={() => setPaso(2)}>
        <Titulo texto="7 días, una receta saludable y un consejo de salud cada día por WhatsApp. Gratis.">¿Quieres tu semana de prueba?</Titulo>
        <div className="mt-6 grid gap-3">
          <Opcion activa={quierePrueba === true} onClick={() => setQuierePrueba(true)} texto="Sí, quiero mi semana de prueba" />
          <Opcion activa={quierePrueba === false} onClick={() => setQuierePrueba(false)} texto="No por ahora, solo avísenme cuando abran los cupos" />
        </div>
        {quierePrueba && (
          <>
            <h2 className="mt-10 text-lg font-light text-ink">{C.alergias.texto}</h2>
            <p className="mt-1 text-sm text-ink-muted">Tus recetas no incluirán lo que no puedes comer.</p>
            <div className="mt-4 grid gap-3 sm:grid-cols-2">
              {C.alergias.opciones.map((o) => (
                <Opcion
                  key={o.id}
                  multiple
                  activa={alergias.includes(o.id)}
                  onClick={() => {
                    setAlergias(alternar(alergias, o.id));
                    setSinAlergias(false);
                  }}
                  texto={o.texto}
                />
              ))}
              <Opcion
                multiple
                activa={sinAlergias}
                onClick={() => {
                  setSinAlergias(!sinAlergias);
                  setAlergias([]);
                }}
                texto="No tengo alergias ni intolerancias"
              />
            </div>
            <h2 className="mt-10 text-lg font-light text-ink">{C.dieta.texto}</h2>
            <div className="mt-4 grid gap-3">
              {C.dieta.opciones.map((o) => (
                <Opcion key={o.id} activa={dieta === o.id} onClick={() => setDieta(o.id)} texto={o.texto} />
              ))}
            </div>
          </>
        )}
      </Pantalla>
    );

  return (
    <Pantalla paso={4} total={4} etiqueta="Tus datos son privados" boton="Inscribirme" puedeSeguir={aceptaDatos && (!quierePrueba || aceptaContacto)} ocupado={ocupado} onSeguir={() => void inscribir()} onAtras={() => setPaso(3)} error={error}>
      <Titulo>Antes de inscribirte: tus datos.</Titulo>
      <div className="mt-6 space-y-4 text-sm leading-relaxed text-ink-muted">
        <p>
          <strong className="font-medium text-ink">Qué datos.</strong> Tu nombre, correo, celular, fecha de nacimiento, sexo si nos lo das, localidad y tus metas. Si pides la semana de prueba, también tus alergias y tu tipo de alimentación: son datos sensibles y no estás obligado a darlos.
        </p>
        <p>
          <strong className="font-medium text-ink">Para qué.</strong> Para enviarte la semana de prueba, avisarte cuando abramos los cupos en Bogotá con el precio, y saber cuántas personas están interesadas y de dónde llegan. No los vendemos ni los usamos para publicidad de otros.
        </p>
        <p>
          <strong className="font-medium text-ink">Servidores fuera de Colombia.</strong> Usamos proveedores con servidores en otros países (Supabase, Vercel, Google y Meta), que guardan tus datos solo por cuenta de Saludly.
        </p>
        <p>
          <strong className="font-medium text-ink">Tus derechos.</strong> Puedes conocer, corregir y borrar tus datos, o retirar esta autorización, escribiendo a carlos@saludly.online. Lee la{" "}
          <a href="/privacidad" target="_blank" rel="noreferrer" className="text-primary underline">
            Política de tratamiento de datos
          </a>
          .
        </p>
      </div>
      <div className="mt-8 grid gap-3">
        <Opcion
          multiple
          activa={aceptaDatos}
          onClick={() => setAceptaDatos((v) => !v)}
          texto="Tengo 18 años o más y autorizo a Saludly a tratar mis datos para lo descrito, incluida su transmisión a servidores fuera de Colombia."
          nota="Obligatoria para inscribirte."
        />
        <Opcion
          multiple
          activa={aceptaContacto}
          onClick={() => setAceptaContacto((v) => !v)}
          texto="Quiero recibir por WhatsApp y correo la semana de prueba, el aviso de apertura, el precio y los beneficios de Saludly."
          nota={quierePrueba ? "Necesaria para enviarte la semana de prueba. Puedes darte de baja escribiendo «BAJA»." : "Opcional. Puedes darte de baja escribiendo «BAJA»."}
        />
      </div>
    </Pantalla>
  );
}
