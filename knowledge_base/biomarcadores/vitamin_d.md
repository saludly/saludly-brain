---
doc_id: SLD-BIO-082
biomarker_id: vitamin_d
name_es: 25-Hidroxivitamina D
name_en: 25-Hydroxyvitamin D
abbreviation: 25(OH)D
sinonimos:
- 25-hidroxivitamina D
- 25-OH vitamina D
- Vitamina D total
- Vitamina D
- 25-Hidroxivitamina D
- 25-OH Vitamina D
- 25(OH)D
- 25-Hydroxyvitamin D
category: Vitaminas
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: ng/mL
specimen: Suero
nivel_catalogo: vitamina
panel: estándar
sexo: ambos
alimenta:
- COND-M3-NU-A02
- COND-M3-NU-A03
combine_with:
- calcium
- pth
- phosphorus
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Regla de vitaminas aprobada: se marca baja, en rango o alta con el intervalo del laboratorio, sin etiqueta de deficiencia y sin dosis (COND-M3-NU-A03). Las definiciones de deficiencia de esta ficha quedan solo como contexto para el médico.'
---

# 25-OH Vitamina D

## Notas de decisión de Saludly (6 de octubre de 2026)

- Regla de vitaminas aprobada: se marca baja, en rango o alta con el intervalo del laboratorio, sin etiqueta de deficiencia y sin dosis (COND-M3-NU-A03). Las definiciones de deficiencia de esta ficha quedan solo como contexto para el médico.
- Reglas que usan esta ficha: COND-M3-NU-A02, COND-M3-NU-A03. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-082. 25(OH)D. Categoría: Vitaminas. Tipo: measured_analyte. Tier 3 (corregido desde Tier 1 en auditoría previa — ver `audit_note` en `00_INDEX.md`): Endocrine Society 2024 no recomienda cribado rutinario en adultos sanos.

## B. Definición

Metabolito de la vitamina D con mayor vida media (2-3 semanas), usado como el mejor indicador del estado de vitamina D corporal — a diferencia de la forma activa (1,25-dihidroxivitamina D), cuya vida media corta (4-6 horas) la hace poco útil para evaluar reservas.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: quimioluminiscencia o HPLC (más preciso, especialmente para distinguir D2 de D3).

### Condiciones de toma de muestra

No requiere ayuno. Relevante: estación del año (niveles más altos en verano por mayor exposición solar), geografía/latitud, etnia (pigmentación cutánea afecta síntesis).

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con disenso documentado (evidencia verificada esta sesión)

- **Clinical decision values (Mayo Clinic Laboratories, basados en el reporte 2011 del Institute of Medicine):** estos son valores de decisión clínica aplicables a todas las edades/sexos, **no rangos poblacionales** — el IOM reconoce explícitamente que los rangos poblacionales varían ampliamente por etnia, edad, geografía y estación, y correlacionan pobremente con los efectos biológicos clínicamente relevantes.
- **Definiciones con disenso activo (verificado esta sesión, múltiples fuentes):** deficiencia **<20 ng/mL** (relativamente consistente entre fuentes); insuficiencia reportada como **<30 ng/mL** en algunas fuentes; deficiencia severa **<10-12 ng/mL** (asociada a mayor mortalidad, susceptibilidad a infecciones). Rango "óptimo" reportado ampliamente: **25-80 ng/mL** — este rango tan amplio refleja precisamente el disenso que Endocrine Society 2024 señaló al retirar la categoría de "insuficiencia" como accionable en población sana.
- **URLs fuente:** https://pediatric.testcatalog.org/show/25HDN (Mayo Clinic, nota metodológica IOM) ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2912737/ (revisión "Vitamin D Deficiency in Adults: When to Test and How to Treat") — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Deficiencia (<20 ng/mL):** puede asociarse a osteoporosis, hiperparatiroidismo secundario; deficiencia severa puede causar osteomalacia en adultos.
- **Dentro del rango "óptimo" amplio (25-80 ng/mL):** sin indicación clara de intervención en persona sin factores de riesgo — este es exactamente el racional detrás de la decisión de Endocrine Society 2024 de no recomendar cribado poblacional.

## F. Contexto del paciente y confusores

### Contexto del paciente

Estación del año, exposición solar habitual, dieta, malabsorción (enfermedad celíaca, cirugía bariátrica), institucionalización, uso de protector solar, pigmentación cutánea, función renal.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Calcio, PTH (deficiencia de vitamina D es causa frecuente de hiperparatiroidismo secundario), Fósforo.
- `pattern_examples`: vitamina D baja + PTH alta + calcio bajo/normal = hiperparatiroidismo secundario por deficiencia de vitamina D.
- `cannot_conclude`: osteoporosis o riesgo de fractura solo con vitamina D — requiere densitometría ósea para ese diagnóstico.

## H. Tendencias

### Tendencias temporales

Fluctúa estacionalmente (más alta en verano) — comparar valores de estaciones distintas sin ajustar por esto puede ser engañoso.

## I. Prevención

### Contexto preventivo

Solo en indicaciones específicas (ver frontmatter) — no como parte del check-up general, decisión de producto ya documentada en la auditoría previa.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Calcio, PTH si hay sospecha de hiperparatiroidismo secundario.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No ofrecer como cribado poblacional general. Escalar ante deficiencia severa (<10-12 ng/mL) con síntomas óseos, o hiperparatiroidismo secundario confirmado.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories + revisión clínica Mayo Clinic Proceedings 2010, ampliamente citada).
- Fuentes verificadas esta sesión: ver URLs en sección E. Nota de auditoría previa: Endocrine Society 2024 (recomendación contra cribado rutinario) verificada en sesión anterior.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "vitamina D baja, considerar en contexto de factores de riesgo específicos (malabsorción, poca exposición solar, osteoporosis) — no ofrecer como hallazgo de cribado general".
- **prohibited_inferences:** recomendar la prueba como parte de un chequeo general sin indicación específica; diagnóstico de osteoporosis solo con este valor.
- **uncertainty_notes:** existe disenso activo en la literatura sobre los umbrales exactos de insuficiencia — comunicar el rango amplio "óptimo" (25-80 ng/mL) en vez de un número único falsamente preciso.
- **professional_review:** deficiencia severa con síntomas óseos, o hiperparatiroidismo secundario confirmado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitamins
  - bone_health
  - tier_3
  - saludly_brain_v1
use_when:
  - "osteoporosis, malabsorción, institucionalización, o hiperparatiroidismo secundario en investigación"
combine_with: [calcium, pth, phosphorus]
do_not_use_alone:
  - "diagnóstico de osteoporosis"
  - "cribado poblacional general sin indicación"
do_not_conclude:
  - "riesgo de fractura sin densitometría ósea"
escalate_when:
  - "deficiencia severa (<10-12 ng/mL) con síntomas óseos"
  - "hiperparatiroidismo secundario confirmado"
```
