---
doc_id: SLD-BIO-036
biomarker_id: bilirubin_direct
name_es: Bilirrubina Directa
name_en: Direct (Conjugated) Bilirubin
abbreviation: BD
sinonimos:
- Bilirrubina directa
- BD
- Bilirrubina conjugada
- Bilirrubina Directa
- Direct (Conjugated) Bilirubin
category: hepatology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M4-GA-003
- COND-M4-GA-A01
combine_with:
- bilirubin_total
- alp
- ggt
- alt
- ast
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

# Bilirrubina Directa (Conjugada)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-003, COND-M4-GA-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-036. BD. Categoría: Hepatología. Tipo: analito medido. Tier 2. Nota de auditoría: elimina el duplicado que existía en la lista original del usuario.

## B. Definición

Fracción de bilirrubina ya procesada (conjugada con ácido glucurónico) por el hígado, lista para excretarse por vía biliar. Su elevación específicamente (a diferencia de la indirecta) señala un problema en la excreción biliar — hepatocelular o de obstrucción — no en la producción/captación de bilirrubina.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico (diazo directo). Unidad: mg/dL. No requiere ayuno. Mismo cuidado de protección de la luz que bilirrubina total.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold:** cuando la bilirrubina directa representa >50% de la bilirrubina total, el patrón se considera predominantemente "directo" o colestásico/hepatocelular, orientando el estudio hacia obstrucción biliar o daño hepatocelular en vez de hemólisis o síndrome de Gilbert.

## E. Interpretación

- **Elevada:** obstrucción biliar (cálculos, tumores, estenosis), enfermedad hepatocelular (hepatitis, cirrosis), colestasis intrahepática.
- La bilirrubina indirecta (no medida directamente por Saludly, sino calculada como Total − Directa) se eleva en hemólisis y síndrome de Gilbert — ver `bilirubin_total.md`.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: síntomas de obstrucción biliar (dolor en hipocondrio derecho, acolia, coluria, prurito), antecedente de cálculos biliares, medicamentos hepatotóxicos.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Bilirrubina total (obligatorio, para calcular el porcentaje directo/indirecto), ALP y GGT (patrón colestásico), ALT/AST (patrón hepatocelular).
- `pattern_examples`: bilirrubina directa elevada + ALP/GGT elevadas = patrón colestásico, sugiere obstrucción biliar o colestasis intrahepática; bilirrubina directa elevada + ALT/AST muy elevadas = patrón hepatocelular con compromiso de excreción.
- `cannot_conclude`: causa anatómica específica (cálculo vs tumor vs estenosis) sin estudios de imagen — fuera del alcance de Saludly.

## H. Tendencias

### Tendencias temporales

Una elevación aguda y progresiva es más preocupante que una elevación leve estable — sugiere proceso obstructivo activo o daño hepatocelular en curso.

## I. Prevención

Utilidad principalmente diagnóstica — no tiene acción preventiva independiente propia.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ecografía hepatobiliar si el patrón sugiere obstrucción (fuera del alcance de Saludly, requiere derivación médica), resto del panel hepático completo.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Es una prueba de orientación diagnóstica dentro del panel hepático, no de cribado poblacional independiente.

## L. Evidencia

### Evidencia científica

- **Guideline complementaria:** ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries, 2017. https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver — verificado esta sesión (ago-2026), mismo racional que el resto del panel hepático.
- **Clinical decision threshold (verificado esta sesión, múltiples fuentes clínicas concordantes):** rango normal de bilirrubina directa **0.0-0.3 mg/dL** (algunas fuentes hasta 0.4 mg/dL). Patrón "predominantemente directo" (hiperbilirrubinemia conjugada): fracción directa **>1.0 mg/dL en términos absolutos, o >50% del total** — comúnmente causado por gallstones (cálculos), tumores, inflamación o estenosis de la vía biliar extrahepática. Un valor de directa >0.4 mg/dL, o >20-30% del total, ya sugiere fuertemente causa hepática/biliar en vez de hemolítica o Gilbert.
- **URL fuente:** https://www.uhhospitals.org/health-information/health-and-wellness-library/article/lab-tests-v1/direct-bilirubin ; https://emedicine.medscape.com/article/2074068-overview — verificadas esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "bilirrubina directa elevada, patrón compatible con posible obstrucción biliar o daño hepatocelular, combinar con ALP/GGT/ALT/AST".
- **prohibited_inferences:** diagnóstico de causa anatómica específica (cálculo, tumor) sin estudios de imagen.
- **uncertainty_notes:** Saludly no ofrece estudios de imagen — cualquier patrón obstructivo sugerido debe derivarse a evaluación médica con imagen, no resolverse dentro de la app.
- **professional_review:** elevación marcada, especialmente con síntomas de obstrucción biliar (dolor, acolia, coluria, prurito) — este patrón amerita evaluación relativamente pronta.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - bilirubin_metabolism
  - biliary_obstruction
  - tier_2
  - saludly_brain_v1

use_when:
  - "bilirrubina total elevada, para determinar el patrón directo/indirecto"
  - "síntomas de obstrucción biliar"

combine_with: [bilirubin_total, alp, ggt, alt, ast]

do_not_use_alone:
  - "diagnóstico de causa anatómica de obstrucción biliar"

do_not_conclude:
  - "presencia de cálculos, tumor o estenosis sin estudios de imagen"

escalate_when:
  - "elevación marcada con síntomas de obstrucción biliar"
  - "patrón hepatocelular con ALT/AST muy elevadas"
```
