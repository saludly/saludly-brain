---
doc_id: "SLD-BIO-113"
biomarker_id: "vitamin_e"
name_es: "Vitamina E (alfa-tocoferol)"
name_en: "Vitamin E (alpha-tocopherol)"
abbreviation: "Vit E"
sinonimos: ["Vitamina E", "Alfa-tocoferol", "Tocoferol", "Vit E"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "mg/L"
specimen: "Suero en ayunas protegido de la luz"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-113 · Vitamina E (alfa-tocoferol)

## A. Identificación
Alfa-tocoferol en suero por HPLC.

## B. Definición
Vitamina liposoluble antioxidante. Viaja en la sangre con el colesterol y los triglicéridos.

## C. Espécimen y toma
Suero en ayunas, protegido de la luz.

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 5,5 a 17,0 mg/L).

## E. Interpretación
Como viaja con los lípidos, sube y baja con el colesterol y los triglicéridos. Con lípidos muy altos o muy bajos, el valor absoluto engaña y el médico puede usar la relación vitamina E/lípidos. El déficit real es raro y suele deberse a mala absorción de grasas.

## F. Contexto del paciente y confusores
Lípidos altos o bajos, suplementos, mala absorción, anticoagulantes (dosis altas de vitamina E aumentan el riesgo de sangrado).

## G. Relaciones
Colesterol total y triglicéridos (M1).

## H. Tendencias
Sin uso de seguimiento en prevención.

## I. Prevención y alimentos
Nueces, maní, semillas de girasol, almendras, aguacate y aceites vegetales.

## J. Pruebas complementarias
Relación vitamina E/lípidos según el médico.

## K. Cuándo no interpretar / cuándo escalar
Con triglicéridos de 500 mg/dL o más o colesterol muy bajo: solo valor. Alta con suplementos y anticoagulantes: escalamiento 1 con sugerencia de consulta.

## L. Evidencia
Regla de vitaminas (documento 07). Fuentes por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "vitamina E fuera de rango; se interpreta junto con tus lípidos".
- Inferencias prohibidas: déficit sin considerar los lípidos, dosis de suplemento.
- Revisión profesional: alta con anticoagulantes.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, liposoluble, vitamina_e, panel_estandar, saludly_brain_v1]
use_when: ["vitamina E fuera de rango"]
combine_with: [total_cholesterol, triglycerides]
do_not_use_alone: ["déficit con lípidos alterados"]
do_not_conclude: ["deficiencia de vitamina E"]
escalate_when: ["vitamina E alta con anticoagulantes"]
```
