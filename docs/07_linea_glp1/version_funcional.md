# Versión funcional GLP-1 · criterios de "Para ti" y plan para la primera paciente

31 de octubre de 2026. Pasa del demo (artifact con datos ficticios) a la app real en `app/` con Supabase, para probarla con la primera paciente.

**Fase:** es la **Fase 6** (PWA y dashboard, gratis en Vercel y Supabase, para los 5 primeros pacientes), en su línea GLP-1; la llamamos **Fase 6B · GLP-1**. La actualización semanal de recomendaciones usa el contenido de la **Fase 5** y por ahora reglas con plantillas, sin LLM. El agente con DeepSeek y el RAG en el VPS siguen siendo la **Fase 2** (cuando se compre el VPS); el dashboard completo y las herramientas internas, la **Fase 7**.

Todo lo que dice "supuesto provisional" lo aprueba el médico revisor (hoy Carlos, decisión del 11 de octubre) o la doctora de cada paciente.

## 1. Criterios clínicos de "Para ti"

### Reglas que no se rompen aplicadas aquí

- **El código decide qué recomendación sale; nunca el LLM.** Cada recomendación tiene un disparador que se calcula con datos (registro de la semana, síntomas, hallazgos del motor, objetivos).
- **Solo contenido aprobado.** Sale de `knowledge_base/fase5` (189 recomendaciones, 119 textos por hallazgo, 125 consejos por objetivo, filtros) o lo escribe la doctora. El RAG sirve para encontrar el fragmento y su guía de respaldo, no para inventar texto.
- **Nada es diagnóstico ni tratamiento.** No se habla de dosis, cambios de medicamento ni suplementos con cantidades. Lo exacto lo define la doctora.
- **Todo pasa por el control de salida** (frases prohibidas) antes de mostrarse o enviarse por WhatsApp.
- Cuando llegue DeepSeek (Fase 2), solo reescribe más natural lo que el código ya eligió, con datos seudonimizados.

### Orden en la pantalla

1. **Mensaje de la doctora** (si lo escribió esta semana). Siempre arriba y con su nombre.
2. **Lo de tus exámenes:** recomendaciones atadas a hallazgos del motor, solo de exámenes que la doctora ya aprobó.
3. **Lo de tu semana:** recomendaciones según lo que la paciente registró.
4. **Para tus objetivos:** un consejo de sus 3 objetivos.
5. **Receta del día:** solo si la pide por WhatsApp.

Máximo **3 recomendaciones nuevas por semana** más el mensaje de la doctora, para que se lean. Cada una dice **por qué le aparece** ("porque esta semana marcaste náuseas").

### Disparadores semanales (supuesto provisional)

| Disparador (lo calcula el código) | Qué sale en Para ti | Qué ve la doctora |
|---|---|---|
| Síntoma de **alarma** (dolor abdominal fuerte, vómito que no para, no retiene líquidos) | Ninguna recomendación: solo el mensaje de seguridad (llamar a la doctora o ir a urgencias) | Alerta roja arriba de su lista |
| Náuseas, acidez o poco apetito | Comidas pequeñas y despacio, parar al sentirse llena, evitar fritos; hidratación | Aparece en efectos reportados |
| Estreñimiento | Agua, fibra (verduras, frutas, avena), caminar | Efectos reportados |
| Bajó más rápido que el límite de la doctora (demo: 1,5 % por semana, 2 semanas) | No se felicita la velocidad: proteína en cada comida y no saltarse comidas | Alerta naranja |
| Sin cambio de peso por 4 semanas o más (la doctora puede cambiar el número) | Es normal que haya mesetas; meta de actividad y fuerza | Para revisar |
| En tratamiento y bajando de peso (todas) | Proteína en cada comida y fuerza 2 veces por semana, para cuidar el músculo | Constancia |
| No registró en 10 días o más | Recordatorio amable para registrar | Alerta naranja a los 14 días |
| Hallazgo del motor en un examen aprobado | El texto aprobado de ese hallazgo, con su nivel de lenguaje (resultado observado, patrón compatible, riesgo potencial o requiere evaluación médica) | Lenguaje médico del motor |
| Objetivos de la paciente | Un consejo de `consejos_objetivos.yaml` | No se muestra |
| Embarazo o lactancia (respuesta del cuestionario) | Solo "habla con tu doctora" | Alerta: la decisión es de ella |

Siempre se aplican los filtros aprobados: alergias, dieta y medicamentos (`filtros.yaml`). Una recomendación no se repite en 3 semanas salvo que su disparador siga activo.

### Cómo se actualiza cada semana

- **Domingo en la noche:** el código calcula los disparadores de cada paciente y arma su lista de la semana (máximo 3 más el mensaje de la doctora).
- **Lunes temprano:** la doctora (en la prueba, Carlos) ve la lista en su panel y puede quitar, cambiar o escribir su mensaje.
- **Lunes 7:00 a. m.:** se publica en Para ti y, si la paciente aceptó WhatsApp, le llega un aviso corto.
- Los avisos de alarma no esperan al lunes: salen en el momento.

## 2. Qué hay que construir

Ya existe en `app/` y Supabase: entrar con Google o correo, registro con autorización (AUT-2026-10-v1), cuestionario, visita, informes con estado `en_revision → aprobado`, vista del médico en `/medico`, WhatsApp y `codigo/pipeline/publicar.py` (PDF → lector → motor → informe en revisión).

Lo nuevo:

| Pieza | Qué hace |
|---|---|
| **Registro GLP-1** (`/peso/empezar`) | La paciente pone fecha de inicio del tratamiento, peso al inicio, peso hoy, peso meta, cintura, talla, medicamento y dosis que le indicó su doctora, y el día de aplicación. Todo queda como "dato de la paciente" hasta que la doctora lo confirme |
| **Autorización nueva** (AUT-2026-11-v1) | Agrega el medicamento como dato sensible y los mensajes comerciales de WhatsApp (exámenes a domicilio) como casilla aparte |
| **App de la paciente** (`/peso`) | Las pantallas del demo con datos reales: Hoy, Progreso, Logros, Exámenes y Para ti |
| **Registro semanal** | Peso, cintura, síntomas, aplicación y metas, guardados en Supabase |
| **Subir el resultado** | La paciente sube el PDF del laboratorio desde Exámenes, a un depósito privado |
| **Procesar el PDF** | Lector y motor generan el informe en revisión, y el PDF se borra después de leerlo (como ya está decidido) |
| **Panel de la doctora** (`/doctora`) | El tablero del demo con datos reales, aprobar el informe y escribir el mensaje de la semana |
| **Recomendaciones semanales** | El código de disparadores, la lista para revisar y la publicación del lunes |
| **Tablas nuevas** | Tratamiento, registros semanales, exámenes subidos, recomendaciones de la semana y mensajes de la doctora, con RLS: cada paciente ve lo suyo y la doctora solo a sus pacientes |

### Orden propuesto

1. Tablas y autorización nueva.
2. Registro GLP-1 y app de la paciente con registro semanal.
3. Panel de la doctora con los datos reales.
4. Subir el PDF y procesarlo.
5. Recomendaciones semanales.
6. Prueba de punta a punta con datos sintéticos y después con la paciente.

## 3. Riesgos para la prueba

- **El lector está hecho para el PDF de ejemplo.** Si el laboratorio de la paciente usa otro formato, no va a leerlo bien. Hace falta un PDF real de ese laboratorio (con los datos tapados) para ajustarlo, o cargar los valores a mano en el panel con doble revisión.
- **Datos reales solo con autorización firmada** (los 5 primeros del piloto) y hacia un LLM externo, nada (esta versión no usa LLM).
- El nombre del medicamento no se usa en mensajes comerciales. Falta la consulta legal del recordatorio.

## Decisiones de Carlos (31 oct 2026)

- **Procesar el PDF:** desde el PC de Carlos, con un programa que revisa cada 5 minutos (la versión en la nube queda para después).
- **Recomendaciones semanales:** las aprueba la doctora (o Carlos) el lunes antes de publicarse.
- **Doctora de la paciente de prueba:** sí tiene y entra al panel con su correo (falta el correo).
- **Laboratorio:** ECOFAM. Falta un PDF real de ECOFAM con los datos personales tapados para ajustar el lector.
- **Registro:** la paciente pone sus datos, su estado actual y su meta; quedan como "dato de la paciente" hasta que la doctora los confirma (ajusta la decisión del 30 oct de que la doctora los define).

## Construido (31 oct 2026)

- **Supabase** (migración `20261031000000_glp1_peso.sql`, ya aplicada): `doctoras`, `tratamientos_peso`, `registros_peso`, `semanas_peso`, la casilla `acepta_comerciales` en `autorizaciones` y permisos: la paciente ve lo suyo, la doctora solo a sus pacientes (las que usaron su código) y el equipo todo.
- **App** (`app/src`): `/peso/empezar` (registro del tratamiento en 5 pasos con la autorización AUT-GLP1-2026-11-v1), `/peso` (Hoy, Progreso, Logros, Exámenes y Para ti con datos reales) y `/doctora` (panel con alertas, gráficas, aprobación del análisis, confirmación del tratamiento y publicación de la semana). El enlace de la doctora es `https://app.saludly.online/?dra=CODIGO`.
- **Análisis del PDF**: la paciente lo sube desde Exámenes y lo analiza la función de Vercel que ya existía (`api/procesar.py`), en la nube, sin depender del PC; el PDF no se guarda. El documento del PDF tiene que ser el de la paciente. Queda "en revisión" hasta que la doctora lo aprueba.
- **Semana**: `python codigo/informe/recomendar_peso.py` (domingo) deja el borrador de cada paciente; la doctora lo revisa y lo publica. Textos nuevos en `knowledge_base/fase5/peso_glp1.yaml`, **pendientes de aprobación**.

## Para la prueba con la primera paciente

1. Publicar la app en Vercel (falta: subir a GitHub o `bash app/desplegar.sh`).
2. Crear a la doctora en Supabase: `insert into doctoras (correo, nombre, codigo) values ('correo@…', 'Dra. …', 'CODIGO');`
3. Mandarle a la paciente el enlace `https://app.saludly.online/?dra=CODIGO`: entra con Google o correo, hace el registro y su tratamiento.
4. La paciente sube su PDF de ECOFAM en Exámenes. Si el lector no lo lee bien (formato real distinto al de ejemplo), hay que ajustar el lector con un PDF de ECOFAM.
5. La doctora entra a `https://app.saludly.online/doctora` con su correo, confirma los datos y aprueba el análisis.
6. El domingo: `python codigo/informe/recomendar_peso.py`; el lunes la doctora publica la semana.

## Prueba con datos de ejemplo (31 oct 2026)

- **Doctora de prueba:** `thecangri.info@gmail.com`, "Dra. Prueba", código **PRUEBA** (ya creada en Supabase). Enlace para la paciente: `https://app.saludly.online/?dra=PRUEBA`.
- **PDF de ejemplo:** `pdf_ejemplo/Ejemplo_resultados_LCD-2026-100124_mujer.pdf` (sintético, 34 años, documento CC 0000000002). El motor lo analizó: 7 hallazgos (hierro bajo, ANA positivo, lipoproteína(a), IMC, TSH, colesterol, vitamina D) y 20 resultados fuera de rango; control de salida sin problemas.
- **Semana armada por el código** con esos datos y estreñimiento reportado: GLP-EST (esta semana), REC-ALI-201 (por sus exámenes) y un consejo de energía y sueño (objetivos).
- **Artifact del flujo:** `flujo_glp1.html` (artifact privado https://claude.ai/artifact/2Y29kBVuahVjmvhywqT1rE). Muestra el recorrido completo con esos datos: subir el PDF → aprobar → publicar la semana → la paciente lo ve.
- En la app real, un PDF sintético solo lo puede procesar el equipo (su documento no es el de la paciente); la paciente sube el suyo.
