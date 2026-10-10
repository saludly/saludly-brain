---
doc_id: "SLD-BIO-136"
biomarker_id: "hb_electrophoresis"
name_es: "Electroforesis de hemoglobina"
name_en: "Hemoglobin electrophoresis"
abbreviation: "EF Hb"
sinonimos: ["Electroforesis de hemoglobina", "Electroforesis alcalina de hemoglobina", "Hemoglobina A2", "HbA2", "Fraccionamiento de hemoglobinas", "Hb electrophoresis"]
category: "Hematología"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo con fracciones (%)"
unidad_canonica: "% por fracción (HbA, HbA2, HbF y variantes)"
activa_si: ["VCM bajo con ferritina normal e índice de Mentzer menor de 13"]
specimen: "Sangre total EDTA de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
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

# SLD-BIO-136 · Electroforesis de hemoglobina

## A. Identificación
Separa los tipos de hemoglobina para detectar talasemias y hemoglobinas anormales.

## B. Definición
Una HbA2 alta (habitualmente 3,5 % o más) confirma el rasgo beta-talasémico. Un resultado normal no descarta el rasgo alfa.

## C. Espécimen y toma
Sangre total EDTA retenida de la misma toma.

## D. Intervalos y umbrales
Se usa el informe del laboratorio. HbA2 de 3,5 % o más: compatible con rasgo beta-talasémico (BSH).

## E. Interpretación
Solo confirma o no la condición COND-M3-HE-A04. El déficit de hierro puede bajar la HbA2 falsamente; por eso solo se pide con ferritina normal.

## F. Contexto del paciente y confusores
Déficit de hierro (baja la HbA2), transfusión reciente.

## G. Relaciones
VCM, eritrocitos, índice de Mentzer (SLD-BIO-143), ferritina.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Estudio de alfa-talasemia si la electroforesis es normal y la microcitosis persiste (lo decide el médico).

## K. Cuándo no interpretar / cuándo escalar
No escala por sí sola.

## L. Evidencia
BSH, guías de tamizaje de hemoglobinopatías. Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "tus glóbulos rojos son pequeños por un rasgo heredado que suele no dar síntomas".
- Inferencias prohibidas: "tienes talasemia" (el rasgo no es la enfermedad).
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, refleja, talasemia, saludly_brain_v1]
use_when: ["microcitosis sin déficit de hierro"]
combine_with: [mcv, erythrocytes, ferritin, mentzer_index]
do_not_use_alone: [hb_electrophoresis]
do_not_conclude: []
escalate_when: []
```
