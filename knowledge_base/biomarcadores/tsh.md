---
doc_id: SLD-BIO-060
biomarker_id: tsh
name_es: TSH (Hormona Estimulante de Tiroides)
abbreviation: TSH
sinonimos:
- TSH
- Hormona estimulante de tiroides
- Tirotropina
- TSH ultrasensible
- TSH (Hormona Estimulante de Tiroides)
category: Tiroides
subcategory: Eje hipotálamo-hipófisis-tiroides
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µUI/mL
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
- free_t4
- free_t3
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
- 'Umbral de decisión adoptado: consenso colombiano 2023, 5,0 mUI/L de 18 a 60 años y 6,0 después; 10 o más, escalamiento 2 (COND-M2-TI-001). La zona 4,5 a 10 de esta ficha se reemplaza por esa regla.'
---

# TSH (Hormona Estimulante de Tiroides)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Umbral de decisión adoptado: consenso colombiano 2023, 5,0 mUI/L de 18 a 60 años y 6,0 después; 10 o más, escalamiento 2 (COND-M2-TI-001). La zona 4,5 a 10 de esta ficha se reemplaza por esa regla.
- Reglas que usan esta ficha: COND-M2-TI-001, COND-M2-TI-002, COND-M2-TI-003, COND-M2-TI-004, COND-M2-TI-005, COND-M2-TI-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-060. TSH. Categoría: Tiroides. Tipo: measured_analyte. Tier 1.

## B. Definición

Hormona hipofisaria que regula la producción de hormonas tiroideas (T4/T3) mediante retroalimentación negativa. Marcador de primera línea para evaluar función tiroidea.

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (suero) · Perfil tiroideo
- Método: inmunoensayo de tercera generación (quimioluminiscencia)
- ¿Ayuno? No requiere estricto; preferible toma matutina por variación circadiana.
- Factores preanalíticos: variación circadiana (más alta en la mañana), embarazo, enfermedad no tiroidea aguda (sick euthyroid syndrome).

### 2. Resultado y tipo de dato

- Unidad: µUI/mL (=mUI/L) · numérico continuo · **Medido**
- Interferencia posible por anticuerpos heterófilos si el resultado es discordante con la clínica.

## D. Intervalos y umbrales

```
lab_reference_interval: depende del laboratorio/método — límite superior de referencia poblacional reportado 4.1-4.5 mIU/L (NHANES, Hanford Thyroid Disease Study, ver evidencia en sección L); ATA 2012 recomienda 4.12 mIU/L para ensayos de tercera generación en zonas con suficiencia de yodo
clinical_decision_threshold: >10 mIU/L justifica considerar tratamiento por sí solo (AACE/ATA); 4.5-10 mIU/L es zona de decisión dependiente de síntomas/Anti-TPO/embarazo
```

## E. Interpretación

- **Elevado:** sugiere hipotiroidismo (primario).
- **Disminuido:** sugiere hipertiroidismo, o supresión por otras causas.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: síntomas (fatiga, cambios de peso, palpitaciones), embarazo.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- **Combinar obligatoriamente con T4 libre** (para clasificar subclínico vs manifiesto) y Anti-TPO si hay sospecha autoinmune.
- TSH alto + T4 libre normal = hipotiroidismo subclínico. TSH alto + T4 libre bajo = hipotiroidismo manifiesto.
- NO puede diagnosticar por sí solo la causa (autoinmune vs otra) sin anticuerpos.

## I. Prevención

- Cribado en población con factores de riesgo (mujeres >35 años, antecedente familiar, síntomas inespecíficos).
- Prohibido: inicio/ajuste de levotiroxina u otro tratamiento tiroideo — exclusivamente médico.

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
- **Fuente institucional de referencia:** American Thyroid Association — guías de manejo de hipotiroidismo e hipertiroidismo.
- **Clinical decision threshold (verificado esta sesión, múltiples fuentes concordantes):** el límite superior de TSH normal recomendado por ATA 2012 para ensayos de tercera generación es de **~4.12 mIU/L en regiones con suficiencia de yodo**. NHANES (EE.UU., 17,353 personas sin enfermedad) reportó un límite superior de **4.5 mIU/L**; el Hanford Thyroid Disease Study (excluyendo anticuerpos positivos) reportó **4.1 mIU/L**. **AACE/ATA** identifican TSH >10 mIU/L como umbral que por sí solo justifica considerar tratamiento en hipotiroidismo subclínico (ver `anti_tpo.md`); entre 4.5-10 mIU/L (rango límite), la decisión depende de síntomas, Anti-TPO y contexto (embarazo).
- **URLs fuente:** https://e-enm.org/journal/view.php?number=2412 (revisión coreana 2023 que resume NHANES/Hanford/ATA) ; https://www.guidelinecentral.com/guideline/6855/ (AACE/ATA) ; https://www.aafp.org/pubs/afp/issues/2005/0501/p1763.html — todas verificadas esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **Inferencia permitida:** "patrón compatible con disfunción tiroidea de tipo X, requiere confirmación con T4 libre".
- **Inferencia PROHIBIDA:** diagnosticar hipotiroidismo/hipertiroidismo solo con TSH sin T4 libre.
- **Confianza por defecto:** media sin T4 libre concurrente; alta con ambos valores concordantes.
- **Activa evaluación profesional:** TSH marcadamente alto/bajo, sintomático, o discordancia TSH/T4.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - tiroides
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["free_t4", "free_t3", "anti_tpo"]

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
