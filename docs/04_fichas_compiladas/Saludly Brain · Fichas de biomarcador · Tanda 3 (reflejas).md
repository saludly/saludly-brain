# Fichas de biomarcador · Tanda 3 — Pruebas reflejas

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Esta tanda crea las fichas base de las 7 pruebas reflejas que no tenían ficha: aldosterona, renina, ARN de hepatitis C, segunda ELISA de Chagas, macroprolactina, PSA libre y ácido metilmalónico. El laboratorio solo las corre cuando un resultado del panel las activa, sobre la misma muestra y sin que el paciente haga nada más.

Usa el esquema 2.1 de las tandas anteriores.

## Fuente verificada en esta tanda

Para aldosterona y renina se leyó el resumen oficial de recomendaciones de la guía de hiperaldosteronismo primario de la Endocrine Society (julio de 2025), publicado en endocrine.org. De ahí salen los cortes de esas dos fichas, que también completan la ficha de condición COND-M2-TI-008, que había quedado sin números. Es la primera fuente de esta serie leída directamente en la página de la sociedad que la emite; el texto completo de la guía en la revista sigue pendiente.

Las demás fichas de la tanda siguen con `fuentes_estado: "por verificar"`.

## Índice

| doc_id | biomarker_id | Prueba refleja | Se activa cuando | Alimenta |
| --- | --- | --- | --- | --- |
| SLD-BIO-124 | aldosterone | Aldosterona | Presión de 130/80 o más, o hipertensión conocida | M2 TI-008 |
| SLD-BIO-125 | renin | Renina (actividad o concentración) | Igual que aldosterona | M2 TI-008 |
| SLD-BIO-126 | hcv_rna | ARN del virus de la hepatitis C | Anti-VHC reactivo | M4 IN-001 |
| SLD-BIO-127 | chagas_elisa_recombinante | Segunda ELISA de Chagas (antígenos recombinantes) | Primera ELISA reactiva | M4 IN-003 |
| SLD-BIO-128 | macroprolactin | Macroprolactina | Prolactina alta | M5 MU-003 |
| SLD-BIO-129 | psa_free | PSA libre | PSA total entre 4 y 10 ng/mL | M5 UR-A02 |
| SLD-BIO-130 | methylmalonic_acid | Ácido metilmalónico | B12 entre 180 y 350 pg/mL | M3 NU-001, HE-004 |

---

## SLD-BIO-124 · Aldosterona

```yaml
doc_id: "SLD-BIO-124"
biomarker_id: "aldosterone"
name_es: "Aldosterona sérica o plasmática"
name_en: "Serum or plasma aldosterone"
abbreviation: "ALDO"
sinonimos: ["Aldosterona", "Aldosterona sérica", "Aldosterona plasmática", "PAC", "Aldosterone"]
category: "Suprarrenal"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/dL"
conversion: "ng/dL x 27,7 = pmol/L"
specimen: "Suero o plasma, en la mañana, sentado"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["COND-M1-CA-006 activa (presión de 130/80 o más)", "hipertensión conocida declarada"]
alimenta: ["COND-M2-TI-008"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "parcial: recomendaciones de Endocrine Society 2025 leídas en endocrine.org; texto completo pendiente"
```

### A. Identificación

Hormona suprarrenal que retiene sodio y elimina potasio. Se mide por inmunoensayo o por espectrometría de masas (LC-MS/MS); el método cambia los cortes.

### B. Definición

En el hiperaldosteronismo primario, la suprarrenal produce aldosterona de forma autónoma y la renina queda suprimida. Es una causa frecuente y tratable de presión alta.

### C. Espécimen y toma

En la mañana, sentado, sin restricción de sal en los días previos. El potasio se mide en la misma toma, porque un potasio bajo puede bajar falsamente la aldosterona.

### D. Intervalos y umbrales (Endocrine Society 2025)

- Aldosterona compatible con hiperaldosteronismo primario, con renina suprimida: **10 ng/dL o más (277 pmol/L o más) por inmunoensayo**, o **7,5 ng/dL o más (208 pmol/L o más) por LC-MS/MS**.
- Zona para repetir: renina suprimida con aldosterona de **5 a 10 ng/dL** por inmunoensayo.
- Forma evidente: aldosterona mayor de 20 ng/dL por inmunoensayo (mayor de 15 por LC-MS/MS) con renina muy suprimida.
- La guía advierte que estos valores son orientativos y pide preferir los cortes del laboratorio local cuando existan.

### E. Interpretación

Nunca se interpreta sola: siempre con la renina y la relación aldosterona/renina (ficha de renina).

### F. Contexto del paciente y confusores

Potasio bajo (baja la aldosterona: falso negativo), enfermedad renal crónica (puede subirla), espironolactona, eplerenona y diuréticos.

### G. Relaciones

Renina, potasio, presión arterial (M1 CA-006, M2 NE-A01).

### H. Tendencias

Varía en el día y con la postura; por eso la toma estandarizada.

### I. Prevención

No aplica.

### J. Pruebas complementarias

Prueba de supresión de aldosterona, tomografía suprarrenal y muestreo venoso suprarrenal, según el especialista.

### K. Cuándo no interpretar / cuándo escalar

Sin renina de la misma muestra: no interpretable. Escala según TI-008.

### L. Evidencia

Endocrine Society 2025, hiperaldosteronismo primario (recomendación 3 y sus notas técnicas), leído en endocrine.org.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "patrón de aldosterona y renina que conviene revisar con el médico".
- Inferencias prohibidas: hiperaldosteronismo, tumor suprarrenal, suspender medicamentos.
- Revisión profesional: todo resultado.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [suprarrenal, hipertension, aldosterona, refleja, saludly_brain_v1]
use_when: ["tamizaje de hiperaldosteronismo en hipertensión"]
combine_with: [renin, potassium]
do_not_use_alone: ["interpretar sin renina"]
do_not_conclude: ["hiperaldosteronismo primario", "adenoma suprarrenal"]
escalate_when: ["tamizaje positivo según COND-M2-TI-008"]
```

---

## SLD-BIO-125 · Renina (actividad o concentración)

```yaml
doc_id: "SLD-BIO-125"
biomarker_id: "renin"
name_es: "Renina plasmática (actividad o concentración directa)"
name_en: "Plasma renin (activity or direct concentration)"
abbreviation: "ARP / DRC"
sinonimos: ["Renina", "Actividad de renina plasmática", "ARP", "PRA", "Renina directa", "Concentración directa de renina", "DRC"]
category: "Suprarrenal"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL/h (actividad) o mU/L (concentración); se guarda con su tipo"
specimen: "Plasma EDTA, en la mañana, sentado, sin refrigerar antes de separar"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["COND-M1-CA-006 activa (presión de 130/80 o más)", "hipertensión conocida declarada"]
alimenta: ["COND-M2-TI-008"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "parcial: recomendaciones de Endocrine Society 2025 leídas en endocrine.org; texto completo pendiente"
```

### A. Identificación

Enzima del riñón que regula la producción de aldosterona. El laboratorio reporta actividad (ARP, en ng/mL/h) o concentración directa (DRC, en mU/L); la ficha guarda cuál de las dos.

### B. Definición

La renina suprimida es el sello del hiperaldosteronismo primario.

### C. Espécimen y toma

Igual que aldosterona: mañana, sentado, sin restricción de sal. La muestra para renina no se refrigera antes de separar el plasma (el frío activa la prorrenina y falsea la concentración).

### D. Intervalos y umbrales (Endocrine Society 2025)

- Renina suprimida: **ARP de 1 ng/mL/h o menos**, o **DRC de 8,2 mU/L o menos**.
- Relación aldosterona/renina elevada (aldosterona por inmunoensayo): **mayor de 20** si es aldosterona en ng/dL sobre ARP en ng/mL/h, o **mayor de 70** si es aldosterona en pmol/L sobre DRC en mU/L. Con aldosterona por LC-MS/MS, el corte de la relación es cerca de 25 % más bajo.
- Tamizaje positivo: renina suprimida **y** aldosterona inapropiadamente alta (ficha de aldosterona) **y** relación elevada.

### E. Interpretación

Renina suprimida sin aldosterona alta no es positivo. Renina alta con presión alta orienta a otras causas (por ejemplo, estenosis de la arteria renal) y la lee el médico.

### F. Contexto del paciente y confusores

- Suben la renina (falso negativo): IECA, ARA II, diuréticos, espironolactona y eplerenona.
- Bajan la renina (falso positivo): betabloqueadores, clonidina y metildopa. Con betabloqueador, un positivo con aldosterona de 10 a 15 ng/dL por inmunoensayo puede ser falso.
- Enfermedad renal crónica: la renina baja y aumentan los falsos positivos.

### G. Relaciones

Aldosterona, potasio, TFG, presión arterial.

### H. Tendencias

Si el primer tamizaje es negativo, la guía sugiere repetirlo ante hipertensión resistente, potasio bajo nuevo o fibrilación auricular sin causa.

### I. Prevención

No aplica.

### J. Pruebas complementarias

Las de la aldosterona.

### K. Cuándo no interpretar / cuándo escalar

Sin tipo de renina declarado (ARP o DRC): no interpretable. Escala según TI-008.

### L. Evidencia

Endocrine Society 2025, hiperaldosteronismo primario, leído en endocrine.org.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "patrón que conviene revisar con el médico; es una causa tratable de presión alta".
- Inferencias prohibidas: suspender medicamentos, nombrar la enfermedad.
- Revisión profesional: todo resultado.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [suprarrenal, hipertension, renina, refleja, saludly_brain_v1]
use_when: ["tamizaje de hiperaldosteronismo en hipertensión"]
combine_with: [aldosterone, potassium, egfr]
do_not_use_alone: ["diagnóstico"]
do_not_conclude: ["hiperaldosteronismo primario", "estenosis de la arteria renal"]
escalate_when: ["tamizaje positivo según COND-M2-TI-008"]
```

---

## SLD-BIO-126 · ARN del virus de la hepatitis C

```yaml
doc_id: "SLD-BIO-126"
biomarker_id: "hcv_rna"
name_es: "ARN del virus de la hepatitis C"
name_en: "Hepatitis C virus RNA"
abbreviation: "ARN VHC"
sinonimos: ["ARN VHC", "Carga viral hepatitis C", "HCV RNA", "PCR hepatitis C", "Viremia VHC"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (detectable / no detectable) o cuantitativo"
unidad_canonica: "UI/mL"
specimen: "Suero o plasma de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["anti_hcv reactivo"]
alimenta: ["COND-M4-IN-001"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Prueba molecular (PCR) que detecta el material genético del virus.

### B. Definición

Es la prueba que confirma si una infección por hepatitis C está activa.

### C. Espécimen y toma

Suero o plasma; el laboratorio debe separar y conservar la muestra según el método molecular.

### D. Intervalos y umbrales

Detectable o no detectable según el límite del método. Si es cuantitativa, se reporta en UI/mL.

### E. Interpretación

Detectable: infección activa. No detectable con anti-VHC reactivo: infección resuelta o falso positivo del anticuerpo.

### F. Contexto del paciente y confusores

Tratamiento antiviral previo, muestra mal conservada (falso no detectable).

### G. Relaciones

Anti-VHC, ALT, FIB-4 (M4).

### H. Tendencias

Se usa para confirmar curación tras tratamiento, según el médico.

### I. Prevención

Tratamiento curativo; no compartir objetos con sangre.

### J. Pruebas complementarias

Genotipo y evaluación de fibrosis, según el médico.

### K. Cuándo no interpretar / cuándo escalar

Siempre con llamada del médico (IN-001).

### L. Evidencia

Lineamiento de hepatitis C del Ministerio de Salud. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "el virus está activo o no está activo".
- Inferencias prohibidas: cirrosis, incurable.
- Revisión profesional: todo resultado.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_c, molecular, refleja, saludly_brain_v1]
use_when: ["anti-VHC reactivo"]
combine_with: [anti_hcv, alt]
do_not_use_alone: []
do_not_conclude: ["cirrosis"]
escalate_when: ["cualquier resultado"]
```

---

## SLD-BIO-127 · Segunda ELISA de Chagas (antígenos recombinantes)

```yaml
doc_id: "SLD-BIO-127"
biomarker_id: "chagas_elisa_recombinante"
name_es: "ELISA de Trypanosoma cruzi con antígenos recombinantes"
name_en: "Trypanosoma cruzi recombinant antigen ELISA"
abbreviation: "ELISA Chagas recombinante"
sinonimos: ["ELISA recombinante Chagas", "Segunda ELISA Chagas", "Chagas antígenos recombinantes", "T. cruzi ELISA recombinante"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["chagas_elisa_total reactivo"]
alimenta: ["COND-M4-IN-003"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Segunda prueba del algoritmo serológico, con antígenos distintos a los de la primera ELISA.

### B. Definición

El diagnóstico serológico de Chagas exige dos pruebas con antígenos o principios distintos; esta es la segunda.

### C. Espécimen y toma

Suero de la misma muestra.

### D. Intervalos y umbrales

Reactivo o no reactivo según el fabricante.

### E. Interpretación

Las dos reactivas: probable infección crónica. Discordantes: se necesita una tercera prueba y el informe queda en espera.

### F. Contexto del paciente y confusores

Reacción cruzada con *Leishmania*.

### G. Relaciones

Primera ELISA (SLD-BIO-109).

### H. Tendencias

No aplica.

### I. Prevención

La de la ficha de la primera ELISA.

### J. Pruebas complementarias

Tercera prueba en discordancia; evaluación cardíaca si las dos son reactivas.

### K. Cuándo no interpretar / cuándo escalar

Las dos reactivas: escalamiento 2 con llamada (IN-003).

### L. Evidencia

Algoritmo de Chagas del Ministerio de Salud; lineamiento del INS para adultos pendiente.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "segunda prueba para Chagas reactiva o no reactiva".
- Inferencias prohibidas: daño cardíaco, mortal.
- Revisión profesional: todo resultado.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, chagas, serologia, refleja, saludly_brain_v1]
use_when: ["primera ELISA de Chagas reactiva"]
combine_with: [chagas_elisa_total]
do_not_use_alone: []
do_not_conclude: ["cardiopatía chagásica"]
escalate_when: ["dos ELISA reactivas", "resultados discordantes"]
```

---

## SLD-BIO-128 · Macroprolactina

```yaml
doc_id: "SLD-BIO-128"
biomarker_id: "macroprolactin"
name_es: "Macroprolactina (prolactina tras precipitación con PEG)"
name_en: "Macroprolactin (post-PEG prolactin)"
abbreviation: "MacroPRL"
sinonimos: ["Macroprolactina", "Prolactina post PEG", "Prolactina monomérica", "Recuperación de prolactina tras PEG"]
category: "Hipófisis"
parameter_type: "measured_analyte"
tipo_resultado: "numérico (porcentaje de recuperación y prolactina monomérica)"
unidad_canonica: "% de recuperación; prolactina monomérica en ng/mL"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja, mujeres"
activa_si: ["prolactin > límite superior"]
alimenta: ["COND-M5-MU-003"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

El laboratorio precipita la muestra con polietilenglicol (PEG) y vuelve a medir la prolactina. Lo que queda es la prolactina monomérica, la forma activa.

### B. Definición

La macroprolactina es prolactina unida a anticuerpos: el análisis la cuenta, pero casi no tiene efecto en el cuerpo. Explica una parte de las prolactinas altas sin síntomas.

### C. Espécimen y toma

Suero de la misma toma.

### D. Intervalos y umbrales

Corte del laboratorio para la recuperación tras PEG. En la literatura, una recuperación menor de 40 % suele indicar predominio de macroprolactina y mayor de 60 % predominio de prolactina monomérica; la zona intermedia se interpreta con la prolactina monomérica frente al intervalo del laboratorio.

### E. Interpretación

Predominio de macroprolactina: hallazgo sin significado clínico habitual (escalamiento 0). Predominio monomérico: la prolactina alta es real y sigue la ficha MU-003.

### F. Contexto del paciente y confusores

Medicamentos que suben la prolactina, embarazo y lactancia (no se interpreta).

### G. Relaciones

Prolactina, TSH, TFG (M2, M5).

### H. Tendencias

La macroprolactinemia suele persistir sin cambios.

### I. Prevención

No aplica.

### J. Pruebas complementarias

Según el médico, si la prolactina monomérica está alta.

### K. Cuándo no interpretar / cuándo escalar

No escala por sí sola; sigue MU-003.

### L. Evidencia

Endocrine Society 2011 y Febrasgo-SBEM 2024 (citadas en el Lote 5). Cortes de recuperación por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "la mayor parte de tu prolactina es una forma que normalmente no tiene efecto".
- Inferencias prohibidas: tumor de hipófisis.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hipofisis, prolactina, refleja, saludly_brain_v1]
use_when: ["prolactina alta"]
combine_with: [prolactin, tsh]
do_not_use_alone: []
do_not_conclude: ["prolactinoma"]
escalate_when: []
```

---

## SLD-BIO-129 · PSA libre

```yaml
doc_id: "SLD-BIO-129"
biomarker_id: "psa_free"
name_es: "Antígeno prostático específico libre"
name_en: "Free prostate-specific antigen"
abbreviation: "PSA libre"
sinonimos: ["PSA libre", "fPSA", "Antígeno prostático libre", "PSA L"]
category: "Salud del hombre"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
calculo_asociado: "porcentaje de PSA libre = PSA libre / PSA total x 100"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja, hombres"
activa_si: ["psa_total entre 4,0 y 10,0 ng/mL"]
alimenta: ["COND-M5-UR-A02"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Fracción del PSA que circula sin unirse a proteínas.

### B. Definición

En la zona gris del PSA total, un porcentaje de PSA libre bajo se asocia a mayor probabilidad de cáncer y uno alto a causas benignas.

### C. Espécimen y toma

Suero de la misma toma, procesado pronto: el PSA libre es menos estable que el total.

### D. Intervalos y umbrales

El corte del porcentaje está pendiente de fuente en el Lote 5. Valores habituales en la literatura: menor de 10 % (mayor probabilidad) y mayor de 25 % (menor probabilidad). Sin firma médica, la ficha UR-A02 solo muestra el porcentaje.

### E. Interpretación

Solo en la vista médica; no cambia el texto del paciente.

### F. Contexto del paciente y confusores

Los mismos del PSA total; demora en el procesamiento baja el PSA libre.

### G. Relaciones

PSA total (SLD-BIO-110).

### H. Tendencias

No aplica.

### I. Prevención

No aplica.

### J. Pruebas complementarias

Las del PSA total.

### K. Cuándo no interpretar / cuándo escalar

No escala por sí solo.

### L. Evidencia

Pendiente de fuente.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "dato de apoyo para tu médico".
- Inferencias prohibidas: probabilidad de cáncer en el texto del paciente.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [salud_hombre, prostata, refleja, saludly_brain_v1]
use_when: ["PSA total en zona gris"]
combine_with: [psa_total]
do_not_use_alone: []
do_not_conclude: ["cáncer de próstata"]
escalate_when: []
```

---

## SLD-BIO-130 · Ácido metilmalónico

```yaml
doc_id: "SLD-BIO-130"
biomarker_id: "methylmalonic_acid"
name_es: "Ácido metilmalónico sérico"
name_en: "Serum methylmalonic acid"
abbreviation: "AMM"
sinonimos: ["Ácido metilmalónico", "AMM", "MMA", "Methylmalonic acid"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µmol/L"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["vitamin_b12 entre 180 y 350 pg/mL"]
alimenta: ["COND-M3-NU-001", "COND-M3-HE-004"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Metabolito que se acumula cuando falta B12 dentro de las células. Se mide por LC-MS/MS.

### B. Definición

Es un marcador funcional: muestra si la B12 alcanza a hacer su trabajo, más allá del valor total en sangre.

### C. Espécimen y toma

Suero de la misma toma.

### D. Intervalos y umbrales

Intervalo del laboratorio (en el PDF de ejemplo, 0,00 a 0,40 µmol/L).

### E. Interpretación

Alto con B12 indeterminada: déficit funcional de B12 (NU-001). Normal: la B12 indeterminada no se interpreta como déficit.

### F. Contexto del paciente y confusores

Función renal baja (sube el ácido metilmalónico sin déficit de B12), edad avanzada, deshidratación.

### G. Relaciones

B12, homocisteína, TFG (M2, M3).

### H. Tendencias

Baja al corregir el déficit.

### I. Prevención

La de la B12.

### J. Pruebas complementarias

Homocisteína (en el panel).

### K. Cuándo no interpretar / cuándo escalar

Con TFG menor de 60: interpretar con cautela y anotarlo en la vista médica.

### L. Evidencia

NICE NG239 2024. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "confirma o descarta un déficit funcional de B12".
- Inferencias prohibidas: anemia perniciosa.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, b12, marcador_funcional, refleja, saludly_brain_v1]
use_when: ["B12 entre 180 y 350"]
combine_with: [vitamin_b12, homocysteine, egfr]
do_not_use_alone: []
do_not_conclude: ["anemia perniciosa"]
escalate_when: []
```

---

## Firma médica de la tanda

| Ficha | Aprobada | Cambios |
| --- | --- | --- |
| SLD-BIO-124 Aldosterona | \[ \] |  |
| SLD-BIO-125 Renina | \[ \] |  |
| SLD-BIO-126 ARN VHC | \[ \] |  |
| SLD-BIO-127 ELISA Chagas recombinante | \[ \] |  |
| SLD-BIO-128 Macroprolactina | \[ \] |  |
| SLD-BIO-129 PSA libre | \[ \] |  |
| SLD-BIO-130 Ácido metilmalónico | \[ \] |  |

- Nombre y registro ReTHUS:
- Fecha:

## Lo que el médico debe mirar con más cuidado

1. Los cortes de aldosterona, renina y relación aldosterona/renina de la Endocrine Society 2025, y si el laboratorio aliado tiene cortes locales, que la guía prefiere.
2. El manejo de medicamentos que alteran la renina, sin pedirle al paciente suspender nada.
3. Los cortes de recuperación de macroprolactina tras PEG.
4. Los cortes del porcentaje de PSA libre, todavía pendientes de fuente.
5. La cautela con el ácido metilmalónico cuando la TFG está baja.