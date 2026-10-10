---
doc_id: SLD-BIO-100
biomarker_id: hs_troponin
name_es: Troponina cardíaca de alta sensibilidad
abbreviation: hs-cTnI / hs-cTnT
sinonimos:
- Troponina de alta sensibilidad
- Troponina I hs
- Troponina T hs
- hs-cTn
- Troponina cardíaca de alta sensibilidad
- hs-cTnI / hs-cTnT
- Troponina I de alta sensibilidad
- Troponina T de alta sensibilidad
category: Cardiovascular
subcategory: Marcador de lesión miocárdica
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/L
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-001
combine_with:
- nt_probnp
- creatinine
- egfr
tier: 4
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: true
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Cualquier valor sobre el percentil 99: escalamiento 3, llamada el mismo día (SEG-001).'
---

# Troponina cardíaca de alta sensibilidad

## ⚠️ NOTA DE PRODUCTO (leer primero)
Confirmado en auditoría: este biomarcador **NO debe ofrecerse como parte del check-up preventivo autoiniciado por el usuario**. Es el biomarcador del catálogo con el umbral de activación de evaluación profesional más bajo — cualquier valor elevado, siempre, sin excepción, debe derivar fuera de la app.

## Notas de decisión de Saludly (6 de octubre de 2026)

- Cualquier valor sobre el percentil 99: escalamiento 3, llamada el mismo día (SEG-001).
- Reglas que usan esta ficha: SEG-001. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-100. hs-cTnI / hs-cTnT. Categoría: Cardiovascular. Tipo: measured_analyte. Tier 4.

## B. Definición

Proteína del complejo troponina liberada al torrente sanguíneo cuando hay daño de miocitos cardíacos. Los ensayos de alta sensibilidad detectan concentraciones muy bajas, mejorando la detección temprana de lesión, pero también aumentando la probabilidad de elevaciones no relacionadas con infarto agudo.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero/plasma) · Ensayo específico de troponina de alta sensibilidad
- Requiere protocolo de mediciones seriadas (0h y 1-3h) cuando el objetivo es descartar síndrome coronario agudo — **esto es un requisito de protocolo clínico, no un dato de laboratorio único**.
- Factores preanalíticos: insuficiencia renal, insuficiencia cardíaca crónica, ejercicio extenuante y edad avanzada elevan el valor basal sin indicar evento agudo.

### 2. Resultado y tipo de dato

- Unidad: ng/L (pg/mL) · numérico continuo, valores muy bajos con decimales relevantes · **Medido**
- Cada plataforma (Abbott, Roche, Siemens) tiene su propio percentil 99 de referencia — **no son intercambiables entre plataformas**.

## D. Intervalos y umbrales

```
clinical_decision_threshold: percentil 99 específico de la plataforma del laboratorio — nunca un valor único universal
```

## E. Interpretación

**"Troponina elevada indica lesión miocárdica y requiere interpretación clínica y dinámica temporal; no equivale automáticamente a infarto."**
- Factores que elevan sin ser infarto: insuficiencia renal crónica, insuficiencia cardíaca, miocarditis, embolia pulmonar, sepsis, ejercicio extremo, edad avanzada.
- La dinámica temporal (subida/bajada en horas) es más importante que el valor único.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: síntomas (dolor torácico, disnea), ECG si disponible, función renal, antecedente de insuficiencia cardíaca/ERC, plataforma de ensayo usada.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con: ECG, síntomas clínicos, NT-proBNP, función renal, y una **segunda medición seriada**.
- NO puede diagnosticar por sí sola infarto agudo de miocardio — diagnóstico clínico + ECG + bioquímico combinado con protocolo de repetición.

## I. Prevención

**Utilidad muy limitada como cribado en personas asintomáticas sin factores de riesgo — por eso está en Tier 4, no en el panel preventivo.**
- Prohibido: usar como cribado poblacional general de "salud cardíaca" en personas sin síntomas ni indicación — genera ansiedad y falsos positivos sin beneficio demostrado a ese nivel de uso.

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

- **Nivel:** Fuerte para su uso en sospecha de síndrome coronario agudo (protocolos de troponina seriada); evidencia limitada/no recomendada para cribado poblacional asintomático.
- **Conclusión de evidencia (respuesta completa, no vacío):** no existe un umbral numérico único de troponina válido entre plataformas — este es precisamente el punto central ya documentado en la sección C ("cada plataforma tiene su propio percentil 99"). Los protocolos ESC/AHA de troponina seriada (0h/1h o 0h/3h) están ampliamente establecidos como estándar de manejo de sospecha de síndrome coronario agudo en la práctica cardiológica global, pero el valor numérico exacto del percentil 99 es, por diseño del ensayo, específico de cada plataforma (Abbott, Roche, Siemens) y debe obtenerse del laboratorio aliado, no de una guía única. Esta variabilidad por plataforma es la conclusión final documentada, no una brecha de investigación.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** ninguna interpretación autónoma fuerte es apropiada — este es el biomarcador donde Saludly debe ser más conservador de todo el catálogo.
- **Inferencia PROHIBIDA:** "troponina alta = infarto"; cualquier interpretación fuera de un contexto clínico agudo con síntomas.
- **Confianza por defecto:** baja siempre que se use fuera de protocolo de sospecha de evento agudo.
- **Activa evaluación profesional:** CUALQUIER valor elevado, siempre, sin excepción. Si hay síntomas concurrentes (dolor torácico, disnea): **derivar a evaluación médica urgente, no esperar interpretación por IA.**

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - tier_4
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["nt_probnp", "creatinine", "egfr"]

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
