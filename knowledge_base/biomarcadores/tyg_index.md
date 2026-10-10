---
doc_id: "SLD-BIO-141"
biomarker_id: "tyg_index"
name_es: "Índice triglicéridos-glucosa (TyG)"
name_en: "Triglyceride-glucose index"
abbreviation: "TyG"
sinonimos: ["Índice TyG", "TyG", "Índice triglicéridos-glucosa", "Triglyceride-glucose index"]
category: "Metabolismo"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
formula: "ln(triglicéridos (mg/dL) × glucosa (mg/dL) / 2)"
entradas: ["triglycerides", "glucose"]
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

# SLD-BIO-141 · Índice triglicéridos-glucosa (TyG)

## A. Identificación
Marcador de resistencia a la insulina que no necesita medir la insulina.

## B. Definición
Se desarrolló y validó en población latinoamericana (México) frente al clamp euglucémico.

## C. Cálculo y condiciones
Solo con ayuno de 8 horas o más y con triglicéridos y glucosa medidos.

## D. Intervalos y umbrales
Corte provisional de 8,8 (por verificar con Guerrero-Romero 2010 y estudios en población colombiana).

## E. Interpretación
Apoyo de la resistencia a la insulina (COND-M1-EM-A04), junto al HOMA-IR. No crea una condición del paciente por sí solo.

## F. Contexto del paciente y confusores
Ayuno insuficiente, diabetes en tratamiento, triglicéridos muy altos por alcohol.

## G. Relaciones
HOMA-IR, relación TG/HDL, glucosa, triglicéridos.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Simental-Mendía 2008; Guerrero-Romero 2010. Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un índice calculado con tus triglicéridos y tu glucosa sugiere que tu cuerpo usa la insulina con más esfuerzo".
- Inferencias prohibidas: "tienes diabetes".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [metabolismo, calculado, resistencia_insulina, saludly_brain_v1]
use_when: ["resistencia a la insulina"]
combine_with: [homa_ir, tg_hdl_ratio]
do_not_use_alone: [tyg_index]
do_not_conclude: []
escalate_when: []
```
