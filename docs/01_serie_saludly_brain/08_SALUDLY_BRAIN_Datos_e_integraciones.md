**SALUDLY BRAIN**

**08 — Datos, integraciones y evolución futura**

*Qué datos maneja Saludly, de dónde vienen y hacia dónde crece · versión 1 · 6 de octubre de 2026*

# **08.1 — Entidades de datos**

| Entidad | Qué guarda | Origen |
| :---- | :---- | :---- |
| Paciente | Identificador interno, nombre, documento, fecha de nacimiento, sexo, teléfono, aseguradora | Agendamiento y visita |
| Consentimiento | Tipo, versión del texto, fecha, firma, estado (vigente o revocado) | Visita y app iOS |
| Visita | Fecha, hora, enfermera, medidas (presión, peso, talla, cintura), cuestionario, confusores, objetivo | Formulario de la enfermera |
| Orden | Número de orden, visita, laboratorio, fechas de toma, recepción y validación | PDF |
| Documento de resultados | PDF original, huella (hash), quién lo cargó, metadatos del PDF | Operaciones |
| Resultado | Biomarcador, valor original, unidad original, valor y unidad canónicos, intervalo, indicador del laboratorio, método, estado del dato, clase | Ingesta y motor |
| Derivado | Biomarcador calculado, valor, fórmula, versión y resultados de origen | Motor |
| Lectura de wearable | Tipo de dato, valor, periodo, fuente (reloj, tensiómetro), fecha de sincronización | App iOS |
| Hallazgo | Condición o relación, criterios cumplidos, coincidencia, escalamiento, nivel de lenguaje, guía | Motor |
| Recomendación | Identificador del catálogo, hallazgo que la activa, prioridad, texto final | Motor y agente |
| Informe | Seis partes, vista médica, versión, estado (borrador, en revisión, aprobado, publicado) | Agente y médico |
| Mensaje | Plantilla, texto, destinatario, estado de envío, aprobación | Agente, médico y WhatsApp |
| Auditoría | Quién, qué, cuándo, desde dónde | Todo el sistema |

# **08.2 — Integración con el laboratorio**

**Hoy.** El laboratorio aliado todavía no entrega formato. Saludly creó su propio PDF de ejemplo con el estilo habitual de los informes de laboratorio en Colombia: encabezado con razón social, NIT y código de habilitación; bloque del paciente con documento, edad, aseguradora, orden, ayuno y fechas de toma, recepción y validación; secciones por área con columnas de examen, resultado, indicador, unidad, valores de referencia y método; pruebas reflejas identificadas; observaciones; y firma del profesional que valida. El PDF trae además metadatos legibles por máquina (título, asunto y palabras clave con orden, documento, sexo y versión de formato).

**Archivos de ejemplo:** orden LCD-2026-100123 (hombre, 46 años) y orden LCD-2026-100124 (mujer, 34 años). Juntos cubren patrones cardiometabólico, hepático y renal, déficit de hierro con anemia, tiroides autoinmune con reflejas, Lp(a) alta, valores menores que el límite, un resultado hemolizado no procesado, una muestra no apta, vitaminas sin intervalo y un ANA positivo.

**Después.** Cuando el laboratorio entregue su formato, el lector se ajusta y se repiten las pruebas. A mediano plazo, conviene pedir una entrega estructurada (archivo de datos o interfaz HL7 o FHIR) para no depender de leer PDF.

# **08.3 — Apple Watch (primera integración de wearable)**

Apple Health guarda los datos en el iPhone y no tiene interfaz web, así que la integración necesita una app de Saludly para iPhone. La app es mínima: inicio de sesión con el mismo método del dashboard, permiso de Apple Health, sincronización en segundo plano y estado de la conexión.

| Dato | Tipo en HealthKit | Uso |
| :---- | :---- | :---- |
| Pasos | stepCount | Recomendaciones de actividad |
| Frecuencia cardíaca en reposo | restingHeartRate | Contexto cardiovascular y de recuperación |
| Variabilidad de la frecuencia cardíaca | heartRateVariabilitySDNN | Contexto de recuperación |
| VO2 máx estimado | vo2Max | Contexto para objetivos deportivos |
| Sueño | sleepAnalysis | Recomendaciones de sueño |
| Temperatura de muñeca durante el sueño | appleSleepingWristTemperature | Contexto del ciclo |
| Presión arterial (de tensiómetro conectado o registro manual) | bloodPressureSystolic, bloodPressureDiastolic | Automonitoreo para confirmar la sospecha de hipertensión |
| Peso (de báscula conectada) | bodyMass | Seguimiento del objetivo de bajar de peso |

**Presión arterial: lo que el reloj sí y no hace.** El Apple Watch no mide la presión arterial; puede enviar una notificación cuando detecta patrones de hipertensión y luego pide registrar la presión con un tensiómetro durante 7 días. Esos registros sí quedan en Apple Health y Saludly los puede leer. Falta verificar si la notificación misma es legible por apps de terceros y si la función está disponible en Colombia.

**Otros wearables.** Android (Health Connect, que también exige app) y marcas con interfaz en la nube quedan para una fase posterior.

# **08.4 — WhatsApp**

WhatsApp Business Platform (API oficial de Meta), con número verificado de Saludly, plantillas aprobadas y opt-in registrado. El canal de WhatsApp que trae OpenClaw (vinculado por código QR a una cuenta normal) no se usa con pacientes. La conexión entre OpenClaw y la API oficial se define en una prueba de concepto.

# **08.5 — Modelo de lenguaje**

| Etapa | Proveedor | Condición |
| :---- | :---- | :---- |
| Pruebas | DeepSeek por API en la nube, a través del proveedor oficial de OpenClaw | Transferencia de datos aprobada por el abogado; datos seudonimizados |
| Operación | Modelos locales de pesos abiertos en servidores con GPU | Deben pasar los mismos casos de prueba antes del cambio |

Hostinger ofrece hoy instancias con GPU que se cobran por hora, separadas de los VPS; el tamaño, el costo de tenerlas encendidas todo el tiempo y la alternativa de otros proveedores se evalúan antes de operar. OpenClaw admite servidores locales compatibles con OpenAI, así que el cambio es de configuración.

# **08.6 — Ambientes**

| Ambiente | Datos | Uso |
| :---- | :---- | :---- |
| Desarrollo | Sintéticos (PDF de ejemplo y casos) | Construir |
| Pruebas | Sintéticos | Correr el set de casos en cada cambio |
| Producción | Reales | Piloto y operación |

Ningún dato real entra a desarrollo ni a pruebas.

# **08.7 — Evolución futura**

1. **Tendencias.** Con una segunda toma, comparar resultados en el tiempo (las fichas ya traen su sección de tendencias; la Lp(a) se mide una vez en la vida).
2. **Entrega estructurada del laboratorio** en vez de PDF.
3. **Android y otros wearables.**
4. **Integración con las EPS** para recibir afiliados autorizados y devolver resultados.
5. **Interoperabilidad con la historia clínica** si las EPS lo exigen.
6. **Segundo laboratorio**, con su propio formato y la advertencia de no comparar resultados entre laboratorios sin aviso.
