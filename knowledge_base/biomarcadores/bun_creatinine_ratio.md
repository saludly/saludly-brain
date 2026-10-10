---
doc_id: SLD-BIO-064
biomarker_id: bun_creatinine_ratio
name_es: Relación BUN/Creatinina
name_en: BUN/Creatinine Ratio
abbreviation: BUN/Cr
sinonimos:
- Relación BUN/creatinina
- Relación BUN/Creatinina
- BUN/Cr
- BUN/Creatinine Ratio
category: renal
parameter_type: derived_ratio
tipo_resultado: numérico
unidad_canonica: sin unidad
specimen: No aplica (calculado)
nivel_catalogo: solo valor y rango
panel: calculado
sexo: ambos
alimenta:
- SEG-014
combine_with:
- bun
- creatinine
- egfr
- sodium
formula: BUN/Creatinina = BUN [mg/dL] ÷ Creatinina [mg/dL]
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

# Relación BUN/Creatinina

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-014. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-064. BUN/Cr. Categoría: Riñón. Tipo: **relación derivada**. Tier 3 — solo útil ante función renal ya alterada, no como cribado.

## B. Definición

Cociente entre BUN y creatinina. Como el BUN es más sensible que la creatinina a factores prerrenales (deshidratación, sangrado digestivo, dieta alta en proteína) mientras que la creatinina refleja más específicamente la filtración glomerular, un ratio desproporcionadamente alto orienta hacia causa prerrenal en vez de daño renal intrínseco.

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio — relación derivada)

- **Fórmula:** BUN/Creatinina = BUN [mg/dL] ÷ Creatinina [mg/dL].
- **Variables necesarias:** BUN, Creatinina (ambas del mismo momento).
- **Cuándo NO debe calcularse:** si BUN y creatinina no son de la misma muestra.
- **Limitación:** solo tiene valor interpretativo cuando la función renal ya está alterada (eGFR bajo o creatinina elevada) — calcularlo con ambos valores normales no aporta información clínica relevante.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende de las variables de entrada.
- **Clinical decision threshold (ampliamente reproducido en fisiología clínica/nefrología estándar):** relación BUN/Creatinina normal aproximadamente **10:1 a 15:1** (usando BUN 7-23 mg/dL y Creatinina 0.6-1.2 mg/dL, ambos ya verificados esta sesión — ver `bun.md`, `creatinine.md`). Un ratio **>20:1** con función renal alterada sugiere causa prerrenal (deshidratación, sangrado digestivo, insuficiencia cardíaca); un ratio dentro de lo normal con función renal alterada sugiere causa renal intrínseca.

## E. Interpretación

- **Ratio elevado con función renal alterada:** sugiere causa prerrenal — deshidratación, sangrado digestivo, insuficiencia cardíaca (bajo flujo renal), dieta alta en proteína.
- **Ratio normal con función renal alterada:** sugiere causa renal intrínseca (daño estructural del riñón) más que prerrenal.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: hidratación, dieta reciente, antecedente de sangrado digestivo, insuficiencia cardíaca conocida.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: BUN, Creatinina/eGFR (variables de entrada), Sodio (contexto de hidratación).
- `cannot_conclude`: diagnóstico definitivo de la causa sin evaluación clínica dirigida — el ratio orienta, no confirma.

## H. Tendencias

### Tendencias temporales

Relevante principalmente en el contexto de un cambio agudo de función renal — su valor es más de orientación puntual que de seguimiento longitudinal.

## I. Prevención

No aplica como marcador preventivo — es una herramienta de orientación diagnóstica ante función renal ya alterada.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Evaluación de hidratación, revisión de medicamentos, considerar sangrado digestivo oculto si el ratio es desproporcionadamente alto sin causa evidente.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado — es una herramienta de orientación diagnóstica exclusivamente en el contexto de función renal ya alterada.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento de fisiología renal estándar, ampliamente reproducido en nefrología clínica.
- **Fuente:** derivado de rangos de BUN y Creatinina ya verificados esta sesión, combinado con el principio de fisiología renal ampliamente reproducido en nefrología clínica (regla de 10:1-20:1) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "ratio BUN/Creatinina elevado en contexto de función renal alterada, sugiere considerar causa prerrenal (hidratación, sangrado digestivo) antes que daño renal intrínseco".
- **prohibited_inferences:** calcular o interpretar este ratio cuando BUN y creatinina están ambos normales (no aporta información); diagnóstico definitivo de la causa sin evaluación clínica.
- **uncertainty_notes:** solo tiene valor interpretativo cuando la función renal de base ya está alterada.
- **professional_review:** ratio marcadamente elevado con función renal alterada, especialmente si hay sospecha de sangrado digestivo o deshidratación significativa.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - renal
  - kidney_function
  - derived_ratio
  - tier_3
  - saludly_brain_v1

use_when:
  - "función renal ya alterada (eGFR bajo o creatinina elevada), para orientar causa"

combine_with: [bun, creatinine, egfr, sodium]

do_not_use_alone:
  - "diagnóstico definitivo de causa prerrenal vs renal intrínseca"

do_not_conclude:
  - "causa específica sin evaluación clínica dirigida"

escalate_when:
  - "ratio marcadamente elevado con función renal alterada"
  - "sospecha de sangrado digestivo o deshidratación significativa"
```
