---
doc_id: SLD-BIO-058
biomarker_id: ggt
name_es: Gamma-Glutamil Transferasa
name_en: Gamma-Glutamyl Transferase
abbreviation: GGT
sinonimos:
- GGT
- Gamma GT
- Gamma glutamil transferasa
- Gamma glutamil transpeptidasa
- Gamma-Glutamil Transferasa
- GGT (Gamma-Glutamil Transferasa)
- Gamma-Glutamyl Transferase
category: hepatology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: U/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M4-GA-003
- COND-M4-GA-A02
combine_with:
- alt
- ast
- alp
- bilirubin_total
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# GGT (Gamma-Glutamil Transferasa)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-003, COND-M4-GA-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-058. GGT. Categoría: Hepatología. Tipo: analito medido. Tier 2 — sensible pero muy inespecífica, no forma parte del panel básico.

## B. Definición

Enzima presente en hígado (particularmente en el epitelio biliar), riñón, páncreas y otros tejidos. Es una de las enzimas hepáticas más sensibles para detectar daño hepatobiliar, pero también una de las menos específicas: se induce por alcohol, muchos medicamentos comunes y obesidad, incluso sin enfermedad hepática significativa.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método enzimático estandarizado (IFCC). Unidad: UI/L. No requiere ayuno estricto. Factor preanalítico/de confusión importante: consumo de alcohol reciente (incluso moderado) e inducción por medicamentos comunes (anticonvulsivantes, algunos antibióticos) elevan GGT sin reflejar necesariamente daño hepático estructural.

## D. Intervalos y umbrales

- **Laboratory reference interval (verificado esta sesión):** rango normal reportado **7-47 UI/L en hombres · 5-25 UI/L en mujeres** (fuente clínica de divulgación de pruebas de laboratorio hepático, 2026) — consistente con el patrón esperado de mayor actividad de GGT en hombres. Saludly debe validar el rango exacto con el laboratorio aliado, dado que GGT tiene variabilidad interlaboratorio relevante.
- **Clinical decision threshold:** según la guía ACG 2017 (Kwo, Cohen, Lim, *Am J Gastroenterol*), GGT se usa principalmente para **confirmar el origen hepático** de una fosfatasa alcalina (ALP) elevada — si GGT está elevada junto con ALP, el origen es hepatobiliar; si ALP está elevada pero GGT es normal, el origen es probablemente óseo, no hepático.
- **URL fuente:** https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver ; https://www.levels.com/blog/levels-guide-liver-blood-tests — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** consumo de alcohol (incluso sin enfermedad hepática establecida), colestasis (obstrucción de vía biliar), esteatosis hepática, inducción enzimática por medicamentos, obesidad/síndrome metabólico.
- Su elevación aislada sin ALT/AST/ALP alteradas tiene bajo valor diagnóstico específico — es la enzima hepática de menor especificidad del panel.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: consumo de alcohol, medicamentos (anticonvulsivantes, ciertos antibióticos), IMC, síntomas de vía biliar (ictericia, coluria, prurito).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ALP (obligatorio, para diferenciar origen hepatobiliar de óseo), ALT/AST (patrón hepatocelular vs colestásico), Bilirrubina total.
- `pattern_examples`: ALP alta + GGT alta = patrón colestásico/hepatobiliar; ALP alta + GGT normal = sugiere origen óseo (embarazo, crecimiento, enfermedad de Paget), no hepático.
- `cannot_conclude`: causa específica de colestasis (intrahepática vs extrahepática) sin imagen (ecografía) — fuera del alcance de Saludly.

## H. Tendencias

### Tendencias temporales

Se normaliza en semanas tras cesar el consumo de alcohol en la mayoría de los casos — útil como marcador de seguimiento de abstinencia, aunque con limitaciones de especificidad.

## I. Prevención

Acciones razonablemente relacionadas: reducción de consumo de alcohol, revisión de medicamentos con potencial inductor enzimático junto a un profesional.

## J. Pruebas complementarias

### Pruebas complementarias posibles

ALP (si no se solicitó junto — debería pedirse siempre en conjunto para el patrón colestásico), ecografía hepatobiliar si el patrón sugiere colestasis (fuera del alcance de Saludly, requiere derivación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica por sí sola de ninguna condición — su valor principal es de confirmación/orientación cuando se combina con ALP y el resto del panel hepático.

## L. Evidencia

### Evidencia científica

- **Guideline (fuerte):** Kwo PY, Cohen SM, Lim JK. "ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries." *Am J Gastroenterol.* 2017. https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver
- Verificado por búsqueda web esta sesión (ago-2026). Nivel de evidencia: guideline de sociedad médica, fuerte.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "GGT elevada, considerar junto a ALP para diferenciar origen hepatobiliar de óseo, y contexto de consumo de alcohol/medicamentos".
- **prohibited_inferences:** "GGT alta = enfermedad hepática" sin el resto del panel; diagnóstico de alcoholismo a partir de GGT aislada.
- **uncertainty_notes:** es la enzima hepática menos específica del panel — su elevación aislada tiene bajo valor diagnóstico.
- **professional_review:** patrón colestásico (ALP + GGT elevadas) persistente, especialmente con síntomas de vía biliar (ictericia, coluria, prurito).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - liver_enzymes
  - tier_2
  - saludly_brain_v1

use_when:
  - "ALP elevada, para diferenciar origen hepatobiliar de óseo"
  - "sospecha de consumo de alcohol relevante"

combine_with: [alp, alt, ast, bilirubin_total]

do_not_use_alone:
  - "diagnóstico de enfermedad hepática"
  - "diagnóstico de alcoholismo"

do_not_conclude:
  - "enfermedad hepática confirmada a partir de GGT aislada"

escalate_when:
  - "patrón colestásico persistente con síntomas de vía biliar"
```
