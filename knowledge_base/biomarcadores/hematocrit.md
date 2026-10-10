---
doc_id: SLD-BIO-002
biomarker_id: hematocrit
name_es: Hematocrito
name_en: Hematocrit
abbreviation: Hto / Hct
sinonimos:
- Hematocrito
- Hto
- HCT
- Hto / Hct
- Hematocrit
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-012
- COND-M3-HE-007
- REL-029
combine_with:
- hemoglobin
- mcv
- erythrocytes
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

# Hematocrito (Hto)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-012. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-002. Hto/Hct. Categoría: Hematología. Tipo: analito medido (algunos analizadores lo calculan a partir del conteo eritrocitario y el VCM — Saludly debe registrar el método del laboratorio aliado). Tier 1.

## B. Definición

Proporción del volumen sanguíneo total ocupada por eritrocitos. Se mueve en paralelo con la hemoglobina en la gran mayoría de condiciones y se interpreta siempre junto a ella.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo (CBC) · Tubo EDTA · Método: centrifugación (microhematocrito) o, más frecuentemente hoy, cálculo automatizado por citometría de flujo a partir de VCM × conteo eritrocitario. Unidad: % (o fracción decimal L/L). No requiere ayuno. Factor preanalítico: hemodilución/hemoconcentración (igual que hemoglobina).

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método, ajustado por sexo/edad/altitud — mismo racional que hemoglobina (ver `hemoglobin.md`).
- **Clinical decision threshold:** el hematocrito no tiene un umbral OMS 2024 propio e independiente — se deriva del umbral de hemoglobina (relación aproximada Hto ≈ Hb × 3). Usando los umbrales OMS 2024 verificados en `hemoglobin.md` (WHO 2024, https://www.ncbi.nlm.nih.gov/books/NBK499994/): hombres <~39%, mujeres no embarazadas <~36%, embarazo <~33% (1er/3er trimestre) — **estas son aproximaciones derivadas de la relación Hb×3, no umbrales OMS medidos directamente para hematocrito**, y deben tratarse con esa calibración de confianza menor.

## E. Interpretación

- Prácticamente siempre se interpreta en paralelo con hemoglobina — un hematocrito bajo sin hemoglobina baja concurrente (o viceversa) es infrecuente y sugiere revisar la muestra o el analizador.
- Elevado: policitemia, deshidratación (hemoconcentración falsa).
- Disminuido: anemia, hemodilución (embarazo, sobrehidratación IV).

## F. Contexto del paciente y confusores

### Contexto del paciente

Igual que hemoglobina: sexo, embarazo, edad, altitud de residencia, estado de hidratación.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Hemoglobina (obligatorio — se interpretan como una unidad), VCM, conteo de eritrocitos.
- `cannot_conclude`: causa de la anemia/policitemia sin el resto del hemograma.

## H. Tendencias

### Tendencias temporales

Sigue la misma tendencia que hemoglobina — un cambio en uno sin el otro debe generar sospecha de error preanalítico o de laboratorio antes que interpretación clínica.

## I. Prevención

Mismas acciones que hemoglobina.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna adicional a las ya indicadas para hemoglobina — hematocrito y hemoglobina se solicitan y evalúan siempre juntos dentro del hemograma.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del hemograma de cribado básico — no diagnóstico aislado de ninguna condición.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar, ampliamente reproducido.
- **Fuente:** derivada de WHO 2024 (ver `hemoglobin.md`) mediante la relación Hto ≈ Hb × 3 — no existe una guía OMS que mida hematocrito de forma independiente para definir anemia; el hematocrito es tradicionalmente un derivado clínico de la hemoglobina, no un criterio primario separado.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** interpretación siempre acoplada a hemoglobina — nunca se genera una inferencia de hematocrito de forma verdaderamente aislada.
- **prohibited_inferences:** cualquier diagnóstico de causa de anemia/policitemia sin el resto del hemograma.
- **uncertainty_notes:** discordancia entre hematocrito y hemoglobina (fuera de la relación esperada ~3:1) sugiere revisar calidad de la muestra antes que asumir hallazgo clínico real.
- **professional_review:** igual criterio que hemoglobina.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - anemia_screening
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando hemograma completo"
  - "evaluando anemia o policitemia junto con hemoglobina"

combine_with: [hemoglobin, mcv, erythrocytes]

do_not_use_alone:
  - "cualquier interpretación sin hemoglobina concurrente"

do_not_conclude:
  - "causa específica de anemia o policitemia sin panel completo"

escalate_when:
  - "valores muy bajos o muy altos"
  - "discordancia inesperada con hemoglobina (sugiere error de muestra/analizador)"
```
