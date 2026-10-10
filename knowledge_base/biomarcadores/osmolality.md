---
doc_id: SLD-BIO-031
biomarker_id: osmolality
name_es: Osmolalidad Sérica
name_en: Serum Osmolality
abbreviation: OSM
sinonimos:
- Osmolalidad sérica
- Osmolalidad
- Osmolalidad Sérica
- OSM
- Serum Osmolality
category: Metabolismo
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mOsm/kg
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-004
combine_with:
- sodium
- glucose
- bun
tier: 4
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: true
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Medido a todos: revisión médica obligatoria; la alarma es la brecha osmolar (SEG-004).'
---

# Osmolalidad Sérica

## Notas de decisión de Saludly (6 de octubre de 2026)

- Medido a todos: revisión médica obligatoria; la alarma es la brecha osmolar (SEG-004).
- Reglas que usan esta ficha: SEG-004. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-031. OSM. Categoría: Metabolismo. Tipo: measured_analyte (con versión calculada disponible para comparación). **Tier 4 — uso casi exclusivamente hospitalario/agudo**, confirmado en esta auditoría: trastornos de sodio, intoxicaciones — sin lugar en un panel preventivo ambulatorio.

## B. Definición

Concentración total de partículas osmóticamente activas en el plasma, determinada principalmente por sodio, glucosa y urea (BUN). Su uso clínico principal es agudo: evaluación de trastornos de sodio y detección de "gap osmolar" en sospecha de intoxicación por alcoholes tóxicos (metanol, etilenglicol).

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: osmómetro de punto de congelación (medición directa) — a diferencia de la mayoría de analitos de este catálogo, requiere un instrumento especializado no disponible en todos los laboratorios.

### Condiciones de toma de muestra

No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Laboratory reference interval:** **275-295 mOsm/kg** (fuentes concordantes: ACCP 275-295, RNpedia 280-300).
- **URLs fuente:** https://www.accp.com/docs/sap/Lab_Values_Table_PSAP.pdf ; https://www.rnpedia.com/tools-apps/normal-laboratory-values/ — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** deshidratación, hiperglucemia severa, intoxicación por alcoholes (con gap osmolar elevado — diferencia entre osmolalidad medida y calculada >10-15 mOsm/kg sugiere presencia de sustancias osmóticamente activas no medidas, como metanol o etilenglicol).
- **Disminuida:** sobrehidratación, SIADH (síndrome de secreción inadecuada de hormona antidiurética).
- **Gap osmolar (medida − calculada):** normalmente <10 mOsm/kg; un gap elevado en contexto de sospecha de intoxicación es una urgencia médica.

## F. Contexto del paciente y confusores

### Contexto del paciente

Estado de hidratación, glucosa, función renal (BUN), sospecha de ingesta de sustancias tóxicas, síntomas neurológicos (confusión, alteración del estado de conciencia).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Sodio, Glucosa, BUN (todos variables del cálculo de osmolalidad calculada, para comparar con la medida y determinar el gap osmolar).
- `cannot_conclude`: causa específica del trastorno sin evaluación clínica y contexto de exposición a tóxicos.

## H. Tendencias

### Tendencias temporales

No aplica seguimiento longitudinal de rutina — uso exclusivamente agudo/hospitalario.

## I. Prevención

### Contexto preventivo

Ninguno — excluido del panel general por diseño.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Sodio, Glucosa, BUN (para calcular la osmolalidad calculada y el gap), evaluación toxicológica si se sospecha intoxicación.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No ofrecer en panel preventivo. Escalar SIEMPRE que se solicite este biomarcador — su indicación típica (sospecha de intoxicación, trastorno agudo de sodio) requiere evaluación médica urgente, no interpretación por IA.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (fuentes clínicas académicas concordantes).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** ninguna interpretación autónoma — este biomarcador, por su contexto de uso casi exclusivamente agudo/hospitalario, debe activar derivación inmediata si aparece.
- **prohibited_inferences:** cualquier interpretación de rutina o tranquilizadora sin considerar el contexto agudo típico de esta prueba.
- **uncertainty_notes:** su sola presencia en un resultado de laboratorio sugiere un contexto clínico agudo que Saludly no está diseñado para manejar de forma autónoma.
- **professional_review:** SIEMPRE — este es uno de los biomarcadores del catálogo con umbral de escalamiento más bajo, junto con troponina, NRBC y ACTH/cortisol.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - acute_care
  - tier_4
  - saludly_brain_v1
use_when:
  - "solo si ya existe sospecha clínica de trastorno agudo de sodio o intoxicación"
combine_with: [sodium, glucose, bun]
do_not_use_alone:
  - "cualquier interpretación de rutina"
do_not_conclude:
  - "tranquilidad clínica sin evaluación del contexto agudo"
escalate_when:
  - "SIEMPRE — requiere evaluación médica urgente"
```
