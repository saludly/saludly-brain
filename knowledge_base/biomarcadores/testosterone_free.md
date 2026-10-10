---
doc_id: SLD-BIO-086
biomarker_id: testosterone_free
name_es: Testosterona Libre
name_en: Free Testosterone
abbreviation: T libre
sinonimos:
- Testosterona libre
- Testosterona libre calculada
- Testosterona Libre
- T libre
- Free Testosterone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: No aplica (calculado)
nivel_catalogo: con patrón
panel: calculado
sexo: ambos
alimenta:
- COND-M5-UR-A01
combine_with:
- testosterone_total
- shbg
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

# Testosterona Libre

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M5-UR-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-086. T libre. Categoría: Endocrinología. Tipo: measured_analyte (idealmente por diálisis de equilibrio; con frecuencia calculada a partir de T total + SHBG cuando no se mide directamente). Tier 3.

## B. Definición

Fracción biológicamente activa de testosterona no unida a proteínas transportadoras. Es más precisa que la testosterona total cuando SHBG está alterado (obesidad, hipertiroidismo, cirrosis, uso de estrógenos/corticoides).

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · **Método de referencia:** diálisis de equilibrio (más preciso pero menos disponible) — el método de inmunoensayo directo tiene precisión limitada y no se recomienda como primera opción. Con frecuencia se calcula matemáticamente (fórmula de Vermeulen) a partir de testosterona total, SHBG y albúmina, en vez de medirse directamente.

### Condiciones de toma de muestra

Igual que testosterona total: horario matutino crítico por variación circadiana.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión)

- **Laboratory reference interval (Mayo Clinic, verificado esta sesión):** Hombres **9-30 ng/dL** · Mujeres **0.3-1.9 ng/dL**.
- **URL fuente:** https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9482678 — verificado esta sesión (ago-2026).
- **Nota metodológica importante (caso clínico documentado, verificado esta sesión):** un caso de deficiencia genética de SHBG mostró que la testosterona libre **calculada** puede ser normal pese a hipogonadismo bioquímico real confirmado por diálisis de equilibrio — el método calculado puede fallar cuando SHBG está muy alterado. Fuente: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12635475/. Esto refuerza que Saludly debe registrar si el valor de T libre es medido (diálisis) o calculado (fórmula), y comunicar esta distinción.

## E. Interpretación

Más confiable que testosterona total cuando SHBG está alterado — su interpretación aislada, sin conocer SHBG y testosterona total, tiene menor valor.

## F. Contexto del paciente y confusores

### Contexto del paciente

IMC, función tiroidea, medicamentos (estrógenos, corticoides), hora de la toma.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Testosterona total (obligatorio), SHBG (obligatorio para interpretar discordancias).
- `cannot_conclude`: diagnóstico sin conocer si el valor es medido o calculado, y sin testosterona total/SHBG.

## H. Tendencias

### Tendencias temporales

Igual patrón de descenso gradual con la edad que testosterona total.

## I. Prevención

### Contexto preventivo

No aplica como cribado — solo refinamiento diagnóstico.

## J. Pruebas complementarias

### Pruebas complementarias posibles

SHBG y testosterona total si no se solicitaron juntas; diálisis de equilibrio si el valor calculado es discordante con la clínica.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin testosterona total y SHBG. Escalar ante discordancia significativa entre el valor calculado y los síntomas clínicos (considerar diálisis de equilibrio).

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic) + caso clínico ilustrativo de limitación metodológica.
- Fuentes verificadas esta sesión: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9482678 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12635475/

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "testosterona libre interpretada junto a total y SHBG; si es calculada y discordante con síntomas, considerar diálisis de equilibrio".
- **prohibited_inferences:** diagnóstico definitivo basado en un valor calculado sin considerar sus limitaciones conocidas.
- **uncertainty_notes:** el método calculado puede fallar en casos de SHBG muy alterado — declarar si el valor es medido o calculado.
- **professional_review:** discordancia entre valor calculado y presentación clínica, o confirmación de hipogonadismo bioquímico.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - hormones
  - tier_3
  - saludly_brain_v1
use_when:
  - "testosterona total límite con SHBG alterado"
combine_with: [testosterone_total, shbg]
do_not_use_alone:
  - "diagnóstico sin testosterona total y SHBG"
do_not_conclude:
  - "diagnóstico definitivo de un valor calculado discordante sin diálisis de equilibrio"
escalate_when:
  - "discordancia entre valor calculado y clínica"
```
