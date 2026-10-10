---
doc_id: SLD-BIO-098
biomarker_id: homocysteine
name_es: Homocisteína
name_en: Homocysteine
abbreviation: Hcy
sinonimos:
- Homocisteína
- Hcy
- Homocysteine
category: Cardiovascular/Metabolismo
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µmol/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-NU-A01
combine_with:
- vitamin_b12
- folate
- vitamin_b6
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
- No se usa como riesgo cardiovascular (descartado en el Lote 1); es marcador funcional de B12 y folato (COND-M3-NU-A01).
---

# Homocisteína

## Notas de decisión de Saludly (6 de octubre de 2026)

- No se usa como riesgo cardiovascular (descartado en el Lote 1); es marcador funcional de B12 y folato (COND-M3-NU-A01).
- Reglas que usan esta ficha: COND-M3-NU-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-098. Hcy. Categoría: Cardiovascular/Metabolismo. Tipo: measured_analyte. Tier 3 — refinamiento de riesgo cardiovascular o marcador funcional de deficiencia de B12/folato, no cribado poblacional aislado de rutina.

## B. Definición

Aminoácido intermedio del metabolismo de metionina, cuyo catabolismo depende de vitamina B12, folato y vitamina B6. Su elevación (hiperhomocisteinemia) es tanto un marcador de deficiencia vitamínica funcional como un factor de riesgo cardiovascular independiente (aunque la relación causal con eventos cardiovasculares sigue debatida).

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (plasma, tubo EDTA en hielo — la muestra debe procesarse rápidamente o separarse pronto porque los eritrocitos siguen liberando homocisteína si la muestra no se centrifuga a tiempo) · Método: inmunoensayo o HPLC.

### Condiciones de toma de muestra

Ayuno recomendado (8-10h). **Suplementación reciente de B12/folato/B6 puede normalizar el valor** y debe registrarse antes de interpretar. Función renal afecta el nivel (ver interpretación).

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, por severidad (evidencia verificada esta sesión)

- **Normal:** <15 µmol/L.
- **Elevación moderada:** 15-30 µmol/L.
- **Elevación intermedia:** 30-100 µmol/L.
- **Elevación severa:** >100 µmol/L.
- **Contexto de enfermedad renal (verificado esta sesión):** en pacientes con enfermedad renal terminal, la hiperhomocisteinemia leve-moderada es frecuente, típicamente en rango 20-80 µmol/L — la función renal reducida por sí sola eleva la homocisteína, independientemente de deficiencia vitamínica.
- **URLs fuente:** https://www.urmc.rochester.edu/encyclopedia/content?ContentTypeID=167&ContentID=homocysteine ; contexto renal verificado en documentación técnica de metabolismo del hierro — ambas verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** deficiencia de B12, folato o B6 (causa más común y corregible), enfermedad renal (reduce la eliminación), hipotiroidismo, genética (mutación MTHFR — de utilidad clínica debatida para pruebas rutinarias), tabaquismo, café en exceso.
- **Diferencial con B12/folato (ver `vitamin_b12.md` y `folate.md`):** homocisteína elevada + MMA normal = más compatible con deficiencia de folato; homocisteína y MMA ambos elevados = más compatible con deficiencia de B12.

## F. Contexto del paciente y confusores

### Contexto del paciente

Función renal (crítico — eleva homocisteína independientemente de vitaminas), suplementación vitamínica reciente, tabaquismo, consumo de café, antecedente de trombosis venosa a edad temprana.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Vitamina B12, Folato, Vitamina B6 (las tres vitaminas cuya deficiencia eleva homocisteína), Creatinina/eGFR (función renal como causa no vitamínica de elevación).
- `pattern_examples`: homocisteína elevada + B12/folato normales + eGFR reducido = la elevación probablemente refleja la función renal, no deficiencia vitamínica.
- `cannot_conclude`: relación causal directa con riesgo cardiovascular — la evidencia de que reducir homocisteína (con suplementación) reduce eventos cardiovasculares es débil/controvertida en la literatura de ensayos clínicos.

## H. Tendencias

### Tendencias temporales

Responde a suplementación vitamínica en semanas si la causa es deficiencia — útil para confirmar respuesta al tratamiento.

## I. Prevención

### Contexto preventivo

Uso principalmente como marcador funcional de deficiencia de B12/folato/B6 en zona gris, o como refinamiento de riesgo cardiovascular en personas con antecedente familiar de trombosis o enfermedad cardiovascular sin otros factores de riesgo evidentes.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Vitamina B12, Folato, Vitamina B6, función renal si no están disponibles.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No concluir sobre riesgo cardiovascular con homocisteína aislada sin el resto del perfil de riesgo. Escalar ante elevación severa (>100 µmol/L, poco frecuente, considerar causas genéticas raras de homocistinuria) o antecedente de trombosis venosa a edad temprana con homocisteína elevada.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte para el rango de referencia (fuente clínica institucional); moderado/controvertido para la relación causal con eventos cardiovasculares (fuera del alcance verificar en esta sesión, área con evidencia de ensayos clínicos mixta ampliamente reportada en la literatura cardiovascular).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "homocisteína elevada, considerar B12/folato/B6 y función renal como causas antes de atribuir el valor a riesgo cardiovascular puro".
- **prohibited_inferences:** "homocisteína alta = va a tener un evento cardiovascular"; recomendar suplementación específica para reducir riesgo cardiovascular (evidencia de beneficio clínico débil).
- **uncertainty_notes:** la relación causal entre reducir homocisteína y reducir eventos cardiovasculares no está bien establecida en ensayos clínicos — comunicar esto con honestidad.
- **professional_review:** elevación severa (>100 µmol/L), o antecedente de trombosis venosa a edad temprana con homocisteína elevada.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - vitamin_deficiency
  - tier_3
  - saludly_brain_v1
use_when:
  - "deficiencia de B12/folato en zona gris"
  - "refinamiento de riesgo cardiovascular"
  - "antecedente de trombosis venosa a edad temprana"
combine_with: [vitamin_b12, folate, vitamin_b6, creatinine, egfr]
do_not_use_alone:
  - "conclusión de riesgo cardiovascular sin el resto del perfil"
do_not_conclude:
  - "certeza de evento cardiovascular futuro"
  - "beneficio de suplementación para reducir riesgo cardiovascular (evidencia débil)"
escalate_when:
  - "elevación severa (>100 µmol/L)"
  - "antecedente de trombosis venosa a edad temprana"
```
