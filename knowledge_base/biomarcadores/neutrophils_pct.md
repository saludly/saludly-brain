---
doc_id: "SLD-BIO-123"
biomarker_id: "neutrophils_pct"
name_es: "Neutrófilos (porcentaje)"
name_en: "Neutrophils (percentage)"
abbreviation: "NEU%"
sinonimos: ["Neutrófilos %", "Neutrófilos relativos", "Segmentados %", "Polimorfonucleares %", "NEU%"]
category: "Hematología"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "%"
specimen: "Sangre total EDTA"
nivel_catalogo: "solo valor y rango (apoyo de condiciones)"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-HE-A02", "SEG-012"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-123 · Neutrófilos %

## A. Identificación
Proporción de neutrófilos entre los leucocitos, en el diferencial del hemograma.

## B. Definición
Los neutrófilos son la primera defensa contra las bacterias.

## C. Espécimen y toma
Sangre total EDTA.

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 40 a 70 %).

## E. Interpretación
El porcentaje solo no basta: la decisión se toma con el recuento absoluto (ficha neutrophils_abs). Un porcentaje alto con recuento normal suele no tener importancia.

## F. Contexto del paciente y confusores
Infección reciente, corticoides, ejercicio, tabaquismo. Las personas de ascendencia africana pueden tener recuentos de neutrófilos más bajos sin enfermedad (neutropenia étnica benigna); es relevante en Colombia y la vista médica lo anota.

## G. Relaciones
Neutrófilos absolutos, leucocitos, linfocitos (M3).

## H. Tendencias
Cambia con infecciones y estrés.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Repetir hemograma.

## K. Cuándo no interpretar / cuándo escalar
No escala por el porcentaje; escala por el absoluto según HE-A02.

## L. Evidencia
Hematología básica. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "dato del diferencial; se interpreta con el recuento absoluto".
- Inferencias prohibidas: infección, defensas bajas, leucemia.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, hemograma, diferencial, panel_estandar, saludly_brain_v1]
use_when: ["diferencial de leucocitos"]
combine_with: [neutrophils_abs, wbc, lymphocytes_pct]
do_not_use_alone: ["decidir neutropenia o neutrofilia"]
do_not_conclude: ["infección", "leucemia"]
escalate_when: []
```
