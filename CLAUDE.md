# CLAUDE.md · Guía para Claude Code

Contexto para que Claude Code trabaje en este proyecto. La descripción general está en [README.md](README.md) y el mapa de la documentación en [docs/README.md](docs/README.md).

## Qué es

Saludly Brain es un agente de IA médico preventivo de Saludly (Bogotá, Colombia). Lee el PDF de un laboratorio, evalúa más de 100 biomarcadores con reglas clínicas y genera un informe preventivo para el paciente y una vista para el médico. El usuario de este repositorio es Carlos, CEO de Saludly.

- **Idioma:** todo el proyecto está en español (documentos, código, nombres de variables y mensajes). Responde en español y escribe código y comentarios en español, igual que el código existente.
- **Contexto clínico:** Colombia. Mandan las guías colombianas, la hemoglobina se ajusta por la altitud de Bogotá y la regulación es la Ley 1581 y el INVIMA.

## Reglas que no se rompen

1. **Los umbrales los evalúa el código, nunca el LLM.** El motor decide qué se cumple; el LLM (DeepSeek) solo redacta a partir de la salida del motor.
2. **No se inventan datos.** No medido, no detectable, menor que el límite e inválido son estados distintos; ninguno es cero. Un nombre que no está en los sinónimos queda como duda: solo valen coincidencias exactas.
3. **Nada es un diagnóstico.** Hay cuatro niveles de lenguaje: resultado observado, patrón compatible, riesgo potencial y condición que requiere evaluación médica. Las frases prohibidas están en el documento 05 y en el documento de relaciones.
4. **Las decisiones clínicas son del médico revisor.** No cambies umbrales, coincidencias ni escalamientos por tu cuenta. Si una prueba contradice una ficha, avisa a Carlos y no "arregles" la ficha. Los supuestos provisionales se marcan como tales.
5. **Datos de pacientes:** datos reales solo con consentimiento firmado durante el piloto (los 5 primeros, decidido el 20 de octubre de 2026); en lo demás, datos sintéticos. Hacia un LLM externo, seudonimizar: edad, sexo, valores y contexto; nunca nombre ni documento.
6. **No toques `_archivo/`.** Es histórico (el 9 de octubre de 2026 ya no estaba dentro de esta carpeta).

## Estructura

```
README.md · CLAUDE.md
docs/                    documentación (no la lee el código); ver docs/README.md
knowledge_base/          fuente de verdad clínica, legible por máquina
  00_INDEX.md / .json    índice generado (sinónimos, unidades, qué alimenta cada biomarcador)
  biomarcadores/*.md     144 fichas (10 vitaminas "fuera del panel base" y la B6 "opcional"), encabezado YAML (biomarker_id, sinonimos, unidad_canonica, alimenta…)
  condiciones/M1..M6/    86 fichas COND-Mx-XX-NNN (incluidas) y COND-…-ANN (apoyo), con bloque ```yaml
  relaciones/REL-*.md    31 relaciones entre módulos (tipo: patron | vigilar | fuera_de_patrones)
  seguridad/SEG-*.md     15 reglas de seguridad
  casos/                 casos de prueba: unitarios (json/yaml/csv) y de punta a punta (e2e/E2E-01 hombre, E2E-02 mujer)
  fase5/                 contenido para el paciente (Fase 5), de "usted" desde el 20 oct 2026: ESQUEMAS.md (formatos y reglas de lenguaje), objetivos.yaml (los 10),
                         filtros.yaml (alergias, dieta y medicamentos: preguntas de la PWA y reglas, aprobadas el 20 oct 2026),
                         frases_prohibidas.yaml (generado), redaccion/<ID>.yaml (119 textos por hallazgo y modulos.yaml),
                         recomendaciones/<tipo>_a|b.yaml (189), recetas/alimentos.yaml (140) y desayunos|meriendas|almuerzos|cenas.yaml (190)
codigo/
  requirements.txt       pdfplumber, pyyaml (reportlab solo para el generador de PDF)
  motor/                 motor de análisis completo (Fase 4)
    motor/motor.py       analizar(lectura, contexto) = flujo completo
    motor/lector.py      copia del lector del PDF
    motor/calculos.py    25 cálculos con trazabilidad (incluye TyG, TG/HDL, Mentzer y NLR)
    motor/clasificacion.py + reglas_parte1.yaml   clasificación, limítrofes, críticos, altitud
    motor/condiciones_m1m2.py   37 evaluadores · condiciones_m3m6.py: 49 evaluadores
    motor/relaciones_seguridad.py   relaciones, seguridad y ensamblar()
    motor/score2.py      SCORE2 recalibrado para Colombia (PURE)
    motor/kb/            COPIA de knowledge_base/{condiciones,relaciones,seguridad}
    pruebas/             probar_parte1..5.py, probar_mvp.py, probar_todo.py, PDF, E2E y 00_INDEX.json (copias)
  lector_pdf/            lector como módulo independiente (Fase 3), con sus propias pruebas
  herramientas/          generar_indice.py (00_INDEX.json y sus copias) · generar_solicitud_laboratorio.py (PDF para el laboratorio)
                         · generar_frases_prohibidas.py · validar_fase5.py (valida todo knowledge_base/fase5)
  informe/               Fase 5: redactar.py (informe en 6 partes, vista médica, WhatsApp), recomendar.py (orden 07.4),
                         nutricion.py (nutrientes de recetas, metas y receta del día), control_salida.py, contenido.py
  pipeline/              saludly.py: PDF → lector → motor → informe JSON + Markdown (ver codigo/pipeline/README.md)
  rag/                   fragmentar, vectorizar (Ollama bge-m3), probar_busqueda y subir a Supabase
  whatsapp/enviar.py     envío por la API oficial de WhatsApp (lee WHATSAPP_TOKEN y WHATSAPP_PHONE_NUMBER_ID del .env; pasa por el control de salida)
app/                     Fase 6: app del paciente (Vite + React + TanStack Router + Tailwind), traída del dashboard de Lovable con la misma experiencia.
                         Pantallas: / (recorrido), /panel, /plan. Hoy lee los informes de codigo/pipeline/ejemplos (demo con selector de caso).
                         `npm --prefix app run dev` (puerto 5173) · `npm --prefix app run build`
pdf_ejemplo/             4 PDF sintéticos (LCD-2026-100123 hombre, 100124 mujer, 100125 hombre con valor crítico y 100126 mujer con hallazgos digestivos) y generar_pdf_ejemplo.py [1 2 3 4]
_archivo/                zips originales, versiones viejas, duplicados
```

## Flujo del código

`lector.leer(pdf, visita, indice)` verifica la identidad (documento y orden), extrae y normaliza, y devuelve el contrato 10.3. Después `motor.analizar(lectura, contexto)` hace esto, en orden:

1. Parte 1: clasificación y cálculos.
2. Parte 2: condiciones M1 y M2.
3. Parte 3: condiciones M3 a M6, que reciben los hallazgos de M1 y M2.
4. Parte 4: relaciones y seguridad, y `ensamblar()` arma la salida final: escalamiento máximo, canal, hallazgos del informe ordenados, vista médica y edad biológica.

Los contratos de datos están en `docs/01_serie_saludly_brain/10_SALUDLY_BRAIN_Especificacion_para_desarrollo.md` (secciones 10.3 a 10.5).

**Importante:** la lógica de cada condición está escrita a mano en `condiciones_*.py`. De las fichas solo se leen el nombre, el nivel de lenguaje y las guías. Si cambia una regla en una ficha, hay que cambiar también el evaluador y su prueba.

## Comandos

```bash
pip install -r codigo/requirements.txt
cd codigo/motor && python pruebas/probar_todo.py       # esperado: TOTAL: 662 de 662
cd codigo/lector_pdf && python pruebas/probar.py        # la prueba del PDF mezclado necesita qpdf instalado
python codigo/herramientas/validar_fase5.py            # esperado: 0 errores
python codigo/pipeline/pruebas/probar_pipeline.py      # esperado: 120 de 120
python codigo/pipeline/saludly.py --pdf … --documento … --orden … --perfil perfil.json --enfermera enfermera.json --salida salida/
```

- Antes y después de cambiar código del motor, corre `probar_todo.py`. No se acepta ninguna regresión.
- Las pruebas reescriben `pruebas/salida_*.json`. En Windows cambian los saltos de línea aunque el contenido sea igual.

## Deuda técnica conocida

- **Copias de la Knowledge Base.** `codigo/motor/motor/kb/`, `codigo/motor/pruebas/00_INDEX.json`, `codigo/motor/pruebas/E2E-*.json` y `codigo/lector_pdf/pruebas/E2E-*.json` son copias de `knowledge_base/`. Hoy están sincronizadas. Si cambias una ficha, cópiala a `codigo/motor/motor/kb/` y corre `python codigo/herramientas/generar_indice.py`, que regenera el índice y sus dos copias. Conviene que el motor lea directo de `knowledge_base/`.
- **El RAG en Supabase** se actualizó el 20 de octubre de 2026 (1.401 fragmentos: fichas, textos para el paciente en usted, recomendaciones y filtros). El plan gratis pausa el proyecto tras 7 días sin uso: hay que reactivarlo antes de subir. Cada vez que cambie la Knowledge Base: `fragmentar.py`, `vectorizar.py` (incremental), `probar_busqueda.py` y `subir.py` (ver `codigo/rag/README.md`).
- **Contenido de la Fase 5 aprobado** por Carlos el 11 de octubre de 2026 (`estado_revision: aprobada`). Las decisiones y las correcciones de ese día están en `docs/02_plan_y_decisiones/Fase5_decisiones_para_revisar.md`.
- **El lector está duplicado** en `codigo/motor/motor/lector.py` y `codigo/lector_pdf/lector.py`, que hoy son idénticos.
- **Git.** El repositorio usa git desde el 9 de octubre de 2026 (rama `main`, sin remoto). `.gitattributes` normaliza los saltos de línea, así que las salidas de las pruebas solo aparecen como cambiadas si cambia su contenido.
- **El lector está hecho para el PDF de ejemplo.** Cuando llegue el formato real del laboratorio, hay que ajustar sus constantes de formato y repetir las pruebas.

## Estado y siguientes pasos

Las Fases 0, 1, 3 y 4 están hechas en versión 1, y la Fase 5 en versión con plantillas (10 de octubre de 2026). Desde el 20 de octubre de 2026 la siguiente es la **Fase 6** (PWA y dashboard del paciente, gratis en Vercel y Supabase, para los 5 primeros pacientes); la **Fase 2** queda para cuando se compre el VPS: OpenClaw en un VPS de **DonWeb** (ya no Hostinger) con DeepSeek (`deepseek-v4-pro`; `deepseek-chat` y `deepseek-reasoner` se retiraron el 24 de julio de 2026), la Knowledge Base vectorizada en **Supabase** y las skills del agente para este proyecto. El plan y el documento 10 todavía dicen Hostinger. Después vienen DeepSeek para volver más naturales las plantillas de la Fase 5 (siempre con el control de salida), la Fase 6 (PWA y dashboard del paciente, agregada el 20 de octubre de 2026), la Fase 7 (dashboard completo y herramientas internas) y la Fase 8 (WhatsApp Business Platform).

Decisiones del 9 de octubre de 2026:

- Las pruebas son solo con pacientes de **Bogotá**; otras altitudes quedan en espera.
- La **firma del médico** se hace al terminar el proyecto; mientras se construye no es un bloqueo.
- La Fase 5 (catálogo de recomendaciones, frases prohibidas centralizadas y control de salida) se construye después, junto con Carlos.

Decisión del 10 de octubre de 2026: **el MVP usa solo pruebas de sangre.** Orina y heces quedan en pausa (uroanálisis, albúmina/creatinina en orina, sangre oculta, antígeno de *H. pylori* y coprológico). `motor.analizar()` trabaja por defecto con `panel: solo_sangre` (`reglas_parte1.yaml > panel`): descarta esos resultados, marca 6 condiciones, REL-010 y SEG-013 como `pausada_mvp` y anota en la vista médica las 5 condiciones que se evalúan a medias. Con `contexto["panel"] = "completo"` se evalúa todo; así corren las partes 1 a 4 de las pruebas, y `probar_mvp.py` prueba el modo solo sangre. Las fichas no se borran.

Decisiones del 10 de octubre de 2026 (propuesta aprobada, `docs/02_plan_y_decisiones/Propuesta_ampliacion_condiciones_sangre.md`):

- **10 condiciones y 4 relaciones nuevas solo con sangre**, más 4 índices calculados (TyG, TG/HDL, Mentzer y NLR). Se prueban en `probar_parte5.py`. Sus umbrales están marcados "por verificar".
- **Pruebas nuevas:** factor reumatoide y grupo sanguíneo en la base; electroforesis de hemoglobina y de proteínas, 17-OHP, haptoglobina y anti-CCP (opcional) como reflejas.
- **10 vitaminas fuera del panel base** (A, E, K1, C, B1, biotina, niacina, CoQ10, omega-3 y omega-6/omega-3) y la **B6 opcional**. Las fichas se conservan.
- **Pregunta obligatoria al paciente en el MVP: "¿tomas biotina?"** Va en el contexto como `toma_biotina` (true o false) y, si es true, bloquea la lectura de tiroides, B12 y folato. Sin respuesta, la vista médica lo marca como dato faltante.
- **Complementos pagados** (AMH, paquete de vitaminas, omega-3): aplazados; recordárselo a Carlos más adelante.
- **Wearables en el MVP:** Apple Health y Android Health Connect, mediante una app móvil mínima de Saludly, con frecuencia en reposo y VFC, pasos, actividad y VO2 máx, sueño, presión, peso y temperatura. Son contexto, nunca umbral. Hoy el motor solo acepta banderas simples en `contexto["wearable"]` (REL-023, REL-025 y REL-026); la integración no está construida.

Pendientes externos: el PDF real del laboratorio, el formulario de la visita de la enfermera y la consulta legal sobre el INVIMA. El detalle está en `docs/02_plan_y_decisiones/Saludly_Plan_de_implementacion.md`.

Decisiones del 11 de octubre de 2026:

- **Carlos aprueba todo por ahora** (hace de médico revisor); no hay un paso de aprobación médica aparte en las demos.
- **El paciente ve los valores exactos del PDF.** La hemoglobina ajustada por altitud solo aparece en la vista médica; al paciente se le explica que en Bogotá se compara con un límite más alto.
- **Las 10 vitaminas fuera del panel base** se descartan en el motor como la orina y las heces (`reglas_parte1.yaml > panel > solo_sangre > biomarcadores_fuera_del_panel`); el médico las ve en `dudas_lectura`.
- **Las recomendaciones pueden tener texto por sexo** (`por_sexo` en `knowledge_base/fase5`).
- **Demo con médicos el miércoles 14 de octubre de 2026**, desde el celular de Carlos, con el artifact privado del recorrido (4 casos; abre en el digestivo para el primer médico, gastroenterólogo).

Fase 5 (10 de octubre de 2026, con Carlos): redacción en idioma paciente sin diagnosticar (qué es, por qué te aparece con tus valores, riesgo claro, un ejemplo simple, incertidumbre); **plantillas ahora y DeepSeek después**; el paciente elige **3 de los 10 objetivos**, responde la biotina y su **nivel de actividad física** (sedentario, ligero, moderado o alto) en la PWA; edad, sexo, ayuno y hora salen del PDF; la ciudad es Bogotá por defecto; la **enfermera aporta presión, cintura, peso y talla**. Recomendaciones clínicas atadas a hallazgos (cada hallazgo tiene al menos una) y **una receta por día por WhatsApp** de un catálogo propio, con nutrientes calculados con la tabla de alimentos. El dashboard (https://github.com/saludly/saludly-dashboard, privado) es un primer borrador: el informe sigue el contrato 10.5 ampliado (ver `codigo/pipeline/README.md`).
