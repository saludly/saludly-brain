---
doc_id: SLD-BIO-005
biomarker_id: homa_ir
name_es: HOMA-IR
name_en: HOMA-IR (Homeostasis Model Assessment of Insulin Resistance)
abbreviation: HOMA-IR
sinonimos:
- HOMA-IR
- Índice HOMA
- HOMA-IR (Índice de Resistencia a la Insulina)
- HOMA-IR (Homeostasis Model Assessment of Insulin Resistance)
category: metabolism_electrolytes
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: sin unidad
specimen: No aplica (calculado)
nivel_catalogo: con patrón
panel: calculado
sexo: ambos
alimenta:
- COND-M1-EM-A02
- REL-028
combine_with:
- glucose
- insulin
- triglycerides
- hdl_c
formula: HOMA-IR = (Glucosa en ayunas [mg/dL] × Insulina en ayunas [µUI/mL]) / 405
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Sin corte universal; Saludly usa 2,5 solo como corte operativo provisional de apoyo y nunca lo muestra al paciente como umbral (COND-M1-EM-A02).
---

# HOMA-IR (Índice de Resistencia a la Insulina)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Sin corte universal; Saludly usa 2,5 solo como corte operativo provisional de apoyo y nunca lo muestra al paciente como umbral (COND-M1-EM-A02).
- Reglas que usan esta ficha: COND-M1-EM-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-005. HOMA-IR. Categoría: Metabolismo. Tipo: **parámetro calculado**. Tier 2. Nota de auditoría: nuevo, incorporado en la primera auditoría como parámetro calculado explícito.

## B. Definición

Índice matemático que estima la resistencia a la insulina a partir de glucosa e insulina en ayunas, sin necesidad del método de referencia (clamp euglucémico-hiperinsulinémico), que es invasivo y poco práctico fuera de investigación. Es una **aproximación**, no una medición directa de sensibilidad a la insulina.

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio para parámetro calculado)

- **Fórmula:** HOMA-IR = (Glucosa en ayunas [mg/dL] × Insulina en ayunas [µUI/mL]) / 405.
- **Variables necesarias:** Glucosa en ayunas, Insulina en ayunas — **ambas de la misma muestra, tomadas en el mismo momento, con ayuno confirmado de ≥8 horas**.
- **Versión de la fórmula:** la constante 405 corresponde a la versión más usada cuando la glucosa está en mg/dL; si el laboratorio reporta glucosa en mmol/L, la constante cambia a 22.5 — Saludly debe verificar la unidad antes de calcular.
- **Cuándo NO debe calcularse:** si glucosa e insulina no son de la misma muestra/momento, o si el paciente no confirma ayuno real de ≥8 horas.
- **Cuándo el cálculo puede ser inválido:** en personas ya en tratamiento con insulina exógena (el índice fue diseñado para insulina endógena) — en ese caso HOMA-IR no debe calcularse ni interpretarse.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión, con nota de disenso fuerte entre poblaciones)

**No existe un umbral universal de HOMA-IR validado internacionalmente** — esta es una limitación documentada extensamente en la literatura, verificada por múltiples fuentes esta sesión:
- Estudio checo (población europea de mediana edad, *Diagnostics* 2019): corte 1.82 para distinguir tolerancia normal de prediabetes; 3.63 para distinguir de diabetes tipo 2 establecida.
- Estudio español EPIRCE (población adulta general): corte 1.85 (hombres) usando criterios de síndrome metabólico, hasta 3.46 usando percentil 90 poblacional.
- Estudio de biobanco a gran escala: corte propuesto 1.878, señalando que reportes previos van desde >1.6 (Omán) hasta >3.04 (Corea) y >2.7 (Brasil).
- Estudio en adolescentes (validado contra clamp hiperglucémico, *Arch Endocrinol Metab* 2022): corte >2.91 (postpuberales) a >3.22 (puberales) — población pediátrica, **no aplicable a adultos**.
- **URLs fuente:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6571793/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4016563/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12104043/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9983787/ — todas verificadas esta sesión (ago-2026).
- **Conclusión de auditoría explícita:** el umbral de HOMA-IR depende de la población de referencia (país, edad, sexo, ensayo de insulina usado) en un grado inusualmente alto para un parámetro de este catálogo. Saludly Brain **no debe presentar un único número de corte como si fuera consenso universal** — debe comunicar el resultado numérico con contexto de que la interpretación depende de la población y el ensayo del laboratorio.

## E. Interpretación

- **Elevado:** compatible con resistencia a la insulina — mayor probabilidad cuanto más se aleje del rango bajo de los cortes reportados en la literatura (aprox. >1.8-2.0 ya empieza a ser señal en varias poblaciones).
- La magnitud del corte "correcto" depende de la población, por lo que Saludly debe tratar HOMA-IR como una **señal de tendencia**, no como un punto de corte binario preciso.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: ayuno confirmado (crítico — un ayuno incompleto invalida el cálculo), uso de insulina exógena (contraindica el cálculo), IMC/circunferencia abdominal, antecedente de síndrome de ovario poliquístico.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Glucosa, Insulina (variables de entrada), Triglicéridos y HDL-C (componentes del síndrome metabólico asociado).
- `pattern_examples`: HOMA-IR elevado + triglicéridos altos + HDL-C bajo + circunferencia abdominal aumentada = patrón compatible con síndrome metabólico con resistencia a la insulina como componente central.
- `cannot_conclude`: diagnóstico de diabetes o prediabetes — esos diagnósticos se basan en criterios de glucosa/HbA1c, no en HOMA-IR.

## H. Tendencias

### Tendencias temporales

Responde a intervenciones de estilo de vida (pérdida de peso, actividad física) en semanas-meses — útil para seguimiento de respuesta a intervención, más que como valor de corte diagnóstico único.

## I. Prevención

Acciones razonablemente relacionadas: manejo de peso, actividad física, reducción de carbohidratos refinados.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna adicional — HOMA-IR ya combina las dos pruebas necesarias (glucosa e insulina).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Herramienta de estimación de resistencia a la insulina para fines de estratificación de riesgo — no es diagnóstica de diabetes, prediabetes ni síndrome metabólico por sí sola (esos tienen criterios propios establecidos).

## L. Evidencia

### Evidencia científica

- **Estudios de cohorte/validación (evidencia observacional, calidad variable, con disenso documentado entre poblaciones):**
  - Kollárová et al., "Optimal HOMA-IR Cut-Offs: Cross-Sectional Study in the Czech Population." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6571793/
  - "Insulin resistance (HOMA-IR) cut-off values... EPIRCE cross-sectional study." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4016563/
  - "Evaluating indices of insulin resistance... large biobank cohort." https://pmc.ncbi.nlm.nih.gov/articles/PMC12104043/
  - "The threshold value for identifying insulin resistance (HOMA-IR) in an admixed adolescent population." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9983787/ (población pediátrica, no aplicable directamente a adultos)
- Todas verificadas por búsqueda web esta sesión (ago-2026). **Nivel de evidencia: cohort/observacional — no existe guideline de sociedad médica que establezca un único umbral universal**, y este documento lo declara explícitamente en vez de presentar un número inventado como consenso.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "HOMA-IR elevado sugiere posible resistencia a la insulina; la magnitud exacta del corte depende de la población de referencia — comunicar como tendencia, no como umbral binario preciso".
- **prohibited_inferences:** presentar un único número de corte como si fuera un consenso médico universal; diagnóstico de diabetes/prediabetes a partir de HOMA-IR.
- **uncertainty_notes:** este es uno de los parámetros del catálogo con mayor variabilidad de umbral reportada en la literatura — la incertidumbre debe comunicarse explícitamente al usuario, no ocultarse detrás de un número aparentemente preciso.
- **professional_review:** HOMA-IR elevado combinado con múltiples componentes de síndrome metabólico, o en contexto de síndrome de ovario poliquístico con sospecha de componente metabólico.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - insulin_resistance
  - calculated_parameter
  - tier_2
  - saludly_brain_v1

use_when:
  - "estimando resistencia a la insulina con glucosa e insulina en ayunas"
  - "evaluando componente metabólico de síndrome de ovario poliquístico"

combine_with: [glucose, insulin, triglycerides, hdl_c]

do_not_use_alone:
  - "diagnóstico de diabetes, prediabetes o síndrome metabólico"

do_not_conclude:
  - "diagnóstico definitivo de resistencia a la insulina con un umbral numérico único y universal"

escalate_when:
  - "HOMA-IR elevado combinado con múltiples componentes de síndrome metabólico"
```
