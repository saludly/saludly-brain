---
doc_id: SLD-BIO-062
biomarker_id: bun
name_es: BUN / Urea
name_en: Blood Urea Nitrogen
abbreviation: BUN
sinonimos:
- BUN
- Nitrógeno ureico
- Nitrógeno ureico en sangre
- BUN / Urea
- Blood Urea Nitrogen
category: renal
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-014
combine_with:
- creatinine
- egfr
- bun_creatinine_ratio
- sodium
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# BUN (Nitrógeno Ureico en Sangre) / Urea

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-014. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-062. BUN. Categoría: Riñón. Tipo: analito medido. Tier 2 (panel avanzado — complementa creatinina/eGFR, no sustituye el cribado básico).

## B. Definición

Producto final del catabolismo proteico, sintetizado en el hígado a partir del amoníaco y eliminado por el riñón. A diferencia de la creatinina, el BUN está influenciado significativamente por factores no renales (ingesta proteica, estado de hidratación, sangrado digestivo, función hepática) — por eso se interpreta principalmente en relación con creatinina (ver `bun_creatinine_ratio.md`), no de forma aislada.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método enzimático (ureasa). Unidad: mg/dL (alt: mmol/L de urea — conversión no directa 1:1, BUN y urea miden fracciones relacionadas pero no idénticas del mismo compuesto; Saludly debe registrar cuál reporta el laboratorio aliado). No requiere ayuno. Factor preanalítico: dieta alta en proteína reciente eleva el valor sin reflejar cambio en función renal.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal **7-20 mg/dL** (varía entre fuentes: 7-18 vs 10-20 mg/dL).
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevado:** puede reflejar reducción de función renal (igual que creatinina, pero menos específico), deshidratación (causa prerrenal), dieta alta en proteína, sangrado digestivo (la sangre digerida es una carga proteica adicional), uso de corticoides.
- **Disminuido:** puede reflejar enfermedad hepática severa (síntesis reducida), dieta muy baja en proteína, sobrehidratación.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: hidratación, dieta reciente (proteína), función hepática, antecedente de sangrado digestivo, medicamentos (corticoides).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Creatinina/eGFR (obligatorio para calcular la relación BUN/Creatinina), Sodio (contexto de hidratación).
- `pattern_examples`: BUN elevado + creatinina normal + relación BUN/Creatinina alta = sugiere causa prerrenal (deshidratación, sangrado digestivo) más que daño renal intrínseco.
- `cannot_conclude`: causa específica de la elevación sin el contexto de hidratación, dieta y función hepática.

## H. Tendencias

### Tendencias temporales

Más variable día a día que creatinina por su sensibilidad a factores no renales (dieta, hidratación) — una tendencia sostenida junto con creatinina alterada es más significativa que una fluctuación aislada de BUN solo.

## I. Prevención

Utilidad principal como parte del panel renal ampliado junto a creatinina — no tiene indicación preventiva independiente.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Creatinina/eGFR si no se solicitaron juntas (deberían pedirse siempre en conjunto).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte de un panel renal ampliado — su valor principal es el contexto que aporta a la interpretación de creatinina/eGFR (relación BUN/Creatinina), no como marcador independiente de cribado.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento de fisiología renal estándar, ampliamente reproducido.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "BUN alterado, interpretar junto a creatinina mediante la relación BUN/Creatinina para orientar causa prerrenal vs renal intrínseca".
- **prohibited_inferences:** diagnóstico de enfermedad renal a partir de BUN aislado.
- **uncertainty_notes:** BUN es menos específico que creatinina para función renal — múltiples factores no renales lo alteran.
- **professional_review:** BUN marcadamente elevado, especialmente combinado con creatinina/eGFR ya alterados o sospecha de sangrado digestivo.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - renal
  - kidney_function
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando función renal junto con creatinina/eGFR"
  - "sospecha de causa prerrenal (deshidratación, sangrado digestivo)"

combine_with: [creatinine, egfr, bun_creatinine_ratio, sodium]

do_not_use_alone:
  - "diagnóstico de enfermedad renal"

do_not_conclude:
  - "causa específica de elevación sin contexto de hidratación/dieta/función hepática"

escalate_when:
  - "BUN marcadamente elevado combinado con creatinina/eGFR alterados"
  - "sospecha de sangrado digestivo"
```
