**SALUDLY BRAIN**

**06 — Experiencia del usuario / UX**

*Qué ve y qué hace cada persona que toca Saludly · versión 1 · 6 de octubre de 2026*

# **06.1 — Principio**

El paciente solo da la muestra, abre el dashboard y lee sus mensajes. Todo lo demás lo hacen la enfermera, operaciones y el médico, cada uno con su herramienta.

# **06.2 — El recorrido del paciente**

| Momento | Qué pasa | Canal |
| :---- | :---- | :---- |
| Antes de la visita | Recordatorio: ayuno de 8 a 12 horas, visita en la mañana, primera orina del día, muestra de heces con el kit | WhatsApp |
| Visita | La enfermera toma las muestras, mide presión, peso, talla y cintura, hace el cuestionario, pregunta el objetivo de salud y recoge las firmas | En casa |
| Espera | Aviso de que las muestras llegaron al laboratorio | WhatsApp |
| Resultado listo | Aviso con enlace al dashboard (salvo nivel 3, que va por llamada) | WhatsApp |
| Lectura | Informe en seis partes | Dashboard web |
| Semanas siguientes | Recomendaciones según su objetivo | WhatsApp |
| Opcional | Conectar Apple Watch desde la app de Saludly para iPhone | App iOS |

# **06.3 — Acceso al dashboard**

Sin registro ni contraseña. El aviso de WhatsApp trae un enlace único; al abrirlo, el paciente recibe un código de un solo uso por WhatsApp y confirma su fecha de nacimiento. La sesión dura lo suficiente para leer y se puede volver a abrir con el mismo método.

# **06.4 — Pantallas del paciente**

1. **Inicio.** Resumen general en tres o cuatro frases, su objetivo de salud y el paso siguiente más importante.
2. **Lo que está bien.** Lo favorable, primero y en serio: no como relleno.
3. **Lo que merece atención.** Hallazgos ordenados por escalamiento, cada uno con su nivel de lenguaje y una línea de "por qué".
4. **Qué podría significar.** Explicación sencilla, con la incertidumbre dicha en voz alta.
5. **Qué puedes hacer.** Recomendaciones agrupadas por tipo (alimentación, actividad, sueño, hidratación, hábitos, vitaminas y terapias), ordenadas por su objetivo.
6. **Cuándo consultar.** Qué conviene llevarle al médico y en qué plazo.
7. **Todos mis resultados.** El catálogo completo: valor, unidad, intervalo del laboratorio y clase (bajo, limítrofe, en rango, alto, no interpretable), con filtros por módulo y por clase, y una ficha corta de cada biomarcador.
8. **Edad biológica.** Pantalla aparte, presentada como estimación de un modelo publicado, nunca como diagnóstico.
9. **Mi objetivo.** Ver y cambiar el objetivo principal y el secundario.
10. **Apple Watch.** Estado de la conexión (activa, última sincronización) y cómo desconectarla. Si no tiene iPhone, la pantalla lo explica y no insiste.

# **06.5 — Herramientas internas**

| Rol | Herramienta | Qué hace |
| :---- | :---- | :---- |
| Enfermera | Formulario en celular o tableta | Perfil (fecha de nacimiento, sexo, embarazo, fecha de última menstruación, anticonceptivo, ciudad, tabaquismo), cuestionario (medicamentos, antecedentes, FINDRISC, alcohol, suplementos, síntomas, confusores recientes), medidas, objetivo y firmas. Funciona sin conexión y sincroniza después |
| Operaciones | Panel de órdenes | Carga del PDF, verificación de identidad y orden, estado de cada informe, reintentos |
| Médico | Vista clínica | Valores con clase, hallazgos con guía, reflejas, conflictos entre guías, datos faltantes, preguntas para el profesional, aprobación o corrección de textos y mensajes, cola de niveles 2 y 3 |

# **06.6 — Tono**

- Español de Colombia, de tú, frases cortas, sin jerga médica innecesaria; cuando un término importa, se explica.
- Sin alarmismo y sin falsa tranquilidad.
- Primero el hecho, después lo que significa, después qué hacer.
- El objetivo del paciente aparece en el tono (por ejemplo, "para tu meta de correr una maratón…"), nunca para suavizar una alerta.

# **06.7 — Mensajes de WhatsApp**

Todos con plantillas aprobadas por Meta y con opt-in registrado en la visita.

| Tipo | Cuándo | Contenido |
| :---- | :---- | :---- |
| Preparación | 24 horas antes de la visita | Ayuno, horario, orina y heces |
| Muestra recibida | Al llegar al laboratorio | Aviso corto |
| Resultado listo | Cuando el médico aprueba | Enlace al dashboard y una frase de resumen sin datos sensibles |
| Recomendación | Una por semana durante 8 semanas | Una acción concreta, ligada a un hallazgo y a su objetivo |
| Recordatorio de consulta | Para hallazgos de nivel 2 | Sin detalles clínicos; invita a abrir el dashboard |

Nunca por WhatsApp: valores críticos, serologías reactivas ni diagnósticos.

# **06.8 — Accesibilidad**

Texto con buen contraste y tamaño ajustable, funcionamiento en celular primero, colores que nunca son la única señal (cada clase lleva también su palabra), y lectura compatible con lectores de pantalla.

# **06.9 — Estados vacíos y errores**

- Sin Apple Watch: el informe se ve completo y no hay mensajes que lo echen de menos.
- Dato faltante: se dice qué falta y por qué importa.
- Resultado no interpretable: se explica la razón (por ejemplo, muestra hemolizada) y qué sigue.
- Informe en revisión: "Tu médico está revisando tus resultados; te avisamos por WhatsApp".
