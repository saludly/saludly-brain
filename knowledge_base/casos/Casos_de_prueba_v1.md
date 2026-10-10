# Set de casos de prueba · versión 1

**Saludly Brain · Knowledge Base · 6 de octubre de 2026**

Este es el set que el motor debe pasar antes de atender pacientes, y el documento para la primera demostración al médico. Junta en un solo lugar todos los casos que estaban repartidos en las fichas, más dos casos de punta a punta construidos con los PDF de ejemplo.

## Qué contiene

| Parte | Cantidad | Archivo |
| --- | --- | --- |
| Casos de punta a punta (un PDF completo de entrada, todo el informe esperado de salida) | 2 | `casos/e2e/E2E-01.json`, `E2E-02.json` |
| Casos unitarios (una ficha, unos datos, un resultado esperado) | 377 | `casos/casos_unitarios.yaml`, `.json` y `.csv` |
| · M1 | 68 |  |
| · M2 | 79 |  |
| · M3 | 60 |  |
| · M4 | 51 |  |
| · M5 | 35 |  |
| · M6 | 22 |  |
| · SEG | 53 |  |
| · Calculados | 9 |  |

## Cómo se usa

**Con el médico.** Se le muestran primero los dos casos de punta a punta, que son lo que vería un paciente real, y después los unitarios del módulo que quiera revisar. El archivo CSV abre en Excel o Google Sheets con dos columnas vacías, "aprobado" y "comentario", para que marque caso por caso.

**Con el motor.** Cada caso de punta a punta trae la entrada exactamente como sale de leer el PDF (127 y 137 resultados con su identificador, valor, estado, unidad, intervalo y método), el contexto de la visita y la lista de hallazgos esperados. La prueba pasa si el motor produce los mismos hallazgos, con la misma coincidencia y el mismo escalamiento. Criterio de paso propuesto (documento 04): cero errores en casos críticos y de escalamiento 3, y ninguna frase prohibida.

**Prueba del diccionario de sinónimos.** Al convertir los PDF en datos, los 264 resultados encontraron su biomarcador. Seis nombres del formato del laboratorio no estaban en los sinónimos (las serologías con su nombre largo, la troponina I y la relación albúmina/creatinina con sigla); se agregaron a sus fichas y el índice se regeneró.

## E2E-01 · Hombre de 46 años (orden LCD-2026-100123)

**Contexto:** 46 años, hombre, Bogotá, ayuno de 11 horas, toma a las 07:15. Sin datos de la enfermera (presión, medidas, cuestionario), a propósito, para probar qué hace el motor con datos faltantes.

**Hallazgos que debe mostrar el informe**

| Ficha | Estado | Coincidencia | Escalamiento | Nota |
| --- | --- | --- | --- | --- |
| COND-M1-EM-001 | activa | alta | 1 |  |
| COND-M1-CA-001 | activa | alta | 1 |  |
| COND-M1-CA-003 | activa | moderada | 1 | sin dato de alcohol en 48 horas: coincidencia moderada (regla de la ficha) |
| COND-M1-EM-003 | activa | moderada | 1 | 3 de 5 componentes; faltan cintura y presión |
| COND-M1-EM-A02 | apoyo |  |  | HOMA-IR 5,48 refuerza EM-001 y EM-003 |
| COND-M1-CA-A02 | apoyo |  |  | hs-CRP 3,4, a confirmar con segunda medición |
| COND-M2-NE-002 | activa | moderada | 1 | A2, una sola toma |
| COND-M3-NU-A03 | activa |  | 0 | vitamina D 21,4 baja; recomendación alimentaria |
| COND-M3-HE-006 | vigilar | baja |  | ferritina 310 con saturación normal, ligada al patrón hepático |
| COND-M4-GA-005 | activa | alta | 2 | incluye limitación del antígeno fecal |
| COND-M4-GA-002 | activa | moderada | 1 | ALT 58 |
| COND-M4-IN-002 | activa |  | 1 | estado susceptible; recomendación de vacuna |
| COND-M6-RE-001 | activa | alta | 1 |  |

**Incompletas, no calculables o no interpretables**

| Ficha o analito | Estado | Por qué |
| --- | --- | --- |
| COND-M1-CA-005 | incompleta | faltan presión y tabaquismo |
| COND-M1-CA-006 | incompleta | falta presión de la enfermera |
| COND-M1-EM-004 | incompleta | faltan peso y talla |
| COND-M4-GA-A02 | incompleta | falta dato de alcohol |
| COND-M6-MI-001 | incompleta | faltan peso y talla |

**Calculados esperados:** egfr = 96; homa_ir = 5.48; non_hdl_c = 192; remnant_cholesterol = 50; tc_hdl_ratio = 6.33; transferrin_saturation = 37; fib4 = 0.89; apob_apoa1_ratio = 1.05; ag_ratio = 1.7; globulin = 2.7; bun_creatinine_ratio = 15.3; phenoage = 44.3; testosterone_free = no se calcula (total 412 y sin IMC).

**No deben activarse:** COND-M1-CA-002, COND-M1-CA-004, COND-M1-EM-002, COND-M1-EM-005, COND-M1-CA-A01, COND-M2-NE-001, COND-M2-NE-004, COND-M2-NE-005, COND-M2-NE-006, COND-M2-TI-001, COND-M3-HE-001, COND-M3-HE-002, COND-M3-NU-001, COND-M4-GA-001, COND-M4-GA-004, COND-M4-IN-001, COND-M4-IN-003, COND-M5-UR-001, COND-M5-UR-002, COND-M6-RE-A01.

**Seguridad:** escalamiento 0 en todos los biomarcadores de solo valor y rango; revisión médica obligatoria de hs_troponin, cortisol, acth, igf1, osmolality, nrbc. Solo valor, sin clase: biotin, niacin, omega3_index, omega6_omega3_ratio, coq10.

**Escalamiento máximo del informe:** 2. El médico revisa antes de publicar.

- La ALT alta debería activar la refleja de celiaquía según el Consolidado; el PDF de ejemplo no la trae. Decidir si se corrige el PDF.

## E2E-02 · Mujer de 34 años (orden LCD-2026-100124)

**Contexto:** 34 años, mujer, Bogotá, ayuno de 12 horas, toma a las 07:40. Día 9 del ciclo, sin anticonceptivo hormonal. Sin datos de la enfermera (presión, medidas, cuestionario), a propósito, para probar qué hace el motor con datos faltantes.

**Hallazgos que debe mostrar el informe**

| Ficha | Estado | Coincidencia | Escalamiento | Nota |
| --- | --- | --- | --- | --- |
| COND-M3-HE-001 | activa | moderada | 2 | anemia moderada; hemoglobina ajustada 9,4; sin dato de tabaquismo: coincidencia moderada (regla de la ficha) |
| COND-M3-HE-002 | activa | alta | 2 | ferritina 7, saturación 8,8 %, VCM 78,2, RDW 16,4 |
| COND-M2-TI-001 | activa | alta | 1 | TSH 6,90 con T4 libre normal; frase para mujer en edad fértil |
| COND-M2-TI-A01 | apoyo |  |  | anti-TPO 186 |
| COND-M1-CA-004 | activa | alta | 1 | Lp(a) 64 mg/dL |
| COND-M1-CA-001 | activa | moderada | 1 | LDL 136, no-HDL 156 |
| COND-M3-NU-A03 | activa |  | 0 | vitamina D 17,8 baja; relación vigilar con ferritina y hemoglobina bajas |
| COND-M6-RE-A01 | activa |  | 2 | ANA 1:160, moteado fino; nota de autoinmunidad tiroidea |
| COND-M4-IN-002 | activa |  | 0 | inmune por vacuna |

**Incompletas, no calculables o no interpretables**

| Ficha o analito | Estado | Por qué |
| --- | --- | --- |
| COND-M1-CA-005 | no_calculable | fuera de 40 a 69 años |
| COND-M1-CA-006 | incompleta | falta presión |
| COND-M1-EM-004 | incompleta | faltan peso y talla |
| COND-M2-NE-004 | no_interpretable | potasio hemolizado; pedir nueva muestra |
| vitamin_c | no_interpretable | muestra no apta |
| COND-M6-MI-001 | incompleta | faltan peso y talla |

**Calculados esperados:** egfr = 112; homa_ir = 1.3; non_hdl_c = 156; remnant_cholesterol = 20; tc_hdl_ratio = 3.69; transferrin_saturation = 8.8; indice_androgenos_libres = 1.79; apob_apoa1_ratio = 0.58; ag_ratio = 1.59; globulin = 2.7; bun_creatinine_ratio = 13.9; hemoglobina_ajustada_altitud = 9.4; phenoage = 34.1; fib4 = no aplica.

**No deben activarse:** COND-M1-EM-001, COND-M1-EM-002, COND-M1-CA-003, COND-M1-EM-003, COND-M1-EM-005, COND-M3-NU-001, COND-M3-NU-002, COND-M3-HE-004, COND-M3-HE-006, COND-M3-HE-A01, COND-M4-GA-006, COND-M5-MU-001, COND-M5-MU-002, COND-M5-MU-003, COND-M2-NE-002, COND-M6-RE-001.

**Seguridad:** escalamiento 0 en todos los biomarcadores de solo valor y rango; revisión médica obligatoria de hs_troponin, cortisol, acth, igf1, osmolality, nrbc. Solo valor, sin clase: biotin, niacin, omega3_index, omega6_omega3_ratio, coq10.

**Recordatorios:** tamizaje de cuello uterino.

**Escalamiento máximo del informe:** 2. El médico revisa antes de publicar.

- PhenoAge se calcula con advertencia: la anemia sube el RDW.
- Reflejas activadas: T4 libre, T3 libre, anti-TPO, reticulocitos, IgA total, anti-tTG IgA, ácido metilmalónico.

## Casos unitarios

Uno por fila. El identificador es la ficha más el número del caso dentro de ella. Los que dicen "PDF" usan los valores de los PDF de ejemplo.

### M1

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| COND-M1-CA-001#01 | Positivo · PDF hombre 46 años | LDL 142, colesterol total 228, HDL 36 (no-HDL 192), triglicéridos 238 | Activa, coincidencia alta, escalamiento 1 |
| COND-M1-CA-001#02 | Positivo moderado · PDF mujer 34 años | LDL 136, colesterol total 214, HDL 58 (no-HDL 156) | Activa, coincidencia moderada, escalamiento 1 |
| COND-M1-CA-001#03 | Negativo | LDL 110, colesterol total 185, HDL 50 (no-HDL 135) | No activa |
| COND-M1-CA-001#04 | Vigilar | LDL 120, no-HDL 150, HDL 35 (hombre), triglicéridos 210 | No activa como condición; se muestra como "vigilar" |
| COND-M1-CA-002#01 | Positivo alto | LDL 205, padre con infarto a los 50 años | Activa, coincidencia alta, escalamiento 2; desplaza a CA-001 |
| COND-M1-CA-002#02 | Positivo moderado | LDL 196, sin dato de antecedente | Activa, coincidencia moderada, escalamiento 2 |
| COND-M1-CA-002#03 | Negativo | LDL 175 | No activa (CA-001 sí puede activarse) |
| COND-M1-CA-002#04 | Con confusor | LDL 198, TSH 9,5 | Activa; la vista médica muestra hipotiroidismo como posible causa secundaria |
| COND-M1-CA-003#01 | Positivo · PDF hombre 46 años | Triglicéridos 238, ayuno 11 h | Activa, coincidencia alta, escalamiento 1 |
| COND-M1-CA-003#02 | Muy alto | Triglicéridos 620, ayuno 10 h | Activa, escalamiento 2 |
| COND-M1-CA-003#03 | Severo | Triglicéridos 1.150 | Activa, escalamiento 2, frase de triglicéridos severos |
| COND-M1-CA-003#04 | Sin ayuno | Triglicéridos 260, ayuno 4 h | No interpretable; no activa |
| COND-M1-CA-003#05 | Negativo · PDF mujer 34 años | Triglicéridos 98 | No activa |
| COND-M1-CA-004#01 | Positivo · PDF mujer 34 años | Lp(a) 64 mg/dL | Activa, coincidencia alta, escalamiento 1 |
| COND-M1-CA-004#02 | Negativo · PDF hombre 46 años | Lp(a) 18 mg/dL | No activa |
| COND-M1-CA-004#03 | Unidad nmol/L | Lp(a) 140 nmol/L | Activa; la vista médica menciona también el corte ACC/AHA |
| COND-M1-CA-004#04 | Sin unidad | Lp(a) 70, unidad vacía | No interpretable; no activa |
| COND-M1-CA-005#01 | Incompleto · PDF hombre 46 años sin datos de la enfermera | Edad 46, colesterol 228, HDL 36; falta presión y tabaquismo | No se calcula; se listan los factores y lo que falta |
| COND-M1-CA-005#02 | Bajo · PDF hombre 46 años con datos de la enfermera | Presión 128, no fumador, colesterol 228, HDL 36 | 2,2 %, bajo a moderado; no activa |
| COND-M1-CA-005#03 | Fuera de edad · PDF mujer 34 años | Edad 34 | No se calcula; se muestran factores sin porcentaje |
| COND-M1-CA-005#04 | Con diabetes | Edad 58, HbA1c 7,1 | No se calcula; la vista médica lo explica |
| COND-M1-CA-005#05 | Muy alto | Hombre 62 años, presión 152, fumador, colesterol 245, HDL 38 | 13,1 % (21,5 % antes de recalibrar), muy alto, escalamiento 2 |
| COND-M1-CA-006#01 | Positivo grado 1 | Promedio 134/84, sin automonitoreo | Activa, coincidencia moderada, escalamiento 1; activa aldosterona y renina |
| COND-M1-CA-006#02 | Positivo grado 2 con confirmación | Promedio 146/92; Apple Health con promedio de 7 días 141/89 | Activa, coincidencia alta, escalamiento 2 |
| COND-M1-CA-006#03 | Severa | Promedio 184/112 | Activa, escalamiento 3, llamada el mismo día |
| COND-M1-CA-006#04 | Negativo | Promedio 118/76 | No activa |
| COND-M1-CA-006#05 | Hipertensión conocida | Promedio 138/86, toma antihipertensivo | No activa como detección; la vista médica muestra control |
| COND-M1-CA-007#01 | Positivo | HbA1c 7,2, glucosa 148, NT-proBNP 210 | Activa, coincidencia alta, escalamiento 2 |
| COND-M1-CA-007#02 | Con confusor | Diabetes conocida, NT-proBNP 180, TFG 48 | Activa, coincidencia moderada |
| COND-M1-CA-007#03 | Negativo | Diabetes conocida, NT-proBNP 60 | No activa |
| COND-M1-CA-007#04 | Sin diabetes | Sin diabetes; la prueba no se pidió | No aplica |
| COND-M1-CA-A01#01 | Positivo | ApoB 138, LDL 118, triglicéridos 240 | Activa como apoyo destacado |
| COND-M1-CA-A01#02 | Negativo · PDF hombre 46 años | ApoB 118, LDL 142 | No activa (no hay discordancia: ambos altos) |
| COND-M1-CA-A01#03 | Negativo | ApoB 95, LDL 110 | No activa |
| COND-M1-CA-A02#01 | Positivo · PDF hombre 46 años | hs-CRP 3,4, sin infección declarada | Activa como apoyo, a confirmar |
| COND-M1-CA-A02#02 | Con confusor | hs-CRP 4,1, infección respiratoria hace 1 semana | No activa; se sugiere repetir |
| COND-M1-CA-A02#03 | Proceso agudo | hs-CRP 18 | No activa; se sugiere repetir |
| COND-M1-CA-A02#04 | Negativo · PDF mujer 34 años | hs-CRP 0,8 | No activa |
| COND-M1-EM-001#01 | Positivo · PDF hombre 46 años | Glucosa 112, HbA1c 6,0, ayuno 11 h | Activa, coincidencia alta, escalamiento 1; HOMA-IR 5,5 como apoyo |
| COND-M1-EM-001#02 | Positivo moderado | Glucosa 94, HbA1c 5,9 | Activa, coincidencia moderada |
| COND-M1-EM-001#03 | Negativo · PDF mujer 34 años | Glucosa 86, HbA1c 5,2 | No activa |
| COND-M1-EM-001#04 | Con anemia | Glucosa 92, HbA1c 5,8, hemoglobina 10,9 | Activa con coincidencia baja ("vigilar"): la HbA1c pierde confianza con anemia |
| COND-M1-EM-001#05 | Diabetes | Glucosa 131, HbA1c 6,7 | No activa (manda EM-002) |
| COND-M1-EM-002#01 | Positivo alto | Glucosa 138, HbA1c 6,9 | Activa, coincidencia alta, escalamiento 2; activa NT-proBNP |
| COND-M1-EM-002#02 | Positivo moderado | Glucosa 128, HbA1c 6,1 | Activa, coincidencia moderada, frase de repetir |
| COND-M1-EM-002#03 | Negativo · PDF hombre 46 años | Glucosa 112, HbA1c 6,0 | No activa (manda EM-001) |
| COND-M1-EM-002#04 | Diabetes conocida | Glucosa 150, HbA1c 7,4, metformina | No activa como detección; vista médica de control |
| COND-M1-EM-003#01 | Positivo moderado · PDF hombre 46 años sin datos de la enfermera | Triglicéridos 238, HDL 36, glucosa 112; falta cintura y presión | Activa con 3 de 5, coincidencia moderada; dice que faltan cintura y presión |
| COND-M1-EM-003#02 | Positivo alto | Lo anterior más cintura 98 cm y presión 128/82 | Activa con 4 de 5, coincidencia alta |
| COND-M1-EM-003#03 | Incompleto | Triglicéridos 170, HDL 52 (hombre), glucosa 92; falta cintura y presión | No activa; se marca incompleto |
| COND-M1-EM-003#04 | Negativo · PDF mujer 34 años | Triglicéridos 98, HDL 58, glucosa 86; cintura 74, presión 112/70 | No activa |
| COND-M1-EM-004#01 | Obesidad | Peso 92 kg, talla 1,75 m (IMC 30,0), cintura 104 cm, hombre | Activa como obesidad con adiposidad central, escalamiento 1 |
| COND-M1-EM-004#02 | Sobrepeso | Peso 70 kg, talla 1,62 m (IMC 26,7) | Activa como sobrepeso, escalamiento 1 |
| COND-M1-EM-004#03 | Clase 3 | Peso 118 kg, talla 1,68 m (IMC 41,8) | Activa, escalamiento 2 |
| COND-M1-EM-004#04 | Negativo | Peso 63 kg, talla 1,68 m (IMC 22,3) | No activa |
| COND-M1-EM-004#05 | Sin medida | Peso o talla faltante | No interpretable |
| COND-M1-EM-005#01 | Alerta | Glucosa 64, tubo con fluoruro, procesada a tiempo | Activa, coincidencia alta, escalamiento 1 |
| COND-M1-EM-005#02 | Significativa confiable | Glucosa 50, tubo con fluoruro, a tiempo | Activa, escalamiento 3 |
| COND-M1-EM-005#03 | Significativa dudosa | Glucosa 50, demora de 7 horas sin fluoruro | Activa, coincidencia moderada, escalamiento 2, pide repetir |
| COND-M1-EM-005#04 | Con medicamento | Glucosa 66, usa glibenclamida | Activa, escalamiento 2 |
| COND-M1-EM-005#05 | Negativo | Glucosa 86 | No activa |
| COND-M1-EM-A01#01 | Refuerza | FINDRISC 15, glucosa 108 | Refuerza EM-001 |
| COND-M1-EM-A01#02 | Vigilar | FINDRISC 13, glucosa 88, HbA1c 5,4 | Se muestra como vigilar |
| COND-M1-EM-A01#03 | Negativo | FINDRISC 7 | No activa |
| COND-M1-EM-A02#01 | Refuerza · PDF hombre 46 años | Glucosa 112, insulina 19,8 (HOMA-IR 5,5) | Refuerza EM-001 y EM-003 |
| COND-M1-EM-A02#02 | Vigilar | Glucosa 90, insulina 14 (HOMA-IR 3,1), sin condiciones activas | Vigilar en la vista médica |
| COND-M1-EM-A02#03 | Negativo · PDF mujer 34 años | Glucosa 86, insulina 6,1 (HOMA-IR 1,3) | No activa |
| COND-M1-EM-A02#04 | No calculable | Usa insulina | No se calcula |

### M2

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| COND-M2-NE-001#01 | Sospecha G3a | TFG 52, albúmina/creatinina 12 | Activa, coincidencia moderada, G3a A1, escalamiento 1; activa cistatina C refleja |
| COND-M2-NE-001#02 | Sospecha G3b | TFG 38, albúmina/creatinina 80 | Activa, G3b A2, escalamiento 2 |
| COND-M2-NE-001#03 | Avanzada | TFG 22 | Activa, G4, escalamiento 3 |
| COND-M2-NE-001#04 | No confirmada | TFG 55 sin albuminuria; TFG combinada con cistatina 68 | Coincidencia baja ("vigilar") |
| COND-M2-NE-001#05 | Negativo · PDF hombre 46 años | TFG 96, albúmina/creatinina 45 (una toma) | No activa (pasa a NE-002) |
| COND-M2-NE-001#06 | Negativo · PDF mujer 34 años | TFG 112, albúmina/creatinina 8 | No activa |
| COND-M2-NE-002#01 | Positivo · PDF hombre 46 años | Albúmina/creatinina 45, TFG 96, una toma | Activa, coincidencia moderada, A2, escalamiento 1 |
| COND-M2-NE-002#02 | A3 | Albúmina/creatinina 420, TFG 88 | Activa, escalamiento 2 |
| COND-M2-NE-002#03 | Con confusor | Albúmina/creatinina 60, ejercicio intenso el día anterior | Activa con coincidencia baja; sugiere repetir |
| COND-M2-NE-002#04 | Negativo · PDF mujer 34 años | Albúmina/creatinina 8 | No activa |
| COND-M2-NE-003#01 | Positivo | Diabetes conocida, albúmina/creatinina 85, TFG 74 | Activa, coincidencia moderada, A2, escalamiento 2; NE-002 no aparece en el informe del paciente |
| COND-M2-NE-003#02 | Hipertensión conocida | Toma antihipertensivo, TFG 54, albúmina/creatinina 20 | Activa, G3a, escalamiento 2 |
| COND-M2-NE-003#03 | Vigilar · PDF hombre 46 años con presión 134/84 sin automonitoreo | Albúmina/creatinina 45, CA-006 moderada | No activa; NE-002 sigue; vista médica marca vigilar |
| COND-M2-NE-003#04 | Negativo | Sin diabetes ni hipertensión, albúmina/creatinina 45 | No activa (manda NE-002) |
| COND-M2-NE-004#01 | No interpretable · PDF mujer 34 años | Potasio "No procesado", muestra hemolizada | No interpretable; pide nueva muestra; no activa |
| COND-M2-NE-004#02 | Leve | Potasio 5,3, centrifugado a tiempo | Activa, coincidencia moderada, escalamiento 1; repetir |
| COND-M2-NE-004#03 | Accionable | Potasio 5,8, sin hemólisis, TFG 48, toma losartán | Activa, coincidencia alta, escalamiento 2 |
| COND-M2-NE-004#04 | Crítico | Potasio 6,6 con bandera crítica del laboratorio | Escalamiento 3 |
| COND-M2-NE-004#05 | Negativo · PDF hombre 46 años | Potasio 4,3 | No activa |
| COND-M2-NE-005#01 | Leve | Sodio 132, glucosa 95 | Activa, escalamiento 1 |
| COND-M2-NE-005#02 | Moderado con tiazida | Sodio 127, toma hidroclorotiazida | Activa, escalamiento 2 |
| COND-M2-NE-005#03 | Profundo | Sodio 121 | Activa, escalamiento 3 |
| COND-M2-NE-005#04 | Corregido | Sodio 131, glucosa 420 (corregido 136,1) | No activa |
| COND-M2-NE-005#05 | Pseudohiponatremia | Sodio 129, triglicéridos 1.400, ISE indirecto | No interpretable |
| COND-M2-NE-005#06 | Negativo · PDF ejemplos | Sodio 140 y 138 | No activa |
| COND-M2-NE-006#01 | Bajo riesgo | 6 hematíes por campo, sin albuminuria | Activa, escalamiento 1 |
| COND-M2-NE-006#02 | Glomerular | 10 hematíes por campo, albúmina/creatinina 140 | Activa, escalamiento 2 |
| COND-M2-NE-006#03 | Menstruación | 15 hematíes por campo, menstruación actual | No interpretable |
| COND-M2-NE-006#04 | Solo tira | Tira con sangre positiva, sedimento 0 a 2 | No activa |
| COND-M2-NE-006#05 | Negativo · PDF ejemplos | Sedimento 0 a 2 por campo | No activa |
| COND-M2-NE-A01#01 | Refuerza | Potasio 3,3, presión 146/92 | Refuerza TI-008 y CA-006 |
| COND-M2-NE-A01#02 | Muy bajo | Potasio 2,8 | Resultado observado, escalamiento 2 |
| COND-M2-NE-A01#03 | Con diurético | Potasio 3,4, toma hidroclorotiazida | Refuerza con nota de diurético |
| COND-M2-NE-A01#04 | Negativo | Potasio 4,3 | No activa |
| COND-M2-NE-A02#01 | No confirma | TFG creatinina 54, albúmina/creatinina 10, TFG combinada 66 | NE-001 baja a vigilar |
| COND-M2-NE-A02#02 | Confirma | TFG creatinina 52, TFG combinada 49 | NE-001 se mantiene con G3a |
| COND-M2-NE-A02#03 | Masa muscular | Objetivo "aumentar mi masa muscular", creatinina 1,35, TFG 68 | Se pide cistatina C; se usa la combinada |
| COND-M2-NE-A02#04 | No aplica | TFG 96 | No se pide |
| COND-M2-NE-A03#01 | Positivo | Bicarbonato 19, NE-001 activa (G3b) | Activa como apoyo |
| COND-M2-NE-A03#02 | Sin ERC | Bicarbonato 20, TFG 95 | No activa; valor fuera de rango |
| COND-M2-NE-A03#03 | Negativo · PDF ejemplos | Bicarbonato 25 y 24 | No activa |
| COND-M2-TI-001#01 | Positivo · PDF mujer 34 años | TSH 6,90, T4 libre 1,02 (0,93 a 1,70), anti-TPO 186 | Activa, coincidencia alta, escalamiento 1; refuerzo autoinmune por TI-A01; frase para mujer en edad fértil |
| COND-M2-TI-001#02 | TSH 10 o más | TSH 11,4, T4 libre normal | Activa, escalamiento 2 |
| COND-M2-TI-001#03 | Vigilar | TSH 4,6 (laboratorio hasta 4,2), edad 40 | Coincidencia baja (vigilar) |
| COND-M2-TI-001#04 | Mayor de 60 | TSH 5,6, edad 68 | No activa (corte 6,0) |
| COND-M2-TI-001#05 | Biotina | TSH 7,2, suplemento de biotina | Bloqueada; pide repetir sin biotina |
| COND-M2-TI-001#06 | Negativo · PDF hombre 46 años | TSH 2,10 | No activa |
| COND-M2-TI-002#01 | Positivo | TSH 14,2, T4 libre 0,71 | Activa, coincidencia alta, escalamiento 2; desplaza a TI-001 |
| COND-M2-TI-002#02 | Con amiodarona | TSH 9,8, T4 libre 0,85, amiodarona | Activa, coincidencia moderada |
| COND-M2-TI-002#03 | Negativo · PDF mujer 34 años | TSH 6,90, T4 libre 1,02 | No activa (es TI-001) |
| COND-M2-TI-003#01 | Positivo | T4 libre 0,68, TSH 1,4 | Activa, escalamiento 2 |
| COND-M2-TI-003#02 | Con corticoides | T4 libre 0,80, TSH 0,9, prednisona | Activa, coincidencia moderada |
| COND-M2-TI-003#03 | Negativo | T4 libre 1,20, TSH 1,8 | No activa |
| COND-M2-TI-004#01 | Leve | TSH 0,18, T4 libre y T3 libre normales | Activa, escalamiento 1 |
| COND-M2-TI-004#02 | Suprimida | TSH 0,05, T4 libre y T3 libre normales | Activa, escalamiento 2 |
| COND-M2-TI-004#03 | Biotina | TSH 0,08, biotina en el cuestionario | Bloqueada; pide repetir sin biotina |
| COND-M2-TI-004#04 | Negativo · PDF ejemplos | TSH 2,10 | No activa |
| COND-M2-TI-005#01 | Manifiesto | TSH \< 0,01, T4 libre 2,9 | Activa, escalamiento 2 |
| COND-M2-TI-005#02 | T3-toxicosis | TSH 0,02, T4 libre 1,5 (normal), T3 libre 6,1 (alta) | Activa, variante T3-toxicosis |
| COND-M2-TI-005#03 | Con levotiroxina | TSH 0,03, T4 libre 2,1, toma levotiroxina | Bloqueada; vista médica: posible sobredosificación |
| COND-M2-TI-005#04 | Negativo | TSH 1,8 | No activa |
| COND-M2-TI-006#01 | Positivo | Embarazo de 10 semanas, TSH 4,8 | Activa, coincidencia alta, escalamiento 2 |
| COND-M2-TI-006#02 | Con T4 libre baja | Embarazo de 22 semanas, TSH 6,5, T4 libre baja | Activa; vista médica destaca la T4 libre baja |
| COND-M2-TI-006#03 | TSH baja | Embarazo de 9 semanas, TSH 0,2 | No activa; resultado observado para el médico |
| COND-M2-TI-006#04 | No embarazada | TSH 4,8 | No aplica (va por TI-001) |
| COND-M2-TI-007#01 | Positivo | Calcio 10,9, albúmina 4,2 (corregido 10,7), PTH 78 (15 a 65) | Activa, coincidencia moderada, escalamiento 2 |
| COND-M2-TI-007#02 | Muy alto | Calcio corregido 12,4, PTH 140 | Activa, escalamiento 3 |
| COND-M2-TI-007#03 | Corregido normal | Calcio 10,4, albúmina 4,9 (corregido 9,7) | No activa; no se pide PTH |
| COND-M2-TI-007#04 | PTH suprimida | Calcio corregido 11,0, PTH 8 | No activa; vista médica: buscar otra causa de calcio alto |
| COND-M2-TI-007#05 | Negativo · PDF ejemplos | Calcio 9,5 y 9,2 | No activa |
| COND-M2-TI-008#01 | Positivo | Presión 148/94; aldosterona 18 ng/dL (inmunoensayo); ARP 0,4 ng/mL/h (relación 45); potasio 3,3 | Activa, coincidencia alta, escalamiento 2; refuerzo por NE-A01 |
| COND-M2-TI-008#02 | Con betabloqueador | Aldosterona 12 ng/dL; ARP 0,5 (relación 24); toma metoprolol | Activa, coincidencia moderada; repetir tras retirar el betabloqueador si el médico lo considera seguro |
| COND-M2-TI-008#03 | Zona para repetir | Aldosterona 7 ng/dL; ARP 0,3 | No activa; repetir otro día |
| COND-M2-TI-008#04 | Negativo | Presión 136/86; aldosterona 9 ng/dL; ARP 2,1 (relación 4,3) | No activa |
| COND-M2-TI-008#05 | Unidades de concentración | Aldosterona 450 pmol/L; DRC 4 mU/L (relación 112) | Activa |
| COND-M2-TI-008#06 | Sin presión elevada · PDF ejemplos sin datos de la enfermera | Aldosterona y renina no se pidieron | No aplica |
| COND-M2-TI-A01#01 | Positivo · PDF mujer 34 años | Anti-TPO 186 (menor de 34), con TSH 6,90 | Refuerza TI-001; se marca relación vigilar con ferritina baja |
| COND-M2-TI-A01#02 | Anti-Tg | Anti-TPO negativo, anti-Tg 210 (menor de 115), TSH 7,0 | Refuerza TI-001 |
| COND-M2-TI-A01#03 | Negativo | Anti-TPO 12 | No activa |

### M3

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| COND-M3-HE-001#01 | Positivo · PDF mujer 34 años | Hemoglobina 11,2; ajustada 9,4; no fuma | Activa, anemia moderada, coincidencia alta, escalamiento 2 |
| COND-M3-HE-001#02 | Positivo oculto por la altura | Mujer, hemoglobina 13,1; ajustada 11,3 | Activa como leve, escalamiento 1 (sin ajuste habría salido normal) |
| COND-M3-HE-001#03 | Negativo · PDF hombre 46 años | Hemoglobina 16,2; ajustada 14,4 | No activa |
| COND-M3-HE-001#04 | Severa | Hombre, hemoglobina 9,4; ajustada 7,6 | Activa, severa, escalamiento 3 |
| COND-M3-HE-001#05 | Embarazo | 2.º trimestre, hemoglobina 12,0; ajustada 10,2 | Activa (corte 10,5) |
| COND-M3-HE-002#01 | Positivo · PDF mujer 34 años | HE-001 activa; ferritina 7, hs-CRP 0,8, saturación 8,8 %, VCM 78,2, RDW 16,4 | Activa, coincidencia alta, escalamiento 2; IgA y anti-tTG reflejas (negativas: sin señal de celiaquía) |
| COND-M3-HE-002#02 | Con inflamación | Anemia, ferritina 45, hs-CRP 12, saturación 12 % | Activa (corte 70), coincidencia alta |
| COND-M3-HE-002#03 | Hombre | Hombre 55 años, anemia, ferritina 9 | Activa, escalamiento 2; la vista médica destaca descartar pérdida digestiva |
| COND-M3-HE-002#04 | Sin anemia | Hemoglobina ajustada normal, ferritina 9 | No activa (va a HE-003) |
| COND-M3-HE-003#01 | Positivo | Mujer 28 años, hemoglobina ajustada 12,6, ferritina 11 | Activa, escalamiento 1 |
| COND-M3-HE-003#02 | Hombre | Hombre 50 años, hemoglobina ajustada 13,8, ferritina 12 | Activa, escalamiento 2 |
| COND-M3-HE-003#03 | Vigilar | Mujer, ferritina 22, hs-CRP 1 | Coincidencia baja (vigilar) |
| COND-M3-HE-003#04 | Con anemia · PDF mujer 34 años | Ferritina 7 con anemia | No activa (manda HE-002) |
| COND-M3-HE-003#05 | Negativo · PDF hombre 46 años | Ferritina 310 | No activa |
| COND-M3-HE-004#01 | B12 | Anemia, VCM 108, B12 140 | Activa, coincidencia alta, escalamiento 2 |
| COND-M3-HE-004#02 | Indeterminada | Anemia, VCM 104, B12 260, ácido metilmalónico alto | Activa |
| COND-M3-HE-004#03 | Folato | Anemia, VCM 103, folato 2,8 | Activa |
| COND-M3-HE-004#04 | Negativo · PDF mujer 34 años | Anemia con VCM 78,2; B12 262 con ácido metilmalónico normal | No activa |
| COND-M3-HE-005#01 | Positivo | Plaquetas 82 | Activa, escalamiento 2; repetir |
| COND-M3-HE-005#02 | Leve | Plaquetas 128 (laboratorio 150 a 450) | Valor fuera de rango, escalamiento 1 |
| COND-M3-HE-005#03 | Seudotrombocitopenia | Plaquetas 64 con comentario de agregados | No interpretable; repetir con citrato |
| COND-M3-HE-005#04 | Crítico | Plaquetas 14 con bandera crítica | Escalamiento 3 |
| COND-M3-HE-005#05 | Negativo · PDF ejemplos | Plaquetas 265 y 330 | No activa |
| COND-M3-HE-006#01 | Positivo | Hombre, saturación 62 %, ferritina 640, hs-CRP 1 | Activa, coincidencia alta, escalamiento 2 |
| COND-M3-HE-006#02 | Vigilar · PDF hombre 46 años | Ferritina 310, saturación 37 %, patrón hepático metabólico | Coincidencia baja (vigilar); la vista médica liga la ferritina al patrón hepático |
| COND-M3-HE-006#03 | Mujer | Mujer 32 años, saturación 51 %, ferritina 260 | Activa |
| COND-M3-HE-006#04 | Negativo · PDF mujer 34 años | Ferritina 7 | No activa |
| COND-M3-HE-A01#01 | Positivo | Anemia, ferritina 180, saturación 14 %, hs-CRP 22 | Activa; HE-001 con escalamiento 2 y sin recomendaciones de hierro |
| COND-M3-HE-A01#02 | Negativo · PDF mujer 34 años | Anemia, ferritina 7, hs-CRP 0,8 | No activa (manda HE-002) |
| COND-M3-HE-A02#01 | Leve | Neutrófilos 1,6 (laboratorio desde 1,8) | Valor fuera de rango, escalamiento 1 |
| COND-M3-HE-A02#02 | Varias líneas | Leucocitos 2,9, plaquetas 95, anemia | Escalamiento 2 |
| COND-M3-HE-A02#03 | Negativo · PDF ejemplos | Leucocitos 7,8 y 6,1 | No activa |
| COND-M3-HE-A03#01 | Positivo | Leucocitos 8,0, eosinófilos 9 % (0,72) | Activa, escalamiento 1 |
| COND-M3-HE-A03#02 | Con parásitos | Lo anterior y coprológico con parásitos | Refuerza parasitosis (M4) |
| COND-M3-HE-A03#03 | Negativo · PDF hombre 46 años | Leucocitos 7,8, eosinófilos 3,2 % (0,25) | No activa |
| COND-M3-NU-001#01 | Positivo | B12 150, toma metformina | Activa, coincidencia alta, escalamiento 1 |
| COND-M3-NU-001#02 | Funcional | B12 240, ácido metilmalónico alto | Activa, coincidencia alta |
| COND-M3-NU-001#03 | Negativo · PDF mujer 34 años | B12 262, ácido metilmalónico 0,28 (normal) | No activa |
| COND-M3-NU-001#04 | Negativo · PDF hombre 46 años | B12 410 | No activa |
| COND-M3-NU-001#05 | Anticonceptivo | B12 165, anticonceptivo oral, sin factor de riesgo | Activa, coincidencia moderada |
| COND-M3-NU-002#01 | Positivo | Folato 2,6 | Activa, coincidencia alta, escalamiento 1 |
| COND-M3-NU-002#02 | Posible | Folato 3,6 | Activa, coincidencia moderada |
| COND-M3-NU-002#03 | Embarazo | Folato 3,2, embarazo de 8 semanas | Activa, escalamiento 2 |
| COND-M3-NU-002#04 | Negativo · PDF ejemplos | Folato 9,8 y 6,2 | No activa |
| COND-M3-NU-A01#01 | Refuerza | B12 220, homocisteína 19 | NU-001 sube a coincidencia alta |
| COND-M3-NU-A01#02 | Vigilar | Homocisteína 17, B12 y folato normales, TFG 58 | Vigilar; vista médica menciona TFG |
| COND-M3-NU-A01#03 | Negativo · PDF ejemplos | Homocisteína 11,8 y 13,9 | No activa |
| COND-M3-NU-A02#01 | Secundaria | PTH 88, calcio corregido 9,4, vitamina D 14 | Vigilar; causa probable: vitamina D baja |
| COND-M3-NU-A02#02 | Sin causa | PTH 82, calcio 9,8, vitamina D 34, TFG 95 | Resultado observado para el médico, escalamiento 1 |
| COND-M3-NU-A02#03 | No aplica · PDF ejemplos | PTH no medida (calcio normal) | No aplica |
| COND-M3-NU-A03#01 | Baja · PDF hombre 46 años | Vitamina D 21,4 (laboratorio 30 a 100) | Marcada baja, escalamiento 0, recomendación alimentaria |
| COND-M3-NU-A03#02 | Baja · PDF mujer 34 años | Vitamina D 17,8 | Marcada baja; relación vigilar con ferritina y hemoglobina bajas |
| COND-M3-NU-A03#03 | Alta | Vitamina D 140 | Marcada alta, escalamiento 1 |
| COND-M3-NU-A03#04 | En rango | Vitamina D 42 | Sin recomendación específica |
| COND-M3-NU-A04#01 | Sin intervalo · PDF ejemplos | Biotina, niacina, índice omega-3, omega-6/omega-3 y CoQ10 con "No establecido" | Solo valor, sin clase |
| COND-M3-NU-A04#02 | No apta · PDF mujer 34 años | Vitamina C "Muestra no apta" | No interpretable |
| COND-M3-NU-A04#03 | En rango · PDF hombre 46 años | B1, B6, A, E, K1, C en rango | Sin recomendación específica |
| COND-M3-NU-A04#04 | Biotina declarada | Suplemento de biotina para el cabello, TSH 0,08 | Bloquea tiroides y B12; pide repetir sin el suplemento |
| COND-M3-NU-A04#05 | Vitamina A alta | Vitamina A 112 (30 a 80) | Marcada alta, escalamiento 1 |
| COND-M3-NU-A04#06 | Tiamina con síntomas | B1 45, alcohol diario, confusión reciente | Escalamiento 3 |

### M4

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| COND-M4-GA-001#01 | Bajo · PDF hombre 46 años | Edad 46, AST 39, ALT 58, plaquetas 265 (FIB-4 0,89) | No activa; la vista médica muestra FIB-4 bajo |
| COND-M4-GA-001#02 | Indeterminado | Edad 58, AST 48, ALT 52, plaquetas 190, diabetes (FIB-4 2,03) | Activa, coincidencia moderada, escalamiento 1 |
| COND-M4-GA-001#03 | Alto | Edad 62, AST 70, ALT 45, plaquetas 140 (FIB-4 4,62) | Activa, escalamiento 2 |
| COND-M4-GA-001#04 | Mayor de 65 | Edad 70, FIB-4 1,1, diabetes | No activa; vista médica: no concluyente |
| COND-M4-GA-001#05 | No aplica · PDF mujer 34 años | Sin factores metabólicos, enzimas normales | No se calcula |
| COND-M4-GA-002#01 | Positivo · PDF hombre 46 años | ALT 58 (laboratorio hasta 50), AST 39, CK normal | Activa, coincidencia moderada, escalamiento 1; ligada a la relación hepática metabólica |
| COND-M4-GA-002#02 | Limítrofe | Mujer, ALT 31 (laboratorio hasta 35) | Vigilar |
| COND-M4-GA-002#03 | Muy alta | ALT 190 (laboratorio hasta 50) | Activa, escalamiento 2 |
| COND-M4-GA-002#04 | Muscular | ALT 48, AST 85, CK 2.400, ejercicio el día anterior | No activa; patrón muscular |
| COND-M4-GA-002#05 | Negativo · PDF mujer 34 años | ALT 18 | No activa |
| COND-M4-GA-003#01 | Positivo | ALP 260 (hasta 129), GGT 180, ALT 40 (R 0,4) | Activa, escalamiento 2 (más del doble) |
| COND-M4-GA-003#02 | Leve | ALP 160, GGT 95, ALT 35 | Activa, escalamiento 1 |
| COND-M4-GA-003#03 | Óseo | ALP 170, GGT 30 | Vigilar; origen óseo probable |
| COND-M4-GA-003#04 | Negativo · PDF hombre 46 años | ALP 88, GGT 72 (hasta 71) | No activa (falta ALP alta) |
| COND-M4-GA-004#01 | Positivo en edad | Edad 58, FIT positivo | Activa, escalamiento 2 |
| COND-M4-GA-004#02 | Positivo joven | Edad 34, FIT positivo | Activa, escalamiento 2; la vista médica anota que está fuera de la franja formal |
| COND-M4-GA-004#03 | Con anemia | FIT positivo y anemia por déficit de hierro (M3) | Activa; la vista médica los cruza |
| COND-M4-GA-004#04 | Negativo · PDF ejemplos | FIT negativo | No activa |
| COND-M4-GA-005#01 | Positivo · PDF hombre 46 años | Antígeno positivo | Activa, escalamiento 2; el informe incluye la limitación del método |
| COND-M4-GA-005#02 | Negativo con omeprazol | Antígeno negativo, omeprazol diario | No activa; vista médica: negativo no concluyente |
| COND-M4-GA-005#03 | Negativo · PDF mujer 34 años | Antígeno negativo, sin medicamentos | No activa |
| COND-M4-GA-006#01 | Positivo | Déficit de hierro, anti-tTG 48 (menor de 7), IgA normal, come gluten | Activa, coincidencia alta, escalamiento 2 |
| COND-M4-GA-006#02 | Déficit de IgA | Anti-tTG 2, IgA 5 (bajo) | No interpretable; sugiere pruebas basadas en IgG |
| COND-M4-GA-006#03 | Negativo · PDF mujer 34 años | Anti-tTG 2,1, IgA 210 | No activa: sin señal de celiaquía |
| COND-M4-GA-006#04 | Sin gluten | Anti-tTG 3, dieta sin gluten | No interpretable |
| COND-M4-GA-A01#01 | Aislada | Bilirrubina total 1,9, directa 0,3, resto normal, hemoglobina normal | Resultado observado, escalamiento 0 |
| COND-M4-GA-A01#02 | Con hemólisis | Bilirrubina total 2,4, directa 0,3, anemia, reticulocitos altos, LDH alta | Activa relación hemólisis, escalamiento 2 |
| COND-M4-GA-A01#03 | Negativo · PDF ejemplos | Bilirrubina total 0,80 y 0,50 | No activa |
| COND-M4-GA-A02#01 | Positivo | Alcohol diario, AST 92, ALT 40, GGT 210 | Activa; destaca AST/ALT de 2,3 |
| COND-M4-GA-A02#02 | Solo GGT | Alcohol los fines de semana, GGT 88 | Activa |
| COND-M4-GA-A02#03 | Sin alcohol · PDF hombre 46 años | Sin dato de alcohol (lo pregunta la enfermera), GGT 72 | No activa hasta tener el dato |
| COND-M4-IN-001#01 | Activa | Anti-VHC reactivo, ARN detectable | Activa, coincidencia alta, escalamiento 2, llamada |
| COND-M4-IN-001#02 | Resuelta | Anti-VHC reactivo, ARN no detectable | Activa, coincidencia baja, llamada con texto de resuelta |
| COND-M4-IN-001#03 | Pendiente | Anti-VHC reactivo, ARN en proceso | Informe en espera; llamada cuando llegue el ARN |
| COND-M4-IN-001#04 | Negativo · PDF ejemplos | Anti-VHC no reactivo | No activa |
| COND-M4-IN-002#01 | Susceptible · PDF hombre 46 años | HBsAg no reactivo, anti-HBc no reactivo, anti-HBs 4,2 | Estado susceptible, escalamiento 1, recomendación de vacuna |
| COND-M4-IN-002#02 | Inmune · PDF mujer 34 años | HBsAg y anti-HBc no reactivos, anti-HBs 85 | Inmune por vacuna, escalamiento 0 |
| COND-M4-IN-002#03 | Activa | HBsAg reactivo | Escalamiento 2, llamada |
| COND-M4-IN-002#04 | Resuelta | HBsAg no reactivo, anti-HBc reactivo, anti-HBs 120 | Escalamiento 1, nota de reactivación |
| COND-M4-IN-002#05 | Anti-HBc aislado | HBsAg no reactivo, anti-HBc reactivo, anti-HBs 3 | Escalamiento 2, llamada |
| COND-M4-IN-003#01 | Positivo | Dos ELISA reactivas, nacido en municipio endémico | Activa, coincidencia alta, escalamiento 2, llamada |
| COND-M4-IN-003#02 | Discordante | ELISA total reactiva, recombinante no reactiva | Informe en espera de tercera prueba |
| COND-M4-IN-003#03 | Negativo · PDF ejemplos | ELISA total no reactiva | No activa; no se corre la segunda |
| COND-M4-IN-A01#01 | Con síntomas | Nitritos positivos, ardor al orinar | Activa, escalamiento 1 |
| COND-M4-IN-A01#02 | Sin síntomas | Esterasa positiva, sin síntomas, no embarazada | No se reporta |
| COND-M4-IN-A01#03 | Embarazo | Nitritos positivos, embarazo de 14 semanas | Vista médica, escalamiento 1 |
| COND-M4-IN-A01#04 | Negativo · PDF ejemplos | Uroanálisis normal | No activa |
| COND-M4-IN-A02#01 | Patógeno | Quistes de Giardia | Activa, escalamiento 1 |
| COND-M4-IN-A02#02 | Con eosinofilia | Huevos de helminto, eosinófilos 0,9 × 10³/µL | Activa, reforzada por HE-A03 |
| COND-M4-IN-A02#03 | Comensal | Quistes de Entamoeba coli | Informativo, escalamiento 0 |
| COND-M4-IN-A02#04 | Negativo · PDF ejemplos | No se observaron parásitos | No activa |

### M5

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| COND-M5-MU-001#01 | Positivo | Mujer 27 años, testosterona 72 ng/dL (hasta 48), SHBG 22, sin anticonceptivo | Activa, coincidencia alta, escalamiento 1 |
| COND-M5-MU-001#02 | Muy alta | Testosterona 140 ng/dL | Activa, escalamiento 2 |
| COND-M5-MU-001#03 | Anticonceptivo | Testosterona 60, toma anticonceptivo oral | No interpretable |
| COND-M5-MU-001#04 | Negativo · PDF mujer 34 años | Testosterona 32, SHBG 62 (índice 1,8), sin anticonceptivo | No activa |
| COND-M5-MU-002#01 | Positivo | Mujer 33 años, FSH 38, sin anticonceptivo | Activa, coincidencia moderada, escalamiento 2 |
| COND-M5-MU-002#02 | Edad 42 | FSH 30 | Sin condición; contexto en la vista médica |
| COND-M5-MU-002#03 | Edad 50 | FSH 60 | No se interpreta |
| COND-M5-MU-002#04 | Anticonceptivo | Mujer 30 años, FSH 2, anticonceptivo oral | No interpretable |
| COND-M5-MU-002#05 | Negativo · PDF mujer 34 años | FSH 6,1 en fase folicular | No activa |
| COND-M5-MU-003#01 | Positivo | Prolactina 41 (hasta 23,3), macroprolactina no predominante | Activa, coincidencia moderada, escalamiento 1 |
| COND-M5-MU-003#02 | Macroprolactina | Prolactina 38, macroprolactina predominante | Escalamiento 0, frase de macroprolactina |
| COND-M5-MU-003#03 | Muy alta | Prolactina 160 | Activa, escalamiento 2 |
| COND-M5-MU-003#04 | Con medicamento | Prolactina 35, toma risperidona | Coincidencia baja |
| COND-M5-MU-003#05 | Embarazo | Prolactina 120, embarazo de 20 semanas | No interpretable |
| COND-M5-MU-003#06 | Negativo · PDF mujer 34 años | Prolactina 14,2 | No activa |
| COND-M5-MU-A01#01 | Positivo | Embarazo de 26 semanas, hemoglobina 12,0 (ajustada 10,2) | Activa, escalamiento 2, ruta prenatal |
| COND-M5-MU-A01#02 | Negativo | Embarazo de 12 semanas, hemoglobina 13,5 (ajustada 11,7) | No activa |
| COND-M5-MU-A01#03 | No aplica · PDF mujer 34 años | No embarazada | No aplica (va por HE-001) |
| COND-M5-UR-001#01 | Tamizaje | Hombre 58 años, PSA 5,6, con consentimiento | Activa, escalamiento 2; PSA libre refleja |
| COND-M5-UR-001#02 | Fuera de edad | Hombre 44 años, PSA 4,8 | Activa, escalamiento 1 |
| COND-M5-UR-001#03 | Muy alto | Hombre 66 años, PSA 14 | Activa, escalamiento 2 |
| COND-M5-UR-001#04 | Finasterida | PSA 2,6 con finasterida (equivale a 5,2) | Activa |
| COND-M5-UR-001#05 | Sin consentimiento | Sin consentimiento de PSA | No medido |
| COND-M5-UR-001#06 | Negativo · PDF hombre 46 años | PSA 1,10 | No activa |
| COND-M5-UR-002#01 | Positivo | Hombre 52 años, testosterona 228 a las 7:30, método certificado, libre baja | Activa, coincidencia alta, escalamiento 1 |
| COND-M5-UR-002#02 | No certificado | Testosterona 230, método sin certificación declarada | Resultado observado, sin etiqueta |
| COND-M5-UR-002#03 | Muy baja | Testosterona 120, certificado | Activa, escalamiento 2 |
| COND-M5-UR-002#04 | Hora | Testosterona 240 a las 15:00 | No interpretable por hora |
| COND-M5-UR-002#05 | Negativo · PDF hombre 46 años | Testosterona 412 | No activa |
| COND-M5-UR-A01#01 | Apoya | Total 250, SHBG 22, albúmina 4,4; libre baja | UR-002 sube a coincidencia alta |
| COND-M5-UR-A01#02 | SHBG alta | Total 330, SHBG 70; libre baja | Vigilar en la vista médica |
| COND-M5-UR-A01#03 | No se calcula · PDF hombre 46 años | Total 412, SHBG 28, IMC sin dato | No se calcula salvo que el IMC sea 30 o más |
| COND-M5-UR-A02#01 | Baja | PSA total 6,2, libre 0,5 (8 %) | Refuerza UR-001 en la vista médica |
| COND-M5-UR-A02#02 | Alta | PSA total 5,0, libre 1,5 (30 %) | Contextualiza UR-001 |
| COND-M5-UR-A02#03 | No aplica · PDF hombre 46 años | PSA total 1,10 | No se mide |

### M6

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| COND-M6-MI-001#01 | Positivo mayor | Edad 74, IMC 20,8, hs-CRP 9 | Activa, coincidencia alta, escalamiento 2 |
| COND-M6-MI-001#02 | Positivo joven | Edad 40, IMC 18,6, come menos hace un mes | Activa, escalamiento 1 |
| COND-M6-MI-001#03 | Vigilar | Edad 30, IMC 19,2, hs-CRP 0,6, ingesta normal | Vigilar |
| COND-M6-MI-001#04 | Sin medidas · PDF ejemplos | Peso y talla aún no registrados | No interpretable |
| COND-M6-MI-A01#01 | Hombre 46 años | — | SCORE2-PURE aplica; PSA y sangre oculta fuera de franja formal; sin recordatorios |
| COND-M6-MI-A01#02 | Mujer 34 años | — | Sin SCORE2-PURE; FSH interpretable como condición; recordatorio de cuello uterino |
| COND-M6-MI-A01#03 | Persona de 17 años | — | Fuera del alcance; no se procesa |
| COND-M6-MI-A02#01 | PDF hombre 46 años | Albúmina 4,6, creatinina 0,98, glucosa 112, hs-CRP 3,4, linfocitos 31,0 %, VCM 89,9, RDW 13,1, fosfatasa alcalina 88, leucocitos 7,8 | PhenoAge 44,3 años (1,7 menos que su edad) |
| COND-M6-MI-A02#02 | PDF mujer 34 años | Albúmina 4,3, creatinina 0,72, glucosa 86, hs-CRP 0,8, linfocitos 35,0 %, VCM 78,2, RDW 16,4, fosfatasa alcalina 62, leucocitos 6,1 | PhenoAge 34,1 años; advertencia: la anemia sube el RDW y puede inflar el valor |
| COND-M6-MI-A02#03 | Falta un analito | Sin fosfatasa alcalina | No se calcula; se dice qué falta |
| COND-M6-MI-A02#04 | Sin ayuno | Ayuno de 4 horas | No se calcula |
| COND-M6-RE-001#01 | Positivo · PDF hombre 46 años | Ácido úrico 7,6 (hasta 7,0), con prediabetes y síndrome metabólico | Activa, escalamiento 1; la vista médica lo liga al contexto cardiometabólico |
| COND-M6-RE-001#02 | Con diurético | Ácido úrico 8,2, toma hidroclorotiazida | Activa; la vista médica menciona el diurético |
| COND-M6-RE-001#03 | Negativo · PDF mujer 34 años | Ácido úrico 4,1 | No activa |
| COND-M6-RE-A01#01 | Positivo · PDF mujer 34 años | ANA positivo 1:160, patrón moteado fino (AC-4), anti-TPO 186 | Escalamiento 2; la vista médica anota la autoinmunidad tiroidea |
| COND-M6-RE-A01#02 | Título bajo | ANA 1:80, AC-2 | Escalamiento 1; nota de patrón frecuente en sanos |
| COND-M6-RE-A01#03 | Sin título | "ANA positivo" sin título | No interpretable; pedir título y patrón al laboratorio |
| COND-M6-RE-A01#04 | Negativo · PDF hombre 46 años | ANA negativo (menor de 1:80) | No activa |
| COND-M6-RE-A02#01 | Aislada | VSG 28 (hasta 15), hs-CRP 1,2 | Escalamiento 1, repetir |
| COND-M6-RE-A02#02 | Con inflamación | VSG 35, hs-CRP 14 | Refuerza la relación de inflamación |
| COND-M6-RE-A02#03 | Muy alta | VSG 110 | Escalamiento 2 |
| COND-M6-RE-A02#04 | Negativo · PDF ejemplos | VSG 12 y 18 | No activa |

### SEG

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| SEG-000#01 | En rango | Cloro 103 (98 a 107) | Escalamiento 0 |
| SEG-000#02 | Fuera de rango | Cloro 110 | Escalamiento 1, texto general |
| SEG-000#03 | Crítico | Cualquier valor con bandera crítica | Escalamiento 3 |
| SEG-001#01 | No detectable · PDF ejemplos | Troponina "\< 3" ng/L (percentil 99: 14) | En rango, escalamiento 0; revisión médica |
| SEG-001#02 | Elevada | Troponina 31 ng/L | Escalamiento 3, llamada el mismo día |
| SEG-001#03 | Límite | Troponina 14 ng/L (igual al percentil 99) | En rango; revisión médica |
| SEG-002#01 | En rango · PDF hombre 46 años | Cortisol 14,2 a las 7:15; ACTH 24 | Escalamiento 0; revisión médica |
| SEG-002#02 | En rango · PDF mujer 34 años | Cortisol 11,6 a las 7:40; ACTH 18 | Escalamiento 0; revisión médica |
| SEG-002#03 | Fuera de horario | Cortisol 9,0 a las 11:20 | No interpretable |
| SEG-002#04 | Bajo | Cortisol 4,1 a las 7:30 | Escalamiento 2 |
| SEG-002#05 | ACTH sin cadena de frío | ACTH sin registro de refrigeración | No interpretable |
| SEG-003#01 | En rango · PDF hombre 46 años | IGF-1 168 (83 a 233 para 45 a 49 años) | Escalamiento 0 |
| SEG-003#02 | Sin intervalo por edad | IGF-1 210 sin intervalo | Solo valor |
| SEG-003#03 | Con biotina | IGF-1 400, biotina declarada | No interpretable |
| SEG-004#01 | Normal · PDF hombre 46 años | Medida 292; calculada 291,6 (sodio 140, glucosa 112, BUN 15); brecha 0,4 | Escalamiento 0 |
| SEG-004#02 | Normal · PDF mujer 34 años | Medida 286; calculada 284,3; brecha 1,7 | Escalamiento 0 |
| SEG-004#03 | Brecha alta | Medida 312; calculada 290; brecha 22 | Escalamiento 2, llamada |
| SEG-005#01 | Normal · PDF ejemplos | NRBC 0,0 | Escalamiento 0 |
| SEG-005#02 | Positivo | NRBC 1,5 | Escalamiento 2, llamada |
| SEG-005#03 | Grave | NRBC 3, hemoglobina ajustada 7,2 | Escalamiento 3 |
| SEG-005#04 | Esplenectomía | NRBC 0,8, esplenectomía declarada | Escalamiento 1 |
| SEG-006#01 | Normal · PDF ejemplos | TP 12,1 y 11,8; INR 1,02 y 0,98; fibrinógeno 360 y 310 | Escalamiento 0 |
| SEG-006#02 | INR alto | INR 1,6 sin anticoagulante | Escalamiento 2 |
| SEG-006#03 | Con warfarina | INR 2,6, toma warfarina | Control en la vista médica |
| SEG-006#04 | Coagulopatía | Fibrinógeno 120, TP 19, plaquetas 60 | Escalamiento 3 |
| SEG-007#01 | Normal · PDF ejemplos | CK 165 y 82; LDH 190 y 160 | Escalamiento 0 |
| SEG-007#02 | Ejercicio | CK 1.600 (hasta 308), maratón hace 2 días, sin síntomas | Escalamiento 1, repetir |
| SEG-007#03 | Sin ejercicio | CK 2.000, sin ejercicio | Escalamiento 2 |
| SEG-007#04 | Urgente | CK 9.000, orina oscura | Escalamiento 3 |
| SEG-007#05 | LDH hemolizada | LDH 420, hemólisis reportada | No interpretable |
| SEG-008#01 | Normal · PDF ejemplos | Magnesio 2,0 y 1,9; cloro 103 y 104; fósforo 3,2 y 3,6 | Escalamiento 0 |
| SEG-008#02 | Magnesio con potasio bajo | Magnesio 1,4, potasio 3,1 | Escalamiento 2 |
| SEG-008#03 | Fósforo con TFG baja | Fósforo 5,2, TFG 38 | Se lee en M2 |
| SEG-009#01 | Normal · PDF ejemplos | A/G 1,70 y 1,59; IgG 1.120 y 1.050; IgM 95 y 140 | Escalamiento 0 |
| SEG-009#02 | Invertida | Albúmina 3,6, globulinas 4,2 (A/G 0,86) | Escalamiento 1; vista médica sugiere electroforesis |
| SEG-009#03 | IgG muy alta | IgG 3.600 sin infección | Escalamiento 2 |
| SEG-010#01 | Normal · PDF ejemplos | Péptido C 3,4 y 1,8; fructosamina 268 y 230 | Escalamiento 0 |
| SEG-010#02 | Fructosamina no confiable | Fructosamina 210, albúmina 2,8 | No interpretable |
| SEG-010#03 | Glucosa baja con péptido C alto | Glucosa 48, péptido C 6,2 | Escalamiento 3 (M1 EM-005) |
| SEG-011#01 | Fase folicular · PDF mujer 34 años | Día 9, estradiol 68, LH 5,4, progesterona 0,4; DHEA-S 180 | Todo en rango de fase, escalamiento 0 |
| SEG-011#02 | Hombre · PDF hombre 46 años | Estradiol 28, LH 4,2 (intervalo masculino); DHEA-S 210 | En rango |
| SEG-011#03 | Anticonceptivo | Estradiol 15, anticonceptivo oral | No interpretable por fase |
| SEG-011#04 | DHEA-S muy alta | Mujer, DHEA-S 820 (hasta 340) | Escalamiento 2 |
| SEG-012#01 | Normal · PDF hombre 46 años | Monocitos 7,1 %, basófilos 0,5 %, VPM 9,8 | Escalamiento 0 |
| SEG-012#02 | Apoyo de anemia · PDF mujer 34 años | HCM 26,0 (bajo), hematocrito 35,0 (bajo) | Se leen dentro de M3; no forman hallazgo propio |
| SEG-012#03 | Basófilos altos | Basófilos 3,5 % | Escalamiento 1, repetir |
| SEG-013#01 | Normal · PDF ejemplos | Tira negativa, urobilinógeno 0,2, heces sin moco ni sangre | Escalamiento 0 |
| SEG-013#02 | Glucosa con medicamento | Glucosa en orina positiva, toma empagliflozina | Escalamiento 0 |
| SEG-013#03 | Cetonas con diabetes | Cetonas positivas, glucosa 280 | Escalamiento 2 |
| SEG-013#04 | Sangre visible | Sangre macroscópica en heces | Escalamiento 2 |
| SEG-014#01 | Normal · PDF ejemplos | ApoA1 112 y 158; transferrina 256 y 346; zinc 82 y 71; BUN 15 y 10 | Escalamiento 0 |
| SEG-014#02 | Zinc sin tubo especial | Zinc 140, tubo estándar | No interpretable |
| SEG-014#03 | BUN alto | BUN 28, creatinina 0,9 (relación 31) | Vigilar hidratación |

### Calculados

| ID | Caso | Datos | Resultado esperado |
| --- | --- | --- | --- |
| remnant_cholesterol#01 | PDF hombre 46 años | Colesterol total 228, HDL 36, LDL medido 142 | 50 mg/dL, solo valor |
| remnant_cholesterol#02 | PDF mujer 34 años | Colesterol total 214, HDL 58, LDL medido 136 | 20 mg/dL, solo valor |
| remnant_cholesterol#03 | LDL calculado | LDL por Friedewald | No se calcula |
| tc_hdl_ratio#01 | PDF hombre 46 años | Colesterol total 228, HDL 36 | 6,33, solo valor |
| tc_hdl_ratio#02 | PDF mujer 34 años | Colesterol total 214, HDL 58 | 3,69, solo valor |
| tc_hdl_ratio#03 | Sin HDL | HDL no medido | No se calcula |
| phenoage#01 | PDF hombre 46 años | Los 9 analitos del PDF | 44,3 años |
| phenoage#02 | PDF mujer 34 años | Los 9 analitos del PDF, con anemia | 34,1 años, con advertencia por anemia |
| phenoage#03 | Falta un analito | Sin fosfatasa alcalina | No se calcula |

## Lo que falta en este set

1. Pasar los casos unitarios de texto a entradas estructuradas, como ya están los de punta a punta. Se hace mejor junto con el motor, en la Fase 4, porque el formato de entrada lo fija el desarrollo.
2. Casos con datos de la enfermera (presión, medidas, cuestionario) y con Apple Watch activo; hoy solo existen dentro de las fichas, no como casos de punta a punta.
3. Un caso de punta a punta con urgencia (escalamiento 3) para probar la llamada del equipo médico.
4. La firma del médico.