/**
 * Saludly · Prueba del programador de la semana de prueba (corre con Node 24 o con Deno).
 *
 * 1. Los mensajes que arma semana.ts deben ser iguales, letra por letra, a los de codigo/informe/semana_prueba.py.
 * 2. Las horas de envío del día 1 siguen semana_prueba.yaml > dia_1, y los días 2 a 7 los horarios fijos.
 * 3. Las respuestas a los botones: día 7, cierre, interés.
 *
 * Uso:
 *   python codigo/herramientas/exportar_semana.py --esperado esperado.json
 *   node supabase/functions/_compartido/probar_semana.ts esperado.json
 */
import { readFileSync } from "node:fs";
import { horaDeEnvio, mensajes, planRecetas, respuestaBoton, semana } from "./semana.ts";

let total = 0, malas = 0;
function ok(cond: boolean, que: string) {
  total++;
  if (!cond) { malas++; console.log("✗", que); }
}

const esperado = JSON.parse(readFileSync(process.argv[2], "utf-8"));
for (const { persona, dias } of esperado) {
  const recetas = await planRecetas(persona);
  for (let d = 1; d <= 7; d++) {
    const ts = mensajes(persona, d, recetas), py = dias[d - 1];
    ok(JSON.stringify(ts) === JSON.stringify(py), `${persona.nombre} (${persona.objetivos.join("+")}) día ${d}: distinto del Python`);
  }
}

// Horas (Bogotá = UTC-5): "2026-10-26T10:00" en Bogotá es 15:00 UTC
const bog = (s: string) => new Date(s + ":00-05:00");
const hora = (inicio: string, dia: number, envio: string) => horaDeEnvio(bog(inicio), dia, envio).toISOString();
const iso = (s: string) => bog(s).toISOString();
ok(hora("2026-10-26T10:00", 1, "manana") === iso("2026-10-26T10:00"), "día 1 a las 10: consejos de una vez");
ok(hora("2026-10-26T10:00", 1, "receta") === iso("2026-10-26T12:00"), "día 1 a las 10: receta 2 horas después");
ok(hora("2026-10-26T10:00", 1, "cortisol") === iso("2026-10-26T13:00"), "día 1 a las 10: cortisol a la 1");
ok(hora("2026-10-26T12:30", 1, "cortisol") === iso("2026-10-26T14:30"), "día 1 a las 12:30: cortisol con la receta");
ok(hora("2026-10-26T10:00", 1, "examen") === iso("2026-10-26T18:00"), "día 1: examen a las 6");
ok(hora("2026-10-26T10:00", 1, "tarde") === iso("2026-10-26T19:30"), "día 1: tarde a las 7:30");
ok(hora("2026-10-26T17:00", 1, "receta") === iso("2026-10-26T17:00"), "día 1 a las 5 p. m.: receta de una vez");
ok(hora("2026-10-26T17:00", 1, "examen") === iso("2026-10-26T19:00"), "día 1 a las 5 p. m.: examen 2 horas después");
ok(hora("2026-10-26T20:00", 1, "tarde") === iso("2026-10-27T07:00"), "día 1 a las 8 p. m.: lo demás al otro día a las 7");
ok(hora("2026-10-26T23:30", 1, "manana") === iso("2026-10-26T23:30"), "día 1 a las 11:30 p. m.: bienvenida de una vez");
ok(hora("2026-10-26T23:30", 2, "manana") === iso("2026-10-27T07:00"), "día 2: consejos a las 7");
ok(hora("2026-10-26T10:00", 7, "examen") === iso("2026-11-01T18:00"), "día 7: cierre a las 6 p. m.");
ok(hora("2026-10-26T10:00", 3, "receta") === iso("2026-10-28T09:00"), "día 3: receta a las 9");

const filas = await semana(esperado[10].persona, bog("2026-10-26T10:00"));
ok(filas.length === esperado[10].dias.flat().length, "semana(): una fila por mensaje");
ok(filas.every((f) => f.resumen && !f.resumen.includes("{")), "semana(): resumen de la plantilla sin variables sueltas");
ok(new Set(filas.map((f) => `${f.dia}|${f.orden}`)).size === filas.length, "semana(): día y orden sin repetir");

ok(respuestaBoton("Mañana sí", 3, "Ana María").texto!.includes("Mañana a las 7"), "días 1 a 6: respuesta de siempre");
ok(!respuestaBoton("¡Sí, quiero más!", 7, "Ana").texto!.includes("Mañana"), "día 7: no promete mañana");
ok(respuestaBoton("Quiero mi cupo", 7, "Ana").cupo, "Quiero mi cupo marca el anticipo");
ok(respuestaBoton("Cuéntame más", 2, "Ana").interes, "Cuéntame más marca interés");
ok(respuestaBoton("Quiero saber", 7, "Ana").texto === null, "Quiero saber de la plantilla: solo entrega el cierre");

console.log(`${total - malas} de ${total}`);
if (malas) process.exit(1);
