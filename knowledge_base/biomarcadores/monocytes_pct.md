---
doc_id: SLD-BIO-013
biomarker_id: monocytes_pct
name_es: Monocitos %
name_en: Monocytes %
abbreviation: Mono%
sinonimos:
- Monocitos %
- MONO%
- Mono%
- Monocytes %
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-012
combine_with:
- wbc
- neutrophils_abs
- lymphocytes_abs
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Monocitos %

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-012. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-013. Mono%. Categoría: Hematología. Tipo: analito medido. Tier 3.

## B. Definición

Proporción de monocitos, células que se diferencian en macrófagos tisulares. Elevaciones leves son frecuentes e inespecíficas; su valor clínico aislado en un panel preventivo ambulatorio es limitado.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo con diferencial · Tubo EDTA. Unidad: %. No requiere ayuno.

## D. Intervalos y umbrales

- **Clinical decision threshold (verificado esta sesión):** rango normal **2-8% del diferencial**, absoluto 0-800/µL.
- **URL fuente:** https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589

## E. Interpretación

- **Elevados:** recuperación de infección aguda (fase de resolución), infecciones crónicas (tuberculosis, endocarditis subaguda), enfermedad inflamatoria crónica, en raros casos procesos hematológicos primarios.
- Elevaciones leves aisladas son frecuentes y con frecuencia no significativas.

## F. Contexto del paciente y confusores

### Contexto del paciente

Infección reciente en fase de resolución, enfermedad inflamatoria crónica conocida.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: WBC total, resto del diferencial.
- `cannot_conclude`: causa específica sin contexto clínico e historia dirigida.

## H. Tendencias

### Tendencias temporales

Una elevación leve transitoria en recuperación de infección no es preocupante; persistencia sostenida amerita más atención.

## I. Prevención

Utilidad preventiva mínima de forma aislada.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna específica sin sospecha clínica dirigida.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica por sí sola.

## L. Evidencia

### Evidencia científica

- **Fuente:** valores de referencia CBC estándar. https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "monocitos elevados, considerar fase de recuperación de infección o proceso inflamatorio crónico si es persistente".
- **prohibited_inferences:** diagnóstico específico (tuberculosis, endocarditis, proceso hematológico) sin evaluación clínica dirigida.
- **uncertainty_notes:** elevaciones leves aisladas son frecuentes y con frecuencia no significativas.
- **professional_review:** elevación marcada y persistente sin causa evidente.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - tier_3
  - saludly_brain_v1
use_when:
  - "evaluando diferencial completo ante sospecha de infección crónica"
combine_with: [wbc, neutrophils_abs, lymphocytes_abs]
do_not_use_alone:
  - "diagnóstico de infección crónica específica"
do_not_conclude:
  - "tuberculosis, endocarditis u otra condición específica sin evaluación dirigida"
escalate_when:
  - "elevación marcada y persistente sin causa evidente"
```
