---
doc_id: SLD-BIO-030
biomarker_id: uric_acid
name_es: Ácido úrico
name_en: Uric Acid
abbreviation: AU
sinonimos:
- Ácido úrico
- Uricemia
- AU
- Uric Acid
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M6-RE-001
combine_with:
- creatinine
- egfr
- glucose
- triglycerides
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

# Ácido úrico

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M6-RE-001. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-030. AU. Categoría: Metabolismo y Electrolitos. Tipo: analito medido. Tier 1. (Nota de auditoría: elimina el duplicado que existía en la lista original del usuario, donde aparecía tanto en "Metabolismo" como en "Riñón" — un solo registro, con relación cruzada a función renal.)

## B. Definición

Producto final del catabolismo de purinas. Se asocia tanto a riesgo de gota (depósito de cristales de urato) como, de forma más amplia, a síndrome metabólico y función renal.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma). Método enzimático (uricasa). Unidad: mg/dL (alt: µmol/L, mmol/L). No requiere ayuno estricto. Variables preanalíticas: dieta reciente alta en purinas (carnes rojas, mariscos, alcohol) puede elevarlo transitoriamente.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (tratamiento, no cribado):** ACR 2020 Guideline for the Management of Gout — el objetivo de tratamiento (treat-to-target) en pacientes ya diagnosticados con gota es reducir el urato sérico a **<6 mg/dL**.
- **Risk threshold (progresión de enfermedad):** ACR 2020 identifica **>9 mg/dL** como nivel de urato marcadamente elevado asociado a mayor probabilidad de progresión de gota (más flares, tofos).
- **Umbral de definición de hiperuricemia asintomática:** **>6.8 mg/dL** (límite de solubilidad del urato) — pero el ACR **recomienda condicionalmente EN CONTRA de iniciar tratamiento farmacológico** en personas con hiperuricemia asintomática sin gota previa ni tofos, incluso con comorbilidades como ERC, enfermedad cardiovascular o hipertensión.
- **URL fuente:** FitzGerald et al., "2020 American College of Rheumatology Guideline for the Management of Gout." *Arthritis Care & Research.* https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/acr.24180 — verificado esta sesión (ago-2026).

## E. Interpretación

**Elevado:**
- Causas frecuentes: dieta alta en purinas/alcohol, síndrome metabólico/resistencia a la insulina, insuficiencia renal (reducción de excreción), medicamentos (diuréticos tiazídicos).
- **Importante para Saludly:** un valor elevado sin gota clínica ni tofos (hiperuricemia asintomática) **NO justifica automáticamente tratamiento** según ACR 2020 — esta es una de las reglas de seguridad más claras y verificadas de todo el catálogo.

**Disminuido:** generalmente sin relevancia clínica mayor de forma aislada; en raros casos asociado a defectos tubulares renales o síndrome de secreción inadecuada.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: dieta reciente, consumo de alcohol, medicamentos (diuréticos), antecedente de gota/tofos, función renal.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Creatinina/eGFR (función renal), Glucosa/Triglicéridos (componente de síndrome metabólico).
- `pattern_examples`: ácido úrico elevado + eGFR bajo + triglicéridos elevados = patrón compatible con síndrome metabólico y riesgo renal combinado.
- `cannot_conclude`: diagnóstico de gota sin historia clínica de flares articulares o tofos — el diagnóstico de gota es clínico (y a veces por análisis de líquido articular), no bioquímico aislado.

## H. Tendencias

### Tendencias temporales

Tendencia ascendente sostenida es relevante como marcador de riesgo metabólico/renal progresivo, independientemente de si hay o no gota clínica.

## I. Prevención

Acciones razonablemente relacionadas: reducción de consumo de alcohol y de dieta alta en purinas, manejo de peso, hidratación adecuada, revisión de diuréticos tiazídicos con un profesional si aplica.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Función renal si no está disponible; perfil metabólico si hay sospecha de síndrome metabólico asociado.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Ácido úrico elevado es un factor de riesgo/marcador metabólico — NO es diagnóstico de gota. El diagnóstico de gota requiere historia clínica de artritis inflamatoria episódica (idealmente confirmada con análisis de líquido articular), no solo un valor de laboratorio.

## L. Evidencia

### Evidencia científica

- **Guideline (fuerte):** FitzGerald JD, et al. "2020 American College of Rheumatology Guideline for the Management of Gout." *Arthritis Care & Research.* 2020. DOI: 10.1002/acr.24180. https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/acr.24180
- **Complementaria:** Qaseem A, et al. "Management of Acute and Recurrent Gout: A Clinical Practice Guideline from the American College of Physicians." *Ann Intern Med.* 2017;166:58-68 (referenciada dentro de la guía ACR, no verificada de forma independiente esta sesión).
- Ambas verificadas por búsqueda web esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "ácido úrico elevado, factor de riesgo metabólico/renal a considerar; en ausencia de síntomas articulares o tofos, no indica tratamiento según guías actuales".
- **prohibited_inferences:** "tiene gota" a partir del valor de laboratorio aislado sin historia clínica de artritis; recomendar inicio de tratamiento farmacológico (esto es explícitamente responsabilidad médica, y la propia guía ACR recomienda en contra del tratamiento en hiperuricemia asintomática).
- **uncertainty_notes:** el umbral de "hiperuricemia asintomática" (>6.8 mg/dL) es un umbral bioquímico de solubilidad, no un criterio diagnóstico de enfermedad — la mayoría de personas con hiperuricemia asintomática nunca desarrollan gota clínica.
- **professional_review:** valores >9 mg/dL, historia de flares articulares agudos, tofos visibles, o combinación con ERC/enfermedad cardiovascular donde el manejo integral requiere evaluación médica.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - renal
  - gout_risk
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando panel metabólico básico"
  - "evaluando riesgo de síndrome metabólico"
  - "usuario pregunta sobre riesgo de gota"

combine_with: [creatinine, egfr, glucose, triglycerides]

do_not_use_alone:
  - "diagnóstico de gota"
  - "decisión de iniciar tratamiento farmacológico"

do_not_conclude:
  - "tiene gota a partir del valor de laboratorio aislado"
  - "requiere tratamiento con ácido úrico elevado asintomático"

escalate_when:
  - "valor >9 mg/dL"
  - "historia de artritis articular episódica o tofos"
  - "combinación con enfermedad renal o cardiovascular ya conocida"
```
