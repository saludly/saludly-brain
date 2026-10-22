---
doc_id: SLD-BIO-061
biomarker_id: free_t4
name_es: T4 libre
name_en: Free T4 (Free Thyroxine)
abbreviation: T4L / FT4
sinonimos:
- T4 libre
- Tiroxina libre
- FT4
- T4L
- T4L / FT4
- Free T4 (Free Thyroxine)
category: thyroid
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-TI-001
- COND-M2-TI-002
- COND-M2-TI-003
- COND-M2-TI-004
- COND-M2-TI-005
- COND-M2-TI-006
combine_with:
- tsh
- total_t3
- anti_tpo
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Desde el 22 de octubre de 2026 va en el panel estándar, para todas las personas, junto con la TSH (decisión de Carlos). Antes era refleja.'
---

# T4 libre (Tiroxina libre)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Desde el 22 de octubre de 2026 va en el panel estándar, para todas las personas, junto con la TSH (decisión de Carlos). Antes era refleja.
- Reglas que usan esta ficha: COND-M2-TI-001, COND-M2-TI-002, COND-M2-TI-003, COND-M2-TI-004, COND-M2-TI-005, COND-M2-TI-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-061. T4L/FT4. Categoría: Tiroides. Tipo: analito medido. **Tier 1 — incluido no por tener un programa de cribado poblacional propio, sino por ser de combinación obligatoria con TSH** (ver nota de auditoría en `00_INDEX.md`).

## B. Definición

Fracción no unida a proteínas (biológicamente activa) de la tiroxina, la principal hormona producida por la tiroides. A diferencia de TSH (que es el marcador de cribado más sensible), T4 libre es lo que permite **clasificar** una alteración de TSH como subclínica o manifiesta.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Perfil tiroideo · Método: inmunoensayo (quimioluminiscencia), idealmente de segunda generación para minimizar interferencia por proteínas de unión. Unidad: ng/dL (alt: pmol/L). No requiere ayuno estricto.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Nota sobre rango de referencia:** el rango de T4 libre es fuertemente dependiente de la plataforma de inmunoensayo utilizada (mayor variabilidad interlaboratorio que TSH) — por eso no existe un valor numérico único citable como consenso universal; esto es una característica reconocida del analito, no una brecha de investigación pendiente de resolver. Saludly debe registrar la plataforma del laboratorio aliado y usar su rango de referencia específico.

## E. Interpretación

- Se interpreta **siempre en combinación con TSH**, nunca de forma aislada:
  - TSH alta + T4 libre normal = hipotiroidismo subclínico.
  - TSH alta + T4 libre baja = hipotiroidismo manifiesto.
  - TSH baja + T4 libre normal = hipertiroidismo subclínico.
  - TSH baja + T4 libre alta = hipertiroidismo manifiesto.
  - TSH alta + T4 libre alta (patrón infrecuente) = considerar resistencia a hormona tiroidea o adenoma hipofisario secretor de TSH — hallazgo raro que amerita evaluación especializada.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: embarazo (los rangos de referencia cambian por trimestre), medicamentos que interfieren con proteínas transportadoras (estrógenos, corticoides en dosis altas), enfermedad no tiroidea aguda concurrente.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: TSH (obligatorio, siempre), T3 total (si hay sospecha de hipertiroidismo), Anti-TPO (si hay sospecha autoinmune).
- `cannot_conclude`: causa de la disfunción tiroidea (autoinmune vs otra) sin anticuerpos.

## H. Tendencias

### Tendencias temporales

Cambia más lentamente que TSH ante alteraciones tiroideas leves (TSH es más sensible a cambios tempranos) — la combinación de ambos permite distinguir alteración reciente de establecida.

## I. Prevención

Se solicita junto a TSH en el mismo contexto de cribado — no tiene indicación preventiva independiente.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Anti-TPO si hay sospecha autoinmune; T3 total si hay sospecha de hipertiroidismo con T4 libre normal (T3-toxicosis, poco frecuente pero descrita).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es en sí misma una prueba de cribado poblacional (ese rol lo cumple TSH) — es la prueba de **clasificación** una vez que TSH ya está alterada.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento endocrinológico estándar sobre el eje hipotálamo-hipófisis-tiroides.
- **Fuente del algoritmo de combinación con TSH:** AACE/ATA Hypothyroidism Guideline, https://www.guidelinecentral.com/guideline/6855/ ; algoritmo diagnóstico Quest/AAFP/ATA/AACE, https://www.questdiagnostics.com/content/dam/corporate/unrestricted/documents/other/thyroid_summary_of_practice_guidelines_brochure/Thyroid_Summary_of_Practice_Guidelines_Brochure.pdf — verificadas esta sesión (ago-2026). El valor numérico de referencia sigue siendo específico de cada plataforma de laboratorio (ver nota en sección D), no un umbral universal.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "en combinación con TSH, permite clasificar la alteración tiroidea como subclínica o manifiesta".
- **prohibited_inferences:** cualquier clasificación de hipotiroidismo/hipertiroidismo con T4 libre sin TSH concurrente.
- **uncertainty_notes:** el patrón TSH alta + T4 libre alta es infrecuente y requiere evaluación especializada, no interpretación automática.
- **professional_review:** cualquier combinación TSH/T4 libre discordante con el patrón esperado, o T4 libre marcadamente alterada.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - thyroid
  - endocrine
  - tier_1
  - saludly_brain_v1

use_when:
  - "TSH está alterada y se requiere clasificar subclínico vs manifiesto"

combine_with: [tsh, total_t3, anti_tpo]

do_not_use_alone:
  - "clasificación de disfunción tiroidea sin TSH concurrente"

do_not_conclude:
  - "causa autoinmune sin anticuerpos"
  - "tipo de disfunción tiroidea sin TSH"

escalate_when:
  - "TSH y T4 libre discordantes con el patrón esperado"
  - "T4 libre marcadamente alterada"
```
