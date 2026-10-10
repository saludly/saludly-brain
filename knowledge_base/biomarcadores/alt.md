---
doc_id: SLD-BIO-051
biomarker_id: alt
name_es: ALT (Alanina Aminotransferasa)
name_en: ALT (Alanine Aminotransferase)
abbreviation: ALT
sinonimos:
- ALT
- TGP
- ALAT
- Alanina aminotransferasa
- Transaminasa pirúvica
- ALT (Alanina Aminotransferasa)
- ALT (Alanine Aminotransferase)
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
- ast
- ggt
- alp
- bilirubin_total
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Entre el valor sano de la ACG (33 UI/L hombres, 25 mujeres) y el límite del laboratorio: limítrofe; por encima del laboratorio: alto (COND-M4-GA-002).'
---

# ALT (Alanina Aminotransferasa)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Entre el valor sano de la ACG (33 UI/L hombres, 25 mujeres) y el límite del laboratorio: limítrofe; por encima del laboratorio: alto (COND-M4-GA-002).
- Reglas que usan esta ficha: COND-M4-GA-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-051. ALT/TGP. Categoría: Hepatología. Tipo: analito medido. Tier 1 (panel preventivo básico).

## B. Definición

Enzima predominantemente hepatocelular (mucho más específica de hígado que AST). Su elevación refleja daño o inflamación de los hepatocitos. Es, junto a AST, el marcador de primera línea para cribado de enfermedad hepática.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma). Método enzimático estandarizado (IFCC). Unidad: UI/L. No requiere ayuno estricto, aunque se recomienda por consistencia con el resto del panel metabólico. Variable preanalítica relevante: ejercicio intenso reciente puede elevar transaminasas transitoriamente.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente

- **Laboratory reference interval:** depende del laboratorio/método; los límites superiores de laboratorio típicos han sido históricamente más altos (~40-56 UI/L) de lo que la evidencia clínica reciente considera "verdaderamente normal".
- **Clinical decision threshold (evidencia primaria verificada esta sesión):** ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries (Kwo, Cohen, Lim, *Am J Gastroenterol* 2017) establece que un ALT verdaderamente normal está entre **29-33 UI/L en hombres y 19-25 UI/L en mujeres**, y que valores por encima deben evaluarse — es decir, el umbral clínico es más bajo que el umbral de referencia tradicional del laboratorio.
- **Screening threshold:** no existe un programa de cribado poblacional formal tipo USPSTF para ALT en población general asintomática; su inclusión en Tier 1 responde a su bajo costo/alta disponibilidad dentro del panel metabólico básico, no a una recomendación de cribado poblacional formal verificada.
- **URL fuente:** https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver — verificado esta sesión (ago-2026).

## E. Interpretación

**Elevado:**
- Causas frecuentes: hígado graso no alcohólico (NAFLD/MASLD) — la causa más común en población asintomática; consumo de alcohol; hepatitis viral (a menudo silente); medicamentos/hepatotóxicos; síndrome metabólico.
- Causas preanalíticas: ejercicio intenso reciente, hemólisis de la muestra.

**Disminuido:**
- En general no tiene significado clínico relevante de forma aislada.

**Dentro del intervalo:**
- Un ALT "normal" según el rango de laboratorio tradicional NO descarta enfermedad hepática temprana — la evidencia ACG 2017 muestra que usar el umbral clínico más bajo (29-33 U/L hombres, 19-25 U/L mujeres) mejora la detección de NAFLD en personas asintomáticas. Esto es clínicamente relevante para Saludly: **no comunicar "ALT normal = hígado sano"** sin matizar.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: IMC/composición corporal, consumo de alcohol, medicamentos hepatotóxicos, actividad física reciente, factores de riesgo metabólico (diabetes, dislipidemia, hipertensión — asociados a NAFLD).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: AST, GGT, Fosfatasa alcalina, Bilirrubina total.
- `pattern_examples`: ALT >> AST sugiere origen hepatocelular (más específico de NAFLD/hepatitis); AST > ALT (ratio invertido) puede sugerir daño alcohólico o cirrosis ya establecida.
- `conflicting_patterns`: ejercicio físico intenso reciente puede simular un patrón de daño hepatocelular leve sin serlo.
- `cannot_conclude`: tipo específico de hepatopatía (NAFLD vs viral vs autoinmune vs medicamentosa) sin estudios adicionales dirigidos.

## H. Tendencias

### Tendencias temporales

Valor aislado tiene menor peso que la persistencia: la guía ACG 2017 y evidencia posterior señalan que la elevación **persistente por 6-12 meses** es el criterio operativo para requerir evaluación comprehensiva (no un solo valor puntual). `analytical_variation`: baja con métodos enzimáticos estandarizados. `clinical_significance`: la tendencia ascendente sostenida es más relevante que una fluctuación aislada.

## I. Prevención

Acciones razonablemente relacionadas: manejo de peso, reducción de consumo de alcohol, actividad física regular, revisión de medicamentos/suplementos hepatotóxicos con un profesional.

## J. Pruebas complementarias

### Pruebas complementarias posibles

`possible_follow_up_tests`: AST, GGT, panel de hepatitis viral (si hay factores de riesgo), perfil metabólico completo (si patrón compatible con NAFLD). Lenguaje correcto: "considerar evaluación adicional según contexto clínico" — nunca automatizado por un solo valor.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

ALT es una prueba de detección/cribado de daño hepatocelular, no diagnóstica de una condición específica. Un ALT elevado no equivale a "tiene hígado graso" ni a "tiene hepatitis" — activa evaluación adicional dirigida.

## L. Evidencia

### Evidencia científica

- **Guideline (fuerte):** Kwo PY, Cohen SM, Lim JK. "ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries." *Am J Gastroenterol.* 2017. DOI/URL: https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver. Verificado esta sesión.
- Respalda: umbrales clínicos de "ALT verdaderamente normal", asociación con mortalidad relacionada a hígado, recomendación de evaluación de causas (NAFLD, alcohol, viral, medicamentosa, autoinmune, hemocromatosis, Wilson, déficit de alfa-1-antitripsina).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "patrón compatible con posible daño hepatocelular, considerando umbral clínico más estricto que el rango de laboratorio tradicional".
- **prohibited_inferences:** "tiene hígado graso", "tiene hepatitis", cualquier diagnóstico específico de causa sin estudios dirigidos.
- **uncertainty_notes:** un ALT "normal" por rango de laboratorio no descarta enfermedad hepática temprana según evidencia ACG — esto debe comunicarse, no ocultarse por simplicidad de UX.
- **professional_review:** elevación persistente >6-12 meses, o cualquier elevación marcada (>3x el límite superior clínico), o síntomas hepáticos concurrentes.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - liver_enzymes
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando función/daño hepático"
  - "evaluando panel metabólico básico"
  - "explorando causas de fatiga o síntomas inespecíficos con sospecha hepática"

combine_with: [ast, ggt, alp, bilirubin_total]

do_not_use_alone:
  - "diagnóstico de enfermedad hepática específica"
  - "descartar enfermedad hepática solo por estar en rango de laboratorio tradicional"

do_not_conclude:
  - "tiene hígado graso / NAFLD confirmado"
  - "tiene hepatitis"
  - "hígado sano únicamente por ALT en rango de laboratorio"

escalate_when:
  - "elevación persistente 6-12 meses"
  - "elevación marcada (>3x umbral clínico)"
  - "síntomas hepáticos concurrentes (ictericia, dolor en hipocondrio derecho, coluria)"
```
