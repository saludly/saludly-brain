---
doc_id: SLD-BIO-052
biomarker_id: ast
name_es: AST (Aspartato Aminotransferasa)
name_en: AST (Aspartate Aminotransferase)
abbreviation: AST
sinonimos:
- AST
- TGO
- ASAT
- Aspartato aminotransferasa
- Transaminasa oxalacética
- AST (Aspartato Aminotransferasa)
- AST (Aspartate Aminotransferase)
category: hepatology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: U/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M4-GA-002
combine_with:
- alt
- ggt
- alp
- ck_cpk
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# AST (Aspartato Aminotransferasa)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-052. AST/TGO. Categoría: Hepatología. Tipo: analito medido. Tier 1.

## B. Definición

Enzima presente en hígado, pero también en músculo esquelético, corazón, riñón y eritrocitos — mucho menos específica de hígado que ALT. Se interpreta siempre junto a ALT.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma). Método enzimático estandarizado (IFCC). Unidad: UI/L. Variables preanalíticas: ejercicio intenso reciente (origen muscular), hemólisis.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold:** se interpreta en conjunto con ALT mediante la **relación AST/ALT**, no como valor aislado — un ratio ≥1.4 se ha asociado en estudios de cohorte con mayor mortalidad por todas las causas en pacientes con enfermedad coronaria estable (evidencia observacional, no causal).
- **Fuente verificada esta sesión:** estudio de cohorte retrospectivo, PMC9163143 — nivel de evidencia observacional/cohorte, no guía de sociedad médica.

## E. Interpretación

**Elevado (junto a ALT):**
- AST > ALT (ratio invertido) sugiere daño hepático alcohólico o cirrosis ya establecida.
- ALT > AST sugiere origen hepatocelular no alcohólico (más compatible con NAFLD).
- Elevación aislada de AST sin ALT elevado sugiere origen no hepático (muscular, cardíaco).

**Disminuido:** sin significado clínico relevante de forma aislada.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: ejercicio físico reciente (origen muscular), consumo de alcohol, medicamentos, antecedente cardíaco (CK-CPK ayuda a diferenciar origen).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ALT (obligatorio, para calcular el ratio), GGT, CK/CPK (para descartar origen muscular).
- `pattern_examples`: AST/ALT ≥1.4 en contexto de enfermedad coronaria — asociación observacional con mortalidad, no diagnóstica per se.
- `cannot_conclude`: origen del daño (hepático vs muscular vs cardíaco) sin CK/CPK y contexto clínico.

## H. Tendencias

### Tendencias temporales

Igual racional que ALT — persistencia sostenida es más relevante que un valor puntual. `clinical_significance` del ratio AST/ALT se establece mejor con mediciones repetidas, no un solo par de valores.

## I. Prevención

Mismas acciones que ALT: manejo de peso, reducción de alcohol, actividad física, revisión de medicamentos.

## J. Pruebas complementarias

### Pruebas complementarias posibles

CK/CPK si se sospecha origen muscular; ALT si no fue solicitada junto; panel de hepatitis viral según contexto.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

AST aislado no es diagnóstico de nada específico — su valor está en la combinación con ALT (ratio) y en el contexto clínico.

## L. Evidencia

### Evidencia científica

- **Cohort study (evidencia observacional):** "Elevated AST/ALT ratio is associated with all-cause mortality in patients with stable coronary artery disease." PMC9163143. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9163143/ — verificado esta sesión.
- **Guideline complementaria (misma que ALT):** ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries, 2017 — https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver
- **Nota de calidad de evidencia:** el hallazgo del ratio AST/ALT ≥1.4 y mortalidad proviene de un estudio observacional en una población específica (enfermedad coronaria estable) — no debe generalizarse como umbral universal de riesgo sin más validación.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "patrón de transaminasas compatible con posible origen hepatocelular/muscular, requiere ALT y contexto para precisar".
- **prohibited_inferences:** diagnóstico de cirrosis, daño hepático alcohólico o evento cardíaco a partir de AST aislado.
- **uncertainty_notes:** el ratio AST/ALT como predictor de mortalidad proviene de evidencia observacional en una población específica, no de un ensayo controlado ni de una guía de sociedad médica.
- **professional_review:** elevación marcada, ratio AST/ALT invertido persistente, o síntomas hepáticos/musculares/cardíacos concurrentes.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - liver_enzymes
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando función/daño hepático junto con ALT"
  - "evaluando panel metabólico básico"

combine_with: [alt, ggt, alp, ck_cpk]

do_not_use_alone:
  - "diagnóstico de enfermedad hepática, muscular o cardíaca"

do_not_conclude:
  - "daño hepático alcohólico confirmado"
  - "cirrosis confirmada"
  - "evento cardíaco a partir de AST aislado"

escalate_when:
  - "ratio AST/ALT invertido persistente"
  - "elevación marcada sin causa muscular evidente"
  - "síntomas hepáticos o cardíacos concurrentes"
```
