---
doc_id: SLD-BIO-095
biomarker_id: pth
name_es: PTH (Hormona Paratiroidea)
name_en: Parathyroid Hormone
abbreviation: PTH
sinonimos:
- PTH
- Hormona paratiroidea
- Paratohormona
- PTH intacta
- PTH (Hormona Paratiroidea)
- Parathyroid Hormone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M2-TI-007
- COND-M3-NU-A02
combine_with:
- calcium
- phosphorus
- vitamin_d
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Refleja solo con calcio corregido alto (Consolidado).
---

# PTH (Hormona Paratiroidea)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Refleja solo con calcio corregido alto (Consolidado).
- Reglas que usan esta ficha: COND-M2-TI-007, COND-M3-NU-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-095. PTH. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3 — solo ante alteración de calcio ya documentada, nunca de entrada.

## B. Definición

Hormona producida por las glándulas paratiroides que regula el calcio sérico, aumentando su reabsorción ósea/renal y activando vitamina D. Se interpreta siempre junto a calcio (y frecuentemente fósforo).

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (plasma o suero, según el ensayo) · Método: inmunoensayo de PTH intacta.

### Condiciones de toma de muestra

No requiere ayuno estricto para PTH intacta en la mayoría de protocolos modernos, aunque algunos laboratorios prefieren toma matutina en ayunas por consistencia con calcio.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión, contexto de hipercalcemia)

- **Contexto de hipercalcemia humoral de malignidad (HHM) vs hiperparatiroidismo primario (Mayo Clinic Laboratories, verificado esta sesión):** en HHM, la PTH típicamente es **<30 pg/mL o indetectable** (suprimida, porque la hipercalcemia no es mediada por la glándula paratiroides sino por PTHrP tumoral). En hiperparatiroidismo primario, la PTH está inapropiadamente normal o elevada en presencia de hipercalcemia — un valor de PTH **>30 pg/mL con hipercalcemia y fósforo normal/límite-bajo** sugiere HHM como diagnóstico a considerar, especialmente en adultos mayores con antecedente oncológico.
- **URL fuente:** https://www.mayocliniclabs.com/test-catalog/overview/81774 ; https://endocrinology.testcatalog.org/show/PTHRP — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada con calcio alto:** hiperparatiroidismo primario (adenoma paratiroideo en la mayoría de los casos).
- **Elevada con calcio bajo/normal:** hiperparatiroidismo secundario (compensatorio, típicamente por deficiencia de vitamina D o enfermedad renal crónica).
- **Suprimida (<30 pg/mL) con calcio alto:** sugiere causa de hipercalcemia NO mediada por PTH — considerar PTHrP (hipercalcemia humoral de malignidad), exceso de vitamina D, u otras causas.

## F. Contexto del paciente y confusores

### Contexto del paciente

Calcio y fósforo concurrentes (obligatorio), función renal, niveles de vitamina D, antecedente oncológico (relevante para HHM).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Calcio (obligatorio, siempre), Fósforo, Vitamina D, Creatinina/eGFR (función renal).
- `pattern_examples`: calcio alto + PTH alta = hiperparatiroidismo primario; calcio alto + PTH suprimida (<30 pg/mL) = considerar PTHrP/malignidad, especialmente en adulto mayor con antecedente oncológico; calcio bajo + PTH alta = hiperparatiroidismo secundario (típicamente deficiencia de vitamina D o ERC).
- `cannot_conclude`: causa definitiva sin calcio, fósforo, vitamina D y función renal.

## H. Tendencias

### Tendencias temporales

Relevante en seguimiento de hiperparatiroidismo secundario en enfermedad renal crónica progresiva.

## I. Prevención

### Contexto preventivo

No aplica como cribado — solo ante alteración de calcio ya documentada.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Calcio y fósforo (si no se solicitaron juntos), Vitamina D, función renal; PTHrP si se sospecha hipercalcemia humoral de malignidad.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No solicitar ni interpretar PTH sin calcio ya alterado. Escalar ante hipercalcemia con PTH suprimida (sospecha de malignidad) o hiperparatiroidismo primario confirmado.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "PTH interpretada junto a calcio (y fósforo/vitamina D/función renal), para diferenciar hiperparatiroidismo primario, secundario, o hipercalcemia no mediada por PTH".
- **prohibited_inferences:** diagnóstico definitivo sin calcio concurrente; solicitar PTH sin alteración de calcio previa.
- **uncertainty_notes:** una PTH suprimida con hipercalcemia en adulto mayor con antecedente oncológico es un patrón de alarma para malignidad, no debe pasarse por alto.
- **professional_review:** hipercalcemia con PTH suprimida (sospecha de malignidad), o hiperparatiroidismo primario confirmado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - calcium_metabolism
  - tier_3
  - saludly_brain_v1
use_when:
  - "calcio ya alterado, para determinar causa"
combine_with: [calcium, phosphorus, vitamin_d]
do_not_use_alone:
  - "cualquier interpretación sin calcio concurrente"
do_not_conclude:
  - "causa definitiva sin fósforo, vitamina D y función renal"
escalate_when:
  - "hipercalcemia con PTH suprimida (sospecha de malignidad)"
  - "hiperparatiroidismo primario confirmado"
```
