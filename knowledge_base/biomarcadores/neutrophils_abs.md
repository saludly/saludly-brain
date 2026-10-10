---
doc_id: SLD-BIO-010
biomarker_id: neutrophils_abs
name_es: Neutrófilos Absolutos
name_en: Absolute Neutrophil Count
abbreviation: ANC
sinonimos:
- Neutrófilos absolutos
- Recuento de neutrófilos
- NEU#
- Neutrófilos Absolutos
- ANC
- Absolute Neutrophil Count
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: x10³/µL
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-A02
- COND-M3-HE-010
- REL-030
combine_with:
- wbc
- lymphocytes_abs
- hs_crp
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

# Neutrófilos Absolutos (ANC)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-010. ANC. Categoría: Hematología. Tipo: analito medido (derivado del diferencial %, reportado también como valor absoluto por el analizador). Tier 2 — más accionable que el porcentaje para decisiones clínicas.

## B. Definición

Número absoluto de neutrófilos circulantes — la primera línea de defensa contra infecciones bacterianas. Es más informativo que el porcentaje de neutrófilos porque el porcentaje puede parecer alterado solo por cambios en otras líneas celulares (ej. linfopenia relativa eleva el % de neutrófilos sin que su número absoluto haya cambiado).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo con diferencial · Tubo EDTA · Método: citometría de flujo automatizada. Unidad: células/µL o ×10³/µL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (referencia institucional UI Health Care / valores CBC estándar, verificado esta sesión):** rango normal absoluto **1,800-7,800/µL (1.8-7.8 ×10³/µL)**. Neutropenia leve 1,000-1,500/µL; moderada 500-1,000/µL; severa <500/µL (riesgo significativo de infección grave) — estos subcortes de severidad son ampliamente usados en oncología/hematología clínica.
- **URL fuente:** https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589

## E. Interpretación

- **Elevado (neutrofilia):** infección bacteriana, inflamación aguda, estrés/corticoides, tabaquismo.
- **Disminuido (neutropenia):** infección viral, medicamentos (quimioterapia, ciertos antibióticos/antipsicóticos), procesos autoinmunes, causas hematológicas. Neutropenia marcada aumenta significativamente el riesgo de infección grave.

## F. Contexto del paciente y confusores

### Contexto del paciente

Medicamentos (quimioterapia, clozapina, ciertos antibióticos), infección/inflamación reciente, fiebre concurrente.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: WBC total, Linfocitos absolutos, hs-CRP.
- `pattern_examples`: neutrofilia + hs-CRP elevada = patrón compatible con infección/inflamación bacteriana aguda.
- `cannot_conclude`: foco específico de infección sin evaluación clínica.

## H. Tendencias

### Tendencias temporales

Cambia rápidamente en horas-días ante procesos agudos — no es un buen marcador de tendencia longitudinal lenta.

## I. Prevención

Utilidad principalmente ante sospecha de infección/inflamación, no como cribado preventivo independiente.

## J. Pruebas complementarias

### Pruebas complementarias posibles

hs-CRP, evaluación clínica de foco infeccioso si hay neutrofilia marcada con fiebre.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica por sí sola de infección — es parte del hemograma diferencial de apoyo.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar.
- **Fuente:** valores de referencia CBC estándar de laboratorio clínico (UI Health Care, hospital académico). https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026). Nivel de evidencia: referencia institucional estándar.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "neutrófilos alterados, compatible con posible proceso infeccioso/inflamatorio (si elevados) o riesgo de infección (si muy disminuidos)".
- **prohibited_inferences:** "tiene una infección bacteriana" sin contexto clínico; diagnóstico hematológico específico sin evaluación dirigida.
- **uncertainty_notes:** cambia rápidamente — un valor puntual refleja el momento, no una tendencia.
- **professional_review:** neutropenia marcada (riesgo de infección grave), o neutrofilia marcada con fiebre/síntomas sistémicos.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - immune_inflammation
  - tier_2
  - saludly_brain_v1
use_when:
  - "evaluando sospecha de infección bacteriana o riesgo de neutropenia"
combine_with: [wbc, lymphocytes_abs, hs_crp]
do_not_use_alone:
  - "diagnóstico de infección o condición hematológica"
do_not_conclude:
  - "tiene infección bacteriana sin contexto clínico"
escalate_when:
  - "neutropenia marcada"
  - "neutrofilia marcada con fiebre o síntomas sistémicos"
```

## N. Nota de consolidación (auditoría posterior)
**Neutrófilos % se consolidó dentro de este registro** — ya estaba documentado que el porcentaje no debe interpretarse sin el valor absoluto (puede alterarse solo por cambios en otras líneas celulares sin cambio real en neutrófilos). Cálculo para referencia: Neutrófilos % = (Neutrófilos absolutos / WBC total) × 100. Si Saludly Brain necesita el porcentaje específicamente, debe calcularlo bajo demanda, sin mantenerlo como registro separado — ver `AUDIT_CHANGELOG` en `00_INDEX.md`.
