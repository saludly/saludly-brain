---
doc_id: SLD-BIO-093
biomarker_id: lh
name_es: LH
name_en: Luteinizing Hormone
abbreviation: LH
sinonimos:
- LH
- Hormona luteinizante
- LH (Hormona Luteinizante)
- Luteinizing Hormone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mUI/mL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-011
combine_with:
- fsh
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
- Se lee con la fase del ciclo calculada con la fecha de última menstruación (SEG-011).
---

# LH (Hormona Luteinizante)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Se lee con la fase del ciclo calculada con la fecha de última menstruación (SEG-011).
- Reglas que usan esta ficha: SEG-011. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-093. LH. Categoría: Endocrinología. Tipo: measured_analyte. **Tier 4 — EXCLUIDO del panel preventivo general**, mismo racional que FSH.

## B. Definición

Gonadotropina hipofisaria cuyo pico a mitad de ciclo desencadena la ovulación. Se interpreta siempre junto a FSH.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo. **Factor preanalítico (Mayo Clinic Laboratories, verificado esta sesión):** suspender suplementos de biotina 12 horas antes de la toma (mismo racional que FSH).

### Condiciones de toma de muestra

Día del ciclo menstrual crítico para interpretación (salvo objetivo de confirmar menopausia, donde FSH es la prueba preferida según Mayo Clinic). Suspender biotina 12h antes.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método, con variación marcada por fase del ciclo (pico ovulatorio muy superior a fase folicular/lútea).
- **Nota de precisión analítica (Mayo Clinic, verificado esta sesión):** límite de cuantificación de 0.01 UI/L — en contextos pediátricos donde se requiere mayor sensibilidad analítica, existe un ensayo pediátrico específico (LHPED).
- **Para confirmar estado menopáusico, Mayo Clinic recomienda usar FSH, no LH** — dato relevante para el diseño de Saludly: no ofrecer LH como prueba de confirmación menopáusica.

## E. Interpretación

### Interpretación (Mayo Clinic Laboratories, verificado esta sesión)

- **Elevada (junto a FSH elevada):** hipogonadismo primario.
- **Disminuida (junto a FSH disminuida):** falla de la hipófisis o el hipotálamo.

## F. Contexto del paciente y confusores

### Contexto del paciente

Día del ciclo menstrual, uso de biotina, síntomas de fertilidad.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: FSH (obligatorio), Estradiol/Progesterona (mujeres), Testosterona total (hombres).
- `pattern_examples`: pico de LH a mitad de ciclo precede a la ovulación por ~24-36h — usado en kits de predicción de ovulación (fuera del alcance actual de Saludly).
- `cannot_conclude`: diagnóstico sin FSH concurrente.

## H. Tendencias

### Tendencias temporales

Su "tendencia" relevante es intracíclica (pico ovulatorio), no de seguimiento longitudinal entre controles distintos.

## I. Prevención

### Contexto preventivo

Ninguno — excluido del panel general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

FSH (siempre en conjunto), Estradiol/Progesterona o Testosterona según sexo y contexto.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin FSH concurrente ni sin conocer el día del ciclo. Escalar ante hipogonadismo confirmado con impacto en fertilidad.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories).
- **Fuentes verificadas esta sesión:** https://endocrinology.testcatalog.org/show/LH ; https://www.mayocliniclabs.com/test-catalog/overview/602752

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "LH interpretado junto a FSH, para diferenciar hipogonadismo primario de secundario, o para timing de ovulación en contexto de fertilidad".
- **prohibited_inferences:** diagnóstico sin FSH concurrente; usar LH en vez de FSH para confirmar menopausia.
- **uncertainty_notes:** verificar uso reciente de biotina antes de interpretar un resultado inesperado.
- **professional_review:** hipogonadismo confirmado con impacto en fertilidad.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - reproductive_hormones
  - tier_4
  - saludly_brain_v1
use_when:
  - "evaluación de fertilidad, timing de ovulación, o sospecha de hipogonadismo junto a FSH"
combine_with: [fsh, estradiol, testosterone_total]
do_not_use_alone:
  - "diagnóstico sin FSH concurrente"
do_not_conclude:
  - "confirmación de menopausia (usar FSH para esto, no LH)"
escalate_when:
  - "hipogonadismo confirmado con impacto en fertilidad"
```
