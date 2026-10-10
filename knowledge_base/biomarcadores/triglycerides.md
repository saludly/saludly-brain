---
doc_id: SLD-BIO-043
biomarker_id: triglycerides
name_es: Triglicéridos
abbreviation: TG
sinonimos:
- Triglicéridos
- TG
- Triglicéridos séricos
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
- COND-M1-CA-003
- COND-M1-CA-A01
- COND-M1-EM-003
- COND-M2-NE-005
combine_with:
- hdl_c
- ldl_c
- glucose
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Desde 500 mg/dL, escalamiento 2; urgencia solo con síntomas o bandera crítica del laboratorio (COND-M1-CA-003). Esta ficha pide evaluación inmediata; manda la ficha de condición.
---

# Triglicéridos (TG)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Desde 500 mg/dL, escalamiento 2; urgencia solo con síntomas o bandera crítica del laboratorio (COND-M1-CA-003). Esta ficha pide evaluación inmediata; manda la ficha de condición.
- Reglas que usan esta ficha: COND-M1-CA-001, COND-M1-CA-003, COND-M1-CA-A01, COND-M1-EM-003, COND-M2-NE-005. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-043. TG. Categoría: Cardiovascular / Lípidos. Tipo: measured_analyte. Tier 1.

## B. Definición

Lípidos circulantes que representan la principal forma de almacenamiento energético; su elevación se asocia a resistencia a la insulina, síndrome metabólico y, en niveles muy altos, a riesgo de pancreatitis aguda.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero/plasma) · Perfil lipídico
- ¿Ayuno? **Sí recomendado (9-12h)** — a diferencia de LDL-C/HDL-C/CT, los triglicéridos son el componente del perfil lipídico más sensible a la ingesta reciente.
- Factor preanalítico crítico: comida reciente, alcohol reciente elevan considerablemente el valor.

### 2. Resultado y tipo de dato

- Unidad: mg/dL (alt: mmol/L) · numérico continuo · **Medido**
- Es además **variable de entrada obligatoria** para calcular LDL-C por Friedewald.

## D. Intervalos y umbrales

```
clinical_decision_threshold: >500 mg/dL activa riesgo de pancreatitis — requiere evaluación médica inmediata
lab_reference_interval: depende del laboratorio/método
```

## E. Interpretación

- **Elevado:** resistencia a la insulina, obesidad, consumo de alcohol, dieta alta en carbohidratos refinados, diabetes mal controlada, hipotiroidismo.
- **Muy elevado (>500 mg/dL):** riesgo de pancreatitis aguda — requiere manejo médico, no solo preventivo.
- Variabilidad preanalítica muy alta (ayuno, alcohol reciente).

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: `estado_ayuno`, `consumo_alcohol_reciente`.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con HDL-C y glucosa (componente del síndrome metabólico).
- Invalida el cálculo de LDL-C por Friedewald si >400 mg/dL.
- NO puede por sí solo diagnosticar síndrome metabólico (requiere criterios combinados: circunferencia abdominal, presión arterial, glucosa, HDL-C).

## I. Prevención

- Recomendaciones permitidas: reducción de carbohidratos refinados y alcohol, actividad física.
- Prohibido: iniciar fibratos/omega-3 de prescripción sin médico.

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

- **Nivel:** Moderado como marcador aislado de cribado; fuerte como componente del síndrome metabólico y como variable de cálculo de LDL-C.
- **Fuente:** USPSTF — "Screening for Lipid Disorders in Adults": *"la evidencia es insuficiente para recomendar a favor o en contra de la medición de triglicéridos como parte del cribado rutinario"* (recomendación histórica I), por evidencia conflictiva sobre triglicéridos como factor de riesgo independiente y falta de datos prospectivos.
- **URL:** https://www.aafp.org/pubs/afp/issues/2002/0115/p273.html — verificado esta sesión.
- **Decisión de producto explícita:** Saludly mantiene TG en Tier 1 no por evidencia de cribado poblacional independiente (que USPSTF calificó como insuficiente), sino porque es **indispensable operativamente** para calcular LDL-C (Friedewald) y para evaluar síndrome metabólico junto a HDL-C y glucosa. El sistema de IA debe comunicar esto con precisión: TG no es, por sí solo, un marcador de cribado con la misma fuerza de evidencia que colesterol total/HDL-C.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "elevado, compatible con patrón metabólico de riesgo; combinar con HDL-C y glucosa".
- **Inferencia PROHIBIDA:** "triglicéridos altos = enfermedad cardiovascular" de forma aislada (evidencia insuficiente como factor independiente según USPSTF).
- **Confianza por defecto:** media, condicionada a confirmar ayuno real.
- **Activa evaluación profesional:** >500 mg/dL (riesgo de pancreatitis) siempre, sin excepción.

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

combine_with: ["hdl_c", "ldl_c", "glucose"]

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
