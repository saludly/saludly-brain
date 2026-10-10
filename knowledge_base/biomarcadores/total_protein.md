---
doc_id: SLD-BIO-037
biomarker_id: total_protein
name_es: Proteínas totales
name_en: Total Protein
abbreviation: PT / TP
sinonimos:
- Proteínas totales
- PT séricas
- PT / TP
- Total Protein
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: g/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-NE-005
- SEG-009
- COND-M6-MI-002
combine_with:
- albumin
- globulin
- ag_ratio
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Proteínas totales

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M2-NE-005, SEG-009. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-037. PT/TP. Categoría: Metabolismo. Tipo: analito medido (variable de entrada para el cálculo de Globulinas). Tier 2.

## B. Definición

Suma de todas las proteínas circulantes en plasma, predominantemente albúmina y globulinas (inmunoglobulinas, proteínas de transporte, factores de coagulación, entre otras). Por sí sola es poco específica — su valor principal en el panel de Saludly es servir de base para calcular Globulinas (Proteínas totales − Albúmina).

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico (biuret, estándar). Unidad: g/dL. No requiere ayuno. Factor preanalítico: hemoconcentración/hemodilución (torniquete prolongado, postura).

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal **6.4-8.3 g/dL** (algunas fuentes 6.0-7.8 g/dL — variación menor entre laboratorios/métodos).
- **URL fuente:** ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf), NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y Medscape Lab Values Normal Adult (https://emedicine.medscape.com/article/2172316-overview) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevadas:** deshidratación (concentración), procesos con aumento de gammaglobulinas (inflamación crónica, gammapatías monoclonales — requiere electroforesis de proteínas para precisar, fuera del alcance actual de Saludly).
- **Disminuidas:** desnutrición, hepatopatía (reducción de síntesis de albúmina), síndrome nefrótico/enteropatía perdedora de proteínas (pérdida), sobrehidratación (dilución).
- Sin desglose en Albúmina y Globulinas, el valor total tiene interpretación clínica limitada.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: estado de hidratación, estado nutricional, función hepática y renal conocidas.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Albúmina (obligatorio, para poder calcular Globulinas), y por extensión, relación A/G.
- `cannot_conclude`: nada específico sin el desglose Albúmina/Globulinas — proteínas totales aisladas son el biomarcador de menor especificidad interpretativa del catálogo.

## H. Tendencias

### Tendencias temporales

Cambia lentamente salvo por hidratación aguda — una tendencia sostenida es más relevante que un valor puntual.

## I. Prevención

Su valor preventivo real está en habilitar el cálculo de Globulinas y la relación A/G, no en sí misma.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Albúmina (si no se solicitó junta — debería pedirse siempre en conjunto); electroforesis de proteínas si hay sospecha de gammapatía monoclonal.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte de un panel metabólico ampliado — sin valor diagnóstico independiente aislado.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento bioquímico estándar.
- **Fuente:** ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf), NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y Medscape Lab Values Normal Adult (https://emedicine.medscape.com/article/2172316-overview) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "proteínas totales alteradas, requiere desglose en Albúmina y Globulinas para interpretación significativa".
- **prohibited_inferences:** cualquier diagnóstico específico a partir de proteínas totales aisladas.
- **uncertainty_notes:** biomarcador de bajo valor interpretativo sin su desglose — Saludly debe siempre presentar Albúmina y Globulinas calculadas junto a este valor, nunca aislado.
- **professional_review:** valores marcadamente alterados, especialmente sin explicación por hidratación.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - protein_panel
  - tier_2
  - saludly_brain_v1

use_when:
  - "calculando globulinas y relación A/G"
  - "evaluando estado nutricional o función hepática/renal junto a albúmina"

combine_with: [albumin, globulin, ag_ratio]

do_not_use_alone:
  - "cualquier interpretación clínica sin desglose en albúmina/globulinas"

do_not_conclude:
  - "diagnóstico específico a partir del valor total aislado"

escalate_when:
  - "valor marcadamente alterado sin explicación por hidratación"
```
