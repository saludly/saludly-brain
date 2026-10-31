/**
 * Línea GLP-1 (Fase 6B): datos de la paciente en tratamiento para bajar de peso y los cálculos que ve ella y su doctora.
 * Tablas: supabase/migrations/20261031000000_glp1_peso.sql. Criterios: docs/07_linea_glp1/version_funcional.md.
 * El nivel y la silueta son motivacionales, no un puntaje clínico. El nivel nunca baja.
 */
import { supabase } from "./sesion";

export const VERSION_AUTORIZACION_PESO = "AUT-GLP1-2026-11-v1";

export interface Tratamiento {
  paciente_id: string;
  doctora_codigo: string | null;
  fecha_inicio: string;
  peso_inicio: number;
  peso_meta: number;
  cintura_inicio: number | null;
  cintura_meta: number | null;
  talla_m: number;
  medicamento: string | null;
  dosis: string | null;
  dia_aplicacion: string | null;
  confirmado_por: string | null;
  confirmado: string | null;
}

export interface Registro {
  id: number;
  paciente_id: string;
  fecha: string;
  peso: number | null;
  cintura: number | null;
  sintomas: string[];
  aplicada: boolean | null;
  metas_cumplidas: number | null;
  metas_total: number | null;
  pregunta: string | null;
}

export interface ItemSemana {
  id: string;
  tipo: string;
  titulo: string;
  texto: string;
  por_que: string;
  fuente: "doctora" | "examenes" | "semana" | "objetivos";
}

export interface Semana {
  id: number;
  paciente_id: string;
  semana: string;
  items: ItemSemana[];
  mensaje_doctora: string | null;
  estado: "borrador" | "publicada";
  publicada: string | null;
}

/** Línea de la app: la paciente llegó por el enlace de su doctora (/peso o ?dra=). Se recuerda en este navegador. */
const CLAVE_LINEA = "saludly-linea";
const CLAVE_DRA = "saludly-dra";
export function marcarLineaPeso(codigo?: string | null) {
  try {
    localStorage.setItem(CLAVE_LINEA, "peso");
    if (codigo) localStorage.setItem(CLAVE_DRA, codigo.toUpperCase());
  } catch {
    /* sin almacenamiento: la paciente vuelve a entrar por el enlace */
  }
}
export function esLineaPeso() {
  try {
    return localStorage.getItem(CLAVE_LINEA) === "peso";
  } catch {
    return false;
  }
}
export function codigoDraGuardado() {
  try {
    return localStorage.getItem(CLAVE_DRA) ?? "";
  } catch {
    return "";
  }
}

// ---------- Síntomas (lista base: la doctora la aprueba en el onboarding; supuesto provisional) ----------
export const SINTOMAS: { id: string; texto: string; alarma: boolean }[] = [
  { id: "bien", texto: "Bien", alarma: false },
  { id: "nauseas", texto: "Náuseas", alarma: false },
  { id: "estrenimiento", texto: "Estreñimiento", alarma: false },
  { id: "diarrea", texto: "Diarrea", alarma: false },
  { id: "acidez", texto: "Acidez", alarma: false },
  { id: "cansancio", texto: "Cansancio", alarma: false },
  { id: "poco_apetito", texto: "Poco apetito", alarma: false },
  { id: "mareo", texto: "Mareo", alarma: false },
  { id: "dolor_abdominal_fuerte", texto: "Dolor abdominal fuerte", alarma: true },
  { id: "vomito_persistente", texto: "Vómito que no para", alarma: true },
  { id: "no_retiene_liquidos", texto: "No retengo líquidos", alarma: true },
];
export const textoSintoma = (id: string) => SINTOMAS.find((s) => s.id === id)?.texto ?? id;
export const esAlarma = (id: string) => SINTOMAS.some((s) => s.id === id && s.alarma);

export const DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"] as const;
export const DIA_TEXTO: Record<string, string> = { lunes: "Lunes", martes: "Martes", miercoles: "Miércoles", jueves: "Jueves", viernes: "Viernes", sabado: "Sábado", domingo: "Domingo" };

// ---------- Formato ----------
export const fmt = (n: number, d = 1) => n.toLocaleString("es-CO", { minimumFractionDigits: d, maximumFractionDigits: d });
export function hoyISO() {
  const h = new Date();
  return `${h.getFullYear()}-${String(h.getMonth() + 1).padStart(2, "0")}-${String(h.getDate()).padStart(2, "0")}`;
}
export function fechaCorta(iso: string) {
  return new Date(iso + "T12:00:00").toLocaleDateString("es-CO", { day: "numeric", month: "short" });
}

// ---------- Cálculos ----------
export const imc = (peso: number, talla: number) => peso / (talla * talla);
/** Masa grasa relativa (Woolcott y Bergman 2018): solo usa talla y cintura. */
export const rfm = (cintura: number, talla: number, mujer = true) => (mujer ? 76 : 64) - 20 * ((talla * 100) / cintura);

/** Serie semanal de peso desde el inicio del tratamiento: semana 0 = peso al inicio; después, el último registro de cada semana. */
export function serieSemanal(t: Tratamiento, registros: Registro[]) {
  const inicio = new Date(t.fecha_inicio + "T12:00:00").getTime();
  const porSemana = new Map<number, number>();
  for (const r of [...registros].sort((a, b) => a.fecha.localeCompare(b.fecha))) {
    if (r.peso == null) continue;
    const s = Math.max(1, Math.ceil((new Date(r.fecha + "T12:00:00").getTime() - inicio) / (7 * 864e5)));
    porSemana.set(s, Number(r.peso));
  }
  const semanas = [...porSemana.keys()].sort((a, b) => a - b);
  const puntos: { semana: number; peso: number }[] = [{ semana: 0, peso: Number(t.peso_inicio) }];
  for (const s of semanas) puntos.push({ semana: s, peso: porSemana.get(s)! });
  return puntos;
}

export function semanaDeTratamiento(t: Tratamiento) {
  return Math.max(1, Math.ceil((Date.now() - new Date(t.fecha_inicio + "T12:00:00").getTime()) / (7 * 864e5)));
}

/** Último peso y cintura registrados (si no hay, los del inicio). */
export function actual(t: Tratamiento, registros: Registro[]) {
  const orden = [...registros].sort((a, b) => b.fecha.localeCompare(a.fecha));
  const peso = Number(orden.find((r) => r.peso != null)?.peso ?? t.peso_inicio);
  const cintura = orden.find((r) => r.cintura != null)?.cintura ?? t.cintura_inicio;
  return { peso, cintura: cintura == null ? null : Number(cintura) };
}

export const fraccion = (t: Tratamiento, peso: number) => Math.max(0, Math.min(1, (t.peso_inicio - peso) / (t.peso_inicio - t.peso_meta)));
export function fraccionCintura(t: Tratamiento, c: number | null) {
  if (c == null || t.cintura_inicio == null || t.cintura_meta == null || t.cintura_inicio <= t.cintura_meta) return null;
  return Math.max(0, Math.min(1, (t.cintura_inicio - c) / (t.cintura_inicio - t.cintura_meta)));
}
/** Avance para la silueta: promedio de peso y cintura (solo peso si no hay cintura). */
export function avance(t: Tratamiento, peso: number, cintura: number | null) {
  const fc = fraccionCintura(t, cintura);
  return fc == null ? fraccion(t, peso) : (fraccion(t, peso) + fc) / 2;
}

// ---------- Logros, retos y nivel ----------
export interface Logro { id: string; m: string; t: string; s: string; pts: number; ok: boolean }

export function logros(t: Tratamiento, registros: Registro[], examenAprobado: boolean): Logro[] {
  const { peso, cintura } = actual(t, registros);
  const bajo = t.peso_inicio - peso;
  const semanasReg = new Set(serieSemanal(t, registros).filter((p) => p.semana > 0).map((p) => p.semana)).size;
  const semanasMetas = registros.filter((r) => r.metas_total && r.metas_cumplidas === r.metas_total).length;
  const bajoCint = t.cintura_inicio != null && cintura != null ? t.cintura_inicio - cintura : 0;
  const total = t.peso_inicio - t.peso_meta;
  return [
    { id: "paso", m: "1", t: "Primer paso", s: "Empezaste el tratamiento", pts: 0, ok: true },
    { id: "kilo", m: "1 kg", t: "Primer kilo", s: "1 kg menos", pts: 0, ok: bajo >= 1 },
    { id: "p5", m: "5 %", t: "5 % de tu peso", s: `${fmt(t.peso_inicio * 0.05)} kg menos`, pts: 0, ok: bajo >= t.peso_inicio * 0.05 },
    { id: "k8", m: "8 kg", t: "8 kilos menos", s: "", pts: 0, ok: bajo >= 8 - 1e-9 },
    { id: "mitad", m: "½", t: "Mitad del camino", s: "", pts: 0, ok: bajo >= total / 2 },
    { id: "k12", m: "12 kg", t: "12 kilos menos", s: "", pts: 0, ok: bajo >= 12 - 1e-9 },
    { id: "p10", m: "10 %", t: "10 % de tu peso", s: "", pts: 0, ok: bajo >= t.peso_inicio * 0.1 },
    { id: "c5", m: "−5", t: "5 cm de cintura", s: "", pts: 0, ok: bajoCint >= 5 },
    { id: "c10", m: "−10", t: "10 cm de cintura", s: "", pts: 0, ok: bajoCint >= 10 },
    { id: "reg4", m: "4 sem", t: "4 semanas registrando", s: "", pts: 4, ok: semanasReg >= 4 },
    { id: "semana", m: "7/7", t: "Semana completa", s: "Cumpliste tus metas", pts: 3, ok: semanasMetas >= 1 },
    { id: "examen", m: "Lab", t: "Exámenes al día", s: "Tu doctora los revisó", pts: 3, ok: examenAprobado },
    { id: "meta", m: "Meta", t: "Llegaste a tu meta", s: "", pts: 0, ok: peso <= t.peso_meta },
  ];
}

/** Nivel = 30 + 42 × lo logrado hacia la meta + puntos de hábitos, hasta 100 (docs/07_linea_glp1/demo_app_y_dashboard.md). */
export function nivel(t: Tratamiento, registros: Registro[], examenAprobado: boolean) {
  const { peso } = actual(t, registros);
  const habitos = logros(t, registros, examenAprobado).filter((l) => l.ok).reduce((a, l) => a + l.pts, 0);
  return Math.min(100, Math.round(30 + 42 * fraccion(t, peso) + habitos));
}

/** El nivel nunca baja: se guarda el mayor visto en este navegador (el registro real sigue en la base). */
export function nivelSinBajar(pacienteId: string, valor: number) {
  const clave = `saludly-nivel-${pacienteId}`;
  try {
    const previo = Number(localStorage.getItem(clave) ?? 0);
    const v = Math.max(previo, valor);
    localStorage.setItem(clave, String(v));
    return v;
  } catch {
    return valor;
  }
}

/** Retos de kilos: 8, 12 y la meta, contados desde el inicio del tratamiento. */
export function retoActual(t: Tratamiento, peso: number) {
  const bajo = Math.max(0, t.peso_inicio - peso);
  const total = t.peso_inicio - t.peso_meta;
  const retos = [
    { id: "k8", t: "8 kilos menos", obj: 8 },
    { id: "k12", t: "12 kilos menos", obj: 12 },
    { id: "meta", t: "Llegar a tu meta", obj: total },
  ].filter((r) => r.obj <= total + 1e-9 || r.id === "meta");
  const r = retos.find((x) => bajo < x.obj - 1e-9);
  return r ? { ...r, bajo, falta: r.obj - bajo } : null;
}

// ---------- Alertas para la doctora (supuestos provisionales; los límites los define ella) ----------
export type Severidad = "alta" | "media" | "info" | "baja" | "ok";
export interface Alerta { s: Severidad; corto: string; texto: string }

export function alertas(t: Tratamiento, registros: Registro[], limite = 1.5, meseta = 4, informeEnRevision = false): Alerta[] {
  const out: Alerta[] = [];
  const orden = [...registros].sort((a, b) => b.fecha.localeCompare(a.fecha));
  const recientes = orden.filter((r) => Date.now() - new Date(r.fecha + "T12:00:00").getTime() < 8 * 864e5);
  const alarma = [...new Set(recientes.flatMap((r) => r.sintomas.filter(esAlarma)))];
  if (alarma.length) out.push({ s: "alta", corto: alarma.map(textoSintoma).join(" y "), texto: `Reportó ${alarma.map(textoSintoma).join(" y ").toLowerCase()} el ${fechaCorta(orden.find((r) => r.sintomas.some(esAlarma))!.fecha)}. La app le indicó llamarla o ir a urgencias.` });
  const serie = serieSemanal(t, registros);
  const v = serie.slice(1).map((p, i) => ((serie[i].peso - p.peso) / serie[i].peso) * 100 / Math.max(1, p.semana - serie[i].semana));
  if (v.length >= 2 && v.slice(-2).every((x) => x > limite)) out.push({ s: "media", corto: `Bajó ${fmt(v[v.length - 1])} % por semana`, texto: `Bajó más de ${fmt(limite)} % por semana las últimas 2 semanas (su límite).` });
  const ultimo = orden[0];
  const dias = ultimo ? Math.floor((Date.now() - new Date(ultimo.fecha + "T12:00:00").getTime()) / 864e5) : null;
  if (dias != null && dias >= 14) out.push({ s: "media", corto: `Sin registrar hace ${dias} días`, texto: `No registra datos hace ${dias} días.` });
  if (serie.length > meseta) {
    const ult = serie.slice(-(meseta + 1));
    if (ult[ult.length - 1].semana - ult[0].semana >= meseta && Math.max(...ult.map((p) => p.peso)) - Math.min(...ult.map((p) => p.peso)) < 0.6)
      out.push({ s: "baja", corto: `Sin cambio en ${meseta} semanas`, texto: `Su peso no cambia hace ${meseta} semanas o más.` });
  }
  if (informeEnRevision) out.push({ s: "info", corto: "Examen para revisar", texto: "Subió un resultado de laboratorio: el análisis espera su revisión." });
  if (!t.confirmado) out.push({ s: "info", corto: "Confirmar datos del tratamiento", texto: "Los datos del tratamiento los escribió la paciente: confírmelos o corríjalos." });
  return out;
}
export const RANGO: Record<Severidad, number> = { alta: 0, media: 1, info: 2, baja: 3, ok: 4 };

// ---------- Lecturas ----------
export async function cargarPaciente(id: string) {
  const [t, r, s] = await Promise.all([
    supabase.from("tratamientos_peso").select("*").eq("paciente_id", id).maybeSingle(),
    supabase.from("registros_peso").select("*").eq("paciente_id", id).order("fecha", { ascending: true }),
    supabase.from("semanas_peso").select("*").eq("paciente_id", id).eq("estado", "publicada").order("semana", { ascending: false }).limit(1),
  ]);
  return {
    tratamiento: t.data ? normalizarT(t.data as Tratamiento) : null,
    registros: ((r.data as Registro[] | null) ?? []).map(normalizar),
    semana: ((s.data?.[0] as Semana | undefined) ?? null),
  };
}
export function normalizar(r: Registro): Registro {
  return { ...r, peso: r.peso == null ? null : Number(r.peso), cintura: r.cintura == null ? null : Number(r.cintura), sintomas: r.sintomas ?? [] };
}
export function normalizarT(t: Tratamiento): Tratamiento {
  const n = (x: number | null) => (x == null ? null : Number(x));
  return { ...t, peso_inicio: Number(t.peso_inicio), peso_meta: Number(t.peso_meta), talla_m: Number(t.talla_m), cintura_inicio: n(t.cintura_inicio), cintura_meta: n(t.cintura_meta) };
}
