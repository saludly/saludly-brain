---
doc_id: SLD-BIO-067
biomarker_id: free_t3
name_es: T3 Libre (Triyodotironina libre)
name_en: Free T3 (Free Triiodothyronine)
abbreviation: T3L / FT3
sinonimos:
- T3 libre
- Triyodotironina libre
- FT3
- T3L
- T3 Libre (Triyodotironina libre)
- T3 Libre
- T3L / FT3
- Free T3 (Free Triiodothyronine)
category: thyroid
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
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
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- El panel usa T3 libre como refleja; la ATA prefiere T3 total. Decisión pendiente del médico.
---

# T3 Libre (Triyodotironina libre)

## Notas de decisión de Saludly (6 de octubre de 2026)

- El panel usa T3 libre como refleja; la ATA prefiere T3 total. Decisión pendiente del médico.
- Reglas que usan esta ficha: COND-M2-TI-004, COND-M2-TI-005. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-067. T3L/FT3. Categoría: Tiroides. Tipo: analito medido. Tier 3 — indicado específicamente ante sospecha de hipertiroidismo con T4 libre normal, no como cribado inicial.

## B. Definición

Fracción activa de T3, la hormona tiroidea con mayor actividad biológica (T4 se convierte en T3 en los tejidos periféricos). Según el algoritmo diagnóstico estándar de sociedades como AAFP/ATA/AACE (verificado esta sesión), T3 total/libre se mide específicamente cuando TSH está baja pero T4 libre es normal, para identificar el escenario de **"T3-toxicosis"** — hipertiroidismo causado por exceso aislado de T3, que de otra forma pasaría desapercibido si solo se midiera T4 libre.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia). Unidad: pg/mL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (algoritmo diagnóstico AAFP/ATA/AACE, verificado esta sesión):** en el flujo diagnóstico de TSH baja, si T4 libre está por encima del rango normal → hipertiroidismo; si T4 libre está dentro del rango normal → medir T3 total; si T3 está por encima del rango normal → confirma T3-toxicosis (patrón de hipertiroidismo Graves u otra causa); si T3 está dentro de rango → considerar otras causas de TSH suprimida (fármacos, enfermedad no tiroidea). Fuente: algoritmo de Quest Diagnostics adaptado de AAFP/ATA/AACE, verificado esta sesión — https://www.questdiagnostics.com/content/dam/corporate/unrestricted/documents/other/thyroid_summary_of_practice_guidelines_brochure/Thyroid_Summary_of_Practice_Guidelines_Brochure.pdf

## E. Interpretación

- **Elevada (con TSH baja y T4 libre normal):** T3-toxicosis — patrón de hipertiroidismo que requiere la misma evaluación y manejo que el hipertiroidismo clásico, pese a que T4 libre por sí sola no lo hubiera detectado.
- **Normal (con TSH baja y T4 libre normal):** sugiere causa no tiroidea de TSH suprimida (fármacos como corticoides/dopamina, enfermedad no tiroidea aguda) — no hipertiroidismo verdadero.

## F. Contexto del paciente y confusores

### Contexto del paciente

Síntomas de hipertiroidismo (palpitaciones, pérdida de peso, temblor, intolerancia al calor), medicamentos que pueden suprimir TSH sin hipertiroidismo real (corticoides, dopamina).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: TSH y T4 libre (obligatorio — T3 libre solo tiene sentido diagnóstico en el contexto específico de TSH baja + T4 libre normal).
- `cannot_conclude`: causa autoinmune específica sin Anti-TPO si se sospecha Graves.

## H. Tendencias

### Tendencias temporales

Relevante principalmente como prueba puntual de confirmación diagnóstica en el algoritmo de hipertiroidismo, no como marcador de seguimiento longitudinal de rutina.

## I. Prevención

No aplica como marcador preventivo independiente — es una prueba de confirmación diagnóstica dirigida.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Anti-TPO/TRAb (anticuerpos de receptor de TSH, no incluidos en el catálogo actual) si se confirma T3-toxicosis y se busca establecer causa autoinmune (Graves).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado — es una prueba de segunda línea en el algoritmo diagnóstico de hipertiroidismo, específicamente cuando TSH está baja y T4 libre es normal.

## L. Evidencia

### Evidencia científica

- **Nivel:** algoritmo diagnóstico adaptado de guías de sociedades médicas (AAFP, ATA, AACE) — evidencia consolidada de práctica clínica estándar.
- **Fuente:** https://www.questdiagnostics.com/content/dam/corporate/unrestricted/documents/other/thyroid_summary_of_practice_guidelines_brochure/Thyroid_Summary_of_Practice_Guidelines_Brochure.pdf — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "en el contexto de TSH baja con T4 libre normal, T3 libre elevada confirma T3-toxicosis (patrón de hipertiroidismo)".
- **prohibited_inferences:** solicitar o interpretar T3 libre sin TSH/T4 libre concurrentes; diagnóstico de causa autoinmune sin anticuerpos.
- **uncertainty_notes:** su valor diagnóstico depende completamente del contexto de TSH/T4 libre — fuera de ese algoritmo específico, tiene poco valor interpretativo.
- **professional_review:** T3-toxicosis confirmada, o síntomas marcados de hipertiroidismo independientemente del resultado numérico exacto.

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

escalate_when:
  - "T3-toxicosis confirmada"
  - "síntomas marcados de hipertiroidismo"
```
