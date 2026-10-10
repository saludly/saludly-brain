---
doc_id: SLD-BIO-003
biomarker_id: erythrocytes
name_es: Eritrocitos
name_en: Red Blood Cell Count
abbreviation: RBC
sinonimos:
- Recuento de eritrocitos
- Eritrocitos
- Glóbulos rojos
- RBC
- Eritrocitos (conteo)
- Red Blood Cell Count
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: x10⁶/µL
specimen: Sangre total EDTA
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-012
- COND-M3-HE-A04
combine_with:
- hemoglobin
- hematocrit
- mcv
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Eritrocitos (conteo, RBC)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-012. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-003. RBC. Categoría: Hematología. Tipo: analito medido (variable de entrada para calcular VCM/HCM). Tier 2 — valor bajo de forma aislada, se usa principalmente como insumo de cálculo.

## B. Definición

Número total de eritrocitos circulantes por volumen de sangre. Junto a hemoglobina y hematocrito conforma la tríada básica de la serie roja, pero es el menos informativo de los tres de forma aislada — dos personas pueden tener el mismo conteo de eritrocitos con hemoglobina muy distinta si el tamaño celular (VCM) difiere.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo (CBC) · Tubo EDTA · Método: citometría de flujo automatizada. Unidad: ×10⁶/µL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método, ajustado por sexo/altitud (igual racional que hemoglobina).
- **Clinical decision threshold (UI Health Care, verificado esta sesión):** rango normal **hombres 4.5-6.2 millones/µL · mujeres 4.0-5.2 millones/µL** (adultos ≥18 años).
- **URL fuente:** https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589

## E. Interpretación

- Prácticamente nunca se interpreta solo — su valor real está en combinarse con hematocrito para calcular VCM (VCM = Hematocrito×10 / Eritrocitos).
- **Elevado:** policitemia, deshidratación. **Disminuido:** anemia.

## F. Contexto del paciente y confusores

### Contexto del paciente

Igual que hemoglobina/hematocrito: sexo, embarazo, altitud, hidratación.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Hemoglobina, Hematocrito (obligatorio para VCM/HCM).
- `cannot_conclude`: nada relevante sin hemoglobina/hematocrito concurrentes.

## H. Tendencias

### Tendencias temporales

Sigue el mismo patrón que hemoglobina/hematocrito.

## I. Prevención

Su valor preventivo real está en habilitar el cálculo de VCM/HCM, no en sí mismo.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna adicional — es parte del hemograma estándar junto a Hb/Hto.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del hemograma de cribado — sin valor diagnóstico independiente aislado.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar.
- **Fuente:** UI Health Care, tabla de rangos CBC por edad/sexo. https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "eritrocitos alterados, interpretar junto a hemoglobina/hematocrito y VCM calculado".
- **prohibited_inferences:** cualquier diagnóstico a partir del conteo aislado.
- **uncertainty_notes:** biomarcador de bajo valor interpretativo aislado.
- **professional_review:** igual criterio que hemoglobina/hematocrito.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - tier_2
  - saludly_brain_v1
use_when:
  - "calculando VCM/HCM junto a hemoglobina/hematocrito"
combine_with: [hemoglobin, hematocrit, mcv]
do_not_use_alone:
  - "cualquier interpretación sin hemoglobina/hematocrito concurrentes"
do_not_conclude:
  - "causa de anemia/policitemia sin panel completo"
escalate_when:
  - "valores muy alterados combinados con hemoglobina/hematocrito"
```
