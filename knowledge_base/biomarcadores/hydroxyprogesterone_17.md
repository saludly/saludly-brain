---
doc_id: "SLD-BIO-138"
biomarker_id: "hydroxyprogesterone_17"
name_es: "17-hidroxiprogesterona"
name_en: "17-hydroxyprogesterone"
abbreviation: "17-OHP"
sinonimos: ["17-hidroxiprogesterona", "17-OH progesterona", "17 OH progesterona", "Hidroxiprogesterona 17 alfa", "17-OHP", "17-hydroxyprogesterone"]
category: "Endocrinología"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
activa_si: ["andrógenos altos (COND-M5-MU-001)"]
specimen: "Suero de la misma toma, de la mañana"
nivel_catalogo: "refleja"
panel: "refleja, mujeres"
alimenta: ["REL-028"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-138 · 17-hidroxiprogesterona

## A. Identificación
Precursor de la producción de cortisol en la glándula suprarrenal.

## B. Definición
Alta en la hiperplasia suprarrenal congénita no clásica, que imita al síndrome de ovario poliquístico.

## C. Espécimen y toma
Suero de la toma de la mañana; idealmente en fase folicular.

## D. Intervalos y umbrales
Se usa el intervalo del laboratorio. Corte de sospecha propuesto: mayor de 2 ng/mL en fase folicular (por verificar).

## E. Interpretación
Descarta la hiperplasia suprarrenal no clásica antes de hablar de SOP, como pide la guía internacional de SOP 2023.

## F. Contexto del paciente y confusores
Fase lútea (sube), embarazo, toma en la tarde.

## G. Relaciones
Testosterona total, SHBG, índice de andrógenos libres, DHEA-S.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Prueba de estimulación con ACTH (la decide el médico).

## K. Cuándo no interpretar / cuándo escalar
Valor alto: revisión médica.

## L. Evidencia
Guía internacional de SOP 2023 (Teede et al.). Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un examen hormonal sirve para descartar otra causa de tus andrógenos altos".
- Inferencias prohibidas: "tienes hiperplasia suprarrenal".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [mujer, refleja, sop, saludly_brain_v1]
use_when: ["andrógenos altos en mujeres"]
combine_with: [testosterone_total, shbg, dhea_s]
do_not_use_alone: [hydroxyprogesterone_17]
do_not_conclude: []
escalate_when: []
```
