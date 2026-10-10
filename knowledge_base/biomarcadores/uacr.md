---
doc_id: SLD-BIO-065
biomarker_id: uacr
name_es: UACR
name_en: Urine Albumin-to-Creatinine Ratio
abbreviation: UACR
sinonimos:
- Relación albúmina/creatinina
- RAC
- Microalbuminuria
- Índice albúmina/creatinina en orina
- UACR
- Relación Albúmina/Creatinina en Orina (UACR)
- Urine Albumin-to-Creatinine Ratio
- Relación albúmina/creatinina (RAC)
category: Riñón
parameter_type: derived_ratio
tipo_resultado: numérico
unidad_canonica: mg/g
specimen: Orina, primera de la mañana
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-NE-001
- COND-M2-NE-002
- COND-M2-NE-006
- COND-M2-NE-A02
combine_with:
- creatinine
- egfr
- glucose
- hba1c
formula: UACR = Albúmina urinaria (mg/dL) / Creatinina urinaria (g/dL), en muestra de orina aislada (idealmente primera de la mañana)
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Ya está en el panel estándar con la muestra de orina de la toma domiciliaria: la nota de implementación original sobre un módulo de orina no disponible queda obsoleta.'
---

# UACR (Relación Albúmina/Creatinina en Orina)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Ya está en el panel estándar con la muestra de orina de la toma domiciliaria: la nota de implementación original sobre un módulo de orina no disponible queda obsoleta.
- Reglas que usan esta ficha: COND-M2-NE-001, COND-M2-NE-002, COND-M2-NE-006, COND-M2-NE-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-065. UACR. Categoría: Riñón. Tipo: **relación derivada**, medida en orina (no en sangre — único biomarcador de orina del catálogo). Tier 1 por importancia clínica real, aunque su implementación depende de una decisión de producto pendiente (módulo de orina).

## B. Definición

Cuantifica la cantidad de albúmina que se filtra anormalmente hacia la orina, normalizada por la creatinina urinaria (para corregir por concentración/dilución de la muestra). Junto con eGFR, es uno de los dos pilares de la clasificación KDIGO de enfermedad renal crónica — **eGFR sin UACR es una evaluación incompleta de la función renal.**

## C. Espécimen y toma

### Examen de laboratorio y espécimen

**Muestra de orina** (no sangre) — idealmente la primera micción de la mañana. Método: inmunoturbidimetría para albúmina, método enzimático para creatinina urinaria, luego calculado como ratio.

### Condiciones de toma de muestra

Evitar ejercicio intenso previo (puede elevar transitoriamente la albuminuria), evitar toma durante infección urinaria activa o menstruación (pueden contaminar la muestra), fiebre reciente (puede elevar transitoriamente).

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, clasificación KDIGO (evidencia verificada esta sesión, Cleveland Clinic + KDIGO)

- **Normal:** **<30 mg/g** — riesgo muy bajo de falla renal, infarto o ACV.
- **Categoría A2 (moderadamente elevada):** **30-299 mg/g** — mayor riesgo de enfermedad renal, cardíaca o ACV; KDIGO recomienda repetir en unos meses para confirmar.
- **Categoría A3 (severamente elevada):** **≥300 mg/g** — nefropatía significativa.
- **URL fuente:** https://my.clevelandclinic.org/health/diagnostics/urine-albumin-creatinine-ratio — verificado esta sesión (ago-2026).
- **Hallazgo relevante (verificado esta sesión, múltiples estudios poblacionales grandes):** incluso **dentro del rango "normal" (<30 mg/g)**, valores más altos dentro de ese rango se asocian de forma independiente con mayor riesgo cardiovascular — un estudio de 317 pacientes con diabetes tipo 2 encontró que UACR ≥10.2 mg/g (dentro de "normal") triplicó el riesgo de hipertrofia ventricular izquierda; estudios NHANES de gran escala (14,919 y otros) confirman asociación con hipertensión, aterosclerosis carotídea subclínica y mortalidad por todas las causas, incluso en rango normal. Esto sugiere que UACR se comporta como un **gradiente continuo de riesgo**, no un umbral binario estricto — similar al hallazgo ya documentado para el ratio ApoB/ApoA1.

## E. Interpretación

- La clasificación KDIGO de ERC requiere **eGFR + UACR combinados** — un eGFR normal con UACR elevada ya indica daño renal (ERC en etapa temprana con función de filtración aún preservada).
- **Elevada:** diabetes (causa más frecuente de daño renal progresivo), hipertensión, enfermedad renal glomerular primaria.

## F. Contexto del paciente y confusores

### Contexto del paciente

Diabetes (crítico — cribado anual recomendado), hipertensión, ejercicio reciente, infección urinaria activa, menstruación, fiebre reciente.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Creatinina/eGFR (obligatorio — juntos completan la clasificación KDIGO de ERC), Glucosa/HbA1c (diabetes como causa principal).
- `pattern_examples`: eGFR normal + UACR 30-299 = ERC categoría A2, función de filtración aún preservada pero con daño glomerular ya presente; eGFR bajo + UACR alta = ERC más avanzada con ambos componentes afectados.
- `cannot_conclude`: diagnóstico de ERC sin confirmar persistencia (KDIGO requiere alteración sostenida ≥3 meses, igual que eGFR).

## H. Tendencias

### Tendencias temporales

Un aumento progresivo, incluso dentro del rango normal, es relevante como señal temprana de riesgo — no solo cruzar el umbral de 30 mg/g importa, sino la trayectoria.

## I. Prevención

### Contexto preventivo

Cribado anual recomendado en diabetes e hipertensión — es una de las pruebas preventivas de mayor valor no implementadas todavía en Saludly v1.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Creatinina/eGFR (siempre en conjunto), repetir UACR en unos meses si está en categoría A2 para confirmar (KDIGO).

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No diagnosticar ERC sin persistencia confirmada y sin eGFR concurrente. Escalar ante UACR ≥300 mg/g (categoría A3), o UACR en categoría A2 confirmada en repetición.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte (Cleveland Clinic, clasificación KDIGO) + múltiples estudios poblacionales de gran escala (NHANES, cohortes asiáticas) para el hallazgo de gradiente de riesgo dentro de rango normal.
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "UACR elevada, combinar con eGFR para clasificación KDIGO completa; incluso valores altos dentro de 'normal' pueden ser relevantes en diabetes/hipertensión".
- **prohibited_inferences:** diagnóstico de ERC sin eGFR concurrente y sin confirmar persistencia.
- **uncertainty_notes:** requiere módulo de toma de muestra de orina no implementado en Saludly v1 — esta ficha está lista para cuando esa decisión de producto se resuelva.
- **professional_review:** UACR ≥300 mg/g, o categoría A2 confirmada en repetición, especialmente en diabetes/hipertensión.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - renal
  - kidney_function
  - diabetes_complication
  - derived_ratio
  - tier_1
  - saludly_brain_v1
use_when:
  - "clasificación completa de ERC junto a eGFR"
  - "cribado renal en diabetes o hipertensión"
combine_with: [creatinine, egfr, glucose, hba1c]
do_not_use_alone:
  - "diagnóstico de ERC sin eGFR concurrente"
do_not_conclude:
  - "ERC confirmada sin persistencia verificada"
escalate_when:
  - "UACR ≥300 mg/g"
  - "categoría A2 confirmada en repetición"
```
