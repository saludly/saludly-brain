---
doc_id: "SLD-BIO-143"
biomarker_id: "mentzer_index"
name_es: "Índice de Mentzer"
name_en: "Mentzer index"
abbreviation: "Mentzer"
sinonimos: ["Índice de Mentzer", "Mentzer", "VCM/eritrocitos", "Mentzer index"]
category: "Hematología"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
formula: "VCM (fL) / eritrocitos (millones/µL)"
entradas: ["mcv", "erythrocytes"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor y rango (apoyo de condiciones)"
panel: "calculado, todas las personas"
alimenta: ["COND-M3-HE-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-143 · Índice de Mentzer

## A. Identificación
Cociente que ayuda a separar el déficit de hierro del rasgo talasémico cuando los glóbulos rojos son pequeños.

## B. Definición
Menor de 13 sugiere rasgo talasémico; mayor de 13, déficit de hierro.

## C. Cálculo y condiciones
Solo se calcula con VCM bajo (menor de 80 fL).

## D. Intervalos y umbrales
Corte: 13 (Mentzer 1973).

## E. Interpretación
Lo usa COND-M3-HE-A04. Nunca confirma: la confirmación es la electroforesis de hemoglobina.

## F. Contexto del paciente y confusores
Déficit de hierro y rasgo talasémico juntos.

## G. Relaciones
VCM, eritrocitos, RDW, ferritina.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Electroforesis de hemoglobina (refleja).

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Mentzer 1973. Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un cálculo con tus glóbulos rojos sugiere estudiar un rasgo heredado".
- Inferencias prohibidas: "tienes talasemia".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, calculado, talasemia, saludly_brain_v1]
use_when: ["microcitosis"]
combine_with: [mcv, erythrocytes, ferritin]
do_not_use_alone: [mentzer_index]
do_not_conclude: []
escalate_when: []
```
