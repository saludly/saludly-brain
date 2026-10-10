---
doc_id: SLD-BIO-018
biomarker_id: reticulocytes_pct
name_es: Reticulocitos %
name_en: Reticulocyte Percentage
abbreviation: Retic%
sinonimos:
- Reticulocitos %
- Retic%
- Reticulocyte Percentage
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M3-HE-001
- COND-M4-GA-A01
combine_with:
- reticulocytes_abs
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

# Reticulocitos %

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-001, COND-M4-GA-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-018. Retic%. Categoría: Hematología. Tipo: analito medido. Tier 3 — solo tiene valor diagnóstico con anemia ya documentada, excluido del panel preventivo básico.

## B. Definición

Porcentaje de eritrocitos jóvenes (reticulocitos) recién liberados de la médula ósea. Es el marcador directo de qué tan activamente está respondiendo la médula ósea a una anemia — distingue anemias por producción reducida (médula no responde, reticulocitos bajos/normales) de anemias por pérdida o destrucción (médula responde, reticulocitos altos).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Tubo EDTA · Método: citometría de flujo con tinción supravital. Unidad: %. No requiere ayuno.

## D. Intervalos y umbrales

- **Clinical decision threshold (verificado esta sesión):** rango normal en adultos **0.5-2.6%** (fuentes varían: 0.5-1.5% NCCPA vs 0.5-2.6% registro de estudio clínico) — reflejando la variabilidad metodológica reconocida entre analizadores. Saludly debe validar con el laboratorio aliado y, cuando sea posible, usar el índice de producción reticulocitaria corregido en vez del porcentaje crudo.
- **URL fuente:** https://www.nccpa.net/wp-content/uploads/NCCPA-Adult-Laboratory-Values.pdf ; https://clinicaltrials.gov/study/NCT00853632
- **Nota metodológica importante:** el porcentaje de reticulocitos debe corregirse por el grado de anemia (reticulocitos corregidos o índice de producción reticulocitaria) para ser clínicamente interpretable — un porcentaje "normal" en presencia de anemia severa puede en realidad representar una respuesta medular inadecuada.

## E. Interpretación

- **Elevado (con anemia):** respuesta medular activa — sangrado agudo, hemólisis, respuesta a tratamiento de deficiencia (hierro/B12 recién iniciado).
- **Bajo/normal (con anemia):** respuesta medular inadecuada — anemia de enfermedad crónica, deficiencia nutricional no tratada, falla medular, infiltración medular.

## F. Contexto del paciente y confusores

### Contexto del paciente

Tratamiento reciente de una deficiencia (hierro/B12 — los reticulocitos suben antes que la hemoglobina, es el primer signo de respuesta al tratamiento), sangrado reciente, síntomas de hemólisis.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Hemoglobina (obligatorio — sin anemia documentada, no tiene indicación), Reticulocitos absolutos, VCM.
- `cannot_conclude`: causa específica de la anemia sin el contexto completo (ferritina, B12/folato, evidencia de hemólisis o sangrado).

## H. Tendencias

### Tendencias temporales

Es el marcador más temprano de respuesta a tratamiento de una deficiencia — sube en días, antes que la hemoglobina, que tarda semanas en normalizarse.

## I. Prevención

No aplica como marcador preventivo — es una herramienta de seguimiento de anemia ya diagnosticada.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Reticulocitos absolutos (siempre en conjunto), Ferritina/B12/Folato según el patrón de VCM.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado — Tier 3, solo con anemia ya documentada.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar sobre respuesta medular.
- **Fuente:** NCCPA Laboratory Values y registro de estudio clínico (ClinicalTrials.gov) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "reticulocitos interpretados junto a hemoglobina para evaluar si la médula ósea está respondiendo activamente a la anemia".
- **prohibited_inferences:** solicitar o interpretar reticulocitos sin anemia documentada; diagnóstico de causa específica sin el resto del panel.
- **uncertainty_notes:** el porcentaje sin corregir por el grado de anemia puede ser engañoso — usar junto al valor absoluto.
- **professional_review:** anemia con respuesta medular inadecuada (reticulocitos bajos pese a anemia significativa), o anemia con reticulocitos muy elevados sugestivos de hemólisis activa.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - anemia_workup
  - tier_3
  - saludly_brain_v1
use_when:
  - "anemia ya documentada, para evaluar respuesta medular"
combine_with: [reticulocytes_abs, hemoglobin, mcv]
do_not_use_alone:
  - "cualquier interpretación sin anemia documentada por hemoglobina"
do_not_conclude:
  - "causa específica sin ferritina/B12/folato/evidencia de hemólisis"
escalate_when:
  - "respuesta medular inadecuada ante anemia significativa"
  - "reticulocitos muy elevados sugestivos de hemólisis activa"
```
