# Fichas de biomarcador · Tanda 4 — Calculados

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Esta tanda cierra las fichas de biomarcador nuevas con los 3 calculados que no tenían ficha: colesterol remanente, relación colesterol total/HDL y edad biológica (PhenoAge). Los tres los calcula el motor de Saludly a partir de valores del laboratorio; ninguno viene en el PDF.

Usa el esquema 2.1. Los calculados agregan dos campos: `formula` y `entradas`, y el motor guarda de qué valores salió cada resultado (trazabilidad, documento 04).

## Cuenta final de fichas nuevas

Con esta tanda son 33 fichas nuevas, de SLD-BIO-101 a SLD-BIO-133: 11 en la tanda 1, 12 en la tanda 2, 7 en la tanda 3 y 3 en esta. Antes había hablado de 34 y luego de 32; los dos números estaban mal porque la HCM aparecía contada dos veces en la lista original. El número correcto es 33.

## Índice

| doc_id | biomarker_id | Calculado | Fórmula | Alimenta |
| --- | --- | --- | --- | --- |
| SLD-BIO-131 | remnant_cholesterol | Colesterol remanente | Colesterol total − HDL − LDL | M1 CA-001 y CA-003 (contexto), SEG-014 |
| SLD-BIO-132 | tc_hdl_ratio | Relación colesterol total/HDL | Colesterol total / HDL | M1 CA-001 y CA-005 (contexto), SEG-014 |
| SLD-BIO-133 | phenoage | Edad biológica (PhenoAge) | Levine et al. 2018 | M6 MI-A02 |

---

## SLD-BIO-131 · Colesterol remanente

```yaml
doc_id: "SLD-BIO-131"
biomarker_id: "remnant_cholesterol"
name_es: "Colesterol remanente"
name_en: "Remnant cholesterol"
abbreviation: "Col. remanente"
sinonimos: ["Colesterol remanente", "Remnant cholesterol", "Colesterol de lipoproteínas remanentes"]
category: "Lípidos"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "mg/dL"
formula: "colesterol total - HDL - LDL"
entradas: ["total_cholesterol", "hdl_c", "ldl_c"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor y rango (contexto)"
panel: "calculado, todas las personas"
alimenta: ["COND-M1-CA-001", "COND-M1-CA-003", "SEG-014"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Colesterol que transportan las lipoproteínas ricas en triglicéridos (las que no son LDL ni HDL).

### B. Definición

Se asocia a riesgo cardiovascular más allá del LDL, sobre todo cuando los triglicéridos están altos.

### C. Cálculo y condiciones

Solo tiene sentido si el LDL es **medido** (directo). Si el laboratorio calcula el LDL con la fórmula de Friedewald, el remanente sale igual a triglicéridos / 5 y no aporta nada nuevo: en ese caso no se calcula. Requiere ayuno de 8 horas o más.

### D. Intervalos y umbrales

Sin intervalo del laboratorio ni corte de guía adoptado en los lotes. Se muestra solo el valor; en la vista médica se puede anotar un corte de la literatura cuando se verifique.

### E. Interpretación

Contexto de dislipidemia e hipertrigliceridemia; nunca forma un hallazgo propio.

### F. Contexto del paciente y confusores

Ayuno insuficiente, LDL calculado, triglicéridos de 400 mg/dL o más (el LDL directo pierde precisión).

### G. Relaciones

Triglicéridos, LDL, no-HDL, ApoB (M1).

### H. Tendencias

Baja con las mismas medidas que bajan los triglicéridos.

### I. Prevención

Reducir azúcar, harinas refinadas y alcohol; actividad física.

### J. Pruebas complementarias

ApoB (en el panel).

### K. Cuándo no interpretar / cuándo escalar

No escala.

### L. Evidencia

Por verificar; sin guía adoptada en los lotes.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "dato de contexto sobre tus grasas en sangre".
- Inferencias prohibidas: riesgo cardiovascular individual a partir del remanente.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [lipidos, calculado, contexto_cardiovascular, saludly_brain_v1]
use_when: ["triglicéridos altos con LDL medido"]
combine_with: [triglycerides, ldl_c, non_hdl_c, apob]
do_not_use_alone: ["estimar riesgo cardiovascular"]
do_not_conclude: ["enfermedad cardiovascular"]
escalate_when: []
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Colesterol total 228, HDL 36, LDL medido 142 | 50 mg/dL, solo valor |
| PDF mujer 34 años | Colesterol total 214, HDL 58, LDL medido 136 | 20 mg/dL, solo valor |
| LDL calculado | LDL por Friedewald | No se calcula |

---

## SLD-BIO-132 · Relación colesterol total/HDL

```yaml
doc_id: "SLD-BIO-132"
biomarker_id: "tc_hdl_ratio"
name_es: "Relación colesterol total/HDL"
name_en: "Total cholesterol to HDL ratio"
abbreviation: "CT/HDL"
sinonimos: ["Relación colesterol total/HDL", "Índice de Castelli", "Índice aterogénico", "CT/HDL", "TC/HDL ratio"]
category: "Lípidos"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
formula: "colesterol total / HDL"
entradas: ["total_cholesterol", "hdl_c"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor y rango (contexto)"
panel: "calculado, todas las personas"
alimenta: ["COND-M1-CA-001", "COND-M1-CA-005", "SEG-014"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Cociente entre el colesterol total y el HDL, conocido también como índice de Castelli.

### B. Definición

Resume en un número el balance entre el colesterol que se acumula en las arterias y el que se retira de ellas.

### C. Cálculo y condiciones

Se calcula siempre que estén colesterol total y HDL medidos.

### D. Intervalos y umbrales

Sin corte de guía adoptado en los lotes. Las guías usadas en el módulo M1 prefieren el no-HDL y la ApoB para decidir; la relación se muestra como valor de contexto. Los cortes tradicionales que circulan en la literatura no se usan hasta verificarlos.

### E. Interpretación

Contexto de dislipidemia y riesgo global; nunca forma un hallazgo propio.

### F. Contexto del paciente y confusores

HDL muy alto puede dar una relación baja que tranquiliza de más.

### G. Relaciones

Colesterol total, HDL, no-HDL, ApoB (M1).

### H. Tendencias

Mejora con más actividad física y menos azúcar.

### I. Prevención

Las de dislipidemia (M1 CA-001).

### J. Pruebas complementarias

No-HDL y ApoB (en el panel).

### K. Cuándo no interpretar / cuándo escalar

No escala.

### L. Evidencia

Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "dato de contexto sobre el balance de tu colesterol".
- Inferencias prohibidas: riesgo cardiovascular individual a partir de la relación.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [lipidos, calculado, contexto_cardiovascular, saludly_brain_v1]
use_when: ["contexto del perfil lipídico"]
combine_with: [total_cholesterol, hdl_c, non_hdl_c, apob]
do_not_use_alone: ["decidir riesgo cardiovascular"]
do_not_conclude: ["enfermedad cardiovascular"]
escalate_when: []
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Colesterol total 228, HDL 36 | 6,33, solo valor |
| PDF mujer 34 años | Colesterol total 214, HDL 58 | 3,69, solo valor |
| Sin HDL | HDL no medido | No se calcula |

---

## SLD-BIO-133 · Edad biológica (PhenoAge)

```yaml
doc_id: "SLD-BIO-133"
biomarker_id: "phenoage"
name_es: "Edad biológica (PhenoAge)"
name_en: "Phenotypic age (PhenoAge)"
abbreviation: "PhenoAge"
sinonimos: ["Edad biológica", "PhenoAge", "Edad fenotípica", "Phenotypic age"]
category: "Envejecimiento"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "años"
formula: "Levine et al. 2018 (ver ficha COND-M6-MI-A02)"
entradas: ["albumin", "creatinine", "glucose", "hs_crp", "lymphocytes_pct", "mcv", "rdw", "alp", "wbc", "edad"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor (pantalla aparte)"
panel: "calculado, todas las personas"
alimenta: ["COND-M6-MI-A02"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "coeficientes tomados de una implementación pública que cita el artículo; verificar contra el artículo original"
```

### A. Identificación

Estimación de la edad cuyo riesgo de mortalidad corresponde al de la persona, a partir de la edad y 9 analitos del panel.

### B. Definición

Modelo publicado por Levine y colaboradores en 2018, entrenado en población de EE. UU. (NHANES III). No tiene validación conocida en Colombia y no es un criterio clínico.

### C. Cálculo y condiciones

Unidades del modelo: albúmina en g/L, creatinina en µmol/L, glucosa en mmol/L, PCR en mg/dL (en logaritmo natural), linfocitos en %, VCM en fL, RDW en %, fosfatasa alcalina en U/L, leucocitos en 10³/µL y edad en años. La fórmula completa está en la ficha COND-M6-MI-A02. Se calcula solo con los 9 analitos medidos, glucosa en ayunas, edad de 20 años o más y sin embarazo.

### D. Intervalos y umbrales

No tiene intervalo: se muestra la edad biológica, la edad cronológica y la diferencia.

### E. Interpretación

Una edad biológica menor que la cronológica sugiere un perfil de riesgo más favorable que el promedio de la población del modelo, y viceversa. Su valor real está en la tendencia entre tomas.

### F. Contexto del paciente y confusores

Anemia (sube el RDW), infección reciente o hs-CRP mayor de 10 mg/L (sube PCR y leucocitos), hiperglucemia puntual. En esos casos se calcula con advertencia.

### G. Relaciones

Sus 9 analitos; ninguna condición depende de ella.

### H. Tendencias

Se compara con la toma siguiente; es el uso que más motiva.

### I. Prevención

Mejora con los mismos hábitos que mejoran sus componentes: control de la glucosa, actividad física, menos inflamación.

### J. Pruebas complementarias

No aplica.

### K. Cuándo no interpretar / cuándo escalar

No escala nunca (escalamiento 0).

### L. Evidencia

Levine ME, Lu AT, Quach A y otros. An epigenetic biomarker of aging for lifespan and healthspan. Aging. 2018;10(4):573-591.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "estimación de un modelo científico, útil para seguir en el tiempo".
- Inferencias prohibidas: expectativa de vida, "tu cuerpo tiene X años", envejecimiento acelerado sin segunda medición.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [envejecimiento, calculado, edad_biologica, pantalla_aparte, saludly_brain_v1]
use_when: ["pantalla de edad biológica", "objetivo envejecer de forma saludable"]
combine_with: [albumin, creatinine, glucose, hs_crp, lymphocytes_pct, mcv, rdw, alp, wbc]
do_not_use_alone: ["conclusiones clínicas"]
do_not_conclude: ["expectativa de vida", "envejecimiento acelerado sin segunda medición"]
escalate_when: []
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Los 9 analitos del PDF | 44,3 años |
| PDF mujer 34 años | Los 9 analitos del PDF, con anemia | 34,1 años, con advertencia por anemia |
| Falta un analito | Sin fosfatasa alcalina | No se calcula |

---

## Firma médica de la tanda

| Ficha | Aprobada | Cambios |
| --- | --- | --- |
| SLD-BIO-131 Colesterol remanente | \[ \] |  |
| SLD-BIO-132 Relación colesterol total/HDL | \[ \] |  |
| SLD-BIO-133 Edad biológica (PhenoAge) | \[ \] |  |

- Nombre y registro ReTHUS:
- Fecha:

## Lo que el médico debe mirar con más cuidado

1. Que el colesterol remanente solo se calcule con LDL medido.
2. Si quiere que se muestren cortes de la literatura para remanente y relación CT/HDL una vez verificados, o dejarlos como solo valor.
3. Los coeficientes de PhenoAge, a verificar contra el artículo original.