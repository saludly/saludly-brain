# Motor de análisis · Parte 3: condiciones de los módulos M3 a M6 · Informe de pruebas

**Saludly Brain · Fase 4 · versión 1 · 6 de octubre de 2026**

La tercera parte del motor evalúa las 42 fichas de condición de los módulos M3 (Sangre y nutrición), M4 (Digestivo e infecciones), M5 (Mujer y hombre) y M6 (Inmunidad y envejecimiento). Usa la misma estructura que la parte 2 y recibe sus resultados, porque algunas condiciones dependen de otras (por ejemplo, la prueba de celiaquía se pide si hay enzimas hepáticas altas o una condición tiroidea).

Con esto el motor evalúa las 76 fichas de condición del Knowledge Base.

## Resultado de las pruebas: 175 de 175

| Grupo | Comprobaciones | Resultado |
| --- | --- | --- |
| Casos de punta a punta, módulos M3 a M6 (incluida la edad biológica) | 46 | Todas correctas |
| 74 casos unitarios estructurados, tomados de las fichas | 129 | Todos correctos |

Las partes 1 y 2 se volvieron a correr: 90 de 90 y 167 de 167.

## Hombre de 46 años (sin datos de la enfermera)

| Ficha | Condición | Estado | Coincidencia | Escalamiento | Detalle |
| --- | --- | --- | --- | --- | --- |
| COND-M3-NU-A03 | Vitamina D baja | activa |  | 0 | recomendación alimentaria y de sol, sin dosis |
| COND-M4-GA-002 | Alteración hepatocelular | activa | moderada | 1 | segunda medición |
| COND-M4-GA-005 | Infección por H. pylori | activa | alta | 2 | incluir la limitación del antígeno fecal frente a la prueba de aliento |
| COND-M4-IN-002 | Hepatitis B y estado frente a la vacuna | activa | alta | 1 | estado hb: susceptible; recomendar vacuna |
| COND-M6-MI-A02 | Edad biológica (PhenoAge) | activa |  | 0 | phenoage: 44.3 |
| COND-M6-RE-001 | Ácido úrico alto sin síntomas | activa | alta | 1 | urico_alto |
| COND-M6-MI-A01 | Lectura por edad del panel | apoyo |  |  |  |
| COND-M3-HE-006 | Posible sobrecarga de hierro | vigilar | baja |  | ferritina alta con saturación normal; ligada a enzimas hepáticas altas |
| COND-M4-GA-006 | Enfermedad celíaca (prueba dirigida) | pendiente_refleja |  |  | el laboratorio debe correr IgA total y anti-tTG IgA (COND-M4-GA-002) |
| COND-M4-GA-A02 | Alteración hepática con consumo de alcohol | incompleta |  |  | consumo de alcohol |
| COND-M6-MI-001 | Riesgo de desnutrición | incompleta |  |  | peso_kg, talla_m, pérdida de peso |

Otras 31 fichas de estos módulos no se activan o no aplican.

## Mujer de 34 años (sin datos de la enfermera)

| Ficha | Condición | Estado | Coincidencia | Escalamiento | Detalle |
| --- | --- | --- | --- | --- | --- |
| COND-M3-HE-001 | Anemia ajustada por altitud y tabaquismo | activa | moderada | 2 | hemoglobina ajustada: 9.4; tabaquismo |
| COND-M3-HE-002 | Anemia por déficit de hierro | activa | alta | 2 | anemia, ferritina_baja, saturacion_baja, vcm_bajo, rdw_alto |
| COND-M3-NU-A03 | Vitamina D baja | activa |  | 0 | recomendación alimentaria y de sol, sin dosis |
| COND-M4-IN-002 | Hepatitis B y estado frente a la vacuna | activa | alta | 0 | estado hb: inmune_por_vacuna; anti_hbs |
| COND-M6-MI-A02 | Edad biológica (PhenoAge) | activa |  | 0 | phenoage: 34.1; Anemia o RDW alto: el valor puede estar inflado. |
| COND-M6-RE-A01 | ANA positivo | activa |  | 2 | autoinmunidad tiroidea asociada |
| COND-M6-MI-A01 | Lectura por edad del panel | apoyo |  |  | recordatorios: tamizaje de cuello uterino |
| COND-M4-GA-A02 | Alteración hepática con consumo de alcohol | incompleta |  |  | consumo de alcohol |
| COND-M6-MI-001 | Riesgo de desnutrición | incompleta |  |  | peso_kg, talla_m, pérdida de peso |

Otras 33 fichas de estos módulos no se activan o no aplican.

## Lo que encontraron las pruebas

- **Otro caso esperado que contradecía su ficha.** La ficha de anemia dice que, sin dato de tabaquismo, la coincidencia es moderada, porque no se puede aplicar ese ajuste. El caso de la mujer decía "alta". Corregí el caso, igual que con los triglicéridos del hombre en la parte 2. Los dos casos de punta a punta no traen datos de la enfermera a propósito, y estas dos correcciones muestran por qué importa esa visita: sin ella, varias coincidencias bajan.
- **Anemia por B12 o folato con glóbulos pequeños.** Una mujer con déficit de hierro (VCM bajo) y folato algo bajo activaba también la anemia por folato. Ahora, con VCM bajo, la anemia se atribuye al hierro y el folato bajo se evalúa por su propia ficha. Es un ajuste fino a la regla de la ficha, que no contemplaba ese caso; queda para que el médico lo confirme.
- **ALT limítrofe con patrón muscular.** Después de ejercicio intenso, una ALT apenas sobre el valor sano salía como "vigilar". Si hay patrón muscular, ahora no se lee como hepática.

## Lo que el motor hace con el caso del hombre y la celiaquía

En la parte de fichas había quedado la duda de si la ALT apenas alta debía activar la prueba refleja de celiaquía, que el PDF de ejemplo no trae. El motor aplica la regla del Consolidado: marca la celiaquía como **pendiente de prueba refleja** y le dice al laboratorio que debe correr IgA total y anti-transglutaminasa. Si el médico decide que una ALT apenas alta no debe pedirla, se cambia una línea.

## Supuestos y pendientes

1. **Índice de andrógenos libres.** El corte para considerarlo alto quedó provisional en 5, porque la ficha remite a la guía de SOP 2023 o al laboratorio y ninguno lo tiene escrito.
2. **Testosterona libre.** Se calcula, pero sin intervalo de referencia no se puede clasificar; por eso la testosterona baja nunca llega a coincidencia alta.
3. **Lista de parásitos.** Patógenos y comensales están en el código como lista inicial; los no clasificados (como Blastocystis) salen como vigilar hasta que el médico firme la lista.
4. **Chagas.** Funciona, pero sigue pendiente el lineamiento del INS para adultos.
5. **Datos del cuestionario.** Varias condiciones de estos módulos dependen de datos que debe recoger la enfermera: síntomas urinarios, alcohol, dieta, cirugía bariátrica, pérdida de peso, ingesta, procedencia de zona endémica, consentimiento de PSA. El formulario de la visita debe incluirlos.

## Lo que sigue

**Parte 4: relaciones y seguridad.** El motor evalúa las 27 relaciones entre módulos (patrones que agrupan condiciones y señales para vigilar) y las 15 fichas de seguridad, y produce la salida final: la lista ordenada de hallazgos con su escalamiento, lista para que el agente redacte el informe.