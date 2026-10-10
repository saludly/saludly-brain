---
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
---

# SLD-BIO-124 · Aldosterona

## A. Identificación
Hormona suprarrenal que retiene sodio y elimina potasio. Se mide por inmunoensayo o por espectrometría de masas (LC-MS/MS); el método cambia los cortes.

## B. Definición
En el hiperaldosteronismo primario, la suprarrenal produce aldosterona de forma autónoma y la renina queda suprimida. Es una causa frecuente y tratable de presión alta.

## C. Espécimen y toma
En la mañana, sentado, sin restricción de sal en los días previos. El potasio se mide en la misma toma, porque un potasio bajo puede bajar falsamente la aldosterona.

## D. Intervalos y umbrales (Endocrine Society 2025)
- Aldosterona compatible con hiperaldosteronismo primario, con renina suprimida: **10 ng/dL o más (277 pmol/L o más) por inmunoensayo**, o **7,5 ng/dL o más (208 pmol/L o más) por LC-MS/MS**.
- Zona para repetir: renina suprimida con aldosterona de **5 a 10 ng/dL** por inmunoensayo.
- Forma evidente: aldosterona mayor de 20 ng/dL por inmunoensayo (mayor de 15 por LC-MS/MS) con renina muy suprimida.
- La guía advierte que estos valores son orientativos y pide preferir los cortes del laboratorio local cuando existan.

## E. Interpretación
Nunca se interpreta sola: siempre con la renina y la relación aldosterona/renina (ficha de renina).

## F. Contexto del paciente y confusores
Potasio bajo (baja la aldosterona: falso negativo), enfermedad renal crónica (puede subirla), espironolactona, eplerenona y diuréticos.

## G. Relaciones
Renina, potasio, presión arterial (M1 CA-006, M2 NE-A01).

## H. Tendencias
Varía en el día y con la postura; por eso la toma estandarizada.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Prueba de supresión de aldosterona, tomografía suprarrenal y muestreo venoso suprarrenal, según el especialista.

## K. Cuándo no interpretar / cuándo escalar
Sin renina de la misma muestra: no interpretable. Escala según TI-008.

## L. Evidencia
Endocrine Society 2025, hiperaldosteronismo primario (recomendación 3 y sus notas técnicas), leído en endocrine.org.

## M. Seguridad para Saludly Brain
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
