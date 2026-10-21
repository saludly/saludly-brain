/**
 * Datos del informe para la app del paciente.
 * Por ahora carga los informes de ejemplo de codigo/pipeline/ejemplos (datos sintéticos);
 * cuando exista la cuenta del paciente, el informe vendrá de Supabase con el mismo contrato.
 */
import type { Clase, Escalamiento, Informe, Resultado } from "./informe";

const EJEMPLOS = import.meta.glob<Informe>("../../../codigo/pipeline/ejemplos/INF-*.json", { eager: true, import: "default" });

export const CASOS: { id: string; nombre: string }[] = [
  { id: "LCD-2026-100123", nombre: "Hombre, 46 años" },
  { id: "LCD-2026-100124", nombre: "Mujer, 34 años" },
  { id: "LCD-2026-100125", nombre: "Hombre con valor crítico" },
  { id: "LCD-2026-100126", nombre: "Mujer con hallazgos digestivos" },
];

export function informeDeEjemplo(orden: string): Informe {
  const par = Object.entries(EJEMPLOS).find(([ruta]) => ruta.includes(orden)) ?? Object.entries(EJEMPLOS)[0];
  if (!par) throw new Error("No hay informes de ejemplo en codigo/pipeline/ejemplos");
  return par[1];
}

/** Estado visual de un resultado. Saludly no usa "óptimo" ni rangos sin fuente: se compara con el intervalo del laboratorio. */
export type Estado = "en_rango" | "fuera" | "pronto" | "sin_lectura";

export function estadoDe(clase: Clase): Estado {
  if (clase === "en_rango") return "en_rango";
  if (clase === "critico") return "pronto";
  if (clase === "bajo" || clase === "alto" || clase === "limitrofe" || clase === "alterado") return "fuera";
  return "sin_lectura";
}

export const ETIQUETA: Record<Estado, string> = {
  en_rango: "En rango",
  fuera: "Fuera de rango",
  pronto: "Atención pronta",
  sin_lectura: "Sin lectura",
};

export const PUNTO: Record<Estado, string> = {
  en_rango: "bg-optimal",
  fuera: "bg-attention",
  pronto: "bg-critical",
  sin_lectura: "bg-ink-faint",
};

export const TEXTO: Record<Estado, string> = {
  en_rango: "text-optimal",
  fuera: "text-attention",
  pronto: "text-critical",
  sin_lectura: "text-ink-faint",
};

export const SUAVE: Record<Estado, string> = {
  en_rango: "bg-optimal-soft text-optimal",
  fuera: "bg-attention-soft text-attention",
  pronto: "bg-critical-soft text-critical",
  sin_lectura: "bg-surface text-ink-faint",
};

/** Escalamiento del hallazgo → estado de color (0 y 1 son cosas para cuidar; 2 y 3 piden consulta). */
export function estadoDeEscalamiento(e: Escalamiento): Estado {
  return e >= 2 ? "pronto" : "fuera";
}

export const PLAZO: Record<Escalamiento, string> = {
  0: "Para cuidar con hábitos",
  1: "Para tu próximo control",
  2: "Consulta en 2 a 4 semanas",
  3: "El equipo médico te llamará hoy",
};

/** Límites numéricos del intervalo del laboratorio ("13,5 – 17,5", "< 5", "> 40"). Null si el texto no se puede leer. */
export function limites(intervalo: string | null): { bajo: number | null; alto: number | null } | null {
  if (!intervalo) return null;
  const num = (s: string) => Number.parseFloat(s.replace(/\./g, "").replace(",", "."));
  const t = intervalo.trim();
  let m = t.match(/^(-?[\d.,]+)\s*[–-]\s*(-?[\d.,]+)$/);
  if (m?.[1] && m[2]) return { bajo: num(m[1]), alto: num(m[2]) };
  m = t.match(/^(<|≤|<=|hasta)\s*([\d.,]+)$/i);
  if (m?.[2]) return { bajo: 0, alto: num(m[2]) };
  m = t.match(/^(>|≥|>=)\s*([\d.,]+)$/);
  if (m?.[2]) return { bajo: num(m[2]), alto: null };
  return null;
}

/** Posición del valor y ventana del intervalo en una barra de 0 a 100. */
export function barra(r: Resultado) {
  const l = limites(r.intervalo);
  const v = typeof r.valor === "number" ? r.valor : null;
  if (!l || v === null) return null;
  const bajo = l.bajo ?? 0;
  const alto = l.alto ?? (bajo * 2 || 1);
  const pad = (alto - bajo || 1) * 0.35;
  const lo = bajo - pad;
  const hi = alto + pad;
  const pct = (x: number) => ((x - lo) / (hi - lo)) * 100;
  return {
    posicion: Math.max(4, Math.min(96, pct(v))),
    inicio: pct(bajo),
    ancho: l.alto === null ? 100 - pct(bajo) : pct(alto) - pct(bajo),
  };
}

export function valorTexto(r: Resultado) {
  if (r.valor === null || r.valor === undefined) return "—";
  if (typeof r.valor === "number") return r.valor.toLocaleString("es-CO", { maximumFractionDigits: 2 });
  return String(r.valor);
}

/** Sistemas del cuerpo para la figura: cada uno agrupa secciones del laboratorio. */
export const SISTEMAS: { nombre: string; secciones: RegExp; top: string; left: string; lado: "izq" | "der" }[] = [
  { nombre: "Tiroides", secciones: /TIROIDES/, top: "19%", left: "50%", lado: "der" },
  { nombre: "Corazón", secciones: /LIPÍDICO|CARDIOVASCULAR/, top: "31%", left: "44%", lado: "izq" },
  { nombre: "Hígado", secciones: /HEPÁTICA/, top: "43%", left: "56%", lado: "der" },
  { nombre: "Metabolismo", secciones: /CARBOHIDRATOS/, top: "50%", left: "47%", lado: "izq" },
  { nombre: "Riñones", secciones: /RENAL|ELECTROLITOS/, top: "55%", left: "55%", lado: "der" },
  { nombre: "Sangre", secciones: /HEMATOLOGÍA|HIERRO|INMUNOLOGÍA|COAGULACIÓN/, top: "64%", left: "48%", lado: "izq" },
];

const ORDEN: Record<Estado, number> = { sin_lectura: 0, en_rango: 1, fuera: 2, pronto: 3 };

export function estadoDeSistema(resultados: Resultado[], secciones: RegExp): Estado | null {
  const de = resultados.filter((r) => r.seccion && secciones.test(r.seccion)).map((r) => estadoDe(r.clase));
  if (!de.length) return null;
  return de.reduce((peor, e) => (ORDEN[e] > ORDEN[peor] ? e : peor), "sin_lectura" as Estado);
}

/** Nombre corto de la sección del laboratorio ("HEMATOLOGÍA · HEMOGRAMA IV" → "Hematología"). */
export function nombreSeccion(s: string | null) {
  const base = (s ?? "Otros").split("·")[0]?.trim() ?? "Otros";
  return base.charAt(0) + base.slice(1).toLowerCase();
}

export function fechaLarga(iso: string | null) {
  if (!iso) return "—";
  return new Date(`${iso}T12:00:00`).toLocaleDateString("es-CO", { day: "numeric", month: "long", year: "numeric" });
}
