---
doc_id: SLD-BIO-066
biomarker_id: esr
name_es: VSG
name_en: Erythrocyte Sedimentation Rate (ESR)
abbreviation: VSG / ESR
sinonimos:
- VSG
- Velocidad de sedimentación globular
- Eritrosedimentación
- VSG (Velocidad de Sedimentación Globular)
- VSG / ESR
- Erythrocyte Sedimentation Rate (ESR)
category: Inflamación
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mm/h
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M6-RE-A02
combine_with:
- hs_crp
- fibrinogen
- ferritin
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

# VSG (Velocidad de Sedimentación Globular)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M6-RE-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-066. VSG/ESR. Categoría: Inflamación. Tipo: measured_analyte. Tier 3 — muy inespecífica y lenta de interpretar frente a hs-CRP, solo complementaria dirigida.

## B. Definición

Mide indirectamente la inflamación a través de la velocidad a la que los eritrocitos sedimentan en una columna de sangre no coagulada — depende principalmente de la concentración de fibrinógeno y otras proteínas de fase aguda que reducen la repulsión entre eritrocitos.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (tubo con citrato o EDTA según método) · Método: Westergren (estándar de referencia) o analizadores automatizados (VES-MATIC, CUBE) — **existen diferencias significativas entre métodos**, Saludly debe registrar cuál usa el laboratorio aliado.

### Condiciones de toma de muestra

No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con fuerte dependencia de edad/sexo (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Rango clásico simple (eMedicine/Medscape):** hombres <15 mm/h; mujeres ≤20 mm/h.
- **Rangos por edad/sexo más recientes (estudio italiano, 989 participantes, método Westergren, verificado esta sesión):** mujeres ≥18 años: **1-22 mm/h** (rango único, sin diferencia relevante por edad); hombres 18-69 años: **1-14 mm/h**; hombres ≥70 años: **1-22 mm/h** (aumenta con la edad, a diferencia de las mujeres).
- **URLs fuente:** https://emedicine.medscape.com/article/2172316-overview ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12071782/ — verificadas esta sesión (ago-2026).
- **Determinantes de estilo de vida (estudio español, 1,472 personas, verificado esta sesión):** VSG más alta en mujeres, aumenta con la edad; IMC elevado, síndrome metabólico y tabaquismo se asocian independientemente con VSG más alta; consumo ligero de alcohol y actividad física regular se asocian con VSG más baja.

## E. Interpretación

- **Elevada:** inflamación/infección (inespecífico), enfermedad reumatológica (especialmente arteritis de células gigantes/polimialgia reumática, donde VSG muy elevada — a menudo >50-100 mm/h — es característica), anemia (afecta la sedimentación independiente de inflamación), embarazo, edad avanzada.
- **VSG extremadamente elevada (≥100 mm/h, verificado esta sesión en estudio de reumatología):** causas más frecuentes son enfermedad reumática, malignidad e infección — albúmina baja, plaquetas y ferritina son otros datos de apoyo relevantes en ese contexto.

## F. Contexto del paciente y confusores

### Contexto del paciente

Edad, sexo, IMC, tabaquismo, actividad física, síndrome metabólico, anemia concurrente (afecta la VSG independientemente de inflamación), embarazo.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: hs-CRP (más específica y de respuesta más rápida — VSG cambia más lentamente), Fibrinógeno, Ferritina, Hemoglobina (la anemia altera la VSG).
- `pattern_examples`: VSG muy elevada (>100 mm/h) + síntomas reumatológicos = considerar arteritis de células gigantes/polimialgia reumática, especialmente en adultos mayores.
- `cannot_conclude`: causa específica de la elevación sin contexto clínico — es de las pruebas menos específicas del catálogo.

## H. Tendencias

### Tendencias temporales

Cambia más lentamente que hs-CRP ante un proceso agudo (sube y baja con más retraso) — útil para inflamación crónica/seguimiento, menos útil para cambios agudos rápidos.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — uso dirigido por sospecha reumatológica o seguimiento de enfermedad inflamatoria ya conocida.

## J. Pruebas complementarias

### Pruebas complementarias posibles

hs-CRP (más específica y rápida), Fibrinógeno, evaluación reumatológica si VSG muy elevada con síntomas sugestivos.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No usar como cribado poblacional general. Escalar ante VSG muy elevada (≥100 mm/h) o síntomas sugestivos de arteritis de células gigantes (cefalea, alteraciones visuales, claudicación mandibular) en adulto mayor — esto último es una urgencia relativa por riesgo de ceguera.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte, múltiples fuentes concordantes (Medscape, estudios de validación de métodos automatizados, estudio poblacional de determinantes).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "VSG elevada, marcador inespecífico de inflamación, considerar junto a hs-CRP y contexto clínico; VSG muy elevada en adulto mayor con síntomas cefálicos/visuales sugiere evaluación urgente por arteritis de células gigantes".
- **prohibited_inferences:** diagnóstico específico de ninguna condición a partir de VSG aislada.
- **uncertainty_notes:** fuertemente influenciada por edad, sexo, anemia e IMC — interpretar con ese contexto siempre.
- **professional_review:** VSG ≥100 mm/h, o síntomas sugestivos de arteritis de células gigantes en adulto mayor (evaluación urgente por riesgo de pérdida visual).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - inflammation
  - rheumatology
  - tier_3
  - saludly_brain_v1
use_when:
  - "sospecha de enfermedad reumatológica o seguimiento de inflamación crónica"
combine_with: [hs_crp, fibrinogen, ferritin]
do_not_use_alone:
  - "diagnóstico de cualquier condición específica"
do_not_conclude:
  - "causa específica sin contexto clínico"
escalate_when:
  - "VSG ≥100 mm/h"
  - "síntomas sugestivos de arteritis de células gigantes en adulto mayor (urgencia relativa)"
```
