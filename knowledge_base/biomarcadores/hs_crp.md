---
doc_id: SLD-BIO-070
biomarker_id: hs_crp
name_es: Proteína C Reactiva ultrasensible (hs-CRP)
abbreviation: hs-CRP
sinonimos:
- PCR ultrasensible
- PCR-us
- hs-CRP
- Proteína C reactiva de alta sensibilidad
- PCR de alta sensibilidad
- Proteína C Reactiva ultrasensible (hs-CRP)
category: Inflamación / Cardiovascular (transversal)
subcategory: Marcador de fase aguda
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-CA-A02
- COND-M3-HE-002
- COND-M3-HE-003
- COND-M3-HE-006
- COND-M3-HE-A01
- COND-M6-MI-001
- COND-M6-MI-A02
- COND-M6-RE-A02
- REL-030
- REL-031
combine_with:
- ldl_c
- hdl_c
- triglycerides
- ferritin
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Mayor de 2 mg/L: modificador cardiovascular a confirmar (COND-M1-CA-A02). Mayor de 5 mg/L: cambia el corte de ferritina (M3). Mayor de 10 mg/L: proceso agudo, repetir.'
---

# Proteína C Reactiva ultrasensible (hs-CRP)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Mayor de 2 mg/L: modificador cardiovascular a confirmar (COND-M1-CA-A02). Mayor de 5 mg/L: cambia el corte de ferritina (M3). Mayor de 10 mg/L: proceso agudo, repetir.
- Reglas que usan esta ficha: COND-M1-CA-A02, COND-M3-HE-002, COND-M3-HE-003, COND-M3-HE-006, COND-M3-HE-A01, COND-M6-MI-001, COND-M6-MI-A02, COND-M6-RE-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-070. hs-CRP. Categoría: Inflamación / Cardiovascular (transversal). Tipo: measured_analyte. Tier 1.

## B. Definición

Proteína de fase aguda producida por el hígado en respuesta a interleucina-6. El ensayo de alta sensibilidad detecta concentraciones bajas relevantes para riesgo cardiovascular residual, no solo inflamación aguda evidente.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero/plasma) · hs-CRP (ensayo distinto del PCR estándar de baja sensibilidad)
- Método: inmunonefelometría o inmunoturbidimetría de alta sensibilidad
- ¿Ayuno? No requiere ayuno estricto.
- Factor preanalítico crítico: cualquier proceso inflamatorio/infeccioso reciente (incluso menor) lo eleva de forma transitoria y no cardiovascular.

### 2. Resultado y tipo de dato

- Unidad: mg/L · numérico continuo · **Medido**
- Valores >10 mg/L sugieren proceso agudo — repetir fuera de ese episodio antes de usar para riesgo cardiovascular.

## D. Intervalos y umbrales

```
clinical_decision_threshold: >10 mg/L sugiere proceso agudo, repetir
lab_reference_interval: depende del laboratorio/método
```

## E. Interpretación

**"PCR elevada = marcador inespecífico que puede aparecer en múltiples procesos inflamatorios y debe interpretarse con contexto"** — no "PCR elevada = infección".
- Factores que aumentan: infección, inflamación crónica, obesidad, tabaquismo, enfermedad autoinmune, trauma reciente.
- Factores que disminuyen: estatinas, pérdida de peso, ejercicio regular.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: síntomas de infección/inflamación reciente, antecedentes autoinmunes, tabaquismo.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con: perfil lipídico completo, historia de infección/inflamación reciente.
- NO puede diagnosticar por sí sola ninguna condición específica.
- Alerta: >10 mg/L (repetir en 2-3 semanas fuera del episodio agudo).

## I. Prevención

- Refinamiento de riesgo cardiovascular cuando el perfil lipídico es límite.
- Prohibido: "tiene una infección" o "tiene enfermedad cardiovascular" a partir de este valor solo.

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

- **Nivel:** Moderada-fuerte para el uso cardiovascular específico; fuerte para su carácter inespecífico como marcador inflamatorio general.
- **Clinical decision threshold (CDC/AHA Workshop on Markers of Inflammation and Cardiovascular Disease, 2003, verificado esta sesión):** categorías de riesgo cardiovascular por hs-CRP — **bajo riesgo <1.0 mg/L · riesgo promedio 1.0-3.0 mg/L · alto riesgo >3.0 mg/L**. Valores >10 mg/L sugieren proceso inflamatorio/infeccioso agudo y deben repetirse cuando la persona esté sana, antes de usarse para estratificación de riesgo cardiovascular.
- **URL fuente:** https://www.ahajournals.org/doi/10.1161/01.cir.0000148980.87579.5e — verificado esta sesión (ago-2026). Nota de vigencia: el 2013 ACC/AHA Guideline on Blood Cholesterol y la National Lipid Association posteriormente reafirmaron hs-CRP como "risk-enhancing factor" opcional cuando la decisión de riesgo es incierta tras la evaluación cuantitativa estándar — no cambia los puntos de corte de 2003, los mantiene vigentes como referencia.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "marcador inflamatorio inespecífico elevado, considerar contexto clínico antes de asociarlo a riesgo cardiovascular".
- **Inferencia PROHIBIDA:** "PCR elevada = infección".
- **Confianza por defecto:** baja-media sin contexto adicional.
- **Activa evaluación profesional:** valores muy elevados persistentes sin causa aguda identificable.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - inflamación___cardiovascular_(transversal)
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["ldl_c", "hdl_c", "triglycerides", "ferritin"]

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
