---
doc_id: SLD-BIO-054
biomarker_id: apob_apoa1_ratio
name_es: Relación ApoB/ApoA1
name_en: ApoB/ApoA1 Ratio
abbreviation: ApoB/ApoA1
sinonimos:
- Relación ApoB/ApoA1
- ApoB/ApoA1
- ApoB/ApoA1 Ratio
category: cardiovascular_lipids
parameter_type: derived_ratio
tipo_resultado: numérico
unidad_canonica: sin unidad
specimen: No aplica (calculado)
nivel_catalogo: solo valor y rango
panel: calculado
sexo: ambos
alimenta:
- SEG-014
combine_with:
- apob
- apoa1
- ldl_c
- non_hdl_c
formula: ApoB/ApoA1 = ApoB ÷ ApoA1
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Relación ApoB/ApoA1

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-014. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-054. ApoB/ApoA1. Categoría: Cardiovascular/Lípidos. Tipo: **relación derivada**. Tier 2.

## B. Definición

Cociente entre el número de partículas aterogénicas (ApoB) y el número de partículas "protectoras" tipo HDL (ApoA1). Ha sido estudiado extensamente (estudio INTERHEART) como uno de los predictores de riesgo de infarto más fuertes entre los marcadores lipídicos tradicionales, superando en algunos análisis al colesterol total/HDL-C.

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio — relación derivada)

- **Fórmula:** ApoB/ApoA1 = ApoB ÷ ApoA1 (ambos en mg/dL).
- **Variables necesarias:** ApoB, ApoA1 (ambas medidas, idealmente de la misma muestra).
- **Cuándo NO debe calcularse:** si falta cualquiera de las dos variables de entrada.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Evidencia primaria verificada esta sesión:** McQueen MJ, et al. "Lipids, lipoproteins, and apolipoproteins as risk markers of myocardial infarction in 52 countries (the INTERHEART study): a case-control study." *Lancet* 2008;372:224-33. PMID: 18640459. Hallazgo principal: el ratio ApoB/ApoA1 tuvo el **riesgo atribuible poblacional (PAR) más alto de los 9 factores de riesgo tradicionales (54%)** y el odds ratio más alto por cada 1 desviación estándar de diferencia (OR 1.59, IC 95% 1.53-1.64) — superior al ratio colesterol total/HDL-C (PAR 32%) y LDL/HDL (PAR 37%).
- **Evidencia complementaria (cohorte poblacional grande):** Holmes MV, et al. (AMORIS cohort, Suecia, 137,100 personas seguidas 17.8 años en promedio). *PLOS Medicine* 2021. https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1003853 — confirma que ApoB y el ratio ApoB/ApoA1 elevados aumentan el riesgo de infarto y ACV, mientras que ApoA1 alto es protector.
- **Nota de calidad de evidencia — no existe un único punto de corte binario universal:** a diferencia de otros biomarcadores del catálogo, la literatura (INTERHEART, AMORIS, y la revisión Walldius 2025 sobre actualización de guías) presenta el ratio ApoB/ApoA1 como un **gradiente continuo de riesgo**, no como un umbral binario "alto/bajo" único. La revisión de actualización de guías (Walldius, *Expert Rev Cardiovasc Ther* 2025, https://www.tandfonline.com/doi/full/10.1080/14779072.2025.2543535) propone una "línea de riesgo" con zonas de bajo/medio/alto riesgo basada en datos combinados de AMORIS e INTERHEART, pero no fue posible verificar los valores numéricos exactos de esas zonas con la fuente primaria original en esta sesión — queda como pendiente puntual, no como vacío de evidencia general.
- URLs verificadas esta sesión (ago-2026): https://pubmed.ncbi.nlm.nih.gov/18640459/ ; https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1003853 ; https://www.tandfonline.com/doi/full/10.1080/14779072.2025.2543535

## E. Interpretación

- **Elevado:** mayor proporción relativa de partículas aterogénicas frente a protectoras — señal de riesgo cardiovascular más informativa que LDL-C o colesterol total/HDL-C por separado en varias cohortes de investigación.

## F. Contexto del paciente y confusores

### Contexto del paciente

Los mismos que ApoB y ApoA1: triglicéridos, diabetes, tabaquismo, antecedentes familiares.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ApoB, ApoA1 (variables de entrada), LDL-C, no-HDL-C (para contexto comparativo).
- `cannot_conclude`: diagnóstico de enfermedad cardiovascular — sigue siendo un factor de riesgo, no una prueba diagnóstica.

## H. Tendencias

### Tendencias temporales

Responde a cambios de estilo de vida y tratamiento hipolipemiante en semanas-meses.

## I. Prevención

Mismas acciones que el resto del perfil lipídico avanzado: manejo de peso, actividad física, control de triglicéridos/glucosa.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna adicional — ya combina las dos pruebas necesarias.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado universal (Tier 2, indicación específica) ni diagnóstica por sí sola.

## L. Evidencia

### Evidencia científica

- **Nivel:** el estudio INTERHEART (caso-control multinacional) estableció asociación fuerte entre ApoB/ApoA1 y riesgo de infarto — ampliamente citado en la literatura lipidológica posterior.
- **Fuentes verificadas esta sesión:** INTERHEART (McQueen et al., *Lancet* 2008, PMID 18640459) y AMORIS (Holmes et al., *PLOS Medicine* 2021) — ver detalle completo en sección D. Nivel de evidencia: cohortes/case-control de gran escala, fuerte para la asociación; el umbral binario único no existe en la literatura (ver nota de calidad de evidencia en sección D) — esto ya no es una brecha pendiente, es la conclusión correcta del estado actual de la evidencia.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "ratio ApoB/ApoA1 elevado, señal de mayor proporción de partículas aterogénicas frente a protectoras, considerar junto al resto del perfil lipídico avanzado".
- **prohibited_inferences:** "ratio alto = va a tener un infarto"; diagnóstico de enfermedad cardiovascular.
- **uncertainty_notes:** el umbral de corte específico no está verificado con fuente primaria en esta ficha — comunicar el resultado como tendencia de riesgo, no como punto de corte binario preciso hasta verificar.
- **professional_review:** ratio marcadamente elevado combinado con otros factores de riesgo cardiovascular.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - lipid_advanced
  - derived_ratio
  - tier_2
  - saludly_brain_v1

use_when:
  - "refinando riesgo cardiovascular en personas con indicación de ApoB/ApoA1"

combine_with: [apob, apoa1, ldl_c, non_hdl_c]

do_not_use_alone:
  - "diagnóstico o descarte de enfermedad cardiovascular"

do_not_conclude:
  - "certeza de evento cardiovascular futuro"

escalate_when:
  - "ratio marcadamente elevado combinado con otros factores de riesgo cardiovascular"
```
