# codigo/rag · Knowledge Base para el RAG en Supabase

Prepara la Knowledge Base para vectorizarla y subirla a Supabase, donde el agente de OpenClaw la consulta.

**El RAG no decide nada clínico.** Los umbrales los evalúa el motor (`codigo/motor`). El RAG solo trae texto para redactar y para responder preguntas abiertas.

## Dos formas de consulta

1. **Por identificador.** Los hallazgos del motor nombran fichas (`COND-M3-HE-002`, `SEG-001`, `ferritin`) y el agente trae ese texto exacto. Es la regla de `knowledge_base/00_INDEX.md`: para redactar se busca por identificador, no por parecido.
2. **Por significado y por palabras (híbrida).** Para preguntas abiertas del médico o de operaciones.

## Fragmentar

```bash
python fragmentar.py            # escribe salida/fragmentos.jsonl (no va a git, se regenera)
```

| Fuente | Cómo se fragmenta |
|---|---|
| `knowledge_base/biomarcadores/` | Por secciones A a N; las pequeñas se unen (150 a 800 tokens). Las "Notas de decisión de Saludly" van solas, con `prioridad: decision_saludly`, porque mandan sobre el resto de la ficha |
| `condiciones/`, `relaciones/`, `seguridad/` | Una ficha, un fragmento; el bloque YAML va también en `metadata` y no se incluye la plantilla de firma |
| `docs/01_serie_saludly_brain/` | Por títulos, tipo `documento_producto` |
| `docs/03_investigacion_clinica/` | Por títulos, tipo `evidencia` |
| No entran | `docs/04_fichas_compiladas` (copias viejas de las fichas), `docs/05` (informes de pruebas), `casos/` (datos de prueba), el plan |

Cada fragmento lleva `huella` (sha256 del contenido) para volver a vectorizar solo lo que cambió, y `version_kb` (versión del índice más el commit de git).

## Pendiente

El esquema de Supabase y la carga de los vectores dependen del modelo de embeddings, que todavía no está decidido.
