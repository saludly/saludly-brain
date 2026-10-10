---
doc_id: SLD-BIO-083
biomarker_id: zinc
name_es: Zinc Sérico
name_en: Serum Zinc
abbreviation: Zn
sinonimos:
- Zinc
- Zn
- Zinc Sérico
- Serum Zinc
category: Vitaminas
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-014
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Zinc Sérico

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-014. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-083. Zn. Categoría: Vitaminas/Micronutrientes. Tipo: measured_analyte. Tier 3 — indicado ante síntomas específicos, no cribado general.

## B. Definición

Micronutriente esencial, cofactor de más de 300 enzimas. Su deficiencia se manifiesta clínicamente con cicatrización deficiente, alopecia, alteración del gusto/olfato, y lesiones cutáneas características.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero, tubo específico libre de contaminación con zinc — **factor preanalítico crítico:** tubos con tapón de caucho estándar pueden contaminar la muestra con zinc, falseando el resultado al alza; se requiere tubo especial certificado libre de trazas).

### Condiciones de toma de muestra — CRÍTICO (Mayo Clinic, verificado esta sesión)

Ayuno matutino recomendado por variación diurna. **Requiere tubo especial libre de metales traza** (tapa azul real/"royal blue", EDTA) — un tubo estándar contamina la muestra con zinc, falseando el resultado al alza. Evitar hemólisis (falsa elevación). **No tomar de una línea vascular** (puede elevar falsamente el resultado; considerar repetir por venopunción si hay duda clínica).

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión — Mayo Clinic Laboratories)

- **Laboratory reference interval:** **66-106 mcg/dL** en adultos (fuente principal, catálogo Mayo Clinic Laboratories). Nota: otra referencia técnica de Mayo Clinic (test de referido) reporta 80-120 mcg/dL — la diferencia probablemente refleja distintas plataformas/métodos analíticos entre laboratorios de referencia de la misma institución; Saludly debe usar el rango específico del laboratorio aliado.
- **Umbral clínico de deficiencia sintomática:** pacientes quemados o con acrodermatitis pueden tener zinc tan bajo como **40 mcg/dL**, respondiendo rápidamente a suplementación.
- **Nota importante (Mayo Clinic, verificado esta sesión):** una concentración de zinc sérico **elevada tiene mínimo interés clínico** — el exceso de zinc no causa toxicidad directa relevante en la mayoría de los casos (se absorbe poco, se excreta el exceso), aunque interfiere con la absorción de cobre y puede causar hipocupremia con uso excesivo prolongado de suplementos.
- **URLs fuente:** https://www.mayocliniclabs.com/test-catalog/overview/7735 ; https://pediatric.testcatalog.org/show/ZN_S — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Disminuido:** dieta deficiente (vegetarianismo/veganismo estricto sin suplementación, ya que el zinc de fuentes vegetales tiene menor biodisponibilidad), malabsorción, enfermedad hepática crónica, diarrea crónica, cirugía bariátrica.
- **Elevado:** poco frecuente, generalmente por suplementación excesiva reciente.

## F. Contexto del paciente y confusores

### Contexto del paciente

Dieta (vegetarianismo/veganismo), malabsorción, diarrea crónica, cirugía bariátrica, síntomas específicos (alopecia, alteración del gusto, cicatrización deficiente, lesiones cutáneas).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ninguno de forma obligatoria en el catálogo actual — su interpretación es principalmente clínica (síntomas + dieta).
- `cannot_conclude`: deficiencia clínicamente significativa solo con el valor sérico, dado que el zinc sérico tiene limitaciones de sensibilidad similares a otros micronutrientes de este catálogo (ej. magnesio).

## H. Tendencias

### Tendencias temporales

Variación diurna e influenciada por ingesta reciente — no es un buen marcador de tendencia sin ajustar por horario de toma.

## I. Prevención

### Contexto preventivo

Indicado solo ante síntomas específicos — no cribado general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna prueba de laboratorio complementaria estándar en el catálogo actual — el diagnóstico se apoya fuertemente en la clínica.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No usar como cribado general. Escalar ante síntomas clínicos claros de deficiencia (alopecia, lesiones cutáneas características, alteración marcada del gusto) independientemente del valor de laboratorio si hay alta sospecha clínica.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Mayo Clinic Laboratories, referencia a Tietz Textbook of Laboratory Medicine 7th ed.).
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "zinc alterado, considerar dieta y síntomas específicos; una elevación tiene mínimo interés clínico según Mayo Clinic".
- **prohibited_inferences:** diagnóstico de deficiencia de zinc basado únicamente en el valor de laboratorio sin síntomas clínicos concordantes.
- **uncertainty_notes:** verificar que la muestra se tomó con tubo libre de metales traza y sin hemólisis antes de interpretar un valor inesperadamente alto.
- **professional_review:** síntomas clínicos claros de deficiencia de zinc, independientemente del valor de laboratorio.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitamins
  - micronutrients
  - tier_3
  - saludly_brain_v1
use_when:
  - "síntomas específicos de deficiencia de zinc (alopecia, alteración del gusto, cicatrización deficiente)"
combine_with: []
do_not_use_alone:
  - "diagnóstico de deficiencia sin síntomas clínicos concordantes"
do_not_conclude:
  - "deficiencia clínicamente significativa solo con el valor sérico"
escalate_when:
  - "síntomas clínicos claros de deficiencia de zinc"
```
