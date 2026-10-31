# Demo GLP-1 · App de la paciente y dashboard de la doctora

Propuesta del 30 de octubre de 2026 para el demo que se le muestra a la doctora en la reunión (y que después usan sus pacientes). Es un borrador: las preguntas abiertas están al final y lo marcado como **supuesto provisional** lo confirma Carlos o la doctora.

Datos del demo: **sintéticos** (regla 5). Pacientes reales solo con consentimiento firmado.

## Principio que ordena todo

- **La paciente ve motivación:** su nivel, sus logros y su silueta cambiando. Cifras simples, nada técnico.
- **La doctora ve decisiones:** qué paciente necesita atención hoy y qué trae cada una al control. Cifras reales, sin gamificación.
- **Los umbrales los evalúa el código, nunca el LLM, y nada es un diagnóstico.** El nivel y la silueta son motivacionales, no un puntaje clínico.

## 1. App de la paciente (estilo iOS)

Se parece a una app nativa de iPhone en cómo funciona y cómo se ve, sin dejar de ser la PWA actual:

- Barra de pestañas abajo: **Hoy · Progreso · Logros · Exámenes · Recomendaciones**.
- Títulos grandes que se encogen al bajar, tarjetas tipo app Salud, hojas que suben desde abajo (registrar peso, reportar cómo se siente) y animaciones con resorte.
- Fuente del sistema (en iPhone sale San Francisco), modo oscuro y área segura de la muesca.

### Pantallas

| Pestaña | Qué tiene |
|---|---|
| **Hoy** | Nivel (anillo de 0 a 100), el siguiente logro ("te faltan 600 g para tu logro de 5 kg"), la meta de la semana y un botón para registrar peso y cintura |
| **Progreso** | La silueta con la capa de grasa (ver abajo), la curva de peso desde el inicio del tratamiento y "antes / hoy" |
| **Logros** | Medallas ganadas y por ganar, en orden; cada una con fecha |
| **Exámenes** | Solo los que pidió la doctora, en lenguaje simple, después de que ella los revise |
| **Recomendaciones** | Recomendaciones de la doctora y de Saludly; aquí está el botón **"Recibir la receta del día por WhatsApp"** |

**Receta del día:** el botón abre WhatsApp con un mensaje ya escrito al +57 301 130 7944 ("Quiero la receta del día"). Así la paciente pide la receta solo si quiere, y como ella escribe primero, se abre la ventana de 24 horas de WhatsApp para responderle sin plantilla pagada. En esa misma conversación, de vez en cuando, va la oferta del domicilio de exámenes (con su autorización para mensajes comerciales).

### El nivel de 0 a 100 (supuesto provisional)

El nivel **nunca baja**: es motivación. Si la paciente sube de peso, el nivel se queda quieto y la doctora ve el dato real.

**Nivel inicial (entre 30 y 72),** calculado con lo que ya logró desde que empezó el tratamiento, aunque no estuviera con nosotros:

```
fracción lograda = (peso al inicio del tratamiento − peso hoy) ÷ (peso al inicio − peso objetivo)
nivel inicial    = 30 + 42 × fracción lograda        (fracción limitada entre 0 y 1)
```

Ejemplo: empezó en 92 kg, su meta es 74 kg y hoy pesa 85 kg. Logró 7 de 18 kg (0,39), así que arranca en **46**.

- Quien recién empieza arranca en 30 (no en 0: ya dio el primer paso).
- Quien ya llegó a la meta arranca en 72; los últimos 28 puntos se ganan con hábitos, controles y mantenimiento.

**Después sube con logros** (puntos por proponer):

| Logro | Ejemplo |
|---|---|
| Hitos de peso | primer kilo, 5 %, 10 %, la mitad de la meta, la meta |
| Cintura | cada 2 cm menos |
| Constancia | registrar el peso 4 semanas seguidas |
| Metas semanales | cumplir la meta de la semana (caminar, proteína, agua) |
| Controles | asistir al control con la doctora |
| Exámenes | tomarse los exámenes que pidió la doctora; un examen que mejora frente al anterior |
| Mantenimiento | sostener el peso 4 semanas después de llegar a la meta |

**Cuidado:** perder peso demasiado rápido no da puntos extra. A partir de cierta velocidad semanal se le avisa a la doctora en vez de premiar a la paciente. El límite lo define la doctora (supuesto provisional para el demo: más de 1,5 % del peso por semana durante 2 semanas).

### La silueta con capa de grasa

Se mantiene la figura 3D de la portada y alrededor se dibuja una **capa translúcida** que representa la grasa estimada. Cada vez que la paciente registra peso o cintura, la capa se anima y se encoge hacia la silueta de la meta.

Cálculo propuesto: **masa grasa relativa (RFM)**, que solo usa talla y cintura (datos que ya tomamos):

```
mujer:  RFM = 76 − 20 × (talla ÷ cintura)
hombre: RFM = 64 − 20 × (talla ÷ cintura)
```

Ejemplo: mujer de 162 cm con 96 cm de cintura → 42 %. Con la cintura meta de 84 cm → 37 %. El grosor de la capa va de su valor al inicio del tratamiento (capa más gruesa) a su valor meta (capa pegada a la silueta). Si solo hay peso y no cintura, se estima con el IMC.

A la paciente no se le muestra el porcentaje, solo la silueta y "llevas el 39 % del camino". El número exacto va en la vista de la doctora.

Cómo se construye depende de qué tenemos de la figura (pregunta 2):

- **Solo la imagen PNG:** la capa se dibuja como un halo con forma de cuerpo detrás de la figura, más ancho en cintura, cadera y brazos, y se anima su grosor. Es rápido y se ve bien en el celular.
- **El modelo 3D original:** la capa es una segunda malla 3D, un poco más grande y translúcida, que se encoge con *morph targets*. Se ve mejor y gira con el dedo, pero toma más trabajo y pesa más en el celular.

## 2. Dashboard de la doctora

### Criterio para decidir qué se muestra

Un dato entra en el dashboard solo si cumple al menos una de estas tres condiciones:

1. **Le cambia una decisión:** necesita llamar, adelantar un control o revisar un examen.
2. **Le ahorra tiempo:** algo que hoy busca a mano, pregunta en consulta o responde por WhatsApp.
3. **Le muestra si el tratamiento funciona** en sus pacientes, en conjunto.

Si no cumple ninguna, no entra, o queda escondido un toque más adentro.

### Lo que sí ve

**Pantalla de inicio · "Hoy":** la lista de pacientes ordenada por quién necesita atención, no alfabética.

| Señal | Por qué |
|---|---|
| Síntoma de alarma reportado | La paciente marcó un síntoma que la doctora definió como alarma (por ejemplo, vómito que no para o dolor abdominal fuerte). Escala según las reglas de seguridad del motor |
| Pérdida demasiado rápida o estancada | Más rápida que el límite de la doctora, o sin cambio en 4 semanas |
| Dejó de registrar | 14 días sin datos: posible abandono |
| Examen nuevo con algo fuera de rango | Viene del motor, en lenguaje médico |
| Pregunta pendiente | La paciente dejó una pregunta para el control |
| Control esta semana | Con el resumen listo para abrir |

**Ficha de cada paciente:**

- El **resumen antes del control** (el mismo de la carta): peso, cintura, exámenes que ella pidió con el inicio y hoy, metas cumplidas, efectos reportados y preguntas.
- Curvas de peso y cintura desde el inicio del tratamiento, con la meta.
- Línea de tiempo de efectos reportados (náuseas, estreñimiento, cansancio…).
- Estado de los exámenes: pedido, muestra tomada, resultado listo, revisado.
- Medicamento y dosis **como ella los registró** (dato suyo; la plataforma no sugiere dosis).
- Botón para aprobar lo que ve la paciente (exámenes y recomendaciones).

**Resumen del consultorio:** pacientes activas, cuántas registraron esta semana, pérdida promedio desde el inicio, abandonos del mes y próximos controles.

### Lo que no ve (o queda escondido)

- El nivel, los puntos y las medallas: solo la constancia (cuántas semanas registró).
- Las recetas y los mensajes de WhatsApp de la receta del día.
- Biomarcadores que ella no pidió.
- Los textos en lenguaje de paciente: ella ve el lenguaje médico del motor.
- Registros diarios sueltos: ve tendencias y semanas.
- Cualquier sugerencia de diagnóstico, dosis o cambio de tratamiento.

### Herramientas que se le pueden ofrecer en el onboarding

Menú para la reunión; se activan solo las que pida:

| Herramienta | Qué automatiza |
|---|---|
| Confirmación de citas | WhatsApp 48 h y 2 h antes, con botón de confirmar o reprogramar |
| Recordatorio de control y de exámenes | Avisa a la paciente cuándo le toca |
| Cuestionario de primera consulta | Llega lleno a la historia antes de la cita |
| Respuestas frecuentes aprobadas | Respuestas que ella escribe y aprueba una vez (por ejemplo, qué hacer con las náuseas leves) |
| Indicaciones después de la consulta | Ella dicta o escribe y le llegan a la paciente |
| Órdenes de exámenes a domicilio | Pide los exámenes y Saludly agenda la toma en casa (es nuestro negocio) |
| Exportar el resumen | PDF para su historia clínica o su software |
| Contenido para redes | Ideas y guiones a partir de preguntas frecuentes anónimas |

## 3. Cómo arrancar el demo

1. **Prototipo clicable en artifact (1 a 2 días):** las pantallas de la paciente en un marco de iPhone y el dashboard de la doctora, con 3 pacientes ficticias. Sirve para iterar el diseño rápido y para mostrarlo en la reunión.
2. **Construirlo dentro de `app/`** cuando el diseño esté aprobado: rutas nuevas para la paciente GLP-1 y para la doctora, reutilizando el registro, `/medico`, Supabase y el WhatsApp que ya existen.
3. **Probarlo con la primera paciente real** de cada doctora (14 a 27 de noviembre).

## Preguntas abiertas

Las respuestas se anotan aquí con fecha.

1. ¿Dónde está el nivel de 0 a 100 que ya muestra saludly.online? No está en este repositorio (`app/`). ¿Es del dashboard de Lovable? Pásame el enlace o una captura.
2. ¿Tienes el modelo 3D original de la figura de la portada (.glb, .fbx, .blend) o solo la imagen? En `app/` solo hay `body.png` y `body-female.png`.
3. ¿Quién define el peso objetivo: la doctora o la paciente? Recomiendo la doctora.
4. ¿Quién registra el peso al inicio del tratamiento y la fecha de inicio: la paciente de memoria, la doctora desde su historia o ambas? Recomiendo la doctora; si no, la paciente con la marca "dato de la paciente".
5. ¿Te sirve la fórmula del nivel (30 + 42 × lo logrado) y que el nivel nunca baje?
6. ¿Qué logros quieres en el demo de la lista, y quieres algo más?
7. ¿Cómo registra la paciente su peso: en casa cada semana, en el control o con la enfermera? ¿Pedimos también la cintura cada 2 semanas?
8. ¿Registramos el medicamento y la dosis que indica la doctora y un recordatorio del día de aplicación? Es útil, pero hay que confirmarlo con la consulta legal.
9. ¿Qué síntomas puede reportar la paciente? Propongo una lista base que la doctora aprueba en el onboarding, y ella marca cuáles son de alarma.
10. ¿El demo incluye también la versión para hombre (misma app con la silueta masculina)?
11. ¿Para qué fecha necesitas el demo? Las llamadas empiezan el 3 de noviembre, así que las primeras reuniones podrían ser hacia el 5 o 6.

## Respuestas de Carlos (30 oct 2026)

1. El nivel de 0 a 100 de saludly.online: Carlos lo muestra con una captura.
2. No hay modelo 3D. Para el demo se usa la figura actual (`body-female.png`) con la capa de grasa dibujada alrededor de su contorno. El 3D con cambio de cuerpo queda para después (ver abajo).
3. La doctora define el peso inicial y el objetivo.
4. La doctora registra el peso y la fecha de inicio mientras agenda el seguimiento.
5. Fórmula del nivel aprobada, y el nivel nunca baja.
6. Logros: lista nueva, revisada a partir de la propuesta.
7. Cintura: sí. Las pacientes anotan su peso y su cintura (se pesan ellas mismas).
8. Medicamento y dosis que indicó la doctora: sí, como recordatorio. Falta la consulta legal (ver abajo).
9. Lista base de síntomas: sí; la doctora la aprueba y marca los de alarma.
10. Demo primero para mujeres.
11. Demo listo para mostrarlo en consultorios desde el 5 de noviembre de 2026.

## Modelo 3D (para después del demo)

- **Recomendado:** Blender con el complemento gratuito MPFB (MakeHuman), que genera un cuerpo con controles de peso y exporta `.glb` con *shape keys*: una forma "inicio" y una forma "meta", y la app mezcla entre las dos según el avance. Carlos lo puede armar con Claude paso a paso; los modelos de MakeHuman se pueden usar comercialmente (revisar la licencia al descargar).
- **Alternativa rápida:** generadores de imagen a 3D (Meshy, Tripo) a partir de la figura actual. Dan una malla bonita, pero sin controles de peso: habría que hacer la forma "meta" a mano.

## Recordatorio del medicamento: puntos para la consulta legal

No es asesoría legal; son las preguntas que hay que llevarle al abogado:

- **Datos sensibles (Ley 1581 de 2012):** el medicamento y la dosis son datos de salud. Hace falta la autorización expresa de la paciente y decir para qué se usan.
- **¿Es dispositivo médico?** Un recordatorio de lo que indicó la doctora, sin calcular ni sugerir dosis, en principio no toma decisiones clínicas. Confirmar si el INVIMA lo consideraría software dispositivo médico (Decreto 4725 de 2005).
- **Publicidad:** en la app se muestra el tratamiento de la paciente, no se promociona. El nombre del medicamento no puede aparecer en mensajes comerciales ni en redes.
- **Domicilio del medicamento:** es otro tema (servicio farmacéutico habilitado y fórmula médica). No se mezcla con el recordatorio.

En el demo el recordatorio dice "Tu aplicación semanal · 0,5 mg · jueves, como indicó tu doctora", sin nombre ni marca del medicamento.
