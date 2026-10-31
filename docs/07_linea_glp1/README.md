# Línea GLP-1 · Saludly para especialistas en peso

Contexto de esta línea de negocio, abierta el 30 de octubre de 2026. Es una estrategia nueva y paralela a la preventa directa al paciente: aquí el cliente que abre la puerta es **la especialista**, y el paciente llega a través de ella.

Estado: **Fase 1 en curso** (respuestas de Carlos del 30 oct 2026 anotadas abajo).

Archivos de esta línea:

- [`guion_llamada.md`](guion_llamada.md): guion de la llamada de diagnóstico, mensajes de WhatsApp, objeciones y hoja de seguimiento.
- [`oferta_una_hoja.html`](oferta_una_hoja.html): carta de Carlos a la doctora con un ejemplo del resumen antes del control, para mandar por WhatsApp después de la llamada (artifact privado https://claude.ai/artifact/Xc4Du2mswTBE1DWWXDUu19; hay que compartirlo o mandar captura). El enlace acepta el apellido: `…#Gomez` muestra "Doctora Gomez:". Rehecha el 30 oct 2026 tras la revisión de CEO: formato carta, "especialistas fundadoras" en vez de "regalo", modelo de negocio dicho de frente. Firma: Carlos Araujo; falta la foto (la toma el 31 oct).
- [`demo_app_y_dashboard.md`](demo_app_y_dashboard.md): propuesta del demo (app de la paciente estilo iOS con nivel de 0 a 100 y silueta con capa de grasa; dashboard de la doctora con criterios de qué mostrar) y sus preguntas abiertas.
- [`version_funcional.md`](version_funcional.md): criterios clínicos de Para ti, recomendaciones semanales y plan de la versión funcional (Fase 6B · GLP-1) para la primera paciente.
- [`demo_glp1.html`](demo_glp1.html): demo clicable (artifact privado https://claude.ai/artifact/Y9qXyXvrqwfD585gxWSTst) con la vista de la paciente en iPhone y la de la doctora. Se genera desde `demo_glp1.plantilla.html` reemplazando `__FIGURA__` por `figura_mujer.webp.b64` (silueta recortada de `app/src/assets/body-female.png`). El enlace acepta `#Apellido` para el nombre de la doctora.

## La idea en una frase

Una versión de Saludly más simple y visual, pensada primero para **mujeres** en tratamiento con GLP-1 para bajar de peso (después la versión para hombres), que interpreta **solo los exámenes que la especialista ya pidió** con el motor y el RAG de Saludly, más una **automatización personalizada del consultorio** de la doctora. A las 2 primeras doctoras se les **regala** la automatización y una asesoría de contenido en redes.

## Modelo de negocio (30 oct 2026)

- **No cobramos** ni a la doctora ni a sus pacientes por la plataforma ni por la automatización.
- **Lo que vendemos:** los **exámenes de laboratorio a domicilio** (tercerizados con ECOFAM o propios, según la negociación) y, en un futuro cercano, el **domicilio del medicamento**.
- **Lo que pedimos a la doctora:** que incluya pacientes suyas en la plataforma y un testimonio.

## Objetivo y plazos

| Meta | Cifra | Fecha límite |
|---|---|---|
| Doctoras aliadas | 2 | 13 de noviembre de 2026 (2 semanas) |
| Pacientes de prueba de confianza | 2 (una de cada doctora, pacientes reales de ellas) | 27 de noviembre de 2026 (2 semanas más) |
| Pacientes probando la plataforma | 10 | después de las 2 de prueba |
| Exámenes completados | 5 | después de cerrar con ECOFAM |
| Documentar | redes (principal) e inversionistas | continuo |

## El proceso de la pizarra

```
2 doctoras ── llamar 10 diarios (lista de Doctoralia)
     │
10 pacientes ── registrar 2 de prueba existentes (1 por doctora, pacientes de ellas)
     │
5 exámenes ── ECOFAM (negociar: tercerizar con ellos o ofrecerlos nosotros)
     │
Producto ── Farmacia (domicilio del medicamento, más adelante)
     │
Documentar ── redes, e inversionistas
```

## Qué especialistas buscar (decidido el 30 oct 2026: opciones 1 y 2)

Carlos no quiere trabajar con medicina estética. Orden recomendado:

1. **Endocrinología (prioridad 1).** Son las que más formulan GLP-1 con criterio, piden exámenes completos (HbA1c, perfil lipídico, función tiroidea, renal y hepática) y su aval le da credibilidad a Saludly ante otras médicas e inversionistas. Contra: agendas llenas y más difíciles de convencer.
2. **Medicina interna con enfoque en obesidad o metabolismo (prioridad 2).** Ven obesidad, prediabetes e hígado graso, piden muchos exámenes y suelen tener consulta privada más flexible.
3. **Ginecología con enfoque endocrino (SOP y menopausia).** Encaja con el foco en mujeres: el peso es un tema central en SOP y menopausia, y piden exámenes hormonales y metabólicos. Hay que confirmar en la llamada si manejan GLP-1.
4. **Medicina familiar o general con diplomado en obesidad.** Más accesibles y con más tiempo, pero menos credibilidad para el caso. Sirven de respaldo.

No recomendados: estética (decisión de Carlos), nutricionistas dietistas (no formulan GLP-1) y perfiles de "medicina funcional" sin especialidad (riesgo de credibilidad con el resto de médicos).

**Filtros en Doctoralia:** Bogotá; consulta privada; reseñas que mencionen peso, obesidad, metabolismo o tiroides; mujeres especialistas de preferencia (conectan con el foco); que tengan Instagram activo o, al revés, que no tengan y les interese empezar. La lista se arma a mano (nombre, especialidad, teléfono, redes, notas) y no con extracción masiva del sitio.

## Fases (ajustadas el 30 oct 2026)

### Fase 1 · Oferta, lista y guion (30 oct a 2 nov)

- Decidir las especialidades (ver arriba).
- Lista de 40 a 60 especialistas de Doctoralia para 4 a 6 días de llamadas.
- **Guion de llamada de diagnóstico:** como la automatización es personalizada, la llamada pregunta dónde le duele el consultorio. Menú de problemas típicos:
  - inasistencias y confirmación de citas;
  - pacientes que abandonan el tratamiento entre consultas;
  - preguntas repetidas por WhatsApp (efectos secundarios, dosis, cuándo repetir exámenes);
  - órdenes de laboratorio y lectura de resultados antes de la consulta;
  - historia y cuestionario previo a la primera cita;
  - poco tiempo o pocas ideas para el contenido en redes.
- **Oferta de una hoja** (PDF o página) para mandar por WhatsApp después de la llamada.
- **Salida:** lista lista, guion y oferta aprobados por Carlos.

### Fase 2 · Llamadas y cierre de 2 doctoras (3 a 13 nov)

- 10 llamadas diarias, registradas en una hoja simple (llamó, contestó, interesada, reunión, cerró).
- Reunión corta con demo en el celular.
- Acuerdo escrito con cada doctora: alcance del regalo, roles de datos (ella responde por los datos de sus pacientes y Saludly es encargada) y consentimiento de las pacientes.
- Preguntar si tienen presupuesto para pauta y si quieren asesoría para usarlo.
- **Salida:** 2 doctoras con acuerdo firmado.

### Fase 3 · Producto GLP-1 mínimo y automatización (en paralelo, 3 a 20 nov)

- **Vista de la paciente:** solo los exámenes que pidió la doctora, con **avances visuales** (peso, cintura, exámenes que mejoran), **metas** y quizás **retos**. Más corta que el informe completo. Primero mujer.
- **WhatsApp:** seguimiento y, de vez en cuando, un mensaje que ofrezca el domicilio de exámenes (con autorización previa de la paciente para mensajes comerciales).
- **Automatización de cada doctora:** se construye según lo que salga de su llamada de diagnóstico.
- Mismo motor y mismas reglas: los umbrales los evalúa el código, nada es un diagnóstico y la doctora revisa antes de que la paciente vea.
- **Salida:** la plataforma lista para recibir a la primera paciente de cada doctora.

### Fase 4 · Pacientes de prueba de confianza (14 a 27 nov)

- 1 paciente real de cada doctora, con consentimiento firmado, usando la plataforma.
- En paralelo, Carlos negocia con ECOFAM (tercerizar o ofrecer los exámenes nosotros).
- **Salida:** 2 pacientes activas y el primer testimonio.

### Fase 5 · 10 pacientes y 5 exámenes (desde el 28 nov)

- Ampliar a 10 pacientes y completar 5 exámenes a domicilio.
- Contenido orgánico de las doctoras con la asesoría de Saludly (ellas publican; Carlos asesora y a veces graba y edita).

### Documentar (continuo, desde la primera llamada)

- **Redes (principal):** el proceso detrás de cámaras (llamadas, reuniones, la construcción del producto, la primera paciente), sin datos de pacientes y sin nombrar medicamentos.
- **Inversionistas:** cifras del embudo (llamadas, reuniones, cierres), tiempo ahorrado a la doctora, uso de la plataforma por las pacientes y exámenes vendidos.

## Lo que ya tenemos y sirve

- Motor de 100+ biomarcadores, RAG en Supabase, control de salida y frases prohibidas.
- App del paciente (Fase 6) con registro, cuestionario y vista del médico en `/medico`.
- WhatsApp oficial (+57 301 130 7944) y la semana de prueba por WhatsApp.
- Costos referenciales de ECOFAM (no oficiales).

## Riesgos a revisar

- **Publicidad de medicamentos con fórmula:** en Colombia no se pueden anunciar al público. El contenido y los mensajes de WhatsApp no deberían nombrar semaglutida, tirzepatida ni marcas. Confirmarlo en la consulta legal pendiente (INVIMA).
- **Domicilio del medicamento:** exige un servicio farmacéutico o droguería habilitados y entregar solo con fórmula. Va como fase futura y con asesoría legal.
- **Ética médica:** el contenido de las doctoras no puede prometer resultados. Saludly no paga ni recibe comisiones de las doctoras por remitir pacientes a nuestros exámenes; la paciente decide dónde se los toma.
- **Datos:** contrato de transmisión de datos con cada doctora (Ley 1581) y consentimiento de cada paciente, también para los mensajes comerciales de WhatsApp.
- **El agente organiza y redacta:** no decide dosis ni ajusta tratamientos.

## Respuestas de Carlos (30 oct 2026)

1. **Especialidades:** sin decidir; nada de estética; pidió recomendaciones (ver arriba).
2. **Doctoras:** partimos de cero; se buscan en Doctoralia.
3. **Regalo:** automatización personalizada del consultorio según los problemas que tenga cada doctora en su proceso.
4. **Redes:** Carlos asesora cómo hacer el contenido y a veces graba y edita; ellas publican. Preguntar si tienen presupuesto para pauta y si quieren asesoría.
5. **A cambio:** pacientes en la plataforma y testimonio. No se cobra a la doctora ni a sus pacientes; se venden exámenes a domicilio y, pronto, el domicilio del medicamento.
6. **"Registrar 2 de prueba existentes":** al menos 2 pacientes, una de cada doctora, que sean pacientes de ellas, como prueba de confianza.
7. **ECOFAM:** negociar para tercerizar con ellos u ofrecer nosotros mismos los exámenes.
8. **Farmacia:** domicilio del medicamento en un futuro cercano.
9. **Exámenes que piden:** sin respuesta; se pregunta en las llamadas.
10. **Más dinámica:** avances visuales, quizás retos, metas y a veces un mensaje de WhatsApp que promocione el domicilio.
11. **Documentar:** redes principalmente, e inversionistas.
12. **Plazo:** 2 semanas para las 2 doctoras y 2 semanas más para las 2 pacientes.

## Decisiones del 30 oct 2026 (segunda ronda)

- **Especialidades:** endocrinología e internistas con enfoque en obesidad o metabolismo (opciones 1 y 2). Ginecología y medicina familiar quedan por fuera por ahora.
- **Llamadas:** las hace Carlos desde el **300 520 7995**.
- **ECOFAM:** sin fecha; propuesta tentativa: **14 de noviembre de 2026**, al día siguiente de cerrar las 2 doctoras.
- A las doctoras se les trata de **usted** en el guion y la oferta.

## Preguntas que siguen abiertas

- ¿Qué precio objetivo llevas a ECOFAM y qué modelo prefieres (tercerizar o ofrecerlos con marca Saludly)?
- ¿La oferta va con tu apellido y una foto tuya?
