---
doc_id: SLD-BIO-035
biomarker_id: phosphorus
name_es: Fósforo
name_en: Phosphorus
abbreviation: P
sinonimos:
- Fósforo
- P
- Fosfato
- Phosphorus
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- SEG-008
combine_with:
- calcium
- pth
- creatinine
- egfr
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Según el Consolidado, es refleja junto con la PTH cuando el calcio corregido sale alto. Los PDF de ejemplo lo traen en el panel estándar: hay que decidir cuál de las dos versiones queda.'
---

# Fósforo

## Notas de decisión de Saludly (6 de octubre de 2026)

- Según el Consolidado, es refleja junto con la PTH cuando el calcio corregido sale alto. Los PDF de ejemplo lo traen en el panel estándar: hay que decidir cuál de las dos versiones queda.
- Reglas que usan esta ficha: SEG-008. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-035. P. Categoría: Metabolismo (relación cruzada con hueso y riñón). Tipo: analito medido. Tier 3 — relevante principalmente junto a calcio/PTH en contexto renal/óseo, no como cribado aislado.

## B. Definición

Mineral esencial para la estructura ósea, la producción de energía celular (ATP) y la regulación ácido-base. Su homeostasis está estrechamente ligada a calcio, PTH y vitamina D.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico estandarizado. Unidad: mg/dL. **Ayuno recomendado** — la ingesta reciente de alimentos altera el fósforo sérico de forma más marcada que otros electrolitos.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método, con variación fisiológica por edad (más alto en niños en crecimiento).
- **Clinical decision threshold (verificado esta sesión):** rango normal en adultos **2.3-4.7 mg/dL** (varía entre fuentes: 3.0-4.5 vs 2.3-4.7 mg/dL). Rango más alto en niños (3.7-5.6 mg/dL) por crecimiento óseo activo — confirma la nota de variación fisiológica por edad ya señalada.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevado:** insuficiencia renal (causa más frecuente — el riñón es el principal regulador de excreción de fósforo), hipoparatiroidismo, exceso de vitamina D.
- **Disminuido:** hiperparatiroidismo, deficiencia de vitamina D, desnutrición severa, síndrome de realimentación (refeeding syndrome — relevante en contextos de desnutrición tratada).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: función renal, edad (crecimiento), estado nutricional, ayuno al momento de la toma.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Calcio (obligatorio — su regulación está entrelazada), PTH, Creatinina/eGFR (la función renal es determinante central).
- `pattern_examples`: fósforo alto + calcio bajo + eGFR bajo = patrón compatible con enfermedad renal crónica avanzada con alteración del metabolismo mineral óseo.
- `cannot_conclude`: causa específica sin PTH y función renal.

## H. Tendencias

### Tendencias temporales

En enfermedad renal crónica, el fósforo tiende a elevarse progresivamente conforme avanza la enfermedad — relevante para seguimiento longitudinal en ese contexto específico.

## I. Prevención

Utilidad limitada como marcador preventivo aislado — más relevante en seguimiento de enfermedad renal o metabolismo óseo ya identificados.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Calcio, PTH, función renal si no están disponibles.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado poblacional independiente — Tier 3, relevante en contexto renal/óseo específico.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento de fisiología mineral ósea/renal estándar.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "fósforo alterado, interpretar junto a calcio, PTH y función renal".
- **prohibited_inferences:** diagnóstico de enfermedad renal o paratiroidea a partir de fósforo aislado.
- **uncertainty_notes:** su interpretación depende fuertemente del contexto renal — poco informativo sin función renal concurrente.
- **professional_review:** alteración marcada combinada con función renal reducida o calcio alterado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - electrolytes
  - bone_metabolism
  - renal
  - tier_3
  - saludly_brain_v1

use_when:
  - "evaluando metabolismo óseo o mineral en contexto renal"

combine_with: [calcium, pth, creatinine, egfr]

do_not_use_alone:
  - "diagnóstico de enfermedad renal o paratiroidea"

do_not_conclude:
  - "causa específica sin PTH y función renal"

escalate_when:
  - "alteración marcada combinada con función renal reducida o calcio alterado"
```
