---
doc_id: SLD-BIO-055
biomarker_id: nt_probnp
name_es: NT-proBNP (Fracción N-terminal del propéptido natriurético tipo B)
name_en: N-terminal pro-B-type Natriuretic Peptide
abbreviation: NT-proBNP
sinonimos:
- NT-proBNP
- Péptido natriurético
- Pro-BNP
- NT-proBNP (Fracción N-terminal del propéptido natriurético tipo B)
- N-terminal pro-B-type Natriuretic Peptide
category: Cardiovascular
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M1-CA-007
- SEG-010
combine_with:
- hs_troponin
- creatinine
- egfr
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Solo se mide como refleja en personas con diabetes (COND-M1-CA-007); fuera de ese contexto, SEG-010.
---

# NT-proBNP

## Notas de decisión de Saludly (6 de octubre de 2026)

- Solo se mide como refleja en personas con diabetes (COND-M1-CA-007); fuera de ese contexto, SEG-010.
- Reglas que usan esta ficha: COND-M1-CA-007, SEG-010. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-055. NT-proBNP. Categoría: Cardiovascular. Tipo: measured_analyte. Tier 3 — indicado ante sospecha de insuficiencia cardíaca/disnea, no cribado asintomático general.

## B. Definición

Fragmento inactivo liberado en proporción equimolar al péptido natriurético BNP, secretado por los miocitos ventriculares en respuesta a estiramiento/sobrecarga de volumen o presión. Es más estable que BNP y no se afecta por inhibidores de neprilisina (relevante en pacientes bajo ese tratamiento), lo que lo hace la prueba preferida actualmente.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (plasma o suero) · Método: inmunoensayo.

### Condiciones de toma de muestra

No requiere ayuno. Factores que elevan independientemente de insuficiencia cardíaca: edad avanzada, fibrilación auricular (niveles hasta 3x más altos que en ritmo sinusal, incluso sin insuficiencia cardíaca), enfermedad renal, valvulopatía. Factores que lo suprimen: IMC elevado (obesidad), ciertos medicamentos.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con doble uso (rule-out ambulatorio vs rule-in urgencias) (evidencia verificada esta sesión, ESC/AHA)

- **Umbral de descarte ambulatorio (ESC/AHA, guías vigentes):** **<125 pg/mL descarta insuficiencia cardíaca crónica** en atención primaria con alta confianza (sensibilidad 94.6%, VPN 98.9% en estudio de validación de 155,347 personas).
- **Umbrales de confirmación ajustados por edad, ESC Heart Failure Association 2023 (consenso clínico, verificado esta sesión) — para servicios de urgencias:** **≥450 pg/mL en <50 años · ≥900 pg/mL en 50-75 años · ≥1,800 pg/mL en >75 años** sugieren fuertemente insuficiencia cardíaca aguda.
- **Umbrales de descarte ambulatorio ajustados por edad (más específicos, con menor sensibilidad):** ≥125 pg/mL (<50 años) · ≥250 pg/mL (50-75 años) · ≥500 pg/mL (>75 años) — mejoran la especificidad (77.6%, 67.8%, 63.5% respectivamente) a costa de sensibilidad más baja.
- **Umbral de alto riesgo:** ≥2,000 pg/mL (especificidad 96.1%).
- **URLs fuente:** https://onlinelibrary.wiley.com/doi/10.1002/ejhf.3036 (consenso ESC HFA 2023) ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12450762/ (estudio de validación, 155,347 personas) ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11424345/ (umbral específico >75 años) — todas verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevado:** insuficiencia cardíaca (con o sin síntomas), fibrilación auricular (independiente de insuficiencia cardíaca), enfermedad renal, edad avanzada, valvulopatía.
- **Bajo con alta sospecha clínica pese al valor bajo:** considerar IMC elevado como causa de supresión falsa del valor.

## F. Contexto del paciente y confusores

### Contexto del paciente

Edad (crítico para umbral), fibrilación auricular conocida, función renal, IMC, síntomas (disnea, edema, ortopnea, fatiga).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Troponina de alta sensibilidad (evaluación cardíaca conjunta), Creatinina/eGFR (la función renal afecta la eliminación de NT-proBNP, elevándolo independientemente de la función cardíaca).
- `pattern_examples`: NT-proBNP elevado + disnea + eGFR normal = insuficiencia cardíaca más probable; NT-proBNP elevado + eGFR muy reducido = considerar contribución renal a la elevación.
- `cannot_conclude`: diagnóstico definitivo de insuficiencia cardíaca sin evaluación clínica y ecocardiograma.

## H. Tendencias

### Tendencias temporales

Útil para seguimiento de respuesta a tratamiento en insuficiencia cardíaca ya diagnosticada — un descenso sostenido sugiere buena respuesta terapéutica.

## I. Prevención

### Contexto preventivo

No aplica como cribado poblacional asintomático general — indicado específicamente ante síntomas sugestivos.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ecocardiograma (confirmatorio, fuera del alcance de Saludly, requiere derivación), función renal si no está disponible.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar insuficiencia cardíaca sin evaluación clínica y ecocardiograma. Escalar ante valores por encima de los umbrales de confirmación ajustados por edad, especialmente con síntomas concurrentes (disnea, edema).

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte — guías ESC/AHA y estudios de validación diagnóstica a gran escala (155,347 y 12,077 pacientes en distintos estudios).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "NT-proBNP elevado, compatible con posible insuficiencia cardíaca, considerar edad, función renal y fibrilación auricular como factores que también lo elevan; requiere evaluación clínica y ecocardiograma para confirmar".
- **prohibited_inferences:** diagnóstico definitivo de insuficiencia cardíaca sin ecocardiograma.
- **uncertainty_notes:** fibrilación auricular puede triplicar el valor independientemente de insuficiencia cardíaca; obesidad puede suprimirlo falsamente.
- **professional_review:** valores por encima del umbral ajustado por edad, especialmente con síntomas (disnea, edema, fatiga).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - heart_failure
  - tier_3
  - saludly_brain_v1
use_when:
  - "sospecha de insuficiencia cardíaca (disnea, edema, fatiga)"
  - "seguimiento de insuficiencia cardíaca ya diagnosticada"
combine_with: [hs_troponin, creatinine, egfr]
do_not_use_alone:
  - "diagnóstico definitivo de insuficiencia cardíaca sin ecocardiograma"
do_not_conclude:
  - "insuficiencia cardíaca confirmada sin evaluación clínica completa"
escalate_when:
  - "valores por encima del umbral ajustado por edad, con síntomas concurrentes"
```
