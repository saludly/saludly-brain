/**
 * Sesión del paciente: cuenta (Supabase Auth con Google o correo), sus datos, su autorización, su cuestionario,
 * la visita de la enfermera y su informe aprobado. También dice si quien entra es del equipo (médico o administración).
 * Tablas y reglas de acceso: supabase/migrations/20261021051858_pacientes_pwa.sql y 20261022000000_visitas_informes_equipo.sql.
 * Como el equipo puede leer los datos de todos, cada consulta de la sesión filtra por el propio usuario.
 */
import { createClient, type Session } from "@supabase/supabase-js";
import { createContext, useCallback, useContext, useEffect, useRef, useState, type ReactNode } from "react";
import type { Informe } from "./informe";
import { esLineaPeso } from "./peso";

export const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY);

export const VERSION_AUTORIZACION = "AUT-2026-10-v1";
/** Autorización del pre-registro (preventa): datos básicos, metas y, si los da, alergias y dieta para las recetas. */
export const VERSION_AUTORIZACION_PRE = "AUT-PRE-2026-10-v1";

/** CC: cédula de ciudadanía · CE: cédula de extranjería · PPT: Permiso por Protección Temporal · PA: pasaporte. */
export type TipoDocumento = "CC" | "CE" | "PPT" | "PA";

export interface Paciente {
  id: string;
  nombre: string;
  tipo_documento: TipoDocumento;
  /** Número del documento, sea cual sea el tipo. */
  cedula: string;
  fecha_nacimiento: string | null;
  celular_whatsapp: string;
  direccion: string;
  edad: number;
  sexo: "hombre" | "mujer";
}

export interface Cuestionario {
  objetivos: string[];
  peso_kg: number | null;
  talla_m: number | null;
  nivel_actividad: string | null;
  toma_biotina: boolean | null;
  alergias: string[];
  alergias_otras: string | null;
  dieta: string | null;
  medicamentos: string[];
  medicamentos_otros: string | null;
  fuma: string | null;
  alcohol: string | null;
  antecedentes: string[];
  embarazo: string | null;
  completo: boolean;
  /** Cuándo salió el WhatsApp para agendar la visita (lo marca la función avisar-listo). */
  aviso_listo?: string | null;
}

export interface Pago {
  codigo: string;
  estado: "pendiente" | "comprobante" | "confirmado" | "rechazado";
  nota: string | null;
}

/** Pre-registro de la preventa (tabla preregistros). estado "cliente": Carlos lo pasó al flujo completo con pago. */
export interface Preregistro {
  nombre: string;
  celular_whatsapp: string;
  fecha_nacimiento: string;
  sexo: "hombre" | "mujer" | null;
  codigo: string;
  objetivos: string[];
  estado: "registrado" | "cliente" | "baja";
  quiere_prueba: boolean;
}

export interface Visita {
  presion_sistolica: number | null;
  presion_diastolica: number | null;
  cintura_cm: number | null;
  cadera_cm: number | null;
  peso_kg: number | null;
  talla_m: number | null;
  enfermera: string | null;
  tomada: string;
}

export const CUESTIONARIO_VACIO: Cuestionario = {
  objetivos: [],
  peso_kg: null,
  talla_m: null,
  nivel_actividad: null,
  toma_biotina: null,
  alergias: [],
  alergias_otras: null,
  dieta: null,
  medicamentos: [],
  medicamentos_otros: null,
  fuma: null,
  alcohol: null,
  antecedentes: [],
  embarazo: null,
  completo: false,
};

interface Valor {
  cargando: boolean;
  sesion: Session | null;
  paciente: Paciente | null;
  autorizado: boolean;
  cuestionario: Cuestionario | null;
  visita: Visita | null;
  informe: Informe | null;
  pago: Pago | null;
  preregistro: Preregistro | null;
  /** configuracion.preventa = "si": quien no es paciente ni cliente hace el pre-registro en vez del registro completo. */
  preventa: boolean;
  /** El paciente vio la pantalla de pago y eligió seguir con las preguntas mientras confirmamos. */
  pagoVisto: boolean;
  marcarPagoVisto: () => void;
  esEquipo: boolean;
  /** Línea GLP-1: la paciente ya registró su tratamiento para bajar de peso. */
  tienePeso: boolean;
  /** La cuenta es de una doctora aliada (tabla doctoras). */
  esDoctora: boolean;
  recargar: () => Promise<void>;
  salir: () => Promise<void>;
}

const Ctx = createContext<Valor | null>(null);

export function SesionProvider({ children }: { children: ReactNode }) {
  const [cargando, setCargando] = useState(true);
  const [sesion, setSesion] = useState<Session | null>(null);
  const [paciente, setPaciente] = useState<Paciente | null>(null);
  const [autorizado, setAutorizado] = useState(false);
  const [cuestionario, setCuestionario] = useState<Cuestionario | null>(null);
  const [visita, setVisita] = useState<Visita | null>(null);
  const [informe, setInforme] = useState<Informe | null>(null);
  const [esEquipo, setEsEquipo] = useState(false);
  const [pago, setPago] = useState<Pago | null>(null);
  const [pagoVisto, setPagoVisto] = useState(false);
  const [preregistro, setPreregistro] = useState<Preregistro | null>(null);
  const [preventa, setPreventa] = useState(false);
  const [tienePeso, setTienePeso] = useState(false);
  const [esDoctora, setEsDoctora] = useState(false);

  const cargarDatos = useCallback(async (s: Session | null) => {
    if (!s) {
      setPaciente(null);
      setAutorizado(false);
      setCuestionario(null);
      setVisita(null);
      setInforme(null);
      setEsEquipo(false);
      setPago(null);
      setPreregistro(null);
      setTienePeso(false);
      setEsDoctora(false);
      return;
    }
    const yo = s.user.id;
    try {
      setPagoVisto(localStorage.getItem(`saludly-pago-visto-${yo}`) === "1");
    } catch {
      /* sin almacenamiento: se vuelve a mostrar la pantalla de pago */
    }
    const [p, a, c, v, i, e, g, r, k, t, d] = await Promise.all([
      supabase.from("pacientes").select("*").eq("id", yo).maybeSingle(),
      supabase.from("autorizaciones").select("id").eq("paciente_id", yo).eq("version", VERSION_AUTORIZACION).limit(1),
      supabase.from("cuestionarios").select("*").eq("paciente_id", yo).maybeSingle(),
      supabase.from("visitas").select("*").eq("paciente_id", yo).maybeSingle(),
      supabase.from("informes").select("informe").eq("paciente_id", yo).eq("estado", "aprobado").order("creado", { ascending: false }).limit(1),
      supabase.rpc("es_equipo"),
      supabase.from("pagos").select("codigo, estado, nota").eq("paciente_id", yo).maybeSingle(),
      supabase.from("preregistros").select("nombre, celular_whatsapp, fecha_nacimiento, sexo, codigo, objetivos, estado, quiere_prueba").eq("id", yo).maybeSingle(),
      supabase.from("configuracion").select("valor").eq("clave", "preventa").maybeSingle(),
      supabase.from("tratamientos_peso").select("paciente_id").eq("paciente_id", yo).maybeSingle(),
      supabase.rpc("es_doctora"),
    ]);
    setPaciente((p.data as Paciente | null) ?? null);
    setAutorizado((a.data?.length ?? 0) > 0);
    setCuestionario((c.data as Cuestionario | null) ?? null);
    setVisita((v.data as Visita | null) ?? null);
    setInforme(((i.data?.[0] as { informe: Informe } | undefined)?.informe) ?? null);
    setEsEquipo(e.data === true);
    setPago((g.data as Pago | null) ?? null);
    setPreregistro((r.data as Preregistro | null) ?? null);
    setPreventa(k.data?.valor === "si");
    setTienePeso(!!t.data);
    setEsDoctora(d.data === true);
  }, []);

  // Datos de la cuenta que ya se cargaron (o se están cargando). La sesión solo se publica cuando sus datos están listos:
  // si no, al volver de Google se alcanzaba a ver /registro medio segundo antes de saber que es preventa.
  const cargados = useRef<{ id: string | null; listo: Promise<void> } | null>(null);

  useEffect(() => {
    const aplicar = async (s: Session | null) => {
      const id = s?.user.id ?? null;
      if (cargados.current?.id !== id) {
        setCargando(true);
        cargados.current = { id, listo: cargarDatos(s) };
      }
      const actual = cargados.current;
      await actual.listo;
      if (cargados.current !== actual) return; // cambió de cuenta mientras cargaba
      setSesion(s);
      setCargando(false);
    };
    supabase.auth.getSession().then(({ data }) => void aplicar(data.session));
    const { data } = supabase.auth.onAuthStateChange((_evento, s) => void aplicar(s));
    return () => data.subscription.unsubscribe();
  }, [cargarDatos]);

  const recargar = useCallback(() => cargarDatos(sesion), [cargarDatos, sesion]);
  const marcarPagoVisto = useCallback(() => {
    setPagoVisto(true);
    try {
      if (sesion) localStorage.setItem(`saludly-pago-visto-${sesion.user.id}`, "1");
    } catch {
      /* ignorar */
    }
  }, [sesion]);
  const salir = useCallback(async () => {
    await supabase.auth.signOut();
  }, []);

  return <Ctx.Provider value={{ cargando, sesion, paciente, autorizado, cuestionario, visita, informe, pago, preregistro, preventa, pagoVisto, marcarPagoVisto, esEquipo, tienePeso, esDoctora, recargar, salir }}>{children}</Ctx.Provider>;
}

export function useSesion() {
  const v = useContext(Ctx);
  if (!v) throw new Error("useSesion fuera de SesionProvider");
  return v;
}

/** A qué pantalla debe ir el paciente según lo que ya completó. */
export function siguientePaso(v: Valor): "/entrar" | "/preregistro" | "/registro" | "/pago" | "/cuestionario" | "/listo" | "/recorrido" | "/medico" | "/peso" | "/peso/empezar" | "/doctora" {
  if (!v.sesion) return "/entrar";
  // Doctora aliada (línea GLP-1): su panel.
  if (v.esDoctora && !v.esEquipo) return "/doctora";
  // Línea GLP-1: llegó por el enlace de su doctora. Sin pago ni cuestionario largo: registro y su tratamiento.
  if (!v.esEquipo && (v.tienePeso || esLineaPeso())) {
    if (!v.paciente || !v.autorizado) return "/registro";
    return v.tienePeso ? "/peso" : "/peso/empezar";
  }
  // El equipo entra siempre a su panel (aunque haya probado el flujo como paciente).
  if (v.esEquipo) return "/medico";
  // Preventa: el que no es paciente hace el pre-registro, salvo que Carlos ya lo haya pasado a cliente.
  if (!v.paciente && v.preventa && v.preregistro?.estado !== "cliente") return "/preregistro";
  if (!v.paciente || !v.autorizado) return "/registro";
  // El pago se muestra después del registro; el cuestionario se puede responder mientras Carlos lo confirma.
  if (!v.pago || (v.pago.estado === "pendiente" && !v.pagoVisto) || v.pago.estado === "rechazado") return "/pago";
  if (!v.cuestionario?.completo) return "/cuestionario";
  if (v.informe) return "/recorrido";
  return "/listo";
}
