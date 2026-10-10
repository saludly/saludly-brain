**SALUDLY BRAIN**

**09 — Modelo de negocio / producto comercial**

*Quién paga, por qué y qué hay que demostrar · versión 1 · 6 de octubre de 2026*

> Este documento no incluye precios ni costos porque todavía no hay cotización del laboratorio ni piloto. Las cifras se llenan con datos reales, no con supuestos.

# **09.1 — La tesis**

Detectar a tiempo riesgos reales de enfermedades crónicas, y tratarlos oportunamente, cuesta menos que atenderlas cuando ya están avanzadas. Por eso la EPS paga el servicio por paciente con cargo a la UPC, siempre con aprobación previa del paciente.

# **09.2 — Actores y propuesta de valor**

| Actor | Rol | Qué gana |
| :---- | :---- | :---- |
| EPS | Paga por paciente | Detección temprana en su población, priorización de quién necesita atención y, según la tesis, menor costo a largo plazo |
| Paciente | Recibe el servicio | Un chequeo completo en casa, sin trámites, con explicaciones claras y recomendaciones según su objetivo |
| Médico | Usa la información | Panorama completo y priorizado del paciente |
| Laboratorio aliado | Procesa las muestras | Volumen de pruebas y pruebas reflejas |

# **09.3 — El producto que se vende**

- Toma domiciliaria en ayunas por enfermera certificada, con medidas físicas.
- Catálogo de más de 100 biomarcadores por persona (111 en mujeres, 109 en hombres), más pruebas reflejas cuando se activan.
- Informe en seis partes y vista médica.
- Recomendaciones por WhatsApp durante 8 semanas, según el objetivo de salud.
- Conexión opcional con Apple Watch.
- Llamada del equipo médico para hallazgos urgentes.

**Promesa comercial:** "más de 100 biomarcadores", que se puede defender contando uno por uno. Las reflejas no se cuentan porque no las recibe todo el mundo.

# **09.4 — Estructura de costos (rubros, sin cifras)**

| Rubro | Depende de |
| :---- | :---- |
| Pruebas de laboratorio | Cotización del catálogo y de las 18 reflejas |
| Visita de enfermería | Tiempo, desplazamiento, kit y centrífuga portátil |
| Cadena de frío y transporte | Nevera a 2 °C y transporte congelado para vitamina C |
| Modelo de lenguaje | Tokens por informe en pruebas; servidores con GPU en operación |
| Infraestructura | VPS de Hostinger, almacenamiento, copias de seguridad |
| WhatsApp | Conversaciones de la API oficial |
| Revisión médica | Horas de médico por informe, sobre todo en el piloto |
| Desarrollo y mantenimiento | Equipo técnico, app iOS, actualización del Knowledge Base |

# **09.5 — Lo que hay que demostrar en el piloto**

| Pregunta de la EPS | Dato del piloto que la responde |
| :---- | :---- |
| ¿Encuentra algo que no sabíamos? | Hallazgos de nivel 1, 2 y 3 por cada 100 pacientes |
| ¿Los hallazgos son correctos? | Concordancia médico-agente |
| ¿Los pacientes actúan? | Porcentaje de hallazgos de nivel 2 y 3 que terminan en consulta |
| ¿Cambian hábitos? | Seguimiento de recomendaciones; pasos y sueño en quienes tienen Apple Watch |
| ¿Cuánto cuesta? | Costo por paciente con todos los rubros |
| ¿Ahorra? | No se puede demostrar en un piloto corto; se propone medir uso de servicios en los meses siguientes |

# **09.6 — Ruta comercial**

1. Piloto controlado con pacientes con consentimiento.
2. Informe del piloto con los datos de 09.5.
3. Propuesta a EPS con la ruta legal ya aprobada por el abogado de Saludly.
4. Contrato por paciente atendido, con aprobación previa de cada paciente.
5. Medición de resultados en la población de la EPS para sostener la tesis de ahorro.

# **09.7 — Riesgos de negocio**

- El ahorro en la UPC es una tesis: tarda en verse y hay que medirlo.
- Más biomarcadores sube el costo por paciente; el catálogo debe justificar cada prueba.
- Un hallazgo falso de nivel 2 o 3 daña la confianza de la EPS más que un hallazgo omitido de nivel 1.
- La dependencia de un solo laboratorio aliado.
