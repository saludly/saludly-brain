---
doc_id: SLD-BIO-085
biomarker_id: testosterone_total
name_es: Testosterona Total
name_en: Total Testosterone
abbreviation: T total
sinonimos:
- Testosterona total
- Testosterona Total
- T total
- Total Testosterone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M5-MU-001
- COND-M5-UR-002
combine_with:
- testosterone_free
- shbg
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Corte adoptado en hombres: 264 ng/dL armonizado por el CDC (Endocrine Society 2018), solo con método certificado (COND-M5-UR-002). Esta ficha cita 240 a 950 ng/dL (Mayo 2013); manda la ficha de condición.'
---

# Testosterona Total

## Notas de decisión de Saludly (6 de octubre de 2026)

- Corte adoptado en hombres: 264 ng/dL armonizado por el CDC (Endocrine Society 2018), solo con método certificado (COND-M5-UR-002). Esta ficha cita 240 a 950 ng/dL (Mayo 2013); manda la ficha de condición.
- Reglas que usan esta ficha: COND-M5-MU-001, COND-M5-UR-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-085. T total. Categoría: Endocrinología. Tipo: measured_analyte. Tier 2 — indicado por síntomas, no cribado general.

## B. Definición

Suma de testosterona libre (~2%), unida débilmente a albúmina (~68%) y unida fuertemente a SHBG (~30%, biológicamente no disponible). Es la prueba de primera línea para evaluar el eje gonadal, pero su interpretación depende críticamente de SHBG cuando este está alterado (ver `shbg.md`).

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia) o LC-MS/MS (más preciso, especialmente en mujeres y niños donde los niveles son bajos). Unidad: ng/dL (alt: nmol/L, factor ×0.0347).

### Condiciones de toma de muestra

- **Horario: crítico** — debe tomarse en la mañana (7-10 AM) por el ritmo circadiano marcado de la testosterona (niveles más altos en la mañana).
- **Ayuno:** no requiere.
- **Sexo:** determinante para el rango de referencia.
- **Repetición:** las guías de Endocrine Society y EAU recomiendan **dos mediciones matutinas consistentemente bajas** antes de establecer diagnóstico de hipogonadismo — un solo valor bajo no es suficiente.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Laboratory reference interval (Mayo Clinic Laboratories, verificado esta sesión):**
  - Hombres ≥19 años: **240-950 ng/dL**
  - Mujeres ≥19 años: **8-60 ng/dL**
- **URL fuente:** https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9482678 (tabla Mayo Clinic 2013, referenciada en documentación técnica) — verificado esta sesión (ago-2026). **Nota de variabilidad poblacional:** un estudio en hombres filipinos sanos (21-40 años) encontró un rango de referencia distinto (7.33-53.01 nmol/L, equivalente a ~211-1,528 ng/dL) — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7719543/, verificado esta sesión, ilustrando que los rangos "estándar" pueden no generalizar perfectamente entre poblaciones.

## E. Interpretación

- **Baja (hombres):** hipogonadismo primario (testicular) o secundario (hipotálamo-hipofisario) — requiere LH/FSH para diferenciar.
- **Baja con SHBG alterado:** la testosterona total puede estar falsamente baja o alta si SHBG está alterado (ej. obesidad reduce SHBG; hipertiroidismo lo aumenta) — en ese caso, testosterona libre calculada o medida por diálisis de equilibrio es más confiable (ver `testosterone_free.md`).
- **Alta (mujeres):** síndrome de ovario poliquístico, hiperplasia suprarrenal congénita, tumor productor de andrógenos (poco frecuente).

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: hora de la toma, medicamentos (corticoides, estrógenos orales alteran SHBG), síntomas específicos, IMC (afecta SHBG).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: SHBG (obligatorio si hay sospecha de discordancia), Testosterona libre, LH/FSH (para diferenciar origen primario vs secundario).
- `cannot_conclude`: diagnóstico de hipogonadismo con un solo valor sin confirmación con segunda medición matutina.

## H. Tendencias

### Tendencias temporales

Disminuye gradualmente con la edad en hombres (~1-2% anual desde los 30-40 años) — un descenso dentro de ese rango esperado no es necesariamente patológico.

## I. Prevención

### Contexto preventivo

Cribado dirigido por síntomas, no cribado poblacional general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

SHBG, Testosterona libre, LH/FSH según el contexto clínico.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar hipogonadismo con un solo valor. Escalar ante confirmación con dos valores matutinos bajos y síntomas concordantes.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (referencia institucional Mayo Clinic) + evidencia de variabilidad poblacional documentada.
- **Fuente del algoritmo diagnóstico (dos mediciones matutinas):** guías de European Association of Urology (EAU) y Endocrine Society, referenciadas en estudio de validación poblacional. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7719543/
- Verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "testosterona baja/alta, considerar SHBG y repetir en la mañana antes de concluir".
- **prohibited_inferences:** diagnóstico de hipogonadismo con un solo valor; recomendar terapia de reemplazo hormonal (decisión médica).
- **uncertainty_notes:** fuertemente dependiente de SHBG y de la hora de la toma — un valor de la tarde no es interpretable de la misma forma.
- **professional_review:** dos valores matutinos consistentemente bajos con síntomas, o valores muy elevados en mujeres.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - hormones
  - tier_2
  - saludly_brain_v1
use_when:
  - "síntomas de hipogonadismo o hiperandrogenismo"
combine_with: [testosterone_free, shbg]
do_not_use_alone:
  - "diagnóstico de hipogonadismo con un solo valor"
do_not_conclude:
  - "diagnóstico definitivo sin segunda medición matutina y SHBG"
escalate_when:
  - "dos valores matutinos bajos consistentes con síntomas"
  - "valores muy elevados en mujeres"
```
