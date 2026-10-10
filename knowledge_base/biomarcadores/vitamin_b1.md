---
doc_id: SLD-BIO-022
biomarker_id: vitamin_b1
name_es: Vitamina B1 (Tiamina)
name_en: Vitamin B1 (Thiamine)
abbreviation: B1 / TDP
sinonimos:
- Vitamina B1
- Tiamina
- Vitamina B1 (Tiamina)
- B1 / TDP
- Vitamin B1 (Thiamine)
category: Vitaminas
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: nmol/L
specimen: Suero
nivel_catalogo: vitamina
panel: estándar
sexo: ambos
alimenta:
- COND-M3-NU-A04
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: true
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Regla de vitaminas; tiamina baja con síntomas neurológicos y factor de riesgo: escalamiento 3 (COND-M3-NU-A04).'
---

# Vitamina B1 (Tiamina)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Regla de vitaminas; tiamina baja con síntomas neurológicos y factor de riesgo: escalamiento 3 (COND-M3-NU-A04).
- Reglas que usan esta ficha: COND-M3-NU-A04. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-022. B1/TDP. Categoría: Vitaminas. Tipo: measured_analyte. Tier 3 — relevante en contexto de consumo de alcohol, cirugía bariátrica o malnutrición, no cribado general.

## B. Definición

Vitamina esencial para el metabolismo de carbohidratos, función cerebral y mielinización de nervios periféricos. Las reservas corporales son limitadas (~30 mg en total en un adulto promedio) — la deficiencia puede desarrollarse rápidamente si la ingesta se interrumpe.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

**Sangre completa** (no suero ni plasma) — el 90% de la vitamina B1 en sangre completa está en forma de TDP (tiamina difosfato, forma biológicamente activa) y el 80% se localiza en los eritrocitos. Método: HPLC-MS/MS. **Proteger de la luz** durante transporte (vial ámbar).

### Condiciones de toma de muestra — CRÍTICO (evidencia verificada esta sesión, Mayo Clinic Laboratories)

- **Ayuno: 12 horas, requerido.**
- **Suspender suplementos vitamínicos 12 horas antes de la toma.**
- **No se afecta por hemólisis, lipemia o ictericia** (ventaja frente a otros analitos del catálogo) — pero no debe enviarse en vial de vidrio.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Laboratory reference interval:** concentración total de tiamina en sangre completa **75-195 nmol/L** (22.4-67.5 ng/mL aproximadamente), de la cual ~80% corresponde a TDP en eritrocitos (70-180 nmol/L).
- **Nota importante de calidad de evidencia (verificado esta sesión, Medscape):** **no existe un umbral de TDP universalmente aceptado para diagnosticar deficiencia de tiamina** — a diferencia de la mayoría de biomarcadores de este catálogo, el diagnóstico de deficiencia de tiamina se apoya fuertemente en la clínica (síntomas neurológicos, contexto de riesgo) más que en un punto de corte numérico único.
- **URLs fuente:** https://emedicine.medscape.com/article/2088582-overview ; https://www.mayocliniclabs.com/test-catalog/overview/42356 — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Baja:** alcoholismo (causa más frecuente en países occidentales), cirugía bariátrica, malnutrición (causa más frecuente a nivel mundial), estados hipermetabólicos (infecciones sistémicas, cánceres agresivos gastrointestinales/hematopoyéticos, diabetes, abstinencia alcohólica, convulsiones — todos aumentan el consumo de tiamina).
- **Síntomas de deficiencia leve-moderada:** inespecíficos — mal sueño, malestar, pérdida de peso, irritabilidad, confusión.
- **Síntomas de deficiencia severa (urgencia médica):** insuficiencia cardíaca congestiva ("beriberi húmedo"), neuropatía periférica ("beriberi seco"), **encefalopatía de Wernicke** (emergencia médica que puede progresar a coma y muerte) y **síndrome de Korsakoff** (pérdida de memoria y demencia frecuentemente irreversible).
- **Alta:** rara, generalmente por consumo excesivo de suplementos.

## F. Contexto del paciente y confusores

### Contexto del paciente

Consumo de alcohol (crítico), cirugía bariátrica previa, estado nutricional, síntomas neurológicos (cambios de comportamiento, alteraciones oculares, alteraciones de la marcha, delirium — estos son señales de alarma que Mayo Clinic identifica específicamente como indicación de la prueba), uso de insulina en paciente con hiperglucemia y nutrición cuestionable (contexto de riesgo específico documentado).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ninguno de forma obligatoria en el catálogo actual — su interpretación es predominantemente clínica.
- `cannot_conclude`: diagnóstico definitivo de deficiencia solo con el valor numérico, dado que no existe umbral universal — la clínica pesa más que el número en este biomarcador específico.

## H. Tendencias

### Tendencias temporales

Las reservas corporales limitadas permiten que la deficiencia se desarrolle rápidamente (días-semanas) tras interrupción de la ingesta — relevante en contextos agudos (post-cirugía, hospitalización, vómito prolongado).

## I. Prevención

### Contexto preventivo

Relevante en personas con consumo de alcohol significativo o cirugía bariátrica — considerar suplementación preventiva es una decisión médica/nutricional, no algo que Saludly deba recomendar de forma automática.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna prueba de laboratorio complementaria estándar en este catálogo — el diagnóstico de deficiencia severa es clínico y urgente.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No usar como cribado general. **Escalar de inmediato** ante síntomas neurológicos agudos (confusión, alteraciones oculares, alteraciones de la marcha) en persona con factor de riesgo (alcoholismo, cirugía bariátrica, malnutrición) — sospecha de encefalopatía de Wernicke es una **urgencia médica que no debe esperar interpretación de laboratorio**, el tratamiento empírico con tiamina se inicia antes de confirmar el diagnóstico bioquímico.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories, Medscape/eMedicine con referencias a Tietz Fundamentals of Clinical Chemistry).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "tiamina baja, considerar contexto de riesgo (alcohol, cirugía bariátrica, malnutrición); la clínica pesa más que el número exacto para este biomarcador".
- **prohibited_inferences:** esperar confirmación de laboratorio antes de sugerir evaluación urgente si hay síntomas neurológicos agudos con factor de riesgo — el tratamiento empírico no espera al laboratorio en sospecha de Wernicke.
- **uncertainty_notes:** no existe un umbral numérico único aceptado universalmente para diagnosticar deficiencia — es uno de los pocos biomarcadores del catálogo donde esto se declara explícitamente como la conclusión correcta, no como brecha de evidencia.
- **professional_review:** **SIEMPRE ante síntomas neurológicos agudos (confusión, alteraciones oculares/marcha) en persona con factor de riesgo — urgencia médica, sospecha de encefalopatía de Wernicke.**

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitamins
  - neurological_risk
  - alcohol_related
  - tier_3
  - saludly_brain_v1
use_when:
  - "consumo de alcohol significativo, cirugía bariátrica, o malnutrición"
  - "síntomas neurológicos agudos: confusión, alteraciones oculares/marcha"
combine_with: []
do_not_use_alone:
  - "diagnóstico de deficiencia solo con el valor numérico sin clínica"
do_not_conclude:
  - "ausencia de deficiencia solo por un valor no marcadamente bajo"
escalate_when:
  - "SIEMPRE ante síntomas neurológicos agudos con factor de riesgo — urgencia médica (sospecha de encefalopatía de Wernicke)"
```
