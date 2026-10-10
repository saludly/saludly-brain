---
doc_id: SLD-BIO-046
biomarker_id: creatinine
name_es: Creatinina Sérica
name_en: Serum Creatinine
abbreviation: CREA
sinonimos:
- Creatinina
- Creatinina sérica
- CREA
- Creatinina Sérica
- Serum Creatinine
category: Riñón
subcategory: Función renal
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-NE-001
- COND-M2-NE-A02
- COND-M6-MI-A02
combine_with:
- egfr
- bun
- uacr
- cystatin_c
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Creatinina Sérica

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M2-NE-001, COND-M2-NE-A02, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-046. CREA. Categoría: Riñón. Tipo: **measured_analyte**. Tier 1. Nota de auditoría: separado de eGFR como registro independiente (antes combinados en un solo archivo `creatinine_egfr.md`) — la creatinina es el analito medido; eGFR es el parámetro calculado que se deriva de ella (ver `egfr.md`).

## B. Definición

Producto de degradación muscular (de la creatina fosfato), filtrado libremente por el glomérulo renal. Es el analito medido que sirve de variable de entrada principal para calcular eGFR.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

- **Examen del que se obtiene:** Química sanguínea básica (BMP) o panel metabólico completo (CMP).
- **Muestra:** sangre venosa (suero o plasma con heparina de litio).
- **Método:** enzimático (preferido, menos interferencias) o Jaffe cinético (más antiguo, más interferencias — Saludly debe registrar cuál usa el laboratorio aliado).
- **Unidad:** mg/dL (alt: µmol/L — factor de conversión ×88.4).

### Condiciones de toma de muestra

- **Ayuno:** no requiere.
- **Horario:** sin restricción horaria específica.
- **Sexo:** relevante para interpretación (valores de referencia distintos hombre/mujer por diferencia de masa muscular), no para la toma en sí.
- **Ciclo menstrual:** no aplica.
- **Factores preanalíticos relevantes:** alto consumo de carne roja reciente (24-48h previas) puede elevarlo transitoriamente; ejercicio intenso previo a la toma puede elevarlo; masa muscular atípica (atletas, sarcopenia, amputación) altera su interpretación sin reflejar cambio real en función renal.

### Resultado y tipo de dato

- **Tipo:** medido directamente (no calculado). Numérico continuo.
- **Limitación de método:** el método de Jaffe tiene mayor interferencia por bilirrubina, cetonas y algunos fármacos que el método enzimático — Saludly debe registrar el método del laboratorio aliado.

## D. Intervalos y umbrales

```
lab_reference_interval: depende del laboratorio/método; valores de referencia distintos por sexo (mayor masa muscular en hombres → creatinina basal más alta)
```
⚠️ **PENDIENTE de verificación:** valor numérico exacto del rango de referencia por sexo — no se fija sin confirmar con fuente primaria específica.

## E. Interpretación

- **Elevada:** deshidratación, dieta alta en proteína, ejercicio intenso, AINEs, reducción real de función renal (ver `egfr.md` para la estimación calculada).
- **Disminuida:** baja masa muscular, embarazo (aumento fisiológico de filtración), desnutrición severa.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: edad, sexo, masa muscular aproximada/nivel de actividad física, medicamentos nefrotóxicos (AINEs, algunos antibióticos), hidratación reciente, dieta proteica reciente.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: **eGFR (calculado a partir de este valor — ver `egfr.md`)**, BUN, Cistatina C.
- `cannot_conclude`: función renal real sin calcular eGFR (la creatinina aislada, sin ajustar por edad/sexo, no equivale a función renal).

## H. Tendencias

### Tendencias temporales

Un aumento sostenido entre controles, incluso dentro de rango "normal", es más relevante que un valor puntual — ver seguimiento longitudinal detallado en `egfr.md`.

## I. Prevención

### Contexto preventivo

Parte del panel preventivo básico — su valor principal es como variable de entrada de eGFR, no como umbral aislado.

## J. Pruebas complementarias

### Pruebas complementarias posibles

BUN, Cistatina C (en extremos de masa muscular), UACR (requiere módulo de orina, no disponible en Saludly v1).

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar la creatinina aislada sin calcular eGFR. Escalar ante eGFR <60 sostenido o caída rápida (ver `egfr.md` para los umbrales exactos).

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento de fisiología renal estándar, ampliamente reproducido.
- **Fecha de actualización:** 2026-09.
- **Fuente complementaria:** KDIGO 2024 Clinical Practice Guideline for CKD (aplica al conjunto creatinina+eGFR). https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf — verificado sesión previa.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "creatinina alterada, calcular eGFR para estimar función renal real antes de cualquier interpretación".
- **prohibited_inferences:** diagnóstico de función renal a partir de creatinina sin calcular eGFR.
- **uncertainty_notes:** interpretación fuertemente dependiente de masa muscular — atletas y personas con sarcopenia requieren ajuste.
- **professional_review:** ver `egfr.md`.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - renal
  - kidney_function
  - measured_analyte
  - tier_1
  - saludly_brain_v1

use_when:
  - "calculando eGFR"
  - "evaluando función renal básica"

combine_with: [egfr, bun, uacr, cystatin_c]

do_not_use_alone:
  - "cualquier conclusión de función renal sin calcular eGFR"

do_not_conclude:
  - "función renal normal o alterada sin eGFR calculado"

escalate_when:
  - "ver egfr.md para umbrales exactos de escalamiento"
```
