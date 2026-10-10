---
doc_id: SLD-BIO-087
biomarker_id: shbg
name_es: SHBG
name_en: Sex Hormone-Binding Globulin
abbreviation: SHBG
sinonimos:
- SHBG
- Globulina fijadora de hormonas sexuales
- SHBG (Globulina Transportadora de Hormonas Sexuales)
- Sex Hormone-Binding Globulin
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: nmol/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M5-MU-001
- COND-M5-UR-002
- COND-M5-UR-A01
combine_with:
- testosterone_total
- testosterone_free
- estradiol
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

# SHBG (Globulina Transportadora de Hormonas Sexuales)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M5-MU-001, COND-M5-UR-002, COND-M5-UR-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-087. SHBG. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3 — complementario a testosterona/estradiol, no aislado.

## B. Definición

Proteína hepática que transporta testosterona y estradiol en sangre, dejándolos biológicamente inactivos mientras están unidos. Su nivel determina qué fracción de testosterona/estradiol total está realmente disponible para los tejidos.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia).

### Condiciones de toma de muestra

No requiere ayuno estricto. Sexo relevante para el rango de referencia.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión)

- **Laboratory reference interval (documentado en caso clínico de deficiencia genética de SHBG, verificado esta sesión):** rango de referencia reportado **14-72 nmol/L** (contexto: hombre adulto) — Saludly debe validar el rango exacto por sexo con el laboratorio aliado, dado que las mujeres típicamente tienen valores más altos que los hombres por efecto estrogénico.
- **URL fuente:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12635475/ — verificado esta sesión (ago-2026). Caso clínico ilustrativo: deficiencia genética de SHBG (2 nmol/L, muy por debajo del rango) causó testosterona total baja con testosterona libre calculada falsamente normal, requiriendo diálisis de equilibrio para confirmar el hipogonadismo bioquímico real.

## E. Interpretación

- **Elevado:** hipertiroidismo, cirrosis hepática, uso de estrógenos orales/anticonceptivos, envejecimiento (SHBG aumenta gradualmente con la edad).
- **Disminuido:** obesidad, resistencia a la insulina/diabetes tipo 2, hipotiroidismo, síndrome nefrótico, uso de andrógenos/corticoides.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorio: IMC, función tiroidea, función hepática, medicamentos (estrógenos, andrógenos, corticoides), edad.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Testosterona total (obligatorio — SHBG explica discordancias entre testosterona total y libre), Estradiol.
- `pattern_examples`: SHBG bajo (por obesidad) + testosterona total baja + testosterona libre normal = la testosterona biológicamente activa puede ser normal pese a testosterona total baja — no diagnosticar hipogonadismo solo con el valor total en este escenario.
- `cannot_conclude`: estado hormonal real sin considerar testosterona/estradiol junto a SHBG.

## H. Tendencias

### Tendencias temporales

Cambia lentamente con IMC, función tiroidea/hepática — relevante para explicar cambios en testosterona total en controles sucesivos sin cambio real en la fracción biodisponible.

## I. Prevención

### Contexto preventivo

No aplica como cribado — uso exclusivamente interpretativo/complementario.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Testosterona libre por diálisis de equilibrio si hay discordancia significativa entre SHBG extremo y la clínica.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No usar testosterona total sola para diagnosticar hipogonadismo sin considerar SHBG. Escalar ante SHBG muy alterado (extremos) con síntomas discordantes del valor de testosterona total.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte, con caso clínico ilustrativo de la limitación de no considerar SHBG.
- Fuente verificada esta sesión: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12635475/

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "SHBG alterado, considerar su efecto sobre la interpretación de testosterona/estradiol totales antes de concluir sobre el estado hormonal real".
- **prohibited_inferences:** diagnóstico de hipogonadismo o exceso hormonal a partir de testosterona/estradiol total sin considerar SHBG cuando este es extremo.
- **uncertainty_notes:** en casos de SHBG muy alterado, la testosterona libre calculada puede ser engañosa — considerar medición directa por diálisis de equilibrio.
- **professional_review:** SHBG en extremos con síntomas discordantes del valor de testosterona/estradiol total.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - hormones
  - tier_3
  - saludly_brain_v1
use_when:
  - "testosterona o estradiol total límite, para evaluar si SHBG explica la discordancia"
combine_with: [testosterone_total, testosterone_free, estradiol]
do_not_use_alone:
  - "diagnóstico hormonal sin testosterona/estradiol concurrentes"
do_not_conclude:
  - "estado hormonal real sin considerar el efecto de SHBG"
escalate_when:
  - "SHBG en extremos con síntomas discordantes del valor hormonal total"
```
