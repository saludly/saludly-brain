/**
 * Saludly · Simulación de la semana de prueba de una persona (Node 24 o Deno), con una base falsa en memoria y sin
 * llamar a Meta: arrancar, envíos a su hora, ventana de 24 horas cerrada (una plantilla al día y lo demás esperando),
 * "Ver ahora" y el cierre del día 7.
 *
 * Uso: node supabase/functions/_compartido/probar_envios.ts
 */
// deno-lint-ignore no-explicit-any
const G = globalThis as any;
// Sin SUPABASE_URL: los salientes no se guardan en whatsapp_mensajes (aquí solo se cuentan los envíos a Meta)
G.Deno ??= { env: { get: (k: string) => (k.startsWith("SUPABASE_") ? undefined : "prueba") } };
// deno-lint-ignore no-explicit-any
const enviados: any[] = [];
G.fetch = async (_url: string, init: { body: string }) => {
  enviados.push(JSON.parse(init.body));
  return new Response("{}", { status: 200 });
};

const { arrancar, entregar } = await import("./semana_envios.ts");

// Base falsa: lo justo de la API de supabase-js que usa semana_envios.ts
// deno-lint-ignore no-explicit-any
const tablas: Record<string, any[]> = { semana_envios: [], preregistros: [] };
let sec = 1;
// deno-lint-ignore no-explicit-any
function consulta(tabla: string, cambio: any = null) {
  // deno-lint-ignore no-explicit-any
  const filtros: ((f: any) => boolean)[] = [];
  // deno-lint-ignore no-explicit-any
  const q: any = {
    eq: (c: string, v: unknown) => (filtros.push((f) => f[c] === v), q),
    in: (c: string, v: unknown[]) => (filtros.push((f) => v.includes(f[c])), q),
    lte: (c: string, v: string) => (filtros.push((f) => f[c] <= v), q),
    select: () => q,
    then: (ok: (r: unknown) => void) => {
      const filas = tablas[tabla].filter((f) => filtros.every((p) => p(f)));
      if (cambio) filas.forEach((f) => Object.assign(f, cambio));
      ok({ data: filas.map((f) => ({ ...f })), error: null });
    },
  };
  return q;
}
const admin = {
  from: (t: string) => ({
    // deno-lint-ignore no-explicit-any
    insert: async (filas: any[]) => { tablas[t].push(...filas.map((f) => ({ id: sec++, estado: "pendiente", ...f }))); return { error: null }; },
    update: (c: unknown) => consulta(t, c),
  }),
};

let total = 0, malas = 0;
function ok(cond: boolean, que: string) { total++; if (!cond) { malas++; console.log("✗", que); } }
const bog = (s: string) => new Date(s + ":00-05:00");
const estado = (dia: number, envio: string) => tablas.semana_envios.filter((f) => f.dia === dia && f.envio === envio).map((f) => f.estado);
const ultimos = () => enviados.splice(0);

const p = {
  id: "u1", nombre: "Ana María Rojas", celular_whatsapp: "573001112233", objetivos: ["maraton", "bajar_peso", "energia_sueno"], alergias: ["mani"],
  codigo: "a1b2c3", estado: "registrado", quiere_prueba: true, prueba_inicio: null as string | null, prueba_dia: 0,
  ultimo_mensaje: bog("2026-10-26T10:00").toISOString() as string | null, ultima_plantilla: null as string | null, bienvenida_enviada: null, creado: "",
};
tablas.preregistros.push(p);

// Día 1, escribe hola a las 10:00
ok(await arrancar(admin, p, bog("2026-10-26T10:00")), "arranca la semana");
ok(!(await arrancar(admin, p, bog("2026-10-26T10:05"))), "no la arma dos veces");
await entregar(admin, p, bog("2026-10-26T10:00"));
let e = ultimos();
ok(e.length === 2 && e[0].text.body.startsWith("¡Hola, Ana!") && e[1].text.body.includes("*Día 1 de 7*"), "10:00 bienvenida y consejos de la mañana");
ok(e[1].text.body.includes("🏃") || e[1].text.body.split("\n\n").length >= 4, "los consejos traen los 3 objetivos en un mensaje");
await entregar(admin, p, bog("2026-10-26T11:00"));
ok(ultimos().length === 0, "11:00 nada");
await entregar(admin, p, bog("2026-10-26T12:00"));
e = ultimos();
ok(e.length === 2 && e[0].type === "text" && e[1].type === "interactive" && e[1].interactive.action.buttons.length === 3, "12:00 receta y pregunta con 3 botones");
ok(e[1].interactive.action.buttons[0].reply.id.startsWith("sp:1:"), "los botones llevan el id del día");
await entregar(admin, p, bog("2026-10-26T13:00"));
ok(ultimos()[0]?.text.body.startsWith("🌿"), "13:00 cortisol");
await entregar(admin, p, bog("2026-10-26T18:00"));
ok(ultimos()[0]?.interactive.body.text.startsWith("🩸"), "18:00 solo tu examen lo dice");
await entregar(admin, p, bog("2026-10-26T19:30"));
ok(ultimos()[0]?.text.body.includes("consejos de la tarde"), "19:30 consejos de la tarde");
ok(p.prueba_dia === 1, "va en el día 1");

// No vuelve a escribir: el día 2 a las 7 la ventana sigue abierta (21 h); a las 9, como su último mensaje fue a las
// 8:30 del día 1, ya está cerrada
await entregar(admin, p, bog("2026-10-27T07:00"));
ok(ultimos().length === 1, "día 2, 7:00 consejos (ventana abierta)");
p.ultimo_mensaje = bog("2026-10-26T08:30").toISOString();
await entregar(admin, p, bog("2026-10-27T09:00"));
e = ultimos();
ok(e.length === 1 && e[0].type === "template" && e[0].template.name === "recordatorio_dia", "día 2, 9:00 ventana cerrada: plantilla recordatorio_dia");
ok(e[0].template.components[0].parameters[1].text.startsWith("tu receta de hoy: "), "la plantilla dice qué le espera");
ok(estado(2, "receta").every((s) => s === "esperando"), "la receta queda esperando");
await entregar(admin, p, bog("2026-10-27T18:00"));
ok(ultimos().length === 0 && estado(2, "examen")[0] === "esperando", "18:00 sin segunda plantilla el mismo día");

// Toca "Ver ahora" a las 20:00: le llega lo pendiente en orden
p.ultimo_mensaje = bog("2026-10-27T20:00").toISOString();
await entregar(admin, p, bog("2026-10-27T20:00"));
e = ultimos();
ok(e.length === 4 && e[0].type === "text" && e[1].type === "interactive" && e[2].type === "interactive", "Ver ahora: receta, pregunta, examen y consejos de la tarde");
ok(tablas.semana_envios.filter((f) => f.dia <= 2).every((f) => f.estado === "enviado"), "días 1 y 2 enviados");

// Día 7 con la ventana cerrada: la plantilla del cierre
p.ultimo_mensaje = bog("2026-10-31T20:00").toISOString();
for (const f of tablas.semana_envios.filter((f) => f.dia < 7)) f.estado = "enviado";
await entregar(admin, p, bog("2026-11-01T09:00"));
ultimos();
p.ultimo_mensaje = bog("2026-10-31T15:00").toISOString();
p.ultima_plantilla = "2026-10-31";
await entregar(admin, p, bog("2026-11-01T18:00"));
e = ultimos();
ok(e.length === 1 && e[0].template?.name === "cierre_semana", "día 7, 18:00 ventana cerrada: plantilla cierre_semana");

// BAJA: nada más
p.estado = "baja";
p.ultimo_mensaje = bog("2026-11-01T19:00").toISOString();
ok((await entregar(admin, p, bog("2026-11-01T19:00"))) === 0 && ultimos().length === 0, "con BAJA no se envía nada");

console.log(`${total - malas} de ${total}`);
if (malas) G.process?.exit(1);
