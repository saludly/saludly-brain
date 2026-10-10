---
doc_id: SLD-BIO-025
biomarker_id: globulin
name_es: Globulinas
name_en: Globulins
abbreviation: GLOB
sinonimos:
- Globulinas
- GLOB
- Globulins
category: metabolism_electrolytes
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: g/dL
specimen: No aplica (calculado)
nivel_catalogo: solo valor y rango
panel: calculado
sexo: ambos
alimenta:
- SEG-009
- COND-M6-MI-002
combine_with:
- total_protein
- albumin
- ag_ratio
- iga
- igg
- igm
formula: Globulinas = Proteínas totales − Albúmina
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

# Globulinas (calculado)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-009. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-025. GLOB. Categoría: Metabolismo. Tipo: **parámetro calculado**. Tier 3 — valor limitado sin electroforesis de proteínas complementaria.

## B. Definición

Fracción proteica plasmática que agrupa inmunoglobulinas, proteínas de transporte y factores de coagulación, entre otras — todo lo que no es albúmina. Es un cálculo grueso: distintas proteínas con funciones muy diferentes se agrupan en un solo número.

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio para parámetro calculado)

- **Fórmula:** Globulinas = Proteínas totales − Albúmina.
- **Variables necesarias:** Proteínas totales, Albúmina (ambas medidas).
- **Cuándo NO debe calcularse:** si falta cualquiera de las dos variables de entrada.
- **Limitación principal:** al ser un cálculo por diferencia, agrupa fracciones proteicas muy heterogéneas (alfa, beta y gamma globulinas) en un solo valor — no permite distinguir, por ejemplo, un aumento de gammaglobulinas (gammapatía) de un aumento de alfa-1/alfa-2 (proceso inflamatorio agudo) sin electroforesis de proteínas, que **no está en el alcance actual de Saludly v1**.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende de las dos variables de entrada, sin un umbral propio independiente.

## E. Interpretación

- **Elevadas:** inflamación crónica, infección crónica, enfermedad autoinmune, gammapatía monoclonal (requiere electroforesis para confirmar).
- **Disminuidas:** inmunodeficiencia, pérdida de proteínas (renal/digestiva), síntesis hepática reducida.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: infección/inflamación crónica conocida, antecedente autoinmune, función hepática/renal.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Albúmina, Relación A/G (calculada a partir de este valor), inmunoglobulinas (IgA/IgG/IgM) si están disponibles.
- `cannot_conclude`: causa específica (gammapatía vs inflamación vs autoinmune) sin electroforesis de proteínas.

## H. Tendencias

### Tendencias temporales

Cambios lentos salvo procesos agudos — relevante en seguimiento de enfermedad crónica ya conocida.

## I. Prevención

Utilidad preventiva limitada de forma aislada — su rol principal es habilitar la relación A/G.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Electroforesis de proteínas si la relación A/G está alterada de forma inexplicada; inmunoglobulinas específicas (IgA/IgG/IgM) si hay sospecha de proceso inmunológico.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstico de ninguna condición específica — es un valor grueso que orienta si se necesita electroforesis de proteínas.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento bioquímico estándar, cálculo aritmético directo sin controversia metodológica.
- **Fuente:** derivado de Proteínas totales (6.4-8.3 g/dL) menos Albúmina (3.5-5.5 g/dL) — rango normal calculado de Globulinas aproximadamente **2.3-3.5 g/dL** según fuente NBME. ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf), NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y Medscape Lab Values Normal Adult (https://emedicine.medscape.com/article/2172316-overview) — verificado esta sesión (ago-2026)

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "globulinas alteradas, considerar relación A/G y, si está alterada de forma inexplicada, sugerir electroforesis de proteínas".
- **prohibited_inferences:** diagnóstico de gammapatía monoclonal o proceso autoinmune sin electroforesis de proteínas.
- **uncertainty_notes:** valor grueso que agrupa fracciones proteicas heterogéneas — baja especificidad diagnóstica aislada.
- **professional_review:** relación A/G marcadamente alterada, especialmente si es invertida (Globulinas > Albúmina de forma marcada).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - protein_panel
  - calculated_parameter
  - tier_3
  - saludly_brain_v1

use_when:
  - "evaluando relación A/G"
  - "sospecha de proceso inflamatorio crónico, autoinmune o gammapatía"

combine_with: [total_protein, albumin, ag_ratio, iga, igg, igm]

do_not_use_alone:
  - "diagnóstico de gammapatía o proceso autoinmune"

do_not_conclude:
  - "causa específica sin electroforesis de proteínas"

escalate_when:
  - "relación A/G marcadamente invertida"
```
