---
doc_id: SLD-BIO-092
biomarker_id: fsh
name_es: FSH
name_en: Follicle-Stimulating Hormone
abbreviation: FSH
sinonimos:
- FSH
- Hormona folículo estimulante
- FSH (Hormona Folículo Estimulante)
- Follicle-Stimulating Hormone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mUI/mL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: mujeres
alimenta:
- COND-M5-MU-002
- COND-M5-MU-004
combine_with:
- lh
- estradiol
- testosterone_total
tier: 4
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- En menores de 40 años, FSH > 25 UI/L (COND-M5-MU-002); desde los 45 no se usa para menopausia (NICE NG23). El umbral de menopausia de esta ficha no se usa con pacientes.
---

# FSH (Hormona Folículo Estimulante)

## Notas de decisión de Saludly (6 de octubre de 2026)

- En menores de 40 años, FSH > 25 UI/L (COND-M5-MU-002); desde los 45 no se usa para menopausia (NICE NG23). El umbral de menopausia de esta ficha no se usa con pacientes.
- Reglas que usan esta ficha: COND-M5-MU-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-092. FSH. Categoría: Endocrinología. Tipo: measured_analyte. **Tier 4 — EXCLUIDO del panel preventivo general**, confirmado en esta auditoría: alta variabilidad por ciclo/edad, solo estudio de fertilidad/eje gonadal dirigido.

## B. Definición

Gonadotropina hipofisaria que controla la gametogénesis en ambos sexos. Junto con LH, define las fases del ciclo menstrual (pico a mitad de ciclo separa fase folicular de lútea).

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo. **Factor preanalítico importante (Mayo Clinic Laboratories, verificado esta sesión):** suplementos de biotina en dosis altas (300 mg/día) pueden interferir con el ensayo — se recomienda suspender biotina 12 horas antes de la toma.

### Condiciones de toma de muestra — CRÍTICO

- **Ciclo menstrual:** determinante — debe conocerse el día del ciclo, salvo que el objetivo sea confirmar menopausia.
- **Biotina:** suspender suplementos con biotina (incluyendo suplementos de pelo/piel/uñas) 12 horas antes.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión)

- **Umbral de menopausia (Medical News Today, resumiendo consenso clínico, verificado esta sesión):** FSH ≥30 UI/L combinado con ausencia de menstruación por 1 año es indicativo de menopausia — aunque los médicos no requieren la prueba para diagnosticar menopausia (el diagnóstico suele ser clínico).
- **Referencia institucional para hombres (Strong Memorial Hospital, citado en revisión 2011):** rango normal 1.4-18.1 UI/L; valores >4.5 UI/L se han asociado con análisis de semen anormal en algunos estudios.
- **Nota de variabilidad:** los rangos varían considerablemente entre laboratorios e instituciones — Saludly debe usar el rango específico del laboratorio aliado.
- **URLs fuente:** https://endocrinology.testcatalog.org/show/FSH ; https://www.medicalnewstoday.com/articles/317746 — verificadas esta sesión (ago-2026).

## E. Interpretación

### Interpretación (Mayo Clinic Laboratories, verificado esta sesión)

- **Elevada (en ambos sexos):** hipogonadismo **primario** (falla gonadal/testicular/ovárica) — el eje hipotálamo-hipófisis intenta compensar produciendo más FSH.
- **Disminuida:** falla de la hipófisis o el hipotálamo (hipogonadismo **secundario**).

## F. Contexto del paciente y confusores

### Contexto del paciente

Día del ciclo menstrual o estado menopáusico, uso de biotina, síntomas de fertilidad/menopausia.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: LH (obligatorio — se interpretan siempre juntos), Estradiol (mujeres), Testosterona total (hombres).
- `pattern_examples`: FSH y LH ambos elevados = hipogonadismo primario; FSH y LH ambos bajos = hipogonadismo secundario (hipofisario/hipotalámico).
- `cannot_conclude`: diagnóstico de menopausia solo con FSH — el diagnóstico es clínico (historia de amenorrea), FSH es de apoyo.

## H. Tendencias

### Tendencias temporales

Aumenta progresivamente en la transición a la menopausia — relevante seguimiento en ese contexto específico, no como marcador de tendencia general.

## I. Prevención

### Contexto preventivo

Ninguno — excluido del panel general por indicación específica de fertilidad/menopausia.

## J. Pruebas complementarias

### Pruebas complementarias posibles

LH (siempre en conjunto), Estradiol o Testosterona según sexo, TSH y Prolactina si hay irregularidad menstrual (para descartar otras causas).

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar menopausia solo con FSH sin historia clínica de amenorrea. Escalar ante hipogonadismo confirmado (FSH/LH alteradas + hormona gonadal alterada) con impacto en fertilidad o síntomas significativos.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "FSH interpretado junto a LH y hormona gonadal correspondiente, para diferenciar hipogonadismo primario de secundario".
- **prohibited_inferences:** diagnóstico de menopausia o infertilidad solo con FSH.
- **uncertainty_notes:** verificar uso reciente de biotina antes de interpretar un resultado inesperado.
- **professional_review:** hipogonadismo confirmado con impacto en fertilidad, o discordancia inesperada con la clínica.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - reproductive_hormones
  - tier_4
  - saludly_brain_v1
use_when:
  - "evaluación de fertilidad o confirmación de estado menopáusico"
combine_with: [lh, estradiol, testosterone_total]
do_not_use_alone:
  - "diagnóstico de menopausia o hipogonadismo sin LH concurrente"
do_not_conclude:
  - "menopausia confirmada solo con FSH sin historia clínica"
escalate_when:
  - "hipogonadismo confirmado con impacto en fertilidad"
```
