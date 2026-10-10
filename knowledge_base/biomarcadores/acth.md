---
doc_id: SLD-BIO-096
biomarker_id: acth
name_es: ACTH
name_en: Adrenocorticotropic Hormone
abbreviation: ACTH
sinonimos:
- ACTH
- Corticotropina
- Hormona adrenocorticotropa
- ACTH (Hormona Adrenocorticotropa)
- Adrenocorticotropic Hormone
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: Plasma EDTA refrigerado de inmediato
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-002
combine_with:
- cortisol
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
- 'Medido a todos: revisión médica obligatoria; interpretación solo en la vista del médico (SEG-002).'
---

# ACTH (Corticotropina)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Medido a todos: revisión médica obligatoria; interpretación solo en la vista del médico (SEG-002).
- Reglas que usan esta ficha: SEG-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-096. ACTH. Categoría: Endocrinología. Tipo: measured_analyte. **Tier 4 — EXCLUIDO del panel preventivo general**, confirmado en esta auditoría: requiere protocolo dinámico e interpretación obligatoria junto a cortisol.

## B. Definición

Hormona hipofisaria que estimula la producción de cortisol suprarrenal. Su valor es casi exclusivamente interpretable en relación con el cortisol simultáneo — ACTH aislada, sin cortisol de la misma muestra, tiene escaso valor clínico.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (plasma, tubo especial refrigerado — la ACTH es inestable a temperatura ambiente) · Método: inmunoensayo.

### Condiciones de toma de muestra — CRÍTICO

- **Horario:** rangos de referencia establecidos **solo para tomas entre 7-10 AM** (Mayo Clinic Laboratories) — **no existen valores de referencia establecidos para tomas vespertinas**.
- **Manejo de la muestra:** requiere procesamiento y refrigeración inmediatos por inestabilidad de la hormona — factor logístico crítico para un modelo de toma a domicilio.
- **Debe medirse siempre junto a cortisol de la misma muestra.**

## E. Interpretación

### Interpretación (siempre junto a cortisol — verificado esta sesión, Mayo Clinic Laboratories)

- **Cortisol bajo + ACTH elevada:** insuficiencia suprarrenal **primaria** (falla de la glándula suprarrenal misma).
- **Cortisol bajo + ACTH no elevada:** insuficiencia suprarrenal **secundaria** (causa hipofisaria o hipotalámica).
- **Cortisol alto (Cushing) + ACTH suprimida:** consistente con adenoma o carcinoma suprarrenal productor de cortisol, o hiperplasia micronodular primaria, o uso de corticosteroides exógenos.
- **Contexto de incidentaloma suprarrenal (estudio retrospectivo de 468 pacientes, verificado esta sesión):** ACTH <10 pg/mL combinado con DHEA-S <40 mcg/dL tuvo la mayor precisión diagnóstica (92% especificidad, 87% VPP) para secreción autónoma de cortisol (definida como cortisol post-supresión con dexametasona >1.8 mcg/dL).

## F. Contexto del paciente y confusores

### Contexto del paciente

Hora exacta de la toma (obligatorio), cortisol de la misma muestra (obligatorio), medicamentos (corticoides exógenos suprimen ACTH), síntomas de insuficiencia o exceso suprarrenal.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Cortisol (absolutamente obligatorio, nunca interpretar ACTH sin cortisol concurrente), DHEA-S (contexto de incidentaloma suprarrenal).
- `cannot_conclude`: primaria vs secundaria sin cortisol concurrente; diagnóstico definitivo sin pruebas dinámicas de confirmación.

## H. Tendencias

### Tendencias temporales

No aplica seguimiento longitudinal de rutina — uso diagnóstico dirigido.

## I. Prevención

### Contexto preventivo

Ninguno — excluido del panel general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Cortisol (obligatorio), DHEA-S, pruebas dinámicas (supresión con dexametasona, estimulación con Cosyntropin) según el patrón encontrado.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

NO interpretar ACTH sin cortisol de la misma muestra. Escalar SIEMPRE que se solicite este biomarcador — requiere evaluación endocrinológica.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories) + estudio retrospectivo de cohorte (468 pacientes con adenoma suprarrenal, 2000-2020) para el contexto de incidentaloma.
- **Fuentes verificadas esta sesión:** https://www.mayocliniclabs.com/test-catalog/overview/8411 ; https://pediatric.testcatalog.org/show/ACTH ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8301396/ (estudio DHEA-S/ACTH en secreción autónoma de cortisol).

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "ACTH interpretado junto a cortisol de la misma muestra, para diferenciar causa primaria vs secundaria de disfunción suprarrenal".
- **prohibited_inferences:** cualquier interpretación de ACTH sin cortisol concurrente; diagnóstico definitivo sin pruebas dinámicas.
- **uncertainty_notes:** hormona inestable — requiere manejo de muestra específico (refrigeración inmediata), factor logístico relevante para toma a domicilio.
- **professional_review:** SIEMPRE que se solicite o aparezca — requiere evaluación endocrinológica dirigida.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - adrenal
  - pituitary
  - tier_4
  - saludly_brain_v1
use_when:
  - "solo con cortisol concurrente, en sospecha clínica dirigida de disfunción suprarrenal"
combine_with: [cortisol, dhea_s]
do_not_use_alone:
  - "cualquier interpretación sin cortisol concurrente"
do_not_conclude:
  - "diagnóstico definitivo sin pruebas dinámicas de confirmación"
escalate_when:
  - "SIEMPRE — requiere evaluación endocrinológica dirigida"
```
