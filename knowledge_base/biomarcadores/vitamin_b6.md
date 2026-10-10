---
doc_id: SLD-BIO-084
biomarker_id: vitamin_b6
name_es: Vitamina B6 (PLP)
name_en: Vitamin B6 (Pyridoxal 5-Phosphate)
abbreviation: B6 / PLP
sinonimos:
- Vitamina B6
- Piridoxal 5-fosfato
- PLP
- Vitamina B6 (PLP)
- Vitamina B6 (Piridoxal-5-Fosfato)
- B6 / PLP
- Vitamin B6 (Pyridoxal 5-Phosphate)
category: Vitaminas
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µg/L
specimen: Suero
nivel_catalogo: vitamina
panel: estándar
sexo: ambos
alimenta:
- COND-M3-NU-A04
combine_with:
- vitamin_b12
- folate
- homocysteine
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Regla de vitaminas (COND-M3-NU-A04).
---

# Vitamina B6 (Piridoxal-5-Fosfato, PLP)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Regla de vitaminas (COND-M3-NU-A04).
- Reglas que usan esta ficha: COND-M3-NU-A04. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-084. B6/PLP. Categoría: Vitaminas. Tipo: measured_analyte. Tier 3.

## B. Definición

El piridoxal-5-fosfato (PLP) es la forma biológicamente activa de la vitamina B6, cofactor de más de 140 reacciones enzimáticas distintas (representa ~4% de toda la actividad catalítica enzimática conocida). Junto con B12 y folato, es necesaria para el metabolismo de homocisteína.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (plasma) · Método: HPLC-MS/MS (cromatografía líquida con espectrometría de masas en tándem) — método de alta precisión. **Proteger la muestra de la luz** (enviar en vial ámbar) — el PLP se degrada con exposición lumínica.

### Condiciones de toma de muestra — CRÍTICO (evidencia verificada esta sesión, Mayo Clinic Laboratories)

- **Ayuno: 12 horas, requerido.**
- **Suspender multivitamínicos o suplementos vitamínicos 24 horas antes de la toma** — la muestra no en ayuno o con suplementación reciente refleja ingesta reciente, no el estado nutricional real.
- **Protección de la luz** durante el transporte de la muestra.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con patrón diagnóstico específico (evidencia verificada esta sesión, Mayo Clinic Laboratories)

- **Laboratory reference interval (adultos en ayunas):** **PLP 5-50 µg/L** (5-50 mcg/L) indica nutrición adecuada. Ácido piridóxico (PA, metabolito): 3-30 µg/L.
- **Patrón de suplementación reciente:** PLP 51-100 µg/L junto con PA >30 µg/L, o PLP >100 µg/L junto con PA >100 µg/L, sugiere que la elevación se debe a suplementación dietética reciente, no a un estado patológico.
- **Patrón de hipofosfatasia (hallazgo incidental relevante):** PLP marcadamente elevado **junto con PA bajo o normal** (patrón discordante) sugiere hipofosfatasia — trastorno genético raro por mutaciones en el gen ALPL (fosfatasa alcalina) — un hallazgo inesperado que vale la pena que Saludly Brain reconozca si aparece.
- **URLs fuente:** https://www.mayocliniclabs.com/test-catalog/overview/42359 ; https://www.mayocliniclabs.com/test-catalog/overview/42361 ; https://www.mayocliniclabs.com/test-catalog/overview/42360 — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Bajo:** deficiencia dietética, alcoholismo, ciertos medicamentos (isoniazida, algunos anticonceptivos), embarazo (mayor demanda). Síntomas de deficiencia: descamación cutánea, gingivitis severa, irritabilidad, debilidad, depresión, mareo, **neuropatía periférica**, convulsiones (en casos severos, especialmente en niños).
- **Muy alto:** paradójicamente, niveles excesivamente altos de vitamina B6 (generalmente por suplementación excesiva) también pueden causar **neuropatías sensitivas y motoras tóxicas** — este es uno de los pocos micronutrientes donde tanto la deficiencia como el exceso causan el mismo tipo de daño neurológico (neuropatía), por mecanismos distintos.
- **Patrón discordante (PLP alto + PA bajo/normal):** considerar hipofosfatasia, no solo suplementación.

## F. Contexto del paciente y confusores

### Contexto del paciente

Ayuno confirmado, suspensión de suplementos 24h antes, dieta, consumo de alcohol, medicamentos (isoniazida), embarazo, síntomas neurológicos (parestesias, debilidad) o cutáneos.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Vitamina B12, Folato (las tres vitaminas del metabolismo de homocisteína), Homocisteína.
- `pattern_examples`: B6 baja + homocisteína elevada + B12/folato normales = deficiencia de B6 como causa aislada de hiperhomocisteinemia.
- `cannot_conclude`: hipofosfatasia sin confirmar el patrón PLP/PA y, si corresponde, estudio genético (ALPL) — es un hallazgo incidental raro, no una conclusión de primera línea.

## H. Tendencias

### Tendencias temporales

Sensible a suplementación reciente — no interpretar cambios sin considerar si hubo suspensión de suplementos previa a la toma.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — relevante en estudio de homocisteína elevada o neuropatía sin causa clara.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Vitamina B12, Folato, Homocisteína (siempre en conjunto para el estudio del metabolismo de metionina).

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin confirmar ayuno y suspensión de suplementos. Escalar ante neuropatía periférica con B6 muy baja o muy alta (ambos extremos causan neuropatía, por mecanismos distintos), o patrón discordante PLP/PA sugestivo de hipofosfatasia.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories, con referencia a NHANES 2003-2004 para datos poblacionales).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "B6 alterada (alta o baja), considerar junto a B12/folato/homocisteína; neuropatía periférica puede deberse tanto a deficiencia como a exceso de B6".
- **prohibited_inferences:** diagnóstico de hipofosfatasia sin confirmar el patrón PLP/PA discordante y estudio adicional; recomendar suplementación sin confirmar deficiencia real (el exceso también es tóxico).
- **uncertainty_notes:** muy sensible a ayuno y suplementación reciente — un valor sin estas condiciones controladas puede ser engañoso.
- **professional_review:** neuropatía periférica con B6 en cualquier extremo, o patrón discordante PLP/PA sugestivo de hipofosfatasia.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitamins
  - neurological_risk
  - homocysteine_metabolism
  - tier_3
  - saludly_brain_v1
use_when:
  - "homocisteína elevada en estudio junto a B12/folato"
  - "neuropatía periférica sin causa clara"
combine_with: [vitamin_b12, folate, homocysteine]
do_not_use_alone:
  - "diagnóstico sin considerar B12/folato/homocisteína"
do_not_conclude:
  - "hipofosfatasia sin patrón PLP/PA confirmado y estudio adicional"
escalate_when:
  - "neuropatía periférica con B6 en cualquier extremo (alta o baja)"
  - "patrón discordante PLP/PA sugestivo de hipofosfatasia"
```
