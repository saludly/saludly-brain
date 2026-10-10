---
doc_id: SLD-BIO-014
biomarker_id: eosinophils_pct
name_es: Eosinófilos %
name_en: Eosinophils %
abbreviation: Eos%
sinonimos:
- Eosinófilos %
- EOS%
- Eos%
- Eosinophils %
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-A03
combine_with:
- wbc
- iga
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

# Eosinófilos %

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-A03. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-014. Eos%. Categoría: Hematología. Tipo: analito medido. Tier 3 — útil solo con sospecha alérgica/parasitaria, sin valor preventivo general aislado.

## B. Definición

Proporción de eosinófilos, células asociadas a respuestas alérgicas y defensa contra parásitos.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo con diferencial · Tubo EDTA. Unidad: %. No requiere ayuno.

## D. Intervalos y umbrales

- **Clinical decision threshold (verificado esta sesión):** rango normal **1-4% del diferencial** (algunas fuentes hasta 7%), absoluto 0-450-500/µL. Eosinofilia leve 500-1,500/µL; moderada 1,500-5,000/µL; severa >5,000/µL (esta última amerita evaluación urgente por riesgo de daño de órgano).
- **URL fuente:** https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589

## E. Interpretación

- **Elevados (eosinofilia):** alergias (rinitis alérgica, asma, dermatitis atópica), infección parasitaria (especialmente helmintos), reacciones a medicamentos, en raros casos procesos hematológicos.

## F. Contexto del paciente y confusores

### Contexto del paciente

Síntomas alérgicos, viajes recientes/exposición a zonas endémicas de parásitos, medicamentos recientes (reacción de hipersensibilidad).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: WBC total, IgA/IgE (no incluida en el catálogo actual — candidato para futuro lote) si hay sospecha alérgica.
- `cannot_conclude`: causa específica sin historia clínica dirigida (alergia vs parásito vs medicamento).

## H. Tendencias

### Tendencias temporales

Fluctúa con exposición alergénica estacional — no es alarmante de forma aislada y leve.

## I. Prevención

Utilidad limitada como marcador preventivo — relevante ante síntomas específicos.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Estudio parasitológico en heces si hay sospecha de infección parasitaria y antecedente de exposición.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado poblacional — Tier 3, indicación específica.

## L. Evidencia

### Evidencia científica

- **Fuente:** valores de referencia CBC estándar. https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "eosinófilos elevados, considerar causa alérgica o parasitaria según contexto de síntomas/exposición".
- **prohibited_inferences:** diagnóstico específico de infección parasitaria sin estudio parasitológico.
- **uncertainty_notes:** elevaciones leves con causa alérgica evidente no requieren alarma.
- **professional_review:** eosinofilia marcada sin causa evidente, o síntomas alérgicos/parasitarios significativos.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - allergy
  - parasitic_infection
  - tier_3
  - saludly_brain_v1
use_when:
  - "síntomas alérgicos o sospecha de infección parasitaria"
combine_with: [wbc, iga]
do_not_use_alone:
  - "diagnóstico de infección parasitaria específica"
do_not_conclude:
  - "infección parasitaria confirmada sin estudio parasitológico"
escalate_when:
  - "eosinofilia marcada sin causa evidente"
```
