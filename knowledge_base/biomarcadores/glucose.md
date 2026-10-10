---
doc_id: SLD-BIO-020
biomarker_id: glucose
name_es: Glucosa en ayunas
abbreviation: GLU
sinonimos:
- Glucosa
- Glicemia
- Glucemia
- Glucosa basal
- Glucosa en ayunas
- GLU
category: Metabolismo y Electrolitos
subcategory: Homeostasis glucémica
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-EM-001
- COND-M1-EM-002
- COND-M1-EM-003
- COND-M1-EM-005
- COND-M6-MI-A02
combine_with:
- hba1c
- insulin
- triglycerides
- hdl_c
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Prediabetes y diabetes (COND-M1-EM-001, EM-002); glucosa < 70 y < 54 con revisión de la muestra (EM-005).
---

# Glucosa en ayunas (GLU)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Prediabetes y diabetes (COND-M1-EM-001, EM-002); glucosa < 70 y < 54 con revisión de la muestra (EM-005).
- Reglas que usan esta ficha: COND-M1-EM-001, COND-M1-EM-002, COND-M1-EM-003, COND-M1-EM-005, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-020. GLU. Categoría: Metabolismo y Electrolitos. Tipo: measured_analyte. Tier 1.

## B. Definición

Concentración de glucosa circulante en plasma/suero. Mide el sustrato energético primario y refleja el balance instantáneo entre ingesta, producción hepática y captación tisular mediada por insulina. Es el analito fundacional del panel metabólico de Saludly.

## C. Espécimen y toma

### Espécimen y laboratorio

- Tipo de muestra: sangre venosa (plasma o suero)
- Examen: Glucosa en ayunas (FPG)
- Método: enzimático hexoquinasa o glucosa oxidasa
- Tubo: fluoruro de sodio/oxalato de potasio preferido sobre tubo seco
- Volumen / estabilidad: depende del laboratorio/método (validar con laboratorio aliado)
- ¿Ayuno? **Sí, ≥8 horas**
- Factores preanalíticos: hemólisis y demora en separación de plasma alteran el resultado (glucólisis in vitro); evitar ejercicio intenso previo.

### 2. Resultado y tipo de dato

- Unidad: mg/dL (alt: mmol/L) · numérico continuo · **Medido** (no calculado)
- Limitaciones: alta precisión analítica; el principal riesgo de error es preanalítico.

## D. Intervalos y umbrales

```
lab_reference_interval: depende del laboratorio/método — validar con aliado
clinical_decision_threshold: ADA — diabetes ≥126 mg/dL, prediabetes 100-125 mg/dL
screening_threshold: mismo umbral ADA, aplicado en cribado anual con factores de riesgo
```

## E. Interpretación

- **Elevado:** resistencia a la insulina, diabetes, estrés agudo, corticoides.
- **Disminuido:** ayuno prolongado, insulinoma, insuficiencia suprarrenal, exceso de hipoglucemiantes.
- Variabilidad biológica intraindividual moderada (~5-7% día a día). Variabilidad preanalítica alta sin tubo inhibidor de glucólisis.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: `estado_ayuno` (horas), `medicamentos` (corticoides, hipoglucemiantes), `embarazo`.
Opcionales: `actividad_física`, `estrés_autoreportado`, `infección_reciente_14d`.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Sistemas relacionados: endocrino, hepático, pancreático.
- Combinar obligatoriamente con: HbA1c, Insulina (HOMA-IR), perfil lipídico.
- **NO puede diagnosticar por sí solo diabetes** — requiere confirmación con segunda prueba alterada o síntomas clásicos (criterio ADA).
- Alerta: ≥126 mg/dL o <70 mg/dL. Repetir si: 100-125 mg/dL (limítrofe) o discordante con HbA1c.

## I. Prevención

- Cribado anual en adultos con factores de riesgo.
- Alerta longitudinal: aumento >10-15 mg/dL entre mediciones sin causa aguda evidente.
- Permitido recomendar: actividad física, manejo de peso, seguimiento de HbA1c.
- Prohibido: inicio/ajuste de medicación (siempre médico).

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

- **Nivel:** Fuerte (guía de sociedad médica de primer nivel).
- **Fuente:** American Diabetes Association — Standards of Care in Diabetes 2026, "Diagnosis and Classification of Diabetes".
- **URL:** https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes
- **Verificado:** sí (búsqueda web, esta sesión, ago-2026).
- Criterios: FPG ≥126 mg/dL = diabetes; 100-125 mg/dL = prediabetes (IFG).

## M. Seguridad para Saludly Brain

- **Input requerido:** estado de ayuno confirmado, medicamentos, HbA1c si existe.
- **Combinar con:** HbA1c, insulina, perfil lipídico, presión arterial.
- **Inferencia permitida:** "patrón compatible con riesgo metabólico elevado, sugiere seguimiento".
- **Inferencia PROHIBIDA:** "tiene diabetes" a partir de un solo valor sin confirmación.
- **Confianza por defecto:** media (requiere segunda prueba para alta confianza diagnóstica).
- **Activa evaluación profesional:** FPG ≥126 mg/dL confirmado, o <70 mg/dL con síntomas, o discordancia persistente con HbA1c.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolismo_y_electrolitos
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["hba1c", "insulin", "triglycerides", "hdl_c"]

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
