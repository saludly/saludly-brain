---
doc_id: SLD-BIO-072
biomarker_id: iga
name_es: Inmunoglobulina A
name_en: Immunoglobulin A
abbreviation: IgA
sinonimos:
- Inmunoglobulina A
- IgA
- IgA total
- IgA (Inmunoglobulina A)
- Immunoglobulin A
category: Inmunidad
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M4-GA-006
combine_with:
- igg
- igm
- anti_ttg_iga
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

# IgA (Inmunoglobulina A)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-072. IgA. Categoría: Inmunidad. Tipo: measured_analyte. Tier 3.

## B. Definición

Principal inmunoglobulina de las mucosas (respiratoria, digestiva). Su medición sérica total es relevante tanto para evaluar inmunodeficiencia como, de forma crítica, para interpretar correctamente el cribado celíaco por Anti-tTG IgA (ver `anti_ttg_iga.md`) — la deficiencia selectiva de IgA (la inmunodeficiencia primaria más común, ~1/500 personas) invalida ese cribado.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: nefelometría o inmunoturbidimetría.

### Condiciones de toma de muestra

No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión — ABIM Laboratory Reference Ranges)

- **Laboratory reference interval:** **90-325 mg/dL** (adultos).
- **URL fuente:** https://www.abim.org/media/e2wdwdqu/laboratory-reference-ranges.pdf — verificado esta sesión (ago-2026). Nivel de evidencia: tabla de referencia usada para certificación de medicina interna en EE.UU. (American Board of Internal Medicine), ampliamente reconocida como estándar educativo/clínico.

## E. Interpretación

- **Muy baja/indetectable:** deficiencia selectiva de IgA — la inmunodeficiencia primaria más común, con frecuencia asintomática pero relevante porque **invalida el cribado celíaco por Anti-tTG IgA** (falsos negativos).
- **Elevada:** infecciones crónicas de mucosas, cirrosis hepática, enfermedades autoinmunes — inespecífica.

## F. Contexto del paciente y confusores

### Contexto del paciente

Antecedente de infecciones respiratorias/digestivas recurrentes, síntomas digestivos crónicos (si se solicita en contexto celíaco), antecedente familiar de deficiencia de IgA.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: **Anti-tTG IgA (obligatorio verificar IgA total antes de confiar en un Anti-tTG IgA negativo)**, IgG, IgM.
- `pattern_examples`: IgA muy baja + Anti-tTG IgA negativo = resultado del cribado celíaco NO confiable, requiere Anti-tTG IgG o Anti-DGP en su lugar.
- `cannot_conclude`: ausencia de enfermedad celíaca basada en Anti-tTG IgA si la IgA total está muy baja.

## H. Tendencias

### Tendencias temporales

Estable en el tiempo salvo cambios en el estado inmunológico general.

## I. Prevención

### Contexto preventivo

Verificación de rutina antes de confiar en cribado celíaco por Anti-tTG IgA.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Anti-tTG IgG o Anti-DGP si IgA total es muy baja y se sospecha enfermedad celíaca.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No confiar en un Anti-tTG IgA negativo sin verificar IgA total normal. Escalar ante deficiencia de IgA con infecciones recurrentes significativas.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (ABIM Laboratory Reference Ranges).
- Fuente verificada esta sesión: ver URL en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "IgA baja, verificar antes de confiar en cribado celíaco por Anti-tTG IgA".
- **prohibited_inferences:** descartar enfermedad celíaca basándose en Anti-tTG IgA sin verificar IgA total.
- **uncertainty_notes:** la deficiencia selectiva de IgA es frecuentemente asintomática — su relevancia principal en este catálogo es como prerequisito de interpretación de otro biomarcador.
- **professional_review:** deficiencia de IgA con infecciones recurrentes significativas.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - immunology
  - celiac_screening
  - tier_3
  - saludly_brain_v1
use_when:
  - "verificando validez de cribado celíaco por Anti-tTG IgA"
  - "sospecha de inmunodeficiencia"
combine_with: [igg, igm, anti_ttg_iga]
do_not_use_alone:
  - "descartar enfermedad celíaca sin considerar el estado de IgA total"
do_not_conclude:
  - "ausencia de celíaca por Anti-tTG IgA negativo sin verificar IgA total"
escalate_when:
  - "deficiencia de IgA con infecciones recurrentes significativas"
```
