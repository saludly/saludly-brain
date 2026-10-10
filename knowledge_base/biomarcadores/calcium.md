---
doc_id: SLD-BIO-029
biomarker_id: calcium
name_es: Calcio Sérico
name_en: Serum Calcium
abbreviation: Ca
sinonimos:
- Calcio
- Calcio total
- Ca
- Calcio Sérico
- Serum Calcium
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-TI-007
- COND-M3-NU-A02
combine_with:
- albumin
- phosphorus
- pth
- alp
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Se usa el calcio corregido por albúmina; la PTH es refleja solo con calcio corregido alto (COND-M2-TI-007).
---

# Calcio Sérico

## Notas de decisión de Saludly (6 de octubre de 2026)

- Se usa el calcio corregido por albúmina; la PTH es refleja solo con calcio corregido alto (COND-M2-TI-007).
- Reglas que usan esta ficha: COND-M2-TI-007, COND-M3-NU-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-029. Ca. Categoría: Metabolismo. Tipo: analito medido. Tier 2.

## B. Definición

El calcio sérico total mide tanto la fracción unida a proteínas (principalmente albúmina, ~40%) como la fracción libre/ionizada biológicamente activa. Su regulación depende de PTH, vitamina D y, en menor medida, calcitonina.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico estandarizado. Unidad: mg/dL. No requiere ayuno. **Factor de confusión crítico:** el calcio total depende directamente del nivel de albúmina — una albúmina baja puede hacer parecer bajo un calcio total que en realidad es normal en su fracción libre ("calcio corregido"). Saludly debe calcular o al menos señalar la necesidad de corregir por albúmina antes de interpretar un calcio bajo.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal de calcio total **8.2-10.5 mg/dL** (varía ligeramente entre fuentes: 8.2-10.2 vs 8.4-10.2 vs 8.5-10.5 mg/dL — Saludly debe usar el rango específico del laboratorio aliado). Calcio iónico (fracción libre, no unida a proteínas): 4.5-5.6 mg/dL (1.05-1.3 mmol/L) cuando está disponible — más preciso que el total porque no requiere corrección por albúmina.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevado (hipercalcemia):** hiperparatiroidismo primario (causa más frecuente en ambulatorios asintomáticos), malignidad (causa más frecuente en hospitalizados), exceso de vitamina D, inmovilización prolongada.
- **Disminuido (hipocalcemia):** hipoparatiroidismo, deficiencia de vitamina D, insuficiencia renal, hipoalbuminemia (falsa hipocalcemia si no se corrige).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: albúmina concurrente (crítico para corrección), función renal, síntomas (calambres, parestesias si bajo; estreñimiento, poliuria, confusión si alto), medicamentos (diuréticos tiazídicos elevan calcio; algunos anticonvulsivantes lo bajan).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Albúmina (obligatorio, para corrección), Fósforo, PTH, ALP (si se sospecha origen óseo).
- `pattern_examples`: calcio alto + fósforo bajo + PTH alta = compatible con hiperparatiroidismo primario; calcio alto + fósforo alto + PTH baja = más compatible con malignidad o exceso de vitamina D.
- `cannot_conclude`: causa específica sin PTH y contexto clínico.

## H. Tendencias

### Tendencias temporales

Generalmente estable — un cambio significativo sostenido amerita evaluación de la causa, no solo repetición.

## I. Prevención

Utilidad como parte del panel metabólico ampliado, especialmente relevante para salud ósea a largo plazo.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Albúmina (si no se solicitó junta), PTH, Fósforo, Vitamina D si hay alteración significativa.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstico aislado — requiere corrección por albúmina y, ante alteración confirmada, PTH para orientar causa.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento endocrinológico/metabólico óseo estándar.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "calcio alterado, requiere corrección por albúmina antes de interpretar; si se confirma alteración real, considerar PTH para orientar causa".
- **prohibited_inferences:** interpretar un calcio bajo sin corregir por albúmina; diagnóstico de hiperparatiroidismo o malignidad sin PTH y contexto clínico.
- **uncertainty_notes:** la dependencia del calcio total de la albúmina es la fuente de error de interpretación más frecuente para este biomarcador — el sistema debe verificar siempre que la corrección se haya considerado.
- **professional_review:** alteración marcada y confirmada tras corrección por albúmina, especialmente con síntomas concurrentes.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - bone_health
  - electrolytes
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando panel metabólico ampliado o salud ósea"
  - "síntomas de hiper/hipocalcemia"

combine_with: [albumin, phosphorus, pth, alp]

do_not_use_alone:
  - "interpretación sin corrección por albúmina"

do_not_conclude:
  - "hiperparatiroidismo o malignidad sin PTH y contexto clínico"

escalate_when:
  - "alteración marcada confirmada tras corrección por albúmina, con o sin síntomas"
```
