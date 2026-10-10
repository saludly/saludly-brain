---
doc_id: SLD-BIO-063
biomarker_id: cystatin_c
name_es: Cistatina C
name_en: Cystatin C
abbreviation: CysC
sinonimos:
- Cistatina C
- CysC
- Cystatin C
category: renal
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/L
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M2-NE-A02
combine_with:
- creatinine
- egfr
- bun
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Refleja con TFG de 45 a 59 sin albuminuria o con masa muscular extrema (COND-M2-NE-A02).
---

# Cistatina C

## Notas de decisión de Saludly (6 de octubre de 2026)

- Refleja con TFG de 45 a 59 sin albuminuria o con masa muscular extrema (COND-M2-NE-A02).
- Reglas que usan esta ficha: COND-M2-NE-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-063. CysC. Categoría: Riñón. Tipo: analito medido (variable de entrada del parámetro calculado eGFRcr-cys). Tier 3 — indicación específica, no cribado universal.

## B. Definición

Proteína producida por todas las células nucleadas a una tasa relativamente constante, filtrada libremente por el glomérulo. A diferencia de la creatinina, **no depende de la masa muscular** — esto la hace especialmente útil quen la creatinina es poco confiable (atletas, sarcopenia, obesidad severa, amputaciones).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método: inmunoturbidimetría o inmunonefelometría. Unidad: mg/L. No requiere ayuno. Factor preanalítico/de confusión importante: **corticoides, tabaquismo, inflamación y disfunción tiroidea pueden elevar la cistatina C independientemente de la función renal real** — es su principal limitación frente a creatinina.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (KDIGO 2024, verificado esta sesión):** en adultos con eGFR por creatinina **45-59 mL/min/1.73m² sin otros marcadores de daño renal**, KDIGO sugiere medir cistatina C para **confirmar** el diagnóstico de ERC — si el eGFR combinado (creatinina+cistatina) resulta <60 mL/min/1.73m², se confirma ERC; si resulta >60, el diagnóstico de ERC **no se confirma**. Este es un uso confirmatorio específico, no de cribado inicial.
- **Población donde KDIGO 2024 recomienda su uso preferente:** obesidad clase III (IMC >40 kg/m², o >35 en algunas regiones) — la ecuación combinada creatinina-cistatina ha demostrado ser la más precisa en esta población.
- **URL fuentes:** https://www.ccjm.org/content/92/9/546 ; http://www.nephjc.com/news/kdigo-ckd-part1 — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** puede reflejar reducción real de la función renal, o elevación por corticoides/inflamación/tabaquismo/disfunción tiroidea sin relación con función renal — requiere contexto para diferenciar.
- La ecuación combinada creatinina-cistatina (eGFRcr-cys) es más precisa que cualquiera de las dos por separado, especialmente en el rango eGFR 45-59 mL/min/1.73m² (zona de mayor incertidumbre diagnóstica según evidencia revisada esta sesión).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: uso de corticoides, tabaquismo, función tiroidea, IMC, masa muscular/nivel de actividad física, inflamación activa.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Creatinina/eGFR (obligatorio — la cistatina C casi nunca se interpreta sola, sino para calcular eGFRcr-cys), BUN.
- `pattern_examples`: eGFR por creatinina 45-59 + eGFRcr-cys <60 = confirma ERC; eGFR por creatinina 45-59 + eGFRcr-cys >60 = no confirma ERC (posible sobreestimación de daño por baja masa muscular).
- `cannot_conclude`: causa de la reducción de función renal sin evaluación adicional.

## H. Tendencias

### Tendencias temporales

Al no depender de masa muscular, sus cambios reflejan más fielmente cambios reales de función renal en el tiempo que la creatinina sola, especialmente en personas con composición corporal cambiante (pérdida de peso, sarcopenia progresiva por edad).

## I. Prevención

Su valor preventivo es principalmente confirmatorio/diagnóstico en la zona gris de eGFR (45-59), no un marcador de cribado poblacional independiente.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Se usa junto a creatinina para el cálculo de eGFRcr-cys — no es una prueba de seguimiento aislada en la mayoría de los casos.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Herramienta confirmatoria de ERC en una zona diagnóstica específica (eGFR 45-59 sin otros marcadores de daño) — no es cribado poblacional general.

## L. Evidencia

### Evidencia científica

- **Guideline (fuerte):** KDIGO 2024 Clinical Practice Guideline for CKD — recomendación específica de uso de cistatina C confirmatoria. https://www.ccjm.org/content/92/9/546 (resumen clínico de la guía KDIGO 2024, Cleveland Clinic Journal of Medicine) ; http://www.nephjc.com/news/kdigo-ckd-part1 (resumen NephJC de KDIGO 2024).
- Ambas verificadas por búsqueda web esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "cistatina C usada junto a creatinina para confirmar o descartar ERC en la zona diagnóstica de eGFR 45-59, o cuando la creatinina es poco confiable por masa muscular atípica".
- **prohibited_inferences:** diagnóstico de ERC con cistatina C aislada sin combinarla con creatinina en la ecuación correspondiente.
- **uncertainty_notes:** corticoides, tabaquismo, inflamación y disfunción tiroidea pueden elevarla independientemente de la función renal real — declarar esta limitación siempre que se interprete.
- **professional_review:** eGFRcr-cys <60 mL/min/1.73m² confirmado, o discordancia relevante entre eGFR por creatinina y eGFRcr-cys.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - renal
  - kidney_function
  - tier_3
  - saludly_brain_v1

use_when:
  - "eGFR por creatinina en zona 45-59 mL/min/1.73m² sin otros marcadores de daño renal"
  - "masa muscular atípica hace la creatinina poco confiable"
  - "obesidad clase III"

combine_with: [creatinine, egfr, bun]

do_not_use_alone:
  - "diagnóstico de ERC sin combinar con creatinina en la ecuación eGFRcr-cys"

do_not_conclude:
  - "función renal alterada sin descartar corticoides/inflamación/tabaquismo como causa de elevación"

escalate_when:
  - "eGFRcr-cys <60 mL/min/1.73m² confirmado"
  - "discordancia relevante entre eGFR por creatinina y eGFRcr-cys"
```
