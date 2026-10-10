---
doc_id: SLD-BIO-094
biomarker_id: prolactin
name_es: Prolactina
name_en: Prolactin
abbreviation: PRL
sinonimos:
- Prolactina
- PRL
- Prolactin
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: mujeres
alimenta:
- COND-M5-MU-003
combine_with:
- fsh
- lh
- tsh
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Siempre se repite; macroprolactina refleja; al paciente nunca se le mencionan tumores, aunque esta ficha cite cortes de macroadenoma (COND-M5-MU-003).
---

# Prolactina (PRL)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Siempre se repite; macroprolactina refleja; al paciente nunca se le mencionan tumores, aunque esta ficha cite cortes de macroadenoma (COND-M5-MU-003).
- Reglas que usan esta ficha: COND-M5-MU-003. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-094. PRL. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3.

## B. Definición

Hormona hipofisaria que controla la lactancia, bajo regulación inhibitoria principal de dopamina. Su elevación patológica más frecuente es por prolactinoma (tumor hipofisario) o por efecto de medicamentos que bloquean dopamina.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (Elecsys, quimioluminiscencia).

### Condiciones de toma de muestra

No requiere ayuno estricto, aunque el estrés de la venopunción puede elevarla levemente. No requiere horario específico crítico como cortisol.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión, Mayo Clinic Laboratories)

- **Correlación tumor-prolactina:** los macroadenomas hipofisarios (>10 mm de diámetro) se asocian típicamente con prolactina **>250 ng/mL**; una concentración **>500 ng/mL es diagnóstica de macroprolactinoma**.
- **Limitación importante:** elevaciones moderadas de prolactina NO son una guía confiable para determinar si existe un adenoma hipofisario productor de prolactina — el diagnóstico definitivo combina el valor con imagen (resonancia hipofisaria).
- **Seguimiento de tratamiento:** tras iniciar tratamiento médico de prolactinomas, la prolactina debe disminuir sustancialmente; 60-80% de pacientes alcanzan niveles normales.
- **URL fuente:** https://www.mayocliniclabs.com/test-catalog/overview/85670 ; https://endocrinology.testcatalog.org/show/PRL — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** prolactinoma, medicamentos (antipsicóticos, metoclopramida, domperidona, estrógenos, opiáceos, alfa-metildopa, cimetidina, antidepresivos — lista amplia de causas medicamentosas verificada esta sesión), hipotiroidismo (la TRH elevada en hipotiroidismo estimula prolactina), embarazo (fisiológico), estrés físico/venopunción (elevación leve transitoria).
- **Macroprolactina:** en hiperprolactinemia asintomática, se sugiere evaluar macroprolactina (prolactina unida a inmunoglobulina, biológicamente menos activa) — la detección varía según el inmunoensayo usado.

## F. Contexto del paciente y confusores

### Contexto del paciente

Medicamentos (lista extensa de causas farmacológicas — ver sección F), función tiroidea (TSH), embarazo, síntomas (galactorrea, cefalea, alteraciones visuales, irregularidad menstrual, disfunción sexual).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: TSH (descartar hipotiroidismo como causa), FSH/LH (la hiperprolactinemia suprime el eje gonadal).
- `pattern_examples`: prolactina >500 ng/mL = diagnóstico de macroprolactinoma; prolactina moderadamente elevada + medicamento causal identificado = probable causa farmacológica, no tumoral.
- `cannot_conclude`: presencia de adenoma hipofisario con elevaciones moderadas sin imagen — el valor y el tamaño tumoral no siempre correlacionan de forma confiable en ese rango.

## H. Tendencias

### Tendencias temporales

Debe disminuir sustancialmente tras iniciar tratamiento de un prolactinoma confirmado — útil para seguimiento de respuesta terapéutica.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — uso dirigido por síntomas.

## J. Pruebas complementarias

### Pruebas complementarias posibles

TSH (descartar hipotiroidismo), revisión de medicamentos, resonancia hipofisaria si hay sospecha de tumor (especialmente con prolactina >250-500 ng/mL o síntomas visuales/cefalea).

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar prolactinoma con elevaciones moderadas sin imagen. Escalar ante prolactina >250 ng/mL, especialmente con cefalea o alteraciones visuales (sospecha de macroadenoma con efecto de masa).

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "prolactina elevada, revisar medicamentos y función tiroidea antes de sospechar causa tumoral; valores >250-500 ng/mL sugieren fuertemente macroadenoma".
- **prohibited_inferences:** diagnóstico definitivo de prolactinoma sin imagen hipofisaria.
- **uncertainty_notes:** elevaciones moderadas no correlacionan de forma confiable con presencia/tamaño de adenoma — requiere imagen para confirmar.
- **professional_review:** prolactina >250 ng/mL, especialmente con cefalea, alteraciones visuales, galactorrea o irregularidad menstrual significativa.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - pituitary
  - tier_3
  - saludly_brain_v1
use_when:
  - "galactorrea, cefalea con síntomas visuales, o irregularidad menstrual sin causa clara"
combine_with: [fsh, lh, tsh]
do_not_use_alone:
  - "diagnóstico de prolactinoma sin imagen hipofisaria"
do_not_conclude:
  - "tamaño o presencia de tumor solo con el valor de prolactina en rangos moderados"
escalate_when:
  - "prolactina >250 ng/mL"
  - "cefalea o alteraciones visuales concurrentes"
```
