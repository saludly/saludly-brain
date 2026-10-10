---
doc_id: SLD-BIO-053
biomarker_id: apoa1
name_es: Apolipoproteína A1
name_en: Apolipoprotein A1
abbreviation: ApoA1
sinonimos:
- Apolipoproteína A1
- ApoA1
- Apo A1
- Apolipoprotein A1
category: cardiovascular_lipids
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-014
combine_with:
- apob
- apob_apoa1_ratio
- hdl_c
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Apolipoproteína A1 (ApoA1)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-014. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-053. ApoA1. Categoría: Cardiovascular/Lípidos. Tipo: analito medido. Tier 3 — solo tiene valor agregado real cuando se combina con ApoB para el ratio; no se ofrece de forma aislada.

## B. Definición

Principal proteína estructural de las partículas HDL. Es al HDL lo que ApoB es a LDL/VLDL — un marcador del número de partículas "protectoras" (aunque el paradigma de HDL como estrictamente protector se ha matizado en la literatura reciente).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método: inmunoturbidimetría o inmunonefelometría estandarizada. Unidad: mg/dL. No requiere ayuno estricto.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Nota (respuesta completa, no vacío de evidencia):** no existe un umbral clínico independiente de ApoA1 validado en la literatura — por diseño, ApoA1 se usa exclusivamente como componente del ratio ApoB/ApoA1 (ver evidencia INTERHEART en sección L), nunca con un punto de corte propio. Esta ausencia de umbral aislado es la conclusión correcta, no una brecha de investigación pendiente de resolver.

## E. Interpretación

- Su interpretación aislada tiene bajo valor clínico — el sistema debe evitar generar conclusiones sobre ApoA1 solo, y presentarlo siempre en el contexto del ratio ApoB/ApoA1.

## F. Contexto del paciente y confusores

### Contexto del paciente

Los mismos que HDL-C: actividad física, tabaquismo, IMC.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ApoB (obligatorio, para el ratio), HDL-C.
- `cannot_conclude`: nada relevante sin ApoB concurrente.

## H. Tendencias

### Tendencias temporales

Relativamente estable salvo cambios significativos de estilo de vida o peso.

## I. Prevención

Su valor preventivo real está en habilitar el ratio ApoB/ApoA1, no en sí misma.

## J. Pruebas complementarias

### Pruebas complementarias posibles

ApoB (si no se solicitó junto — deben pedirse siempre en conjunto).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado independiente — Tier 3, solo con indicación de cálculo de ratio.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento lipidológico estándar sobre la estructura de HDL.
- **Fuente primaria verificada esta sesión:** McQueen MJ, et al. INTERHEART study, *Lancet* 2008;372:224-33. PMID: 18640459 — https://pubmed.ncbi.nlm.nih.gov/18640459/. ApoA1 mostró una reducción de riesgo del 33% por cada 1 DE de diferencia (comparado con 15% para HDL-C), confirmando que ApoA1 es un mejor predictor que HDL-C solo. **Nivel de evidencia:** case-control multinacional de gran escala (52 países), fuerte.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** ninguna de forma aislada — solo en combinación con ApoB para el ratio.
- **prohibited_inferences:** cualquier conclusión de riesgo cardiovascular a partir de ApoA1 sola.
- **uncertainty_notes:** valor clínico limitado sin ApoB concurrente.
- **professional_review:** solo relevante en el contexto del ratio ApoB/ApoA1 marcadamente alterado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - lipid_advanced
  - tier_3
  - saludly_brain_v1

use_when:
  - "calculando la relación ApoB/ApoA1"

combine_with: [apob, apob_apoa1_ratio, hdl_c]

do_not_use_alone:
  - "cualquier interpretación sin ApoB concurrente"

do_not_conclude:
  - "riesgo cardiovascular a partir de ApoA1 aislada"

escalate_when:
  - "ratio ApoB/ApoA1 marcadamente alterado"
```
