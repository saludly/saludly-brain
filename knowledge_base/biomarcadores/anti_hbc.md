---
doc_id: SLD-BIO-108
biomarker_id: anti_hbc
name_es: Anticuerpos totales contra el antígeno core de hepatitis B
name_en: Total hepatitis B core antibody
abbreviation: Anti-HBc total
sinonimos:
- Anti-HBc total
- Anti core hepatitis B
- AcHBc total
- HBcAb total
- Anticuerpos totales contra core hepatitis B (anti-HBc)
- Anticuerpos totales contra core hepatitis B
category: Infecciosas
parameter_type: measured_analyte
tipo_resultado: cualitativo (reactivo / no reactivo) con índice
unidad_canonica: índice
specimen: Suero
nivel_catalogo: con patrón
panel: estándar, todas las personas, con consentimiento
alimenta:
- COND-M4-IN-002
tier: 1
status: BORRADOR
schema_version: '2.1'
clinical_priority: high
requires_professional_review: true
source_version: 2026-10
fuentes_estado: por verificar
---

# SLD-BIO-108 · Anticuerpos totales contra el core de hepatitis B (anti-HBc)

## A. Identificación
Inmunoensayo que detecta anticuerpos (IgG e IgM) contra el núcleo del virus de la hepatitis B.

## B. Definición
Indica infección pasada o actual; la vacuna no lo produce. Es la prueba que separa la inmunidad por vacuna de la inmunidad por infección.

## C. Espécimen y toma
Suero, sin ayuno específico.

## D. Intervalos y umbrales
Reactivo o no reactivo según el índice y el corte del fabricante.

## E. Interpretación
Reactivo con HBsAg no reactivo y anti-HBs protector: infección pasada resuelta. Reactivo aislado (HBsAg y anti-HBs negativos): varias interpretaciones posibles (infección resuelta con anticuerpos que bajaron, falso positivo, infección oculta); requiere evaluación médica.

## F. Contexto del paciente y confusores
Falsos positivos con índices bajos; transfusiones recientes.

## G. Relaciones
Siempre con HBsAg y anti-HBs (IN-002).

## H. Tendencias
Persiste de por vida tras la infección.

## I. Prevención
Importante si la persona va a recibir inmunosupresión o quimioterapia: hay riesgo de reactivación.

## J. Pruebas complementarias
Carga viral de hepatitis B ante anti-HBc aislado, según el médico.

## K. Cuándo no interpretar / cuándo escalar
Anti-HBc aislado: escalamiento 2 con llamada. Infección pasada resuelta: escalamiento 1 con nota de reactivación (IN-002).

## L. Evidencia
CDC 2023. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "señal de una infección por hepatitis B, actual o pasada".
- Inferencias prohibidas: infección activa sin HBsAg, contagio.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_b, serologia, panel_estandar, saludly_brain_v1]
use_when: ["interpretar el panel de hepatitis B", "riesgo de reactivación con inmunosupresión"]
combine_with: [hbsag, anti_hbs]
do_not_use_alone: ["afirmar infección activa"]
do_not_conclude: ["infección activa sin HBsAg"]
escalate_when: ["anti-HBc aislado", "anti-HBc reactivo con inmunosupresión declarada"]
```
