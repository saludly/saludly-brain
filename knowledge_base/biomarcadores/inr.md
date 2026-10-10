---
doc_id: SLD-BIO-056
biomarker_id: inr
name_es: INR
name_en: International Normalized Ratio
abbreviation: INR
sinonimos:
- INR
- INR (Razón Internacional Normalizada)
- International Normalized Ratio
category: Hígado
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: sin unidad
specimen: Plasma citrato
nivel_catalogo: solo valor y rango
panel: calculado
sexo: ambos
alimenta:
- SEG-006
combine_with:
- pt
- albumin
formula: INR = (PT paciente / PT control)^ISI — el ISI (Índice de Sensibilidad Internacional) es específico del reactivo de tromboplastina de cada laboratorio
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# INR (Razón Internacional Normalizada)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-056. INR. Categoría: Hígado. Tipo: **calculated_parameter**. Tier 3.

## B. Definición

Estandarización del PT desarrollada por un comité de la OMS para permitir comparar resultados entre laboratorios con distintos reactivos de tromboplastina, cuya sensibilidad varía. Es la prueba estándar para monitorear anticoagulación con warfarina.

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio para parámetro calculado)

- **Fórmula:** INR = (PT paciente ÷ PT control)^ISI.
- **Variables necesarias:** PT del paciente, PT control del laboratorio, ISI del reactivo específico usado.
- **Limitación importante (verificada esta sesión):** el INR está **validado únicamente para pacientes en tratamiento con warfarina** — existe preocupación documentada sobre su validez para determinar riesgo de sangrado en pacientes con hepatopatía crónica, donde el grado de prolongación predice el riesgo de sangrado solo de forma aproximada, no como en el contexto de warfarina.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Laboratory reference interval (sin anticoagulación):** **0.8-1.2** (rango consolidado de fuentes concordantes: Medscape 0.8-1.1, estudio clínico 0.9-1.2).
- **Rango terapéutico en anticoagulación con warfarina (uso clínico estándar, no cribado):** típicamente 2.0-3.0 para la mayoría de indicaciones (fibrilación auricular, TVP) — este rango terapéutico específico depende de la indicación clínica exacta y es decisión médica, no un valor que Saludly deba usar para interpretación autónoma.
- **URLs fuente:** https://emedicine.medscape.com/article/2086058-overview ; https://clinicaltrials.gov/study/NCT01623531 — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevado (sin anticoagulación conocida):** hepatopatía con síntesis reducida de factores de coagulación, deficiencia de vitamina K, coagulopatía.
- **En paciente anticoagulado con warfarina:** el objetivo es mantenerlo dentro del rango terapéutico específico de su indicación — fuera de ese contexto de manejo médico activo.

## F. Contexto del paciente y confusores

### Contexto del paciente

Uso de warfarina (crítico — cambia completamente la interpretación), hepatopatía conocida, dieta (vitamina K).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: PT (del cual se deriva, obligatorio), Albúmina (función hepática de síntesis).
- `cannot_conclude`: riesgo de sangrado en hepatopatía crónica con la misma precisión que en pacientes con warfarina — es una limitación de validación documentada.

## H. Tendencias

### Tendencias temporales

En hepatopatía progresiva, aumento sostenido refleja deterioro de función de síntesis — relevante para seguimiento de severidad (ej. en el contexto de scores pronósticos hepáticos).

## I. Prevención

### Contexto preventivo

No aplica como cribado — uso en monitoreo de anticoagulación o evaluación de hepatopatía ya conocida.

## J. Pruebas complementarias

### Pruebas complementarias posibles

PT (base del cálculo), Albúmina, función hepática completa.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No usar el INR para predecir riesgo de sangrado en hepatopatía con la misma confianza que en warfarina. Escalar ante INR elevado sin anticoagulación conocida (sospecha de hepatopatía severa o coagulopatía), o fuera de rango terapéutico en paciente anticoagulado con síntomas de sangrado o trombosis.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte para su rol en monitoreo de warfarina; con limitación de validez documentada para predicción de sangrado en hepatopatía crónica.
- Fuentes verificadas esta sesión: ver URLs en sección D.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "INR elevado sin anticoagulación conocida, considerar hepatopatía o deficiencia de vitamina K; en paciente anticoagulado, el objetivo terapéutico es decisión médica".
- **prohibited_inferences:** usar el INR para predecir riesgo de sangrado en hepatopatía con la misma confianza que en pacientes anticoagulados con warfarina; ajustar dosis de warfarina (decisión médica exclusiva).
- **uncertainty_notes:** validado específicamente para warfarina — su aplicación en otros contextos (hepatopatía) tiene limitaciones reconocidas.
- **professional_review:** INR elevado sin anticoagulación conocida, o fuera de rango terapéutico en paciente anticoagulado con síntomas.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - coagulation
  - anticoagulation_monitoring
  - calculated_parameter
  - tier_3
  - saludly_brain_v1
use_when:
  - "monitoreo de warfarina, o hepatopatía conocida"
combine_with: [pt, albumin]
do_not_use_alone:
  - "predicción de riesgo de sangrado en hepatopatía con la misma confianza que en warfarina"
do_not_conclude:
  - "ajuste de dosis de warfarina (decisión médica)"
escalate_when:
  - "INR elevado sin anticoagulación conocida"
  - "fuera de rango terapéutico con síntomas de sangrado o trombosis"
```
