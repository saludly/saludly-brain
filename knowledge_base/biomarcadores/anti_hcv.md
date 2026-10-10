---
doc_id: SLD-BIO-105
biomarker_id: anti_hcv
name_es: Anticuerpos contra el virus de la hepatitis C
name_en: Hepatitis C virus antibody
abbreviation: Anti-VHC
sinonimos:
- Anti-VHC
- Anti HCV
- Anticuerpos hepatitis C
- HCV Ab
- Hepatitis C anticuerpos totales
- Anticuerpos contra hepatitis C (anti-VHC)
- Anticuerpos contra hepatitis C
category: Infecciosas
parameter_type: measured_analyte
tipo_resultado: cualitativo (reactivo / no reactivo) con índice
unidad_canonica: índice (S/CO)
specimen: Suero
nivel_catalogo: con patrón
panel: estándar, todas las personas, con consentimiento
alimenta:
- COND-M4-IN-001
tier: 1
status: BORRADOR
schema_version: '2.1'
clinical_priority: high
requires_professional_review: true
source_version: 2026-10
fuentes_estado: por verificar
---

# SLD-BIO-105 · Anticuerpos contra hepatitis C (anti-VHC)

## A. Identificación
Inmunoensayo que detecta anticuerpos contra el virus de la hepatitis C. Es la prueba inicial del algoritmo de tamizaje.

## B. Definición
Un resultado reactivo indica contacto con el virus en algún momento. No distingue infección activa de infección resuelta: para eso está el ARN viral, que el laboratorio corre como refleja.

## C. Espécimen y toma
Suero, sin ayuno específico.

## D. Intervalos y umbrales
Reactivo o no reactivo según el índice y el corte del fabricante (por ejemplo, índice menor de 1,00 = no reactivo en el PDF de ejemplo).

## E. Interpretación
No reactivo: sin evidencia de infección, salvo exposición muy reciente (los anticuerpos tardan semanas o meses en aparecer). Reactivo: se interpreta solo con el ARN viral.

## F. Contexto del paciente y confusores
Exposición reciente (periodo de ventana), inmunosupresión (puede no generar anticuerpos), falsos positivos con índices bajos.

## G. Relaciones
Con ALT alta, se lee en el patrón hepático (M4).

## H. Tendencias
Los anticuerpos suelen persistir tras la curación; no sirven para controlar el tratamiento.

## I. Prevención
No compartir objetos con sangre; tratamiento curativo disponible.

## J. Pruebas complementarias
ARN de hepatitis C (refleja).

## K. Cuándo no interpretar / cuándo escalar
Reactivo: escalamiento 2 con llamada del médico, nunca por WhatsApp (IN-001).

## L. Evidencia
Lineamiento de tamizaje de hepatitis C del Ministerio de Salud, USPSTF 2020. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "anticuerpos reactivos; se necesita el ARN viral para saber si la infección está activa".
- Inferencias prohibidas: cirrosis, incurable, contagio a la familia.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_c, serologia, panel_estandar, saludly_brain_v1]
use_when: ["anti-VHC reactivo o no reactivo"]
combine_with: [hcv_rna, alt, ast]
do_not_use_alone: ["afirmar infección activa"]
do_not_conclude: ["cirrosis", "infección activa sin ARN"]
escalate_when: ["cualquier resultado reactivo"]
```
