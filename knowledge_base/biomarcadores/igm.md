---
doc_id: SLD-BIO-074
biomarker_id: igm
name_es: Inmunoglobulina M
name_en: Immunoglobulin M
abbreviation: IgM
sinonimos:
- Inmunoglobulina M
- IgM
- IgM (Inmunoglobulina M)
- Immunoglobulin M
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
- COND-M6-MI-002
combine_with:
- iga
- igg
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

# IgM (Inmunoglobulina M)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-009. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-074. IgM. Categoría: Inmunidad. Tipo: measured_analyte. Tier 3.

## B. Definición

Primera inmunoglobulina producida en una respuesta inmune (antes que IgG) — su elevación en el contexto de una infección específica sugiere exposición reciente/aguda, a diferencia de IgG que indica exposición pasada o inmunidad establecida.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: nefelometría o inmunoturbidimetría.

### Condiciones de toma de muestra

No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión — ABIM Laboratory Reference Ranges)

- **Laboratory reference interval:** **45-150 mg/dL** (adultos).
- **URL fuente:** https://www.abim.org/media/e2wdwdqu/laboratory-reference-ranges.pdf — verificado esta sesión (ago-2026).
- **Nota de determinantes poblacionales (Rotterdam Study, verificado esta sesión):** a diferencia de IgA e IgG, **las mujeres tienen IgM más alto que los hombres** (patrón inverso al de IgA/IgG).

## E. Interpretación

- **Elevada:** infección aguda reciente (en el contexto de una prueba serológica específica), macroglobulinemia de Waldenström (gammapatía monoclonal IgM, poco frecuente).
- **Baja:** inmunodeficiencia.

## F. Contexto del paciente y confusores

### Contexto del paciente

Sexo (determinante conocido, patrón inverso a IgA/IgG), síntomas de infección aguda reciente si se solicita en ese contexto.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: IgA, IgG (el patrón IgM alto + IgG bajo/normal sugiere infección reciente; IgG alto + IgM normal sugiere inmunidad establecida/pasada).
- `cannot_conclude`: gammapatía monoclonal IgM sin electroforesis de proteínas.

## H. Tendencias

### Tendencias temporales

Se eleva rápidamente en respuesta a una infección aguda y desciende en semanas conforme la respuesta madura hacia IgG.

## I. Prevención

### Contexto preventivo

No aplica como cribado general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Electroforesis de proteínas si se sospecha macroglobulinemia de Waldenström.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar macroglobulinemia sin electroforesis. Escalar ante IgM muy elevada sin contexto infeccioso claro.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (ABIM) + estudio poblacional de determinantes.
- Fuentes verificadas esta sesión: ver URL en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "IgM elevada compatible con infección aguda reciente si hay contexto clínico; considerar sexo como determinante".
- **prohibited_inferences:** diagnóstico de macroglobulinemia sin electroforesis de proteínas.
- **uncertainty_notes:** patrón por sexo inverso al de IgA/IgG.
- **professional_review:** IgM muy elevada sin contexto infeccioso claro.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - immunology
  - acute_infection
  - tier_3
  - saludly_brain_v1
use_when:
  - "sospecha de infección aguda reciente, junto a IgG"
combine_with: [iga, igg]
do_not_use_alone:
  - "diagnóstico de macroglobulinemia sin electroforesis"
do_not_conclude:
  - "gammapatía IgM confirmada sin electroforesis"
escalate_when:
  - "IgM muy elevada sin contexto infeccioso claro"
```
