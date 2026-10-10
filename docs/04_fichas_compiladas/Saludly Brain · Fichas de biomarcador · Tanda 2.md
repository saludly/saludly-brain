# Fichas de biomarcador · Tanda 2 — Vitaminas nuevas, TIBC, HCM y neutrófilos %

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Esta tanda crea las fichas base de 12 analitos del panel estándar: las 9 vitaminas y nutrientes que entraron en el Lote 6, la TIBC, la HCM y el porcentaje de neutrófilos. Usa el esquema 2.1 de la tanda 1.

## Cómo se aplica aquí la regla de vitaminas

Todas las vitaminas siguen la regla aprobada (documento 07 y ficha COND-M3-NU-A04): se clasifican con el intervalo del laboratorio; si está baja, se recomiendan alimentos y el suplemento solo se menciona como opción para hablar con el médico, sin dosis; sin intervalo, se muestra solo el valor. Cada ficha agrega lo propio de su vitamina: qué alimentos la aportan (con ejemplos fáciles de conseguir en Colombia), qué la falsea y con qué medicamentos choca.

Tres hallazgos de esta tanda que cambian cómo se interpreta:

- **Vitaminas A y E dependen de otros valores.** La vitamina A baja con la inflamación aunque no falte, y la E sube y baja con el colesterol y los triglicéridos. Se leen con hs-CRP y con el perfil lipídico.
- **La vitamina K1 choca con la warfarina.** A quien toma warfarina nunca se le recomienda comer más hojas verdes sin hablar con su médico.
- **La niacina en sangre no es el marcador habitual.** Su estado se evalúa normalmente con metabolitos en orina. El valor en sangre se muestra solo como información.

## Estado de las fuentes

Igual que en la tanda 1: sin fuentes leídas completas en esta sesión. Todas llevan `status: "BORRADOR"` y `fuentes_estado: "por verificar"`.

## Índice

| doc_id | biomarker_id | Analito | Unidad canónica | Alimenta |
| --- | --- | --- | --- | --- |
| SLD-BIO-112 | vitamin_a | Vitamina A (retinol) | µg/dL | M3 NU-A04 |
| SLD-BIO-113 | vitamin_e | Vitamina E (alfa-tocoferol) | mg/L | M3 NU-A04 |
| SLD-BIO-114 | vitamin_k1 | Vitamina K1 (filoquinona) | ng/mL | M3 NU-A04 |
| SLD-BIO-115 | vitamin_c | Vitamina C (ácido ascórbico) | mg/dL | M3 NU-A04 |
| SLD-BIO-116 | biotin | Biotina (vitamina B7) | ng/L | M3 NU-A04, regla de interferencia |
| SLD-BIO-117 | niacin | Niacina (vitamina B3) | µg/mL | M3 NU-A04 |
| SLD-BIO-118 | omega3_index | Índice omega-3 | % | M3 NU-A04 |
| SLD-BIO-119 | omega6_omega3_ratio | Relación omega-6/omega-3 | sin unidad | M3 NU-A04 |
| SLD-BIO-120 | coq10 | Coenzima Q10 | µg/mL | M3 NU-A04 |
| SLD-BIO-121 | tibc | Capacidad total de fijación de hierro | µg/dL | M3 HE-002, HE-006 |
| SLD-BIO-122 | mch | Hemoglobina corpuscular media (HCM) | pg | M3 HE-002, SEG-012 |
| SLD-BIO-123 | neutrophils_pct | Neutrófilos % | % | M3 HE-A02, SEG-012 |

---

## SLD-BIO-112 · Vitamina A (retinol)

```yaml
doc_id: "SLD-BIO-112"
biomarker_id: "vitamin_a"
name_es: "Vitamina A (retinol sérico)"
name_en: "Vitamin A (serum retinol)"
abbreviation: "Vit A"
sinonimos: ["Vitamina A", "Retinol", "Retinol sérico", "Vit A"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/dL"
specimen: "Suero protegido de la luz"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Retinol en suero, medido habitualmente por HPLC.

### B. Definición

Vitamina liposoluble necesaria para la visión, la piel y la inmunidad. Se almacena en el hígado, así que el valor en sangre se mantiene estable hasta que las reservas se agotan o se saturan.

### C. Espécimen y toma

Suero en ayunas, protegido de la luz (el retinol se degrada con ella).

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 30 a 80 µg/dL).

### E. Interpretación

Bajo: ingesta insuficiente, mala absorción de grasas o inflamación. Alto: suplementos o exceso de hígado en la dieta; la vitamina A se acumula.

### F. Contexto del paciente y confusores

La inflamación baja el retinol sin que falte (con hs-CRP mayor de 5 mg/L, un valor bajo no se interpreta como déficit). La enfermedad renal crónica lo sube. Embarazo: el exceso es dañino para el bebé.

### G. Relaciones

hs-CRP (inflamación), TFG (función renal), albúmina.

### H. Tendencias

Cambia lentamente; refleja reservas del hígado.

### I. Prevención y alimentos

Huevo, lácteos e hígado (vitamina A directa); zanahoria, ahuyama, mango, papaya y espinaca (provitamina A, que el cuerpo convierte según lo necesita).

### J. Pruebas complementarias

Según el médico.

### K. Cuándo no interpretar / cuándo escalar

Bajo con hs-CRP mayor de 5: no interpretable como déficit. Alto: escalamiento 1 y pregunta por suplementos; en embarazo, escalamiento 2.

### L. Evidencia

Regla de vitaminas (documento 07). Fuentes por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "vitamina A por debajo o por encima del rango del laboratorio".
- Inferencias prohibidas: déficit con inflamación, dosis de suplemento, recomendar hígado en embarazo.
- Revisión profesional: alta en embarazo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, liposoluble, vitamina_a, panel_estandar, saludly_brain_v1]
use_when: ["vitamina A fuera de rango"]
combine_with: [hs_crp, egfr, albumin]
do_not_use_alone: ["déficit de vitamina A con inflamación"]
do_not_conclude: ["deficiencia de vitamina A"]
escalate_when: ["vitamina A alta en embarazo", "vitamina A alta con suplementos"]
```

---

## SLD-BIO-113 · Vitamina E (alfa-tocoferol)

```yaml
doc_id: "SLD-BIO-113"
biomarker_id: "vitamin_e"
name_es: "Vitamina E (alfa-tocoferol)"
name_en: "Vitamin E (alpha-tocopherol)"
abbreviation: "Vit E"
sinonimos: ["Vitamina E", "Alfa-tocoferol", "Tocoferol", "Vit E"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "mg/L"
specimen: "Suero en ayunas protegido de la luz"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Alfa-tocoferol en suero por HPLC.

### B. Definición

Vitamina liposoluble antioxidante. Viaja en la sangre con el colesterol y los triglicéridos.

### C. Espécimen y toma

Suero en ayunas, protegido de la luz.

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 5,5 a 17,0 mg/L).

### E. Interpretación

Como viaja con los lípidos, sube y baja con el colesterol y los triglicéridos. Con lípidos muy altos o muy bajos, el valor absoluto engaña y el médico puede usar la relación vitamina E/lípidos. El déficit real es raro y suele deberse a mala absorción de grasas.

### F. Contexto del paciente y confusores

Lípidos altos o bajos, suplementos, mala absorción, anticoagulantes (dosis altas de vitamina E aumentan el riesgo de sangrado).

### G. Relaciones

Colesterol total y triglicéridos (M1).

### H. Tendencias

Sin uso de seguimiento en prevención.

### I. Prevención y alimentos

Nueces, maní, semillas de girasol, almendras, aguacate y aceites vegetales.

### J. Pruebas complementarias

Relación vitamina E/lípidos según el médico.

### K. Cuándo no interpretar / cuándo escalar

Con triglicéridos de 500 mg/dL o más o colesterol muy bajo: solo valor. Alta con suplementos y anticoagulantes: escalamiento 1 con sugerencia de consulta.

### L. Evidencia

Regla de vitaminas (documento 07). Fuentes por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "vitamina E fuera de rango; se interpreta junto con tus lípidos".
- Inferencias prohibidas: déficit sin considerar los lípidos, dosis de suplemento.
- Revisión profesional: alta con anticoagulantes.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, liposoluble, vitamina_e, panel_estandar, saludly_brain_v1]
use_when: ["vitamina E fuera de rango"]
combine_with: [total_cholesterol, triglycerides]
do_not_use_alone: ["déficit con lípidos alterados"]
do_not_conclude: ["deficiencia de vitamina E"]
escalate_when: ["vitamina E alta con anticoagulantes"]
```

---

## SLD-BIO-114 · Vitamina K1 (filoquinona)

```yaml
doc_id: "SLD-BIO-114"
biomarker_id: "vitamin_k1"
name_es: "Vitamina K1 (filoquinona)"
name_en: "Vitamin K1 (phylloquinone)"
abbreviation: "Vit K1"
sinonimos: ["Vitamina K1", "Filoquinona", "Vitamina K", "Phylloquinone"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
specimen: "Suero en ayunas protegido de la luz"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Filoquinona en suero por HPLC.

### B. Definición

Vitamina liposoluble necesaria para la coagulación y el hueso.

### C. Espécimen y toma

Suero en ayunas: refleja sobre todo lo que se comió el día anterior. Protegido de la luz.

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 0,10 a 2,20 ng/mL).

### E. Interpretación

Muestra la ingesta reciente más que las reservas. Viaja con los triglicéridos, que la suben. El déficit con efecto en la coagulación se ve en el tiempo de protrombina y el INR, no en este valor.

### F. Contexto del paciente y confusores

Warfarina (antagonista de la vitamina K), antibióticos prolongados, mala absorción de grasas, triglicéridos altos.

### G. Relaciones

Tiempo de protrombina e INR (SEG-006), triglicéridos.

### H. Tendencias

Varía de un día a otro con la dieta.

### I. Prevención y alimentos

Espinaca, brócoli, repollo, lechuga y otras hojas verdes. **A quien toma warfarina nunca se le recomienda comer más hojas verdes sin hablar con su médico**: un cambio brusco altera el efecto del medicamento.

### J. Pruebas complementarias

Tiempo de protrombina e INR (ya en el panel).

### K. Cuándo no interpretar / cuándo escalar

Con warfarina: sin recomendación alimentaria, solo nota para el médico. Bajo con INR alto sin anticoagulante: se lee en SEG-006 (escalamiento 2).

### L. Evidencia

Regla de vitaminas (documento 07). Fuentes por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "vitamina K1 baja en esta toma; refleja sobre todo la alimentación reciente".
- Inferencias prohibidas: cambiar la dieta a personas con warfarina, problema de coagulación por este valor.
- Revisión profesional: personas con warfarina.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, liposoluble, vitamina_k, coagulacion, panel_estandar, saludly_brain_v1]
use_when: ["vitamina K1 fuera de rango"]
combine_with: [pt, inr, triglycerides]
do_not_use_alone: ["evaluar coagulación"]
do_not_conclude: ["trastorno de coagulación"]
escalate_when: ["vitamina K1 baja con INR alto sin anticoagulante"]
```

---

## SLD-BIO-115 · Vitamina C (ácido ascórbico)

```yaml
doc_id: "SLD-BIO-115"
biomarker_id: "vitamin_c"
name_es: "Vitamina C (ácido ascórbico)"
name_en: "Vitamin C (ascorbic acid)"
abbreviation: "Vit C"
sinonimos: ["Vitamina C", "Ácido ascórbico", "Ascorbato", "Vit C"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "mg/dL"
specimen: "Plasma heparinizado, congelado y protegido de la luz"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Ácido ascórbico en plasma por HPLC.

### B. Definición

Vitamina hidrosoluble antioxidante, necesaria para el colágeno y para absorber el hierro de los vegetales.

### C. Espécimen y toma

Es la muestra más delicada del panel: se degrada en pocas horas a temperatura ambiente. Exige separar el plasma, protegerlo de la luz y transportarlo congelado. Sin eso, el resultado sale falsamente bajo (protocolo de toma, Lote 6).

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 0,4 a 2,0 mg/dL).

### E. Interpretación

Refleja la ingesta de los días recientes. El déficit grave (escorbuto) es raro.

### F. Contexto del paciente y confusores

Tabaquismo (baja la vitamina C), transporte no congelado, suplementos en dosis altas (interfieren con algunas pruebas, como la fructosamina).

### G. Relaciones

Hierro y ferritina (M3): la vitamina C ayuda a absorber hierro de los vegetales.

### H. Tendencias

Cambia rápido con la dieta.

### I. Prevención y alimentos

Guayaba, naranja, mandarina, limón, kiwi, fresa, pimentón y brócoli.

### J. Pruebas complementarias

No aplica.

### K. Cuándo no interpretar / cuándo escalar

Sin transporte congelado validado: no interpretable. Las dosis altas de suplemento se asocian a cálculos renales en personas predispuestas: si está alta con suplementos, escalamiento 1.

### L. Evidencia

Regla de vitaminas (documento 07), protocolo de toma domiciliaria. Fuentes por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "vitamina C baja; refleja tu alimentación de los últimos días".
- Inferencias prohibidas: escorbuto, dosis de suplemento, interpretar sin transporte congelado.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, hidrosoluble, vitamina_c, preanalitica_critica, panel_estandar, saludly_brain_v1]
use_when: ["vitamina C fuera de rango", "recomendación para absorber hierro"]
combine_with: [ferritin, serum_iron]
do_not_use_alone: ["interpretar sin transporte congelado"]
do_not_conclude: ["escorbuto"]
escalate_when: ["vitamina C alta con suplementos"]
```

---

## SLD-BIO-116 · Biotina (vitamina B7)

```yaml
doc_id: "SLD-BIO-116"
biomarker_id: "biotin"
name_es: "Biotina (vitamina B7)"
name_en: "Biotin (vitamin B7)"
abbreviation: "B7"
sinonimos: ["Biotina", "Vitamina B7", "Vitamina H", "Biotin"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/L"
specimen: "Suero"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04", "regla de interferencia de biotina (documento 04)"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Biotina en suero por inmunoensayo.

### B. Definición

Vitamina hidrosoluble del grupo B. Su importancia en el panel no es el déficit, que es raro, sino el exceso: los suplementos para cabello, piel y uñas traen dosis muy altas que alteran muchos inmunoensayos.

### C. Espécimen y toma

Suero. La enfermera pregunta si toma suplementos de biotina o "para el cabello y las uñas" y cuándo fue la última dosis.

### D. Intervalos y umbrales

El laboratorio de ejemplo no reporta intervalo ("No establecido"); el laboratorio aliado debe confirmar si lo tiene.

### E. Interpretación

Biotina alta, o suplemento declarado, invalida la interpretación de TSH, T4 libre, T3 libre, anticuerpos tiroideos, B12, folato, IGF-1 y otros inmunoensayos hasta repetirlos sin el suplemento. Según el método, puede dar valores falsamente altos o bajos y puede imitar un hipertiroidismo.

### F. Contexto del paciente y confusores

Suplementos de belleza, multivitamínicos, dosis altas por indicación médica.

### G. Relaciones

Todas las pruebas por inmunoensayo del panel.

### H. Tendencias

Baja en pocos días al suspender el suplemento.

### I. Prevención y alimentos

Huevo cocido, nueces y semillas. La clara de huevo cruda reduce su absorción.

### J. Pruebas complementarias

Repetir las pruebas afectadas sin el suplemento.

### K. Cuándo no interpretar / cuándo escalar

Biotina alta o suplemento declarado: bloquea las pruebas afectadas (escalamiento 1, repetir). Sin intervalo del laboratorio, la regla depende solo del cuestionario.

### L. Evidencia

Advertencia de la FDA sobre interferencia de biotina en pruebas de laboratorio. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "la biotina puede alterar algunos de tus resultados; hay que repetirlos sin el suplemento".
- Inferencias prohibidas: interpretar tiroides u otras pruebas afectadas con biotina alta.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, interferencia, biotina, inmunoensayo, panel_estandar, saludly_brain_v1]
use_when: ["biotina alta", "suplemento de biotina declarado", "resultados de tiroides incongruentes"]
combine_with: [tsh, free_t4, free_t3, vitamin_b12, folate, igf1]
do_not_use_alone: []
do_not_conclude: ["deficiencia de biotina"]
escalate_when: ["biotina alta con resultados de tiroides alterados"]
```

---

## SLD-BIO-117 · Niacina (vitamina B3)

```yaml
doc_id: "SLD-BIO-117"
biomarker_id: "niacin"
name_es: "Niacina (vitamina B3)"
name_en: "Niacin (vitamin B3)"
abbreviation: "B3"
sinonimos: ["Niacina", "Vitamina B3", "Ácido nicotínico", "Nicotinamida", "Niacin"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/mL"
specimen: "Suero o plasma"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Niacina o sus formas en sangre, habitualmente por LC-MS/MS.

### B. Definición

Vitamina hidrosoluble del grupo B, necesaria para el metabolismo energético. Su déficit grave (pelagra) es raro.

### C. Espécimen y toma

Suero o plasma en ayunas.

### D. Intervalos y umbrales

El laboratorio de ejemplo no reporta intervalo ("No establecido").

### E. Interpretación

El estado de niacina se evalúa normalmente con metabolitos en orina, no con el valor en sangre. Por eso se muestra solo como información, sin clase, aunque el laboratorio dé un intervalo, hasta que el médico decida otra cosa.

### F. Contexto del paciente y confusores

Suplementos en dosis altas (enrojecimiento, daño hepático), alcohol, isoniazida.

### G. Relaciones

ALT y GGT si toma niacina en dosis altas.

### H. Tendencias

Sin uso de seguimiento.

### I. Prevención y alimentos

Carnes, pollo, pescado, maní y cereales integrales.

### J. Pruebas complementarias

Metabolitos en orina, según el médico.

### K. Cuándo no interpretar / cuándo escalar

Siempre solo valor. Suplemento en dosis altas con ALT alta: escalamiento 1.

### L. Evidencia

Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "valor de niacina mostrado como información".
- Inferencias prohibidas: déficit o exceso a partir del valor en sangre.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, hidrosoluble, niacina, solo_informativo, panel_estandar, saludly_brain_v1]
use_when: ["valor de niacina"]
combine_with: [alt, ggt]
do_not_use_alone: ["evaluar el estado de niacina"]
do_not_conclude: ["pelagra", "deficiencia de niacina"]
escalate_when: ["suplemento de niacina en dosis altas con ALT alta"]
```

---

## SLD-BIO-118 · Índice omega-3

```yaml
doc_id: "SLD-BIO-118"
biomarker_id: "omega3_index"
name_es: "Índice omega-3"
name_en: "Omega-3 index"
abbreviation: "O3I"
sinonimos: ["Índice omega-3", "Omega-3 index", "EPA+DHA en eritrocitos", "Índice de omega 3"]
category: "Ácidos grasos"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "%"
specimen: "Sangre total (membranas de glóbulos rojos)"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Porcentaje de EPA y DHA sobre el total de ácidos grasos de las membranas de los glóbulos rojos, por cromatografía de gases.

### B. Definición

Refleja el consumo de omega-3 de origen marino en los últimos meses, porque los glóbulos rojos viven unos 120 días.

### C. Espécimen y toma

Sangre total; el ayuno no es crítico.

### D. Intervalos y umbrales

El laboratorio de ejemplo no reporta intervalo ("No establecido"). En la literatura se ha propuesto un índice de 8 % o más como deseable y menor de 4 % como de mayor riesgo cardiovascular, pero no es un estándar clínico: esos cortes solo se muestran en la vista médica, como contexto.

### E. Interpretación

Se muestra el valor al paciente sin clase. Bajo en la vista médica: refuerza la recomendación de pescado.

### F. Contexto del paciente y confusores

Suplementos de omega-3, dieta vegetariana (el ALA de la linaza o la chía se convierte poco en EPA y DHA).

### G. Relaciones

Triglicéridos y riesgo cardiovascular (M1), como contexto.

### H. Tendencias

Cambia en semanas a meses con la dieta.

### I. Prevención y alimentos

Sardina, atún, salmón, trucha y otros pescados grasos dos veces por semana. Linaza y chía aportan omega-3 vegetal.

### J. Pruebas complementarias

Relación omega-6/omega-3 (en el panel).

### K. Cuándo no interpretar / cuándo escalar

No escala. Los suplementos en dosis altas con anticoagulantes requieren hablarlo con el médico.

### L. Evidencia

Por verificar. Corte del 8 %: propuesto en la literatura (Harris y von Schacky, 2004), sin consenso de guía.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "valor de omega-3; comer pescado graso con regularidad lo mejora".
- Inferencias prohibidas: riesgo cardiovascular individual a partir del índice, dosis de suplemento.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [acidos_grasos, omega3, nutricion, panel_estandar, saludly_brain_v1]
use_when: ["índice omega-3", "recomendación de pescado"]
combine_with: [omega6_omega3_ratio, triglycerides]
do_not_use_alone: ["estimar riesgo cardiovascular"]
do_not_conclude: ["riesgo cardiovascular alto"]
escalate_when: []
```

---

## SLD-BIO-119 · Relación omega-6/omega-3

```yaml
doc_id: "SLD-BIO-119"
biomarker_id: "omega6_omega3_ratio"
name_es: "Relación omega-6/omega-3"
name_en: "Omega-6 to omega-3 ratio"
abbreviation: "O6/O3"
sinonimos: ["Relación omega 6/omega 3", "Ratio omega-6/omega-3", "Cociente omega 6 omega 3"]
category: "Ácidos grasos"
parameter_type: "derived_ratio"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
specimen: "Sangre total"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Cociente entre ácidos grasos omega-6 y omega-3 en sangre, por cromatografía de gases.

### B. Definición

Indica el balance entre los aceites vegetales (ricos en omega-6) y el pescado (rico en omega-3) en la dieta.

### C. Espécimen y toma

Sangre total.

### D. Intervalos y umbrales

Sin intervalo de referencia establecido ni meta de consenso.

### E. Interpretación

Siempre solo valor. Una relación alta acompaña a un índice omega-3 bajo y refuerza la misma recomendación.

### F. Contexto del paciente y confusores

Suplementos de omega-3, dieta con mucho aceite de soya o de maíz.

### G. Relaciones

Índice omega-3 (siempre juntos).

### H. Tendencias

Cambia con la dieta en semanas a meses.

### I. Prevención y alimentos

Más pescado graso; preferir aceite de oliva o de canola en lugar de cantidades grandes de aceites de soya o maíz.

### J. Pruebas complementarias

No aplica.

### K. Cuándo no interpretar / cuándo escalar

No escala.

### L. Evidencia

Por verificar; sin meta de consenso.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "valor informativo del balance de grasas de la dieta".
- Inferencias prohibidas: riesgo de enfermedad a partir de la relación.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [acidos_grasos, omega3, omega6, solo_informativo, panel_estandar, saludly_brain_v1]
use_when: ["relación omega-6/omega-3"]
combine_with: [omega3_index]
do_not_use_alone: ["estimar riesgo"]
do_not_conclude: ["inflamación", "riesgo cardiovascular"]
escalate_when: []
```

---

## SLD-BIO-120 · Coenzima Q10

```yaml
doc_id: "SLD-BIO-120"
biomarker_id: "coq10"
name_es: "Coenzima Q10"
name_en: "Coenzyme Q10"
abbreviation: "CoQ10"
sinonimos: ["Coenzima Q10", "CoQ10", "Ubiquinona", "Ubiquinol"]
category: "Nutrientes"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/mL"
specimen: "Plasma o suero en ayunas, protegido de la luz"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Coenzima Q10 total en plasma por HPLC.

### B. Definición

Molécula que el cuerpo produce y que participa en la producción de energía de las células. No es una vitamina en sentido estricto.

### C. Espécimen y toma

Plasma o suero en ayunas, protegido de la luz.

### D. Intervalos y umbrales

El laboratorio de ejemplo no reporta intervalo ("No establecido").

### E. Interpretación

Viaja con el colesterol LDL, así que baja cuando baja el LDL. Las estatinas reducen la CoQ10 en sangre; no está establecido que eso explique los síntomas musculares ni que suplementar los mejore.

### F. Contexto del paciente y confusores

Estatinas, LDL bajo o alto, suplementos.

### G. Relaciones

LDL (M1), CK si hay síntomas musculares con estatinas (SEG-007).

### H. Tendencias

Sin uso de seguimiento en prevención.

### I. Prevención y alimentos

Carnes, pescados grasos y vísceras aportan algo; el cuerpo produce la mayor parte.

### J. Pruebas complementarias

No aplica.

### K. Cuándo no interpretar / cuándo escalar

Solo valor. Los suplementos pueden disminuir el efecto de la warfarina: con anticoagulante, escalamiento 1 y sugerencia de consulta.

### L. Evidencia

Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "valor informativo de coenzima Q10".
- Inferencias prohibidas: recomendar suspender estatinas, dosis de suplemento, déficit.
- Revisión profesional: suplemento con warfarina.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [nutrientes, coq10, solo_informativo, panel_estandar, saludly_brain_v1]
use_when: ["valor de coenzima Q10", "estatinas con síntomas musculares"]
combine_with: [ldl_c, ck_cpk]
do_not_use_alone: ["explicar síntomas musculares"]
do_not_conclude: ["deficiencia de CoQ10", "miopatía por estatinas"]
escalate_when: ["suplemento de CoQ10 con warfarina"]
```

---

## SLD-BIO-121 · Capacidad total de fijación de hierro (TIBC)

```yaml
doc_id: "SLD-BIO-121"
biomarker_id: "tibc"
name_es: "Capacidad total de fijación de hierro"
name_en: "Total iron-binding capacity"
abbreviation: "TIBC"
sinonimos: ["TIBC", "CTFH", "Capacidad total de fijación de hierro", "Capacidad de fijación del hierro"]
category: "Metabolismo del hierro"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/dL"
specimen: "Suero en ayunas"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-HE-002", "COND-M3-HE-006", "saturación de transferrina (calculado)"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Cantidad máxima de hierro que puede transportar la transferrina en sangre.

### B. Definición

Mide indirectamente la transferrina. Sube cuando el cuerpo necesita hierro y baja con la inflamación.

### C. Espécimen y toma

Suero en ayunas, en la mañana (el hierro sérico, que se usa con ella, varía en el día).

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 250 a 450 µg/dL).

### E. Interpretación

Alta: déficit de hierro, embarazo, anticonceptivos con estrógenos. Baja: inflamación, desnutrición, enfermedad hepática. Se usa sobre todo para calcular la saturación de transferrina (hierro / TIBC × 100).

### F. Contexto del paciente y confusores

Embarazo, anticonceptivos, inflamación, desnutrición.

### G. Relaciones

Ferritina, hierro sérico, saturación, transferrina, hs-CRP (M3).

### H. Tendencias

Baja al corregir el déficit de hierro.

### I. Prevención

La de hierro (M3).

### J. Pruebas complementarias

Ninguna adicional.

### K. Cuándo no interpretar / cuándo escalar

No escala sola; se lee dentro de las condiciones de hierro.

### L. Evidencia

OMS 2020 (ferritina y estado de hierro). Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "dato de apoyo para entender tu hierro".
- Inferencias prohibidas: diagnóstico con TIBC aislada.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hierro, hematologia, tibc, panel_estandar, saludly_brain_v1]
use_when: ["cálculo de saturación de transferrina", "perfil de hierro"]
combine_with: [serum_iron, ferritin, transferrin, transferrin_saturation, hs_crp]
do_not_use_alone: ["diagnóstico de déficit de hierro"]
do_not_conclude: ["anemia ferropénica con TIBC sola"]
escalate_when: []
```

---

## SLD-BIO-122 · Hemoglobina corpuscular media (HCM)

```yaml
doc_id: "SLD-BIO-122"
biomarker_id: "mch"
name_es: "Hemoglobina corpuscular media"
name_en: "Mean corpuscular hemoglobin"
abbreviation: "HCM"
sinonimos: ["HCM", "MCH", "Hemoglobina corpuscular media", "Hb corpuscular media"]
category: "Hematología"
parameter_type: "derived_index"
tipo_resultado: "numérico"
unidad_canonica: "pg"
specimen: "Sangre total EDTA"
nivel_catalogo: "solo valor y rango (apoyo de condiciones)"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-HE-002", "SEG-012"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Índice del hemograma: hemoglobina / recuento de eritrocitos × 10.

### B. Definición

Cantidad promedio de hemoglobina en cada glóbulo rojo.

### C. Espécimen y toma

Sangre total EDTA, la del hemograma.

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 27,0 a 33,0 pg).

### E. Interpretación

Baja: glóbulos rojos con poca hemoglobina, típico del déficit de hierro y de los rasgos talasémicos. Alta: glóbulos rojos grandes (déficit de B12 o folato, alcohol, hipotiroidismo). Acompaña al VCM; casi nunca aporta algo que el VCM no diga.

### F. Contexto del paciente y confusores

Lipemia o leucocitos muy altos pueden falsear el cálculo.

### G. Relaciones

VCM, hemoglobina, RDW, ferritina (M3).

### H. Tendencias

Se normaliza al corregir la causa.

### I. Prevención

La de la causa.

### J. Pruebas complementarias

Las de la anemia (M3).

### K. Cuándo no interpretar / cuándo escalar

No escala sola (SEG-012).

### L. Evidencia

Hematología básica. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "dato de apoyo del hemograma".
- Inferencias prohibidas: talasemia o anemia por HCM aislada.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, hemograma, indice_eritrocitario, panel_estandar, saludly_brain_v1]
use_when: ["apoyo en anemia"]
combine_with: [mcv, hemoglobin, rdw, ferritin]
do_not_use_alone: ["clasificar anemia"]
do_not_conclude: ["talasemia"]
escalate_when: []
```

---

## SLD-BIO-123 · Neutrófilos %

```yaml
doc_id: "SLD-BIO-123"
biomarker_id: "neutrophils_pct"
name_es: "Neutrófilos (porcentaje)"
name_en: "Neutrophils (percentage)"
abbreviation: "NEU%"
sinonimos: ["Neutrófilos %", "Neutrófilos relativos", "Segmentados %", "Polimorfonucleares %", "NEU%"]
category: "Hematología"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "%"
specimen: "Sangre total EDTA"
nivel_catalogo: "solo valor y rango (apoyo de condiciones)"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-HE-A02", "SEG-012"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Proporción de neutrófilos entre los leucocitos, en el diferencial del hemograma.

### B. Definición

Los neutrófilos son la primera defensa contra las bacterias.

### C. Espécimen y toma

Sangre total EDTA.

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 40 a 70 %).

### E. Interpretación

El porcentaje solo no basta: la decisión se toma con el recuento absoluto (ficha neutrophils_abs). Un porcentaje alto con recuento normal suele no tener importancia.

### F. Contexto del paciente y confusores

Infección reciente, corticoides, ejercicio, tabaquismo. Las personas de ascendencia africana pueden tener recuentos de neutrófilos más bajos sin enfermedad (neutropenia étnica benigna); es relevante en Colombia y la vista médica lo anota.

### G. Relaciones

Neutrófilos absolutos, leucocitos, linfocitos (M3).

### H. Tendencias

Cambia con infecciones y estrés.

### I. Prevención

No aplica.

### J. Pruebas complementarias

Repetir hemograma.

### K. Cuándo no interpretar / cuándo escalar

No escala por el porcentaje; escala por el absoluto según HE-A02.

### L. Evidencia

Hematología básica. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "dato del diferencial; se interpreta con el recuento absoluto".
- Inferencias prohibidas: infección, defensas bajas, leucemia.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, hemograma, diferencial, panel_estandar, saludly_brain_v1]
use_when: ["diferencial de leucocitos"]
combine_with: [neutrophils_abs, wbc, lymphocytes_pct]
do_not_use_alone: ["decidir neutropenia o neutrofilia"]
do_not_conclude: ["infección", "leucemia"]
escalate_when: []
```

---

## Firma médica de la tanda

| Ficha | Aprobada | Cambios |
| --- | --- | --- |
| SLD-BIO-112 Vitamina A | \[ \] |  |
| SLD-BIO-113 Vitamina E | \[ \] |  |
| SLD-BIO-114 Vitamina K1 | \[ \] |  |
| SLD-BIO-115 Vitamina C | \[ \] |  |
| SLD-BIO-116 Biotina | \[ \] |  |
| SLD-BIO-117 Niacina | \[ \] |  |
| SLD-BIO-118 Índice omega-3 | \[ \] |  |
| SLD-BIO-119 Relación omega-6/omega-3 | \[ \] |  |
| SLD-BIO-120 Coenzima Q10 | \[ \] |  |
| SLD-BIO-121 TIBC | \[ \] |  |
| SLD-BIO-122 HCM | \[ \] |  |
| SLD-BIO-123 Neutrófilos % | \[ \] |  |

- Nombre y registro ReTHUS:
- Fecha:

## Lo que el médico debe mirar con más cuidado

1. Que la vitamina A baja con hs-CRP mayor de 5 no se lea como déficit.
2. La regla de no recomendar hojas verdes a personas con warfarina (vitamina K1).
3. La decisión de mostrar la niacina siempre solo como valor, aunque haya intervalo.
4. Los cortes del índice omega-3 (8 % y 4 %), que solo aparecen en la vista médica.
5. La nota de neutropenia étnica benigna en el porcentaje de neutrófilos.