---
doc_id: SLD-BIO-015
biomarker_id: basophils_pct
name_es: Basófilos %
name_en: Basophils %
abbreviation: Baso%
sinonimos:
- Basófilos %
- BASO%
- Baso%
- Basophils %
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
tier: 4
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Basófilos %

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-012. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-015. Baso%. Categoría: Hematología. Tipo: analito medido. **Tier 4 — bajísimo valor preventivo aislado, casi siempre irrelevante sin sospecha hematológica específica.**

## B. Definición

El menos abundante de los leucocitos. Su elevación en un panel preventivo ambulatorio es infrecuente y, cuando ocurre de forma marcada y persistente, tiene mayor relevancia como posible marcador de proceso mieloproliferativo que como hallazgo reactivo común (a diferencia de neutrófilos, linfocitos o eosinófilos).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo con diferencial · Tubo EDTA. Unidad: %. No requiere ayuno.

## D. Intervalos y umbrales

- **Clinical decision threshold (StatPearls/NCBI, verificado esta sesión):** rango normal **0.5-1% del diferencial, o 0-200 células/µL**. La fuente StatPearls confirma explícitamente el racional de auditoría ya aplicado en esta ficha: *"basofilia aislada es extremadamente infrecuente y amerita estudio para descartar un proceso mieloproliferativo"* — coincide exactamente con la clasificación Tier 4 ya asignada.
- **URL fuente:** https://www.ncbi.nlm.nih.gov/sites/books/NBK604207/ — verificado esta sesión (ago-2026).

## E. Interpretación

- **Elevados:** reacciones alérgicas (leve), hipotiroidismo, en casos infrecuentes procesos mieloproliferativos (leucemia mieloide crónica) cuando la elevación es marcada y persistente — esta última asociación es la razón de su clasificación Tier 4.

## F. Contexto del paciente y confusores

### Contexto del paciente

Función tiroidea, síntomas alérgicos, síntomas sistémicos (fatiga, pérdida de peso, sudoración nocturna) si se sospecha proceso mieloproliferativo.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: WBC total, TSH (si se sospecha causa tiroidea), resto del diferencial.
- `cannot_conclude`: proceso mieloproliferativo sin evaluación hematológica dirigida (frotis, y si corresponde, estudios adicionales).

## H. Tendencias

### Tendencias temporales

Una elevación leve fluctuante no es preocupante; persistencia marcada sí amerita atención.

## I. Prevención

Utilidad preventiva mínima o nula de forma aislada — por eso Tier 4.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Frotis de sangre periférica si hay elevación marcada persistente sin causa evidente (fuera del alcance de Saludly, requiere derivación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado — Tier 4, no se ofrece en panel general.

## L. Evidencia

### Evidencia científica

- **Fuente:** StatPearls (NCBI Bookshelf), "Normal and Abnormal Complete Blood Count With Differential." https://www.ncbi.nlm.nih.gov/sites/books/NBK604207/ — verificado esta sesión (ago-2026). Nivel de evidencia: referencia clínica revisada por pares (NCBI/NIH).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** ninguna interpretación proactiva fuerte — este es un hallazgo de bajo valor preventivo que Saludly Brain debe conocer pero no ofrecer ni destacar en panel general.
- **prohibited_inferences:** cualquier sugerencia de proceso mieloproliferativo sin evaluación hematológica dirigida — riesgo de generar alarma desproporcionada.
- **uncertainty_notes:** el hallazgo relevante (proceso mieloproliferativo) es infrecuente; la mayoría de elevaciones leves son reactivas y benignas.
- **professional_review:** elevación marcada y persistente sin causa evidente (alergia, hipotiroidismo), especialmente con síntomas sistémicos concurrentes.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - tier_4
  - saludly_brain_v1
use_when:
  - "solo si aparece como hallazgo incidental marcado y persistente"
combine_with: [wbc]
do_not_use_alone:
  - "cualquier sugerencia de proceso mieloproliferativo"
do_not_conclude:
  - "leucemia mieloide crónica u otro proceso hematológico sin evaluación dirigida"
escalate_when:
  - "elevación marcada y persistente sin causa evidente, especialmente con síntomas sistémicos"
```
