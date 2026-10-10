---
doc_id: SLD-BIO-023
biomarker_id: fructosamine
name_es: Fructosamina
name_en: Fructosamine
abbreviation: FRUC
sinonimos:
- Fructosamina
- FRUC
- Fructosamine
category: Metabolismo
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µmol/L
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-010
combine_with:
- hba1c
- glucose
- albumin
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Fructosamina

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-010. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-023. FRUC. Categoría: Metabolismo. Tipo: measured_analyte. Tier 3 — solo cuando HbA1c no es confiable.

## B. Definición

Mide la glucosilación de proteínas séricas, predominantemente albúmina (la proteína más abundante en plasma). A diferencia de HbA1c (que refleja ~2-3 meses, limitada por la vida media del eritrocito), fructosamina refleja el control glucémico de las **últimas 2-3 semanas** (vida media de la albúmina) — útil precisamente cuando una condición altera el recambio eritrocitario y hace a HbA1c no confiable.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: ensayo colorimétrico (nitroblue tetrazolium).

### Condiciones de toma de muestra

No requiere ayuno. **Factor preanalítico crítico:** niveles altos de ácido ascórbico (vitamina C) interfieren con el ensayo — se recomienda suspender suplementos de vitamina C al menos 24h antes de la toma.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con dependencia crítica de albúmina (evidencia verificada esta sesión)

- **Laboratory reference interval:** **200-285 µmol/L** cuando la albúmina sérica es 5 g/dL (valor de referencia). Otra fuente reporta **175-265 µmol/L** en no diabéticos con albúmina normal.
- **Limitación crítica:** el valor se vuelve **poco confiable cuando la albúmina es <3.0 g/dL** (hepatopatía, síndrome nefrótico) — una albúmina reducida disminuye artificialmente el valor de fructosamina, sin reflejar mejor control glucémico real.
- **Correlación aproximada con HbA1c (estudio verificado esta sesión):** los puntos de corte de fructosamina correspondientes a HbA1c 5.7% (prediabetes) y 6.5% (diabetes) fueron aproximadamente **241 µmol/L** y **270 µmol/L** respectivamente, según percentiles poblacionales — esta correlación es aproximada, no exacta.
- **URLs fuente:** https://emedicine.medscape.com/article/2089070-overview ; estudio de correlación HbA1c-fructosamina (NCT06057805) — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** control glucémico deficiente en las últimas 2-3 semanas.
- **Interpretación requiere conocer la albúmina concurrente** — sin ese dato, el valor de fructosamina puede malinterpretarse.

## F. Contexto del paciente y confusores

### Contexto del paciente

Albúmina sérica concurrente (obligatorio), hepatopatía o síndrome nefrótico conocidos, condición que motivó no usar HbA1c (hemoglobinopatía, embarazo, anemia hemolítica, ERC avanzada, transfusión reciente), uso reciente de suplementos de vitamina C.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Albúmina (obligatorio, para contextualizar la fiabilidad del valor), HbA1c (cuando esté disponible, aunque la razón de pedir fructosamina es precisamente que HbA1c no es confiable), Glucosa.
- `cannot_conclude`: control glucémico real si la albúmina está muy baja (<3.0 g/dL) — el valor no es interpretable en ese contexto.

## H. Tendencias

### Tendencias temporales

Refleja una ventana más corta (2-3 semanas) que HbA1c — útil para detectar cambios recientes en el control glucémico más rápidamente que HbA1c.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — es una alternativa específica cuando HbA1c no es confiable.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Albúmina (siempre en conjunto), Glucosa.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin conocer la albúmina concurrente. No usar como sustituto rutinario de HbA1c sin una razón específica documentada.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Medscape/eMedicine, con referencias a textos de referencia en medicina de laboratorio).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "fructosamina interpretada junto a albúmina; útil como alternativa a HbA1c en condiciones que alteran el recambio eritrocitario".
- **prohibited_inferences:** interpretar fructosamina sin considerar la albúmina concurrente; usarla como sustituto rutinario de HbA1c sin indicación específica.
- **uncertainty_notes:** la correlación con HbA1c es aproximada, no una conversión exacta.
- **professional_review:** valores muy alterados con albúmina normal, especialmente en el contexto de la condición que motivó su uso (embarazo, hemoglobinopatía, etc.).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - diabetes_monitoring
  - tier_3
  - saludly_brain_v1
use_when:
  - "HbA1c no confiable: hemoglobinopatía, anemia hemolítica, embarazo, transfusión reciente, ERC avanzada"
combine_with: [hba1c, glucose, albumin]
do_not_use_alone:
  - "interpretación sin albúmina concurrente"
do_not_conclude:
  - "control glucémico real con albúmina muy baja (<3.0 g/dL)"
escalate_when:
  - "valores muy alterados con albúmina normal en el contexto de la condición que motivó su uso"
```
