---
doc_id: "SLD-BIO-126"
biomarker_id: "hcv_rna"
name_es: "ARN del virus de la hepatitis C"
name_en: "Hepatitis C virus RNA"
abbreviation: "ARN VHC"
sinonimos: ["ARN VHC", "Carga viral hepatitis C", "HCV RNA", "PCR hepatitis C", "Viremia VHC"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (detectable / no detectable) o cuantitativo"
unidad_canonica: "UI/mL"
specimen: "Suero o plasma de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["anti_hcv reactivo"]
alimenta: ["COND-M4-IN-001"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-126 · ARN del virus de la hepatitis C

## A. Identificación
Prueba molecular (PCR) que detecta el material genético del virus.

## B. Definición
Es la prueba que confirma si una infección por hepatitis C está activa.

## C. Espécimen y toma
Suero o plasma; el laboratorio debe separar y conservar la muestra según el método molecular.

## D. Intervalos y umbrales
Detectable o no detectable según el límite del método. Si es cuantitativa, se reporta en UI/mL.

## E. Interpretación
Detectable: infección activa. No detectable con anti-VHC reactivo: infección resuelta o falso positivo del anticuerpo.

## F. Contexto del paciente y confusores
Tratamiento antiviral previo, muestra mal conservada (falso no detectable).

## G. Relaciones
Anti-VHC, ALT, FIB-4 (M4).

## H. Tendencias
Se usa para confirmar curación tras tratamiento, según el médico.

## I. Prevención
Tratamiento curativo; no compartir objetos con sangre.

## J. Pruebas complementarias
Genotipo y evaluación de fibrosis, según el médico.

## K. Cuándo no interpretar / cuándo escalar
Siempre con llamada del médico (IN-001).

## L. Evidencia
Lineamiento de hepatitis C del Ministerio de Salud. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "el virus está activo o no está activo".
- Inferencias prohibidas: cirrosis, incurable.
- Revisión profesional: todo resultado.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_c, molecular, refleja, saludly_brain_v1]
use_when: ["anti-VHC reactivo"]
combine_with: [anti_hcv, alt]
do_not_use_alone: []
do_not_conclude: ["cirrosis"]
escalate_when: ["cualquier resultado"]
```
