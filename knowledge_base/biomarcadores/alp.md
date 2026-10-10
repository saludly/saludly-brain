---
doc_id: SLD-BIO-059
biomarker_id: alp
name_es: Fosfatasa Alcalina
name_en: Alkaline Phosphatase
abbreviation: ALP / FA
sinonimos:
- Fosfatasa alcalina
- FA
- ALP
- FAL
- Fosfatasa Alcalina
- ALP / FA
- Alkaline Phosphatase
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
- COND-M6-MI-A02
combine_with:
- ggt
- alt
- ast
- bilirubin_total
- calcium
- phosphorus
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

# Fosfatasa Alcalina (ALP)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-003, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-059. ALP/FA. Categoría: Hepatología (con relación cruzada a hueso). Tipo: analito medido. Tier 2.

## B. Definición

Enzima presente principalmente en hígado (canalículos biliares) y hueso (osteoblastos), y en menor medida en intestino y placenta. Su origen (hepático vs óseo) no puede determinarse sin una prueba complementaria (GGT, o isoenzimas de ALP si están disponibles).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método enzimático estandarizado. Unidad: UI/L. No requiere ayuno. Factor fisiológico importante: **fisiológicamente elevada en niños/adolescentes en crecimiento y en el tercer trimestre de embarazo** (origen placentario) — no debe interpretarse como patológica en esos contextos sin más evaluación.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método, con variación fisiológica marcada por edad (crecimiento óseo) y embarazo.
- **Clinical decision threshold:** según ACG 2017, ALP elevada con GGT concurrentemente elevada sugiere origen hepatobiliar (colestasis); ALP elevada con GGT normal sugiere origen óseo — mismo racional documentado en `ggt.md`. Fuente verificada esta sesión: guía ACG 2017 (ver referencia en L).

## E. Interpretación

- **Elevada (origen hepático):** colestasis intrahepática o extrahepática, cirrosis biliar, infiltración hepática.
- **Elevada (origen óseo):** crecimiento normal (niños/adolescentes), embarazo (tercer trimestre, fisiológico), enfermedad de Paget, fracturas en consolidación, metástasis óseas, hiperparatiroidismo.
- **Disminuida:** poco frecuente y de menor relevancia clínica aislada; en raros casos asociada a hipofosfatasia (condición genética) o desnutrición severa.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: edad (crecimiento óseo en niños/adolescentes), embarazo y trimestre, síntomas óseos (dolor, fracturas), síntomas de vía biliar.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: GGT (obligatorio, para diferenciar origen hepático de óseo), Calcio y Fósforo (si se sospecha origen óseo), Bilirrubina total, ALT/AST.
- `pattern_examples`: ALP alta + GGT alta = colestasis; ALP alta + GGT normal + calcio/fósforo alterados = considerar origen óseo (hiperparatiroidismo, enfermedad de Paget).
- `cannot_conclude`: diagnóstico específico de la causa ósea o hepática sin estudios de imagen o marcadores óseos adicionales que Saludly no ofrece en v1.

## H. Tendencias

### Tendencias temporales

En niños/adolescentes, valores elevados son esperables y fluctúan con la velocidad de crecimiento — no deben alarmar sin contexto de edad. En adultos, una tendencia ascendente sostenida sin explicación por edad/embarazo es más relevante que un valor puntual.

## I. Prevención

Utilidad principalmente confirmatoria/de orientación diagnóstica junto al resto del panel hepático — no tiene una acción preventiva independiente propia.

## J. Pruebas complementarias

### Pruebas complementarias posibles

GGT (si no se solicitó junto), Calcio/Fósforo (si se sospecha origen óseo), imagen ósea o hepatobiliar según el patrón (fuera del alcance de Saludly, requiere derivación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica por sí sola — requiere GGT (y en algunos casos calcio/fósforo) para orientar el origen antes de cualquier interpretación significativa.

## L. Evidencia

### Evidencia científica

- **Guideline (fuerte):** Kwo PY, Cohen SM, Lim JK. "ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries." *Am J Gastroenterol.* 2017. https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver — verificado esta sesión (ago-2026).
- Nivel de evidencia: guideline de sociedad médica, fuerte, para el uso combinado con GGT.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "ALP elevada, considerar edad/embarazo como causa fisiológica antes de interpretar como patológica; combinar con GGT para diferenciar origen hepático de óseo".
- **prohibited_inferences:** diagnóstico de enfermedad hepática o de Paget a partir de ALP aislada; interpretar como patológica una elevación esperada por crecimiento o embarazo.
- **uncertainty_notes:** su interpretación depende críticamente de edad y estado de embarazo — omitir este contexto genera alto riesgo de falsa alarma.
- **professional_review:** ALP marcadamente elevada sin explicación por edad/embarazo, especialmente combinada con GGT alterada (patrón colestásico) o con dolor óseo/fracturas.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - bone_metabolism
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando patrón colestásico junto a GGT"
  - "sospecha de origen óseo (dolor óseo, fracturas, hiperparatiroidismo)"

combine_with: [ggt, alt, ast, bilirubin_total, calcium, phosphorus]

do_not_use_alone:
  - "diagnóstico de enfermedad hepática u ósea"

do_not_conclude:
  - "patología a partir de ALP elevada explicable por edad o embarazo"

escalate_when:
  - "ALP marcadamente elevada sin explicación fisiológica, combinada con GGT o síntomas óseos"
```
