---
doc_id: SLD-BIO-071
biomarker_id: folate
name_es: Folato Sérico
name_en: Serum Folate
abbreviation: Folato / B9
sinonimos:
- Ácido fólico
- Folato
- Folato sérico
- Folato Sérico
- Folato (Ácido Fólico / Vitamina B9)
- Folato / B9
- Serum Folate
category: Vitaminas
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: vitamina con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-004
- COND-M3-NU-002
combine_with:
- vitamin_b12
- homocysteine
- mcv
- hemoglobin
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Cortes adoptados: < 4 ng/mL posible déficit, < 3 déficit (COND-M3-NU-002).'
---

# Folato (Vitamina B9)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Cortes adoptados: < 4 ng/mL posible déficit, < 3 déficit (COND-M3-NU-002).
- Reglas que usan esta ficha: COND-M3-HE-004, COND-M3-NU-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-071. Folato/B9. Categoría: Vitaminas. Tipo: measured_analyte. Tier 2.

## B. Definición

Vitamina esencial para la síntesis de ADN, junto con B12. Su deficiencia causa anemia macrocítica indistinguible morfológicamente de la deficiencia de B12 — se interpretan siempre juntas.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero o plasma heparinizado — **NO usar plasma EDTA**) · Método: inmunoensayo (quimioluminiscencia). También existe la medición de folato eritrocitario (RBC folate), que refleja mejor las reservas tisulares que el folato sérico.

### Condiciones de toma de muestra — CRÍTICO

- **Ayuno: requerido, 8 horas** (verificado esta sesión).
- **Evitar inyección de vitamina B12 antes de la prueba** (puede interferir).
- **Limitación central:** el folato sérico está **fuertemente influenciado por la ingesta reciente** y es un índice poco confiable de las reservas tisulares reales — una sola comida rica en folato puede normalizar el valor sérico temporalmente. El folato eritrocitario (RBC) es más representativo de reservas a largo plazo cuando está disponible.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Rango clásico:** 2-20 ng/mL (adultos).
- **Rango actualizado post-fortificación obligatoria de cereales con ácido fólico en EE.UU. (verificado esta sesión):** **5.8-32.8 ng/mL (13.1-74.3 nmol/L)** para folato sérico; **153-515 ng/mL (347-1167 nmol/L)** para folato eritrocitario — esto ilustra la importancia de rangos específicos por región/país (Colombia no tiene fortificación obligatoria idéntica a EE.UU., Saludly debe validar con el laboratorio aliado).
- **Umbral de deficiencia bioquímica:** <3 ng/mL (<6.7 nmol/L) para folato sérico; <140 ng/mL (<322 nmol/L) para folato eritrocitario.
- **URL fuente:** https://emedicine.medscape.com/article/2085523-overview — verificado esta sesión (ago-2026).

## E. Interpretación

- **Diferencial clave con B12 (verificado esta sesión):** en deficiencia de folato, la **homocisteína está elevada pero el ácido metilmalónico (MMA) es normal**; en deficiencia de B12, **tanto homocisteína como MMA están elevados**. Esta distinción bioquímica permite diferenciar ambas deficiencias cuando el cuadro es dudoso (MMA no está actualmente en el catálogo de Saludly — candidato para futuro lote).
- **Baja:** dieta deficiente, malabsorción, alcoholismo, embarazo (mayor demanda), medicamentos (metotrexato, algunos anticonvulsivantes).

## F. Contexto del paciente y confusores

### Contexto del paciente

Dieta reciente (crítico, dado que el valor sérico es sensible a ingesta reciente), embarazo/planificación de embarazo, consumo de alcohol, medicamentos, malabsorción.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Vitamina B12 (obligatorio — deficiencias combinadas o diferenciales), Homocisteína, VCM/Hemoglobina (anemia macrocítica).
- `pattern_examples`: folato bajo + homocisteína alta + MMA normal = deficiencia de folato; folato normal + B12 baja + homocisteína y MMA ambos altos = deficiencia de B12, no de folato.
- `cannot_conclude`: reservas tisulares reales con folato sérico aislado — considerar folato eritrocitario si está disponible y hay discordancia clínica.

## H. Tendencias

### Tendencias temporales

Muy sensible a cambios agudos de dieta — no es un buen marcador de tendencia longitudinal salvo que se use folato eritrocitario.

## I. Prevención

### Contexto preventivo

Especialmente relevante en mujeres en edad fértil/embarazo (prevención de defectos del tubo neural) y en personas con dieta restrictiva o malabsorción.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Vitamina B12, Homocisteína; folato eritrocitario si hay discordancia entre el valor sérico y la clínica.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No concluir sobre reservas reales con un solo valor sérico sin considerar ingesta reciente. Escalar ante anemia macrocítica confirmada con folato bajo, o planificación de embarazo con deficiencia.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Medscape/eMedicine, revisión clínica con referencias a valores de fortificación poblacional).
- Fuente verificada esta sesión: ver URL en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "folato bajo, considerar junto a B12 y homocisteína para diferenciar causa de anemia macrocítica o hiperhomocisteinemia".
- **prohibited_inferences:** concluir sobre reservas tisulares reales con un solo valor sérico sin considerar la ingesta reciente.
- **uncertainty_notes:** el folato sérico es altamente sensible a la ingesta reciente — una comida rica en folato puede normalizarlo temporalmente sin reflejar reservas reales.
- **professional_review:** anemia macrocítica confirmada con folato bajo, o deficiencia en embarazo/planificación de embarazo.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitamins
  - anemia_workup
  - pregnancy_relevant
  - tier_2
  - saludly_brain_v1
use_when:
  - "anemia macrocítica junto a B12"
  - "homocisteína elevada"
  - "embarazo o planificación de embarazo"
combine_with: [vitamin_b12, homocysteine, mcv, hemoglobin]
do_not_use_alone:
  - "conclusión sobre reservas reales sin considerar ingesta reciente"
do_not_conclude:
  - "deficiencia de B12 vs folato sin homocisteína/MMA diferencial"
escalate_when:
  - "anemia macrocítica confirmada con folato bajo"
  - "deficiencia en embarazo o planificación de embarazo"
```
