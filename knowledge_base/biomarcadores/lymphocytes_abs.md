---
doc_id: SLD-BIO-012
biomarker_id: lymphocytes_abs
name_es: Linfocitos Absolutos
name_en: Absolute Lymphocyte Count
abbreviation: ALC
sinonimos:
- Linfocitos absolutos
- LYM#
- Linfocitos Absolutos
- ALC
- Absolute Lymphocyte Count
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
- REL-030
combine_with:
- wbc
- neutrophils_abs
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

# Linfocitos Absolutos (ALC)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-012. ALC. Categoría: Hematología. Tipo: analito medido. Tier 2 — más accionable que el porcentaje.

## B. Definición

Número absoluto de linfocitos circulantes (células T, B y NK combinadas — sin desglose en el hemograma estándar). Central en la respuesta inmune adaptativa y frente a infecciones virales.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo con diferencial · Tubo EDTA · Método: citometría de flujo automatizada. Unidad: células/µL o ×10³/µL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método, con variación relevante por edad (los niños tienen linfocitosis relativa fisiológica).
- **Clinical decision threshold (verificado esta sesión):** rango normal absoluto **1,000-4,800/µL (1.0-4.8 ×10³/µL)** según fuentes institucionales estándar.
- **URL fuente:** https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589

## E. Interpretación

- **Elevado (linfocitosis):** infección viral (causa más frecuente en ambulatorios), en niños puede ser fisiológico.
- **Disminuido (linfopenia):** infección viral aguda (puede cursar con linfopenia transitoria, ej. COVID-19), corticoides, procesos autoinmunes, inmunodeficiencia.

## F. Contexto del paciente y confusores

### Contexto del paciente

Edad (linfocitosis relativa fisiológica en niños), infección viral reciente, medicamentos (corticoides), antecedente autoinmune.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: WBC total, Neutrófilos absolutos (el patrón neutrófilos vs linfocitos ayuda a diferenciar infección bacteriana de viral).
- `pattern_examples`: linfocitosis con neutrófilos normales/bajos = más compatible con infección viral; neutrofilia con linfocitos normales/bajos = más compatible con infección bacteriana.
- `cannot_conclude`: tipo específico de infección sin evaluación clínica.

## H. Tendencias

### Tendencias temporales

Cambia en días ante procesos agudos — no es marcador de tendencia longitudinal lenta.

## I. Prevención

Utilidad ante sospecha de infección viral, no como cribado preventivo independiente.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna adicional específica — evaluación clínica del contexto infeccioso.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica por sí sola.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico/inmunológico estándar.
- **Fuente:** valores de referencia CBC estándar. https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "linfocitos alterados, considerar junto a neutrófilos para diferenciar patrón viral vs bacteriano".
- **prohibited_inferences:** diagnóstico de infección específica o inmunodeficiencia sin evaluación clínica dirigida.
- **uncertainty_notes:** en niños, la linfocitosis relativa es fisiológica — considerar edad antes de interpretar como alterado.
- **professional_review:** linfopenia marcada persistente, o linfocitosis marcada sin causa infecciosa evidente (considerar evaluación hematológica).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - immune_inflammation
  - tier_2
  - saludly_brain_v1
use_when:
  - "diferenciando patrón viral vs bacteriano junto a neutrófilos"
combine_with: [wbc, neutrophils_abs]
do_not_use_alone:
  - "diagnóstico de tipo de infección"
do_not_conclude:
  - "inmunodeficiencia sin evaluación clínica dirigida"
escalate_when:
  - "linfopenia marcada persistente"
  - "linfocitosis marcada sin causa infecciosa evidente"
```
