---
doc_id: SLD-BIO-080
biomarker_id: ferritin
name_es: Ferritina
abbreviation: FERR
sinonimos:
- Ferritina
- Ferritina sérica
- FERR
category: Vitaminas / Hierro / Micronutrientes
subcategory: Metabolismo del hierro
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-002
- COND-M3-HE-003
- COND-M3-HE-006
- COND-M3-HE-A01
combine_with:
- serum_iron
- transferrin
- transferrin_saturation
- hs_crp
- hemoglobin
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Corte adoptado: déficit con ferritina < 15 ng/mL, o < 70 si hs-CRP > 5 mg/L; la zona 15 a 29 es vigilar (COND-M3-HE-002, HE-003). Esta ficha cita < 30; manda la ficha de condición.'
---

# Ferritina

## Notas de decisión de Saludly (6 de octubre de 2026)

- Corte adoptado: déficit con ferritina < 15 ng/mL, o < 70 si hs-CRP > 5 mg/L; la zona 15 a 29 es vigilar (COND-M3-HE-002, HE-003). Esta ficha cita < 30; manda la ficha de condición.
- Reglas que usan esta ficha: COND-M3-HE-002, COND-M3-HE-003, COND-M3-HE-006, COND-M3-HE-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-080. FERR. Categoría: Vitaminas / Hierro / Micronutrientes. Tipo: measured_analyte. Tier 1.

## B. Definición

Proteína de almacenamiento de hierro; refleja de forma indirecta las reservas corporales de hierro, pero también se comporta como reactante de fase aguda positivo — lo que complica su interpretación aislada.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero) · Perfil de hierro
- Método: inmunoensayo (quimioluminiscencia)
- ¿Ayuno? No estricto, aunque suele solicitarse junto a hierro sérico que sí se beneficia de ayuno matutino.
- Factor preanalítico crítico: cualquier proceso inflamatorio/infeccioso agudo la eleva independientemente del estado real de hierro.

### 2. Resultado y tipo de dato

- Unidad: ng/mL (=µg/L) · numérico continuo · **Medido**

## D. Intervalos y umbrales

```
clinical_decision_threshold: <30 ng/mL en adultos sanos (evidencia moderna, más sensible que el umbral OMS clásico de <15 ng/mL); considerar hasta <50 ng/mL si hay inflamación concurrente (hs-CRP elevada)
```

## E. Interpretación

- **Elevada:** puede reflejar reservas altas, pero también inflamación/infección, hepatopatía, síndrome metabólico — requiere descartar estas causas antes de asumir sobrecarga de hierro.
- **Disminuida:** indicador sensible y específico de depleción de reservas de hierro.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: evidencia de proceso inflamatorio/infeccioso reciente, patrón de sangrado (menstrual, digestivo).

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con: hierro sérico, transferrina, saturación de transferrina, **hs-CRP** (descartar elevación por inflamación), hemograma completo.
- Patrón clásico de deficiencia: ferritina baja + hierro bajo + saturación de transferrina baja.
- Patrón de confusión inflamatoria: ferritina alta + hs-CRP alta = probable elevación inflamatoria, no sobrecarga real.
- NO puede diagnosticar por sí sola ni deficiencia ni sobrecarga de hierro sin el resto del perfil.

## I. Prevención

- Alta utilidad en cribado de deficiencia de hierro, especialmente en mujeres en edad fértil.
- Prohibido: recomendar suplementación de hierro sin confirmar deficiencia real (el exceso de hierro también tiene riesgos).

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

- **Nivel:** Fuerte para su rol como marcador de reservas de hierro y como reactante de fase aguda (ambos ampliamente documentados en hematología clínica).
- **Fuente institucional de referencia:** NIH/NIDDK — recursos sobre deficiencia de hierro y anemia.
- **Clinical decision threshold (evidencia verificada esta sesión, con disenso documentado entre umbrales):** el umbral OMS histórico de <15 ng/mL es ampliamente reconocido como **demasiado bajo** en la literatura reciente. Evidencia convergente propone <30 ng/mL como umbral más sensible para deficiencia de hierro en adultos sanos (Pasricha et al., *Lancet* 2021; ACOG usa este mismo umbral en embarazo, con ~92% de sensibilidad según revisión ASH 2023), y hasta <50 ng/mL cuando hay inflamación concurrente (ferritina como reactante de fase aguda eleva falsamente el valor). Guías de condiciones específicas usan umbrales aún más altos ajustados por contexto: KDIGO (enfermedad renal) y ECCO (enfermedad inflamatoria intestinal) usan <100 ng/mL combinado con saturación de transferrina <20% para indicar tratamiento; ESC (insuficiencia cardíaca) usa <100 ng/mL o 100-299 ng/mL con saturación <20%.
- **URLs fuente:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11817370/ (revisión de umbrales globales) ; https://www.ncbi.nlm.nih.gov/books/NBK542171/ (NIH StatPearls, resume KDIGO/ECCO/ESC) ; https://www.sciencedirect.com/science/article/pii/S000649712505356X (impacto clínico de rangos de laboratorio discordantes) — todas verificadas esta sesión (ago-2026).
- **Decisión de producto para Saludly:** dado el disenso activo en la literatura, Saludly debe presentar <30 ng/mL como umbral primario de alerta en adultos sanos (más sensible que el umbral OMS clásico de 15), y explicar que valores 30-50 ng/mL con síntomas o inflamación concurrente también ameritan considerar deficiencia funcional — no ocultar que el "rango normal" de muchos laboratorios (con frecuencia partiendo desde ~10-12 ng/mL) es más permisivo que la evidencia clínica reciente.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "patrón compatible con depleción de reservas de hierro" o "ferritina elevada posiblemente relacionada con proceso inflamatorio concurrente, requiere contexto".
- **Inferencia PROHIBIDA:** "ferritina alta = sobrecarga de hierro" sin descartar inflamación.
- **Confianza por defecto:** baja-media sin el resto del perfil de hierro y sin hs-CRP.
- **Activa evaluación profesional:** ferritina muy baja con síntomas de anemia, o muy alta sin causa inflamatoria evidente.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitaminas___hierro___micronutrientes
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["serum_iron", "transferrin", "transferrin_saturation", "hs_crp", "hemoglobin"]

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
