# codigo/pipeline · Comando de punta a punta (MVP)

PDF del laboratorio → lector → motor → informe para el dashboard, mensajes de WhatsApp y resumen en Markdown.

```bash
python saludly.py --pdf resultado.pdf --documento "CC 0000000001" --orden LCD-2026-100123 \
                  --perfil perfil.json --enfermera enfermera.json --salida salida/
```

| Entrada | Quién la da | Contenido |
|---|---|---|
| PDF | Laboratorio, por la plataforma o por correo | Resultados, edad, sexo, horas de ayuno y hora de toma. **No se guarda** |
| `--documento` y `--orden` | Operaciones | Tienen que coincidir con el PDF; si no, se rechaza (código 2) |
| `perfil.json` | Paciente, en la PWA | `{"objetivos": [3 de los 10 de knowledge_base/fase5/objetivos.yaml], "toma_biotina": true o false, "nivel_actividad": "sedentario", "ligero", "moderado" o "alto"}` |
| `enfermera.json` | Enfermera, como datos complementarios | Presión, cintura, peso, talla y, si los toma, tabaquismo, medicamentos, suplementos, embarazo, fecha de última menstruación, anticonceptivo y ciudad (Bogotá por defecto) |

**Salida:** `INF-<orden>-v1.json` (el informe) y `INF-<orden>-v1.md` (el resumen de lo extraído). El paciente va con un seudónimo (`P-XXXXXXXX`, sacado del documento y de la variable `SALUDLY_SAL_SEUDONIMO`); el nombre y el documento nunca salen.

## Qué trae el informe (contrato del documento 10.5, ampliado)

| Campo | Para qué |
|---|---|
| `paciente.resumen`, `lo_que_esta_bien`, `lo_que_merece_atencion`, `que_podria_significar`, `que_puedes_hacer`, `cuando_consultar`, `informativos` | Las 6 partes del informe en idioma paciente, con los valores reales del paciente |
| `resultados` | Pantalla "Todos mis resultados": valor, unidad, intervalo y clase de cada biomarcador |
| `edad_biologica` | Pantalla aparte (PhenoAge) |
| `nutricion` | Meta diaria orientativa (calorías y macronutrientes), restricciones por hallazgo y el plan de recetas |
| `whatsapp` | Aviso de resultado listo, recordatorio de consulta (nivel 2), una recomendación por semana durante 8 semanas y una receta por día |
| `medico` | Vista clínica: hallazgos con criterios y guías, reflejas pendientes, datos faltantes, qué confirmar, preguntas para el profesional |
| `estado` | `en_revision` (el médico revisa todo en el piloto), `requiere_revision` (el control de salida encontró algo) o `retenido_hasta_llamada` (escalamiento 3 o serología reactiva: nada sale por WhatsApp hasta la llamada) |
| `control_salida` | Problemas de lenguaje encontrados y hallazgos sin texto |

## Cómo se redacta

Hoy con **plantillas** de `knowledge_base/fase5/` (decisión de Carlos: plantillas ahora y DeepSeek después). Todo texto pasa por `codigo/informe/control_salida.py`, que bloquea diagnósticos, dosis, porcentajes de riesgo, falsas tranquilidades y las frases prohibidas de cada ficha. El objetivo del paciente solo cambia el orden de las recomendaciones, nunca los hallazgos.

## Pruebas

```bash
python pruebas/probar_pipeline.py      # 76 comprobaciones con los dos PDF de ejemplo
python ../herramientas/validar_fase5.py
```

## Ejemplos

`ejemplos/` tiene los informes generados con los dos PDF sintéticos (hombre de 46 años con metas de bajar de peso, energía y prevención; mujer de 34 años con metas de energía, maratón y salud general), con sus `perfil_*.json` y `enfermera_*.json`. Son datos inventados: sirven para que el dashboard se construya contra el formato real del informe.
