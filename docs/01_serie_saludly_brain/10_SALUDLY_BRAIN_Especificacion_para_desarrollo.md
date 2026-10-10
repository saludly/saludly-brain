**SALUDLY BRAIN**

**10 — Especificación final para desarrollo**

*Componentes, contratos de datos, interfaces y criterios de aceptación · versión 1 · 6 de octubre de 2026*

> Lo que está marcado como "propuesta" es una elección técnica de Claude que el equipo puede cambiar. Lo que está marcado como "decidido" viene de las decisiones del equipo de Saludly.

# **10.1 — Componentes**

| Componente | Responsabilidad | Tecnología |
| :---- | :---- | :---- |
| Servicio de ingesta | Recibir PDF, verificar identidad, extraer, normalizar y validar | Propuesta: Python con pdfplumber |
| Motor de reglas | Cálculos, clasificación, confusores, patrones, coincidencia y escalamiento | Propuesta: Python; reglas en YAML desde el Knowledge Base |
| Agente Saludly Brain | Redactar informe, vista médica y recomendaciones | Decidido: OpenClaw en Hostinger |
| Modelo de lenguaje | Interpretación y redacción | Decidido: DeepSeek por API en pruebas; modelos locales en operación |
| Knowledge Base | Fichas, condiciones, relaciones, reglas, recomendaciones | Decidido: Markdown con YAML en un repositorio versionado |
| Índice de búsqueda | Texto de fichas para el agente y preguntas del médico | Decidido: memoria de OpenClaw con embeddings locales |
| API de Saludly | Datos de pacientes, visitas, informes, mensajes y permisos | Propuesta: Python (FastAPI) |
| Base de datos | Entidades del documento 08 | Propuesta: PostgreSQL, cifrada en reposo |
| Archivos | PDF originales | Propuesta: disco cifrado del VPS con copia de seguridad |
| Dashboard web | Paciente, médico y operaciones | Decidido: web; propuesta: mantener el stack del mock actual (TypeScript) |
| Formulario de la enfermera | Captura en la visita, sin conexión | Propuesta: aplicación web instalable en tableta |
| App iOS | Conectar Apple Health | Decidido: Apple Watch primero; propuesta: Swift con HealthKit |
| Mensajería | Avisos y recomendaciones | Decidido: WhatsApp Business Platform |

Todo corre en el VPS de Hostinger, salvo el modelo de lenguaje en pruebas (nube de DeepSeek) y la app iOS (en el teléfono del paciente). El plan de Hostinger lo compra el equipo cuando se llegue a la Fase 2.

# **10.2 — Flujo de extremo a extremo**

1. Operaciones carga el PDF en el panel → API guarda el archivo y su huella.
2. Ingesta verifica documento y orden contra la visita → si no coinciden, se detiene.
3. Ingesta extrae y normaliza → resultados con estado del dato.
4. Motor calcula, clasifica, aplica confusores, evalúa patrones → hallazgos con niveles.
5. API envía al agente de OpenClaw el paquete seudonimizado → el agente devuelve el informe en JSON.
6. Validador de salida revisa el JSON → aprobado o en revisión manual.
7. Médico revisa y aprueba → informe publicado.
8. Mensajería envía el aviso por WhatsApp (o el médico llama si hay nivel 3).
9. Durante 8 semanas, mensajería envía una recomendación semanal aprobada.

La forma exacta de llamar al agente de OpenClaw desde la API (línea de comandos, interfaz del gateway o webhook) se define en la prueba de concepto de la Fase 4.

# **10.3 — Contrato: resultado normalizado**

```json
{
  "orden": "LCD-2026-100124",
  "biomarcador_id": "ferritin",
  "nombre_original": "Ferritina",
  "seccion_original": "METABOLISMO DEL HIERRO",
  "valor_original": "7",
  "unidad_original": "ng/mL",
  "valor": 7.0,
  "unidad": "ng/mL",
  "operador": "=",
  "intervalo_lab": {"bajo": 13, "alto": 150, "texto": "13 – 150"},
  "indicador_lab": "L",
  "metodo": "Quimioluminiscencia",
  "estado": "medido",
  "clase": "bajo",
  "es_refleja": false,
  "activada_por": null,
  "dudas": []
}
```

Valores permitidos: `operador` en {"=", "<", ">"}; `estado` en {"medido", "menor_que_limite", "mayor_que_limite", "cualitativo", "invalido", "no_medido"}; `clase` en {"no_interpretable", "critico", "bajo", "limitrofe", "en_rango", "alto", null}.

# **10.4 — Contrato: hallazgo**

```json
{
  "hallazgo_id": "H-100124-03",
  "tipo": "condicion",
  "referencia": "COND-M3-HE-002",
  "nombre": "Anemia por déficit de hierro",
  "modulo": "M3",
  "criterios_cumplidos": ["hemoglobina:bajo", "ferritina:bajo", "saturacion_transferrina:bajo", "rdw:alto"],
  "datos_faltantes": [],
  "confusores_aplicados": [],
  "coincidencia": "alta",
  "escalamiento": 2,
  "nivel_lenguaje": "condicion_requiere_evaluacion",
  "guias": ["OMS 2024, cortes de hemoglobina", "Lote 3"],
  "recomendaciones": ["REC-ALI-021", "REC-TER-003"]
}
```

# **10.5 — Contrato: informe**

```json
{
  "informe_id": "INF-100124-v1",
  "paciente_ref": "P-8F3A21",
  "objetivo": {"principal": "energia_sueno", "secundario": null},
  "wearable": {"activo": false},
  "paciente": {
    "resumen": "…",
    "lo_que_esta_bien": ["…"],
    "lo_que_merece_atencion": [{"hallazgo_id": "H-100124-03", "texto": "…"}],
    "que_podria_significar": ["…"],
    "que_puedes_hacer": [{"recomendacion_id": "REC-ALI-021", "texto": "…"}],
    "cuando_consultar": [{"escalamiento": 2, "texto": "…"}]
  },
  "medico": {
    "hallazgos": ["H-100124-01", "H-100124-02", "H-100124-03"],
    "reflejas": ["free_t4", "free_t3", "anti_tpo", "reticulocytes_pct", "iga", "anti_ttg_iga", "methylmalonic_acid"],
    "conflictos_entre_guias": ["…"],
    "datos_faltantes": ["potasio: muestra hemolizada", "vitamina C: muestra no apta"],
    "que_conviene_confirmar": ["…"],
    "preguntas_para_el_profesional": ["…"]
  },
  "edad_biologica": {"phenoage": null, "motivo": "…"},
  "estado": "en_revision",
  "version_kb": "2026.10.06",
  "version_modelo": "deepseek/deepseek-v4-pro"
}
```

`paciente_ref` es el identificador seudonimizado; el nombre nunca viaja al agente.

# **10.6 — Interfaz de la API (propuesta)**

| Método | Ruta | Uso | Rol |
| :---- | :---- | :---- | :---- |
| POST | /visitas | Crear visita con formulario de la enfermera | Enfermera |
| POST | /ordenes/{orden}/pdf | Cargar PDF | Operaciones |
| GET | /ordenes/{orden}/estado | Estado de procesamiento | Operaciones |
| GET | /informes/{id} | Ver informe | Paciente, médico |
| POST | /informes/{id}/aprobacion | Aprobar o corregir | Médico |
| GET | /pacientes/{id}/resultados | Catálogo completo con clases | Paciente, médico |
| PUT | /pacientes/{id}/objetivo | Cambiar objetivo | Paciente |
| POST | /pacientes/{id}/wearable/lecturas | Subir lecturas de Apple Health | App iOS |
| DELETE | /pacientes/{id}/wearable | Desconectar | Paciente |
| POST | /mensajes/{id}/aprobacion | Aprobar mensaje de WhatsApp | Médico |
| POST | /acceso/enlace | Enviar enlace y código por WhatsApp | Sistema |

Todas las rutas exigen autenticación, revisan el rol y quedan en auditoría.

# **10.7 — Estructura del repositorio de conocimiento**

```
knowledge-base/
  biomarcadores/        # 133 fichas, una por biomarcador
  condiciones/M1 … M6/  # 50 incluidas y 26 de apoyo
  relaciones/           # patrones y vigilar entre módulos
  reglas/               # vitaminas, objetivos, confusores, wearables, seguridad
  recomendaciones/      # catálogo de recomendaciones
  sinonimos.yaml        # nombres del laboratorio → identificador interno
  unidades.yaml         # conversiones permitidas
  frases_prohibidas.yaml
  casos/                # casos de prueba firmados, con resultado esperado
  00_INDEX.md
```

# **10.8 — Requisitos no funcionales**

- Seguridad y privacidad según el documento 05.
- Tiempo de procesamiento de un PDF hasta el informe en revisión: propuesta, menos de 10 minutos.
- Disponibilidad del dashboard en horario hábil durante el piloto.
- Todo cambio de reglas o de modelo corre el set de casos antes de desplegarse.
- Registros de auditoría inmutables.

# **10.9 — Criterios de aceptación de la versión 1**

| Área | Criterio |
| :---- | :---- |
| Ingesta | Los dos PDF de ejemplo se extraen sin errores; el potasio hemolizado y la vitamina C no apta salen como "inválido" |
| Identidad | Un PDF con documento u orden que no coincide no se procesa |
| Cálculos | La TFG estimada calculada coincide con la del PDF (96 y 112) y cada derivado guarda su origen |
| Clasificación | Las vitaminas sin intervalo salen sin clase; "< 3" sale como menor que el límite |
| Patrones caso 1 | Prediabetes con coincidencia alta, dislipidemia aterogénica, hipertrigliceridemia a confirmar, resistencia a la insulina como apoyo (HOMA-IR 5,5), patrón hepático metabólico, albuminuria a confirmar, ácido úrico alto, hs-CRP alta como apoyo, H. pylori positivo, vitamina D baja y anti-HBs no protector. Síndrome metabólico queda incompleto hasta tener presión y cintura de la enfermera |
| Patrones caso 2 | Anemia por déficit de hierro, hipotiroidismo subclínico con autoinmunidad, Lp(a) elevada, vitamina D baja, ANA 1:160 para consulta, B12 sin déficit funcional (ácido metilmalónico normal) y sin señal de celiaquía (anti-tTG negativo con IgA normal) |
| Seguridad | Ninguna frase prohibida; ningún hallazgo sin regla; ninguna dosis |
| Informe | Seis partes completas y vista médica con datos faltantes |
| Mensajes | Plantillas aprobadas por Meta; nada sale sin aprobación médica en el piloto |
| Apple Health | La app lee pasos, sueño, frecuencia en reposo y presión registrada; desconectar detiene el uso |
| Casos | Cero errores en casos críticos y de escalamiento 3 |

Los patrones esperados de los casos 1 y 2 son la propuesta inicial; el médico los confirma al firmar los casos.
