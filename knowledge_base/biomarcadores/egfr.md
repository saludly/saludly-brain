---
doc_id: SLD-BIO-047
biomarker_id: egfr
name_es: eGFR
name_en: Estimated Glomerular Filtration Rate
abbreviation: eGFR / TFG
sinonimos:
- TFG estimada
- TFGe
- Tasa de filtración glomerular estimada
- CKD-EPI
- eGFR
- eGFR (Tasa de Filtración Glomerular Estimada, CKD-EPI 2021)
- eGFR / TFG
- Estimated Glomerular Filtration Rate
category: Riñón
subcategory: Función renal
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: mL/min/1,73 m²
specimen: No aplica (calculado)
nivel_catalogo: con patrón
panel: calculado
sexo: ambos
alimenta:
- COND-M2-NE-001
- COND-M2-NE-002
- COND-M2-NE-006
- COND-M2-NE-A02
- COND-M3-NU-A02
combine_with:
- creatinine
- bun
- uacr
- cystatin_c
formula: 'CKD-EPI 2021 (sin coeficiente racial); variables: creatinina, edad, sexo. Versión combinada eGFRcr-cys añade cistatina C.'
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- CKD-EPI 2021 sin coeficiente de raza; enfermedad renal exige persistencia de 3 meses (COND-M2-NE-001).
---

# eGFR (Tasa de Filtración Glomerular Estimada)

## Notas de decisión de Saludly (6 de octubre de 2026)

- CKD-EPI 2021 sin coeficiente de raza; enfermedad renal exige persistencia de 3 meses (COND-M2-NE-001).
- Reglas que usan esta ficha: COND-M2-NE-001, COND-M2-NE-002, COND-M2-NE-006, COND-M2-NE-A02, COND-M3-NU-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-047. eGFR/TFG. Categoría: Riñón. Tipo: **calculated_parameter**. Tier 1. Nota de auditoría: separado de Creatinina como registro independiente — eGFR es el parámetro calculado que se deriva de creatinina + edad + sexo (ver `creatinine.md` para el analito medido base).

## B. Definición

Estimación calculada de la tasa de filtración glomerular, el mejor indicador global de función renal disponible de forma no invasiva. No se mide directamente — se deriva matemáticamente de la creatinina sérica, ajustada por edad y sexo (y opcionalmente cistatina C).

## C. Espécimen y toma

### Examen de laboratorio del que se deriva

No tiene examen de laboratorio propio — se calcula automáticamente a partir del resultado de creatinina sérica (ver `creatinine.md`) mediante la ecuación CKD-EPI 2021.

### Condiciones de "toma de muestra"

No aplica — es un cálculo, no una medición. Hereda las condiciones preanalíticas de la creatinina (ver `creatinine.md`).

### Resultado y tipo de dato

- **Fórmula:** CKD-EPI 2021 (sin coeficiente racial), variables: creatinina, edad, sexo.
- **Versión combinada (eGFRcr-cys):** añade cistatina C, más precisa en extremos de masa muscular — ver `cystatin_c.md`.
- **Unidad:** mL/min/1.73m².
- **Limitación:** estimación poblacional — subestima/sobreestima en extremos de masa muscular (atletas, sarcopenia); cistatina C ayuda a refinar en esos casos.
- **Cuándo NO debe calcularse:** si falta creatinina, edad o sexo.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente

```
clinical_decision_threshold (KDIGO 2024, verificado): G1 ≥90 | G2 60-89 | G3a 45-59 | G3b 30-44 | G4 15-29 | G5 <15 (mL/min/1.73m²)
screening_threshold: eGFR <60 mL/min/1.73m² sostenido ≥3 meses = criterio de ERC
```

## E. Interpretación

- eGFR bajo sostenido (≥3 meses) → enfermedad renal crónica, estadificada según KDIGO G1-G5 + albuminuria A1-A3.
- La clasificación KDIGO requiere eGFR + albuminuria juntos, nunca eGFR aislado.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: edad, sexo, masa muscular aproximada/nivel de actividad física, medicamentos nefrotóxicos, hidratación reciente (heredadas de creatinina).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Creatinina (variable de entrada, obligatoria), BUN, electrolitos, **UACR** cuando esté disponible (dependencia de módulo de orina — ver `uacr.md`), Cistatina C (para refinar en extremos de masa muscular).
- `pattern_examples`: eGFR <60 + UACR elevada = ERC confirmada con daño renal documentado; eGFR 45-59 sin otros marcadores = zona gris, considerar cistatina C confirmatoria.
- `cannot_conclude`: diagnóstico de ERC con un solo valor sin persistencia de 3 meses, ni sin albuminuria cuando esté disponible.

## H. Tendencias

### Tendencias temporales

- **Importancia de la tendencia sobre el valor aislado:** una caída sostenida ≥25% respecto al valor basal es más relevante clínicamente que un solo valor bajo.
- **Necesidad de repetir:** todo primer valor alterado debe confirmarse a los 3 meses antes de establecer diagnóstico de ERC.
- **Variación biológica vs analítica:** la creatinina (variable base) tiene variabilidad biológica moderada; el cálculo en sí no añade variabilidad analítica relevante más allá de la propia de creatinina.

## I. Prevención

### Contexto preventivo y de riesgo

- Alta utilidad para detección temprana de deterioro renal silente.
- Riesgo cardiovascular: ERC es factor de riesgo cardiovascular independiente.

## J. Pruebas complementarias

### Pruebas complementarias posibles

UACR, Cistatina C (en extremos de masa muscular), ecografía renal si hay deterioro significativo — lenguaje correcto: "considerar evaluación adicional según contexto clínico", nunca automatizado.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

- **NO interpretar:** un solo valor alterado sin confirmación a 3 meses como diagnóstico de ERC.
- **Escalar:** eGFR <60 sostenido, caída rápida >25%, o eGFR <30 (derivación más urgente, categoría KDIGO G4-G5).

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte.
- **Fuente:** KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney International, marzo 2024. https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf
- **Complementaria:** UK Kidney Association, staging G1-G5/A1-A3. https://www.ukkidney.org/health-professionals/information-resources/uk-eckd-guide/ckd-staging
- **Fecha de actualización:** 2026-09. Verificado sesión previa (ago-2026).

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "eGFR sugiere posible reducción de función renal, requiere confirmación con control seriado y, si está disponible, albuminuria".
- **prohibited_inferences:** diagnóstico de ERC con un solo valor sin persistencia de 3 meses.
- **uncertainty_notes:** estimación poblacional — pierde precisión en extremos de masa muscular; considerar cistatina C en esos casos.
- **professional_review:** eGFR <60 sostenido, caída rápida >25%, o eGFR <30.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - renal
  - kidney_function
  - calculated_parameter
  - tier_1
  - saludly_brain_v1

use_when:
  - "evaluando función renal"
  - "clasificando estadio de ERC según KDIGO"

combine_with: [creatinine, bun, uacr, cystatin_c]

do_not_use_alone:
  - "diagnóstico de ERC sin persistencia de 3 meses ni albuminuria"

do_not_conclude:
  - "presencia confirmada de ERC a partir de un solo valor"
  - "ausencia de ERC a partir de un valor normal aislado"

escalate_when:
  - "eGFR <60 sostenido"
  - "caída rápida >25% respecto a basal"
  - "eGFR <30 (derivación más urgente)"
```
