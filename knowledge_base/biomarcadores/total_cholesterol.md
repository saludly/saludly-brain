---
doc_id: SLD-BIO-039
biomarker_id: total_cholesterol
name_es: Colesterol total
abbreviation: CT
sinonimos:
- Colesterol total
- CT
- Colesterol
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
- COND-M1-CA-005
combine_with:
- ldl_c
- hdl_c
- triglycerides
- non_hdl_c
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

# Colesterol total (CT)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M1-CA-005. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-039. CT. Categoría: Cardiovascular / Lípidos. Tipo: measured_analyte. Tier 1.

## B. Definición

Suma de todo el colesterol transportado en las distintas lipoproteínas circulantes (LDL, HDL, VLDL). Es la medida más antigua y menos específica del perfil lipídico, pero sigue siendo la base del cribado poblacional junto a HDL-C.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero/plasma) · Perfil lipídico
- Método: enzimático colorimétrico estandarizado
- ¿Ayuno? Ver nota en `ldl_c.md` — depende del protocolo del laboratorio aliado.

### 2. Resultado y tipo de dato

- Unidad: mg/dL (alt: mmol/L) · numérico continuo · **Medido**

## D. Intervalos y umbrales

```
screening_threshold (USPSTF, histórico): medición conjunta con HDL-C recomendada desde los 20 años
clinical_decision_threshold: siempre en conjunto con LDL-C/HDL-C/TG, no aislado
```

## E. Interpretación

- Refleja la carga lipídica total, sin distinguir la fracción aterogénica (LDL) de la protectora (HDL) — por eso nunca debe interpretarse solo.
- Factores que aumentan: dieta, hipotiroidismo, síndrome nefrótico, embarazo (fisiológico).
- Factores que disminuyen: hipertiroidismo, malabsorción, hepatopatía severa, estatinas.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: ninguna crítica aislada más allá del contexto general del perfil lipídico (edad, sexo, antecedentes familiares).

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con HDL-C (mínimo indispensable), idealmente perfil completo.
- NO permite por sí solo estratificar riesgo cardiovascular sin la fracción HDL/LDL.

## I. Prevención

- Componente central del cribado poblacional según USPSTF (medición conjunta con HDL-C).
- Recomendaciones permitidas: hábitos, seguimiento periódico.

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
- **Fuente:** USPSTF — "Screening for Lipid Disorders in Adults" (recomendación histórica B para medición conjunta de colesterol total + HDL-C).
- **URL:** https://www.aafp.org/pubs/afp/issues/2002/0115/p273.html
- **Verificado:** sí, esta sesión (ago-2026). Nota: la versión archivada de USPSTF referenciada aquí es la base metodológica histórica; se recomienda verificar en el próximo lote si existe una actualización 2023-2026 vigente antes de publicar en producción.

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "parte del perfil lipídico, requiere el resto de fracciones para interpretación de riesgo".
- **Inferencia PROHIBIDA:** cualquier juicio de riesgo cardiovascular basado solo en colesterol total.
- **Confianza por defecto:** baja de forma aislada; media-alta combinado con LDL-C/HDL-C/TG.
- **Activa evaluación profesional:** valores muy elevados (>300 mg/dL) o combinado con perfil aterogénico completo.

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

combine_with: ["ldl_c", "hdl_c", "triglycerides", "non_hdl_c"]

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
