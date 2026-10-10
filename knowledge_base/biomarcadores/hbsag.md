---
doc_id: "SLD-BIO-106"
biomarker_id: "hbsag"
name_es: "Antígeno de superficie del virus de la hepatitis B"
name_en: "Hepatitis B surface antigen"
abbreviation: "HBsAg"
sinonimos: ["HBsAg", "Antígeno de superficie hepatitis B", "AgHBs", "Antígeno Australia"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas, con consentimiento"
alimenta: ["COND-M4-IN-002"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-106 · Antígeno de superficie de hepatitis B (HBsAg)

## A. Identificación
Inmunoensayo que detecta una proteína de la envoltura del virus de la hepatitis B.

## B. Definición
Su presencia indica infección actual, aguda o crónica. Si persiste más de 6 meses, la infección es crónica.

## C. Espécimen y toma
Suero, sin ayuno específico.

## D. Intervalos y umbrales
Reactivo o no reactivo según el índice y el corte del fabricante.

## E. Interpretación
Siempre se interpreta con anti-HBc total y anti-HBs, en los cinco estados de la ficha IN-002.

## F. Contexto del paciente y confusores
La vacuna puede dar un HBsAg reactivo transitorio en los días siguientes a la aplicación; la enfermera pregunta si hubo vacuna reciente. Falsos positivos con índices bajos.

## G. Relaciones
Con ALT alta, se lee en el patrón hepático (M4).

## H. Tendencias
La negativización con aparición de anti-HBs indica resolución.

## I. Prevención
Vacunación de convivientes y parejas; no compartir objetos con sangre.

## J. Pruebas complementarias
Carga viral, HBeAg, anti-HBc IgM, según el médico.

## K. Cuándo no interpretar / cuándo escalar
Reactivo: escalamiento 2 con llamada (IN-002).

## L. Evidencia
CDC 2023 (interpretación serológica), Res. 1314 de 2020. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "la prueba muestra una infección por hepatitis B; el médico explicará los siguientes pasos".
- Inferencias prohibidas: hepatitis crónica sin tiempo de evolución, cirrosis, incurable.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_b, serologia, panel_estandar, saludly_brain_v1]
use_when: ["interpretar el panel de hepatitis B"]
combine_with: [anti_hbc, anti_hbs, alt]
do_not_use_alone: ["clasificar el estado de hepatitis B"]
do_not_conclude: ["infección crónica sin persistencia de 6 meses", "cirrosis"]
escalate_when: ["cualquier resultado reactivo"]
```
