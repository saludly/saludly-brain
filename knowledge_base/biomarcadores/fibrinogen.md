---
doc_id: SLD-BIO-075
biomarker_id: fibrinogen
name_es: Fibrinógeno
name_en: Fibrinogen
abbreviation: FIB
sinonimos:
- Fibrinógeno
- FIB
- Fibrinogen
category: Inflamación/Coagulación
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Plasma citrato
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-006
combine_with:
- pt
- hs_crp
- esr
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

# Fibrinógeno

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-075. FIB. Categoría: Inflamación/Coagulación. Tipo: measured_analyte. Tier 3 — relevante en contexto de riesgo trombótico/inflamatorio dirigido, no cribado poblacional.

## B. Definición

Proteína plasmática soluble producida por el hígado, precursora de la fibrina en la formación del coágulo. También se comporta como reactante de fase aguda positivo (se eleva con inflamación), lo que la hace doblemente relevante: coagulación y marcador inflamatorio.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa, plasma (tubo de citrato) · Método: ensayo funcional (Clauss) o inmunológico (antigénico). **Muestras hemolizadas o de más de 24h no son aceptables** — factor preanalítico crítico.

### Condiciones de toma de muestra

No requiere ayuno. Estabilidad: refrigerado 24h, congelado hasta 1 mes.

## D. Intervalos y umbrales

### Intervalos y umbrales (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Laboratory reference interval:** **150-400 mg/dL** (rango consolidado de fuentes concordantes: Medscape 150-400, ACP 150-350, RNpedia 203-377).
- **Fibrinógeno antigénico (método inmunológico, ligeramente distinto):** 149-353 mg/dL.
- **URLs fuente:** https://emedicine.medscape.com/article/2085501-overview ; https://annualmeeting.acponline.org/educational-program/reference-ranges ; https://www.rnpedia.com/tools-apps/normal-laboratory-values/ — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevado:** inflamación/infección (reactante de fase aguda), embarazo (fisiológico), tabaquismo, síndrome metabólico, mayor riesgo trombótico relativo.
- **Disminuido:** hepatopatía severa (síntesis reducida), coagulación intravascular diseminada (CID — consumo acelerado), deficiencia congénita (afibrinogenemia, poco frecuente).

## F. Contexto del paciente y confusores

### Contexto del paciente

Embarazo, tabaquismo, proceso inflamatorio/infeccioso activo, hepatopatía conocida, sospecha de CID (contexto clínico grave).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: PT/INR (panel de coagulación, especialmente si se sospecha CID o hepatopatía severa), hs-CRP y VSG (contexto inflamatorio).
- `pattern_examples`: fibrinógeno bajo + PT prolongado + plaquetas bajas = patrón compatible con CID, requiere evaluación urgente; fibrinógeno alto + hs-CRP alta = patrón inflamatorio inespecífico.
- `cannot_conclude`: diagnóstico específico sin el resto del panel de coagulación/inflamación y contexto clínico.

## H. Tendencias

### Tendencias temporales

Se eleva/desciende en el curso de días ante procesos agudos (inflamación o consumo en CID) — relevante para seguimiento en esos contextos específicos, no para cribado longitudinal general.

## I. Prevención

### Contexto preventivo

Utilidad limitada como marcador preventivo aislado — su valor está en contextos clínicos dirigidos (riesgo trombótico, coagulopatía).

## J. Pruebas complementarias

### Pruebas complementarias posibles

PT/INR, plaquetas, hs-CRP, VSG según el contexto sospechado.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No usar como cribado poblacional general. Escalar ante fibrinógeno muy bajo con PT prolongado y plaquetas bajas (patrón de CID, urgencia médica), o hepatopatía severa con síntesis muy reducida.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte, múltiples fuentes clínicas concordantes.
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "fibrinógeno alterado, considerar contexto inflamatorio o de coagulación según el patrón (elevado vs. disminuido)".
- **prohibited_inferences:** diagnóstico de CID o hepatopatía sin el resto del panel de coagulación y contexto clínico.
- **uncertainty_notes:** comportamiento dual (coagulación + reactante de fase aguda) requiere considerar ambos contextos antes de interpretar.
- **professional_review:** patrón sugestivo de CID (fibrinógeno bajo + PT prolongado + plaquetas bajas) — urgencia médica.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - inflammation
  - coagulation
  - tier_3
  - saludly_brain_v1
use_when:
  - "evaluación de riesgo trombótico/inflamatorio, o panel de coagulación dirigido"
combine_with: [pt, hs_crp, esr]
do_not_use_alone:
  - "diagnóstico de CID o hepatopatía sin panel completo"
do_not_conclude:
  - "causa específica sin contexto clínico y panel de coagulación completo"
escalate_when:
  - "patrón sugestivo de CID (urgencia médica)"
```
