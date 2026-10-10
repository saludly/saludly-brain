---
doc_id: "SLD-BIO-135"
biomarker_id: "abo_rh"
name_es: "Grupo sanguíneo ABO y factor Rh"
name_en: "ABO blood group and Rh factor"
abbreviation: "ABO/Rh"
sinonimos: ["Grupo sanguíneo", "Hemoclasificación", "Grupo sanguíneo y Rh", "Hemoclasificación ABO y Rh", "Grupo ABO", "Factor Rh", "ABO/Rh"]
category: "Hematología"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo"
unidad_canonica: "grupo (A, B, AB, O) y Rh (positivo o negativo)"
specimen: "Sangre total EDTA"
nivel_catalogo: "dato (sin condición)"
panel: "estándar, una sola vez"
alimenta: []
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-135 · Grupo sanguíneo ABO y factor Rh

## A. Identificación
Clasificación de los glóbulos rojos según los antígenos A, B y D (Rh).

## B. Definición
Es un dato de identificación útil para el paciente (donación, embarazo, transfusiones). No es una medida de salud.

## C. Espécimen y toma
Sangre total EDTA. Se hace una sola vez en la vida del paciente en Saludly: si ya está registrado, no se repite.

## D. Intervalos y umbrales
No tiene intervalo. Resultado: A, B, AB u O, y Rh positivo o negativo.

## E. Interpretación
Se muestra al paciente como dato. No alimenta condiciones ni cambia escalamientos.

## F. Contexto del paciente y confusores
Ninguno relevante para Saludly.

## G. Relaciones
Ninguna.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Práctica estándar de banco de sangre.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "tu grupo sanguíneo es…".
- Inferencias prohibidas: "tu grupo sanguíneo indica riesgo de…", recomendaciones de dieta por grupo sanguíneo.
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, dato, saludly_brain_v1]
use_when: ["el paciente pregunta por su grupo sanguíneo"]
combine_with: []
do_not_use_alone: [abo_rh]
do_not_conclude: []
escalate_when: []
```
