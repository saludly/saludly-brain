---
doc_id: SLD-BIO-021
biomarker_id: hba1c
name_es: Hemoglobina A1c (HbA1c)
abbreviation: HbA1c
sinonimos:
- Hemoglobina glicosilada
- Hemoglobina glucosilada
- HbA1c
- A1C
- Hemoglobina A1c
- Hemoglobina A1c (HbA1c)
category: Metabolismo y Electrolitos
subcategory: Homeostasis glucémica
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-EM-001
- COND-M1-EM-002
combine_with:
- glucose
- fructosamine
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
- 'Con anemia o hemoglobinopatía, baja confianza: manda la glucosa (COND-M1-EM-001).'
---

# Hemoglobina A1c (HbA1c)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Con anemia o hemoglobinopatía, baja confianza: manda la glucosa (COND-M1-EM-001).
- Reglas que usan esta ficha: COND-M1-EM-001, COND-M1-EM-002. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-021. HbA1c. Categoría: Metabolismo y Electrolitos. Tipo: measured_analyte. Tier 1.

## B. Definición

Fracción de hemoglobina unida covalentemente a glucosa. Refleja la glicemia promedio ponderada de los últimos ~2-3 meses, con mayor peso de las 4 semanas más recientes (vida media eritrocitaria ~120 días).

## C. Espécimen y toma

### Espécimen y laboratorio

- Muestra: sangre venosa (o capilar según método) · Tubo EDTA (tapa lila)
- Método: HPLC, inmunoensayo, o electroforesis de afinidad al boronato
- ¿Ayuno? **No requiere**
- Factores preanalíticos: hemoglobinopatías (Hb variantes), anemia hemolítica, transfusión reciente, ERC y embarazo alteran la fiabilidad.

### 2. Resultado y tipo de dato

- Unidad: % (alt: mmol/mol IFCC) · numérico continuo · **Medido**
- Limitación: interferencia posible por hemoglobinas variantes (ej. Hb G-Coushatta, Hb Queens) según plataforma — Saludly debe registrar la plataforma del laboratorio.

## D. Intervalos y umbrales

```
clinical_decision_threshold: ADA — diabetes ≥6.5%, prediabetes 5.7-6.4%, normal <5.7%
lab_reference_interval: depende de la plataforma (HPLC vs inmunoensayo vs boronato)
```

## E. Interpretación

- **Elevado:** hiperglucemia sostenida 2-3 meses previos.
- **Falsamente bajo/alterado:** anemia hemolítica, hemoglobinopatías, embarazo, transfusión reciente, ERC avanzada.
- Variabilidad biológica baja-moderada; variabilidad analítica relevante solo si hay Hb variante.

## F. Contexto del paciente y confusores

### Contexto del paciente

Obligatorias: antecedente de anemia/hemoglobinopatía, transfusión reciente, embarazo.
Opcionales: raza/etnia solo si es clínicamente relevante para variantes de Hb conocidas.

## G. Relaciones con otros biomarcadores

### Contexto clínico y relaciones con otros biomarcadores

- Combinar obligatoriamente con: Glucosa en ayunas; con Fructosamina en casos dudosos.
- NO debe usarse aislado en condiciones que alteran el recambio eritrocitario.
- Alerta: ≥6.5% o discordancia marcada con glucosa. Repetir si: 5.7-6.4% (limítrofe) o sospecha de interferencia.

## I. Prevención

- Herramienta central de seguimiento longitudinal de control glucémico.
- Alerta: aumento ≥0.3-0.5% entre controles sin justificación clínica.
- Prohibido: ajuste de fármacos antidiabéticos sin médico.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ver `possible_follow_up_tests` implícito en la sección G (combine_with) y en `RAG_INSTRUCTIONS` al final de
este archivo — Saludly Brain no debe recomendar pruebas adicionales de forma automática; el lenguaje correcto
es "considerar evaluación adicional según contexto clínico", nunca una orden imperativa.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Este parámetro es una herramienta de cribado/seguimiento dentro de un panel preventivo, no una prueba
diagnóstica aislada de ninguna condición específica. Ver `prohibited_inferences.md` para el detalle de qué
conclusiones diagnósticas están prohibidas para este y el resto del catálogo.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte, con matiz de evidencia moderada sobre su sensibilidad diagnóstica aislada.
- **Fuente:** ADA Standards of Care in Diabetes 2026 (HbA1c ≥6.5% diabetes; 5.7-6.4% prediabetes).
- **URL:** https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes
- **Verificado:** sí, esta sesión.
- **Limitación documentada:** estudios muestran que la sensibilidad de HbA1c ≥6.5% frente a FPG y 2hPG puede ser considerablemente menor de lo asumido en algunas cohortes (PMC4997021) — Saludly no debe sobrestimar la capacidad diagnóstica aislada de HbA1c frente a glucosa/OGTT.

## M. Seguridad para Saludly Brain

- **Input requerido:** glucosa en ayunas si disponible, antecedentes de anemia/hemoglobinopatía, embarazo.
- **Inferencia permitida:** "control glucémico promedio de los últimos 2-3 meses compatible con X".
- **Inferencia PROHIBIDA:** diagnóstico definitivo sin considerar condiciones que alteran el recambio eritrocitario.
- **Confianza por defecto:** alta si no hay condiciones interferentes conocidas; baja si hay anemia/hemoglobinopatía reportada.
- **Activa evaluación profesional:** ≥6.5%, o discordancia relevante con glucosa/fructosamina.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolismo_y_electrolitos
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando resultados de este parámetro específico"
  - "combinando este parámetro con otros del mismo panel"

combine_with: ["glucose", "fructosamine", "hemoglobin"]

do_not_use_alone:
  - "diagnóstico de cualquier enfermedad"
  - "confirmación o descarte de riesgo sin el resto del panel relacionado"

do_not_conclude:
  - "presencia confirmada de una enfermedad a partir de este valor aislado"
  - "ausencia de enfermedad a partir de un valor dentro de rango"

escalate_when:
  - "resultado marcadamente fuera de rango"
  - "síntomas o contexto clínico preocupante concurrente"
  - "discordancia relevante con biomarcadores combinados obligatorios"
```

**Nota de retrofit:** este bloque RAG_INSTRUCTIONS fue añadido en la segunda auditoría (schema v2). El contenido
clínico de la ficha (secciones 1-10 arriba) no cambió — sigue siendo el mismo verificado en la primera entrega.
Este archivo cumple el schema nuevo en su estructura de metadatos y seguridad, pero su encabezado de secciones
(A-N según spec del prompt maestro) todavía usa la numeración original 1-10; la re-escritura completa a
encabezados A-N está en el próximo lote — el contenido y las reglas de seguridad ya son equivalentes.
