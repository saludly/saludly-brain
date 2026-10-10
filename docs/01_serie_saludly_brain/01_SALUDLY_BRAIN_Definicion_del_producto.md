**SALUDLY BRAIN**

**01 — Definición del producto**

*Qué es Saludly Brain, para quién es y qué hace y no hace · versión 1 · 6 de octubre de 2026*

# **01.1 — Qué es**

Saludly Brain es el motor que convierte los resultados de una sola toma de sangre, orina y heces en una visión preventiva de la salud de una persona. Recibe el PDF del laboratorio aliado, lo convierte en datos, busca patrones entre más de 100 biomarcadores con reglas tomadas de guías clínicas, y entrega un informe sencillo en el dashboard web y recomendaciones por WhatsApp.

No es un diagnóstico. Cada hallazgo es una asociación con un nivel de coincidencia y una recomendación de seguimiento; el diagnóstico siempre lo hace un médico.

# **01.2 — El problema**

La mayoría de las enfermedades crónicas que más pesan en Colombia (diabetes, enfermedad cardiovascular, enfermedad renal, hígado graso, anemia, tiroides) se pueden sospechar años antes con exámenes de laboratorio. Hoy esas señales se pierden porque las pruebas se piden por partes, se leen una por una y nadie cruza los resultados entre sí.

# **01.3 — Para quién**

| Actor | Qué necesita | Qué le da Saludly Brain |
| :---- | :---- | :---- |
| Paciente | Saber a tiempo si algo anda mal, sin trámites | Una sola toma en casa, un informe que entiende y recomendaciones que puede seguir |
| Médico | Ver el panorama completo del paciente | Hallazgos ordenados por prioridad, con su guía, sus datos faltantes y lo que conviene confirmar |
| EPS | Bajar el costo de la UPC a largo plazo | Detección temprana de riesgos reales en su población afiliada, con aprobación previa de cada paciente |
| Equipo de Saludly | Operar con calidad y trazabilidad | Flujo controlado desde la carga del PDF hasta el mensaje, con aprobación médica |

# **01.4 — Qué hace el paciente**

Nada más que tres cosas: dar la muestra en su casa (en ayunas y en la mañana), abrir el dashboard y recibir los mensajes de WhatsApp. La enfermera toma en la visita los datos de perfil, el cuestionario, las medidas, el objetivo de salud y los consentimientos. Si el paciente tiene Apple Watch, puede conectarlo desde la app de Saludly para iPhone; es opcional.

# **01.5 — Qué entrega la versión 1**

| Elemento | Alcance |
| :---- | :---- |
| Catálogo | 99 analitos medidos, 12 calculados y la edad biológica (PhenoAge): 111 valores por mujer y 109 por hombre, más 18 pruebas reflejas que el laboratorio corre solo cuando un resultado las activa |
| Conocimiento clínico | 12 especialidades en 6 módulos, 50 condiciones incluidas y 26 de apoyo, más las relaciones entre módulos |
| Informe | Seis partes: resumen general, lo que está bien, lo que merece atención, qué podría significar, qué puedes hacer y cuándo consultar |
| Vista médica | Valores, clasificación, guías, reflejas, conflictos entre guías, datos faltantes y preguntas para el profesional |
| Recomendaciones | Alimentación, hidratación, actividad física, sueño, hábitos, actividades saludables, vitaminas y terapias, ordenadas según el objetivo de salud |
| Canales | Dashboard web; WhatsApp Business (API oficial); app para iPhone solo para conectar Apple Health |
| Wearables | Apple Watch a través de Apple Health, opcional |

# **01.6 — Qué no hace**

- No diagnostica ni le dice a nadie "tienes" una enfermedad.
- No prescribe medicamentos ni da dosis de suplementos.
- No reemplaza la consulta médica ni el tratamiento que el paciente ya tiene.
- No entrega por WhatsApp resultados críticos ni serologías reactivas: esos los comunica el equipo médico por llamada.
- No detecta enfermedades con el reloj: los datos del wearable son contexto, nunca umbral.
- No mide VIH, sífilis, clamidia ni gonorrea (decisión del 6 de octubre de 2026, por el Decreto 1543 de 1997).

# **01.7 — Principios del producto**

1. Los valores medidos salen del laboratorio; Saludly no inventa ni completa datos.
2. Las reglas deciden qué se cumple; el modelo de lenguaje solo redacta y explica.
3. Un patrón exige al menos dos señales concordantes; un valor aislado nunca es una enfermedad.
4. Cada hallazgo se puede rastrear hasta sus valores, su regla y su guía.
5. Lo que llega al paciente pasa antes por un médico mientras dure el piloto.
6. El objetivo de salud cambia el orden de las recomendaciones, nunca las alertas.
7. Ante la duda, se escala a un profesional.

# **01.8 — Cómo se mide el éxito**

| Métrica | Para qué |
| :---- | :---- |
| Concordancia médico-agente en los hallazgos | Saber si el motor razona como el médico |
| Errores de extracción por PDF | Saber si los datos de entrada son confiables |
| Tiempo de la toma al informe | Saber si el servicio es oportuno |
| Pacientes con hallazgos de escalamiento 2 o 3 que consultaron | Saber si la detección se convierte en atención |
| Seguimiento de recomendaciones (con wearable, pasos y sueño) | Saber si las recomendaciones cambian hábitos |
| Costo por paciente | Saber si el modelo con EPS es viable |

# **01.9 — Glosario**

- **Analito medido:** valor que reporta el laboratorio.
- **Calculado:** valor que Saludly deriva de otros (por ejemplo, HOMA-IR o la TFG estimada).
- **Prueba refleja:** prueba que el laboratorio corre sobre la misma muestra solo si un resultado la activa.
- **Condición incluida:** hallazgo que aparece en el informe con su propio nombre.
- **Condición de apoyo:** señal que modifica otra condición pero no aparece sola.
- **Vigilar:** relación con evidencia de asociación, que se muestra como seguimiento y nunca como condición.
- **Nivel de coincidencia:** alta, moderada o baja, según cuántos criterios se cumplen y qué tan completos están los datos.
- **Escalamiento:** de 0 a 3, qué tan pronto debe intervenir un profesional.

# **Relación con los demás documentos**

01 define el producto · 02 cómo funciona · 03 el conocimiento clínico · 04 el motor · 05 la seguridad · 06 la experiencia · 07 las recomendaciones · 08 los datos e integraciones · 09 el modelo de negocio · 10 la especificación para desarrollo.
