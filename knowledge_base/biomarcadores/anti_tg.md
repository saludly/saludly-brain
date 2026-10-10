---
doc_id: SLD-BIO-069
biomarker_id: anti_tg
name_es: Anticuerpos Antitiroglobulina
name_en: Anti-Thyroglobulin Antibodies
abbreviation: Anti-Tg / TgAb
sinonimos:
- Anti-Tg
- Anticuerpos antitiroglobulina
- Anticuerpos Antitiroglobulina
- Anti-Tg / TgAb
- Anti-Thyroglobulin Antibodies
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
- anti_tpo
- tsh
- free_t4
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Anticuerpos Antitiroglobulina (Anti-Tg)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M2-TI-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-069. Anti-Tg/TgAb. Categoría: Tiroides. Tipo: analito medido. Tier 3 — mismo racional que Anti-TPO, pero de menor sensibilidad diagnóstica cuando se usa solo.

## B. Definición

Anticuerpos contra la tiroglobulina, la proteína precursora de las hormonas tiroideas. En el contexto de tiroiditis autoinmune, Anti-Tg tiene **menor sensibilidad que Anti-TPO** cuando se usa de forma aislada — su rol principal en el catálogo de Saludly es complementario, no de primera línea.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia). Unidad: UI/mL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Evidencia primaria verificada esta sesión:** estudio de 2,030 pacientes consecutivos evaluados con ambos anticuerpos: **anti-TPO (antimicrosomal) positivo en 99% de los casos de tiroiditis de Hashimoto, frente a solo 36% para Anti-Tg** — diferencia de sensibilidad sustancial que confirma cuantitativamente el racional ya expuesto en esta ficha. Conclusión de la fuente: *"TgAb testing is not recommended for the diagnosis of Hashimoto's thyroiditis"* (no se recomienda Anti-Tg como prueba de diagnóstico de tiroiditis de Hashimoto, precisamente por su baja sensibilidad comparada con Anti-TPO).
- **Prevalencia en población general (verificado esta sesión):** autoanticuerpos tiroideos presentes en aproximadamente 3-10% de la población general sin enfermedad tiroidea manifiesta — relevante para no generar alarma ante una positividad aislada sin TSH alterada.
- **URL fuente:** https://emedicine.medscape.com/article/2086797-overview — verificado esta sesión (ago-2026). Nivel de evidencia: revisión clínica basada en estudio de cohorte grande (2,030 pacientes).

## E. Interpretación

- **Positivo:** compatible con tiroiditis autoinmune, especialmente relevante cuando Anti-TPO es negativo pero la sospecha clínica persiste (un pequeño porcentaje de personas con Hashimoto tiene solo Anti-Tg positivo, sin Anti-TPO).

## F. Contexto del paciente y confusores

### Contexto del paciente

Los mismos que Anti-TPO: embarazo, síntomas de hipotiroidismo, antecedente familiar de enfermedad tiroidea autoinmune.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Anti-TPO (obligatorio como primera línea — Anti-Tg es complementario, no sustituto), TSH, T4 libre.
- `cannot_conclude`: diagnóstico de hipotiroidismo sin TSH alterada.

## H. Tendencias

### Tendencias temporales

Igual racional que Anti-TPO — no requiere seguimiento frecuente una vez confirmado.

## I. Prevención

Su valor preventivo es complementario a Anti-TPO, para los casos donde este es negativo pero la sospecha clínica persiste.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Anti-TPO (si no se solicitó junto — es la prueba de primera línea).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado poblacional ni de primera línea — Tier 3, uso complementario a Anti-TPO.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento endocrinológico estándar sobre serología de tiroiditis autoinmune.
- **Fuente:** Medscape, "Antithyroglobulin: Reference Range, Interpretation." Estudio de cohorte de 2,030 pacientes. https://emedicine.medscape.com/article/2086797-overview — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "Anti-Tg positivo, considerar junto a Anti-TPO y TSH para evaluar autoinmunidad tiroidea, especialmente si Anti-TPO es negativo pero hay sospecha clínica".
- **prohibited_inferences:** diagnóstico de hipotiroidismo a partir de Anti-Tg aislado sin TSH alterada.
- **uncertainty_notes:** menor sensibilidad que Anti-TPO cuando se usa solo — no debe ser la primera prueba solicitada.
- **professional_review:** igual criterio que Anti-TPO — positivo con TSH límite y síntomas, embarazo o antecedente de pérdida gestacional.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - thyroid
  - autoimmune
  - tier_3
  - saludly_brain_v1

use_when:
  - "Anti-TPO negativo con alta sospecha clínica de tiroiditis autoinmune"

combine_with: [anti_tpo, tsh, free_t4]

do_not_use_alone:
  - "diagnóstico de hipotiroidismo sin TSH alterada"
  - "cribado de primera línea (usar Anti-TPO primero)"

do_not_conclude:
  - "hipotiroidismo confirmado a partir de Anti-Tg aislado"

escalate_when:
  - "positivo con TSH límite y síntomas, embarazo o antecedente de pérdida gestacional"
```
