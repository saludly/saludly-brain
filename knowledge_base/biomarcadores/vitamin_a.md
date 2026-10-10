---
doc_id: "SLD-BIO-112"
biomarker_id: "vitamin_a"
name_es: "Vitamina A (retinol sérico)"
name_en: "Vitamin A (serum retinol)"
abbreviation: "Vit A"
sinonimos: ["Vitamina A", "Retinol", "Retinol sérico", "Vit A"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/dL"
specimen: "Suero protegido de la luz"
nivel_catalogo: "vitamina"
panel: "fuera del panel base"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-112 · Vitamina A (retinol)

> **Decisión del 10 de octubre de 2026.** Retirada del panel base el 10 de octubre de 2026 (aprobación de Carlos): es una prueba especializada que no ofrecen los laboratorios clínicos comunes o que exige transporte especial, y ni Function Health ni Superpower la incluyen en su panel base. La ficha se conserva: si el resultado llega, se interpreta igual.

## A. Identificación
Retinol en suero, medido habitualmente por HPLC.

## B. Definición
Vitamina liposoluble necesaria para la visión, la piel y la inmunidad. Se almacena en el hígado, así que el valor en sangre se mantiene estable hasta que las reservas se agotan o se saturan.

## C. Espécimen y toma
Suero en ayunas, protegido de la luz (el retinol se degrada con ella).

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 30 a 80 µg/dL).

## E. Interpretación
Bajo: ingesta insuficiente, mala absorción de grasas o inflamación. Alto: suplementos o exceso de hígado en la dieta; la vitamina A se acumula.

## F. Contexto del paciente y confusores
La inflamación baja el retinol sin que falte (con hs-CRP mayor de 5 mg/L, un valor bajo no se interpreta como déficit). La enfermedad renal crónica lo sube. Embarazo: el exceso es dañino para el bebé.

## G. Relaciones
hs-CRP (inflamación), TFG (función renal), albúmina.

## H. Tendencias
Cambia lentamente; refleja reservas del hígado.

## I. Prevención y alimentos
Huevo, lácteos e hígado (vitamina A directa); zanahoria, ahuyama, mango, papaya y espinaca (provitamina A, que el cuerpo convierte según lo necesita).

## J. Pruebas complementarias
Según el médico.

## K. Cuándo no interpretar / cuándo escalar
Bajo con hs-CRP mayor de 5: no interpretable como déficit. Alto: escalamiento 1 y pregunta por suplementos; en embarazo, escalamiento 2.

## L. Evidencia
Regla de vitaminas (documento 07). Fuentes por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "vitamina A por debajo o por encima del rango del laboratorio".
- Inferencias prohibidas: déficit con inflamación, dosis de suplemento, recomendar hígado en embarazo.
- Revisión profesional: alta en embarazo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, liposoluble, vitamina_a, panel_estandar, saludly_brain_v1]
use_when: ["vitamina A fuera de rango"]
combine_with: [hs_crp, egfr, albumin]
do_not_use_alone: ["déficit de vitamina A con inflamación"]
do_not_conclude: ["deficiencia de vitamina A"]
escalate_when: ["vitamina A alta en embarazo", "vitamina A alta con suplementos"]
```
