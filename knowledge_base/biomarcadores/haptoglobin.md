---
doc_id: "SLD-BIO-139"
biomarker_id: "haptoglobin"
name_es: "Haptoglobina"
name_en: "Haptoglobin"
abbreviation: "Hp"
sinonimos: ["Haptoglobina", "Hp", "Haptoglobin"]
category: "Hematología"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "mg/dL"
activa_si: ["anemia con reticulocitos altos y bilirrubina indirecta o LDH altas (REL-009)"]
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
alimenta: ["REL-009"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-139 · Haptoglobina

## A. Identificación
Proteína que captura la hemoglobina libre en la sangre.

## B. Definición
Baja cuando los glóbulos rojos se destruyen dentro de los vasos (hemólisis).

## C. Espécimen y toma
Suero retenido de la misma toma.

## D. Intervalos y umbrales
Se usa el intervalo del laboratorio. Baja: por debajo del límite inferior.

## E. Interpretación
Refuerza el patrón de hemólisis (REL-009). Es una proteína de fase aguda: la inflamación la sube y puede ocultar una hemólisis.

## F. Contexto del paciente y confusores
Inflamación (sube), enfermedad hepática (baja), estrógenos.

## G. Relaciones
Hemoglobina, reticulocitos, bilirrubina indirecta, LDH.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Prueba de Coombs y frotis (los decide el médico).

## K. Cuándo no interpretar / cuándo escalar
Baja con anemia: se suma al escalamiento del patrón de hemólisis.

## L. Evidencia
Práctica hematológica estándar. Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un examen apoya la idea de que tus glóbulos rojos se están destruyendo más rápido".
- Inferencias prohibidas: "tienes anemia hemolítica autoinmune".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, refleja, hemolisis, saludly_brain_v1]
use_when: ["sospecha de hemólisis"]
combine_with: [hemoglobin, reticulocytes_pct, bilirubin_total, ldh]
do_not_use_alone: [haptoglobin]
do_not_conclude: []
escalate_when: []
```
