---
doc_id: SLD-BIO-067
biomarker_id: total_t3
name_es: T3 total (Triyodotironina total)
name_en: Total T3 (Total Triiodothyronine)
abbreviation: T3T / TT3
sinonimos:
- T3 total
- T3 Total
- Triyodotironina total
- Triyodotironina
- TT3
- T3T
- T3 total (Triyodotironina total)
- Total T3 (Total Triiodothyronine)
category: thyroid
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-TI-004
- COND-M2-TI-005
combine_with:
- tsh
- free_t4
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-22'
fuentes_estado: 'según la ficha original de T3 libre: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'T3 total en lugar de T3 libre, como prefiere la ATA (decisión de Carlos, 22 de octubre de 2026). Esta ficha reemplaza a la de T3 libre (free_t3) y conserva su doc_id.'
- 'Va en el panel estándar, para todas las personas, junto con la TSH y la T4 libre. Antes era refleja.'
- 'Las reglas comparan con el intervalo de referencia del laboratorio; no hay umbrales propios de Saludly.'
---

# T3 total (Triyodotironina total)

## Notas de decisión de Saludly (22 de octubre de 2026)

- T3 total en lugar de T3 libre, como prefiere la ATA (decisión de Carlos, 22 de octubre de 2026). Esta ficha reemplaza a la de T3 libre (free_t3) y conserva su doc_id.
- Va en el panel estándar, para todas las personas, junto con la TSH y la T4 libre. Antes era refleja.
- Las reglas comparan con el intervalo de referencia del laboratorio; no hay umbrales propios de Saludly.
- Reglas que usan esta ficha: COND-M2-TI-004, COND-M2-TI-005. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-067. T3T/TT3. Categoría: Tiroides. Tipo: analito medido. Tier 3 — su valor diagnóstico está en el contexto de TSH baja con T4 libre normal; en Saludly se mide a todas las personas junto con la TSH y la T4 libre.

## B. Definición

T3 total es toda la triyodotironina circulante, la unida a proteínas y la libre. La T3 es la hormona tiroidea con mayor actividad biológica (la T4 se convierte en T3 en los tejidos periféricos). Según el algoritmo diagnóstico estándar de sociedades como AAFP/ATA/AACE, la T3 (total o libre; la ATA prefiere la total) se mide cuando la TSH está baja y la T4 libre es normal, para identificar la **"T3-toxicosis"**: hipertiroidismo por exceso aislado de T3, que pasaría desapercibido si solo se midiera la T4 libre.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia). Unidad: ng/dL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio y del método; se usa el intervalo que reporta el laboratorio aliado.
- **Clinical decision threshold (algoritmo diagnóstico AAFP/ATA/AACE):** en el flujo diagnóstico de TSH baja, si la T4 libre está por encima del rango normal → hipertiroidismo; si la T4 libre está dentro del rango normal → medir T3 total; si la T3 está por encima del rango normal → confirma T3-toxicosis (patrón de hipertiroidismo, Graves u otra causa); si la T3 está dentro de rango → considerar otras causas de TSH suprimida (fármacos, enfermedad no tiroidea). Fuente: algoritmo de Quest Diagnostics adaptado de AAFP/ATA/AACE — https://www.questdiagnostics.com/content/dam/corporate/unrestricted/documents/other/thyroid_summary_of_practice_guidelines_brochure/Thyroid_Summary_of_Practice_Guidelines_Brochure.pdf

## E. Interpretación

- **Elevada (con TSH baja y T4 libre normal):** T3-toxicosis — patrón de hipertiroidismo que requiere la misma evaluación y manejo que el hipertiroidismo clásico, pese a que la T4 libre por sí sola no lo hubiera detectado.
- **Normal (con TSH baja y T4 libre normal):** sugiere causa no tiroidea de TSH suprimida (fármacos como corticoides o dopamina, enfermedad no tiroidea aguda) — no hipertiroidismo verdadero.
- **Con TSH normal:** se reporta como resultado observado; por sí sola no define un patrón.

## F. Contexto del paciente y confusores

### Contexto del paciente

Síntomas de hipertiroidismo (palpitaciones, pérdida de peso, temblor, intolerancia al calor), medicamentos que pueden suprimir la TSH sin hipertiroidismo real (corticoides, dopamina).

### Confusores propios de la T3 total

Por incluir la fracción unida a proteínas, la T3 total cambia cuando cambian las proteínas transportadoras: sube con el embarazo y con estrógenos (anticonceptivos orales, terapia hormonal) y baja con enfermedad aguda o desnutrición, sin que cambie la función tiroidea. La biotina en dosis altas interfiere con muchos inmunoensayos (ver pregunta de biotina).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: TSH y T4 libre (obligatorio — la T3 total solo tiene sentido diagnóstico en el contexto de TSH baja con T4 libre normal).
- `cannot_conclude`: causa autoinmune específica sin anti-TPO si se sospecha Graves.

## H. Tendencias

### Tendencias temporales

Relevante principalmente como prueba de confirmación en el algoritmo de hipertiroidismo, no como marcador de seguimiento longitudinal de rutina.

## I. Prevención

No aplica como marcador preventivo independiente — su papel es completar la lectura de la TSH y la T4 libre.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Anti-TPO o TRAb (anticuerpos contra el receptor de TSH, no incluidos en el catálogo actual) si se confirma T3-toxicosis y se busca establecer causa autoinmune (Graves).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado por sí sola — es una prueba de segunda línea en el algoritmo diagnóstico de hipertiroidismo, específicamente cuando la TSH está baja y la T4 libre es normal. En Saludly se mide a todos para tenerla disponible en ese caso sin repetir la toma.

## L. Evidencia

### Evidencia científica

- **Nivel:** algoritmo diagnóstico adaptado de guías de sociedades médicas (AAFP, ATA, AACE) — evidencia consolidada de práctica clínica estándar.
- **Fuente:** https://www.questdiagnostics.com/content/dam/corporate/unrestricted/documents/other/thyroid_summary_of_practice_guidelines_brochure/Thyroid_Summary_of_Practice_Guidelines_Brochure.pdf

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "en el contexto de TSH baja con T4 libre normal, T3 total elevada es compatible con T3-toxicosis (patrón de hipertiroidismo)".
- **prohibited_inferences:** interpretar la T3 total sin TSH y T4 libre concurrentes; diagnóstico de causa autoinmune sin anticuerpos; leer una T3 total alta en embarazo o con estrógenos como hipertiroidismo sin la TSH.
- **uncertainty_notes:** su valor diagnóstico depende del contexto de TSH y T4 libre, y la afectan las proteínas transportadoras.
- **professional_review:** T3-toxicosis compatible, o síntomas marcados de hipertiroidismo independientemente del resultado numérico exacto.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - thyroid
  - hyperthyroidism
  - tier_3
  - saludly_brain_v1

use_when:
  - "TSH baja con T4 libre normal — para descartar T3-toxicosis"
  - "sospecha clínica de hipertiroidismo"

combine_with: [tsh, free_t4]

do_not_use_alone:
  - "cualquier interpretación sin TSH y T4 libre concurrentes"

do_not_conclude:
  - "causa autoinmune específica (Graves) sin anticuerpos"
  - "hipertiroidismo con T3 total alta en embarazo o con estrógenos, sin la TSH"

escalate_when:
  - "T3-toxicosis compatible"
  - "síntomas marcados de hipertiroidismo"
```
