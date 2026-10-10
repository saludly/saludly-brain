---
doc_id: SLD-BIO-011
biomarker_id: lymphocytes_pct
name_es: Linfocitos %
name_en: Lymphocytes %
abbreviation: Linf%
sinonimos:
- Linfocitos %
- LYM%
- Linf%
- Lymphocytes %
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M6-MI-A02
combine_with:
- lymphocytes_abs
- wbc
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

# Linfocitos % (porcentaje)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-011. Linf%. Categoría: Hematología. Tipo: analito medido. Tier 3 — mismo racional que neutrófilos %: se prioriza el valor absoluto.

## B. Definición

Proporción de linfocitos dentro del total de leucocitos — sujeta a la misma limitación que neutrófilos%: puede alterarse solo por cambios en otras líneas celulares.

## C. Espécimen y toma

### Espécimen, laboratorio, umbrales

Ver `wbc.md` y `lymphocytes_abs.md`. Unidad: %.

## E. Interpretación

### Interpretación

No debe interpretarse sin el valor absoluto correspondiente.

### (abreviado por redundancia)

Ver `lymphocytes_abs.md`.

## L. Evidencia

### Evidencia científica

- **Fuente:** valores de referencia CBC estándar (20-40% del diferencial). https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** ninguna sin el valor absoluto concurrente.
- **prohibited_inferences:** cualquier interpretación basada solo en el porcentaje.
- **uncertainty_notes:** el porcentaje puede alterarse sin cambio real en linfocitos.
- **professional_review:** igual criterio que `lymphocytes_abs.md`.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - tier_3
  - saludly_brain_v1
use_when:
  - "siempre junto al conteo absoluto de linfocitos"
combine_with: [lymphocytes_abs, wbc]
do_not_use_alone:
  - "cualquier interpretación sin el valor absoluto"
do_not_conclude:
  - "alteración real sin verificar el valor absoluto"
escalate_when:
  - "igual criterio que lymphocytes_abs"
```
