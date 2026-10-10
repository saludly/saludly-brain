---
doc_id: SLD-BIO-017
biomarker_id: mpv
name_es: VPM
name_en: MPV (Mean Platelet Volume)
abbreviation: VPM / MPV
sinonimos:
- VPM
- MPV
- Volumen plaquetario medio
- VPM/MPV (Volumen Plaquetario Medio)
- VPM / MPV
- MPV (Mean Platelet Volume)
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: fL
specimen: Sangre total EDTA
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-012
combine_with:
- platelets
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

# VPM (Volumen Plaquetario Medio)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-012. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-017. VPM/MPV. Categoría: Hematología. Tipo: analito medido. Tier 3 — valor limitado sin trombocitopenia/trombocitosis ya documentada.

## B. Definición

Tamaño promedio de las plaquetas. Plaquetas más grandes (VPM alto) suelen ser más jóvenes y recién producidas — útil para orientar si la médula ósea está respondiendo activamente a una trombocitopenia (produciendo plaquetas nuevas más grandes) o si la producción está reducida.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo · Tubo EDTA · Unidad: fL. No requiere ayuno. Factor preanalítico: el VPM tiende a aumentar con el tiempo transcurrido en el tubo EDTA antes del procesamiento — relevante si hay demora en el laboratorio.

## D. Intervalos y umbrales

- **Clinical decision threshold (verificado esta sesión):** rango normal típico **9.2-12.7 fL** según referencia institucional (Johns Hopkins Pathology). Saludly debe validar con el laboratorio aliado dado que MPV tiene variabilidad relevante entre analizadores y es sensible al tiempo de procesamiento (ver limitación ya señalada en esta ficha).
- **URL fuente:** https://pathology.jhu.edu/build/assets/department/files/Core-Lab-Reference-Ranges.pdf — verificado esta sesión (ago-2026).

## E. Interpretación

- Se interpreta principalmente junto a un conteo de plaquetas ya alterado: VPM alto + plaquetas bajas sugiere destrucción periférica con médula respondiendo activamente; VPM normal/bajo + plaquetas bajas sugiere producción medular reducida.
- Sin alteración del conteo de plaquetas, tiene poco valor interpretativo aislado.

## F. Contexto del paciente y confusores

### Contexto del paciente

Los mismos que plaquetas: síntomas de sangrado, medicamentos, antecedente de esplenectomía.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Plaquetas (obligatorio — sin trombocitopenia/trombocitosis, VPM aislado no es informativo).
- `cannot_conclude`: causa específica sin el conteo de plaquetas y contexto clínico.

## H. Tendencias

### Tendencias temporales

Sensible al tiempo de procesamiento de la muestra — un cambio inexplicado puede reflejar demora de laboratorio más que un hallazgo real.

## I. Prevención

Utilidad preventiva mínima aislada.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ninguna adicional específica sin trombocitopenia/trombocitosis ya documentada.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado independiente.

## L. Evidencia

### Evidencia científica

- **Fuente:** Johns Hopkins Pathology, Core Lab Reference Ranges (abril 2025). https://pathology.jhu.edu/build/assets/department/files/Core-Lab-Reference-Ranges.pdf — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "VPM interpretado junto a plaquetas alteradas, para orientar entre destrucción periférica y producción medular reducida".
- **prohibited_inferences:** cualquier interpretación de VPM sin plaquetas alteradas concurrentes.
- **uncertainty_notes:** sensible al tiempo de procesamiento de la muestra.
- **professional_review:** trombocitopenia/trombocitosis marcada con VPM discordante del patrón esperado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - hemostasis
  - tier_3
  - saludly_brain_v1
use_when:
  - "plaquetas ya alteradas, para orientar causa"
combine_with: [platelets]
do_not_use_alone:
  - "cualquier interpretación sin plaquetas alteradas"
do_not_conclude:
  - "causa específica sin conteo de plaquetas y contexto clínico"
escalate_when:
  - "trombocitopenia/trombocitosis marcada con VPM discordante"
```
