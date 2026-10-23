import { useEffect, useMemo, useState, type ReactNode } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Check, ChevronDown, Globe, HeartPulse, MessageCircle, ScrollText, Search, Share2, ShieldCheck } from "lucide-react";
import { BotonGoogle } from "@/components/BotonGoogle";
import { Opcion } from "@/components/Formulario";
import { BotonChico, Ficha, PantallaPre, claseFicha } from "@/components/FlujoPre";
import { leerOrigen } from "@/lib/origen";
import { GROSOR_Y, TRAZO_Y } from "@/lib/trazo_y";
import { VERSION_AUTORIZACION_PRE, siguientePaso, supabase, useSesion, type Preregistro as DatosPre } from "@/lib/sesion";
import C from "@/lib/contenido.json";

/**
 * Preventa: pre-registro gratis (tabla preregistros). Sin documento, dirección ni datos clínicos.
 * Portada: logo, imagen, título y Google (o correo). Con sesión, 6 pantallas al estilo de un onboarding de celular
 * (FlujoPre): quién eres → cumpleaños → dónde vives → objetivo → alergias → términos.
 * Al final: escribir "hola" por WhatsApp para empezar la semana de recetas e invitar a alguien.
 * El anticipo no va aquí: lo pide el WhatsApp al terminar la semana.
 * En desarrollo, /preregistro?demo (y &paso=1..6 o demo=listo) muestra las pantallas sin cuenta, con datos de ejemplo.
 */

const LOCALIDADES = [
  "Usaquén", "Chapinero", "Santa Fe", "San Cristóbal", "Usme", "Tunjuelito", "Bosa", "Kennedy", "Fontibón", "Engativá",
  "Suba", "Barrios Unidos", "Teusaquillo", "Los Mártires", "Antonio Nariño", "Puente Aranda", "La Candelaria",
  "Rafael Uribe Uribe", "Ciudad Bolívar", "Sumapaz", "Municipio cercano a Bogotá", "Fuera de Bogotá",
];

const MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

const OTRO = "otro";

const params = new URLSearchParams(window.location.search);
const DEMO = import.meta.env.DEV && params.has("demo");
/** Se volvió de Google con la cuenta en la dirección: mientras Supabase la lee (y la borra de ahí), no se muestra la portada otra vez. */
const vuelveDeGoogle = () => /access_token|refresh_token/.test(window.location.hash);

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

/** Fecha AAAA-MM-DD si el día existe en ese mes y año; si no, "". */
function fechaDe(dia: string, mes: string, anio: string) {
  const d = Number(dia), m = Number(mes), a = Number(anio);
  if (!d || !m || anio.length !== 4) return "";
  const f = new Date(a, m - 1, d);
  if (f.getFullYear() !== a || f.getMonth() !== m - 1 || f.getDate() !== d) return "";
  return `${a}-${String(m).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
}

function Portada() {
  const [error, setError] = useState<string | null>(null);
  return (
    <main className="min-h-screen bg-white">
      <div className="mx-auto flex min-h-screen max-w-md flex-col px-6 pb-8 pt-6">
        <img src="/marca/saludly.svg" alt="Saludly" className="mx-auto h-10 w-auto" />
        <section className="rise flex flex-1 flex-col justify-center py-6">
          <img src="/preregistro/salmon.png" alt="Sartén con un filete de salmón y dos medios limones" width={1280} height={960} className="mx-auto w-full max-w-[22rem] mix-blend-multiply [mask-composite:intersect] [mask-image:linear-gradient(to_right,transparent,#000_8%,#000_92%,transparent),linear-gradient(to_bottom,transparent,#000_8%,#000_92%,transparent)]" />
          <div className="mt-4 text-center">
            <h1 className="text-balance text-[28px] font-normal leading-tight tracking-tight text-ink">Una receta y recomendaciones saludables al día, 7 días gratis.</h1>
            <p className="mx-auto mt-3 max-w-[22rem] text-pretty text-base leading-relaxed text-ink-muted">
              Te llega por WhatsApp con un consejo de salud. Y quedas de primero en la lista de Saludly en Bogotá.
            </p>
          </div>
        </section>
        <div>
          {error && <p className="mb-3 rounded-xl bg-critical-soft px-4 py-2 text-center text-sm text-critical">{error}</p>}
          <BotonGoogle texto="signup_with" alError={setError} />
          <a href="/entrar" className="mt-4 block text-center text-[15px] text-ink-muted underline-offset-4 hover:underline">
            Prefiero usar mi correo
          </a>
          <p className="mt-5 text-center text-xs text-ink-faint">
            Es gratis. Lee cómo cuidamos tus datos en la{" "}
            <a href="/privacidad" target="_blank" rel="noreferrer" className="underline">
              política de datos
            </a>
            .
          </p>
        </div>
      </div>
    </main>
  );
}

function Listo({ datos }: { datos: Pick<DatosPre, "nombre" | "codigo"> }) {
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
  const nombre = datos.nombre.split(" ")[0];
  const mensaje = `Hola, soy ${datos.nombre}. Quiero empezar mi semana de recetas en Saludly. Mi código es ${datos.codigo}.`;
  const enlace = `${window.location.origin}/preregistro?ref=amigo-${datos.codigo}`;
  const invitar = async () => {
    const texto = "Me inscribí en Saludly: 7 días de recetas y recomendaciones saludables gratis por WhatsApp. Inscríbete aquí:";
    try {
      if (navigator.share) return await navigator.share({ title: "Saludly", text: texto, url: enlace });
      await navigator.clipboard.writeText(`${texto} ${enlace}`);
      setCopiado(true);
    } catch {
      /* compartir cancelado o sin portapapeles */
    }
  };
  return (
    <main className="min-h-screen bg-white">
      <div className="mx-auto flex min-h-screen max-w-md flex-col justify-center px-6 py-10 text-center">
        {/* La "y" de Saludly se dibuja de punta a punta, sin parar. */}
        <svg viewBox="0 0 981.45 1248.02" className="mx-auto h-44 w-auto" role="img" aria-label="Saludly">
          <path d={TRAZO_Y} pathLength={1} className="trazo-espera" fill="none" stroke="#2793ff" strokeWidth={GROSOR_Y} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <h1 className="mt-10 text-balance text-[30px] font-normal leading-tight tracking-tight text-ink">¡Ya estás en la lista, {nombre}!</h1>
        <p className="mx-auto mt-3 max-w-[22rem] text-pretty text-[17px] leading-relaxed text-ink-muted">
          Escríbenos por WhatsApp para empezar tu semana de recetas. Así sabemos que el número es tuyo y te llega la primera receta con recomendaciones y hábitos saludables.
        </p>
        <a
          href={whatsapp ? `https://wa.me/${whatsapp}?text=${encodeURIComponent(mensaje)}` : undefined}
          target="_blank"
          rel="noreferrer"
          className="mt-9 flex h-14 w-full items-center justify-center gap-2.5 rounded-full bg-[#25D366] px-4 text-base text-white"
        >
          <MessageCircle className="h-5 w-5" />
          Empezar mi semana por WhatsApp
        </a>
        <button type="button" onClick={() => void invitar()} className="mt-3 flex h-14 w-full items-center justify-center gap-2.5 rounded-full bg-[#f2f4f7] px-4 text-[14px] whitespace-nowrap text-ink">
          <Share2 className="h-5 w-5" />
          {copiado ? "Enlace copiado" : "Invita a alguien a quien le sirva como a ti"}
        </button>
      </div>
    </main>
  );
}

/** Fila de los términos: ícono en cuadro gris y texto; abre la política de datos. */
function Termino({ icono, children }: { icono: ReactNode; children: ReactNode }) {
  return (
    <a href="/privacidad" target="_blank" rel="noreferrer" className="flex items-center gap-4 py-3">
      <span className="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-[#f2f4f7] text-ink">{icono}</span>
      <span className="text-base leading-snug text-ink">{children}</span>
    </a>
  );
}

export function Preregistro() {
  const s = useSesion();
  const navigate = useNavigate();
  const ejemplo = DEMO;
  const [paso, setPaso] = useState(Math.min(6, Math.max(1, Number(params.get("paso")) || 1)));
  const [nombre, setNombre] = useState(ejemplo ? "Ana María Rojas" : "");
  const [celular, setCelular] = useState(ejemplo ? "3001234567" : "");
  const [sexo, setSexo] = useState<"hombre" | "mujer" | "">(ejemplo ? "mujer" : "");
  const [dia, setDia] = useState(ejemplo ? "14" : "");
  const [mes, setMes] = useState(ejemplo ? "3" : "");
  const [anio, setAnio] = useState(ejemplo ? "1988" : "");
  const [localidad, setLocalidad] = useState(ejemplo ? "Chapinero" : "");
  const [buscar, setBuscar] = useState("");
  const [metas, setMetas] = useState<string[]>(ejemplo ? ["salud_general", "bajar_peso"] : []);
  const [otro, setOtro] = useState("");
  const [alergias, setAlergias] = useState<string[]>([]);
  const [sinAlergias, setSinAlergias] = useState(ejemplo);
  const [acepta, setAcepta] = useState(ejemplo);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [demoListo, setDemoListo] = useState(DEMO && params.get("demo") === "listo");

  // Pacientes, clientes y el equipo siguen su propio flujo.
  useEffect(() => {
    if (DEMO || s.cargando || !s.sesion) return;
    const ir = siguientePaso(s);
    if (ir !== "/preregistro") void navigate({ to: ir });
  }, [s, navigate]);

  // El nombre sale de la cuenta de Google.
  useEffect(() => {
    const n = s.sesion?.user.user_metadata?.full_name;
    if (typeof n === "string") setNombre((x) => x || n);
  }, [s.sesion]);

  // Localidades que coinciden con la búsqueda; la elegida va de primera, separada de las demás.
  const lista = useMemo(() => {
    const sinTilde = (t: string) => t.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
    const filtradas = LOCALIDADES.filter((l) => sinTilde(l).includes(sinTilde(buscar.trim())));
    return localidad && filtradas.includes(localidad) ? [localidad, ...filtradas.filter((l) => l !== localidad)] : filtradas;
  }, [buscar, localidad]);

  if (DEMO && demoListo) return <Listo datos={{ nombre, codigo: "a1b2c3" }} />;
  if (!DEMO) {
    if (s.cargando) return <div className="min-h-screen bg-white" />;
    if (!s.sesion) return vuelveDeGoogle() ? <div className="min-h-screen bg-white" /> : <Portada />;
    if (s.preregistro) return <Listo datos={s.preregistro} />;
  }
  if (DEMO && params.get("demo") === "portada") return <Portada />;

  const nacimiento = fechaDe(dia, mes, anio);
  const edad = edadDe(nacimiento);
  const datosValidos = nombre.trim().length >= 3 && /^3\d{9}$/.test(celular);
  const fechaValida = !!nacimiento && edad >= 18 && edad <= 110;
  const metasValidas = metas.length > 0 && (!metas.includes(OTRO) || otro.trim().length >= 3);
  const alergiasValidas = sinAlergias || alergias.length > 0;
  const cambiarCuenta = <BotonChico onClick={() => void s.salir()}>Salir</BotonChico>;

  const inscribir = async () => {
    if (DEMO) return setDemoListo(true);
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
      alergias,
      dieta: null,
      quiere_prueba: true,
      acepta_datos: true,
      acepta_contacto: true,
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
      <PantallaPre paso={1} titulo="Cuéntanos quién eres" boton="Siguiente" puedeSeguir={datosValidos} onSeguir={() => setPaso(2)} derecha={cambiarCuenta}>
        <div className="grid gap-3">
          <Ficha etiqueta="Nombre">
            <input autoComplete="name" value={nombre} onChange={(e) => setNombre(e.target.value)} className={claseFicha} />
          </Ficha>
          <Ficha etiqueta="Celular con WhatsApp">
            <span className="text-ink-muted">+57</span>
            <input inputMode="tel" autoComplete="tel-national" value={celular} onChange={(e) => setCelular(e.target.value.replace(/\D/g, "").slice(0, 10))} className={claseFicha} placeholder="300 123 4567" />
          </Ficha>
          <Ficha etiqueta="Sexo (opcional)">
            <select value={sexo} onChange={(e) => setSexo(e.target.value as "hombre" | "mujer" | "")} className={claseFicha}>
              <option value="">Prefiero no decirlo</option>
              <option value="mujer">Femenino</option>
              <option value="hombre">Masculino</option>
            </select>
            <ChevronDown className="h-5 w-5 shrink-0 text-ink-muted" />
          </Ficha>
        </div>
      </PantallaPre>
    );

  if (paso === 2)
    return (
      <PantallaPre paso={2} titulo="¿Cuándo es tu cumpleaños?" boton="Siguiente" puedeSeguir={fechaValida} onSeguir={() => setPaso(3)} onAtras={() => setPaso(1)} derecha={cambiarCuenta}>
        <div className="grid grid-cols-[1fr_1.7fr_1.3fr] gap-3">
          <Ficha etiqueta="Día">
            <input inputMode="numeric" autoComplete="bday-day" value={dia} onChange={(e) => setDia(e.target.value.replace(/\D/g, "").slice(0, 2))} className={claseFicha} placeholder="20" />
          </Ficha>
          <Ficha etiqueta="Mes">
            <select autoComplete="bday-month" value={mes} onChange={(e) => setMes(e.target.value)} className={claseFicha}>
              <option value="" disabled>
                Elige
              </option>
              {MESES.map((m, i) => (
                <option key={m} value={String(i + 1)}>
                  {m}
                </option>
              ))}
            </select>
          </Ficha>
          <Ficha etiqueta="Año">
            <input inputMode="numeric" autoComplete="bday-year" value={anio} onChange={(e) => setAnio(e.target.value.replace(/\D/g, "").slice(0, 4))} className={claseFicha} placeholder="1990" />
          </Ficha>
        </div>
        {nacimiento && edad < 18 && <p className="mt-4 text-sm text-critical">Saludly es solo para mayores de 18 años.</p>}
        {dia && mes && anio.length === 4 && !nacimiento && <p className="mt-4 text-sm text-critical">Revisa la fecha: ese día no existe.</p>}
      </PantallaPre>
    );

  if (paso === 3)
    return (
      <PantallaPre paso={3} titulo="¿Dónde vives?" boton="Siguiente" puedeSeguir={localidad !== ""} onSeguir={() => setPaso(4)} onAtras={() => setPaso(2)} derecha={cambiarCuenta}>
        <label className="flex items-center gap-3 rounded-[22px] bg-[#f2f4f7] px-5 py-4">
          <Search className="h-5 w-5 shrink-0 text-ink-muted" />
          <input value={buscar} onChange={(e) => setBuscar(e.target.value)} className={claseFicha} placeholder="Buscar localidad" aria-label="Buscar localidad" />
        </label>
        <ul className="mt-4">
          {lista.map((l, i) => {
            const activa = l === localidad;
            return (
              <li key={l} className={activa && i === 0 && lista.length > 1 ? "border-b border-rule" : ""}>
                <button type="button" onClick={() => setLocalidad(l)} aria-pressed={activa} className="flex w-full items-center gap-4 py-3.5 text-left">
                  <span className="grid h-11 w-11 shrink-0 place-items-center rounded-full bg-[#eaf3ff] text-sm font-medium text-[#2793ff]">
                    {l
                      .split(" ")
                      .filter((p) => p.length > 2)
                      .slice(0, 2)
                      .map((p) => p[0])
                      .join("")}
                  </span>
                  <span className="flex-1 text-[17px] text-ink">{l}</span>
                  <span className={`grid h-6 w-6 place-items-center rounded-full border-2 ${activa ? "border-ink" : "border-rule"}`}>{activa && <span className="h-3 w-3 rounded-full bg-ink" />}</span>
                </button>
              </li>
            );
          })}
          {lista.length === 0 && <li className="py-4 text-sm text-ink-muted">No encontramos esa localidad.</li>}
        </ul>
      </PantallaPre>
    );

  if (paso === 4)
    return (
      <PantallaPre
        paso={4}
        titulo="¿Cuál es tu objetivo?"
        texto="Elige hasta 3. Con ellos escogemos tus recetas y consejos."
        boton="Siguiente"
        puedeSeguir={metasValidas}
        onSeguir={() => setPaso(5)}
        onAtras={() => setPaso(3)}
        derecha={cambiarCuenta}
      >
        <div className="grid gap-3">
          {C.objetivos.map((o) => (
            <Opcion key={o.id} multiple activa={metas.includes(o.id)} onClick={() => setMetas(alternar(metas, o.id, 3))} texto={o.nombre} />
          ))}
          <Opcion multiple activa={metas.includes(OTRO)} onClick={() => setMetas(alternar(metas, OTRO, 3))} texto="Otro" />
          {metas.includes(OTRO) && (
            <Ficha etiqueta="¿Cuál es tu otro objetivo?">
              <input value={otro} maxLength={200} onChange={(e) => setOtro(e.target.value)} className={claseFicha} placeholder="Por ejemplo: controlar el estrés" />
            </Ficha>
          )}
        </div>
      </PantallaPre>
    );

  if (paso === 5)
    return (
      <PantallaPre
        paso={5}
        titulo="Solo para saber qué recomendarte, dinos si tienes alergias"
        texto="Tus recetas no incluirán lo que no puedes comer."
        boton="Siguiente"
        puedeSeguir={alergiasValidas}
        onSeguir={() => setPaso(6)}
        onAtras={() => setPaso(4)}
        derecha={cambiarCuenta}
      >
        <div className="grid gap-3">
          <Opcion
            multiple
            activa={sinAlergias}
            onClick={() => {
              setSinAlergias(!sinAlergias);
              setAlergias([]);
            }}
            texto="No tengo alergias"
          />
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
        </div>
      </PantallaPre>
    );

  return (
    <PantallaPre
      paso={6}
      titulo="Revisa y acepta los términos"
      texto="Al marcar la casilla confirmas que tienes 18 años o más y aceptas recibir por WhatsApp y correo tu semana de recetas y novedades. Te das de baja escribiendo «BAJA»."
      boton="Aceptar y continuar"
      puedeSeguir={acepta}
      ocupado={ocupado}
      onSeguir={() => void inscribir()}
      onAtras={() => setPaso(5)}
      derecha={cambiarCuenta}
      error={error}
      encimaBoton={
        <button type="button" onClick={() => setAcepta((v) => !v)} aria-pressed={acepta} className="flex items-center gap-3 rounded-[20px] bg-[#f2f4f7] px-6 py-3.5 text-[17px] text-ink">
          {acepta ? "Aceptado" : "Acepto"}
          <span className={`grid h-6 w-6 place-items-center rounded-md border-2 ${acepta ? "border-ink bg-ink text-white" : "border-ink/30"}`}>{acepta && <Check className="h-4 w-4" strokeWidth={3} />}</span>
        </button>
      }
    >
      <div className="grid gap-1">
        <Termino icono={<ShieldCheck className="h-6 w-6" />}>Autorización de tratamiento de datos (Ley 1581)</Termino>
        <Termino icono={<HeartPulse className="h-6 w-6" />}>Tus alergias son datos sensibles: solo para tus recetas</Termino>
        <Termino icono={<Globe className="h-6 w-6" />}>Servidores fuera de Colombia (Supabase, Vercel, Google y Meta)</Termino>
        <Termino icono={<ScrollText className="h-6 w-6" />}>Tus derechos: conocer, corregir o borrar tus datos</Termino>
      </div>
    </PantallaPre>
  );
}
