/** Piezas de la línea GLP-1 que comparten la paciente y la doctora: anillo, silueta con capa y tooltip de las gráficas. */
import { useEffect, useRef, useState } from "react";
import silueta from "@/assets/silueta-mujer.webp";
import { CIRC } from "@/lib/graficas";

const reduce = () => typeof matchMedia !== "undefined" && matchMedia("(prefers-reduced-motion: reduce)").matches;

/** Anillo de progreso (0 a 1) con un número y una línea debajo. Se anima al cambiar. */
export function Anillo({ f, grande, chico, color = "var(--marca)", grosor = 12, clase = "anillo" }: { f: number; grande: string; chico?: string; color?: string; grosor?: number; clase?: string }) {
  const [v, setV] = useState(0);
  useEffect(() => {
    const id = requestAnimationFrame(() => setV(Math.max(0, Math.min(1, f))));
    return () => cancelAnimationFrame(id);
  }, [f]);
  return (
    <div className={clase}>
      <svg viewBox="0 0 120 120" aria-hidden="true">
        <circle cx="60" cy="60" r="52" fill="none" stroke="var(--ios-fill)" strokeWidth={grosor} />
        <circle className="val" cx="60" cy="60" r="52" fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round" strokeDasharray={CIRC} strokeDashoffset={CIRC * (1 - v)} />
      </svg>
      <div className="num">
        <div>
          <b>{grande}</b>
          {chico && <span>{chico}</span>}
        </div>
      </div>
    </div>
  );
}

/** Número que cuenta desde el valor anterior hasta el nuevo. */
export function useContador(valor: number) {
  const [n, setN] = useState(valor);
  const previo = useRef(valor);
  useEffect(() => {
    const desde = previo.current;
    previo.current = valor;
    if (reduce() || desde === valor) return void setN(valor);
    const t0 = performance.now();
    let id = 0;
    const paso = (t: number) => {
      const k = Math.min(1, (t - t0) / 1100);
      setN(Math.round(desde + (valor - desde) * (1 - Math.pow(1 - k, 3))));
      if (k < 1) id = requestAnimationFrame(paso);
    };
    id = requestAnimationFrame(paso);
    return () => cancelAnimationFrame(id);
  }, [valor]);
  return n;
}

/**
 * Silueta de la portada con la capa translúcida de lo que falta para la meta.
 * grosor: 1 = como al inicio del tratamiento, 0 = en la meta (la capa pegada al cuerpo).
 * La capa sigue el contorno de la figura y se acumula más en cintura, cadera y muslos.
 */
export function Silueta({ grosor }: { grosor: number }) {
  const lienzo = useRef<HTMLCanvasElement>(null);
  const datos = useRef<{ img: HTMLImageElement; W: number; H: number; dist: Float32Array; peso: Float32Array } | null>(null);
  const actual = useRef<number | null>(null);
  const TMAX = 30;

  const dibuja = (T: number) => {
    const c = lienzo.current, d = datos.current;
    if (!c || !d) return;
    const ctx = c.getContext("2d")!;
    ctx.clearRect(0, 0, d.W, d.H);
    const capa = ctx.createImageData(d.W, d.H), px = capa.data;
    const m = getComputedStyle(c).getPropertyValue("--capa").match(/[\d.]+/g)?.map(Number) ?? [39, 147, 255, 0.3];
    const [r, g, b, al] = m;
    for (let y = 0; y < d.H; y++) {
      const lim = T * d.peso[y];
      if (lim < 0.3) continue;
      for (let x = 0; x < d.W; x++) {
        const i = y * d.W + x, v = d.dist[i];
        if (v === 0 || v > lim + 1.5) continue;
        const borde = Math.min(1, (lim + 1.5 - v) / 1.5), filo = v > lim - 1.2 ? 1.6 : 1;
        const k = i * 4;
        px[k] = r; px[k + 1] = g; px[k + 2] = b; px[k + 3] = Math.min(255, 255 * al * borde * filo);
      }
    }
    ctx.putImageData(capa, 0, 0);
    ctx.drawImage(d.img, 0, 0);
  };

  useEffect(() => {
    const img = new Image();
    img.onload = () => {
      const W = img.naturalWidth, H = img.naturalHeight, c = lienzo.current;
      if (!c) return;
      c.width = W; c.height = H;
      const o = document.createElement("canvas");
      o.width = W; o.height = H;
      const oc = o.getContext("2d")!;
      oc.drawImage(img, 0, 0);
      const a = oc.getImageData(0, 0, W, H).data;
      // Distancia hacia afuera de la silueta (chaflán 3-4).
      const dist = new Float32Array(W * H), INF = 1e9;
      for (let i = 0; i < W * H; i++) dist[i] = a[i * 4 + 3] > 128 ? 0 : INF;
      for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
        const i = y * W + x; let d = dist[i]; if (!d) continue;
        if (x > 0) d = Math.min(d, dist[i - 1] + 3);
        if (y > 0) { d = Math.min(d, dist[i - W] + 3); if (x > 0) d = Math.min(d, dist[i - W - 1] + 4); if (x < W - 1) d = Math.min(d, dist[i - W + 1] + 4); }
        dist[i] = d;
      }
      for (let y = H - 1; y >= 0; y--) for (let x = W - 1; x >= 0; x--) {
        const i = y * W + x; let d = dist[i]; if (!d) continue;
        if (x < W - 1) d = Math.min(d, dist[i + 1] + 3);
        if (y < H - 1) { d = Math.min(d, dist[i + W] + 3); if (x < W - 1) d = Math.min(d, dist[i + W + 1] + 4); if (x > 0) d = Math.min(d, dist[i + W - 1] + 4); }
        dist[i] = d;
      }
      for (let i = 0; i < W * H; i++) dist[i] = dist[i] / 3;
      // Dónde se acumula: cintura, cadera y muslos más; cabeza, pantorrillas y pies casi nada.
      const zonas = [[0, 0.05], [0.15, 0.08], [0.2, 0.25], [0.3, 0.6], [0.4, 1], [0.5, 1], [0.6, 0.85], [0.7, 0.4], [0.8, 0.25], [0.92, 0.05], [1, 0]];
      const peso = new Float32Array(H);
      for (let y = 0; y < H; y++) {
        const t = y / H; let k = 0;
        while (k < zonas.length - 2 && zonas[k + 1][0] < t) k++;
        const [t0, w0] = zonas[k], [t1, w1] = zonas[k + 1];
        const u = Math.min(1, Math.max(0, (t - t0) / (t1 - t0)));
        peso[y] = w0 + (w1 - w0) * (u * u * (3 - 2 * u));
      }
      datos.current = { img, W, H, dist, peso };
      actual.current = grosor * TMAX;
      dibuja(actual.current);
    };
    img.src = silueta;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (!datos.current) return;
    const hasta = grosor * TMAX, desde = actual.current ?? hasta;
    actual.current = hasta;
    if (reduce()) return dibuja(hasta);
    const t0 = performance.now();
    let id = 0;
    const paso = (t: number) => {
      const k = Math.min(1, (t - t0) / 1400);
      dibuja(desde + (hasta - desde) * (1 - Math.pow(1 - k, 3)));
      if (k < 1) id = requestAnimationFrame(paso);
    };
    id = requestAnimationFrame(paso);
    return () => cancelAnimationFrame(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [grosor]);

  return (
    <div className="lienzo">
      <canvas ref={lienzo} aria-label="Silueta con la capa que te falta para tu meta" />
    </div>
  );
}

/** Tooltip de las gráficas (elementos con data-tip). */
export function Tooltip() {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const mover = (e: PointerEvent) => {
      const tip = ref.current;
      if (!tip) return;
      const t = (e.target as Element | null)?.closest?.("[data-tip]") as HTMLElement | null;
      if (!t) return void tip.classList.remove("on");
      tip.textContent = t.dataset.tip ?? "";
      tip.classList.add("on");
      tip.style.left = Math.min(innerWidth - tip.offsetWidth - 8, e.clientX + 14) + "px";
      tip.style.top = Math.max(8, e.clientY - tip.offsetHeight - 12) + "px";
    };
    document.addEventListener("pointermove", mover);
    return () => document.removeEventListener("pointermove", mover);
  }, []);
  return <div className="tip" ref={ref} role="tooltip" />;
}

/** Aviso tipo notificación de iOS que baja desde arriba. */
export function Notificacion({ aviso }: { aviso: { m: string; t: string; s: string; id: number } | null }) {
  const [on, setOn] = useState(false);
  useEffect(() => {
    if (!aviso) return;
    setOn(true);
    const id = setTimeout(() => setOn(false), 3600);
    return () => clearTimeout(id);
  }, [aviso]);
  return (
    <div className={`notif${on ? " on" : ""}`} role="status" aria-live="polite">
      <div className="m">{aviso?.m}</div>
      <div>
        <b>{aviso?.t}</b>
        <span>{aviso?.s}</span>
      </div>
    </div>
  );
}
