---
doc_id: SLD-BIO-045
biomarker_id: ck_cpk
name_es: Creatina Quinasa
name_en: Creatine Kinase
abbreviation: CK / CPK
sinonimos:
- CK
- CPK
- Creatina quinasa
- Creatinfosfoquinasa
- Creatina Quinasa
- CK / CPK (Creatina Quinasa)
- CK / CPK
- Creatine Kinase
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
- ldh
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

# CK / CPK (Creatina Quinasa)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-007. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-045. CK/CPK. Categoría: Metabolismo. Tipo: measured_analyte. Tier 3 — relevante con síntomas musculares o uso de estatinas, no cribado general.

## B. Definición

Enzima predominantemente de músculo esquelético (isoenzima CK-MM), con contribución menor de miocardio (CK-MB) y tejido neuronal (CK-BB). Es el marcador de primera línea para sospecha de daño muscular.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método enzimático estandarizado.

### Condiciones de toma de muestra

Evitar ejercicio intenso en las 24-48h previas (eleva CK significativamente incluso en personas sanas). No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente por sexo y etnia (evidencia verificada esta sesión — revisión sistemática mundial, PMC12163646)

- **Límite superior de referencia, hombres:** caucásicos/asiáticos **227-440 U/L**; **individuos de raza negra 520-810 U/L** (significativamente más alto — diferencia bien documentada, no debe interpretarse como patológica sin ajustar por este factor).
- **Límite superior de referencia, mujeres:** caucásicas/asiáticas **135-248 U/L**; raza negra hasta **354 U/L**.
- **URL fuente:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12163646/ ("What Are the Normal Serum Creatine Kinase Values for Skeletal Muscle? A Worldwide Systematic Review") — verificado esta sesión (ago-2026).
- **Nota de variabilidad adicional:** los rangos también varían según el ensayo y la temperatura de referencia usada por el laboratorio — Saludly debe validar con el laboratorio aliado, especialmente el ajuste por etnia (relevante en Colombia por la diversidad étnica de la población).

## E. Interpretación

- **Elevada:** ejercicio intenso reciente (causa más frecuente de elevación leve-moderada en personas sanas), miopatía inducida por estatinas, rabdomiólisis (elevación marcada, orina oscura, urgencia médica), distrofias musculares, hipotiroidismo (puede elevar CK moderadamente), infarto de miocardio (histórico — CK-MB específica, hoy sustituida por troponina).

## F. Contexto del paciente y confusores

### Contexto del paciente

Ejercicio reciente (crítico), etnia (determinante documentado del rango de referencia), uso de estatinas, síntomas musculares (dolor, debilidad, orina oscura), función tiroidea.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: LDH (inespecífico, apoya sospecha de daño tisular), AST (también presente en músculo, ayuda a diferenciar origen hepático de muscular si está elevada de forma proporcional).
- `pattern_examples`: CK muy elevada + orina oscura + síntomas musculares tras ejercicio extremo = sospecha de rabdomiólisis, requiere evaluación urgente (riesgo de daño renal agudo).
- `cannot_conclude`: origen cardíaco vs muscular sin CK-MB específica o troponina.

## H. Tendencias

### Tendencias temporales

Se eleva en 2-12 horas tras daño muscular agudo y puede permanecer elevada varios días — relevante para el seguimiento tras sospecha de rabdomiólisis.

## I. Prevención

### Contexto preventivo

No aplica como cribado general — relevante en seguimiento de terapia con estatinas si hay síntomas musculares.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Función renal (si se sospecha rabdomiólisis, por riesgo de daño renal agudo), función tiroidea si no hay causa evidente.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar sin considerar ejercicio reciente y etnia. Escalar ante CK muy elevada (varias veces el límite superior) con síntomas de rabdomiólisis (orina oscura, dolor muscular severo) — urgencia médica por riesgo renal.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (revisión sistemática mundial, PMC12163646).
- Fuente verificada esta sesión: ver URL en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "CK elevada, considerar ejercicio reciente y etnia antes de interpretar como patológica; si hay síntomas de rabdomiólisis, escalar de inmediato".
- **prohibited_inferences:** diagnóstico de miopatía o infarto sin contexto clínico y pruebas complementarias.
- **uncertainty_notes:** diferencia significativa por etnia (hasta 2x más alto en personas de raza negra) — no aplicar un umbral único sin ajustar.
- **professional_review:** CK muy elevada con síntomas de rabdomiólisis (urgencia por riesgo renal), o síntomas musculares significativos con uso de estatinas.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - muscle_damage
  - tier_3
  - saludly_brain_v1
use_when:
  - "síntomas musculares con uso de estatinas, o sospecha de rabdomiólisis"
combine_with: [ldh, ast]
do_not_use_alone:
  - "diagnóstico de miopatía o evento cardíaco sin pruebas complementarias"
do_not_conclude:
  - "origen cardíaco sin CK-MB o troponina"
escalate_when:
  - "CK muy elevada con síntomas de rabdomiólisis (urgencia por riesgo renal)"
```
