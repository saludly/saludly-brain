# docs · Documentación de Saludly Brain

En esta carpeta va todo lo que explica el producto: **qué** hace, **por qué** y **con qué evidencia clínica**. Nada de aquí lo lee el código. Lo que el motor usa está en [`../knowledge_base/`](../knowledge_base/00_INDEX.md).

## Qué hay en cada carpeta

### `01_serie_saludly_brain/` · Definición del producto

Son los 10 documentos que definen Saludly Brain de principio a fin, en versión 1 del 6 de octubre de 2026. Para entender el producto, se leen en orden.

| Doc | Tema | Para qué sirve |
|---|---|---|
| 01 | Definición del producto | Qué es Saludly Brain, para quién es y qué no hace |
| 02 | Arquitectura funcional | El flujo de 13 pasos, del examen al informe. Es el documento base |
| 03 | Knowledge Base / RAG | Esquema de las fichas, reglas de vitaminas, conflictos entre guías (03.6) y relaciones (03.7) |
| 04 | Motor de análisis | Estados del dato, clasificación, confusores, coincidencia y escalamiento |
| 05 | Seguridad y escalamiento | Niveles de 0 a 3, canales, frases prohibidas y control de salida |
| 06 | Experiencia de usuario | Informe en 6 partes, dashboard y vistas por rol |
| 07 | Recomendaciones y personalización | Objetivos de salud, wearables y tipos de recomendación |
| 08 | Datos e integraciones | Laboratorio, Apple Health, WhatsApp y datos personales |
| 09 | Modelo de negocio | Modelo con EPS y cobro con cargo a la UPC |
| 10 | Especificación para desarrollo | Contratos de datos en JSON, estructura del repositorio y criterios de aceptación. **El más útil para programar** |

### `02_plan_y_decisiones/` · Plan y decisiones

| Archivo | Para qué sirve |
|---|---|
| `Saludly_Plan_de_implementacion.md` (y `.docx`) | El plan maestro: las decisiones tomadas, las 10 fases (de la 0 a la 9), riesgos y pendientes. Usa las imágenes `arquitectura.png` y `ruta.png` |
| `Costos_biomarcadores_ECOFAM_2025.md` | Estimación referencial (no oficial) del costo de los 133 biomarcadores originales con las tarifas de ECOFAM 2025; incluye una nota con los cambios del 10 de octubre |
| `Solicitud_pruebas_laboratorio.pdf` | Lista de pruebas para presentar al laboratorio y pedir cotización: 66 pruebas de sangre del panel estándar y 23 reflejas, sin precios (orina y heces en pausa en el MVP; sin las vitaminas retiradas). Se genera con `codigo/herramientas/generar_solicitud_laboratorio.py` |
| `Integracion_dashboard.md` | Cómo se conecta el informe con el borrador del dashboard (repositorio saludly-dashboard) y qué partes del borrador chocan con las reglas de Saludly |
| `Fase5_decisiones_para_revisar.md` | Decisiones clínicas tomadas al escribir los textos para el paciente, las recomendaciones y las recetas (10 de octubre de 2026), para que Carlos las apruebe |
| `Propuesta_ampliacion_condiciones_sangre.md` | Propuesta **aprobada** y construida (10 de octubre de 2026): comparación con Function Health y Superpower, 12 condiciones nuevas solo con sangre, pruebas baratas nuevas y qué vitaminas quitar |
| `Consolidado.md` | Resumen de los Lotes 1 a 6: las 12 especialidades, las condiciones, el panel estándar y las reflejas. Es anterior al catálogo ampliado de 112 valores |

### `03_investigacion_clinica/` · Investigación clínica

Es la evidencia de la que salen las reglas.

| Archivo | Para qué sirve |
|---|---|
| `Lote 1` a `Lote 6` | La matriz de condiciones por especialidad: patrones, guías, detectabilidad y conflictos entre guías |
| `Relaciones entre 100 Biomarcadores.md` | Cómo se conectan biomarcadores de módulos distintos. De aquí salen las 27 relaciones |
| `Protocolo de toma domiciliaria.md` | Tubos, transporte y preguntas al laboratorio. Es un borrador 0.1 |

### `04_fichas_compiladas/` · Fichas compiladas

Versiones para leer de las fichas: cada documento junta muchas fichas en uno solo. **Las fichas sueltas y vigentes que usa el motor están en `knowledge_base/`.** Si hay diferencias, manda `knowledge_base/`.

| Archivo | Contenido |
|---|---|
| `M1_…` a `Módulo M6 …` | Fichas de condición de cada uno de los 6 módulos |
| `Fichas de biomarcador · Tanda 1 a 4` | Las 33 fichas que se escribieron en la Fase 1 (orina, heces, serologías, vitaminas, reflejas y calculados) |
| `Fichas de seguridad del catálogo` | Las 15 reglas de seguridad (SEG-000 a SEG-014) |

### `05_informes_de_pruebas/` · Informes de pruebas

Resultados de la construcción del lector (Fase 3) y del motor (Fase 4): qué se probó, qué errores aparecieron y cómo se corrigieron, y qué supuestos quedaron pendientes para el médico.

| Archivo | Cubre |
|---|---|
| `Lector del PDF · Informe de pruebas` | Fase 3, el lector |
| `Motor_parte1` | Cálculos y clasificación (90 comprobaciones) |
| `Motor_parte2` | Condiciones M1 y M2 y SCORE2-PURE (167) |
| `Motor · Parte 3` | Condiciones M3 a M6 (175) |
| `Motor · Parte 4` | Relaciones, seguridad y salida final (76) |

## Dónde buscar qué

- **Qué hace el producto:** documentos 01 y 02
- **Qué tengo que programar:** documento 10, más el plan de implementación
- **Por qué una regla es así:** el Lote correspondiente y la ficha en `knowledge_base/`
- **Qué falta decidir:** la sección "Lo que sigue pendiente" del plan y la sección "Pendientes" de cada informe de pruebas
