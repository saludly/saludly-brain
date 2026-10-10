# Motor de análisis · Parte 4: relaciones, seguridad y salida final · Informe de pruebas

**Saludly Brain · Fase 4 · versión 1 · 6 de octubre de 2026**

La cuarta y última parte del motor evalúa las 27 relaciones entre módulos y las 15 fichas de seguridad, y arma la salida final: la lista ordenada de hallazgos que el agente convertirá en el informe del paciente, la vista para el médico, el escalamiento máximo y el canal de comunicación. Con esto el motor de análisis de la versión 1 queda completo.

## Resultado de las pruebas: 508 de 508 en todo el motor

| Parte | Qué prueba | Comprobaciones |
| --- | --- | --- |
| 1 | Cálculos y clasificación | 90 de 90 |
| 2 | Condiciones M1 y M2, más SCORE2-PURE | 167 de 167 |
| 3 | Condiciones M3 a M6 | 175 de 175 |
| 4 | Relaciones, seguridad y salida final | 76 de 76 |
| **Total** | Se corre con `python pruebas/probar_todo.py` | **508 de 508** |

La parte 4 comprueba:

- Las 27 relaciones en los dos casos de punta a punta: cuáles se activan, cuáles quedan para vigilar, cuáles quedan incompletas y cuáles no se activan, según el documento de relaciones.
- 13 relaciones con casos sembrados (hemólisis, PTH con TFG baja, patrón muscular, entre otras).
- 19 casos de las fichas de seguridad (troponina alta, eritroblastos, coagulopatía, CK muy alta con orina oscura, entre otros).
- Que una urgencia o una serología reactiva cambien el canal a llamada del equipo médico.
- Que ninguna condición aparezca dos veces en el informe.

## Cómo se arma el informe

1. **Patrones primero.** Si una relación de tipo patrón está activa y agrupa dos o más condiciones activas, esas condiciones salen juntas bajo el nombre del patrón. Una condición solo puede estar en un patrón: si ya está en otro, la relación queda anotada como "relacionado con".
2. **Patrón con una sola condición.** La condición sale sola, con el patrón anotado como contexto (por ejemplo, la dislipidemia del hombre lleva el patrón aterogénico, porque la ApoB también está alta).
3. **Orden.** Primero por escalamiento, de mayor a menor; dentro del mismo escalamiento, seguridad, luego patrones, luego condiciones, y después por coincidencia.
4. **Lo que no llega al paciente.** Las señales para vigilar, los apoyos, las pruebas reflejas pendientes, lo incompleto y lo no interpretable van solo a la vista médica.
5. **Canal.** Escalamiento 3 o serología reactiva: llamada del equipo médico antes de publicar. Escalamiento 2: revisión médica antes de publicar. En el piloto, el médico revisa todo.

## Hombre de 46 años

**Escalamiento máximo 2 · revisión médica antes de publicar.**

| # | Escalamiento | Tipo | Hallazgo | Detalle |
| --- | --- | --- | --- | --- |
| 1 | 2 | condicion | Infección por H. pylori |  |
| 2 | 1 | patron | Patrón cardiometabólico | Agrupa: COND-M1-EM-001, COND-M1-EM-003, COND-M1-CA-003. |
| 3 | 1 | condicion | Dislipidemia aterogénica | Parte de: Patrón aterogénico. |
| 4 | 1 | condicion | Hepatitis B y estado frente a la vacuna |  |
| 5 | 1 | condicion | Ácido úrico alto sin síntomas |  |
| 6 | 1 | condicion | Albuminuria con TFG normal |  |
| 7 | 1 | condicion | Alteración hepatocelular | Parte de: Patrón hepático metabólico. |
| 8 | 0 | condicion | Vitamina D baja |  |

Edad biológica: 44.3 años (-1.7 frente a su edad).

**Vista médica**

- **Para vigilar:** Posible sobrecarga de hierro, Patrón cardiometabólico con inflamación, Vitamina D baja con hs-CRP alta.
- **Apoyos que refuerzan hallazgos:** Inflamación de bajo grado, Resistencia a la insulina por HOMA-IR, Lectura por edad del panel.
- **Pruebas reflejas pendientes:** COND-M4-GA-006.
- **Incompletas por falta de datos de la visita:** COND-M1-CA-005, COND-M1-CA-006, COND-M1-EM-004, COND-M1-EM-A01, COND-M4-GA-A02, COND-M6-MI-001.
- **No interpretables:** ninguna.
- **Revisión médica obligatoria de:** acth, cortisol, hs_troponin, igf1, nrbc, osmolality.

## Mujer de 34 años

**Escalamiento máximo 2 · revisión médica antes de publicar.** Recordatorio: tamizaje de cuello uterino.

| # | Escalamiento | Tipo | Hallazgo | Detalle |
| --- | --- | --- | --- | --- |
| 1 | 2 | patron | Patrón de déficit de hierro | Agrupa: COND-M3-HE-001, COND-M3-HE-002. |
| 2 | 2 | condicion | ANA positivo |  |
| 3 | 1 | condicion | Lipoproteína(a) elevada |  |
| 4 | 1 | condicion | Hipotiroidismo subclínico | Parte de: Patrón tiroideo autoinmune. |
| 5 | 1 | condicion | Dislipidemia aterogénica |  |
| 6 | 0 | condicion | Hepatitis B y estado frente a la vacuna |  |
| 7 | 0 | condicion | Vitamina D baja |  |

Edad biológica: 34.1 años (+0.1 frente a su edad); Anemia o RDW alto: el valor puede estar inflado.

**Vista médica**

- **Para vigilar:** Hierro bajo con anticuerpos tiroideos, TSH alta con colesterol, CK u homocisteína altos, TSH alterada con hierro bajo, Vitamina D baja con ferritina o hemoglobina bajas.
- **Apoyos que refuerzan hallazgos:** Autoinmunidad tiroidea, Lectura por edad del panel.
- **Pruebas reflejas pendientes:** ninguna.
- **Incompletas por falta de datos de la visita:** COND-M1-CA-006, COND-M1-EM-004, COND-M1-EM-A01, COND-M4-GA-A02, COND-M6-MI-001, REL-026.
- **No interpretables:** COND-M2-NE-004, COND-M2-NE-A01.
- **Revisión médica obligatoria de:** acth, cortisol, hs_troponin, igf1, nrbc, osmolality.

## Lo que encontraron las pruebas

- **Condiciones repetidas en dos patrones.** La primera versión ponía la prediabetes y los triglicéridos del hombre tanto en el patrón cardiometabólico como en el hepático metabólico. Ahora cada condición queda en un solo patrón y el segundo se anota como relacionado. La prueba que lo verifica quedó fija.
- **La edad biológica salía en la lista de hallazgos.** Debe ir en su pantalla aparte (ficha MI-A02); ya no entra en la lista.
- **Patrones con una sola condición.** El patrón aterogénico del hombre y el tiroideo autoinmune de la mujer agrupan una sola condición activa; ahora se muestran como contexto de esa condición en lugar de desaparecer.

## Pendientes

1. **La redacción.** El motor entrega la lista ordenada y las frases permitidas de cada ficha; la redacción del informe la hará DeepSeek cuando exista el servidor (Fase 2), con la validación de salida del documento 05.
2. **Criterios definidos por Saludly en las relaciones.** Hemólisis y "T4 libre límite" (décimo inferior del intervalo) siguen para revisión del médico.
3. **Relaciones con Apple Watch.** Funcionan con datos sembrados; falta la app de iOS (Fase 6) para probarlas con datos reales.
4. **Formulario de la enfermera.** Las pruebas mostraron que, sin la visita, quedan incompletas la presión, el riesgo cardiovascular, el peso, el FINDRISC, la desnutrición y el alcohol. Ese formulario es lo que más mejora el informe.

## Lo que sigue

Con el motor completo, termina todo lo que se puede construir sin servidor. Lo siguiente es la **Fase 2: el servidor en Hostinger con OpenClaw y DeepSeek**, que depende de comprar el plan. Ahí se instalan el lector y el motor, se conecta DeepSeek para la redacción y se prueba el flujo de punta a punta con los dos PDF. Mientras tanto, la demostración al médico ya se puede hacer con todo lo que hay.