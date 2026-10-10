---
doc_id: SLD-BIO-048
biomarker_id: lpa
name_es: Lipoproteína(a)
name_en: Lipoprotein(a)
abbreviation: Lp(a)
sinonimos:
- Lipoproteína (a)
- Lp(a)
- Lipoproteína a
- Lipoproteína(a)
- Lipoproteína(a) [Lp(a)]
- Lipoprotein(a)
category: cardiovascular_lipids
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL o nmol/L (se guarda con la unidad del laboratorio, sin convertir)
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-CA-004
combine_with:
- apob
- ldl_c
- total_cholesterol
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Corte adoptado: más de 50 mg/dL o 105 nmol/L (ESC/EAS); 125 nmol/L de ACC/AHA solo en la vista médica; nunca convertir entre unidades (COND-M1-CA-004).'
---

# Lipoproteína(a) [Lp(a)]

## Notas de decisión de Saludly (6 de octubre de 2026)

- Corte adoptado: más de 50 mg/dL o 105 nmol/L (ESC/EAS); 125 nmol/L de ACC/AHA solo en la vista médica; nunca convertir entre unidades (COND-M1-CA-004).
- Reglas que usan esta ficha: COND-M1-CA-004. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-048. Lp(a). Categoría: Cardiovascular/Lípidos. Tipo: analito medido. Tier 2.

## B. Definición

Partícula similar a LDL unida covalentemente a apolipoproteína(a). Es un factor de riesgo cardiovascular independiente y causal, determinado predominantemente por genética (no por dieta ni estilo de vida) — esto la distingue de casi todos los demás biomarcadores del catálogo de Saludly.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método: inmunoensayo estandarizado (idealmente insensible a isoformas de tamaño de apo(a), fuente de variabilidad interlaboratorio conocida). Unidad: mg/dL (alt: nmol/L — **no intercambiables por una simple conversión matemática**, ya que dependen del número de repeticiones "kringle" de la isoforma de apo(a); Saludly debe registrar en qué unidad reporta el laboratorio aliado). No requiere ayuno.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión, con nota de disenso entre sociedades)

- **No existe consenso único internacional** (verificado explícitamente esta sesión vía ACC): distintas sociedades usan distintos puntos de corte:
  - **ACC/AHA:** ≥50 mg/dL (≥125 nmol/L) como umbral de riesgo aumentado.
  - **European Atherosclerosis Society (EAS):** <30 mg/dL normal, 30-50 mg/dL intermedio, >50 mg/dL anormal.
  - **National Lipid Association (NLA, actualización 2024):** <30 mg/dL (75 nmol/L) bajo riesgo, 30-50 mg/dL (75-125 nmol/L) riesgo intermedio, ≥50 mg/dL (≥125 nmol/L) alto riesgo.
  - **Canadian Cardiovascular Society:** ≥50 mg/dL (≥100 nmol/L).
- **Magnitud de riesgo:** ACC/AHA 2026 — Lp(a) ≥125 nmol/L se asocia a ~1.4x mayor riesgo a largo plazo de infarto/ACV; Lp(a) ≥250 nmol/L se asocia a al menos 2x mayor riesgo.
- **Umbral de intervención invasiva:** ≥60 mg/dL (~150 nmol/L) es el umbral usado en Alemania y otros países para considerar aféresis de lipoproteínas en pacientes de muy alto riesgo con LDL-C ya controlado.
- **URLs fuente:** https://www.acc.org/Latest-in-Cardiology/Articles/2023/09/19/10/54/An-Update-on-Lipoprotein-a ; https://www.acc.org/about-acc/press-releases/2026/03/13/18/01/accaha-issue-updated-guideline-for-managing-lipids-cholesterol ; https://www.lipid.org/sites/default/files/files/PIIS1933287424000333.pdf — todas verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada:** factor de riesgo cardiovascular independiente y causal (no solo asociación) — el nivel se mantiene relativamente estable durante toda la vida adulta, por lo que un valor elevado es un hallazgo de por vida, no un estado transitorio a monitorear repetidamente.
- **No existe fenotipo adverso conocido asociado a Lp(a) baja** — un valor bajo no requiere ninguna acción.
- El tratamiento actual (estatinas, ezetimiba) **no reduce Lp(a) de forma significativa** — el manejo en personas con Lp(a) elevada se centra en intensificar el control de LDL-C y otros factores de riesgo modificables, no en "tratar" la Lp(a) directamente (los inhibidores de PCSK9 sí la reducen parcialmente).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: antecedentes familiares de enfermedad cardiovascular precoz o de Lp(a) elevada — dado su fuerte componente hereditario, este es uno de los biomarcadores donde el antecedente familiar es más determinante que en el resto del catálogo.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: ApoB, LDL-C — Lp(a) elevada no siempre se acompaña de ApoB elevado (son mediciones parcialmente independientes).
- `pattern_examples`: Lp(a) elevada + LDL-C ya controlado = candidato a manejo más intensivo de otros factores de riesgo modificables según guías 2026.
- `cannot_conclude`: diagnóstico de enfermedad cardiovascular — es un factor de riesgo, no una prueba diagnóstica.

## H. Tendencias

### Tendencias temporales

**Excepción relevante para el diseño de Saludly Brain:** a diferencia de prácticamente todo el resto del catálogo, Lp(a) no requiere seguimiento longitudinal repetido — es genéticamente determinada y estable. El sistema debe evitar solicitarla repetidamente en controles sucesivos salvo indicación excepcional (ej. verificación de un resultado dudoso).

## I. Prevención

Los cambios de estilo de vida tienen efecto mínimo sobre el nivel de Lp(a) en sí — el valor preventivo real está en usar un resultado elevado para intensificar el manejo de los factores de riesgo que sí son modificables (LDL-C, presión arterial, tabaquismo, control glucémico) y en considerar cribado en cascada de familiares de primer grado.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Cribado en cascada de familiares de primer grado si Lp(a) está elevada (recomendación NLA 2024) — fuera del alcance operativo actual de Saludly v1, pero el sistema debe poder comunicarlo como recomendación general.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Cribado de una sola vez en la vida adulta (recomendación ACC/AHA 2026 y NLA) — no es diagnóstico de enfermedad cardiovascular, es estratificación de riesgo genético.

## L. Evidencia

### Evidencia científica

- **Scientific statement (fuerte):** Koschinsky ML, et al. "A focused update to the 2019 NLA scientific statement on use of lipoprotein(a) in clinical practice." *J Clin Lipidology* 2024. https://www.lipid.org/sites/default/files/files/PIIS1933287424000333.pdf
- **Guideline (fuerte):** ACC/AHA Updated Guideline for Managing Lipids, Cholesterol, 2026. https://www.acc.org/about-acc/press-releases/2026/03/13/18/01/accaha-issue-updated-guideline-for-managing-lipids-cholesterol
- **Revisión (fuerte):** "An Update on Lipoprotein(a)." American College of Cardiology, 2023. https://www.acc.org/Latest-in-Cardiology/Articles/2023/09/19/10/54/An-Update-on-Lipoprotein-a
- Todas verificadas por búsqueda web esta sesión (ago-2026). **Nota de calidad de evidencia:** existe disenso documentado entre sociedades sobre el umbral exacto — el sistema debe presentar el umbral ACC/AHA como referencia primaria por ser la guía estadounidense más reciente, mencionando que otras sociedades usan valores distintos, no ocultar la discrepancia.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "Lp(a) elevada es un factor de riesgo cardiovascular genético independiente; no requiere repetirse, pero sí considerar manejo más intensivo de otros factores de riesgo modificables".
- **prohibited_inferences:** "Lp(a) alta = va a tener un infarto"; recomendar aféresis o tratamiento farmacológico específico (decisión médica especializada).
- **uncertainty_notes:** existe disenso entre sociedades médicas sobre el umbral exacto de riesgo — comunicar con transparencia, no presentar un único número como consenso universal.
- **professional_review:** Lp(a) ≥125 nmol/L (~50 mg/dL), especialmente combinado con antecedente familiar de enfermedad cardiovascular precoz o LDL-C ya elevado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - cardiovascular
  - lipid_advanced
  - genetic_risk
  - tier_2
  - saludly_brain_v1

use_when:
  - "cribado de una sola vez en la vida adulta"
  - "antecedente familiar de enfermedad cardiovascular precoz o de Lp(a) elevada"
  - "enfermedad cardiovascular sin otros factores de riesgo evidentes"

combine_with: [apob, ldl_c, total_cholesterol]

do_not_use_alone:
  - "diagnóstico de enfermedad cardiovascular"
  - "decisión de tratamiento (aféresis, PCSK9)"

do_not_conclude:
  - "certeza de evento cardiovascular futuro"

escalate_when:
  - "Lp(a) ≥125 nmol/L (~50 mg/dL) combinado con antecedente familiar o LDL-C elevado"
```
