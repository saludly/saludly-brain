/**
 * Sesión del paciente: cuenta (Supabase Auth con Google o correo), sus datos, su autorización y su cuestionario.
 * Las tablas y sus reglas de acceso están en supabase/migrations/20261021000000_pacientes_pwa.sql.
 */
import { createClient, type Session } from "@supabase/supabase-js";
import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from "react";

export const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY);

export const VERSION_AUTORIZACION = "AUT-2026-10-v1";

export interface Paciente {
  id: string;
  nombre: string;
  cedula: string;
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

  const cargarDatos = useCallback(async (s: Session | null) => {
    if (!s) {
      setPaciente(null);
      setAutorizado(false);
      setCuestionario(null);
      return;
    }
    const [p, a, c] = await Promise.all([
      supabase.from("pacientes").select("*").maybeSingle(),
      supabase.from("autorizaciones").select("id").eq("version", VERSION_AUTORIZACION).limit(1),
      supabase.from("cuestionarios").select("*").maybeSingle(),
    ]);
    setPaciente((p.data as Paciente | null) ?? null);
    setAutorizado((a.data?.length ?? 0) > 0);
    setCuestionario((c.data as Cuestionario | null) ?? null);
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

  return <Ctx.Provider value={{ cargando, sesion, paciente, autorizado, cuestionario, recargar, salir }}>{children}</Ctx.Provider>;
}

export function useSesion() {
  const v = useContext(Ctx);
  if (!v) throw new Error("useSesion fuera de SesionProvider");
  return v;
}

/** A qué pantalla debe ir el paciente según lo que ya completó. */
export function siguientePaso(v: Valor): "/entrar" | "/registro" | "/cuestionario" | "/listo" {
  if (!v.sesion) return "/entrar";
  if (!v.paciente || !v.autorizado) return "/registro";
  if (!v.cuestionario?.completo) return "/cuestionario";
  return "/listo";
}
