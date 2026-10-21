/**
 * Sesión del paciente: cuenta (Supabase Auth con Google o correo), sus datos, su autorización, su cuestionario,
 * la visita de la enfermera y su informe aprobado. También dice si quien entra es del equipo (médico o administración).
 * Tablas y reglas de acceso: supabase/migrations/20261021051858_pacientes_pwa.sql y 20261022000000_visitas_informes_equipo.sql.
 * Como el equipo puede leer los datos de todos, cada consulta de la sesión filtra por el propio usuario.
 */
import { createClient, type Session } from "@supabase/supabase-js";
import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from "react";
import type { Informe } from "./informe";

export const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY);

export const VERSION_AUTORIZACION = "AUT-2026-10-v1";

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
  esEquipo: boolean;
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

  const cargarDatos = useCallback(async (s: Session | null) => {
    if (!s) {
      setPaciente(null);
      setAutorizado(false);
      setCuestionario(null);
      setVisita(null);
      setInforme(null);
      setEsEquipo(false);
      return;
    }
    const yo = s.user.id;
    const [p, a, c, v, i, e] = await Promise.all([
      supabase.from("pacientes").select("*").eq("id", yo).maybeSingle(),
      supabase.from("autorizaciones").select("id").eq("paciente_id", yo).eq("version", VERSION_AUTORIZACION).limit(1),
      supabase.from("cuestionarios").select("*").eq("paciente_id", yo).maybeSingle(),
      supabase.from("visitas").select("*").eq("paciente_id", yo).maybeSingle(),
      supabase.from("informes").select("informe").eq("paciente_id", yo).eq("estado", "aprobado").order("creado", { ascending: false }).limit(1),
      supabase.rpc("es_equipo"),
    ]);
    setPaciente((p.data as Paciente | null) ?? null);
    setAutorizado((a.data?.length ?? 0) > 0);
    setCuestionario((c.data as Cuestionario | null) ?? null);
    setVisita((v.data as Visita | null) ?? null);
    setInforme(((i.data?.[0] as { informe: Informe } | undefined)?.informe) ?? null);
    setEsEquipo(e.data === true);
  }, []);

  useEffect(() => {
    supabase.auth.getSession().then(async ({ data }) => {
      setSesion(data.session);
      await cargarDatos(data.session);
      setCargando(false);
    });
    const { data } = supabase.auth.onAuthStateChange((_evento, s) => {
      setSesion(s);
      void cargarDatos(s);
    });
    return () => data.subscription.unsubscribe();
  }, [cargarDatos]);

  const recargar = useCallback(() => cargarDatos(sesion), [cargarDatos, sesion]);
  const salir = useCallback(async () => {
    await supabase.auth.signOut();
  }, []);

  return <Ctx.Provider value={{ cargando, sesion, paciente, autorizado, cuestionario, visita, informe, esEquipo, recargar, salir }}>{children}</Ctx.Provider>;
}

export function useSesion() {
  const v = useContext(Ctx);
  if (!v) throw new Error("useSesion fuera de SesionProvider");
  return v;
}

/** A qué pantalla debe ir el paciente según lo que ya completó. */
export function siguientePaso(v: Valor): "/entrar" | "/registro" | "/cuestionario" | "/listo" | "/recorrido" | "/medico" {
  if (!v.sesion) return "/entrar";
  if (v.esEquipo && !v.paciente) return "/medico";
  if (!v.paciente || !v.autorizado) return "/registro";
  if (!v.cuestionario?.completo) return "/cuestionario";
  if (v.informe) return "/recorrido";
  return "/listo";
}
