---
doc_id: SLD-BIO-107
biomarker_id: anti_hbs
name_es: Anticuerpos contra el antígeno de superficie de hepatitis B
name_en: Hepatitis B surface antibody
abbreviation: Anti-HBs
sinonimos:
- Anti-HBs
- AcHBs
- Anticuerpos anti antígeno de superficie
- HBsAb
- Anticuerpos contra antígeno de superficie (anti-HBs)
- Anticuerpos contra antígeno de superficie
category: Infecciosas
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mUI/mL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar, todas las personas, con consentimiento
alimenta:
- COND-M4-IN-002
tier: 1
status: BORRADOR
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-10
fuentes_estado: por verificar
---

# SLD-BIO-107 · Anticuerpos contra el antígeno de superficie (anti-HBs)

## A. Identificación
Inmunoensayo cuantitativo de los anticuerpos protectores contra la hepatitis B.

## B. Definición
Aparecen tras la vacuna o tras una infección resuelta. Con anti-HBc no reactivo indican inmunidad por vacuna.

## C. Espécimen y toma
Suero, sin ayuno específico.

## D. Intervalos y umbrales
10 mUI/mL o más: nivel considerado protector. Menos de 10: sin anticuerpos detectables en nivel protector.

## E. Interpretación
Menos de 10 con HBsAg y anti-HBc no reactivos: estado susceptible y recomendación de vacuna. En personas vacunadas hace años, los anticuerpos pueden bajar de 10 aunque quede memoria inmunológica; el médico decide si basta una dosis de refuerzo.

## F. Contexto del paciente y confusores
Inmunosupresión y diálisis (respuesta menor a la vacuna), tiempo desde la última dosis.

## G. Relaciones
Siempre con HBsAg y anti-HBc (IN-002).

## H. Tendencias
Baja con los años tras la vacunación.

## I. Prevención
Vacuna contra la hepatitis B.

## J. Pruebas complementarias
Anti-HBs después de la vacuna, según el médico.

## K. Cuándo no interpretar / cuándo escalar
No escala por sí solo; el estado susceptible tiene escalamiento 1 (IN-002).

## L. Evidencia
CDC 2023. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "no tienes anticuerpos detectables en nivel protector; existe una vacuna".
- Inferencias prohibidas: "nunca te vacunaron", "no tienes defensas" sin matizar.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_b, vacunacion, panel_estandar, saludly_brain_v1]
use_when: ["estado de inmunidad contra hepatitis B"]
combine_with: [hbsag, anti_hbc]
do_not_use_alone: ["clasificar infección"]
do_not_conclude: ["nunca vacunado"]
escalate_when: []
```
