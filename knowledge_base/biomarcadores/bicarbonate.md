---
doc_id: SLD-BIO-033
biomarker_id: bicarbonate
name_es: Bicarbonato / CO2
name_en: Bicarbonate / CO2
abbreviation: HCO3- / CO2
sinonimos:
- Bicarbonato
- CO2 total
- HCO3
- Bicarbonato / CO2
- HCO3- / CO2
- Bicarbonate / CO2
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mmol/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-NE-A03
combine_with:
- sodium
- potassium
- chloride
- creatinine
- egfr
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Bicarbonato / CO2 (HCO3-)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M2-NE-A03. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-033. HCO3-/CO2. Categoría: Metabolismo. Tipo: analito medido (reportado en el panel electrolítico venoso como "CO2 total", que aproxima el bicarbonato). Tier 2.

## B. Definición

Principal sistema amortiguador (buffer) del equilibrio ácido-base sanguíneo, regulado por los riñones (reabsorción/excreción) y, en conjunto con el CO2 respiratorio, por los pulmones. Su alteración señala trastornos ácido-base metabólicos (cuando cambia de forma primaria) o respiratorios compensatorios.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) — el "CO2 total" venoso es una aproximación razonable del bicarbonato para fines de panel metabólico ambulatorio (a diferencia de una gasometría arterial, que mide bicarbonato con mayor precisión junto al pH). Método: enzimático o electrodo específico. Unidad: mEq/L. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal (CO2 venoso total) **22-28 mEq/L**, consistente entre todas las fuentes consultadas.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Disminuido (acidosis metabólica):** insuficiencia renal (acumulación de ácidos), diarrea (pérdida de bicarbonato), cetoacidosis diabética, acidosis láctica.
- **Elevado (alcalosis metabólica o compensación respiratoria):** vómito prolongado, uso de diuréticos, compensación de acidosis respiratoria crónica (ej. EPOC).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: función renal (eGFR/creatinina), vómito/diarrea reciente, antecedente de diabetes (riesgo de cetoacidosis), enfermedad pulmonar crónica conocida.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Sodio, Potasio, Cloro (panel electrolítico completo), Creatinina/eGFR (la insuficiencia renal es causa frecuente de acidosis metabólica crónica).
- `pattern_examples`: bicarbonato bajo + eGFR bajo = acidosis metabólica de causa renal; bicarbonato bajo + potasio alto = patrón compatible con acidosis metabólica con componente de hiperpotasemia (frecuente en insuficiencia renal avanzada).
- `cannot_conclude`: tipo específico de trastorno ácido-base sin gasometría (pH, pCO2) — Saludly no ofrece gasometría, por lo que su interpretación con el panel venoso solo es aproximada.

## H. Tendencias

### Tendencias temporales

En insuficiencia renal crónica, un descenso progresivo del bicarbonato es un marcador de progresión de la enfermedad renal relevante para seguimiento longitudinal.

## I. Prevención

Utilidad principalmente en el contexto de seguimiento de función renal ya alterada, más que como marcador de cribado independiente en población sana.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Panel electrolítico completo, función renal si no está disponible; gasometría si hay alteración marcada con síntomas (fuera del alcance ambulatorio de Saludly, requiere derivación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del panel metabólico ampliado — su interpretación diagnóstica precisa de un trastorno ácido-base requiere gasometría, que Saludly no ofrece.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento de fisiología ácido-base estándar.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "bicarbonato alterado, compatible con posible trastorno ácido-base metabólico, considerar función renal y contexto clínico (vómito/diarrea)".
- **prohibited_inferences:** diagnóstico definitivo de tipo de trastorno ácido-base sin gasometría.
- **uncertainty_notes:** el panel venoso ambulatorio de Saludly permite aproximar pero no confirmar con precisión un trastorno ácido-base — comunicar esta limitación.
- **professional_review:** bicarbonato marcadamente alterado, especialmente combinado con función renal alterada o síntomas (confusión, taquipnea, síntomas de cetoacidosis).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - electrolytes
  - acid_base
  - renal
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando panel electrolítico completo o función renal"
  - "sospecha de trastorno ácido-base"

combine_with: [sodium, potassium, chloride, creatinine, egfr]

do_not_use_alone:
  - "diagnóstico de tipo de trastorno ácido-base sin gasometría"

do_not_conclude:
  - "tipo específico de acidosis/alcalosis sin gasometría"

escalate_when:
  - "bicarbonato marcadamente alterado con función renal comprometida o síntomas"
```
