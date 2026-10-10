---
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
---

# SLD-BIO-125 · Renina (actividad o concentración)

## A. Identificación
Enzima del riñón que regula la producción de aldosterona. El laboratorio reporta actividad (ARP, en ng/mL/h) o concentración directa (DRC, en mU/L); la ficha guarda cuál de las dos.

## B. Definición
La renina suprimida es el sello del hiperaldosteronismo primario.

## C. Espécimen y toma
Igual que aldosterona: mañana, sentado, sin restricción de sal. La muestra para renina no se refrigera antes de separar el plasma (el frío activa la prorrenina y falsea la concentración).

## D. Intervalos y umbrales (Endocrine Society 2025)
- Renina suprimida: **ARP de 1 ng/mL/h o menos**, o **DRC de 8,2 mU/L o menos**.
- Relación aldosterona/renina elevada (aldosterona por inmunoensayo): **mayor de 20** si es aldosterona en ng/dL sobre ARP en ng/mL/h, o **mayor de 70** si es aldosterona en pmol/L sobre DRC en mU/L. Con aldosterona por LC-MS/MS, el corte de la relación es cerca de 25 % más bajo.
- Tamizaje positivo: renina suprimida **y** aldosterona inapropiadamente alta (ficha de aldosterona) **y** relación elevada.

## E. Interpretación
Renina suprimida sin aldosterona alta no es positivo. Renina alta con presión alta orienta a otras causas (por ejemplo, estenosis de la arteria renal) y la lee el médico.

## F. Contexto del paciente y confusores
- Suben la renina (falso negativo): IECA, ARA II, diuréticos, espironolactona y eplerenona.
- Bajan la renina (falso positivo): betabloqueadores, clonidina y metildopa. Con betabloqueador, un positivo con aldosterona de 10 a 15 ng/dL por inmunoensayo puede ser falso.
- Enfermedad renal crónica: la renina baja y aumentan los falsos positivos.

## G. Relaciones
Aldosterona, potasio, TFG, presión arterial.

## H. Tendencias
Si el primer tamizaje es negativo, la guía sugiere repetirlo ante hipertensión resistente, potasio bajo nuevo o fibrilación auricular sin causa.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Las de la aldosterona.

## K. Cuándo no interpretar / cuándo escalar
Sin tipo de renina declarado (ARP o DRC): no interpretable. Escala según TI-008.

## L. Evidencia
Endocrine Society 2025, hiperaldosteronismo primario, leído en endocrine.org.

## M. Seguridad para Saludly Brain
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
