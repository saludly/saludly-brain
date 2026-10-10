---
doc_id: SLD-BIO-027
biomarker_id: potassium
name_es: Potasio
name_en: Potassium
abbreviation: K+
sinonimos:
- Potasio
- K
- Potasio sérico
- K+
- Potassium
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mmol/L
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M2-NE-004
- COND-M2-NE-A01
combine_with:
- sodium
- chloride
- bicarbonate
- creatinine
- egfr
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- Nunca se escala con un valor hemolizado o aislado; plasma separado en menos de 30 minutos (COND-M2-NE-004).
---

# Potasio (K+)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Nunca se escala con un valor hemolizado o aislado; plasma separado en menos de 30 minutos (COND-M2-NE-004).
- Reglas que usan esta ficha: COND-M2-NE-004, COND-M2-NE-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-027. K+. Categoría: Metabolismo y Electrolitos. Tipo: analito medido. Tier 1.

## B. Definición

Principal catión intracelular; su concentración sérica (que representa <2% del potasio corporal total) es crítica para la excitabilidad neuromuscular y cardíaca. Es uno de los pocos electrolitos donde una alteración significativa puede ser una urgencia médica.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma). Método: electrodo ion-selectivo. Unidad: mEq/L (=mmol/L). No requiere ayuno. **Factor preanalítico crítico:** hemólisis de la muestra (por punción traumática, torniquete prolongado, demora en procesamiento) libera potasio intracelular y produce **pseudohiperpotasemia** — esta es una de las interferencias preanalíticas más frecuentes y clínicamente importantes de todo el panel metabólico.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método — rango fisiológico típico ampliamente reproducido en fisiología clínica estándar (aprox. 3.5-5.0 mEq/L), a validar con el laboratorio aliado.
- **Clinical decision threshold:** valores marcadamente elevados (hiperpotasemia severa) o disminuidos (hipopotasemia severa) son urgencias médicas por riesgo de arritmia cardíaca.
- **Estado de verificación:** ⚠️ Mismo caso que sodio — conocimiento fisiológico estándar, pero el umbral exacto de urgencia debe verificarse con fuente primaria (ej. guías de manejo de hiperpotasemia) antes de fijarse como umbral de producto.

## E. Interpretación

**Elevado (hiperpotasemia):**
- Causas frecuentes: insuficiencia renal (reducción de la excreción), medicamentos (IECA, ARA-II, espironolactona, AINEs), acidosis metabólica (desplazamiento de K+ del espacio intracelular al extracelular).
- **Causa preanalítica muy frecuente:** hemólisis de la muestra — Saludly debe registrar si el laboratorio reporta hemólisis visible antes de interpretar un valor alto como real.

**Disminuido (hipopotasemia):**
- Causas frecuentes: diuréticos, vómito/diarrea, hiperaldosteronismo, ingesta insuficiente.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: función renal (creatinina/eGFR), medicamentos (IECA, ARA-II, diuréticos), vómito/diarrea reciente, síntomas (debilidad muscular, palpitaciones).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Sodio, Cloro, Bicarbonato, **Creatinina/eGFR (obligatorio — la función renal es el determinante más común de hiperpotasemia crónica)**.
- `pattern_examples`: hiperpotasemia + eGFR bajo = sugiere causa renal; hiperpotasemia sin insuficiencia renal ni medicamentos relevantes = considerar hemólisis de la muestra antes que patología real.
- `cannot_conclude`: causa específica sin conocer función renal y medicamentos concurrentes.

## H. Tendencias

### Tendencias temporales

Al igual que sodio, las alteraciones significativas de potasio son predominantemente agudas y requieren manejo en tiempo real. Un potasio crónicamente en el límite superior en alguien con eGFR reducido es una tendencia longitudinal relevante para seguimiento de función renal.

## I. Prevención

Acciones razonables: revisión de medicamentos con un profesional (especialmente combinaciones de IECA/ARA-II + espironolactona), atención a hidratación en episodios de vómito/diarrea.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Repetir sin hemólisis si hay sospecha de interferencia preanalítica; función renal si no está disponible; ECG si hay alteración marcada con síntomas.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del panel metabólico básico de rutina — su valor principal en un contexto preventivo es detectar disfunción renal temprana o efectos de medicación, no diagnosticar una condición primaria del potasio en sí.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento fisiológico estándar (`expert_consensus` / `educational_reference`).
- **Guideline (fuerte, verificado esta sesión):** KDIGO 2024 clasifica la hiperpotasemia aguda por severidad: **leve 5.0-5.9 mmol/L · moderada 6.0-6.4 mmol/L · severa ≥6.5 mmol/L**. Fuente: consenso KDIGO citado en Nefrología (Elsevier), https://revistanefrologia.com/en-consensus-document-on-management-hyperkalemia-avance-S2013251423001785 y confirmado en estudio de validación 2026: https://arxiv.org/pdf/2603.14177
- **Umbral de riesgo cardiorrenal (meta-análisis CKD Prognosis Consortium, >1 millón de sujetos):** el riesgo cardiorrenal es más bajo con potasio 4-4.5 mEq/L y **aumenta progresivamente desde el umbral de 5.0 mEq/L** en todos los estratos de eGFR — es decir, el riesgo empieza antes del punto clásico de "hiperpotasemia franca". Fuente: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8000881/
- **Nota de disenso entre especialidades (verificado esta sesión):** nefrología (KDIGO) usa 5.5 mEq/L como umbral de acción sobre medicamentos IECA/ARA-II en ERC; cardiología (ESC) es más permisiva, tolerando continuar estos medicamentos hasta 6.5 mEq/L usando quelantes de potasio como primera línea. Saludly debe comunicar el umbral KDIGO como referencia primaria (más conservador, más apropiado para un contexto preventivo sin supervisión médica directa), señalando que existe variación entre especialidades.
- Todas las fuentes verificadas por búsqueda web esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "alteración del potasio, considerar función renal y medicamentos como primeras causas a evaluar; si el valor es alto sin explicación clínica evidente, considerar también hemólisis de la muestra".
- **prohibited_inferences:** diagnóstico de insuficiencia renal, hiperaldosteronismo u otra condición específica a partir del potasio aislado.
- **uncertainty_notes:** la hemólisis de la muestra es una causa preanalítica frecuente de falsa elevación — el sistema debe verificar si el laboratorio reportó hemólisis antes de generar cualquier interpretación de un valor alto.
- **professional_review:** cualquier valor marcadamente fuera de rango — este es, junto con troponina, uno de los biomarcadores del catálogo con mayor potencial de urgencia médica real si el valor es genuino (no artefactual).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - electrolytes
  - metabolism
  - renal
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando panel electrolítico"
  - "evaluando función renal junto con creatinina/eGFR"
  - "revisando efectos de medicamentos (IECA, ARA-II, diuréticos)"

combine_with: [sodium, chloride, bicarbonate, creatinine, egfr]

do_not_use_alone:
  - "diagnóstico de insuficiencia renal, hiperaldosteronismo, o causa específica"

do_not_conclude:
  - "insuficiencia renal confirmada solo por potasio elevado"
  - "hiperpotasemia real sin descartar hemólisis de la muestra"

escalate_when:
  - "valor marcadamente elevado o disminuido, sin hemólisis reportada por el laboratorio"
  - "síntomas concurrentes (debilidad muscular marcada, palpitaciones, arritmia conocida)"
```
