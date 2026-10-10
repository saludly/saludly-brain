---
doc_id: SLD-BIO-057
biomarker_id: albumin
name_es: Albúmina
name_en: Albumin
abbreviation: ALB
sinonimos:
- Albúmina
- Albúmina sérica
- ALB
- Albumin
category: hepatology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: g/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-TI-007
- COND-M5-UR-A01
- COND-M6-MI-A02
- COND-M6-MI-002
combine_with:
- globulin
- ag_ratio
- creatinine
- egfr
- alt
- ast
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Albúmina

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M2-TI-007, COND-M5-UR-A01, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-057. ALB. Categoría: Hepatología (nota de auditoría: consolidada aquí desde la lista original del usuario, donde aparecía duplicada en "Metabolismo" e "Hígado" — un solo registro). Tipo: analito medido. Tier 1.

## B. Definición

Proteína sintetizada exclusivamente por el hígado; es la proteína más abundante en plasma. Refleja tanto función de síntesis hepática como estado nutricional y, de forma indirecta, pérdida renal de proteínas (síndrome nefrótico) cuando está muy disminuida.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Panel metabólico/hepático · Método colorimétrico (verde de bromocresol, estándar) · Unidad: g/dL. No requiere ayuno. Variable preanalítica: hemoconcentración/hemodilución (torniquete prolongado, postura) puede alterar levemente el valor.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal en adultos **3.5-5.5 g/dL** (algunas fuentes 3.5-5.0 g/dL — variación menor entre fuentes académicas).
- **URL fuente:** ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf), NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y Medscape Lab Values Normal Adult (https://emedicine.medscape.com/article/2172316-overview) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Disminuida:** desnutrición proteico-calórica, hepatopatía crónica (reducción de síntesis), síndrome nefrótico (pérdida renal), inflamación/infección aguda (reactante de fase aguda negativo — disminuye con la inflamación independientemente del estado nutricional real), enteropatía perdedora de proteínas.
- **Elevada:** rara vez tiene significado clínico relevante de forma aislada; casi siempre refleja deshidratación/hemoconcentración.
- **Dentro del intervalo:** no descarta hepatopatía temprana — la albúmina tiene una vida media larga (~20 días), por lo que cambios agudos de función hepática pueden no reflejarse todavía en un valor puntual.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: estado nutricional, infección/inflamación reciente (reactante de fase aguda negativo — mismo principio de confusión que ferritina pero en dirección opuesta), función hepática y renal conocidas, embarazo (dilución fisiológica).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Globulinas y relación Albúmina/Globulina (calculados a partir de proteínas totales), ALT/AST/Bilirrubina (función hepática), Creatinina/eGFR (si se sospecha pérdida renal).
- `pattern_examples`: albúmina baja + proteinuria (fuera del alcance actual de Saludly, requiere módulo de orina) = sugiere síndrome nefrótico; albúmina baja + transaminasas alteradas + INR/PT prolongado = sugiere insuficiencia hepática de síntesis.
- `cannot_conclude`: causa específica de hipoalbuminemia sin contexto clínico e inflamatorio (hs-CRP ayuda a diferenciar inflamación de desnutrición/hepatopatía real).

## H. Tendencias

### Tendencias temporales

Dada su vida media larga (~20 días), es un marcador de función hepática/nutricional de evolución **lenta** — no refleja cambios agudos. Una tendencia descendente sostenida en varios controles es más relevante que un valor puntual bajo aislado (que puede deberse a inflamación transitoria).

## I. Prevención

Acciones razonables: evaluación nutricional, seguimiento si hay tendencia descendente sostenida.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Proteínas totales/globulinas si no se solicitaron juntas; función hepática completa; hs-CRP para diferenciar inflamación de causa real.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Marcador de cribado de función hepática/estado nutricional — no diagnóstico de una condición específica por sí solo.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento bioquímico/hepatológico estándar, ampliamente reproducido; su comportamiento como reactante de fase aguda negativo está bien documentado en fisiología clínica.
- **Fuente:** ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf), NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y Medscape Lab Values Normal Adult (https://emedicine.medscape.com/article/2172316-overview) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "albúmina baja compatible con posible desnutrición, hepatopatía, proceso inflamatorio reciente, o pérdida renal — requiere contexto para diferenciar".
- **prohibited_inferences:** diagnóstico específico (síndrome nefrótico, cirrosis) a partir de albúmina aislada.
- **uncertainty_notes:** la inflamación aguda reciente reduce la albúmina independientemente del estado nutricional/hepático real — mismo tipo de confusión que ferritina, en dirección opuesta.
- **professional_review:** albúmina marcadamente baja, especialmente con edema, o combinada con alteración hepática/renal ya documentada.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - nutrition
  - renal
  - tier_1
  - saludly_brain_v1

use_when:
  - "evaluando función hepática de síntesis"
  - "evaluando estado nutricional"
  - "sospecha de pérdida de proteínas (renal o digestiva)"

combine_with: [globulin, ag_ratio, creatinine, egfr, alt, ast]

do_not_use_alone:
  - "diagnóstico de síndrome nefrótico, cirrosis, o desnutrición"

do_not_conclude:
  - "causa específica de hipoalbuminemia sin contexto inflamatorio/nutricional/hepático/renal"

escalate_when:
  - "albúmina marcadamente baja"
  - "edema concurrente"
  - "combinación con función hepática o renal ya alterada"
```
