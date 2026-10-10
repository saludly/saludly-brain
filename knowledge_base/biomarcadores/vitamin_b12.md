---
doc_id: SLD-BIO-081
biomarker_id: vitamin_b12
name_es: Vitamina B12
name_en: Vitamin B12 (Cobalamin)
abbreviation: B12
sinonimos:
- Vitamina B12
- Cobalamina
- Cianocobalamina
- B12
- Vitamin B12 (Cobalamin)
category: vitamins_micronutrients
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: pg/mL
specimen: Suero
nivel_catalogo: vitamina con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-004
- COND-M3-NU-001
combine_with:
- folate
- homocysteine
- mcv
- hemoglobin
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: high
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Corte adoptado NICE: < 180 pg/mL déficit; 180 a 350 indeterminado con ácido metilmalónico reflejo (COND-M3-NU-001). Esta ficha cita < 200; manda la ficha de condición.'
---

# Vitamina B12 (Cobalamina)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Corte adoptado NICE: < 180 pg/mL déficit; 180 a 350 indeterminado con ácido metilmalónico reflejo (COND-M3-NU-001). Esta ficha cita < 200; manda la ficha de condición.
- Reglas que usan esta ficha: COND-M3-HE-004, COND-M3-NU-001. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-081. B12. Categoría: Vitaminas/Micronutrientes. Tipo: analito medido. Tier 1.

## B. Definición

Vitamina esencial para la síntesis de ADN y el mantenimiento de la vaina de mielina. Su deficiencia causa tanto anemia macrocítica como daño neurológico progresivo, que puede ser irreversible si no se trata a tiempo — esto la hace clínicamente prioritaria a pesar de que la prueba estándar (B12 sérica total) tiene limitaciones reconocidas.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método: inmunoensayo (quimioluminiscencia). Unidad: pg/mL (alt: pmol/L). No requiere ayuno estricto. Limitación metodológica importante: la B12 sérica total mide predominantemente la fracción unida a haptocorrina, que es **biológicamente inactiva** — esto explica por qué algunas personas con síntomas neurológicos de deficiencia tienen B12 sérica "normal-baja" (zona gris 200-350 pg/mL).

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente (evidencia verificada esta sesión)

- **Laboratory reference interval:** rango típico amplio, aproximadamente 200-900 pg/mL — depende del laboratorio/método, validar con laboratorio aliado.
- **Clinical decision threshold (deficiencia franca):** <200 pg/mL — clasificación ampliamente usada en la literatura clínica y epidemiológica (prevalencia de deficiencia franca ~3.6% en adultos según revisión de Medscape/eMedicine referenciada).
- **Risk threshold / zona gris clínicamente relevante:** 200-350 pg/mL — evidencia de revisión sistemática reciente (ScienceDirect, 2025) documenta que **personas en este rango pueden tener síntomas neurológicos y metabólicos de deficiencia** pese a no cumplir el criterio numérico estricto de "deficiencia". Esto es clínicamente relevante: Saludly no debe comunicar "B12 normal" sin matiz si el valor está en esta zona.
- **Nota de evolución de umbrales:** existe evidencia (Cesana et al., *J Lab Precis Med* 2025, sobre revisión de umbrales NICE) de que las guías están revisando al alza los puntos de corte de deficiencia — este es un área activa de cambio, Saludly debe monitorear actualizaciones.
- **URL fuentes:** https://www.sciencedirect.com/science/article/pii/S266645932500040X ; https://jlpm.amegroups.org/article/view/10559/html ; https://emedicine.medscape.com/article/1152670-overview — verificadas esta sesión (ago-2026).

## E. Interpretación

**Disminuida:**
- Causas frecuentes: dieta vegetariana/vegana estricta sin suplementación, malabsorción (anemia perniciosa, enfermedad de Crohn, cirugía bariátrica), uso crónico de metformina o inhibidores de bomba de protones (IBP), edad avanzada (absorción reducida).
- Consecuencias si no se trata: anemia macrocítica, neuropatía periférica, degeneración combinada subaguda de la médula espinal (potencialmente irreversible si el tratamiento se retrasa).

**Dentro del intervalo pero en zona gris (200-350 pg/mL):** puede coexistir con síntomas neurológicos reales — no debe descartarse deficiencia funcional solo por estar "en rango de laboratorio".

**Elevada:** generalmente por suplementación reciente (oral o inyectada) — sin significado patológico en ese contexto; en raros casos, elevaciones muy marcadas sin suplementación pueden asociarse a enfermedad hepática o mieloproliferativa (hallazgo infrecuente, requiere contexto).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: dieta (vegetarianismo/veganismo), medicamentos (metformina, IBP), cirugía bariátrica previa, edad, síntomas neurológicos (parestesias, inestabilidad de la marcha, deterioro cognitivo), suplementación reciente.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Folato (deficiencias combinadas o que se enmascaran mutuamente), Homocisteína (marcador funcional más sensible — puede estar elevada incluso con B12 sérica "normal-baja"), VCM/Hemoglobina (para identificar anemia macrocítica asociada).
- `pattern_examples`: B12 en zona gris + homocisteína elevada = mayor sospecha de deficiencia funcional real pese a B12 "normal" por laboratorio; VCM elevado + B12 baja = anemia macrocítica por deficiencia de B12.
- `conflicting_patterns`: deficiencia de folato puede enmascarar (corregir parcialmente) la anemia por deficiencia de B12 sin corregir el daño neurológico — por eso ambos deben evaluarse juntos, nunca folato solo como sustituto de B12.
- `cannot_conclude`: causa específica de la deficiencia (dietética vs malabsortiva vs medicamentosa) sin historia clínica dirigida.

## H. Tendencias

### Tendencias temporales

El desarrollo de deficiencia por malabsorción toma 2-5 años (dado el almacenamiento hepático); por causa dietética estricta (veganismo) puede tardar 10-20 años en manifestarse clínicamente, según la literatura revisada. Esto significa que un valor "normal" hoy en una persona con dieta de riesgo no garantiza ausencia de depleción progresiva — es útil para seguimiento longitudinal, no solo para un corte puntual.

## I. Prevención

Acciones razonablemente relacionadas: suplementación dietética o vitamínica en personas con dieta vegetariana/vegana estricta (recomendación general, no dosis específica — eso es responsabilidad médica/nutricional), seguimiento en personas con factores de riesgo conocidos (metformina, IBP crónicos, edad avanzada).

## J. Pruebas complementarias

### Pruebas complementarias posibles

Homocisteína (más sensible para detectar deficiencia funcional en zona gris), Folato (siempre junto), ácido metilmalónico (MMA) si está disponible — marcador más específico de deficiencia funcional de B12, aunque **no está actualmente en el catálogo de Saludly v1** (candidato para futuro lote de Tier 2/3).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

B12 sérica es la prueba de cribado inicial estándar, pero tiene sensibilidad limitada en la zona gris — un valor "normal" no descarta deficiencia funcional con certeza absoluta, especialmente en personas con factores de riesgo o síntomas neurológicos.

## L. Evidencia

### Evidencia científica

- **Revisión sistemática (evidencia moderada-fuerte):** "Vitamin B12 deficiency and cognitive impairment: A comprehensive review of neurological impact." *ScienceDirect*, 2025. https://www.sciencedirect.com/science/article/pii/S266645932500040X
- **Revisión de umbrales clínicos:** Cesana BM, et al. "Changing the bar for B12 deficiency: possible clinical impact of NICE's thresholds revisions." *J Lab Precis Med* 2025;10:18. DOI: 10.21037/jlpm-25-49. https://jlpm.amegroups.org/article/view/10559/html
- **Referencia general de fisiopatología/epidemiología:** eMedicine/Medscape, "Vitamin B12-Associated Neurological Diseases." https://emedicine.medscape.com/article/1152670-overview
- Todas verificadas por búsqueda web esta sesión (ago-2026). Nota de calidad: la fuente eMedicine es una referencia educativa/clínica agregadora, no una guía de sociedad médica primaria — se usa aquí para datos epidemiológicos generales, no como fuente de umbral de decisión.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "B12 baja o en zona gris (200-350 pg/mL), considerar evaluación funcional con homocisteína, especialmente si hay síntomas neurológicos o factores de riesgo (dieta vegana, metformina, IBP, edad)".
- **prohibited_inferences:** "B12 normal = sin deficiencia funcional posible" cuando el valor está en zona gris; diagnóstico de anemia perniciosa u otra causa específica sin estudios adicionales.
- **uncertainty_notes:** la prueba estándar de B12 sérica total tiene sensibilidad limitada; los umbrales de deficiencia están en revisión activa en la literatura reciente (2025) — Saludly debe tratar este biomarcador como un área de evidencia evolutiva, no estática.
- **professional_review:** B12 <200 pg/mL, zona gris con síntomas neurológicos concurrentes (parestesias, inestabilidad de la marcha, deterioro cognitivo), o anemia macrocítica asociada.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - vitamins
  - neurological_risk
  - anemia_workup
  - tier_1
  - saludly_brain_v1

use_when:
  - "evaluando anemia macrocítica"
  - "síntomas neurológicos inespecíficos (parestesias, inestabilidad, deterioro cognitivo)"
  - "dieta vegetariana/vegana estricta, uso crónico de metformina o IBP"

combine_with: [folate, homocysteine, mcv, hemoglobin]

do_not_use_alone:
  - "descartar deficiencia funcional de B12 solo por estar en rango de laboratorio (zona gris 200-350 pg/mL)"

do_not_conclude:
  - "causa específica de deficiencia sin historia clínica dirigida"
  - "ausencia de deficiencia funcional solo por B12 sérica normal"

escalate_when:
  - "B12 <200 pg/mL"
  - "zona gris (200-350 pg/mL) con síntomas neurológicos concurrentes"
  - "anemia macrocítica asociada"
```
