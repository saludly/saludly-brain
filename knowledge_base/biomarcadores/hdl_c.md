---
doc_id: SLD-BIO-042
biomarker_id: hdl_c
name_es: Colesterol HDL (HDL-C)
abbreviation: HDL-C
sinonimos:
- Colesterol HDL
- HDL
- HDL-C
- Colesterol HDL (HDL-C)
category: Cardiovascular / Lípidos
subcategory: Perfil lipídico
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-CA-001
- COND-M1-CA-005
- COND-M1-EM-003
combine_with:
- total_cholesterol
- ldl_c
- triglycerides
- apoa1
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Colesterol HDL (HDL-C)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M1-CA-001, COND-M1-CA-005, COND-M1-EM-003. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-042. HDL-C. Categoría: Cardiovascular / Lípidos. Tipo: measured_analyte. Tier 1.

## B. Definición

Colesterol transportado en partículas de alta densidad, involucradas en el transporte reverso de colesterol desde tejidos periféricos hacia el hígado. Niveles bajos se asocian a mayor riesgo cardiovascular independiente del LDL-C.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero/plasma) · Perfil lipídico
- Método: enzimático homogéneo directo (métodos modernos no requieren precipitación de otras lipoproteínas)
- ¿Ayuno? Igual consideración que el resto del perfil lipídico — depende del protocolo del laboratorio.

### 2. Resultado y tipo de dato

- Unidad: mg/dL (alt: mmol/L) · numérico continuo · **Medido**

## D. Intervalos y umbrales

```
clinical_decision_threshold: HDL-C bajo generalmente <40 mg/dL en hombres, <50 mg/dL en mujeres (validar contra guía específica del laboratorio/sociedad antes de mostrarlo como umbral fijo en producto)
```

## E. Interpretación

- **Bajo:** asociado a mayor riesgo cardiovascular independientemente de LDL-C.
- **Muy alto (>90-100 mg/dL):** en general no es protector adicional y en casos raros puede reflejar disfunción de partícula HDL — no se recomienda interpretar como "mejor cuanto más alto" sin límite.
- Factores que disminuyen: tabaquismo, sedentarismo, obesidad abdominal, dietas muy altas en carbohidratos refinados, ciertos fármacos.
- Factores que aumentan: actividad física aeróbica regular, alcohol moderado (no se recomienda como intervención), pérdida de peso.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: tabaquismo, actividad física, IMC.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con Colesterol total, LDL-C, Triglicéridos.
- Es uno de los dos componentes (junto a colesterol total) que USPSTF identificó con evidencia sólida para cribado poblacional.
- NO puede por sí solo confirmar o descartar riesgo cardiovascular.

## I. Prevención

- Recomendaciones permitidas: actividad física aeróbica, manejo de peso, cesación de tabaquismo.
- Prohibido: recomendar consumo de alcohol como estrategia para elevar HDL-C (el balance de riesgo/beneficio del alcohol es negativo en términos generales de salud).

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

- **Nivel:** Fuerte.
- **Fuente:** USPSTF — evidencia de que HDL-C junto a colesterol total mejora la identificación de riesgo cardiovascular; personas con HDL-C bajo sin colesterol total alto también se benefician de manejo de riesgo.
- **URL:** https://www.aafp.org/pubs/afp/issues/2002/0115/p273.html
- **Verificado:** sí, esta sesión.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "HDL-C bajo es un factor de riesgo independiente, considerar junto al resto del perfil".
- **Inferencia PROHIBIDA:** recomendar alcohol para elevar HDL-C.
- **Confianza por defecto:** media — más útil combinado que aislado.
- **Activa evaluación profesional:** HDL-C muy bajo combinado con LDL-C alto y/o triglicéridos altos (perfil aterogénico).

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

combine_with: ["total_cholesterol", "ldl_c", "triglycerides", "apoa1"]

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
