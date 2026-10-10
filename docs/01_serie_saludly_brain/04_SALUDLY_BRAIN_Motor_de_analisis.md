**SALUDLY BRAIN**

**04 — Motor de análisis e interpretación**

*Cómo pasa Saludly Brain de un PDF a una lista de hallazgos trazables · versión 1 · 6 de octubre de 2026*

> Las decisiones clínicas de este documento las tomó Claude por encargo del equipo de Saludly. Antes de usarse con pacientes reales necesitan la firma de un médico.

# **04.1 — Principio de diseño**

Las reglas deciden; el modelo de lenguaje explica. El motor evalúa umbrales, criterios y niveles con código determinista sobre el Knowledge Base (documento 03). DeepSeek recibe hallazgos ya decididos y las fichas que los explican, y redacta. El modelo nunca crea un hallazgo, cambia un nivel ni elige un umbral.

# **04.2 — Etapas**

| Etapa | Entrada | Salida | Quién la hace |
| :---- | :---- | :---- | :---- |
| 1 · Ingesta | PDF cargado por operaciones | Archivo guardado con huella (hash), quién lo cargó y cuándo | Servicio de ingesta |
| 2 · Identidad | Documento y orden del PDF | PDF asociado a la visita correcta, o rechazado | Servicio de ingesta |
| 3 · Extracción | PDF | Filas: nombre, resultado, indicador, unidad, intervalo, método, sección, observaciones | Lector del formato (IA solo como respaldo) |
| 4 · Normalización | Filas | Cada fila con su identificador interno, valor numérico y unidad canónica, conservando el original | Diccionario de sinónimos y reglas de unidades |
| 5 · Validación | Resultados normalizados | Estado del dato y dudas marcadas | Reglas de validación |
| 6 · Cálculos | Resultados válidos y perfil | 12 derivados y PhenoAge, con trazabilidad | Motor |
| 7 · Contexto | Visita de la enfermera, perfil, objetivo, Apple Health | Contexto del análisis | Motor |
| 8 · Clasificación | Valores y contexto | Clase de cada valor | Motor |
| 9 · Confusores | Contexto | Ajustes a la interpretación | Motor |
| 10 · Patrones | Clases, contexto, reglas | Hallazgos por módulo y entre módulos | Motor |
| 11 · Riesgo | Hallazgos | Coincidencia, escalamiento, nivel de lenguaje y orden | Motor |
| 12 · Redacción | Hallazgos y fichas | Textos para paciente y médico | Agente en OpenClaw con DeepSeek |
| 13 · Control de salida | Textos | Textos aprobados o rechazados | Validador automático y médico |

# **04.3 — Estados del dato**

| Estado | Ejemplo en el PDF | Qué hace el motor |
| :---- | :---- | :---- |
| Medido | "112" | Clasifica |
| Menor que el límite | "< 3" | Guarda el límite; clasifica como por debajo si el límite está bajo el intervalo |
| Mayor que el límite | "> 2000" | Guarda el límite; clasifica como alto |
| No detectable / cualitativo | "No reactivo", "Negativo" | Guarda el texto y su equivalente codificado |
| Inválido | "No procesado", "Muestra no apta" | No clasifica; lo informa y, si aplica, pide nueva muestra |
| No medido | No aparece en el PDF | No inventa; marca el dato como faltante |

Ningún estado distinto de "medido" se convierte en cero.

# **04.4 — Clasificación**

Cada valor recibe una de seis clases:

1. **No interpretable:** dato inválido, unidad dudosa, contexto obligatorio faltante (por ejemplo, ayuno menor de 8 horas para glucosa, o cortisol tomado fuera de 6:00 a 10:00).
2. **Crítico:** bandera crítica del laboratorio o umbral de urgencia escrito en una guía. Saludly no inventa umbrales de urgencia.
3. **Bajo / Alto:** fuera del intervalo de referencia del laboratorio.
4. **Limítrofe:** dentro del intervalo del laboratorio pero fuera de un umbral clínico que la ficha o la guía definen (por ejemplo, ALT entre 33 UI/L y el límite del laboratorio en hombres).
5. **En rango.**

Si el laboratorio no reporta intervalo ("No establecido"), el valor se muestra sin clase.

# **04.5 — Cálculos**

Solo se calculan si están todas las variables, en estado medido, y se cumplen sus condiciones. Cada derivado guarda de qué valores salió.

| Derivado | Fórmula o fuente | Condiciones |
| :---- | :---- | :---- |
| HOMA-IR | glucosa (mg/dL) × insulina (µUI/mL) / 405 | Ayuno de 8 horas o más; no en personas que usan insulina |
| Colesterol no-HDL | colesterol total − HDL | — |
| Colesterol remanente | colesterol total − HDL − LDL | LDL medido o calculado declarado |
| Relación colesterol total/HDL | colesterol total / HDL | — |
| Saturación de transferrina | hierro / TIBC × 100 | Si el laboratorio la reporta, manda la del laboratorio |
| TFG estimada | CKD-EPI 2021 con creatinina, sin coeficiente de raza | Creatinina trazable a IDMS; si el laboratorio la reporta, se compara y se usa la del laboratorio |
| Testosterona libre | Fórmula de Vermeulen con testosterona total, SHBG y albúmina | Solo si los tres están medidos |
| Globulinas | proteínas totales − albúmina | — |
| Relación albúmina/globulina | albúmina / globulinas | — |
| Relación BUN/creatinina | BUN / creatinina | — |
| Relación ApoB/ApoA1 | ApoB / ApoA1 | — |
| INR | Reportado por el laboratorio | No se recalcula |
| Edad biológica | PhenoAge (Levine, 2018) con edad y 9 analitos: albúmina, creatinina, glucosa, PCR, % de linfocitos, VCM, RDW, fosfatasa alcalina y leucocitos | Los 9 medidos; coeficientes del artículo original verificados contra su ejemplo publicado |

Fórmula CKD-EPI 2021 (creatinina): 142 × min(Cr/κ, 1)^α × max(Cr/κ, 1)^−1,200 × 0,9938^edad × 1,012 si es mujer, con κ = 0,7 y α = −0,241 en mujeres, y κ = 0,9 y α = −0,302 en hombres.

Las conversiones de unidades viven en una tabla versionada (por ejemplo, glucosa mg/dL × 0,0555 = mmol/L). Ninguna conversión se hace fuera de esa tabla.

# **04.6 — Confusores**

| Confusor (de la visita o del perfil) | Afecta | Qué hace el motor |
| :---- | :---- | :---- |
| Ayuno menor de 8 horas | Glucosa, triglicéridos, insulina, HOMA-IR | No interpretables |
| Ejercicio intenso en las últimas 48 horas | CK, AST, ALT, LDH, creatinina, albuminuria | Baja la coincidencia y sugiere repetir |
| Infección o fiebre en las últimas 2 semanas | hs-CRP, VSG, ferritina, leucocitos, fibrinógeno | hs-CRP no se usa como riesgo cardiovascular; ferritina se lee con el corte de inflamación |
| Alcohol en las últimas 48 horas | GGT, triglicéridos, ALT | Baja la coincidencia del patrón hepático |
| Menstruación actual | Sangre en orina, hematíes del sedimento | No se interpreta hematuria |
| Embarazo | Hormonas, hemoglobina, TSH, prolactina, ALP y otros | Reglas propias de embarazo o "no interpretable" |
| Suplemento de biotina o biotina alta | TSH, T4 libre, B12, folato y otros inmunoensayos | No se interpretan hasta repetir sin el suplemento |
| Corticoides | Glucosa, leucocitos, cortisol | Baja la coincidencia; cortisol no interpretable |
| Anticonceptivo hormonal | SHBG, hormonas del ciclo | Hormonas del ciclo no interpretables por fase |
| Hemólisis declarada | Potasio, LDH, AST | No interpretables; nueva muestra |
| Patrón muscular (CK, AST y LDH altas) | AST, LDH | No se leen como hepáticas |

# **04.7 — Patrones**

1. Se evalúan primero las reglas de cada módulo, en paralelo.
2. Después se evalúan las relaciones entre módulos del documento 03.
3. Un patrón necesita al menos dos señales concordantes y una explicación biológica plausible (la de su ficha).
4. Si falta un dato obligatorio, el patrón se marca "incompleto" y el informe dice qué falta.
5. Las condiciones que se excluyen entre sí (por ejemplo, prediabetes y diabetes en rango diagnóstico) se resuelven a favor de la más alta.

# **04.8 — Coincidencia, escalamiento y orden**

**Coincidencia.** Alta: todos los criterios centrales con datos completos. Moderada: criterios centrales con datos incompletos, o uno central más apoyo. Baja: solo criterios de apoyo; se muestra como "vigilar", nunca como condición.

**Escalamiento.**

| Nivel | Significado | Ejemplos |
| :---- | :---- | :---- |
| 0 | Informativo | Valores en rango; vitaminas en rango |
| 1 | Seguimiento de rutina: comentarlo en el próximo control | Prediabetes, LDL alto sin otros factores, vitamina D baja |
| 2 | Consulta médica recomendada en las próximas semanas | Sangre oculta positiva, albuminuria con TFG baja, déficit de hierro con anemia, serología reactiva, ANA desde 1:160 |
| 3 | Contacto del equipo médico de Saludly el mismo día hábil | Bandera crítica del laboratorio, troponina fuera de rango, glucosa menor de 54 mg/dL confirmada |

**Orden.** Escalamiento, luego coincidencia, luego fuerza de evidencia.

**Nivel de lenguaje.** Cada hallazgo lleva uno de los cuatro del documento 02: resultado observado, patrón compatible, riesgo potencial, condición que requiere evaluación médica.

# **04.9 — El papel de DeepSeek**

Entrada al modelo, siempre seudonimizada: edad, sexo, objetivo de salud, hallazgos con sus valores y niveles, fichas aplicables (cargadas por identificador), recomendaciones permitidas y frases prohibidas. Nunca nombre, documento ni teléfono.

Instrucciones fijas del agente: redactar solo sobre los hallazgos recibidos; no agregar hallazgos, umbrales ni dosis; respetar el nivel de lenguaje; citar la guía de cada hallazgo en la vista del médico; responder en español de Colombia, claro y sin alarmismo; devolver el JSON del contrato (documento 10).

Parámetros: temperatura baja, salida en JSON estructurado.

**Proveedor del modelo.** En pruebas, DeepSeek por API en la nube (aprobado). En operación, modelos locales de pesos abiertos en servidores con GPU. El motor habla con el modelo a través de OpenClaw, así que cambiar de proveedor es cambiar la configuración del modelo, no el motor. Antes del cambio, el modelo local debe pasar los mismos casos de prueba.

# **04.10 — Control de salida**

Un validador automático revisa cada texto antes de mostrarlo:

- Cada hallazgo mencionado existe en la lista del motor, con el mismo nivel.
- No aparece ninguna frase prohibida (documento 05) ni ningún número que no esté en los datos.
- No aparecen dosis de medicamentos ni de suplementos.
- El JSON cumple el esquema.

Si falla, se reintenta una vez; si vuelve a fallar, el informe queda en revisión manual. En el piloto, el médico aprueba todo lo que va al paciente.

# **04.11 — Pruebas**

Cada cambio en reglas, fichas, prompts o modelo corre el set completo de casos firmados. Criterio de paso: cero errores en casos críticos y de escalamiento 3, y ninguna frase prohibida. Los dos PDF de ejemplo (órdenes LCD-2026-100123 y LCD-2026-100124) son los primeros casos de extremo a extremo.
