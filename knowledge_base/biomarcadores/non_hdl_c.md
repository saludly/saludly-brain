---
doc_id: SLD-BIO-044
biomarker_id: non_hdl_c
name_es: Colesterol no-HDL
name_en: Non-HDL Cholesterol
abbreviation: non-HDL-C
sinonimos:
- Colesterol no HDL
- No-HDL
- Non-HDL
- Colesterol no-HDL
- non-HDL-C
- Non-HDL Cholesterol
category: cardiovascular_lipids
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: No aplica (calculado)
nivel_catalogo: con patrón
panel: calculado
sexo: ambos
alimenta:
- COND-M1-CA-001
combine_with:
- total_cholesterol
- hdl_c
- ldl_c
- apob
formula: Colesterol no-HDL = Colesterol total − HDL-C
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Corte operativo de tamizaje: 160 mg/dL (COND-M1-CA-001).'
---

# Colesterol no-HDL (calculado)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Corte operativo de tamizaje: 160 mg/dL (COND-M1-CA-001).
- Reglas que usan esta ficha: COND-M1-CA-001. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-044. non-HDL-C. Categoría: Cardiovascular/Lípidos. **Tipo: parámetro calculado** (nunca medido directamente). Tier 1.

## B. Definición

Suma de todo el colesterol transportado en partículas potencialmente aterogénicas (LDL, VLDL, IDL, Lp(a)) — se obtiene restando el HDL-C del colesterol total. A diferencia de LDL-C (que depende de la fórmula de Friedewald y se invalida con triglicéridos altos), el colesterol no-HDL **no requiere ayuno** y sigue siendo válido incluso con triglicéridos elevados, lo que lo hace operativamente más robusto.

## C. Espécimen y toma

### Espécimen y laboratorio

No aplica obtención directa — es un cálculo derivado del perfil lipídico ya obtenido (ver `total_cholesterol.md` y `hdl_c.md`). Unidad: mg/dL (misma que sus componentes).

### Fórmula y limitaciones (obligatorio para parámetro calculado)

- **Fórmula:** Colesterol no-HDL = Colesterol total − HDL-C.
- **Variables necesarias:** Colesterol total, HDL-C (ambos medidos).
- **Versión de la fórmula:** cálculo aritmético directo, sin variantes metodológicas (a diferencia de LDL-C, que sí tiene versiones — Friedewald vs Martin-Hopkins).
- **Ventaja sobre LDL-C:** no se invalida con triglicéridos elevados y no requiere ayuno.
- **Cuándo NO debe calcularse:** si falta cualquiera de las dos variables de entrada (colesterol total o HDL-C).
- **Cuándo el cálculo puede ser inválido:** prácticamente nunca, dado que es una resta directa entre dos valores medidos — su principal limitación no es de cálculo sino de interpretación (ver sección E).

## E. Interpretación

- **Elevado:** mayor carga de partículas potencialmente aterogénicas en conjunto (no solo LDL).
- Especialmente útil en personas con triglicéridos elevados, donde LDL-C calculado por Friedewald pierde precisión o se invalida — el colesterol no-HDL se mantiene confiable en ese escenario.
- **Dentro del intervalo:** no descarta un perfil de partículas aterogénicas anormal si ApoB no ha sido evaluado (algunas personas tienen partículas LDL pequeñas y densas, más aterogénicas, con colesterol no-HDL aparentemente normal).

## F. Contexto del paciente y confusores

### Contexto del paciente

Los mismos que colesterol total y HDL-C: antecedentes familiares de enfermedad cardiovascular precoz, tabaquismo, diabetes, presión arterial.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Colesterol total, HDL-C (variables de origen), LDL-C, ApoB (para refinar cuando triglicéridos están elevados o hay sospecha de partículas pequeñas y densas).
- `pattern_examples`: triglicéridos elevados + LDL-C no calculable de forma confiable → colesterol no-HDL se vuelve la métrica lipídica primaria de referencia en ese escenario.
- `cannot_conclude`: diagnóstico de enfermedad cardiovascular a partir de este valor aislado — mismo racional que LDL-C.

## H. Tendencias

### Tendencias temporales

Sigue la misma lógica que el resto del perfil lipídico — la tendencia sostenida en el tiempo es más relevante que un valor puntual.

## I. Prevención

Mismas recomendaciones que LDL-C/colesterol total: hábitos alimentarios, actividad física, seguimiento periódico. Prohibido: decisiones de tratamiento farmacológico automatizadas.

## J. Pruebas complementarias

### Pruebas complementarias posibles

ApoB cuando se busca mayor precisión sobre el número de partículas aterogénicas, especialmente en personas con triglicéridos elevados o síndrome metabólico.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del perfil lipídico de cribado — no diagnóstico de enfermedad cardiovascular por sí solo.

## L. Evidencia

### Evidencia científica

- **Nivel:** el colesterol no-HDL como métrica lipídica está ampliamente respaldado en la literatura de lípidos como alternativa robusta a LDL-C, especialmente en hipertrigliceridemia — es un cálculo aritmético estándar, no requiere una guía específica para su definición matemática.
- **Clinical decision threshold (2026 ACC/AHA/Multisociety Dyslipidemia Guideline, verificado esta sesión):** meta de no-HDL-C <85 mg/dL (2.2 mmol/L) para prevención secundaria en personas de muy alto riesgo ASCVD, presentada junto a la meta de LDL-C <55 mg/dL. La guía no especifica una meta de no-HDL-C independiente para las demás categorías de riesgo (límite/intermedio, alto) — para esas categorías, Saludly debe usar la aproximación práctica ampliamente reconocida de LDL-C objetivo + 30 mg/dL, señalando que es una regla práctica y no una meta formal de la guía en esas categorías.
- **URL fuente:** https://www.jacc.org/doi/10.1016/j.jacc.2026.02.4872 ; https://newsroom.heart.org/news/accaha-issue-updated-guideline-for-managing-lipids-cholesterol — verificadas esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "medida más robusta que LDL-C cuando hay triglicéridos elevados; considerar junto al resto del perfil lipídico".
- **prohibited_inferences:** "colesterol no-HDL alto = enfermedad cardiovascular" (mismo racional que LDL-C).
- **uncertainty_notes:** al ser un cálculo directo, no tiene la limitación de invalidación por triglicéridos que sí tiene LDL-C (Friedewald) — esto debe comunicarse como ventaja operativa, no confundirse con mayor precisión diagnóstica inherente.
- **professional_review:** valores marcadamente elevados combinados con otros factores de riesgo cardiovascular.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - lipid_profile
  - calculated_parameter
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando riesgo cardiovascular lipídico"
  - "triglicéridos elevados invalidan o reducen la precisión de LDL-C calculado"

combine_with: [total_cholesterol, hdl_c, ldl_c, apob]

do_not_use_alone:
  - "diagnóstico o descarte de enfermedad cardiovascular"

do_not_conclude:
  - "presencia o ausencia de enfermedad cardiovascular a partir de este valor aislado"

escalate_when:
  - "valor marcadamente elevado combinado con otros factores de riesgo cardiovascular"
```
