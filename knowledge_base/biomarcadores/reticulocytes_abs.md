---
doc_id: SLD-BIO-019
biomarker_id: reticulocytes_abs
name_es: Reticulocitos Absolutos
name_en: Absolute Reticulocyte Count
abbreviation: ARC
sinonimos:
- Reticulocitos absolutos
- Reticulocitos Absolutos
- ARC
- Absolute Reticulocyte Count
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: x10³/µL
specimen: Sangre total EDTA
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M3-HE-001
- COND-M4-GA-A01
combine_with:
- reticulocytes_pct
- hemoglobin
- mcv
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

# Reticulocitos Absolutos (ARC)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-001, COND-M4-GA-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-019. ARC. Categoría: Hematología. Tipo: analito medido. Tier 3 — más útil clínicamente que el porcentaje, mismo racional de indicación.

## B. Definición

Número absoluto de reticulocitos circulantes. Más preciso que el porcentaje cuando el conteo total de eritrocitos está alterado (situación común en anemia), porque no depende de la proporción relativa a un denominador que también cambió.

## C. Espécimen y toma

### Espécimen y laboratorio

Igual que reticulocitos %: sangre venosa, tubo EDTA, citometría de flujo. Unidad: células/µL o ×10³/µL.

## D. Intervalos y umbrales

- **Clinical decision threshold (verificado esta sesión):** derivado del porcentaje (0.5-2.6%, ver `reticulocytes_pct.md`) combinado con el conteo total de eritrocitos — el valor absoluto normal aproximado en adultos es **25,000-75,000/µL**, calculado a partir del rango de porcentaje y el conteo eritrocitario normal.
- **URL fuente:** ver `reticulocytes_pct.md` para fuentes primarias (NCCPA, ClinicalTrials.gov) — verificado esta sesión (ago-2026).

## E. Interpretación

### Interpretación

Mismo racional que reticulocitos % pero con mayor precisión al no depender de un denominador alterado — preferible sobre el porcentaje cuando ambos están disponibles.

### (abreviado por redundancia con reticulocitos %)

Ver `reticulocytes_pct.md` para contexto de paciente, relaciones, tendencias, prevención y screening — idénticos, con la ventaja de mayor precisión del valor absoluto.

## L. Evidencia

### Evidencia científica

- **Fuente:** ver `reticulocytes_pct.md` — mismas fuentes, valor absoluto derivado matemáticamente.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** igual que reticulocitos %, con mayor confianza por ser el valor absoluto.
- **prohibited_inferences:** igual que reticulocitos %.
- **uncertainty_notes:** preferible sobre el porcentaje cuando el conteo eritrocitario está muy alterado.
- **professional_review:** igual criterio que reticulocitos %.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - anemia_workup
  - tier_3
  - saludly_brain_v1
use_when:
  - "anemia ya documentada, para evaluar respuesta medular con precisión"
combine_with: [reticulocytes_pct, hemoglobin, mcv]
do_not_use_alone:
  - "cualquier interpretación sin anemia documentada"
do_not_conclude:
  - "causa específica sin ferritina/B12/folato/evidencia de hemólisis"
escalate_when:
  - "igual criterio que reticulocytes_pct"
```
