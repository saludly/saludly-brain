---
doc_id: SLD-BIO-001
biomarker_id: hemoglobin
name_es: Hemoglobina
abbreviation: Hb
sinonimos:
- Hemoglobina
- Hb
- HGB
category: Hematología
subcategory: Serie roja
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: g/dL
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-001
- COND-M3-HE-002
- COND-M3-HE-004
- COND-M5-MU-A01
combine_with:
- hematocrit
- mcv
- ferritin
- reticulocytes_abs
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Antes del corte OMS se resta el ajuste por altitud de residencia (1,8 g/dL en Bogotá) y por tabaquismo (COND-M3-HE-001).
---

# Hemoglobina (Hb)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Antes del corte OMS se resta el ajuste por altitud de residencia (1,8 g/dL en Bogotá) y por tabaquismo (COND-M3-HE-001).
- Reglas que usan esta ficha: COND-M3-HE-001, COND-M3-HE-002, COND-M3-HE-004, COND-M5-MU-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-001. Hb. Categoría: Hematología. Tipo: measured_analyte. Tier 1.

## B. Definición

Proteína transportadora de oxígeno en los eritrocitos. Es el parámetro central para el diagnóstico y clasificación de anemia y, en menor medida, de policitemia.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (o capilar en algunos contextos) · Hemograma completo (CBC)
- Método: analizador hematológico automatizado (espectrofotometría/citometría de flujo)
- Tubo: EDTA (tapa lila)
- ¿Ayuno? **No requiere**
- Factores preanalíticos: hemodilución (embarazo, sobrehidratación IV) o hemoconcentración (deshidratación) alteran el valor sin reflejar cambio real en masa eritrocitaria.

### 2. Resultado y tipo de dato

- Unidad: g/dL (alt: g/L) · numérico continuo · **Medido**

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

```
lab_reference_interval: depende del laboratorio, ajustado por sexo/edad/embarazo/altitud
clinical_decision_threshold (OMS 2024, primera actualización desde 1968):
  - Hombres adultos: <13.0 g/dL
  - Mujeres adultas no embarazadas: <12.0 g/dL
  - Embarazo (1er y 3er trimestre): <11.0 g/dL
  - Embarazo (2do trimestre, actualizado 2024): <10.5 g/dL
  - Niños 6-23 meses (actualizado 2024, antes 11.0): <10.5 g/dL
  - Niños 2-11 años: <11.0 g/dL · Niños 12-14 años: <12.0 g/dL
```
**Fuente:** WHO. "Guideline on Haemoglobin Cutoffs to Define Anaemia in Individuals and Populations." 2024, resumida vía NCBI StatPearls: https://www.ncbi.nlm.nih.gov/books/NBK499994/ — verificado esta sesión (ago-2026).
**Nota de calidad de evidencia:** Braat et al. (*Lancet Haematology* 2024, DOI: 10.1016/S2352-3026(24)00030-9) sugieren que el umbral en hombres podría ser más alto (13.5 g/dL) de lo que la OMS mantuvo (13.0 g/dL); la OMS reconoció esta incertidumbre y decidió conservar 13.0 g/dL. No ocultar esta discrepancia.
**Nota de altitud (relevante para Bogotá, ~2,640 msnm):** los umbrales OMS son a nivel del mar; a esta altitud los valores fisiológicamente esperables son más altos por adaptación — Saludly debe ajustar por altitud de residencia, no aplicar el umbral OMS sin corrección.

## E. Interpretación

- **Disminuida:** anemia — requiere clasificación posterior por VCM (micro/normo/macrocítica) y contexto (ferropenia, deficiencia de B12/folato, enfermedad crónica, pérdida sanguínea).
- **Elevada:** policitemia (vera o secundaria — hipoxia crónica, tabaquismo, altitud, deshidratación).
- Variabilidad fisiológica por altitud (relevante para Colombia/Bogotá — valores de referencia a nivel del mar no aplican igual a >2,600 msnm) y por sexo.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: sexo biológico, embarazo, edad, altitud de residencia (relevante en Colombia).
Opcionales: antecedente de sangrado (menstrual, digestivo), dieta.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con: Hematocrito, VCM, Ferritina (si hay sospecha de causa ferropénica), Reticulocitos absolutos (si ya hay anemia documentada).
- Sistemas relacionados: hematológico, y de forma secundaria renal (eritropoyetina) y nutricional.
- NO puede por sí sola establecer la causa de la anemia — solo confirma su presencia y severidad.
- Alerta: valores muy bajos (<8-9 g/dL según edad/sexo) o síntomas de anemia severa (disnea, taquicardia, palidez marcada).

## I. Prevención

- Cribado de rutina de alto valor, especialmente en mujeres en edad fértil y adultos mayores.
- Alerta longitudinal: descenso progresivo sostenido entre controles, incluso dentro de rango "normal".
- Recomendaciones permitidas: ajuste dietético, seguimiento.
- Prohibido: recomendar suplementación de hierro sin confirmar causa ferropénica (puede haber otras causas de anemia donde el hierro no ayuda o incluso perjudica).

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

- **Nivel:** Fuerte — guideline OMS 2024.
- **Fuente:** WHO. "Guideline on Haemoglobin Cutoffs to Define Anaemia in Individuals and Populations." 2024. https://www.ncbi.nlm.nih.gov/books/NBK499994/ ; evidencia complementaria: Braat S, et al. *Lancet Haematology* 2024. DOI: 10.1016/S2352-3026(24)00030-9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10983828/
- Ambas verificadas por búsqueda web esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **Input requerido:** sexo, embarazo, altitud de residencia, antecedente de sangrado.
- **Combinar con:** Hematocrito, VCM, Ferritina.
- **Inferencia permitida:** "valores compatibles con anemia de tipo [micro/normo/macrocítica], requiere estudio de causa".
- **Inferencia PROHIBIDA:** atribuir causa específica (ferropenia, B12, enfermedad crónica) sin el resto del panel (VCM, ferritina, B12/folato).
- **Confianza por defecto:** alta para detectar la anemia; baja para atribuir causa sin panel completo.
- **Activa evaluación profesional:** Hb muy baja, síntomas de anemia severa, o policitemia no explicada por altitud/tabaquismo/deshidratación evidente.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematología
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["hematocrit", "mcv", "ferritin", "reticulocytes_abs"]

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
