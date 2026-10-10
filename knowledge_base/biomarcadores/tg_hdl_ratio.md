---
doc_id: "SLD-BIO-142"
biomarker_id: "tg_hdl_ratio"
name_es: "Relación triglicéridos/HDL"
name_en: "Triglyceride to HDL ratio"
abbreviation: "TG/HDL"
sinonimos: ["Relación TG/HDL", "TG/HDL", "Triglicéridos/HDL", "Triglyceride/HDL ratio"]
category: "Metabolismo"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad (con valores en mg/dL)"
formula: "triglicéridos (mg/dL) / HDL (mg/dL)"
entradas: ["triglycerides", "hdl_c"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor y rango (apoyo de condiciones)"
panel: "calculado, todas las personas"
alimenta: ["COND-M1-EM-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-142 · Relación triglicéridos/HDL

## A. Identificación
Cociente simple asociado a resistencia a la insulina y a LDL pequeña y densa.

## B. Definición
Útil cuando no se mide la insulina; su corte varía según la población.

## C. Cálculo y condiciones
Solo con ayuno de 8 horas o más.

## D. Intervalos y umbrales
Corte provisional de 3,0 (McLaughlin 2003); en población hispana puede ser menor (por verificar).

## E. Interpretación
Apoyo de COND-M1-EM-A04.

## F. Contexto del paciente y confusores
Ayuno insuficiente, alcohol.

## G. Relaciones
TyG, HOMA-IR, perfil lipídico.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
McLaughlin 2003. Pendiente de verificar en población hispana.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "la relación entre tus triglicéridos y tu colesterol bueno sugiere resistencia a la insulina".
- Inferencias prohibidas: "tienes diabetes".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [metabolismo, calculado, resistencia_insulina, saludly_brain_v1]
use_when: ["resistencia a la insulina"]
combine_with: [tyg_index, homa_ir]
do_not_use_alone: [tg_hdl_ratio]
do_not_conclude: []
escalate_when: []
```
