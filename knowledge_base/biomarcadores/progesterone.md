---
doc_id: SLD-BIO-089
biomarker_id: progesterone
name_es: Progesterona
name_en: Progesterone
abbreviation: PROG
sinonimos:
- Progesterona
- PROG
- Progesterone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: mujeres
alimenta:
- SEG-011
combine_with:
- estradiol
- fsh
- lh
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Solo se mide en mujeres; se lee con la fase del ciclo (SEG-011).
---

# Progesterona

## Notas de decisión de Saludly (6 de octubre de 2026)

- Solo se mide en mujeres; se lee con la fase del ciclo (SEG-011).
- Reglas que usan esta ficha: SEG-011. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-089. PROG. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3.

## B. Definición

Hormona producida por el cuerpo lúteo tras la ovulación (y por la placenta en el embarazo). Su elevación en la fase lútea es la confirmación bioquímica estándar de que hubo ovulación.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia).

### Condiciones de toma de muestra — CRÍTICO

- **Ciclo menstrual: determinante absoluto.** Debe tomarse en fase lútea media (~día 21 de un ciclo de 28 días, o ~7 días después de la ovulación estimada) para el propósito de confirmar ovulación — tomarla en el momento equivocado del ciclo invalida la interpretación.
- **Sexo:** en hombres y mujeres posmenopáusicas, niveles siempre bajos (<0.5 ng/mL).

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente por fase (evidencia verificada esta sesión, Mayo Clinic/Cleveland Clinic/ACOG concordantes)

- **Fase folicular:** <1 ng/mL.
- **Fase lútea:** 2-25 ng/mL, con pico ~7 días después de la ovulación.
- **Umbral de confirmación de ovulación (Mayo Clinic Laboratories, verificado esta sesión):** progesterona en fase lútea media **>10 ng/mL confirma ovulación**; <10 ng/mL puede indicar anovulación o toma en momento incorrecto del ciclo.
- **Posmenopausia y hombres:** <0.5 ng/mL.
- **URLs fuente:** https://themetabolicjournal.com/biomarkers/progesterone-levels (compendio de rangos Mayo Clinic/Cleveland Clinic/ACOG) ; https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11744920 (<2 ng/mL preovulatorio, >5 ng/mL posovulatorio) — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada en fase lútea media (>10 ng/mL):** confirma que hubo ovulación en ese ciclo.
- **Baja en fase lútea media (<10 ng/mL):** anovulación, insuficiencia lútea, o toma en momento incorrecto del ciclo — requiere repetir con timing correcto antes de concluir.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorio: día del ciclo, regularidad menstrual, uso de anticonceptivos hormonales, embarazo (los niveles aumentan progresivamente y no son comparables con el ciclo no gestante).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Estradiol, LH (el pico de LH precede a la ovulación por ~24-36h).
- `cannot_conclude`: insuficiencia lútea con una sola medición — típicamente requiere evaluación en más de un ciclo.

## H. Tendencias

### Tendencias temporales

Igual que estradiol: la "tendencia" relevante es intracíclica, no entre controles de fechas distintas sin ajustar por día del ciclo.

## I. Prevención

### Contexto preventivo

No aplica como cribado general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Estradiol, LH, seguimiento en más de un ciclo si se sospecha insuficiencia lútea.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin conocer el día del ciclo. Escalar ante sospecha de insuficiencia lútea recurrente en contexto de infertilidad, o anovulación persistente.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories, Cleveland Clinic, ACOG — fuentes concordantes).
- Verificadas esta sesión (ago-2026), ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "progesterona en fase lútea media >10 ng/mL confirma ovulación; <10 ng/mL sugiere repetir con timing correcto antes de concluir anovulación".
- **prohibited_inferences:** diagnóstico de infertilidad o insuficiencia lútea con una sola medición.
- **uncertainty_notes:** el timing de la toma es tan importante como el valor numérico — un valor bajo puede reflejar toma en el día incorrecto, no patología real.
- **professional_review:** anovulación persistente en varios ciclos, o sospecha de insuficiencia lútea en contexto de infertilidad.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - reproductive_hormones
  - fertility
  - tier_3
  - saludly_brain_v1
use_when:
  - "confirmando ovulación o evaluando fertilidad"
combine_with: [estradiol, fsh, lh]
do_not_use_alone:
  - "diagnóstico de infertilidad o insuficiencia lútea con una sola medición"
do_not_conclude:
  - "anovulación sin verificar timing correcto de la toma"
escalate_when:
  - "anovulación persistente en varios ciclos"
  - "sospecha de insuficiencia lútea en contexto de infertilidad"
```
