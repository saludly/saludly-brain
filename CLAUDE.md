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
5. **Datos de pacientes:** solo datos sintéticos. Hacia un LLM externo, seudonimizar: edad, sexo, valores y contexto; nunca nombre ni documento.
6. **No toques `_archivo/`.** Es histórico.

## Estructura

```
README.md · CLAUDE.md
docs/                    documentación (no la lee el código); ver docs/README.md
knowledge_base/          fuente de verdad clínica, legible por máquina
  00_INDEX.md / .json    índice generado (sinónimos, unidades, qué alimenta cada biomarcador)
  biomarcadores/*.md     133 fichas, encabezado YAML (biomarker_id, sinonimos, unidad_canonica, alimenta…)
  condiciones/M1..M6/    76 fichas COND-Mx-XX-NNN (incluidas) y COND-…-ANN (apoyo), con bloque ```yaml
  relaciones/REL-*.md    27 relaciones entre módulos (tipo: patron | vigilar | fuera_de_patrones)
  seguridad/SEG-*.md     15 reglas de seguridad
  casos/                 casos de prueba: unitarios (json/yaml/csv) y de punta a punta (e2e/E2E-01 hombre, E2E-02 mujer)
codigo/
  requirements.txt       pdfplumber, pyyaml (reportlab solo para el generador de PDF)
  motor/                 motor de análisis completo (Fase 4)
    motor/motor.py       analizar(lectura, contexto) = flujo completo
    motor/lector.py      copia del lector del PDF
    motor/calculos.py    21 cálculos con trazabilidad
    motor/clasificacion.py + reglas_parte1.yaml   clasificación, limítrofes, críticos, altitud
    motor/condiciones_m1m2.py   34 evaluadores · condiciones_m3m6.py: 42 evaluadores
    motor/relaciones_seguridad.py   relaciones, seguridad y ensamblar()
    motor/score2.py      SCORE2 recalibrado para Colombia (PURE)
    motor/kb/            COPIA de knowledge_base/{condiciones,relaciones,seguridad}
    pruebas/             probar_parte1..4.py, probar_todo.py, PDF, E2E y 00_INDEX.json (copias)
  lector_pdf/            lector como módulo independiente (Fase 3), con sus propias pruebas
pdf_ejemplo/             2 PDF sintéticos (órdenes LCD-2026-100123 y LCD-2026-100124) y generar_pdf_ejemplo.py
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
cd codigo/motor && python pruebas/probar_todo.py       # esperado: TOTAL: 508 de 508
cd codigo/lector_pdf && python pruebas/probar.py        # la prueba del PDF mezclado necesita qpdf instalado
```

- Antes y después de cambiar código del motor, corre `probar_todo.py`. No se acepta ninguna regresión.
- Las pruebas reescriben `pruebas/salida_*.json`. En Windows cambian los saltos de línea aunque el contenido sea igual.

## Deuda técnica conocida

- **Copias de la Knowledge Base.** `codigo/motor/motor/kb/`, `codigo/motor/pruebas/00_INDEX.json` y `pruebas/E2E-*.json` son copias de `knowledge_base/`. Hoy están sincronizadas. Si cambias una, sincroniza la otra; conviene que el motor lea directo de `knowledge_base/`.
- **El lector está duplicado** en `codigo/motor/motor/lector.py` y `codigo/lector_pdf/lector.py`, que hoy son idénticos.
- **Rutas fijas.** `pdf_ejemplo/generar_pdf_ejemplo.py` escribe en `/home/claude/saludly/`; hay que cambiarlo antes de usarlo.
- **Sin control de versiones.** El proyecto todavía no usa git.
- **El lector está hecho para el PDF de ejemplo.** Cuando llegue el formato real del laboratorio, hay que ajustar sus constantes de formato y repetir las pruebas.

## Estado y siguientes pasos

Las Fases 0, 1, 3 y 4 están hechas en versión 1. La siguiente es la **Fase 2**: OpenClaw en un VPS de Hostinger con DeepSeek (`deepseek-v4-pro`; `deepseek-chat` y `deepseek-reasoner` se retiraron el 24 de julio de 2026) y embeddings locales. Después vienen la Fase 5 (redacción del informe con control de salida), la Fase 6 (dashboard, formulario de la enfermera y app iOS mínima) y la Fase 7 (WhatsApp Business Platform).

Pendientes externos: la firma del médico, el PDF real del laboratorio, el formulario de la visita de la enfermera y la consulta legal sobre el INVIMA. El detalle está en `docs/02_plan_y_decisiones/Saludly_Plan_de_implementacion.md`.
