# Motor de análisis · Parte 2: condiciones de los módulos M1 y M2 · Informe de pruebas

**Saludly Brain · Fase 4 · versión 1 · 6 de octubre de 2026**

La segunda parte del motor evalúa las 34 fichas de condición de los módulos M1 (Cardiometabólico) y M2 (Riñón y glándulas) sobre la salida de la parte 1. Cada condición termina en un estado, con su coincidencia, su escalamiento, los criterios que se cumplieron, los datos que faltan y los confusores aplicados. Los metadatos (nombre, nivel de lenguaje, guías) se leen de cada ficha del Knowledge Base.

## Resultado de las pruebas: 167 de 167

| Grupo | Comprobaciones | Resultado |
| --- | --- | --- |
| Casos de punta a punta, módulos M1 y M2 (estado, coincidencia, escalamiento, lo que no debe activarse y lo incompleto) | 89 | Todas correctas |
| 69 casos unitarios estructurados, tomados de las fichas de condición | 78 | Todos correctos |
| SCORE2 frente al ejemplo publicado del artículo original (hombre y mujer, regiones baja y muy alta) | 4 | Todos idénticos (5,9 %, 14,0 %, 4,2 %, 13,7 %) |

La parte 1 se volvió a correr y sigue en 90 de 90.

## Los estados

| Estado | Qué significa |
| --- | --- |
| activa | La condición se cumple y aparece en el informe |
| apoyo | Refuerza otra condición; no aparece sola |
| vigilar | Coincidencia baja; solo en la vista médica salvo aprobación |
| control | Condición ya conocida o en tratamiento: se muestra como control al médico, no como hallazgo nuevo |
| pendiente_refleja | Falta una prueba refleja que el laboratorio debe correr (por ejemplo, NT-proBNP o PTH) |
| incompleta | Faltan datos que podrían activarla (sobre todo los de la enfermera) |
| no_calculable | La calculadora no aplica (por edad, diabetes) o aún no está implementada |
| no_interpretable | El contexto o la muestra impiden evaluarla |
| no_aplica / no_activa | No corresponde o no se cumple |

## Hombre de 46 años (sin datos de la enfermera)

| Ficha | Condición | Estado | Coincidencia | Escalamiento | Detalle |
| --- | --- | --- | --- | --- | --- |
| COND-M1-CA-001 | Dislipidemia aterogénica | activa | alta | 1 | ldl_alto, no_hdl_alto, hdl_bajo, tg_alto |
| COND-M1-CA-003 | Hipertrigliceridemia | activa | moderada | 1 | alcohol_48h |
| COND-M1-EM-001 | Prediabetes | activa | alta | 1 | glucosa, hba1c |
| COND-M1-EM-003 | Síndrome metabólico | activa | moderada | 1 | 3 de 5; cintura, presion |
| COND-M2-NE-002 | Albuminuria con TFG normal | activa | moderada | 1 | estadio G1 A2; segunda muestra |
| COND-M1-CA-A02 | Inflamación de bajo grado | apoyo |  |  | a confirmar con una segunda medición |
| COND-M1-EM-A02 | Resistencia a la insulina por HOMA-IR | apoyo |  |  | HOMA-IR 5.48: refuerza COND-M1-EM-001, COND-M1-EM-003 |
| COND-M1-CA-005 | Riesgo cardiovascular global elevado | incompleta |  |  | sin todas las entradas no se calcula porcentaje |
| COND-M1-CA-006 | Hipertensión arterial o presión elevada (sospecha) | incompleta |  |  | presion_enfermera |
| COND-M1-EM-004 | Obesidad y sobrepeso | incompleta |  |  | peso_kg, talla_m |
| COND-M1-EM-A01 | Riesgo alto de diabetes por FINDRISC | incompleta |  |  | findrisc_puntaje |

No activas o no aplican: COND-M1-CA-002, COND-M1-CA-004, COND-M1-CA-007, COND-M1-CA-A01, COND-M1-EM-002, COND-M1-EM-005, COND-M2-NE-001, COND-M2-NE-003, COND-M2-NE-004, COND-M2-NE-005, COND-M2-NE-006, COND-M2-NE-A01, COND-M2-NE-A02, COND-M2-NE-A03, COND-M2-TI-001, COND-M2-TI-002, COND-M2-TI-003, COND-M2-TI-004, COND-M2-TI-005, COND-M2-TI-006, COND-M2-TI-007, COND-M2-TI-008, COND-M2-TI-A01.

## Mujer de 34 años (sin datos de la enfermera)

| Ficha | Condición | Estado | Coincidencia | Escalamiento | Detalle |
| --- | --- | --- | --- | --- | --- |
| COND-M1-CA-001 | Dislipidemia aterogénica | activa | moderada | 1 | ldl_alto |
| COND-M1-CA-004 | Lipoproteína(a) elevada | activa | alta | 1 | lpa_alta |
| COND-M2-TI-001 | Hipotiroidismo subclínico | activa | alta | 1 | Si busca embarazo, comentarlo pronto con el médico. |
| COND-M2-TI-A01 | Autoinmunidad tiroidea | apoyo |  |  | causa autoinmune probable |
| COND-M1-CA-006 | Hipertensión arterial o presión elevada (sospecha) | incompleta |  |  | presion_enfermera |
| COND-M1-EM-004 | Obesidad y sobrepeso | incompleta |  |  | peso_kg, talla_m |
| COND-M1-EM-A01 | Riesgo alto de diabetes por FINDRISC | incompleta |  |  | findrisc_puntaje |
| COND-M1-CA-005 | Riesgo cardiovascular global elevado | no_calculable |  |  | solo se calcula entre 40 y 69 años; se muestran los factores de riesgo |
| COND-M2-NE-004 | Potasio alto | no_interpretable |  |  | potassium: resultado no válido según el laboratorio |
| COND-M2-NE-A01 | Potasio bajo | no_interpretable |  |  | potassium: resultado no válido según el laboratorio |

No activas o no aplican: COND-M1-CA-002, COND-M1-CA-003, COND-M1-CA-007, COND-M1-CA-A01, COND-M1-CA-A02, COND-M1-EM-002, COND-M1-EM-001, COND-M1-EM-003, COND-M1-EM-005, COND-M1-EM-A02, COND-M2-NE-001, COND-M2-NE-002, COND-M2-NE-003, COND-M2-NE-005, COND-M2-NE-006, COND-M2-NE-A02, COND-M2-NE-A03, COND-M2-TI-002, COND-M2-TI-003, COND-M2-TI-004, COND-M2-TI-005, COND-M2-TI-006, COND-M2-TI-007, COND-M2-TI-008.

## Lo que encontraron las pruebas

- **El caso esperado de triglicéridos estaba mal, no el motor.** La ficha de hipertrigliceridemia dice que, sin dato de alcohol en las últimas 48 horas, la coincidencia es moderada. Yo había escrito "alta" en el caso de punta a punta del hombre. Corregí el caso (y el documento de casos de prueba) para que siga a la ficha. Es justo lo que deben hacer estas pruebas: cuando el motor y el caso no coinciden, se revisa cuál de los dos contradice la ficha.
- **El potasio hemolizado salía como "incompleto" en la ficha de potasio bajo.** Debía salir como no interpretable, igual que en la de potasio alto. Corregido.
- **La confirmación con cistatina C no se aplicaba.** Si la TFG combinada con cistatina C era normal, el motor dejaba la enfermedad renal como no activa en lugar de "vigilar". Ya está corregido.

## Supuestos y pendientes

1. **SCORE2-PURE: resuelto.** La calculadora usa los coeficientes de SCORE2 (región de riesgo alto) multiplicados por 0,61 en hombres y 0,75 en mujeres, los factores de PURE-Colombia. Reproduce exactamente el ejemplo publicado del artículo original. Queda por confirmar si la GPC 2025 usa las mismas categorías por edad que la ESC 2021.
2. **TFG con cistatina C.** La ecuación CKD-EPI 2021 creatinina-cistatina se implementó de memoria; hay que verificar sus coeficientes contra la publicación.
3. **Glucosa baja.** El tiempo máximo de la toma al procesamiento que hace "confiable" una glucosa baja quedó en 4 horas como valor provisional; debe salir del protocolo validado por el laboratorio.
4. **Umbrales en el código.** Los umbrales están en el código de cada evaluador, citando su ficha. Una mejora para la versión 2 es leerlos directamente del YAML de la ficha, para que un cambio de umbral firmado por el médico no requiera tocar código.

## Lo que sigue

**Parte 3: las condiciones de los módulos M3 a M6** (42 fichas: sangre y nutrición, digestivo e infecciones, mujer y hombre, inmunidad y envejecimiento), con la misma estructura de pruebas.