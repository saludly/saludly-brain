---
doc_id: "SLD-BIO-121"
biomarker_id: "tibc"
name_es: "Capacidad total de fijación de hierro"
name_en: "Total iron-binding capacity"
abbreviation: "TIBC"
sinonimos: ["TIBC", "CTFH", "Capacidad total de fijación de hierro", "Capacidad de fijación del hierro"]
category: "Metabolismo del hierro"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/dL"
specimen: "Suero en ayunas"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-HE-002", "COND-M3-HE-006", "saturación de transferrina (calculado)"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-121 · Capacidad total de fijación de hierro (TIBC)

## A. Identificación
Cantidad máxima de hierro que puede transportar la transferrina en sangre.

## B. Definición
Mide indirectamente la transferrina. Sube cuando el cuerpo necesita hierro y baja con la inflamación.

## C. Espécimen y toma
Suero en ayunas, en la mañana (el hierro sérico, que se usa con ella, varía en el día).

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 250 a 450 µg/dL).

## E. Interpretación
Alta: déficit de hierro, embarazo, anticonceptivos con estrógenos. Baja: inflamación, desnutrición, enfermedad hepática. Se usa sobre todo para calcular la saturación de transferrina (hierro / TIBC × 100).

## F. Contexto del paciente y confusores
Embarazo, anticonceptivos, inflamación, desnutrición.

## G. Relaciones
Ferritina, hierro sérico, saturación, transferrina, hs-CRP (M3).

## H. Tendencias
Baja al corregir el déficit de hierro.

## I. Prevención
La de hierro (M3).

## J. Pruebas complementarias
Ninguna adicional.

## K. Cuándo no interpretar / cuándo escalar
No escala sola; se lee dentro de las condiciones de hierro.

## L. Evidencia
OMS 2020 (ferritina y estado de hierro). Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "dato de apoyo para entender tu hierro".
- Inferencias prohibidas: diagnóstico con TIBC aislada.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hierro, hematologia, tibc, panel_estandar, saludly_brain_v1]
use_when: ["cálculo de saturación de transferrina", "perfil de hierro"]
combine_with: [serum_iron, ferritin, transferrin, transferrin_saturation, hs_crp]
do_not_use_alone: ["diagnóstico de déficit de hierro"]
do_not_conclude: ["anemia ferropénica con TIBC sola"]
escalate_when: []
```
