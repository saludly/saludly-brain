---
doc_id: SLD-BIO-050
biomarker_id: apob
name_es: Apolipoproteína B
name_en: Apolipoprotein B
abbreviation: ApoB
sinonimos:
- Apolipoproteína B
- ApoB
- Apo B
- Apolipoproteína B (ApoB)
- Apolipoprotein B
category: cardiovascular_lipids
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-CA-A01
combine_with:
- ldl_c
- non_hdl_c
- triglycerides
- apoa1
- apob_apoa1_ratio
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Discordancia con LDL desde 130 mg/dL (COND-M1-CA-A01).
---

# Apolipoproteína B (ApoB)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Discordancia con LDL desde 130 mg/dL (COND-M1-CA-A01).
- Reglas que usan esta ficha: COND-M1-CA-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-050. ApoB. Categoría: Cardiovascular/Lípidos. Tipo: analito medido. Tier 2 (panel avanzado — no rutinario para todos).

## B. Definición

Proteína estructural presente en una copia por cada partícula LDL, VLDL, IDL y quilomicrón remanente — es decir, ApoB cuenta el **número total de partículas aterogénicas**, a diferencia de LDL-C/no-HDL-C que miden la masa de colesterol que transportan. Dos personas pueden tener el mismo LDL-C con números de partículas muy distintos (partículas pequeñas y densas vs grandes) — ApoB captura esa diferencia.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Perfil lipídico avanzado · Método: inmunoturbidimetría o inmunonefelometría estandarizada. Unidad: mg/dL. No requiere ayuno estricto (a diferencia de triglicéridos/LDL-C calculado).

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (National Lipid Association, Expert Clinical Consensus, *J Clin Lipidology* 2024):** umbrales de ApoB sugeridos según categoría de riesgo ASCVD — **muy alto riesgo: <60 mg/dL** · **alto riesgo: <70 mg/dL** · **riesgo limítrofe-intermedio: <90 mg/dL** — diseñados para corresponder con las metas actuales de tratamiento de LDL-C y no-HDL-C.
- **Risk-enhancing threshold:** ApoB ≥130 mg/dL corresponde aproximadamente al percentil 90 de la población adulta no tratada — factor de riesgo adicional que amerita conversación clínico-paciente sobre inicio/intensificación de tratamiento hipolipemiante.
- **URL fuente:** https://www.lipidjournal.com/article/S1933-2874(24)00240-X/fulltext — verificado esta sesión (ago-2026).
- **Contexto AHA/ACC 2026 (guía actualizada de manejo de lípidos, verificada esta sesión):** ApoB se recomienda para evaluar riesgo residual y guiar tratamiento en personas con síndrome cardiovascular-renal-metabólico, diabetes tipo 2, triglicéridos altos, o enfermedad cardiovascular conocida que ya alcanzaron sus metas de LDL-C/no-HDL-C. Fuente: https://www.acc.org/about-acc/press-releases/2026/03/13/18/01/accaha-issue-updated-guideline-for-managing-lipids-cholesterol

## E. Interpretación

**Elevado:** mayor número de partículas aterogénicas circulantes, independientemente de la masa de colesterol que transporten — relevante especialmente en triglicéridos altos, diabetes, síndrome metabólico, donde predominan partículas LDL pequeñas y densas con LDL-C aparentemente normal pero ApoB alto.

**Dentro del intervalo:** en general tranquilizador, pero debe interpretarse en conjunto con LDL-C/no-HDL-C — discordancia entre ellos (LDL-C bajo, ApoB alto) es precisamente el escenario donde ApoB aporta más valor.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: triglicéridos concurrentes, diabetes/resistencia a la insulina, antecedente de enfermedad cardiovascular, tratamiento hipolipemiante actual.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: LDL-C, no-HDL-C, Triglicéridos, ApoA1 (para el ratio ApoB/ApoA1).
- `pattern_examples`: LDL-C normal + ApoB elevado (discordancia) = partículas pequeñas y densas, mayor riesgo del sugerido por LDL-C solo — patrón típico de resistencia a la insulina/síndrome metabólico.
- `conflicting_patterns`: hipertrigliceridemia severa con quilomicronemia, donde el objetivo primario es reducir triglicéridos (riesgo de pancreatitis), no ApoB.
- `cannot_conclude`: diagnóstico de enfermedad cardiovascular — ApoB es un refinamiento de estratificación de riesgo, no una prueba diagnóstica.

## H. Tendencias

### Tendencias temporales

Relativamente estable en el tiempo salvo cambios significativos de peso, tratamiento o control metabólico — útil para seguimiento de respuesta a intervención (estilo de vida o farmacológica) en quienes ya lo tienen elevado.

## I. Prevención

Acciones razonablemente relacionadas: manejo de peso, actividad física, control de triglicéridos/glucosa cuando aplique.

## J. Pruebas complementarias

### Pruebas complementarias posibles

ApoA1 (para calcular el ratio ApoB/ApoA1); considerar en conjunto con evaluación de riesgo cardiovascular global, no de forma aislada.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado poblacional universal (por eso es Tier 2, `not_routine_for_everyone: true`) — es una prueba de refinamiento de riesgo en personas con indicación específica (`indications_for_testing` en el frontmatter).

## L. Evidencia

### Evidencia científica

- **Expert Clinical Consensus (evidencia fuerte):** National Lipid Association. "Role of apolipoprotein B in the clinical management of cardiovascular risk in adults." *J Clin Lipidology* 2024. https://www.lipidjournal.com/article/S1933-2874(24)00240-X/fulltext
- **Guideline (fuerte):** ACC/AHA Updated Guideline for Managing Lipids, Cholesterol, 2026. https://www.acc.org/about-acc/press-releases/2026/03/13/18/01/accaha-issue-updated-guideline-for-managing-lipids-cholesterol
- Ambas verificadas por búsqueda web esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "ApoB elevado sugiere mayor número de partículas aterogénicas, especialmente relevante si hay discordancia con LDL-C; considerar como refinamiento de riesgo cardiovascular junto al resto del perfil".
- **prohibited_inferences:** "ApoB alto = enfermedad cardiovascular"; recomendar inicio de tratamiento hipolipemiante (decisión médica).
- **uncertainty_notes:** no debe ofrecerse como prueba de cribado universal — Saludly debe presentarlo solo cuando el usuario cumple alguna de las `indications_for_testing`.
- **professional_review:** ApoB ≥130 mg/dL, o discordancia relevante con LDL-C en persona con factores de riesgo cardiovascular ya conocidos.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - lipid_advanced
  - tier_2
  - saludly_brain_v1

use_when:
  - "triglicéridos elevados o síndrome metabólico presente"
  - "LDL-C en meta pero se sospecha riesgo residual"
  - "refinando riesgo cardiovascular más allá del panel básico"

combine_with: [ldl_c, non_hdl_c, triglycerides, apoa1, apob_apoa1_ratio]

do_not_use_alone:
  - "diagnóstico o descarte de enfermedad cardiovascular"
  - "decisión de tratamiento farmacológico"

do_not_conclude:
  - "presencia confirmada de enfermedad cardiovascular"

escalate_when:
  - "ApoB ≥130 mg/dL"
  - "discordancia marcada con LDL-C en persona con factores de riesgo cardiovascular conocidos"
```
