---
doc_id: SLD-BIO-038
biomarker_id: ldh
name_es: Lactato Deshidrogenasa
name_en: Lactate Dehydrogenase
abbreviation: LDH
sinonimos:
- LDH
- Lactato deshidrogenasa
- DHL
- Lactato Deshidrogenasa
- LDH (Lactato Deshidrogenasa)
- Lactate Dehydrogenase
category: Metabolismo
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: U/L
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-007
combine_with:
- ck_cpk
- bilirubin_total
- alt
- ast
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

# LDH (Lactato Deshidrogenasa)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-007. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-038. LDH. Categoría: Metabolismo. Tipo: measured_analyte. Tier 3 — muy inespecífico aislado, solo útil en contexto dirigido.

## B. Definición

Enzima presente en prácticamente todos los tejidos (hígado, corazón, músculo, eritrocitos, pulmón, riñón). Esta ubicuidad es precisamente su limitación central: una elevación no indica de qué tejido proviene sin contexto clínico adicional.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método enzimático estandarizado. **Factor preanalítico crítico:** la hemólisis de la muestra (por punción traumática o demora en procesamiento) libera LDH de los eritrocitos, elevando falsamente el resultado — una de las interferencias preanalíticas más frecuentes para este analito.

### Condiciones de toma de muestra

No requiere ayuno. Evitar ejercicio intenso previo (puede elevarlo transitoriamente por origen muscular).

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión — ABIM Laboratory Reference Ranges)

- **Laboratory reference interval:** **80-225 U/L** (adultos).
- **URL fuente:** https://www.abim.org/media/e2wdwdqu/laboratory-reference-ranges.pdf — verificado esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** hemólisis (real o de la muestra — requiere diferenciar), daño hepático, infarto de miocardio (histórico, hoy sustituido por troponina), daño muscular (junto a CK), procesos oncológicos (marcador de recambio celular acelerado, inespecífico), neumonía, embolia pulmonar.

## F. Contexto del paciente y confusores

### Contexto del paciente

Ejercicio reciente, síntomas de hemólisis, antecedente oncológico, síntomas musculares (junto a CK).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: CK/CPK (si se sospecha origen muscular), Bilirrubina total/indirecta (si se sospecha hemólisis), ALT/AST (si se sospecha origen hepático).
- `cannot_conclude`: origen del LDH elevado (qué tejido) sin el contexto clínico y biomarcadores de apoyo específicos de cada sistema.

## H. Tendencias

### Tendencias temporales

En seguimiento oncológico, una tendencia ascendente sostenida puede reflejar progresión de enfermedad — pero LDH nunca es diagnóstica por sí sola en ese contexto, solo un marcador de apoyo.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — su valor es exclusivamente en contexto clínico dirigido.

## J. Pruebas complementarias

### Pruebas complementarias posibles

CK/CPK, Bilirrubina total e indirecta, haptoglobina (no incluida en el catálogo actual) según la sospecha clínica.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar LDH aislada sin contexto clínico específico. Escalar según la causa sospechada del contexto (ej. hemólisis significativa, sospecha oncológica con otros hallazgos).

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (ABIM Laboratory Reference Ranges).
- Fuente verificada esta sesión: ver URL en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "LDH elevada, requiere contexto clínico y biomarcadores de apoyo específicos para orientar el origen (hemólisis, hepático, muscular, oncológico)".
- **prohibited_inferences:** cualquier diagnóstico específico a partir de LDH aislada, incluyendo sugerir cáncer sin contexto clínico y estudios apropiados.
- **uncertainty_notes:** la hemólisis de la muestra es una causa preanalítica muy frecuente de falsa elevación — verificar si el laboratorio reportó hemólisis antes de interpretar.
- **professional_review:** elevación marcada con contexto clínico preocupante (síntomas oncológicos, hemólisis significativa, síntomas cardíacos/pulmonares agudos).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - tissue_damage
  - tier_3
  - saludly_brain_v1
use_when:
  - "sospecha de hemólisis, daño tisular, o seguimiento oncológico"
combine_with: [ck_cpk, bilirubin_total, alt, ast]
do_not_use_alone:
  - "diagnóstico de cualquier condición específica"
do_not_conclude:
  - "cáncer o condición específica sin contexto clínico y estudios apropiados"
escalate_when:
  - "elevación marcada con contexto clínico preocupante"
```
