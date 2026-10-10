---
doc_id: SLD-BIO-099
biomarker_id: c_peptide
name_es: Péptido C
name_en: C-Peptide
abbreviation: CP
sinonimos:
- Péptido C
- CP
- C-Peptide
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-010
combine_with:
- glucose
- insulin
- hba1c
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Péptido C

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-010. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-099. CP. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3 — solo para diferenciación diagnóstica de diabetes o estudio de hipoglucemia, no cribado general.

## B. Definición

Fragmento de 31 aminoácidos liberado en cantidad equimolar a la insulina durante el clivaje de la proinsulina en las células beta pancreáticas. A diferencia de la insulina exógena (inyectada), que no contiene péptido C, esta molécula permite medir la producción **endógena** real de insulina incluso en personas que reciben insulina inyectada — su vida media es 3-4 veces más larga que la de la insulina, lo que la hace más estable para medición.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (ej. Roche/Cobas). Ayuno de 8 horas recomendado para la medición basal estándar.

### Condiciones de toma de muestra

Ayuno de 8 horas para la medición basal. Se elimina principalmente por vía renal — la función renal reducida puede elevar falsamente los niveles.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con aplicación diagnóstica específica (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Laboratory reference interval (ayuno):** rango consolidado de fuentes concordantes **0.8-4 ng/mL** (algunas fuentes reportan 0.8-3 ng/mL, o 1.1-4.4 ng/mL) — depende del ensayo específico del laboratorio.
- **Umbrales de diferenciación diagnóstica (estudio de validación, verificado esta sesión):** péptido C promedio por tipo de diabetes: **Diabetes tipo 1: 0.2 ng/mL** (muy bajo — refleja destrucción autoinmune de células beta) · **Diabetes tipo 2: 2.4 ng/mL** · **MODY: 1.14 ng/mL** · **LADA: 1.87 ng/mL**. Puntos de corte discriminativos: **0.95 ng/mL diferencia tipo 1 de tipo 2** (sensibilidad 82%, especificidad 77%); **0.82 ng/mL diferencia tipo 1 de LADA** (sensibilidad 82%, especificidad 77%); **1.65 ng/mL diferencia tipo 2 de MODY** (sensibilidad 72%, especificidad 72%).
- **Regla práctica simplificada (patente farmacéutica, calidad de evidencia menor, usar con cautela):** <0.5 ng/mL sugiere producción insuficiente de insulina; 0.5-2.0 ng/mL considerado normal/no diabético; >2.0 ng/mL sugiere niveles altos de insulina (resistencia).
- **URLs fuente:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11122504/ (estudio de diferenciación diagnóstica) ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9506304/ (caso clínico ilustrativo) — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Muy bajo (<0.95 ng/mL aprox.):** sugiere diabetes tipo 1 o LADA — producción insulínica endógena muy reducida por destrucción autoinmune de células beta.
- **Normal-alto en diabetes ya diagnosticada:** sugiere diabetes tipo 2 (resistencia a la insulina con producción endógena preservada o incluso elevada compensatoriamente).
- **Hallazgo inusual (caso clínico documentado):** un paciente con diabetes tipo 1 autoanticuerpo-negativa mostró **aumento** de péptido C casi una década después del diagnóstico inicial, sugiriendo posible regeneración/recuperación de función de células beta — un hallazgo atípico que ilustra que la producción endógena puede cambiar con el tiempo, no es estática.

## F. Contexto del paciente y confusores

### Contexto del paciente

Tipo de diabetes ya diagnosticada o en estudio, uso de insulina exógena (el péptido C sigue siendo útil en este contexto, a diferencia de medir insulina directamente), función renal, contexto de hipoglucemia si se solicita para ese estudio.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Glucosa (debe medirse simultáneamente para interpretación adecuada), Insulina, HbA1c, anticuerpos anti-GAD65/IA2/ZnT8 (no incluidos en el catálogo actual, relevantes para confirmar autoinmunidad).
- `pattern_examples`: péptido C muy bajo + anticuerpos anti-GAD65 positivos = diabetes tipo 1/LADA confirmada; péptido C normal-alto en persona con diabetes = más compatible con tipo 2.
- `cannot_conclude`: tipo específico de diabetes con alta certeza usando solo péptido C — los puntos de corte tienen sensibilidad/especificidad moderadas (70-82%), no son perfectos; anticuerpos son complementarios importantes.

## H. Tendencias

### Tendencias temporales

Puede cambiar con el tiempo incluso en diabetes ya diagnosticada (ver caso clínico de regeneración de función beta) — no asumir que el tipo de diabetes está fijo para siempre basado en una sola medición histórica.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — uso diagnóstico dirigido específico.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Glucosa simultánea (obligatorio), anticuerpos anti-GAD65/IA2/ZnT8 si se busca confirmar autoinmunidad.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No clasificar el tipo de diabetes con alta certeza usando solo péptido C sin anticuerpos y contexto clínico. Escalar ante hipoglucemia con péptido C elevado (sospecha de insulinoma o hipoglucemia facticia por sulfonilureas) — requiere evaluación urgente.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte para los puntos de corte de diferenciación diagnóstica (estudio de validación con población mexicana, 2024) + caso clínico ilustrativo de regeneración de células beta.
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "péptido C bajo/alto, considerar junto a glucosa y contexto clínico para orientar tipo de diabetes; los puntos de corte tienen sensibilidad/especificidad moderadas, no son definitivos".
- **prohibited_inferences:** clasificación definitiva del tipo de diabetes solo con péptido C sin anticuerpos y contexto clínico completo.
- **uncertainty_notes:** la producción endógena de insulina puede cambiar con el tiempo — no asumir estabilidad permanente del resultado.
- **professional_review:** hipoglucemia con péptido C elevado (sospecha de insulinoma o hipoglucemia facticia), o discordancia relevante entre péptido C y el tipo de diabetes previamente asumido.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - diabetes_classification
  - tier_3
  - saludly_brain_v1
use_when:
  - "diferenciación de tipo de diabetes (tipo 1 vs tipo 2 vs MODY vs LADA)"
  - "estudio de hipoglucemia"
combine_with: [glucose, insulin, hba1c]
do_not_use_alone:
  - "clasificación definitiva del tipo de diabetes sin anticuerpos y contexto clínico"
do_not_conclude:
  - "tipo de diabetes con alta certeza usando solo péptido C"
escalate_when:
  - "hipoglucemia con péptido C elevado (sospecha de insulinoma o hipoglucemia facticia)"
```
