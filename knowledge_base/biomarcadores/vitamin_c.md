---
doc_id: "SLD-BIO-115"
biomarker_id: "vitamin_c"
name_es: "Vitamina C (ácido ascórbico)"
name_en: "Vitamin C (ascorbic acid)"
abbreviation: "Vit C"
sinonimos: ["Vitamina C", "Ácido ascórbico", "Ascorbato", "Vit C"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "mg/dL"
specimen: "Plasma heparinizado, congelado y protegido de la luz"
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

# SLD-BIO-115 · Vitamina C (ácido ascórbico)

## A. Identificación
Ácido ascórbico en plasma por HPLC.

## B. Definición
Vitamina hidrosoluble antioxidante, necesaria para el colágeno y para absorber el hierro de los vegetales.

## C. Espécimen y toma
Es la muestra más delicada del panel: se degrada en pocas horas a temperatura ambiente. Exige separar el plasma, protegerlo de la luz y transportarlo congelado. Sin eso, el resultado sale falsamente bajo (protocolo de toma, Lote 6).

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 0,4 a 2,0 mg/dL).

## E. Interpretación
Refleja la ingesta de los días recientes. El déficit grave (escorbuto) es raro.

## F. Contexto del paciente y confusores
Tabaquismo (baja la vitamina C), transporte no congelado, suplementos en dosis altas (interfieren con algunas pruebas, como la fructosamina).

## G. Relaciones
Hierro y ferritina (M3): la vitamina C ayuda a absorber hierro de los vegetales.

## H. Tendencias
Cambia rápido con la dieta.

## I. Prevención y alimentos
Guayaba, naranja, mandarina, limón, kiwi, fresa, pimentón y brócoli.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
Sin transporte congelado validado: no interpretable. Las dosis altas de suplemento se asocian a cálculos renales en personas predispuestas: si está alta con suplementos, escalamiento 1.

## L. Evidencia
Regla de vitaminas (documento 07), protocolo de toma domiciliaria. Fuentes por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "vitamina C baja; refleja tu alimentación de los últimos días".
- Inferencias prohibidas: escorbuto, dosis de suplemento, interpretar sin transporte congelado.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, hidrosoluble, vitamina_c, preanalitica_critica, panel_estandar, saludly_brain_v1]
use_when: ["vitamina C fuera de rango", "recomendación para absorber hierro"]
combine_with: [ferritin, serum_iron]
do_not_use_alone: ["interpretar sin transporte congelado"]
do_not_conclude: ["escorbuto"]
escalate_when: ["vitamina C alta con suplementos"]
```
