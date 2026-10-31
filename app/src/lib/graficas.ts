/**
 * Gráficas de la línea GLP-1 (paciente y doctora), en SVG con los colores del tema (un solo tono de marca;
 * el color de estado siempre va con su texto). Cada marca lleva data-tip para el tooltip.
 * Mismo diseño del demo aprobado (docs/07_linea_glp1/demo_glp1.plantilla.html).
 */
import { fmt, esAlarma, textoSintoma, type Registro, type Tratamiento } from "./peso";

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]!);
const T = (x: number, y: number, s: string, a = "start", extra = "") => `<text x="${x}" y="${y}" text-anchor="${a}" class="ley" ${extra}>${esc(s)}</text>`;
export const CIRC = 326.73;

/** Peso semanal con la meta. */
export function grafPeso(serie: { semana: number; peso: number }[], meta: number, w = 380, h = 210) {
  const L0 = 34, R0 = 64, T0 = 12, B0 = 24;
  const ps = serie.map((p) => p.peso);
  const min = Math.floor(Math.min(meta, ...ps) - 1), max = Math.ceil(Math.max(...ps) + 1);
  const smax = Math.max(1, serie[serie.length - 1].semana);
  const X = (s: number) => L0 + (s / smax) * (w - L0 - R0), Y = (v: number) => T0 + ((max - v) / (max - min)) * (h - T0 - B0);
  const ticks = [max, Math.round((max + min) / 2), min];
  const pts = serie.map((p) => `${X(p.semana).toFixed(1)},${Y(p.peso).toFixed(1)}`).join(" ");
  const u = serie[serie.length - 1];
  return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Peso de ${fmt(serie[0].peso)} a ${fmt(u.peso)} kg, meta ${fmt(meta, 0)} kg">
    ${ticks.map((t) => `<line x1="${L0}" x2="${w - R0}" y1="${Y(t)}" y2="${Y(t)}" stroke="var(--ios-sep)" stroke-width="1"/>${T(L0 - 6, Y(t) + 4, String(t), "end")}`).join("")}
    <line x1="${L0}" x2="${w - R0}" y1="${Y(meta)}" y2="${Y(meta)}" stroke="var(--ios-green)" stroke-width="1.5" stroke-dasharray="5 4"/>
    ${T(w - R0 + 6, Y(meta) + 4, "Meta " + fmt(meta, 0))}
    <polygon points="${X(0)},${Y(min)} ${pts} ${X(u.semana)},${Y(min)}" fill="var(--marca)" fill-opacity=".08"/>
    <polyline points="${pts}" fill="none" stroke="var(--marca)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
    ${serie.map((p, i) => `<circle cx="${X(p.semana)}" cy="${Y(p.peso)}" r="${i === serie.length - 1 ? 5 : 3}" fill="var(--marca)" stroke="var(--ios-card)" stroke-width="2"/><circle cx="${X(p.semana)}" cy="${Y(p.peso)}" r="11" fill="transparent" data-tip="${p.semana ? "Semana " + p.semana : "Inicio"} · ${fmt(p.peso)} kg"/>`).join("")}
    ${T(w - R0 + 6, Y(u.peso) + 4, fmt(u.peso) + " kg", "start", 'style="font-weight:600;fill:var(--ios-label)"')}
    ${T(L0, h - 6, "Inicio")}${T(w - R0, h - 6, "Semana " + u.semana, "end")}
  </svg>`;
}

/** Porcentaje del peso que bajó cada semana, con el límite de la doctora. */
export function grafVel(serie: { semana: number; peso: number }[], limite: number, w = 380, h = 190) {
  if (serie.length < 2) return `<p class="nota">Aparece con el segundo registro.</p>`;
  const v = serie.slice(1).map((p, i) => ({ s: p.semana, x: (((serie[i].peso - p.peso) / serie[i].peso) * 100) / Math.max(1, p.semana - serie[i].semana) }));
  const L0 = 34, R0 = 64, T0 = 14, B0 = 24, n = v.length;
  const max = Math.max(limite * 1.5, ...v.map((a) => a.x)), min = Math.min(0, ...v.map((a) => a.x)) - 0.2;
  const Y = (x: number) => T0 + ((max - x) / (max - min)) * (h - T0 - B0), paso = (w - L0 - R0) / n, ancho = Math.min(18, paso * 0.62);
  const sobre = v.some((a) => a.x > limite);
  return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Pérdida semanal; límite ${fmt(limite)} % por semana">
    <line x1="${L0}" x2="${w - R0}" y1="${Y(0)}" y2="${Y(0)}" stroke="var(--ios-sep)"/>${T(L0 - 6, Y(0) + 4, "0", "end")}
    ${v.map((a, i) => {
      const cx = L0 + paso * (i + 0.5), y = Math.min(Y(a.x), Y(0)), hh = Math.max(2, Math.abs(Y(a.x) - Y(0)));
      const col = a.x > limite ? "var(--media)" : a.x < 0 ? "var(--baja)" : "var(--marca)";
      return `<rect x="${(cx - ancho / 2).toFixed(1)}" y="${y.toFixed(1)}" width="${ancho.toFixed(1)}" height="${hh.toFixed(1)}" rx="3" fill="${col}"/>` +
        `<rect x="${(cx - paso / 2).toFixed(1)}" y="${T0}" width="${paso.toFixed(1)}" height="${h - T0 - B0}" fill="transparent" data-tip="Semana ${a.s} · ${a.x >= 0 ? "bajó" : "subió"} ${fmt(Math.abs(a.x))} %${a.x > limite ? " (sobre su límite)" : ""}"/>`;
    }).join("")}
    <line x1="${L0}" x2="${w - R0}" y1="${Y(limite)}" y2="${Y(limite)}" stroke="var(--media)" stroke-width="1.5" stroke-dasharray="5 4"/>
    ${T(w - R0 + 6, Y(limite) + 4, "Su límite")}${T(w - R0 + 6, Y(limite) + 18, fmt(limite) + " %/sem")}
    ${T(L0, h - 6, "Semana " + v[0].s)}${T(w - R0, h - 6, "Semana " + v[n - 1].s, "end")}
    ${sobre ? `<rect x="${L0 + 120}" y="${h - 15}" width="10" height="10" rx="2" fill="var(--media)"/>${T(L0 + 134, h - 6, "Sobre su límite")}` : ""}
  </svg>`;
}

/** Barras de inicio → hoy → meta (cintura y grasa estimada). */
export function bullet(filas: { n: string; ini: number; hoy: number; meta: number; u: string; d: number }[], w = 380) {
  const fh = 64, h = filas.length * fh + 6, L0 = 96, R0 = 20;
  return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Inicio, hoy y meta">${filas.map((f, k) => {
    const y = 26 + k * fh, lo = f.meta - (f.ini - f.meta) * 0.12, hi = f.ini + (f.ini - f.meta) * 0.12;
    const X = (v: number) => L0 + ((Math.max(lo, Math.min(hi, v)) - lo) / (hi - lo)) * (w - L0 - R0);
    return `${T(0, y + 4, f.n, "start", 'style="font-size:14px;font-weight:600;fill:var(--ios-label)"')}
      <line x1="${X(f.meta)}" x2="${X(f.ini)}" y1="${y}" y2="${y}" stroke="var(--ios-fill)" stroke-width="10" stroke-linecap="round"/>
      <line x1="${X(f.hoy)}" x2="${X(f.ini)}" y1="${y}" y2="${y}" stroke="var(--marca)" stroke-width="10" stroke-linecap="round" opacity=".9"/>
      <line x1="${X(f.meta)}" x2="${X(f.meta)}" y1="${y - 10}" y2="${y + 10}" stroke="var(--ios-green)" stroke-width="2"/>
      <circle cx="${X(f.hoy)}" cy="${y}" r="8" fill="var(--marca)" stroke="var(--ios-card)" stroke-width="3" data-tip="${esc(f.n)} hoy · ${fmt(f.hoy, f.d)} ${f.u}"/>
      ${T(X(f.hoy), y - 14, "Hoy " + fmt(f.hoy, f.d) + " " + f.u, "middle", 'style="font-weight:600;fill:var(--ios-label)"')}
      ${T(X(f.meta), y + 26, "Meta " + fmt(f.meta, f.d), "middle")}${T(X(f.ini), y + 26, "Inicio " + fmt(f.ini, f.d), "middle")}`;
  }).join("")}</svg>`;
}

/** Laboratorios: antes y ahora, con el valor de referencia. */
export function pesas(labs: { n: string; antes: number | null; ahora: number; u: string; ref: number | null; d: number }[], w = 380) {
  const fh = 58, h = labs.length * fh + 4, L0 = 104, R0 = 20;
  return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Laboratorios antes y ahora">${labs.map((l, k) => {
    const y = 28 + k * fh, vals = [l.antes, l.ahora, l.ref].filter((x): x is number => x != null), lo = Math.min(...vals), hi = Math.max(...vals), pad = (hi - lo) * 0.25 || Math.abs(hi) * 0.1 || 1;
    const X = (v: number) => L0 + ((v - (lo - pad)) / (hi - lo + 2 * pad)) * (w - L0 - R0);
    return `${T(0, y + 4, l.n, "start", 'style="font-size:13px;font-weight:600;fill:var(--ios-label)"')}
      <line x1="${L0}" x2="${w - R0}" y1="${y}" y2="${y}" stroke="var(--ios-sep)"/>
      ${l.ref != null ? `<line x1="${X(l.ref)}" x2="${X(l.ref)}" y1="${y - 12}" y2="${y + 12}" stroke="var(--ios-2)" stroke-dasharray="2 3"/>${T(X(l.ref), y + 26, "Referencia " + fmt(l.ref, l.d), "middle")}` : ""}
      ${l.antes != null ? `<line x1="${X(l.antes)}" x2="${X(l.ahora)}" y1="${y}" y2="${y}" stroke="var(--marca)" stroke-width="2.5"/>
      <circle cx="${X(l.antes)}" cy="${y}" r="6" fill="var(--ios-card)" stroke="var(--marca)" stroke-width="2" data-tip="${esc(l.n)} antes · ${fmt(l.antes, l.d)} ${l.u}"/>${T(X(l.antes), y - 13, fmt(l.antes, l.d), "middle")}` : ""}
      <circle cx="${X(l.ahora)}" cy="${y}" r="7" fill="var(--marca)" stroke="var(--ios-card)" stroke-width="2" data-tip="${esc(l.n)} · ${fmt(l.ahora, l.d)} ${l.u}"/>
      ${T(X(l.ahora), y - 13, fmt(l.ahora, l.d) + " " + l.u, "middle", 'style="font-weight:600;fill:var(--ios-label)"')}`;
  }).join("")}</svg>`;
}

/** Semanas desde el inicio con registro, aplicación y metas cumplidas. */
export function constancia(t: Tratamiento, registros: Registro[], semanas: number, w = 380) {
  const ini = new Date(t.fecha_inicio + "T12:00:00").getTime();
  const sem = (r: Registro) => Math.max(1, Math.ceil((new Date(r.fecha + "T12:00:00").getTime() - ini) / (7 * 864e5)));
  const n = Math.max(1, Math.min(semanas, 26)), desde = semanas - n + 1;
  const de = (f: (r: Registro) => boolean) => Array.from({ length: n }, (_, i) => registros.some((r) => sem(r) === desde + i && f(r)));
  const filas: [string, boolean[], string, string][] = [
    ["Registró", de((r) => r.peso != null), "registró peso", "no registró"],
    ["Aplicación", de((r) => r.aplicada === true), "marcó la aplicación", "sin marcar"],
    ["Metas", de((r) => !!r.metas_total && r.metas_cumplidas === r.metas_total), "cumplió sus metas", "no las cumplió"],
  ];
  const L0 = 78, cel = Math.min(16, (w - L0) / n - 4), g = 4, h = filas.length * (cel + 10) + 20;
  return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Constancia semanal">${filas.map((f, k) => {
    const y = k * (cel + 10);
    return T(0, y + cel - 3, f[0], "start", 'style="font-size:13px;fill:var(--ios-label)"') + f[1].map((x, i) =>
      `<rect x="${L0 + i * (cel + g)}" y="${y}" width="${cel}" height="${cel}" rx="4" fill="${x ? "var(--marca)" : "var(--ios-fill)"}" data-tip="Semana ${desde + i} · ${x ? f[2] : f[3]}"/>`).join("");
  }).join("")}${T(L0, h - 4, "Semana " + desde)}${T(L0 + (n - 1) * (cel + g) + cel, h - 4, "Semana " + semanas, "end")}</svg>`;
}

/** Efectos que marcó la paciente, por semana; los de alarma en rojo con la palabra "alarma". */
export function efectos(t: Tratamiento, registros: Registro[], semanas: number, w = 380) {
  const ini = new Date(t.fecha_inicio + "T12:00:00").getTime();
  const por = new Map<string, Set<number>>();
  for (const r of registros) for (const s of r.sintomas) {
    if (s === "bien") continue;
    const sm = Math.max(1, Math.ceil((new Date(r.fecha + "T12:00:00").getTime() - ini) / (7 * 864e5)));
    if (!por.has(s)) por.set(s, new Set());
    por.get(s)!.add(sm);
  }
  const filas = [...por.entries()];
  if (!filas.length) return `<p class="nota" style="margin:0">No ha reportado efectos.</p>`;
  const L0 = 136, R0 = 10, fh = 28, h = filas.length * fh + 26, X = (s: number) => L0 + ((s - 1) / Math.max(1, semanas - 1)) * (w - L0 - R0);
  return `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Efectos reportados por semana">${filas.map(([id, sems], k) => {
    const y = 14 + k * fh, al = esAlarma(id), nom = textoSintoma(id);
    return `${T(0, y + 4, nom + (al ? " · alarma" : ""), "start", `style="font-size:13px;fill:${al ? "var(--alta)" : "var(--ios-label)"};font-weight:${al ? 600 : 400}"`)}
      <line x1="${L0}" x2="${w - R0}" y1="${y}" y2="${y}" stroke="var(--ios-sep)"/>
      ${[...sems].map((s) => `<circle cx="${X(s)}" cy="${y}" r="6" fill="${al ? "var(--alta)" : "var(--marca)"}" stroke="var(--ios-card)" stroke-width="2" data-tip="${esc(nom)} · semana ${s}"/>`).join("")}`;
  }).join("")}${T(L0, h - 4, "Semana 1")}${T(w - R0, h - 4, "Semana " + semanas, "end")}</svg>`;
}
