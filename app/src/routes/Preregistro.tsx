import { useEffect, useMemo, useRef, useState, type ReactNode } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Check, ChevronDown, Copy, Globe, HeartPulse, MessageCircle, ScrollText, Search, Share2, ShieldCheck } from "lucide-react";
import { BotonGoogle } from "@/components/BotonGoogle";
import { Opcion } from "@/components/Formulario";
import { Ficha, PantallaPre, claseFicha } from "@/components/FlujoPre";
import { leerOrigen } from "@/lib/origen";
import { GROSOR_Y, TRAZO_Y } from "@/lib/trazo_y";
import { VERSION_AUTORIZACION_PRE, siguientePaso, supabase, useSesion, type Preregistro as DatosPre } from "@/lib/sesion";
import C from "@/lib/contenido.json";

/**
 * Preventa: pre-registro gratis (tabla preregistros). Sin documento, dirección ni datos clínicos.
 * Portada: logo, imagen, título y Google (o correo). Con sesión, 6 pantallas al estilo de un onboarding de celular
 * (FlujoPre): quién eres → cumpleaños → dónde vives → objetivo → alergias → términos.
 * Al final: un consejo breve de su objetivo y escribir "hola" por WhatsApp para recibir la primera receta (el premio), e invitar a alguien.
 * Cada paso se guarda en el navegador (borrador por cuenta) para que nadie pierda lo que escribió si cierra la app.
 * Menores de edad: pueden inscribirse (Carlos, 24 oct 2026); los términos les piden que su mamá, papá o acudiente esté de acuerdo.
 * El anticipo no va aquí: lo pide el WhatsApp al terminar la semana.
 * En desarrollo, /preregistro?demo (y &paso=1..6 o demo=listo) muestra las pantallas sin cuenta, con datos de ejemplo.
 */

// "Fuera de Bogotá" va de primera para quien se inscribe desde otra ciudad o desde el exterior (24 oct 2026).
const LOCALIDADES = [
  "Fuera de Bogotá", "Usaquén", "Chapinero", "Santa Fe", "San Cristóbal", "Usme", "Tunjuelito", "Bosa", "Kennedy", "Fontibón", "Engativá",
  "Suba", "Barrios Unidos", "Teusaquillo", "Los Mártires", "Antonio Nariño", "Puente Aranda", "La Candelaria",
  "Rafael Uribe Uribe", "Ciudad Bolívar", "Sumapaz", "Municipio cercano a Bogotá",
];

/** Celular con indicativo, solo dígitos. Colombia (+57): 10 dígitos que empiezan por 3; otros países: de 6 a 13. */
function celularValido(indicativo: string, numero: string) {
  if (!/^[1-9]\d{0,3}$/.test(indicativo)) return false;
  if (indicativo === "57") return /^3\d{9}$/.test(numero);
  return /^\d{6,13}$/.test(numero) && (indicativo + numero).length <= 15;
}

const MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

const OTRO = "otro";

/** Número de WhatsApp de Saludly si no se puede leer de configuracion (para que el botón final nunca quede muerto). */
const WHATSAPP_SALUDLY = "573011307944";

/** Navegadores dentro de Facebook, Instagram o Messenger: Google no deja iniciar sesión ahí. */
const enFacebook = () => /FBAN|FBAV|FB_IAB|FBIOS|Instagram|Messenger/i.test(navigator.userAgent);

/** Borrador del pre-registro en este navegador, por cuenta. */
const claveBorrador = (id: string) => `saludly-pre-${id}`;

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

/** Dentro de Facebook: cómo abrir la misma página (con su ?ref=) en Chrome o Safari. */
function AvisoFacebook() {
  const [copiado, setCopiado] = useState(false);
  const url = window.location.href;
  const android = /Android/i.test(navigator.userAgent);
  const copiar = async () => {
    try {
      await navigator.clipboard.writeText(url);
      setCopiado(true);
    } catch {
      /* sin portapapeles */
    }
  };
  return (
    <div role="alert" className="mb-4 rounded-[22px] bg-ficha px-5 py-4 text-left">
      <p className="text-base text-ink">Estás dentro de Facebook y Google no deja entrar desde aquí.</p>
      <p className="mt-1 text-base text-ink-muted">
        {android ? "Ábrela en Chrome y sigue desde allá." : "Toca los tres puntos (···) de arriba y elige «Abrir en el navegador»."}
      </p>
      <div className="mt-3 flex flex-wrap gap-2">
        {android && (
          <a href={`intent://${url.replace(/^https?:\/\//, "")}#Intent;scheme=https;package=com.android.chrome;end`} className="rounded-full bg-ink px-4 py-2.5 text-base text-white">
            Abrir en Chrome
          </a>
        )}
        <button type="button" onClick={() => void copiar()} className="flex items-center gap-2 rounded-full bg-white px-4 py-2.5 text-base text-ink">
          <Copy className="h-4 w-4" />
          {copiado ? "Enlace copiado" : "Copiar enlace"}
        </button>
      </div>
    </div>
  );
}

function Portada() {
  const [error, setError] = useState<string | null>(null);
  const facebook = enFacebook() || (DEMO && params.has("facebook"));
  return (
    <main className="min-h-screen bg-white">
      <div className="mx-auto flex min-h-screen max-w-md flex-col px-6 pb-8 pt-6">
        <img src="/marca/saludly.svg" alt="Saludly" className="mx-auto h-10 w-auto" />
        <section className="rise flex flex-1 flex-col justify-center py-6">
          <img src="/preregistro/salmon.png" alt="Sartén con un filete de salmón y dos medios limones" width={1280} height={960} className="mx-auto w-full max-w-[22rem] mix-blend-multiply [mask-composite:intersect] [mask-image:linear-gradient(to_right,transparent,#000_8%,#000_92%,transparent),linear-gradient(to_bottom,transparent,#000_8%,#000_92%,transparent)]" />
          <div className="mt-4 text-center">
            <h1 className="text-balance text-[28px] font-normal leading-tight tracking-tight text-ink">Una receta y recomendaciones saludables al día, 7 días gratis.</h1>
            <p className="mx-auto mt-3 max-w-[22rem] text-pretty text-base leading-relaxed text-ink-muted">
              Te llega por WhatsApp con un consejo de salud. Al terminar, puedes apartar tu examen de sangre con enfermera a domicilio en Bogotá.
            </p>
          </div>
        </section>
        <div>
          {facebook && <AvisoFacebook />}
          {error && !facebook && <p role="alert" className="mb-3 rounded-xl bg-critical-soft px-4 py-2 text-center text-base text-critical">{error}</p>}
          <BotonGoogle texto="signup_with" alError={setError} />
          <a href="/entrar" className="mt-4 block text-center text-[15px] text-ink-muted underline-offset-4 hover:underline">
            Prefiero usar mi correo
          </a>
          <p className="mt-5 text-center text-base text-ink-muted">
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

/** El consejo breve del primer objetivo que eligió (con "Otro" o sin objetivo conocido, el de salud general). */
function consejoDe(objetivos: string[]) {
  const o = C.objetivos.find((x) => objetivos.includes(x.id)) ?? C.objetivos.find((x) => x.id === "salud_general")!;
  return { objetivo: o.nombre, consejo: o.consejo_inicio };
}

function Listo({ datos }: { datos: Pick<DatosPre, "nombre" | "codigo" | "objetivos"> }) {
  const [whatsapp, setWhatsapp] = useState(WHATSAPP_SALUDLY);
  const [copiado, setCopiado] = useState(false);
  useEffect(() => {
    void supabase
      .from("configuracion")
      .select("valor")
      .eq("clave", "whatsapp_saludly")
      .maybeSingle()
      .then(({ data }) => data?.valor && setWhatsapp(data.valor));
  }, []);
  const nombre = datos.nombre.split(" ")[0];
  const { objetivo, consejo } = consejoDe(datos.objetivos ?? []);
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
        <svg viewBox="0 0 981.45 1248.02" className="mx-auto h-32 w-auto" role="img" aria-label="Saludly">
          <path d={TRAZO_Y} pathLength={1} className="trazo-espera" fill="none" stroke="var(--marca)" strokeWidth={GROSOR_Y} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <h1 className="mt-8 text-balance text-[30px] font-normal leading-tight tracking-tight text-ink">¡Ya estás en la lista, {nombre}!</h1>
        <figure className="mt-6 rounded-[22px] bg-ficha px-5 py-4 text-left">
          <figcaption className="text-base text-ink-muted">Tu primer consejo · {objetivo}</figcaption>
          <blockquote className="mt-1 text-pretty text-[17px] leading-relaxed text-ink">{consejo}</blockquote>
        </figure>
        <p className="mx-auto mt-6 max-w-[22rem] text-pretty text-[17px] leading-relaxed text-ink-muted">
          Tu primera receta ya está lista. Escríbenos por WhatsApp y te llega con el resto de tu semana.
        </p>
        <a
          href={`https://wa.me/${whatsapp}?text=${encodeURIComponent(mensaje)}`}
          target="_blank"
          rel="noreferrer"
          className="mt-7 flex h-14 w-full items-center justify-center gap-2.5 rounded-full bg-whatsapp px-4 text-lg text-white"
        >
          <MessageCircle className="h-5 w-5" />
          Recibir mi primera receta
        </a>
        <button type="button" onClick={() => void invitar()} className="mt-3 flex min-h-14 w-full items-center justify-center gap-2.5 rounded-full bg-ficha px-5 py-3 text-base text-ink">
          <Share2 className="h-5 w-5 shrink-0" />
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
      <span className="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-ficha text-ink">{icono}</span>
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
  const [indicativo, setIndicativo] = useState("57");
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
  const uid = s.sesion?.user.id;
  const borradorLeido = useRef(false);

  // Recupera el borrador de esta cuenta (si cerró la app a mitad de camino) y después lo guarda en cada cambio.
  useEffect(() => {
    if (DEMO || !uid || borradorLeido.current) return;
    borradorLeido.current = true;
    try {
      const b = JSON.parse(localStorage.getItem(claveBorrador(uid)) ?? "null");
      if (!b) return;
      setPaso(b.paso ?? 1);
      if (b.nombre) setNombre(b.nombre);
      setIndicativo(b.indicativo ?? "57");
      setCelular(b.celular ?? "");
      setSexo(b.sexo ?? "");
      setDia(b.dia ?? "");
      setMes(b.mes ?? "");
      setAnio(b.anio ?? "");
      setLocalidad(b.localidad ?? "");
      setMetas(b.metas ?? []);
      setOtro(b.otro ?? "");
      setAlergias(b.alergias ?? []);
      setSinAlergias(!!b.sinAlergias);
    } catch {
      /* sin almacenamiento o borrador dañado: empieza de cero */
    }
  }, [uid]);
  useEffect(() => {
    if (DEMO || !uid || !borradorLeido.current) return;
    try {
      localStorage.setItem(claveBorrador(uid), JSON.stringify({ paso, nombre, indicativo, celular, sexo, dia, mes, anio, localidad, metas, otro, alergias, sinAlergias }));
    } catch {
      /* sin almacenamiento */
    }
  }, [uid, paso, nombre, indicativo, celular, sexo, dia, mes, anio, localidad, metas, otro, alergias, sinAlergias]);

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

  if (DEMO && demoListo) return <Listo datos={{ nombre, codigo: "a1b2c3", objetivos: metas }} />;
  if (!DEMO) {
    if (s.cargando) return <div className="min-h-screen bg-white" />;
    if (!s.sesion) return vuelveDeGoogle() ? <div className="min-h-screen bg-white" /> : <Portada />;
    if (s.preregistro) return <Listo datos={s.preregistro} />;
  }
  if (DEMO && params.get("demo") === "portada") return <Portada />;

  const nacimiento = fechaDe(dia, mes, anio);
  const edad = edadDe(nacimiento);
  const nombreValido = nombre.trim().length >= 3;
  const datosValidos = nombreValido && celularValido(indicativo, celular);
  const fechaValida = !!nacimiento && edad >= 0 && edad <= 110;
  const menor = fechaValida && edad < 18;
  const metasValidas = metas.length > 0 && (!metas.includes(OTRO) || otro.trim().length >= 3);
  const alergiasValidas = sinAlergias || alergias.length > 0;

  // Lo que dice encima del botón gris mientras no deja seguir
  const motivoDatos = !nombreValido
    ? "Escribe tu nombre para seguir."
    : indicativo === "57"
      ? "Escribe tu celular de WhatsApp: 10 números que empiezan por 3."
      : "Escribe el indicativo de tu país y tu número de WhatsApp.";
  const motivoFecha =
    dia && mes && anio.length === 4 && !nacimiento
      ? "Revisa la fecha: ese día no existe."
      : nacimiento && !fechaValida
        ? "Revisa el año de tu cumpleaños."
        : "Escribe el día, el mes y el año en que naciste.";
  const motivoMetas = metas.length === 0 ? "Elige al menos un objetivo para seguir." : "Escribe cuál es tu otro objetivo.";

  const inscribir = async () => {
    if (DEMO) return setDemoListo(true);
    setOcupado(true);
    setError(null);
    const { fuente, referido_por } = leerOrigen();
    const { error } = await supabase.from("preregistros").insert({
      nombre: nombre.trim(),
      correo: s.sesion!.user.email ?? null,
      celular_whatsapp: `${indicativo}${celular}`,
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
    if (error) return setError("No pudimos guardar tu inscripción. Revisa tu conexión e intenta de nuevo: lo que escribiste sigue aquí.");
    try {
      localStorage.removeItem(claveBorrador(s.sesion!.user.id));
    } catch {
      /* ignorar */
    }
    await s.recargar();
  };

  if (paso === 1)
    return (
      <PantallaPre paso={1} titulo="Cuéntanos quién eres" boton="Siguiente" puedeSeguir={datosValidos} onSeguir={() => setPaso(2)} motivo={motivoDatos}>
        <div className="grid gap-3">
          <Ficha etiqueta="Nombre">
            <input autoComplete="name" value={nombre} onChange={(e) => setNombre(e.target.value)} className={claseFicha} />
          </Ficha>
          <Ficha etiqueta="Celular con WhatsApp">
            <span className="text-ink-muted">+</span>
            <input
              id="indicativo"
              inputMode="numeric"
              autoComplete="tel-country-code"
              aria-label="Indicativo del país"
              value={indicativo}
              onChange={(e) => setIndicativo(e.target.value.replace(/\D/g, "").replace(/^0+/, "").slice(0, 4))}
              className={claseFicha.replace("w-full", "flex-none")}
              style={{ width: `${Math.max(2, indicativo.length) + 0.6}ch` }}
            />
            <span className="h-6 w-px shrink-0 bg-rule" />
            <input
              id="celular"
              inputMode="tel"
              autoComplete="tel-national"
              value={celular}
              onChange={(e) => setCelular(e.target.value.replace(/\D/g, "").slice(0, indicativo === "57" ? 10 : 13))}
              className={claseFicha}
              placeholder={indicativo === "57" ? "300 123 4567" : "Número sin el indicativo"}
            />
          </Ficha>
          {indicativo !== "57" && <p className="-mt-1 px-2 text-base text-ink-muted">¿Vives fuera de Colombia? Escribe el indicativo de tu país (por ejemplo, 1 para Estados Unidos o 34 para España) y tu número sin el cero inicial.</p>}
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
      <PantallaPre paso={2} titulo="¿Cuándo es tu cumpleaños?" boton="Siguiente" puedeSeguir={fechaValida} onSeguir={() => setPaso(3)} onAtras={() => setPaso(1)} motivo={motivoFecha}>
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
      </PantallaPre>
    );

  if (paso === 3)
    return (
      <PantallaPre paso={3} titulo="¿Dónde vives?" boton="Siguiente" puedeSeguir={localidad !== ""} onSeguir={() => setPaso(4)} onAtras={() => setPaso(2)} motivo="Elige dónde vives para seguir.">
        <label className="flex items-center gap-3 rounded-[22px] bg-ficha px-5 py-4 focus-within:ring-2 focus-within:ring-marca/50">
          <Search className="h-5 w-5 shrink-0 text-ink-muted" />
          <input value={buscar} onChange={(e) => setBuscar(e.target.value)} className={claseFicha} placeholder="Buscar localidad" aria-label="Buscar localidad" />
        </label>
        <ul className="mt-4" role="radiogroup" aria-label="Localidad">
          {lista.map((l, i) => {
            const activa = l === localidad;
            return (
              <li key={l} className={activa && i === 0 && lista.length > 1 ? "border-b border-rule" : ""}>
                <label className="flex w-full cursor-pointer items-center gap-4 py-4 text-left">
                  <input type="radio" name="localidad" value={l} checked={activa} onChange={() => setLocalidad(l)} className="peer sr-only" />
                  <span className="flex-1 text-[17px] text-ink">{l}</span>
                  <span
                    className={`grid h-6 w-6 shrink-0 place-items-center rounded-full border-2 peer-focus-visible:ring-2 peer-focus-visible:ring-marca/50 ${activa ? "border-ink" : "border-ink/25"}`}
                  >
                    {activa && <span className="h-3 w-3 rounded-full bg-ink" />}
                  </span>
                </label>
              </li>
            );
          })}
          {lista.length === 0 && <li className="py-4 text-base text-ink-muted">No encontramos esa localidad.</li>}
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
        motivo={motivoMetas}
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
        motivo="Elige tus alergias o marca «No tengo alergias»."
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
      texto={
        menor
          ? "Como tienes menos de 18 años, al marcar la casilla confirmas que tu mamá, papá o acudiente está de acuerdo y aceptas recibir por WhatsApp y correo tu semana de recetas y novedades. Te das de baja escribiendo «BAJA»."
          : "Al marcar la casilla confirmas que tienes 18 años o más y aceptas recibir por WhatsApp y correo tu semana de recetas y novedades. Te das de baja escribiendo «BAJA»."
      }
      boton="Aceptar y continuar"
      puedeSeguir={acepta}
      ocupado={ocupado}
      onSeguir={() => void inscribir()}
      onAtras={() => setPaso(5)}
      motivo="Marca la casilla «Acepto» para terminar."
      error={error}
      encimaBoton={
        <label className="flex cursor-pointer items-center gap-3 rounded-[20px] bg-ficha px-6 py-3.5 text-[17px] text-ink">
          <input type="checkbox" checked={acepta} onChange={(e) => setAcepta(e.target.checked)} className="peer sr-only" />
          {acepta ? "Aceptado" : "Acepto"}
          <span
            className={`grid h-6 w-6 place-items-center rounded-md border-2 peer-focus-visible:ring-2 peer-focus-visible:ring-marca/50 ${acepta ? "border-ink bg-ink text-white" : "border-ink/30"}`}
          >
            {acepta && <Check className="h-4 w-4" strokeWidth={3} />}
          </span>
        </label>
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
