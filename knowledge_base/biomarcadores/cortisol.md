---
doc_id: SLD-BIO-090
biomarker_id: cortisol
name_es: Cortisol
name_en: Cortisol
abbreviation: CORT
sinonimos:
- Cortisol
- Cortisol matutino
- Cortisol AM
- CORT
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-002
- COND-M2-TI-009
combine_with:
- acth
- dhea_s
tier: 4
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: true
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Medido a todos: ''escalar siempre'' se traduce en revisión médica obligatoria; solo se interpreta con toma entre 6:00 y 10:00 (SEG-002).'
---

# Cortisol

## Notas de decisión de Saludly (6 de octubre de 2026)

- Medido a todos: 'escalar siempre' se traduce en revisión médica obligatoria; solo se interpreta con toma entre 6:00 y 10:00 (SEG-002).
- Reglas que usan esta ficha: SEG-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-090. CORT. Categoría: Endocrinología. Tipo: measured_analyte. **Tier 4 — EXCLUIDO del panel preventivo general** (confirmado en esta auditoría): alta variabilidad circadiana, requiere protocolo dinámico (no una sola toma) para ser interpretable con confianza.

## B. Definición

Hormona del eje hipotálamo-hipófisis-suprarrenal, con el ritmo circadiano más marcado de todo el catálogo hormonal: pico entre 6-8 AM, nadir alrededor de las 11 PM. Una sola medición sin conocer la hora exacta y sin protocolo específico tiene valor interpretativo muy limitado.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Mayo Clinic Laboratories especifica: **muestra matutina (8 AM) preferida, aceptable entre 6-10:30 AM.** No existen valores de referencia establecidos para tomas vespertinas — esto por sí solo excluye a este biomarcador de un panel de laboratorio a domicilio sin horario controlado estricto.

### Condiciones de toma de muestra — CRÍTICO

- **Horario: absolutamente crítico**, con ventana estrecha (6-10:30 AM) y sin valores de referencia para otros horarios.
- **Ayuno:** no especificado como crítico, pero el estrés de la venopunción en sí puede elevar transitoriamente el cortisol.
- **Estrés agudo:** cualquier situación de estrés físico o emocional reciente eleva el cortisol de forma aguda, independiente del eje hipotálamo-hipófisis-suprarrenal basal.

## E. Interpretación

- **Un valor bajo aislado NO es diagnóstico de insuficiencia suprarrenal congénita ni adquirida** — Mayo Clinic Laboratories declara explícitamente que un cortisol plasmático bajo no da indicación concluyente por sí solo.
- **Elevado:** estrés agudo, síndrome de Cushing (requiere pruebas dinámicas de confirmación — supresión con dexametasona —, no un valor aislado).
- **Disminuido:** insuficiencia suprarrenal (requiere ACTH concurrente para diferenciar primaria de secundaria — ver `acth.md`), o simplemente toma fuera del horario de pico.

## F. Contexto del paciente y confusores

### Contexto del paciente

Hora exacta de la toma (obligatorio), nivel de estrés físico/emocional reciente, medicamentos (corticoides exógenos suprimen el eje), síntomas (fatiga, hipotensión si se sospecha insuficiencia; ganancia de peso central, estrías si se sospecha Cushing).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ACTH (obligatorio para diferenciar causa primaria vs secundaria en sospecha de insuficiencia suprarrenal), DHEA-S (útil en el contexto de incidentaloma suprarrenal y secreción autónoma de cortisol).
- `pattern_examples`: cortisol bajo + ACTH alta = insuficiencia suprarrenal primaria (falla de la glándula); cortisol bajo + ACTH baja/normal = insuficiencia secundaria (causa hipofisaria/hipotalámica).
- `cannot_conclude`: diagnóstico de Cushing o insuficiencia suprarrenal con un solo valor aislado sin protocolo dinámico (supresión con dexametasona, o estimulación con ACTH sintético).

## H. Tendencias

### Tendencias temporales

No aplica un seguimiento longitudinal de rutina tipo "control cada 6 meses" — su uso es diagnóstico dirigido y dinámico, no de tendencia preventiva.

## I. Prevención

### Contexto preventivo

**Ninguno.** Este es explícitamente uno de los biomarcadores que Saludly Brain conoce pero nunca ofrece en un panel autoiniciado por el usuario.

## J. Pruebas complementarias

### Pruebas complementarias posibles

ACTH (obligatorio si se sospecha insuficiencia o exceso), prueba de supresión con dexametasona o estimulación con ACTH sintético (Cosyntropin) — protocolos dinámicos fuera del alcance de un panel de laboratorio a domicilio.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

**NO interpretar** un valor aislado fuera de protocolo como diagnóstico de nada. **Escalar siempre** ante sospecha clínica de insuficiencia suprarrenal (síntomas de crisis addisoniana: hipotensión severa, debilidad extrema) o de Cushing — esto requiere evaluación endocrinológica con protocolo dinámico, no interpretación por IA de un valor aislado.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories, guías Endocrine Society referenciadas).
- **Fuentes verificadas esta sesión:** https://www.testcatalog.org/show/CORTO (Mayo Clinic) ; https://www.mayocliniclabs.com/test-catalog/overview/8411 (ACTH, referencia cruzada) ; guías Endocrine Society citadas: "Diagnosis and treatment of primary adrenal insufficiency" (*J Clin Endocrinol Metab* 2016) y "The diagnosis of Cushing's syndrome" (*Endocrine Society*).

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** ninguna interpretación autónoma fuerte de un valor aislado — este es uno de los biomarcadores del catálogo donde el sistema debe ser más conservador, junto con troponina y NRBC.
- **prohibited_inferences:** cualquier diagnóstico de Cushing o insuficiencia suprarrenal a partir de un valor único sin protocolo dinámico.
- **uncertainty_notes:** sin hora exacta de la toma y sin protocolo dinámico, el valor es prácticamente no interpretable con confianza clínica.
- **professional_review:** SIEMPRE que se solicite o aparezca este biomarcador — requiere evaluación endocrinológica dirigida, no interpretación automática.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - adrenal
  - tier_4
  - saludly_brain_v1
use_when:
  - "solo si ya existe sospecha clínica dirigida de insuficiencia suprarrenal o Cushing, con protocolo dinámico"
combine_with: [acth, dhea_s]
do_not_use_alone:
  - "cualquier interpretación de un valor aislado sin protocolo dinámico"
do_not_conclude:
  - "diagnóstico de Cushing o insuficiencia suprarrenal sin pruebas dinámicas"
escalate_when:
  - "SIEMPRE — requiere evaluación endocrinológica dirigida"
```
