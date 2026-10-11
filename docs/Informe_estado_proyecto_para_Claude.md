# Saludly Brain · Informe de estado del proyecto

**Corte: 11 de octubre de 2026.** Documento de traspaso para usar como contexto en otro proyecto de Claude. Resume qué es Saludly Brain, en qué fase va, qué se decidió, qué está construido, qué falta, las memorias de trabajo y las skills usadas.

> **Sin secretos.** Este documento no trae llaves ni contraseñas. Viven solo en el archivo `.env` de la carpeta del proyecto, que no va a git.

---

## 1. Qué es Saludly Brain

Saludly es una empresa de salud preventiva de Bogotá. Una enfermera toma **una sola muestra de sangre a domicilio**, un laboratorio aliado la procesa y envía un PDF, y **Saludly Brain**, un agente de IA médico, lee ese PDF, evalúa más de 100 biomarcadores con reglas clínicas y entrega:

- al **paciente**, un informe en 6 partes en un dashboard (PWA) y recomendaciones saludables por WhatsApp, incluida una receta diaria;
- al **médico**, una vista clínica con hallazgos, guías, reflejas pendientes y datos faltantes.

**Nada es un diagnóstico.** Cada hallazgo es un resultado observado, un patrón compatible, un riesgo potencial o una condición que requiere evaluación médica.

**Usuario y dueño:** Carlos, CEO de Saludly. Todo se trabaja en **español** (documentos, código, variables y comentarios). Carlos hace de médico revisor durante las pruebas. Usa VS Code con Claude Code en Windows 11 y Python 3.14.

**Modelo de negocio objetivo:** que las EPS paguen el servicio por paciente con cargo a la UPC, con la tesis de que detectar riesgos a tiempo baja costos. **Competencia estudiada:** Function Health y Superpower (Estados Unidos).

---

## 2. Principio de diseño y reglas que no se rompen

```
PDF del laboratorio → Lector (extrae y normaliza) → Motor de reglas en Python (cálculos, condiciones, relaciones, seguridad)
                    → Redacción (plantillas hoy; DeepSeek después) → Control de salida → Informe (PWA) + WhatsApp
```

1. **Los umbrales los evalúa el código, nunca el LLM.** El motor decide qué se cumple; el LLM (DeepSeek) solo redacta a partir de la salida del motor.
2. **No se inventan datos.** No medido, no detectable, menor que el límite e inválido son estados distintos; ninguno es cero. Un nombre que no está en los sinónimos queda como duda: solo valen coincidencias exactas.
3. **Nada es diagnóstico.** Cuatro niveles de lenguaje; las frases prohibidas viven en la Knowledge Base y las revisa un control de salida automático.
4. **Las decisiones clínicas son del médico revisor (Carlos durante las pruebas).** No se cambian umbrales, coincidencias ni escalamientos sin aprobación; lo provisional se marca "por verificar".
5. **Solo datos sintéticos.** Hacia un LLM externo se seudonimiza: edad, sexo, valores y contexto, nunca nombre ni documento.
6. **Regulación:** Ley 1581 de 2012 (datos de salud sensibles) e INVIMA (consulta legal pendiente).

---

## 3. Estado por fase

| Fase | Qué es | Estado al 11 de octubre de 2026 |
|---|---|---|
| 0 | Definiciones de producto y clínica | Hecha en versión 1 (serie de documentos 01 a 10) |
| 1 | Knowledge Base ejecutable | Hecha y ampliada: 144 fichas de biomarcador, 86 de condición, 31 relaciones, 15 de seguridad |
| 2 | Servidor: OpenClaw en un VPS de DonWeb con DeepSeek | **Siguiente paso.** El VPS no se ha comprado. El RAG ya está en Supabase |
| 3 | Lector del PDF | Hecho. Lee el 100 % de los campos del PDF de ejemplo (formato propio de Saludly) |
| 4 | Motor de análisis | Hecho. **662 de 662 pruebas.** En el MVP trabaja solo con sangre |
| 5 | Redacción, recomendaciones e informe | **Hecha con plantillas:** 119 textos para el paciente, 189 recomendaciones, 190 recetas y el comando de punta a punta (76 de 76 pruebas). DeepSeek, después |
| 6 | Dashboard (PWA), herramientas internas | Hay un borrador en Lovable; falta conectarlo al informe |
| 7 | WhatsApp Business Platform (API oficial) | Pendiente. Los mensajes ya se generan |
| 8 | Piloto controlado | Pendiente |
| 9 | Escala y modelo con EPS | Pendiente |

**Git:** carpeta local `C:\Users\Carlos\Documents\Saludly Proyecto IA`, sin remoto. El último commit es `9b0a89e` en la rama **`fase5-mvp`**: MVP solo sangre, ampliación de condiciones y Fase 5. **Todavía no se ha fusionado a `main`.**

---

## 4. Decisiones de Carlos (cronológicas)

### 6 de octubre de 2026 (fases 0 y 1)
- 50 condiciones incluidas. VIH, sífilis, clamidia y gonorrea quedan fuera; infectología se queda con hepatitis B, hepatitis C y Chagas.
- Cortisol solo con toma entre 6:00 y 10:00. ACTH solo para el médico. Las hormonas del ciclo se leen con la fecha de la última menstruación.
- Todas las tomas en ayunas y por la mañana.
- Saludly diseñó su propio PDF de ejemplo (órdenes LCD-2026-100123, hombre de 46 años, y LCD-2026-100124, mujer de 34) mientras llega el formato real del laboratorio.

### 9 de octubre de 2026
- La carpeta se reorganizó, porque el código vivía en zips: `docs/`, `knowledge_base/`, `codigo/`, `pdf_ejemplo/` y `_archivo/`.
- **Solo pacientes de Bogotá** en las pruebas: la hemoglobina se ajusta por altitud (2.640 m) y otras ciudades quedan en espera.
- **La firma médica se hace al terminar el proyecto.** No se pide ni se lista como riesgo mientras se construye.
- **Infraestructura:**
  - VPS en **DonWeb** (2 vCPU, 4 GB, 10 GB, backup diario) con **OpenClaw**; todavía no se compra.
  - **Supabase** en la nube, solo para la Knowledge Base, nunca para datos de pacientes. El proyecto es `saludly-brain-kb` en sa-east-1.
  - **Un solo agente** con todas las skills, usando DeepSeek `deepseek-v4-pro`.
  - El código llega al VPS por un repositorio privado de GitHub.
- **Flujo del MVP:**
  - El PDF no se guarda. Llega por la plataforma administrativa o por correo al agente; se lee y se descarta.
  - Solo se guarda lo extraído, en Markdown y con un seudónimo.
- **Embeddings** locales con Ollama `bge-m3` (1.024 dimensiones). Claude no genera embeddings; se calcularon en el computador de Carlos.

### 10 de octubre de 2026
- **El MVP usa solo pruebas de sangre.** Orina y heces quedan en pausa: uroanálisis, albúmina/creatinina en orina, sangre oculta, antígeno de *H. pylori* y coprológico. El motor trabaja por defecto con `panel: solo_sangre`.
- **Ampliación aprobada** después de comparar con Function Health y Superpower:
  - 10 condiciones y 4 patrones nuevos, todos solo con sangre:
    - eritrocitosis ajustada por altitud;
    - trombocitosis;
    - rasgo talasémico;
    - macrocitosis sin anemia;
    - dos o más líneas bajas;
    - posible gammapatía;
    - cortisol matutino bajo;
    - diabetes con posible falta de insulina;
    - resistencia a la insulina por TyG;
    - transición a la menopausia;
    - patrones de SOP metabólico, eritrocitosis con testosterona, NLR con PCR y factor reumatoide.
  - 4 índices calculados: TyG, TG/HDL, Mentzer y NLR.
  - Pruebas nuevas baratas: factor reumatoide y grupo ABO/Rh. Reflejas nuevas: electroforesis de hemoglobina, electroforesis de proteínas, 17-OHP y haptoglobina; anti-CCP opcional.
  - **10 vitaminas fuera del panel base**, por especializadas: A, E, K1, C, B1, biotina, niacina, CoQ10, índice omega-3 y relación omega-6/omega-3. **La B6 queda opcional.**
- **Pregunta obligatoria en la PWA: "¿tomas biotina?"** Si la respuesta es sí, no se interpretan tiroides, B12 ni folato.
- **Complementos pagados** (AMH, paquete de vitaminas, omega-3, repetición a 6 meses): **aplazados.** Recordárselos a Carlos más adelante.
- **Precios de ECOFAM 2025:** solo referenciales, no oficiales. Se actualizan cuando haya negociación con el laboratorio.
- **El MVP es una PWA**, sin app nativa. **Los wearables van cuando el MVP ya funcione.** Con una PWA no se pueden leer Apple Health ni Health Connect; las salidas posibles son los Atajos de iPhone, las APIs en la nube (Garmin, Fitbit, Oura, Whoop, Polar, Withings) o una app nativa más adelante.
- **Fase 5:**
  - Idioma paciente sin diagnosticar: qué es, por qué le aparece con sus valores, riesgo claro, un ejemplo simple e incertidumbre.
  - **Plantillas ahora y DeepSeek después**, siempre con el control de salida.
  - **Datos del paciente en la PWA:** elige **3 de 10 objetivos**, responde lo de la biotina y su **nivel de actividad física** (sedentario, ligero, moderado o alto).
  - **Del PDF salen** la edad, el sexo, las horas de ayuno y la hora de toma. La **ciudad es Bogotá** por defecto.
  - **La enfermera aporta** presión, cintura, peso y talla.
  - **Contenido:** recomendaciones clínicas reales y **una receta diaria por WhatsApp** de un **catálogo propio**; a la larga, quizá una API de recetas.
- **Aprobaciones clínicas de Carlos:**
  - El texto del potasio alto puede nombrar el corazón.
  - Ante cualquier riesgo cardiovascular, aunque sea leve, se pide consulta antes del ejercicio intenso.
  - Los alimentos aproximados se verifican con la tabla del ICBF (hecho).

---

## 5. Qué está construido

### Knowledge Base (`knowledge_base/`, fuente de verdad clínica)

| Pieza | Cantidad |
|---|---|
| Fichas de biomarcador | 144: 92 del panel estándar, 24 reflejas, 17 calculadas, 10 fuera del panel base y 1 opcional |
| Fichas de condición (6 módulos) | 86: 56 incluidas y 30 de apoyo |
| Relaciones entre módulos | 31 (patrón, vigilar y fuera de patrones) |
| Reglas de seguridad | 15 (SEG-000 a SEG-014) |
| Casos de prueba | Unitarios y de punta a punta (E2E-01 hombre, E2E-02 mujer) |
| Índice | `00_INDEX.json` y `00_INDEX.md`, generados desde las fichas |

**Módulos:** M1 cardiometabólico, M2 riñón y glándulas, M3 sangre y nutrición, M4 digestivo e infecciones, M5 mujer y hombre, M6 inmunidad y envejecimiento.

### Fase 5 (`knowledge_base/fase5/`)

| Pieza | Contenido |
|---|---|
| `ESQUEMAS.md` | Formatos y reglas de lenguaje |
| `objetivos.yaml` | Los 10 objetivos: salud general, prevenir, cuidar una condición, bajar de peso, masa muscular, rendimiento, maratón, ser más atlético, energía y sueño, envejecer saludable |
| `redaccion/` | 119 textos por hallazgo (con variantes por estado para la hepatitis B) y `modulos.yaml` ("lo que está bien") |
| `recomendaciones/` | 189 recomendaciones de 9 tipos, cada una atada a hallazgos, con contraindicaciones, objetivos que prioriza y su mensaje de WhatsApp |
| `recetas/` | 140 alimentos (USDA y la tabla del ICBF de 2015; 2 siguen aproximados) y 190 recetas colombianas propias: 45 desayunos, 35 meriendas, 60 almuerzos y 50 cenas |
| `frases_prohibidas.yaml` | Generado: 10 patrones y frases de 111 fichas |

### Código (`codigo/`)

| Carpeta | Qué hace |
|---|---|
| `motor/` | Motor en Python: 25 cálculos, clasificación, 86 evaluadores de condición, relaciones, seguridad y `ensamblar()`. Pruebas en 6 partes: **662 de 662** |
| `lector_pdf/` | Lector del PDF: verifica identidad (documento y orden), extrae, normaliza y marca dudas |
| `informe/` | Redacción (6 partes, vista médica, WhatsApp), selección de recomendaciones, nutrición (nutrientes, metas con Mifflin-St Jeor y plan de recetas) y control de salida |
| `pipeline/` | `saludly.py`: PDF → informe JSON + Markdown. Pruebas **76 de 76**. Contrato TypeScript en `contrato/informe.ts` y ejemplos en `ejemplos/` |
| `rag/` | Fragmenta, vectoriza (Ollama bge-m3), prueba la búsqueda (19 de 20) y sube a Supabase: **1.397 fragmentos** |
| `herramientas/` | `generar_indice.py`, `generar_frases_prohibidas.py`, `validar_fase5.py` (0 errores) y `generar_solicitud_laboratorio.py` |

**Comandos:**

```bash
pip install -r codigo/requirements.txt
cd codigo/motor && python pruebas/probar_todo.py            # 662 de 662
python codigo/herramientas/validar_fase5.py                 # 0 errores
python codigo/pipeline/pruebas/probar_pipeline.py           # 76 de 76
python codigo/pipeline/saludly.py --pdf … --documento … --orden … --perfil perfil.json --enfermera enfermera.json --salida salida/
```

### Documentos clave (`docs/`)

- Serie Saludly Brain 01 a 10. El documento 10 tiene los contratos de datos.
- Plan de implementación (todavía dice Hostinger y que no hay nada técnico construido; está desactualizado en eso).
- Lotes 1 a 6 de investigación clínica.
- `docs/02_plan_y_decisiones/`:
  - `Propuesta_ampliacion_condiciones_sangre.md`: aprobada.
  - `Fase5_decisiones_para_revisar.md`: 20 decisiones clínicas, algunas ya aprobadas.
  - `Integracion_dashboard.md`: mapeo entre el informe y el dashboard.
  - `Costos_biomarcadores_ECOFAM_2025.md`: referencial.
  - `Solicitud_pruebas_laboratorio.pdf`: 66 pruebas de sangre más 23 reflejas, sin precios.

### Dashboard

Repositorio privado `saludly/saludly-dashboard` (Lovable con TanStack Start). Es un borrador que funciona, con datos inventados. **No se ha modificado**, porque está conectado a Lovable. Choques con las reglas de Saludly, todavía por resolver:
1. Usa estados "óptimo" y "crítico"; la propuesta es "En rango · Fuera de rango · Requiere atención pronta".
2. Muestra un puntaje general de salud sin un modelo que lo respalde.
3. Dice "bebe 2,5 L de agua" a todos, aunque no aplica con enfermedad renal.
4. Recomienda suplementos con producto y precio del marketplace, lo que va contra la regla de no prescribir y la decisión de aplazar los complementos pagados.

---

## 6. Pendientes y siguientes pasos

1. **Fusionar la rama `fase5-mvp` a `main`**, si Carlos está de acuerdo.
2. **Fase 2:**
   - comprar el VPS de DonWeb;
   - instalar OpenClaw y DeepSeek;
   - instalar el modelo de embeddings `bge-m3` en el VPS (1,2 GB de RAM);
   - escribir las skills del agente: ingesta del PDF, motor, redacción, WhatsApp y consultas al RAG;
   - armar la plataforma administrativa.
3. **Conectar el dashboard** al informe con `contrato/informe.ts` y resolver los 4 choques.
4. **DeepSeek** para volver más naturales las plantillas, siempre pasando por el control de salida y con datos seudonimizados.
5. **WhatsApp Business Platform:** API oficial, plantillas aprobadas por Meta y opt-in.
6. **Wearables, después del MVP:** Atajos de iPhone o APIs en la nube.
7. **Propuesta en espera de visto bueno:** unos 7 cocientes calculados con utilidad clínica (brecha aniónica, APRI, glucosa promedio estimada, testosterona biodisponible, índice de andrógenos libres, HOMA-B, LDL/ApoB).
8. **Pendientes externos:**
   - el PDF real del laboratorio (hay que ajustar el lector);
   - la cotización oficial y la validación del protocolo de toma;
   - la consulta legal sobre el INVIMA;
   - la firma médica al final del proyecto.
9. **Revisar las decisiones clínicas** de `Fase5_decisiones_para_revisar.md` que siguen pendientes.

**Inconsistencias conocidas:**
- La prueba del PDF mezclado del lector necesita `qpdf`, que no está instalado.
- La ficha de parasitosis usa `stool_parasites`, un identificador que no existe; está en pausa.
- `_archivo/` aparece mencionado, pero podría no estar en la carpeta.
- El plan de implementación está desactualizado (dice Hostinger y que no hay nada construido).

---

## 7. Memorias de trabajo (copia completa, sin secretos)

> Estas son las memorias que Claude Code guarda para este proyecto. Se copian casi textuales para que el otro proyecto tenga el mismo contexto.

### Carlos
Carlos es CEO de Saludly (salud preventiva, Bogotá), no necesariamente desarrollador. Todo se trabaja en español: respuestas, documentos, código, variables y comentarios. Usa VS Code con la extensión de Claude Code (Windows 11, Python 3.14). Prefiere revisar antes de cambiar. **Cómo aplicarlo:** responder en español, explicar los riesgos en términos de producto y clínica además de los técnicos, y pedir confirmación antes de cambios grandes.

### Estado del proyecto
Saludly Brain es un agente de IA médico preventivo: lee el PDF del laboratorio, evalúa más de 100 biomarcadores con reglas en Python y genera un informe para el paciente y una vista médica. Verificado el 10 de octubre de 2026: el motor pasa 662 de 662 (el 9 de octubre eran 508). La Knowledge Base es la fuente de verdad clínica; el motor está en `codigo/motor/motor/` (`analizar()` en `motor.py`); los contratos están en el documento 10. El 9 de octubre se reorganizó la carpeta, que antes vivía en zips. El commit `9b0a89e` está en la rama `fase5-mvp`, sin fusionar.

### Reglas que no se rompen
Umbrales en código y nunca en el LLM; no inventar datos; nada es diagnóstico (4 niveles de lenguaje y frases prohibidas); las decisiones clínicas son del médico revisor; solo datos sintéticos y seudonimización hacia LLM externos. **Por qué:** es software clínico regulado en Colombia (Ley 1581 e INVIMA); un umbral mal aplicado se vuelve un hallazgo falso para un paciente.

### Sin firma médica durante la construcción
El proyecto lo firmará un médico al final. Mientras se construye no se pide la firma ni se lista como riesgo. Sigue valiendo no cambiar decisiones clínicas sin aprobación y marcar lo provisional.

### Alcance: Bogotá y Fase 5
Solo Bogotá: otras altitudes quedan en espera; en `reglas_parte1.yaml` solo existe la franja de 2.500 a 2.999 m. La Fase 5 se hizo con Carlos el 10 de octubre.

### Infraestructura: OpenClaw en DonWeb y Supabase
- VPS DonWeb (2 vCPU, 4 GB, 10 GB, backup diario) con OpenClaw. Todavía no se compra.
- Supabase solo para la Knowledge Base, nunca para pacientes: proyecto `saludly-brain-kb`, región sa-east-1. Los proyectos viejos "dashboard" y "saludly's Project" están pausados y no se tocan. Migraciones en `supabase/migrations/`; las llaves solo en `.env`.
- Un solo agente con todas las skills, usando DeepSeek `deepseek-v4-pro`.
- El código llega al VPS por un GitHub privado; Carlos usa GitHub Desktop y `gh` no está instalado.
- Carlos habla con el agente desde una plataforma administrativa (por crear). Los resultados van al dashboard y las recomendaciones a WhatsApp.
- Carlos hace de médico revisor en las pruebas.
- En el PC de Carlos: Node 24 y Ollama, sin WSL ni Docker.

### Correr las pruebas sin ensuciar
`probar_todo.py` reescribe `codigo/motor/pruebas/salida_*`. En sesiones de solo lectura, respaldar esos archivos, correr con `PYTHONDONTWRITEBYTECODE=1`, comparar y restaurar. `.gitattributes` normaliza los saltos de línea.

### Inconsistencias detectadas
- **Resueltas el 9 de octubre:** conteos de fichas, casos de punta a punta sincronizados, guardia del calcio en REL-020 y git iniciado.
- **Abiertas:**
  - La carpeta `_archivo/` se menciona en los documentos, pero podría no estar en la carpeta del proyecto.
  - La tabla de casos de HE-001 dice "no fuma → coincidencia alta", y el caso E2E-02 trae `tabaquismo: null`.
  - El plan de implementación está desactualizado.
  - `motor.py` tiene el docstring y el bloque `__main__` desordenados.
  - La prueba del PDF mezclado del lector necesita `qpdf`.

### Flujo del MVP
- El PDF no se guarda: se lee y se descarta. Llega por la plataforma o por correo.
- Solo se guarda lo extraído, en Markdown y con seudónimo; nunca en Supabase ni en git.
- El paciente da sus 3 objetivos (además de la biotina y el nivel de actividad).
- Los objetivos solo ordenan las recomendaciones; nunca cambian umbrales ni hallazgos.
- Embeddings con Ollama `bge-m3`.
- **Preguntas abiertas:** cómo se asocia el PDF al paciente sin visita registrada, guardar la huella del PDF para auditoría y la seguridad del buzón de correo.

### MVP solo sangre y ampliación
Orina y heces en pausa. Ampliación del 10 de octubre: 10 condiciones, 4 relaciones, 4 índices, pruebas nuevas, 10 vitaminas fuera del panel base, la B6 opcional y la pregunta de biotina. SEG-002 y SEG-009 no repiten alertas cuando la condición nueva está activa (SEG-009 sigue avisando si la gammapatía espera la electroforesis). Queda pendiente la propuesta de unos 7 cocientes. **Cómo aplicarlo:** no reactivar orina ni heces sin Carlos; toda prueba nueva debe ser barata y de laboratorio común; nada de cocientes "de marketing" sin guía.

### Fase 5: decisiones y estado
Las decisiones de la sección 4. Construido: `knowledge_base/fase5`, `codigo/informe` y `codigo/pipeline` (76 de 76), y el RAG actualizado. Dashboard revisado (ver `Integracion_dashboard.md`). Aprobado: el potasio alto nombra el corazón y la consulta antes del ejercicio intenso ante cualquier riesgo cardiovascular. **Cómo aplicarlo:** todo contenido nuevo pasa `validar_fase5.py`; si cambian las fichas, se regeneran las frases prohibidas; el objetivo solo ordena.

### Wearables
El MVP es una PWA, sin app; los wearables van **después de que el MVP funcione**. Antes se había pensado en una app para Apple Health y Health Connect con frecuencia en reposo y VFC, pasos, actividad y VO2 máx, sueño, presión, peso y temperatura. Hoy el motor solo acepta banderas en `contexto["wearable"]`. Son contexto, nunca umbral.

### Complementos pagados (recordar)
Aplazados el 10 de octubre: AMH, paquete de vitaminas, omega-3 y una repetición a los 6 meses. Recordárselo a Carlos cuando se hable de modelo de negocio, precios, la cotización con el laboratorio o al terminar el MVP.

### Costos ECOFAM 2025 (referenciales)
El anexo de ECOFAM sirvió solo para estimar. De 133 biomarcadores: 61 con precio, 47 ofrecidos sin precio, 12 no ofrecidos y 13 calculados. Total parcial referencial: mujer $674.500 y hombre $629.500. Con los cambios del MVP, unos $624.500 y $579.500. **No son precios oficiales;** se actualizan cuando haya negociación.

---

## 8. Skills y herramientas usadas en Claude Code

| Skill o herramienta | Para qué se usó |
|---|---|
| **`anthropic-skills:pdf`** (skill) | Generar con reportlab el PDF "Solicitud de pruebas al laboratorio" y leer el anexo de tarifas de ECOFAM |
| **Subagentes (`general-purpose`)** | Investigar a Function Health y Superpower; escribir en paralelo los 119 textos para el paciente, las 189 recomendaciones, la tabla de 140 alimentos y las 190 recetas; verificar los alimentos con la tabla del ICBF |
| **Herramientas de archivos y consola** (leer, editar, Bash y PowerShell) | Todo el código, las fichas y las pruebas |
| **Python en un entorno virtual** | `pdfplumber`, `pyyaml`, `reportlab` y `pypdfium2` (para mostrar páginas de PDF) |
| **Ollama con `bge-m3`** (en el PC de Carlos) | Embeddings del RAG |
| **Supabase CLI** (`npx supabase`) | Migraciones de la tabla de la Knowledge Base |
| **Git y Git Credential Manager** | Commits locales y clonar el dashboard privado |

**Skills del agente de OpenClaw (por construir en la Fase 2):** ingesta del PDF (plataforma o correo, sin guardarlo), análisis (lector, motor e informe con `codigo/pipeline/saludly.py`), consulta del RAG por identificador o por búsqueda híbrida, redacción con DeepSeek pasando por el control de salida, y envío por WhatsApp con las reglas de canal (nada de escalamiento 3 ni serologías reactivas).

---

## 9. Cómo usar este documento en otro proyecto de Claude

1. Súbelo como conocimiento del proyecto, junto con `CLAUDE.md`, `README.md`, `docs/README.md` y `codigo/pipeline/README.md`.
2. Pídele a Claude que respete las reglas de la sección 2 y que trabaje en español.
3. Para preguntas clínicas, la fuente de verdad son las fichas de `knowledge_base/`; para el producto, los documentos 01 a 10 de `docs/01_serie_saludly_brain/`.
4. Este documento es una foto del 11 de octubre de 2026. Si el proyecto cambia, genera uno nuevo.
