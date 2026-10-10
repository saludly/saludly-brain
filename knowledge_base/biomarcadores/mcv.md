---
doc_id: SLD-BIO-004
biomarker_id: mcv
name_es: VCM (Volumen Corpuscular Medio)
name_en: MCV (Mean Corpuscular Volume)
abbreviation: VCM / MCV
sinonimos:
- VCM
- MCV
- Volumen corpuscular medio
- VCM (Volumen Corpuscular Medio)
- VCM / MCV
- MCV (Mean Corpuscular Volume)
category: hematology
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: fL
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-002
- COND-M3-HE-004
- COND-M6-MI-A02
- COND-M3-HE-A04
- COND-M3-HE-009
combine_with:
- hemoglobin
- hematocrit
- ferritin
- vitamin_b12
- folate
formula: VCM = (Hematocrito × 10) / Eritrocitos (millones/µL); reportado directamente por la mayoría de analizadores automatizados modernos a partir de la medición directa del volumen celular por citometría de flujo.
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

# VCM (Volumen Corpuscular Medio)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-002, COND-M3-HE-004, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-004. VCM/MCV. Categoría: Hematología. **Tipo: parámetro calculado** en analizadores clásicos, aunque en analizadores hematológicos modernos de citometría de flujo se **mide directamente** el volumen celular individual y luego se promedia — Saludly debe registrar cuál es el caso en el laboratorio aliado. Tier 1.

## B. Definición

Volumen promedio de los eritrocitos. Es la variable central para clasificar una anemia como microcítica, normocítica o macrocítica — clasificación que orienta directamente hacia las causas más probables.

## C. Espécimen y toma

### Espécimen y laboratorio

No aplica obtención independiente — se deriva del mismo hemograma completo que hemoglobina/hematocrito/eritrocitos. Unidad: fL (femtolitros).

### Fórmula y limitaciones

- **Fórmula clásica:** VCM = (Hematocrito × 10) / Eritrocitos (millones/µL).
- **Variables necesarias:** Hematocrito, conteo de eritrocitos (o medición directa por citometría en analizadores modernos).
- **Cuándo NO debe calcularse por fórmula:** cuando el analizador ya reporta medición directa por citometría de flujo — en ese caso el valor reportado es la medición primaria, no un cálculo secundario, y Saludly debe registrar esta distinción en el campo `parameter_type` real del laboratorio aliado.

## E. Interpretación

- **Bajo (microcítico, <80 fL aprox., valor exacto depende del laboratorio):** sugiere deficiencia de hierro, talasemia, anemia de enfermedad crónica en fase avanzada.
- **Normal (normocítico):** anemia de enfermedad crónica en fase temprana, pérdida sanguínea aguda, anemia hemolítica.
- **Alto (macrocítico, >100 fL aprox.):** deficiencia de B12/folato, hipotiroidismo, consumo de alcohol, enfermedad hepática, ciertos medicamentos (ej. algunos antirretrovirales, hidroxiurea).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: dieta (vegetarianismo/veganismo estricto para B12), consumo de alcohol, función tiroidea, medicamentos, antecedente de sangrado.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Hemoglobina, Hematocrito (obligatorio — VCM sin anemia documentada tiene poco valor clínico aislado), Ferritina (si microcítico), Vitamina B12/Folato (si macrocítico).
- `pattern_examples`: anemia + VCM bajo + ferritina baja = patrón compatible con deficiencia de hierro; anemia + VCM alto + B12 baja = patrón compatible con deficiencia de B12.
- `cannot_conclude`: causa definitiva sin el biomarcador específico correspondiente (ferritina para microcítica, B12/folato para macrocítica).

## H. Tendencias

### Tendencias temporales

Cambia lentamente (semanas-meses) porque refleja la población eritrocitaria completa, no solo los eritrocitos más recientes — un cambio de tendencia es señal de un proceso ya establecido, no agudo.

## I. Prevención

Utilidad alta para orientar la causa de una anemia detectada por hemoglobina/hematocrito y dirigir la siguiente prueba (ferritina vs B12/folato) de forma eficiente, sin pedir todo el panel de micronutrientes a ciegas.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ferritina (si microcítico), Vitamina B12 y Folato (si macrocítico), función tiroidea (si macrocítico sin causa evidente).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del hemograma de cribado — su valor es clasificatorio (orienta la causa de una anemia ya detectada), no diagnóstico por sí solo.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar, ampliamente reproducido y sin controversia relevante en su interpretación básica.
- **Fuente (UI Health Care, verificado esta sesión):** rango normal VCM en adultos **82-99 fL**. https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html — verificado esta sesión (ago-2026). Los puntos de corte de "microcítico <80" / "macrocítico >100" citados en la literatura general son aproximaciones ampliamente usadas y consistentes con este rango institucional (82-99 fL), con el margen esperable de variación entre laboratorios.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "en presencia de anemia, el VCM orienta hacia [microcítica/normocítica/macrocítica], sugiere evaluar [ferritina/B12-folato] según corresponda".
- **prohibited_inferences:** usar VCM sin anemia documentada (Hb/Hto normales) para generar cualquier alarma o recomendación.
- **uncertainty_notes:** el VCM aislado sin el resto del hemograma tiene valor interpretativo mínimo.
- **professional_review:** anemia con VCM marcadamente alterado sin causa evidente tras evaluación de ferritina/B12/folato.

## N. Notas de auditoría

### Nota de consolidación (auditoría posterior)

**HCM (Hemoglobina Corpuscular Media) se consolidó dentro de este registro** — ya estaba documentada como en gran medida redundante con VCM para la mayoría de decisiones clínicas ambulatorias (se mueve en la misma dirección que VCM en la gran mayoría de los casos). Fórmula de HCM para referencia: HCM = (Hemoglobina × 10) / Eritrocitos. Si Saludly Brain necesita el valor de HCM específicamente, debe calcularlo bajo demanda con esta fórmula, sin mantenerlo como registro separado del catálogo — ver `AUDIT_CHANGELOG` en `00_INDEX.md`.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - anemia_classification
  - calculated_parameter
  - tier_1
  - saludly_brain_v1

use_when:
  - "clasificando una anemia ya detectada por hemoglobina/hematocrito"

combine_with: [hemoglobin, hematocrit, ferritin, vitamin_b12, folate]

do_not_use_alone:
  - "cualquier interpretación sin hemoglobina/hematocrito alterados"

do_not_conclude:
  - "causa definitiva de anemia sin ferritina o B12/folato según corresponda"

escalate_when:
  - "anemia con VCM marcadamente alterado sin causa evidente tras evaluación básica"
```
