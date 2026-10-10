---
doc_id: SLD-BIO-026
biomarker_id: sodium
name_es: Sodio
name_en: Sodium
abbreviation: Na+
sinonimos:
- Sodio
- Na
- Sodio sérico
- Na+
- Sodium
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mmol/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-NE-005
combine_with:
- potassium
- chloride
- bicarbonate
- osmolality
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Corrección por glucosa de 200 mg/dL o más y descarte de pseudohiponatremia (COND-M2-NE-005).
---

# Sodio (Na+)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Corrección por glucosa de 200 mg/dL o más y descarte de pseudohiponatremia (COND-M2-NE-005).
- Reglas que usan esta ficha: COND-M2-NE-005. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-026. Na+. Categoría: Metabolismo y Electrolitos. Tipo: analito medido. Tier 1.

## B. Definición

Principal catión extracelular; determina en gran medida la osmolalidad plasmática y el estado de hidratación. Su alteración refleja predominantemente trastornos del balance de agua (no solo de sodio en sí).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma). Método: electrodo ion-selectivo (estándar en analizadores automatizados). Unidad: mEq/L (=mmol/L). No requiere ayuno. Variable preanalítica relevante: hemólisis no suele afectarlo significativamente (a diferencia de potasio), pero muestras mal conservadas pueden alterar el resultado.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método — rango fisiológico típico ampliamente reproducido en fisiología clínica estándar (aprox. 135-145 mEq/L), pero **Saludly debe validar el rango exacto con el laboratorio aliado** antes de fijarlo como umbral de producto.
- **Clinical decision threshold:** hiponatremia/hipernatremia significativas son alteraciones agudas que se manejan clínicamente, no por seguimiento preventivo ambulatorio.
- **Estado de verificación:** ⚠️ No ejecuté una búsqueda dedicada a una guía de sociedad específica sobre umbrales de sodio en esta sesión — el rango fisiológico general es conocimiento médico estándar ampliamente reproducido en fisiología clínica, pero el umbral exacto de decisión debe verificarse con fuente primaria (ej. guías de hiponatremia de sociedades de endocrinología/nefrología) antes de publicarse en producción.

## E. Interpretación

**Elevado (hipernatremia):** generalmente refleja déficit relativo de agua libre — deshidratación, diabetes insípida, ingesta insuficiente de agua, diarrea/vómito con reposición inadecuada.

**Disminuido (hiponatremia):** múltiples causas — exceso de agua relativo (SIADH, insuficiencia cardíaca, insuficiencia hepática, insuficiencia renal), pérdida de sodio (diuréticos, insuficiencia suprarrenal), o hiponatremia dilucional.

**Dentro del intervalo:** no descarta trastornos leves de la regulación de agua que no alcanzan a alterar el sodio sérico de forma medible en una sola toma.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: hidratación reciente, medicamentos (diuréticos, IECA, ISRS asociados a SIADH), síntomas neurológicos (confusión, cefalea — pueden indicar alteración aguda), vómito/diarrea reciente.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Potasio, Cloro, Bicarbonato (panel electrolítico completo), Osmolalidad si está disponible.
- `pattern_examples`: hiponatremia + potasio elevado puede sugerir insuficiencia suprarrenal.
- `cannot_conclude`: causa específica del trastorno sin evaluación clínica y, frecuentemente, sin osmolalidad urinaria/sérica que Saludly no ofrece en v1.

## H. Tendencias

### Tendencias temporales

Los trastornos de sodio son predominantemente agudos y se manejan en tiempo real, no por tendencia longitudinal lenta como otros biomarcadores preventivos. Un cambio brusco entre controles es más relevante clínicamente que una tendencia gradual.

## I. Prevención

Acciones razonables: hidratación adecuada, revisión de medicamentos con potencial efecto sobre sodio (diuréticos, ISRS) junto a un profesional.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Panel electrolítico completo si no se solicitó junto; osmolalidad si hay alteración significativa (fuera del alcance actual de Saludly v1).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

El sodio es parte de un panel metabólico básico de rutina, no una prueba diagnóstica por sí sola de ninguna condición específica.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento fisiológico estándar (`expert_consensus` / `educational_reference`), ampliamente reproducido en fisiología clínica.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026). Nivel de evidencia: referencia académica estándar (NBME es la entidad que produce los exámenes de licencia médica en EE.UU.; sus tablas de valores reflejan consenso educativo ampliamente aceptado).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "alteración del sodio compatible con posible trastorno del balance de agua, requiere contexto de hidratación y medicamentos".
- **prohibited_inferences:** diagnóstico de causa específica (SIADH, insuficiencia suprarrenal, diabetes insípida) sin evaluación clínica dirigida.
- **uncertainty_notes:** los trastornos de sodio son frecuentemente agudos; un valor alterado en un panel preventivo de rutina puede requerir manejo más urgente que otros biomarcadores de este catálogo.
- **professional_review:** cualquier valor marcadamente fuera de rango, especialmente con síntomas neurológicos concurrentes (confusión, cefalea, convulsiones).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - electrolytes
  - metabolism
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando panel electrolítico"
  - "evaluando estado de hidratación"

combine_with: [potassium, chloride, bicarbonate, osmolality]

do_not_use_alone:
  - "diagnóstico de causa de hipo/hipernatremia"

do_not_conclude:
  - "SIADH, insuficiencia suprarrenal, o diabetes insípida confirmados"

escalate_when:
  - "valor marcadamente fuera de rango"
  - "síntomas neurológicos concurrentes (confusión, cefalea, convulsiones)"
```
