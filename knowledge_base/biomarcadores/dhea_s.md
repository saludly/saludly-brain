---
doc_id: SLD-BIO-091
biomarker_id: dhea_s
name_es: DHEA-S
name_en: Dehydroepiandrosterone Sulfate
abbreviation: DHEA-S
sinonimos:
- DHEA-S
- Sulfato de dehidroepiandrosterona
- DHEAS
- DHEA-S (Sulfato de Dehidroepiandrosterona)
- Dehydroepiandrosterone Sulfate
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-011
combine_with:
- cortisol
- acth
- testosterone_total
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

# DHEA-S (Sulfato de Dehidroepiandrosterona)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-011. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-091. DHEA-S. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3.

## B. Definición

Andrógeno producido casi exclusivamente por la glándula suprarrenal (a diferencia de la testosterona, de origen mixto gonadal/suprarrenal). Su vida media larga y estabilidad en sangre (a diferencia de cortisol/ACTH) lo hace menos dependiente del horario exacto de la toma — una ventaja práctica relevante para un modelo de toma a domicilio.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia).

### Condiciones de toma de muestra

No requiere horario específico crítico (a diferencia de cortisol/ACTH) por su vida media larga y estabilidad relativamente constante a lo largo del día. No requiere ayuno.

## D. Intervalos y umbrales

### Interpretación y umbrales (evidencia verificada esta sesión)

- **Contexto de incidentaloma suprarrenal (estudio retrospectivo de 468 pacientes, verificado esta sesión):** DHEA-S <40 mcg/dL diagnosticó secreción autónoma de cortisol (ACS) con 84% especificidad y 81% VPP; combinado con ACTH <10 pg/mL, la precisión diagnóstica combinada alcanzó 92% especificidad y 87% VPP.
- **Elevado:** hiperplasia suprarrenal congénita de inicio tardío, tumor suprarrenal productor de andrógenos (especialmente si la elevación es marcada y de inicio rápido — señal de alarma para malignidad), síndrome de ovario poliquístico (elevación leve-moderada, componente suprarrenal).
- **Disminuido:** insuficiencia suprarrenal, envejecimiento (DHEA-S declina naturalmente con la edad desde la adultez temprana), secreción autónoma de cortisol (ver hallazgo de incidentaloma arriba — la producción de DHEA-S se suprime cuando hay exceso autónomo de cortisol).

## F. Contexto del paciente y confusores

### Contexto del paciente

Edad (declive fisiológico natural), síntomas de hiperandrogenismo (hirsutismo, acné, virilización — y su velocidad de instauración, crítica para diferenciar SOP de tumor), hallazgo incidental de masa suprarrenal en imagen.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ACTH y Cortisol (contexto de incidentaloma suprarrenal), Testosterona total (contexto de hiperandrogenismo).
- `pattern_examples`: DHEA-S muy elevado + hirsutismo de inicio rápido (<1 año) = señal de alarma para tumor suprarrenal productor de andrógenos, requiere evaluación urgente; DHEA-S levemente elevado + hirsutismo de larga evolución = más compatible con SOP.
- `cannot_conclude`: diagnóstico de tumor suprarrenal sin imagen; diagnóstico de SOP sin criterios clínicos completos.

## H. Tendencias

### Tendencias temporales

Declina gradualmente con la edad desde los 20-30 años — un descenso dentro de ese patrón esperado no es preocupante. Una elevación de inicio rápido en cualquier edad sí lo es.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — uso dirigido por síntomas o hallazgo incidental.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Testosterona total (si hiperandrogenismo), ACTH y cortisol (si incidentaloma suprarrenal), imagen suprarrenal si hay sospecha de tumor.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar SOP o tumor suprarrenal sin el contexto clínico completo. Escalar ante elevación marcada de inicio rápido (sospecha de tumor) o hirsutismo/virilización de progresión rápida.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte — estudio retrospectivo de cohorte de 468 pacientes con adenoma suprarrenal (2000-2020).
- **Fuente verificada esta sesión:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8301396/

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "DHEA-S alterado, considerar junto a cortisol/ACTH (incidentaloma) o testosterona (hiperandrogenismo), y la velocidad de instauración de síntomas".
- **prohibited_inferences:** diagnóstico de tumor suprarrenal o SOP sin evaluación clínica completa e imagen cuando corresponda.
- **uncertainty_notes:** la velocidad de instauración de síntomas (rápida vs gradual) es tan importante como el valor numérico para diferenciar causas benignas de malignas.
- **professional_review:** elevación marcada de inicio rápido, hirsutismo/virilización de progresión rápida, o hallazgo de incidentaloma suprarrenal.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - adrenal
  - hyperandrogenism
  - tier_3
  - saludly_brain_v1
use_when:
  - "hiperandrogenismo de inicio rápido en mujeres"
  - "incidentaloma suprarrenal, junto a ACTH"
combine_with: [cortisol, acth, testosterone_total]
do_not_use_alone:
  - "diagnóstico de tumor suprarrenal o SOP"
do_not_conclude:
  - "malignidad o SOP sin evaluación clínica completa"
escalate_when:
  - "elevación marcada de inicio rápido"
  - "hirsutismo/virilización de progresión rápida"
```
