---
doc_id: SLD-BIO-088
biomarker_id: estradiol
name_es: Estradiol
name_en: Estradiol (E2)
abbreviation: E2
sinonimos:
- Estradiol
- E2
- Estradiol (E2)
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-011
combine_with:
- fsh
- lh
- progesterone
- shbg
tier: 3
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

# Estradiol (E2)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Se lee con la fase del ciclo calculada con la fecha de última menstruación (SEG-011).
- Reglas que usan esta ficha: SEG-011. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-088. E2. Categoría: Endocrinología. Tipo: measured_analyte. Tier 3 — alta variabilidad por ciclo, requiere contexto específico.

## B. Definición

Principal estrógeno en mujeres premenopáusicas, producido predominantemente por los folículos ováricos. Sus niveles fluctúan de forma predecible a lo largo del ciclo menstrual — la interpretación sin conocer el día del ciclo es prácticamente imposible.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia) o LC-MS/MS (más preciso en niveles bajos, ej. posmenopausia).

### Condiciones de toma de muestra — CRÍTICO

- **Ciclo menstrual: determinante absoluto de la interpretación.** Debe registrarse el día del ciclo o la fase (folicular/ovulatoria/lútea) al momento de la toma.
- **Sexo:** rangos completamente distintos hombres/mujeres/posmenopausia.
- **Ayuno:** no requiere.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, por fase (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Fase folicular:** ~70-500 pmol/L (~19-136 pg/mL), más baja al inicio de la fase folicular temprana.
- **Pico preovulatorio:** típicamente >300 pg/mL (puede llegar a 130-400 pg/mL según variabilidad individual, algunos laboratorios reportan límites superiores hasta 750 pg/mL).
- **Fase lútea:** ~200-800 pmol/L (~100-150 pg/mL en fase lútea temprana/media, cayendo a ~40 pg/mL en fase lútea tardía).
- **Posmenopausia:** generalmente <100-180 pmol/L, frecuentemente <40 pmol/L.
- **Hombres:** niveles considerablemente más bajos que en mujeres premenopáusicas.
- **URLs fuente:** https://endocrinology.testcatalog.org/show/EEST (Mayo Clinic Labs) ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8042396/ (estudio multicéntrico de 85 mujeres, ensayo Elecsys) ; https://www.dramytung.com/blog/hormone-blood-tests-for-women-understanding-estradiol-progesterone-and-testosterone-ranges — todas verificadas esta sesión (ago-2026).
- **Nota de variabilidad interensayo:** el estudio multicéntrico (PMC8042396) enfatiza que los inmunoensayos automatizados muestran sesgos variables entre plataformas — enfatiza la necesidad de rangos específicos por método, no un valor único universal.

## E. Interpretación

- **Bajo en mujer premenopáusica joven:** sugiere hipogonadismo — si LH/FSH están elevadas, indica falla gonadal primaria.
- **Alto con ciclos irregulares/ausentes:** sugiere posible SOP, tumor productor de andrógenos o de estrógenos — requiere evaluación adicional (testosterona, androstenediona, DHEA-S, SHBG, y posiblemente imagen).

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorio: día del ciclo menstrual o fase, estado menopáusico, uso de anticonceptivos hormonales o terapia hormonal (altera completamente la interpretación).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: FSH, LH (obligatorio para diferenciar causa central vs ovárica), Progesterona (para confirmar ovulación), SHBG.
- `cannot_conclude`: diagnóstico sin conocer la fase del ciclo.

## H. Tendencias

### Tendencias temporales

Su "tendencia" real es intracíclica (varía día a día dentro de un mismo ciclo) — no se compara entre controles de fechas distintas sin ajustar por fase del ciclo.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — uso exclusivamente dirigido por indicación.

## J. Pruebas complementarias

### Pruebas complementarias posibles

FSH, LH, Progesterona; testosterona/DHEA-S/SHBG si hay sospecha de hiperandrogenismo.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin conocer el día del ciclo o estado menopáusico. Escalar ante hipogonadismo confirmado con FSH/LH elevadas, o patrón sugestivo de tumor productor de hormonas.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Labs + estudio multicéntrico de validación de ensayo).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "estradiol interpretado según fase del ciclo o estado menopáusico declarado".
- **prohibited_inferences:** cualquier interpretación sin conocer fase del ciclo/estado menopáusico/uso de hormonas exógenas.
- **uncertainty_notes:** variabilidad interensayo significativa entre plataformas — usar el rango del laboratorio aliado.
- **professional_review:** hipogonadismo confirmado, o patrón sugestivo de SOP/tumor productor de hormonas.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - reproductive_hormones
  - tier_3
  - saludly_brain_v1
use_when:
  - "evaluación de fertilidad, ciclo menstrual, o sospecha de hipogonadismo/hiperandrogenismo"
combine_with: [fsh, lh, progesterone, shbg]
do_not_use_alone:
  - "cualquier interpretación sin conocer fase del ciclo o estado menopáusico"
do_not_conclude:
  - "diagnóstico sin FSH/LH concurrentes"
escalate_when:
  - "hipogonadismo confirmado con FSH/LH elevadas"
  - "patrón sugestivo de tumor productor de hormonas"
```
