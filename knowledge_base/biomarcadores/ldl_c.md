---
doc_id: SLD-BIO-040
biomarker_id: ldl_c
name_es: Colesterol LDL (LDL-C)
abbreviation: LDL-C
sinonimos:
- Colesterol LDL
- LDL
- LDL directo
- LDL calculado
- LDL-C
- Colesterol LDL (LDL-C)
category: Cardiovascular / Lípidos
subcategory: Perfil lipídico
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-CA-001
- COND-M1-CA-002
- COND-M1-CA-A01
combine_with:
- total_cholesterol
- hdl_c
- triglycerides
- apob
- lpa
- hs_crp
formula: 'Friedewald: LDL-C = CT − HDL-C − (TG/5) [mg/dL]; inválida si TG >400 mg/dL. Alternativa más precisa: Martin-Hopkins.'
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Cortes operativos de tamizaje: 130 mg/dL (COND-M1-CA-001) y 190 mg/dL (CA-002).'
---

# Colesterol LDL (LDL-C)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Cortes operativos de tamizaje: 130 mg/dL (COND-M1-CA-001) y 190 mg/dL (CA-002).
- Reglas que usan esta ficha: COND-M1-CA-001, COND-M1-CA-002, COND-M1-CA-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-040. LDL-C. Categoría: Cardiovascular / Lípidos. Tipo: calculated_parameter. Tier 1.

## B. Definición

Concentración de colesterol transportado en partículas LDL, principal vehículo de colesterol hacia tejidos periféricos y componente central del riesgo aterogénico cuando está elevado de forma sostenida.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero/plasma) · Perfil lipídico
- ¿Ayuno? Tradicionalmente sí (9-12h); guías recientes aceptan no-ayuno para cribado inicial — **Saludly debe registrar el protocolo del laboratorio aliado**.
- Factor preanalítico crítico: TG >400 mg/dL invalida la fórmula de Friedewald.

### 2. Resultado y tipo de dato

- Unidad: mg/dL (alt: mmol/L) · **Frecuentemente calculado** (ver frontmatter), puede ser medido directo según laboratorio.

## D. Intervalos y umbrales

```
clinical_decision_threshold: dependiente de riesgo cardiovascular global (no un único punto de corte universal)
screening_threshold: >190 mg/dL activa sospecha de hipercolesterolemia familiar
```

## E. Interpretación

- **Elevado:** mayor exposición acumulada a colesterol aterogénico.
- **Disminuido:** en general no alarmante, salvo malnutrición, hipertiroidismo severo o hepatopatía.
- Variabilidad preanalítica: afectada por ayuno y postura.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: antecedentes familiares de enfermedad cardiovascular precoz, tabaquismo, presión arterial, diabetes.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con: Colesterol total, HDL-C, Triglicéridos, ApoB, Lp(a), hs-CRP.
- **NO puede diagnosticar por sí solo enfermedad cardiovascular** ni predecir un evento individual.
- Alerta: >190 mg/dL → descartar hipercolesterolemia familiar. Complementaria: ApoB (más preciso en número de partículas).

## I. Prevención

- Alerta: aumento sostenido >20-30 mg/dL sin cambio de estilo de vida identificado.
- Prohibido: recomendar o suspender estatinas — decisión médica basada en riesgo cardiovascular global, no solo LDL-C.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ver `possible_follow_up_tests` implícito en la sección G (combine_with) y en `RAG_INSTRUCTIONS` al final de
este archivo — Saludly Brain no debe recomendar pruebas adicionales de forma automática; el lenguaje correcto
es "considerar evaluación adicional según contexto clínico", nunca una orden imperativa.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Este parámetro es una herramienta de cribado/seguimiento dentro de un panel preventivo, no una prueba
diagnóstica aislada de ninguna condición específica. Ver `prohibited_inferences.md` para el detalle de qué
conclusiones diagnósticas están prohibidas para este y el resto del catálogo.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte para el uso del perfil lipídico en cribado cardiovascular.
- **Fuente institucional de referencia:** AHA/ACC — guías de manejo de colesterol.
- **Clinical decision threshold (2026 ACC/AHA/Multisociety Dyslipidemia Guideline, publicada marzo 2026, verificado esta sesión):** reintroduce metas de tratamiento de LDL-C por categoría de riesgo:
  - **Prevención primaria, riesgo límite/intermedio:** <100 mg/dL
  - **Prevención primaria, riesgo alto** (incluye hipercolesterolemia familiar heterocigota, ≥1 factor de riesgo ASCVD, o aterosclerosis subclínica): <70 mg/dL
  - **Prevención secundaria (ASCVD clínica), riesgo no muy alto:** <70 mg/dL
  - **Prevención secundaria, riesgo muy alto:** <55 mg/dL (junto con no-HDL-C <85 mg/dL)
  - **Con score de calcio coronario (CAC):** CAC 1-99 UA → <100 mg/dL · CAC 100-299 UA o ≥percentil 75 → <70 mg/dL · CAC ≥1000 UA → <55 mg/dL
  - **Adultos jóvenes:** LDL-C ≥160 mg/dL o fuerte antecedente familiar de ASCVD precoz → indica consejería de hábitos de salud desde temprano.
- **URLs fuente:** https://www.acc.org/about-acc/press-releases/2026/03/13/18/01/accaha-issue-updated-guideline-for-managing-lipids-cholesterol ; https://www.lipid.org/nla/2026-accahamultisociety-dyslipidemia-guideline-released ; https://www.ahajournals.org/doi/10.1161/CIR.0000000000001423 — todas verificadas esta sesión (ago-2026).
- Nota de auditoría USPSTF (verificada sesión anterior): el cribado de colesterol total + HDL tiene recomendación B histórica; la evidencia para triglicéridos aislados fue calificada como insuficiente (I) — esto refuerza que LDL-C debe interpretarse siempre dentro del perfil completo, no aislado.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "biomarcador/factor relacionado con riesgo aterosclerótico, requiere evaluación de riesgo global".
- **Inferencia PROHIBIDA:** "LDL alto = tiene enfermedad cardiovascular".
- **Confianza por defecto:** media — requiere el resto del perfil para ser útil.
- **Activa evaluación profesional:** LDL-C >190 mg/dL, o perfil aterogénico combinado (LDL alto + HDL bajo + TG alto + ApoB alto).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular___lípidos
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["total_cholesterol", "hdl_c", "triglycerides", "apob", "lpa", "hs_crp"]

do_not_use_alone:
  - "diagnóstico de cualquier enfermedad"
  - "confirmación o descarte de riesgo sin el resto del panel relacionado"

do_not_conclude:
  - "presencia confirmada de una enfermedad a partir de este valor aislado"
  - "ausencia de enfermedad a partir de un valor dentro de rango"

escalate_when:
  - "resultado marcadamente fuera de rango"
  - "síntomas o contexto clínico preocupante concurrente"
  - "discordancia relevante con biomarcadores combinados obligatorios"
```

**Nota de retrofit:** este bloque RAG_INSTRUCTIONS fue añadido en la segunda auditoría (schema v2). El contenido
clínico de la ficha (secciones 1-10 arriba) no cambió — sigue siendo el mismo verificado en la primera entrega.
Este archivo cumple el schema nuevo en su estructura de metadatos y seguridad, pero su encabezado de secciones
(A-N según spec del prompt maestro) todavía usa la numeración original 1-10; la re-escritura completa a
encabezados A-N está en el próximo lote — el contenido y las reglas de seguridad ya son equivalentes.
