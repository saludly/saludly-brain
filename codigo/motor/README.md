# Motor de análisis · Saludly Brain · Fase 4

## Parte 1: cálculos y clasificación (lista)

    pip install pdfplumber pyyaml
    python pruebas/probar_parte1.py

- `motor/motor.py`: flujo de la parte 1 (`analizar_parte1(lectura, contexto)`).
- `motor/clasificacion.py`: clases de cada resultado y reglas de contexto.
- `motor/calculos.py`: 21 cálculos con trazabilidad.
- `motor/reglas_parte1.yaml`: limítrofes, críticos por guía, bloqueos por contexto y altitud (las reglas son datos).
- `motor/lector.py`: copia del lector del PDF (Fase 3) para las pruebas.
- `pruebas/`: PDF de ejemplo, casos de punta a punta, índice del Knowledge Base, pruebas y salidas.

Contexto mínimo de la visita: edad, sexo, ciudad, ayuno_horas, hora_toma; en mujeres, fecha_ultima_menstruacion,
anticonceptivo_hormonal y embarazo; opcionales: medicamentos, suplementos, tabaquismo, peso_kg, talla_m, cintura_cm,
y `laboratorio.transporte_vitamina_c_validado`.

## Partes siguientes
2. Condiciones M1 y M2 · 3. Condiciones M3 a M6 · 4. Relaciones y seguridad.

## Parte 2: condiciones M1 y M2 (lista)

    python pruebas/probar_parte2.py

- `motor/condiciones_m1m2.py`: 34 evaluadores (`evaluar_m1m2(salida_parte1, contexto)`), con exclusiones entre condiciones.
- `motor/kb/condiciones/`: fichas de condición; de ahí salen nombre, nivel de lenguaje y guías.

- `motor/score2.py`: SCORE2 recalibrado para Colombia (región de riesgo alto × 0,61 hombres / 0,75 mujeres, PURE-Colombia 2025), verificado contra el ejemplo publicado del artículo SCORE2.

## Parte 3: condiciones M3 a M6 (lista)

    python pruebas/probar_parte3.py

- `motor/condiciones_m3m6.py`: 42 evaluadores (`evaluar_m3m6(salida_parte1, contexto, hallazgos_m1m2)`).
- El contexto de la visita puede incluir: alcohol_consumo, sintomas_urinarios, dieta_sin_gluten, dieta_vegana, cirugia_bariatrica,
  perdida_peso_no_intencional, ingesta_reducida, procedencia_endemica, familiar_celiaco, menopausia, lactancia, eyaculacion_48h,
  ciclismo_48h, sintomas_neurologicos y consentimientos.psa.

## Parte 4: relaciones, seguridad y salida final (lista)

    python pruebas/probar_todo.py      # corre las cuatro partes

- `motor/relaciones_seguridad.py`: 27 relaciones, 15 fichas de seguridad y `ensamblar(...)`.
- `motor.analizar(lectura, contexto)`: flujo completo. Devuelve escalamiento_maximo, canal, llamadas, hallazgos_informe (ordenados,
  con patrones agrupados), vista_medica, recordatorios, edad_biologica, calculados, y el detalle de condiciones, relaciones y seguridad.
