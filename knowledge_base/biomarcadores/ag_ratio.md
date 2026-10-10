---
doc_id: SLD-BIO-028
biomarker_id: ag_ratio
name_es: Relación Albúmina/Globulina
name_en: Albumin/Globulin Ratio
abbreviation: A/G
sinonimos:
- Relación albúmina/globulina
- Relación A/G
- Relación Albúmina/Globulina
- Relación Albúmina/Globulina (A/G ratio)
- A/G
- Albumin/Globulin Ratio
category: metabolism_electrolytes
parameter_type: derived_ratio
tipo_resultado: numérico
unidad_canonica: sin unidad
specimen: No aplica (calculado)
nivel_catalogo: solo valor y rango
panel: calculado
sexo: ambos
alimenta:
- SEG-009
- COND-M6-MI-002
combine_with:
- albumin
- globulin
- total_protein
formula: A/G = Albúmina ÷ Globulinas
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

# Relación Albúmina/Globulina (A/G)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-009. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-028. A/G. Categoría: Metabolismo. Tipo: **relación derivada** (segundo orden — depende de un valor ya calculado). Tier 3. Nota de auditoría: nuevo, incorporado para reemplazar el espacio liberado por la eliminación de "Apo(a)" redundante en la primera auditoría.

## B. Definición

Cociente entre Albúmina (medida) y Globulinas (calculada). Un valor bajo (globulinas relativamente altas respecto a albúmina) orienta hacia procesos inflamatorios crónicos, autoinmunes o gammapatías; un valor alto orienta hacia pérdida o síntesis reducida de globulinas (poco frecuente como hallazgo aislado relevante).

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio — relación derivada de segundo orden)

- **Fórmula:** A/G = Albúmina ÷ Globulinas (donde Globulinas = Proteínas totales − Albúmina).
- **Variables necesarias:** Albúmina (medida), Proteínas totales (medida) — Globulinas se calcula como paso intermedio.
- **Propagación de incertidumbre:** al depender de un cálculo intermedio (Globulinas), cualquier imprecisión en la medición de Albúmina o Proteínas totales se amplifica en el ratio final — Saludly debe tratar este valor con menor confianza puntual que un analito medido directamente.
- **Cuándo NO debe calcularse:** si falta Albúmina o Proteínas totales.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende de las variables de entrada — sin umbral universal fijo verificado en esta sesión.

## E. Interpretación

- **Bajo (invertido, <1 aproximadamente, valor exacto por verificar):** sugiere aumento relativo de globulinas — inflamación crónica, enfermedad autoinmune, gammapatía monoclonal, cirrosis (donde además hay síntesis reducida de albúmina).
- **Alto:** poco frecuente como hallazgo aislado relevante; puede verse en estados de pérdida selectiva de globulinas.

## F. Contexto del paciente y confusores

### Contexto del paciente

Los mismos que Albúmina y Globulinas: función hepática, estado inflamatorio/autoinmune, estado nutricional.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Albúmina, Globulinas, Proteínas totales (las tres variables involucradas en su cálculo).
- `cannot_conclude`: diagnóstico específico sin electroforesis de proteínas cuando el ratio está alterado.

## H. Tendencias

### Tendencias temporales

Cambios lentos, relevantes principalmente en seguimiento de enfermedad hepática o inflamatoria crónica ya conocida.

## I. Prevención

Utilidad preventiva limitada como marcador aislado — más útil como señal de "profundizar con electroforesis" que como objetivo de intervención en sí mismo.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Electroforesis de proteínas si el ratio está marcadamente alterado sin explicación evidente.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstico — es una señal de orientación hacia procesos hepáticos, inflamatorios o autoinmunes que requieren estudio dirigido.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento bioquímico estándar; cálculo aritmético establecido sin controversia metodológica.
- **Clinical decision threshold (derivado de componentes ya verificados esta sesión):** con Albúmina 3.5-5.5 g/dL y Globulinas ~2.3-3.5 g/dL (ver `albumin.md`, `globulin.md`), el ratio A/G normal calculado es aproximadamente **1.1-2.2** (ampliamente citado en la literatura de química clínica como >1.0 = normal, <1.0 = invertido/patológico). Un ratio <1.0 (globulinas superando a albúmina) es el umbral clásico de alerta.
- **URL fuente:** derivado de fuentes ya citadas en `albumin.md`/`globulin.md` (ACCP, NBME, Medscape) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "relación A/G invertida sugiere aumento relativo de globulinas, considerar electroforesis de proteínas si no hay explicación evidente".
- **prohibited_inferences:** diagnóstico de cirrosis, gammapatía o enfermedad autoinmune sin estudios adicionales.
- **uncertainty_notes:** al ser un cálculo de segundo orden (depende de Globulinas, que a su vez es calculada), su precisión puntual es menor que la de un analito medido — comunicar con esa calibración de confianza.
- **professional_review:** ratio marcadamente invertido sin explicación evidente por deshidratación o proceso agudo conocido.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - protein_panel
  - derived_ratio
  - tier_3
  - saludly_brain_v1

use_when:
  - "screening inicial de posible proceso hepático, inflamatorio crónico o autoinmune"

combine_with: [albumin, globulin, total_protein]

do_not_use_alone:
  - "diagnóstico de cirrosis, gammapatía o enfermedad autoinmune"

do_not_conclude:
  - "causa específica sin electroforesis de proteínas"

escalate_when:
  - "ratio marcadamente invertido sin explicación evidente"
```
