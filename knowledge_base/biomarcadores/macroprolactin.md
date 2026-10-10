---
doc_id: "SLD-BIO-128"
biomarker_id: "macroprolactin"
name_es: "Macroprolactina (prolactina tras precipitación con PEG)"
name_en: "Macroprolactin (post-PEG prolactin)"
abbreviation: "MacroPRL"
sinonimos: ["Macroprolactina", "Prolactina post PEG", "Prolactina monomérica", "Recuperación de prolactina tras PEG"]
category: "Hipófisis"
parameter_type: "measured_analyte"
tipo_resultado: "numérico (porcentaje de recuperación y prolactina monomérica)"
unidad_canonica: "% de recuperación; prolactina monomérica en ng/mL"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja, mujeres"
activa_si: ["prolactin > límite superior"]
alimenta: ["COND-M5-MU-003"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-128 · Macroprolactina

## A. Identificación
El laboratorio precipita la muestra con polietilenglicol (PEG) y vuelve a medir la prolactina. Lo que queda es la prolactina monomérica, la forma activa.

## B. Definición
La macroprolactina es prolactina unida a anticuerpos: el análisis la cuenta, pero casi no tiene efecto en el cuerpo. Explica una parte de las prolactinas altas sin síntomas.

## C. Espécimen y toma
Suero de la misma toma.

## D. Intervalos y umbrales
Corte del laboratorio para la recuperación tras PEG. En la literatura, una recuperación menor de 40 % suele indicar predominio de macroprolactina y mayor de 60 % predominio de prolactina monomérica; la zona intermedia se interpreta con la prolactina monomérica frente al intervalo del laboratorio.

## E. Interpretación
Predominio de macroprolactina: hallazgo sin significado clínico habitual (escalamiento 0). Predominio monomérico: la prolactina alta es real y sigue la ficha MU-003.

## F. Contexto del paciente y confusores
Medicamentos que suben la prolactina, embarazo y lactancia (no se interpreta).

## G. Relaciones
Prolactina, TSH, TFG (M2, M5).

## H. Tendencias
La macroprolactinemia suele persistir sin cambios.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Según el médico, si la prolactina monomérica está alta.

## K. Cuándo no interpretar / cuándo escalar
No escala por sí sola; sigue MU-003.

## L. Evidencia
Endocrine Society 2011 y Febrasgo-SBEM 2024 (citadas en el Lote 5). Cortes de recuperación por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "la mayor parte de tu prolactina es una forma que normalmente no tiene efecto".
- Inferencias prohibidas: tumor de hipófisis.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hipofisis, prolactina, refleja, saludly_brain_v1]
use_when: ["prolactina alta"]
combine_with: [prolactin, tsh]
do_not_use_alone: []
do_not_conclude: ["prolactinoma"]
escalate_when: []
```
