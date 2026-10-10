# Lector del PDF de resultados · Fase 3 · Informe de pruebas

**Saludly Brain · versión 1 · 6 de octubre de 2026**

El lector convierte el PDF del laboratorio en datos estructurados, listos para el motor de análisis (Fase 4). Está escrito en Python, se probó aquí con los dos PDF de ejemplo y queda listo para instalarse en el servidor cuando exista. El código, las pruebas y las instrucciones van en el zip.

## Resultado de las pruebas

| Prueba | Resultado |
| --- | --- |
| PDF del hombre de 46 años (127 resultados) | 1.497 de 1.497 campos correctos (100 %) |
| PDF de la mujer de 34 años (137 resultados) | 1.615 de 1.615 campos correctos (100 %) |
| Orden equivocada | Rechazado |
| Documento equivocado | Rechazado |
| PDF con páginas de dos pacientes | Rechazado, nombrando los dos documentos y las dos órdenes |
| Glucosa en mmol/L con regla de conversión | Convertida a mg/dL (6,2 → 111,7) |
| Ácido úrico en µmol/L sin regla | Marcado como duda; no se convierte |
| Analito que no existe en el catálogo ("Lipoproteína X") | Marcado como duda; no se asigna a ningún biomarcador |
| Resultado repetido en otra página | Marcado como duplicado |
| Potasio hemolizado y vitamina C no apta | Estado inválido y duda |

Los campos comparados en cada resultado son: nombre, biomarcador, campo, valor original, valor numérico, indicador, unidad, intervalo, método, sección, muestra y si es refleja.

## Qué tan lejos llega este 100 %

El 100 % prueba que el lector lee bien **el formato que yo mismo diseñé**. No prueba que lea bien el PDF real del laboratorio aliado, que tendrá otro diseño. Cuando llegue ese formato, hay que ajustar las constantes de formato del lector y volver a correr las mismas pruebas con PDF reales. Lo que sí se mantiene con cualquier formato: la verificación de identidad, la normalización con sinónimos, los estados del dato, las conversiones solo por tabla y las dudas.

## Un error que encontraron las pruebas

La primera versión del lector, cuando no encontraba un nombre exacto, buscaba el sinónimo más parecido. Con el analito sembrado "Lipoproteína X" eso lo asignó a la Lp(a), que es otra prueba. Ahora el lector solo acepta coincidencias exactas y todo lo demás queda como duda para que operaciones lo revise. Es la misma regla del documento 02: si un valor no se reconoce, no se inventa.

## Qué entrega el lector por cada PDF

- Estado: aceptado o rechazado, con el motivo.
- Huella SHA-256 del archivo, para trazabilidad.
- Encabezado: paciente, documento, edad, sexo, orden, fechas de toma, recepción y validación, ayuno.
- Metadatos del PDF.
- Cada resultado con el contrato del documento 10 (sección 10.3): biomarcador, valor, estado, operador, unidad, intervalo interpretado, indicador, método, sección, muestra, página, si es refleja y qué la activó, más sus dudas.
- Observaciones del laboratorio.
- Lista de dudas para operaciones.

## Salida textual de las pruebas

```
E2E-01: 1497/1497 campos correctos (100.0 %)
E2E-02: 1615/1615 campos correctos (100.0 %)
Orden equivocada: rechazado · El PDF no coincide con la visita: PDF CC 0000000002 / LCD-2026-100124, visita CC 0000000002 / LCD-2026-999999
Documento equivocado: rechazado · El PDF no coincide con la visita: PDF CC 0000000002 / LCD-2026-100124, visita CC 0000000001 / LCD-2026-100124
PDF con páginas de dos pacientes: rechazado · Las páginas no son del mismo paciente u orden: documentos ['CC 0000000001', 'CC 0000000002'], órdenes ['LCD-2026-100123', 'LCD-2026-100124']
Glucosa en mmol/L: 6.2 mmol/L -> 111.6992 mg/dL
  duda: Ácido úrico: Unidad 'µmol/L' distinta de la canónica 'mg/dL' y sin regla de conversión.
  duda: Lipoproteína X: Nombre no reconocido en el diccionario de sinónimos.
  duda: Triglicéridos: Resultado duplicado (también en la página 1).
  duda: Antígeno de Helicobacter pylori en heces: El laboratorio marcó este resultado con una observación (*).
```

## Lo que sigue

1. **Fase 4 · Motor de análisis.** Toma la salida del lector y aplica cálculos, clasificación, confusores, condiciones, relaciones y seguridad del Knowledge Base. Se prueba contra los hallazgos esperados de los dos casos de punta a punta.
2. **Formato real del laboratorio.** Cuando llegue, se ajusta el lector y se repiten estas pruebas.
3. **Panel de operaciones (Fase 6).** El lector se conecta a la pantalla donde operaciones carga el PDF y ve las dudas.