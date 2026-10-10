---
doc_id: SLD-BIO-073
biomarker_id: igg
name_es: Inmunoglobulina G
name_en: Immunoglobulin G
abbreviation: IgG
sinonimos:
- Inmunoglobulina G
- IgG
- IgG (Inmunoglobulina G)
- Immunoglobulin G
category: Inmunidad
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-009
combine_with:
- iga
- igm
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

# IgG (Inmunoglobulina G)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-009. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-073. IgG. Categoría: Inmunidad. Tipo: measured_analyte. Tier 3.

## B. Definición

Inmunoglobulina más abundante en sangre, responsable de la memoria inmunológica a largo plazo. Su determinante principal es la exposición inmunológica acumulada (infecciones, vacunas) a lo largo de la vida.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: nefelometría o inmunoturbidimetría.

### Condiciones de toma de muestra

No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión — ABIM Laboratory Reference Ranges)

- **Laboratory reference interval:** **800-1,500 mg/dL** (adultos).
- **URL fuente:** https://www.abim.org/media/e2wdwdqu/laboratory-reference-ranges.pdf — verificado esta sesión (ago-2026).
- **Nota de determinantes poblacionales (Rotterdam Study, 8,768 participantes, verificado esta sesión):** IgG aumenta de forma no lineal con la edad; mujeres tienen IgG más bajo que hombres; tabaquismo (actual, especialmente) se asocia con IgG más bajo; consumo elevado de alcohol se asocia con IgG más bajo; uso de corticoides se asocia con IgG más bajo. Fuente: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8604889/

## E. Interpretación

- **Baja:** inmunodeficiencia (primaria o secundaria — corticoides, enfermedades que causan pérdida de proteínas), puede aumentar riesgo de infecciones recurrentes.
- **Elevada:** infecciones/inflamación crónica, enfermedades autoinmunes, gammapatía monoclonal (requiere electroforesis de proteínas para precisar si es policlonal o monoclonal).

## F. Contexto del paciente y confusores

### Contexto del paciente

Edad, sexo, tabaquismo, consumo de alcohol, uso de corticoides — todos determinantes documentados de los niveles de IgG.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: IgA, IgM, Globulinas/Relación A-G (si se sospecha gammapatía).
- `cannot_conclude`: gammapatía monoclonal sin electroforesis de proteínas.

## H. Tendencias

### Tendencias temporales

Cambia lentamente, influenciada por exposición inmunológica acumulada — no es un marcador de cambio agudo.

## I. Prevención

### Contexto preventivo

No aplica como cribado general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Electroforesis de proteínas si se sospecha gammapatía monoclonal.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar gammapatía sin electroforesis. Escalar ante IgG muy baja con infecciones recurrentes, o muy alta con sospecha de gammapatía monoclonal.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (ABIM) + estudio poblacional de determinantes (Rotterdam Study).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "IgG alterada, considerar edad, tabaquismo, alcohol y corticoides como determinantes antes de sospechar patología".
- **prohibited_inferences:** diagnóstico de gammapatía monoclonal sin electroforesis de proteínas.
- **uncertainty_notes:** múltiples factores de estilo de vida (tabaco, alcohol) alteran IgG independientemente de patología inmunológica real.
- **professional_review:** IgG muy baja con infecciones recurrentes, o muy alta con sospecha de gammapatía.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - immunology
  - tier_3
  - saludly_brain_v1
use_when:
  - "sospecha de inmunodeficiencia o gammapatía monoclonal"
combine_with: [iga, igm]
do_not_use_alone:
  - "diagnóstico de gammapatía sin electroforesis de proteínas"
do_not_conclude:
  - "gammapatía monoclonal confirmada sin electroforesis"
escalate_when:
  - "IgG muy baja con infecciones recurrentes"
  - "IgG muy alta con sospecha de gammapatía"
```
