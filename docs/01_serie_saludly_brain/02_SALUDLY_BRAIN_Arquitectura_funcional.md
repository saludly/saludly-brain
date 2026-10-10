**SALUDLY BRAIN**

**02 — Arquitectura funcional / Cómo funciona Saludly Brain**

*Documento de definición funcional del producto*

# **Objetivo del documento**

Este documento define cómo funciona Saludly Brain como producto: qué información recibe, cómo procesa los resultados de laboratorio, cómo utiliza el Knowledge Base (RAG), cómo identifica patrones y riesgos potenciales y cómo transforma ese análisis en recomendaciones comprensibles para el usuario.

Describe la arquitectura funcional del producto. No define todavía servidores, APIs, proveedores tecnológicos, infraestructura ni código.

# **02.1 — Objetivo de la arquitectura**

La función de Saludly Brain es transformar resultados de laboratorio en una visión preventiva y comprensible de la salud del usuario.

* Recibir resultados reales producidos por un laboratorio.  
* Extraer los biomarcadores y parámetros disponibles.  
* Identificar correctamente cada parámetro y su unidad.  
* Distinguir resultados medidos de parámetros calculados o derivados.  
* Aplicar cálculos únicamente cuando existan las variables necesarias y se cumplan sus condiciones de validez.  
* Combinar resultados, contexto del usuario y conocimiento científico.  
* Buscar relaciones y patrones entre diferentes resultados.  
* Identificar riesgos potenciales sin convertir automáticamente un patrón en un diagnóstico.  
* Generar recomendaciones preventivas y accionables.  
* Escalar a atención profesional cuando existan situaciones que lo requieran.

# **02.2 — Flujo completo del usuario**

El flujo funcional principal es:

| Paso | Módulo | Función |
| :---- | :---- | :---- |
| 1 | Usuario | Realiza un examen de laboratorio. |
| 2 | Resultado de laboratorio | El laboratorio procesa la muestra y genera los resultados. |
| 3 | Ingesta del PDF | El usuario carga el informe en Saludly. |
| 4 | Extracción de datos | Saludly identifica nombres, valores, unidades y demás información. |
| 5 | Normalización | Los resultados se relacionan con los identificadores internos de Saludly. |
| 6 | Cálculos | Saludly calcula parámetros derivados cuando existen datos suficientes y se cumplen las condiciones. |
| 7 | Contexto del usuario | Se incorpora la información contextual disponible. |
| 8 | Knowledge Base / RAG | El motor consulta conocimiento científico y reglas de seguridad. |
| 9 | Motor de análisis | Combina resultados, cálculos, contexto y conocimiento. |
| 10 | Detección de patrones | Busca relaciones relevantes entre múltiples parámetros. |
| 11 | Evaluación de riesgos | Identifica señales o riesgos potenciales manteniendo la incertidumbre. |
| 12 | Recomendaciones | Genera acciones generales y personalizadas. |
| 13 | Informe final | Entrega una explicación sencilla, estructurada y accionable. |

# **02.3 — Entrada de datos**

La entrada principal de esta primera fase es el informe de laboratorio, normalmente en PDF. Cuando estén disponibles, el sistema debe identificar:

* Nombre del biomarcador o parámetro.  
* Resultado.  
* Unidad.  
* Rango de referencia del laboratorio.  
* Fecha y hora de la toma o del resultado.  
* Identificación de la prueba u orden.  
* Comentarios y banderas del laboratorio.  
* Método analítico, cuando esté disponible.

La arquitectura debe asumir que diferentes laboratorios pueden presentar los mismos resultados con nombres, formatos, unidades o rangos de referencia diferentes.

# **02.4 — Procesamiento de resultados**

## **A. Extracción**

La IA convierte el informe en datos estructurados. En esta etapa no debe realizar una interpretación clínica innecesaria.

* Glucosa → 96 → mg/dL  
* HDL → 48 → mg/dL  
* Triglicéridos → 180 → mg/dL

## **B. Normalización**

La normalización permite reconocer que diferentes laboratorios pueden utilizar nombres distintos para el mismo parámetro.

* Glucosa / Glucose / GLU / Glucemia → mismo parámetro interno.  
* Conservar el valor original y su unidad reportada.  
* Las conversiones de unidades deben tener reglas explícitas y trazables.

## **C. Validación**

* Si el valor no fue encontrado, no se debe inventar.  
* Si la unidad no es clara, marcar la incertidumbre.  
* Si existen datos contradictorios, conservar la discrepancia y evitar una conclusión falsa.  
* Conservar el rango de referencia del laboratorio como contexto.

# **02.5 — Motor de análisis**

El motor combina cuatro fuentes:

* Resultados reales del laboratorio.  
* Parámetros calculados o derivados por Saludly.  
* Contexto declarado o disponible del usuario.  
* Knowledge Base / RAG con evidencia científica, relaciones, limitaciones y reglas de seguridad.

El objetivo no es interpretar cada biomarcador de forma aislada, sino analizar el conjunto y detectar relaciones clínicamente relevantes para prevención.

# **02.6 — Generación de riesgos y patrones**

Saludly Brain debe buscar patrones formados por varios parámetros. Un resultado alterado por sí solo no debe convertirse automáticamente en una enfermedad o diagnóstico.

Ejemplo conceptual:

Triglicéridos ↑ \+ HDL ↓ \+ Glucosa ↑ \+ HOMA-IR ↑  
↓  
Patrón metabólico potencial  
↓  
Evaluación preventiva  
↓  
Recomendaciones y, cuando corresponda, seguimiento profesional

El lenguaje final debe diferenciar entre resultado observado, patrón compatible, riesgo potencial y condición que requiere evaluación médica.

# **02.7 — Generación de recomendaciones**

Después de identificar los hallazgos relevantes, el sistema genera recomendaciones preventivas relacionadas con los resultados y el contexto del usuario.

* Alimentación.  
* Hidratación.  
* Actividad física y caminatas.  
* Sueño.  
* Hábitos generales de bienestar.  
* Lectura y otras actividades saludables.  
* Suplementos generales únicamente cuando corresponda y sin presentarlos como prescripciones.

Las recomendaciones deben ser concretas, comprensibles y accionables, estar relacionadas con los hallazgos y evitar alarmismo.

# **02.8 — Resultado final para el usuario**

**1\. Resumen general**

Explicación breve del panorama general.

**2\. Lo que está bien**

Principales resultados o patrones favorables.

**3\. Lo que merece atención**

Resultados o patrones que justifican seguimiento o cambios de hábitos.

**4\. Qué podría significar**

Explicación sencilla de posibles significados, manteniendo la incertidumbre.

**5\. Qué puedes hacer**

Recomendaciones prácticas relacionadas con los hallazgos.

**6\. Cuándo consultar**

Indicación clara de cuándo se requiere evaluación o atención profesional.

# **Diagrama maestro del flujo**

USUARIO  
↓  
EXAMEN DE LABORATORIO  
↓  
RESULTADOS  
↓  
INGESTA DEL PDF  
↓  
EXTRACCIÓN DE DATOS  
↓  
NORMALIZACIÓN Y VALIDACIÓN  
↓  
CÁLCULOS Y PARÁMETROS DERIVADOS  
↓  
CONTEXTO DEL USUARIO  
↓  
KNOWLEDGE BASE / RAG  
↓  
MOTOR DE ANÁLISIS  
↓  
DETECCIÓN DE PATRONES  
↓  
EVALUACIÓN DE RIESGOS  
↓  
RECOMENDACIONES  
↓  
INFORME PERSONALIZADO

# **Principios funcionales que deben mantenerse**

* Los resultados del laboratorio son la fuente primaria de los valores medidos.  
* Saludly no debe inventar datos que no estén presentes o no sean suficientemente claros.  
* Los parámetros calculados deben conservar trazabilidad hacia sus variables de entrada.  
* La interpretación debe considerar contexto y relaciones entre biomarcadores.  
* Un patrón o riesgo potencial no equivale automáticamente a un diagnóstico.  
* Las recomendaciones deben estar conectadas con los hallazgos y respetar las reglas de seguridad.  
* Los parámetros de mayor riesgo deben contar con reglas claras de escalamiento.  
* El Knowledge Base es la fuente de conocimiento clínico utilizada por el motor de análisis.

# **Relación con los demás documentos**

* Documento 01 → define qué es Saludly Brain y qué producto queremos construir.  
* Documento 02 → define cómo funciona el producto de principio a fin.  
* Documento 03 → define el Knowledge Base / RAG y el conocimiento clínico que utilizará el motor.  
* Documentos posteriores → detallarán el motor de análisis, seguridad, experiencia de usuario, recomendaciones, datos e implementación.

La secuencia que te propuse es conceptualmente:

1. **01 — Definición del producto / Product Definition** ← **ESTAMOS AQUÍ**  
2. **02 — Arquitectura funcional / cómo funciona Saludly Brain**  
3. **03 — Knowledge Base / RAG clínico**  
4. **04 — Motor de análisis e interpretación**  
5. **05 — Seguridad, límites y escalamiento**  
6. **06 — Experiencia del usuario / UX**  
7. **07 — Recomendaciones y personalización**  
8. **08 — Datos, integraciones y evolución futura**  
9. **09 — Modelo de negocio / producto comercial**  
10. **10 — Especificación final para desarrollo**

