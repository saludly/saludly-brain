---
doc_id: SLD-BIO-049
biomarker_id: pt
name_es: Tiempo de Protrombina
name_en: Prothrombin Time
abbreviation: PT
sinonimos:
- Tiempo de protrombina
- TP
- PT
- Tiempo de Protrombina
- Tiempo de Protrombina (PT)
- Prothrombin Time
category: Hígado
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: s
specimen: Plasma citrato
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-006
combine_with:
- inr
- albumin
- alt
- ast
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

# Tiempo de Protrombina (PT)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-049. PT. Categoría: Hígado. Tipo: measured_analyte. Tier 3.

## B. Definición

Mide la integridad de la vía extrínseca y común de la coagulación (factor tisular, factores VII, II, V, X, I). Su prolongación refleja deficiencia de factores de coagulación — por síntesis hepática reducida, deficiencia de vitamina K, o anticoagulación con warfarina.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa, tubo de citrato de sodio (tapa azul claro) — volumen exacto crítico para la relación sangre:anticoagulante. Método: se añade calcio y tromboplastina a la muestra, midiendo el tiempo hasta formación del coágulo de fibrina.

### Condiciones de toma de muestra

No requiere ayuno. **Llenado incompleto del tubo de citrato invalida la muestra** (relación anticoagulante:sangre incorrecta). Estabilidad: refrigerado hasta 24h, congelado hasta 36h (a temperatura ambiente se deteriora en 12h).

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Laboratory reference interval:** **11-13.5 segundos** (rango consolidado de fuentes concordantes: Medscape 11.0-12.5s, RNpedia 11-13s, revisión de valores de coagulación 11-13.5s) — **depende fuertemente del reactivo de tromboplastina usado por cada laboratorio**, por eso existe el INR para estandarizar entre laboratorios (ver `inr.md`).
- **Anticoagulación terapéutica completa (warfarina):** >1.5-2 veces el valor control.
- **URLs fuente:** https://emedicine.medscape.com/article/2086058-overview ; https://www.rnpedia.com/tools-apps/normal-laboratory-values/ ; https://www.droracle.ai/articles/680824/what-are-the-normal-laboratory-values-for-coagulation-tests — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Prolongado:** deficiencia de vitamina K, hepatopatía (reducción de síntesis de factores), warfarina, deficiencia congénita de factores de la vía extrínseca (poco frecuente), CID (coagulación intravascular diseminada).

## F. Contexto del paciente y confusores

### Contexto del paciente

Uso de warfarina u otros anticoagulantes, hepatopatía conocida, dieta (deficiencia de vitamina K), síntomas de sangrado.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: INR (calculado a partir de PT — ver `inr.md`), Albúmina y transaminasas (contexto de función hepática de síntesis).
- `cannot_conclude`: causa específica de prolongación sin contexto de medicamentos y función hepática.

## H. Tendencias

### Tendencias temporales

En hepatopatía progresiva, un PT/INR en aumento sostenido refleja deterioro de la función de síntesis hepática — relevante para seguimiento de severidad.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — indicado en hepatopatía conocida, antes de procedimientos invasivos, o monitoreo de warfarina (vía INR).

## J. Pruebas complementarias

### Pruebas complementarias posibles

INR (siempre calculado a partir de PT), albúmina, función hepática completa.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin contexto de medicamentos anticoagulantes. Escalar ante prolongación marcada sin uso de anticoagulantes conocido (sospecha de hepatopatía severa o coagulopatía), o síntomas de sangrado.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte, múltiples fuentes clínicas concordantes.
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "PT prolongado, considerar función hepática, vitamina K, o uso de anticoagulantes; calcular/interpretar junto a INR".
- **prohibited_inferences:** diagnóstico de hepatopatía o coagulopatía sin contexto clínico completo.
- **uncertainty_notes:** fuertemente dependiente del reactivo del laboratorio — por eso el INR existe para estandarizar.
- **professional_review:** prolongación marcada sin anticoagulantes conocidos, o síntomas de sangrado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - coagulation
  - tier_3
  - saludly_brain_v1
use_when:
  - "hepatopatía conocida, sospecha de coagulopatía, o previo a procedimientos"
combine_with: [inr, albumin, alt, ast]
do_not_use_alone:
  - "diagnóstico de hepatopatía o coagulopatía sin contexto"
do_not_conclude:
  - "causa específica sin contexto de medicamentos y función hepática"
escalate_when:
  - "prolongación marcada sin anticoagulantes conocidos"
  - "síntomas de sangrado"
```
