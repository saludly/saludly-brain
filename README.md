# Saludly Brain

Agente de IA médico de **Saludly**, empresa de salud preventiva con sede en Bogotá.

Saludly toma una sola muestra de sangre a domicilio; un laboratorio aliado la procesa y envía un PDF con los resultados. Saludly Brain lee ese PDF, busca patrones entre más de 100 biomarcadores apoyado en guías clínicas y entrega al paciente un informe preventivo en el dashboard web, con recomendaciones que también le llegan por WhatsApp. Ningún hallazgo es un diagnóstico: cada uno es un resultado observado, un patrón compatible, un riesgo potencial o una condición que requiere evaluación médica.

## Cómo funciona

```
PDF del laboratorio → Lector (extrae y normaliza) → Motor de reglas (cálculos, condiciones, relaciones, seguridad)
                    → LLM (solo redacta) → Informe en 6 partes (dashboard) + recomendaciones (WhatsApp)
```

Principio de diseño: **los umbrales los evalúa el código, no el LLM.** El motor decide qué se cumple y con qué nivel; el modelo de lenguaje (DeepSeek) solo redacta, con datos seudonimizados y un control de salida que bloquea las frases prohibidas.

## Estado del proyecto (10 de octubre de 2026)

| Fase | Qué es | Estado |
|---|---|---|
| 0 | Definiciones de producto y clínica | Hecha en versión 1. Falta la firma del médico revisor |
| 1 | Knowledge Base ejecutable | Hecha: 144 fichas de biomarcador, 86 de condición, 31 relaciones y 15 fichas de seguridad (ampliada el 10 de octubre de 2026) |
| 2 | Servidor: OpenClaw en Hostinger con DeepSeek | **Siguiente paso.** Espera la compra del plan |
| 3 | Lector del PDF | Hecho. Lee el 100 % de los campos del PDF de ejemplo |
| 4 | Motor de análisis | Hecho. Pasa 662 de 662 pruebas. En el MVP trabaja solo con sangre (orina y heces en pausa) |
| 5 | Recomendaciones e informe | Hecha con plantillas: 119 textos para el paciente, 189 recomendaciones, 190 recetas y el comando de punta a punta. DeepSeek, después |
| 6 | Dashboard web, formulario de la enfermera y app iOS mínima | Pendiente |
| 7 | WhatsApp Business (API oficial) | Pendiente |
| 8 | Piloto controlado | Pendiente |
| 9 | Escala y modelo con EPS | Pendiente |

**Pendientes que no son técnicos:** la firma del médico (decisiones clínicas y casos de prueba), el formato real del PDF del laboratorio, la cotización y validación del protocolo de toma, el formulario de la visita de la enfermera y la consulta legal sobre el INVIMA.

## Carpetas

| Carpeta | Para qué sirve |
|---|---|
| [`docs/`](docs/README.md) | Documentación del producto: la serie Saludly Brain 01 a 10, el plan, la investigación clínica, las fichas compiladas y los informes de pruebas |
| [`knowledge_base/`](knowledge_base/00_INDEX.md) | Conocimiento clínico en formato que el código lee: fichas con encabezado YAML más texto. Es la fuente de verdad clínica |
| [`codigo/motor/`](codigo/motor/README.md) | Motor de análisis en Python (incluye una copia del lector) con sus pruebas |
| [`codigo/lector_pdf/`](codigo/lector_pdf/README.md) | Lector del PDF como módulo independiente, con sus pruebas propias |
| [`codigo/pipeline/`](codigo/pipeline/README.md) | Comando de punta a punta: PDF → informe JSON para el dashboard, WhatsApp y resumen en Markdown |
| `pdf_ejemplo/` | Los dos PDF de ejemplo que inventó Saludly (hombre de 46 años y mujer de 34) y el script que los genera |
| `_archivo/` | Zips originales, versiones anteriores y duplicados. No se usa para trabajar; se conserva por si hace falta recuperar algo |

## Correr las pruebas

Hace falta Python 3.10 o superior.

```bash
pip install -r codigo/requirements.txt
cd codigo/motor
python pruebas/probar_todo.py
```

Resultado esperado: `TOTAL: 662 de 662`.

## Stack decidido

- **Agente:** OpenClaw en un VPS de Hostinger
- **LLM:** DeepSeek (`deepseek-v4-pro` o Flash) para las pruebas; modelos locales con GPU en operación
- **Embeddings:** locales, para que las fichas no salgan del servidor
- **Wearables:** primero Apple Watch, a través de Apple Health, con una app iOS mínima
- **Mensajería:** WhatsApp Business Platform (API oficial de Meta)

El detalle está en [docs/02_plan_y_decisiones/Saludly_Plan_de_implementacion.md](docs/02_plan_y_decisiones/Saludly_Plan_de_implementacion.md).
