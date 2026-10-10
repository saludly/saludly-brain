---
doc_id: SLD-BIO-068
biomarker_id: anti_tpo
name_es: Anticuerpos Anti-Peroxidasa Tiroidea
name_en: Anti-Thyroid Peroxidase Antibodies
abbreviation: Anti-TPO / TPOAb
sinonimos:
- Anti-TPO
- Anticuerpos antiperoxidasa
- Ac anti TPO
- Anticuerpos Anti-Peroxidasa Tiroidea
- Anticuerpos Anti-TPO
- Anti-TPO / TPOAb
- Anti-Thyroid Peroxidase Antibodies
category: thyroid
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: UI/mL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M2-TI-A01
combine_with:
- tsh
- free_t4
- anti_tg
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

# Anticuerpos Anti-TPO

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M2-TI-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-068. Anti-TPO/TPOAb. Categoría: Tiroides. Tipo: analito medido. Tier 3 — indicado cuando TSH ya está alterada o hay sospecha autoinmune/embarazo, no como cribado poblacional aislado.

## B. Definición

Anticuerpos dirigidos contra la peroxidasa tiroidea, la enzima central en la síntesis de hormonas tiroideas. Su positividad es el marcador serológico más usado para identificar tiroiditis autoinmune (Hashimoto), la causa más frecuente de hipotiroidismo en zonas con suficiencia de yodo.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia). Unidad: UI/mL. No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Laboratory reference interval:** depende del laboratorio/método (positivo/negativo con un título específico según el ensayo).
- **Clinical decision threshold (AACE/ATA Hypothyroidism Guideline, verificado esta sesión):** en hipotiroidismo subclínico (TSH elevada, T4 libre normal), la guía conjunta AACE/ATA identifica **Anti-TPO positivo como uno de los criterios que justifica considerar tratamiento con levotiroxina**, junto con TSH >10 mIU/L, síntomas de hipotiroidismo, o deseo de embarazo — en ausencia de estos criterios, el tratamiento no está indicado de rutina. Fuente: https://www.guidelinecentral.com/guideline/6855/
- **Contexto de embarazo (ATA, verificado esta sesión):** en mujeres con TPOAb positivo y TSH por encima del rango de referencia específico del embarazo, se considera levotiroxina; en mujeres TPOAb-negativas con TSH normal, no se recomienda tratamiento. Fuente: https://www.endocrinologyadvisor.com/features/ata-guidelines-for-managing-subclinical-hypothyroidism-during-pregnancy-update/

## E. Interpretación

- **Positivo:** indica autoinmunidad tiroidea (tiroiditis de Hashimoto en la mayoría de los casos) — no equivale a hipotiroidismo en sí mismo; una persona puede tener Anti-TPO positivo y función tiroidea (TSH/T4 libre) completamente normal durante años.
- Su valor principal en el contexto de TSH límite es predictivo: identifica quiénes tienen mayor probabilidad de progresar a hipotiroidismo manifiesto en el futuro.

## F. Contexto del paciente y confusores

### Contexto del paciente

Embarazo o planificación de embarazo (crítico — cambia el umbral de decisión), antecedente de pérdida gestacional, síntomas de hipotiroidismo, antecedente familiar de enfermedad tiroidea autoinmune.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: TSH (obligatorio — Anti-TPO se interpreta como criterio adicional cuando TSH ya está alterada, no de forma aislada), T4 libre, Anti-Tg.
- `pattern_examples`: TSH límite (4.5-10 mIU/L) + Anti-TPO positivo = mayor probabilidad de progresión a hipotiroidismo manifiesto, criterio para considerar tratamiento según AACE/ATA; TSH normal + Anti-TPO positivo = autoinmunidad presente sin disfunción actual, requiere seguimiento periódico de TSH, no tratamiento.
- `cannot_conclude`: diagnóstico de hipotiroidismo a partir de Anti-TPO aislado sin TSH alterada.

## H. Tendencias

### Tendencias temporales

El título de Anti-TPO no necesita repetirse frecuentemente una vez confirmado positivo (a diferencia de TSH, que sí requiere seguimiento periódico) — es principalmente informativo para estratificar riesgo futuro, no para monitorear actividad de enfermedad en el corto plazo.

## I. Prevención

Su valor preventivo real está en identificar personas con mayor riesgo de progresión a hipotiroidismo manifiesto, para intensificar el seguimiento de TSH (más frecuente) en vez de esperar a que aparezcan síntomas.

## J. Pruebas complementarias

### Pruebas complementarias posibles

TSH y T4 libre (si no se solicitaron juntas — deben pedirse siempre en conjunto), seguimiento periódico de TSH si Anti-TPO es positivo con función tiroidea actualmente normal.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstico de hipotiroidismo por sí solo — es un marcador de riesgo/pronóstico que se usa junto a TSH para decisiones de seguimiento y, en casos específicos (TSH límite + síntomas o embarazo), de tratamiento.

## L. Evidencia

### Evidencia científica

- **Guideline (fuerte):** AACE/ATA Clinical Practice Guidelines for Hypothyroidism in Adults, 2012 (vigente como referencia consolidada). https://www.guidelinecentral.com/guideline/6855/
- **Guideline específica de embarazo (fuerte):** ATA Guidelines for Managing Thyroid Dysfunction During Pregnancy, actualización reportada 2024. https://www.endocrinologyadvisor.com/features/ata-guidelines-for-managing-subclinical-hypothyroidism-during-pregnancy-update/
- Ambas verificadas por búsqueda web esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "Anti-TPO positivo indica autoinmunidad tiroidea; en combinación con TSH límite, es un criterio reconocido para considerar seguimiento más cercano o, según contexto (síntomas, embarazo), conversación sobre tratamiento".
- **prohibited_inferences:** "Anti-TPO positivo = tiene hipotiroidismo" sin TSH alterada concurrente; decisión de tratamiento (siempre médica).
- **uncertainty_notes:** una persona con Anti-TPO positivo y función tiroidea normal puede permanecer así por años — no generar alarma desproporcionada sin TSH alterada.
- **professional_review:** Anti-TPO positivo con TSH límite (4.5-10 mIU/L) y síntomas, embarazo o planificación de embarazo, o antecedente de pérdida gestacional.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - thyroid
  - autoimmune
  - pregnancy_relevant
  - tier_3
  - saludly_brain_v1

use_when:
  - "TSH límite o alterada, para evaluar causa autoinmune y riesgo de progresión"
  - "embarazo o planificación de embarazo con TSH límite"

combine_with: [tsh, free_t4, anti_tg]

do_not_use_alone:
  - "diagnóstico de hipotiroidismo sin TSH alterada"

do_not_conclude:
  - "hipotiroidismo confirmado a partir de Anti-TPO aislado"

escalate_when:
  - "TSH límite + Anti-TPO positivo + síntomas, embarazo o planificación de embarazo"
```
