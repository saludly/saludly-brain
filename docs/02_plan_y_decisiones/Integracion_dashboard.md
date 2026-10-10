# Integración del informe con el dashboard

**10 de octubre de 2026.** Revisión del borrador https://github.com/saludly/saludly-dashboard (Lovable, TanStack Start, último commit "Eliminó paso de correo"). Es un primer borrador que funciona; la experiencia de usuario cambiará. Este documento dice qué campo del informe alimenta cada pantalla y dónde choca el borrador con las reglas de Saludly. No se tocó el repositorio del dashboard.

**Contrato:** `codigo/pipeline/contrato/informe.ts` (tipos TypeScript, listos para copiar) y los ejemplos `codigo/pipeline/ejemplos/INF-*.json`.

## Qué hay hoy en el dashboard

| Pantalla | Archivo | Datos que usa |
|---|---|---|
| Inicio y recorrido | `src/routes/index.tsx` | `healthIndicators`, `overallHealthScore` y un recorrido de 3 pasos (agua, nutrición semanal, vitaminas con productos) |
| Panel de biomarcadores | `src/routes/panel.tsx` y `components/saludly/*` | `src/data/biomarkers.ts`: datos inventados (en inglés) con `status: optimal | attention | critical` y `low/high` numéricos |
| Protocolo | `src/routes/protocolo.tsx` | Textos fijos: "Bebe 2.5 L", plan semanal fijo, suplementos con producto y precio |
| Productos | `src/routes/productos.tsx` | Marketplace de suplementos, sueros, masajes y pruebas, con carrito |

## Cómo se conecta

| Lo que muestra el dashboard | Campo del informe |
|---|---|
| Biomarcadores (panel, figura del cuerpo, tarjetas) | `resultados[]`: `nombre`, `valor`, `unidad`, `intervalo` (texto del laboratorio), `clase`. El estado visual sale de `clase`: `en_rango` → en rango; `bajo`, `alto` o `limitrofe` → fuera de rango; `critico` → solo con bandera del laboratorio; `no_interpretable` → gris, con `motivo` |
| Ficha corta de cada biomarcador ("about") | Sale de la Knowledge Base (fichas de biomarcador). Se puede exportar a JSON cuando se necesite |
| Inicio: resumen | `paciente.resumen` y `objetivos` |
| Lo que está bien / lo que merece atención | `paciente.lo_que_esta_bien`, `paciente.lo_que_merece_atencion` (con `por_que` usando sus valores y `ejemplo`) |
| Qué podría significar / cuándo consultar | `paciente.que_podria_significar`, `paciente.cuando_consultar` |
| Protocolo: hidratación, nutrición, vitaminas y estilo de vida | `paciente.que_puedes_hacer` agrupado por `tipo` (hidratacion, alimentacion, vitaminas_suplementos, sueno, actividad, habitos, terapias, controles) |
| Nutrición semanal | `nutricion.meta_diaria` y `nutricion.plan` (7 recetas, una por día); el texto completo de cada receta está en `whatsapp.recetas_diarias` |
| Edad biológica | `edad_biologica`, en pantalla aparte |
| Mi objetivo | `objetivos` (3 de 10) y `perfil.nivel_actividad` |
| Estado del informe | Si `estado` es `retenido_hasta_llamada`, el dashboard no muestra el informe y dice que el equipo médico llamará |

## Lo que choca con las reglas de Saludly (cambiar en el dashboard)

1. **"Óptimo" y "crítico".** El borrador marca como "critical" valores apenas fuera de rango (por ejemplo, un cortisol de 22,4) y como "optimal" los que están en rango. Saludly no usa rangos óptimos sin fuente y reserva "crítico" para la bandera del laboratorio o un umbral de guía. Propuesta: **En rango · Fuera de rango · Requiere atención pronta**, y usar el `escalamiento` del hallazgo para el color de alerta.
2. **Puntaje general de salud** (`overallHealthScore`). El motor no produce un puntaje y no hay un modelo validado detrás. Si se quiere mantener, debe calcularse solo con las clases (por ejemplo, porcentaje de resultados en rango por sistema) y decir que es un resumen, no una medida de salud.
3. **"Bebe 2,5 L de agua" fijo.** Con enfermedad renal, sodio bajo o insuficiencia cardíaca, la hidratación es "sigue la indicación de tu médico". El texto debe salir de `que_puedes_hacer` (tipo `hidratacion`), que ya respeta esas contraindicaciones.
4. **Suplementos con producto y precio en el protocolo** (vitamina D3, magnesio, omega-3). Choca con dos decisiones: (a) los suplementos solo como opción general para hablar con el médico, sin dosis ni marcas (documentos 05 y 07); (b) los complementos pagados están aplazados. Además, el omega-3 salió del panel base. Mientras tanto, el marketplace no debería aparecer al lado de una recomendación clínica.
5. **Datos de ejemplo escritos en inglés y traducidos al mostrarlos, con biomarcadores que no están en el panel** (T3 reversa, leptina, etc.). Se reemplazan por `resultados[]`, que ya trae los nombres en español del índice.
6. **Rangos numéricos `low/high`.** El informe trae el intervalo como texto del laboratorio (a veces es "< 5" o por fase del ciclo). Para la barra de rango se pueden añadir `bajo` y `alto` numéricos si el dashboard los necesita (están en el motor).

## Siguiente paso sugerido

Copiar `informe.ts` y uno de los ejemplos al dashboard, reemplazar `src/data/biomarkers.ts` por un cargador del informe y conectar las pantallas según la tabla de arriba. El repositorio está conectado a Lovable: cada cambio en `main` aparece en el editor, así que conviene trabajarlo en una rama.
