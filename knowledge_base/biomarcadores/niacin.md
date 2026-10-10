---
doc_id: "SLD-BIO-117"
biomarker_id: "niacin"
name_es: "Niacina (vitamina B3)"
name_en: "Niacin (vitamin B3)"
abbreviation: "B3"
sinonimos: ["Niacina", "Vitamina B3", "Ácido nicotínico", "Nicotinamida", "Niacin"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/mL"
specimen: "Suero o plasma"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-117 · Niacina (vitamina B3)

## A. Identificación
Niacina o sus formas en sangre, habitualmente por LC-MS/MS.

## B. Definición
Vitamina hidrosoluble del grupo B, necesaria para el metabolismo energético. Su déficit grave (pelagra) es raro.

## C. Espécimen y toma
Suero o plasma en ayunas.

## D. Intervalos y umbrales
El laboratorio de ejemplo no reporta intervalo ("No establecido").

## E. Interpretación
El estado de niacina se evalúa normalmente con metabolitos en orina, no con el valor en sangre. Por eso se muestra solo como información, sin clase, aunque el laboratorio dé un intervalo, hasta que el médico decida otra cosa.

## F. Contexto del paciente y confusores
Suplementos en dosis altas (enrojecimiento, daño hepático), alcohol, isoniazida.

## G. Relaciones
ALT y GGT si toma niacina en dosis altas.

## H. Tendencias
Sin uso de seguimiento.

## I. Prevención y alimentos
Carnes, pollo, pescado, maní y cereales integrales.

## J. Pruebas complementarias
Metabolitos en orina, según el médico.

## K. Cuándo no interpretar / cuándo escalar
Siempre solo valor. Suplemento en dosis altas con ALT alta: escalamiento 1.

## L. Evidencia
Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "valor de niacina mostrado como información".
- Inferencias prohibidas: déficit o exceso a partir del valor en sangre.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, hidrosoluble, niacina, solo_informativo, panel_estandar, saludly_brain_v1]
use_when: ["valor de niacina"]
combine_with: [alt, ggt]
do_not_use_alone: ["evaluar el estado de niacina"]
do_not_conclude: ["pelagra", "deficiencia de niacina"]
escalate_when: ["suplemento de niacina en dosis altas con ALT alta"]
```
