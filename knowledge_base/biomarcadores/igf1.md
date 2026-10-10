---
doc_id: SLD-BIO-097
biomarker_id: igf1
name_es: IGF-1
name_en: Insulin-like Growth Factor 1
abbreviation: IGF-1
sinonimos:
- IGF-1
- Somatomedina C
- IGF-1 (Factor de Crecimiento Similar a la Insulina Tipo 1)
- Insulin-like Growth Factor 1
category: Endocrinología
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-003
tier: 4
status: PARCIAL
schema_version: '2.1'
clinical_priority: low
requires_professional_review: true
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Medido a todos: revisión médica obligatoria; ficha en estado PARCIAL hasta tener la tabla por edad (SEG-003).'
---

# IGF-1 (Factor de Crecimiento Similar a la Insulina Tipo 1)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Medido a todos: revisión médica obligatoria; ficha en estado PARCIAL hasta tener la tabla por edad (SEG-003).
- Reglas que usan esta ficha: SEG-003. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-097. IGF-1. Categoría: Endocrinología. Tipo: measured_analyte. **Tier 4 — EXCLUIDO del panel preventivo general**, confirmado en esta auditoría: específico para sospecha de trastornos de hormona de crecimiento, sin rol como marcador preventivo poblacional.

## B. Definición

Mediador principal de los efectos de la hormona de crecimiento (GH). A diferencia de GH (que se secreta en pulsos y es difícil de interpretar en una sola toma), IGF-1 tiene niveles estables a lo largo del día, lo que la hace la prueba de cribado preferida para sospecha de exceso o deficiencia de GH — pero exclusivamente en ese contexto clínico específico.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo.

### Condiciones de toma de muestra

No requiere ayuno ni horario específico crítico (ventaja frente a GH directa, por su estabilidad a lo largo del día). **Factor preanalítico crítico (LabCorp, verificado esta sesión): suspender consumo de biotina al menos 72 horas antes de la toma** — la biotina interfiere con este inmunoensayo, igual que con TSH/T4/FSH/LH ya documentado en otras fichas del catálogo.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión — LabCorp, calibrado a estándar OMS)

- **Fuente institucional real (LabCorp, verificado esta sesión):** el ensayo IDS iSYS IGF-1 está calibrado al estándar de referencia recombinante de la OMS (02/254) y sigue el consenso de estandarización de ensayos de IGF-1. Los intervalos de referencia se determinaron en una **cohorte de 1,488,925 personas** (778,173 hombres y 710,752 mujeres, 0-90 años), representativa de la población de EE.UU. en sexo, raza y etnia, ajustados por edad y sexo mediante el método de Hoffman modificado.
- **URL fuente:** https://www.labcorp.com/tests/010363/insulin-like-growth-factor-1-igf-1 — verificado esta sesión (ago-2026). **Nota:** LabCorp no publica la tabla numérica completa de rangos por edad en la página pública consultada (remite a informe de laboratorio específico) — Saludly debe obtener la tabla completa del reporte técnico del ensayo o del laboratorio aliado antes de fijar valores de producto.
- **Tabla de referencia adicional (LabCorp Specialty Testing, verificado esta sesión, población pediátrica/adolescente detallada):** para adultos jóvenes (16-17 años, Tanner 4-5): 177-516 ng/mL — la tabla completa de LabCorp Specialty Testing cubre en detalle 0-17 años por estadio de Tanner, pero no incluye explícitamente los grupos de adultos >18 años en el extracto consultado.
- **Determinantes poblacionales documentados (estudio en 2,791 adultos chinos sanos, verificado esta sesión):** el IGF-1 disminuye gradualmente con la edad (18-70 años) en ambos sexos; existe relación inversa con el IMC; y el nivel varía por región geográfica incluso dentro del mismo país — refuerza que los rangos por edad de una sola fuente occidental no deben aplicarse sin ajuste a poblaciones latinoamericanas como la de Saludly.
- **Nota sobre la fuente previamente citada (patente farmacéutica):** los valores de esa fuente (17-24 años ~180-780 ng/mL · 25-39 años ~114-400 ng/mL · 40-54 años ~90-360 ng/mL · >54 años ~70-290 ng/mL) siguen sin verificarse contra un documento clínico primario con la tabla completa — se mantienen como referencia orientativa de patrón (magnitud y tendencia descendente con la edad son consistentes con la literatura real ahora citada), pero no como valores de producto certificados.

## E. Interpretación

- **Baja:** sugiere deficiencia de hormona de crecimiento (requiere pruebas de estimulación para confirmar, no solo IGF-1 basal); malnutrición (LabCorp señala explícitamente que la malnutrición causa niveles bajos de somatomedina-C **pese a cantidades normales de hormona de crecimiento circulante** — es una fuente de falso positivo para deficiencia de GH).
- **Alta:** sugiere exceso de hormona de crecimiento (acromegalia en adultos, gigantismo si es antes del cierre de placas de crecimiento) — requiere prueba de supresión con glucosa oral para confirmar.
- **Limitación diagnóstica documentada (LabCorp, verificado esta sesión):** el nivel de somatomedina-C **no distingue** entre enanismo hipofisario (deficiencia real de GH) y retraso constitucional del crecimiento y desarrollo (variante normal) — ambos pueden presentar IGF-1 bajo en niños/adolescentes, requiere evaluación clínica adicional para diferenciar.

## F. Contexto del paciente y confusores

### Contexto del paciente

Edad (determinante del rango de referencia), estado nutricional (la desnutrición reduce IGF-1 independientemente de la GH real — fuente de falso positivo), función hepática (síntesis hepática), diabetes mal controlada (puede alterar IGF-1), IMC (relación inversa documentada), consumo de biotina reciente, región geográfica/etnia (documentado como determinante en estudio poblacional chino).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ninguno del catálogo actual de Saludly de forma directa — su interpretación requiere pruebas dinámicas (supresión con glucosa oral para sospecha de exceso, pruebas de estimulación para sospecha de deficiencia) fuera del alcance de un panel de laboratorio estándar.
- `cannot_conclude`: diagnóstico de acromegalia o deficiencia de GH sin pruebas dinámicas de confirmación.

## H. Tendencias

### Tendencias temporales

Disminuye progresivamente con la edad de forma fisiológica — un valor bajo en una persona mayor no es necesariamente patológico sin contexto clínico (síntomas, antecedentes).

## I. Prevención

### Contexto preventivo

Ninguno — excluido del panel general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Prueba de supresión con glucosa oral (sospecha de acromegalia), pruebas de estimulación de GH (sospecha de deficiencia) — ambas fuera del alcance operativo de Saludly.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar acromegalia ni deficiencia de GH con IGF-1 aislada. Escalar SIEMPRE que aparezca este biomarcador con sospecha clínica de trastorno de hormona de crecimiento (cambios en rasgos faciales/manos/pies para acromegalia; talla baja o retraso de crecimiento en deficiencia).

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte — LabCorp, ensayo calibrado a estándar OMS 02/254, validado en cohorte de 1,488,925 personas (0-90 años), representativa de la población de EE.UU.
- **Complementaria:** estudio de determinantes poblacionales en 2,791 adultos chinos sanos (edad, IMC, región geográfica).
- **Limitación remanente:** la tabla numérica completa de rangos por edad para adultos no se obtuvo de la página pública de LabCorp consultada — requiere el reporte técnico completo del ensayo antes de fijar valores exactos de producto. Los valores de la fuente de patente farmacéutica se mantienen solo como referencia orientativa de patrón, no como dato certificado.
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "IGF-1 alterada sugiere posible trastorno del eje de hormona de crecimiento o malnutrición, requiere pruebas dinámicas de confirmación — nunca concluir con este valor aislado".
- **prohibited_inferences:** diagnóstico de acromegalia o deficiencia de GH sin pruebas dinámicas; usar los rangos numéricos de la fuente de patente farmacéutica como umbral de producto certificado (siguen sin verificación completa contra la tabla técnica de LabCorp).
- **uncertainty_notes:** el ensayo de referencia (LabCorp/IDS iSYS, calibrado OMS) es sólido, pero la tabla numérica completa de rangos por edad para adultos requiere el reporte técnico específico, no solo la página pública consultada. Verificar consumo reciente de biotina antes de interpretar un resultado inesperado.
- **professional_review:** SIEMPRE que aparezca este biomarcador con sospecha clínica de trastorno de GH — requiere evaluación endocrinológica con pruebas dinámicas.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - endocrinology
  - growth_hormone
  - tier_4
  - saludly_brain_v1
use_when:
  - "sospecha clínica específica de acromegalia o deficiencia de GH"
combine_with: []
do_not_use_alone:
  - "diagnóstico de acromegalia o deficiencia de GH"
do_not_conclude:
  - "diagnóstico sin pruebas dinámicas de confirmación"
escalate_when:
  - "SIEMPRE ante sospecha clínica de trastorno de hormona de crecimiento"
```
