---
doc_id: SLD-BIO-032
biomarker_id: chloride
name_es: Cloro
name_en: Chloride
abbreviation: Cl-
sinonimos:
- Cloro
- Cl
- Cloruro
- Cl-
- Chloride
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mmol/L
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-008
combine_with:
- sodium
- potassium
- bicarbonate
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

# Cloro (Cl-)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-008. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-032. Cl-. Categoría: Metabolismo. Tipo: analito medido. Tier 3 — rara vez altera decisiones sin el resto del panel electrolítico ya alterado.

## B. Definición

Principal anión extracelular, se mueve en paralelo con el sodio en la mayoría de las condiciones (por eso rara vez se interpreta de forma aislada). Su relación con el bicarbonato es relevante para evaluar el equilibrio ácido-base.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método: electrodo ion-selectivo. Unidad: mEq/L. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal **96-106 mEq/L** (algunas fuentes 95-105).
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevado:** generalmente sigue al sodio (deshidratación), o puede indicar acidosis metabólica hiperclorémica (ej. diarrea, ciertos tipos de acidosis tubular renal).
- **Disminuido:** vómito prolongado (pérdida de ácido clorhídrico gástrico), uso de diuréticos, alcalosis metabólica.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: vómito/diarrea reciente, medicamentos diuréticos, estado de hidratación.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Sodio (obligatorio — se mueven en paralelo en la mayoría de casos), Bicarbonato (para evaluar el "anion gap" y equilibrio ácido-base — cálculo no incluido explícitamente en el catálogo actual de Saludly).
- `cannot_conclude`: causa específica de un trastorno ácido-base sin el panel electrolítico completo.

## H. Tendencias

### Tendencias temporales

Sigue el mismo patrón que sodio — trastornos agudos, no de seguimiento longitudinal lento.

## I. Prevención

Utilidad preventiva mínima de forma aislada — parte del panel electrolítico de rutina.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Panel electrolítico completo si no se solicitó junto.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del panel metabólico básico — sin valor diagnóstico independiente aislado.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento fisiológico estándar.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "cloro alterado, interpretar junto a sodio y bicarbonato para evaluar contexto de hidratación o equilibrio ácido-base".
- **prohibited_inferences:** diagnóstico de un trastorno ácido-base específico a partir de cloro aislado.
- **uncertainty_notes:** biomarcador de bajo valor interpretativo aislado — casi siempre se mueve junto a sodio.
- **professional_review:** alteración marcada combinada con el resto del panel electrolítico.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - electrolytes
  - metabolism
  - tier_3
  - saludly_brain_v1

use_when:
  - "evaluando panel electrolítico completo"

combine_with: [sodium, potassium, bicarbonate]

do_not_use_alone:
  - "cualquier interpretación sin sodio y bicarbonato concurrentes"

do_not_conclude:
  - "trastorno ácido-base específico a partir de cloro aislado"

escalate_when:
  - "alteración marcada combinada con el resto del panel electrolítico"
```
