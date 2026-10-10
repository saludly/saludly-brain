## COND-M2-NE-004 · Potasio alto

**Qué detecta.** Potasio por encima del intervalo del laboratorio. Desde 5,5 mmol/L KDIGO plantea acciones. En toma domiciliaria el riesgo de falso alto es grande (hemólisis, puño apretado, demora en separar el plasma), así que nunca se escala con un valor aislado: se repite primero, salvo bandera crítica del laboratorio.

```yaml
id: COND-M2-NE-004
nombre: Potasio alto
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: k_alto
    biomarcador: potassium
    condicion: "> límite superior del laboratorio"
    unidad: mmol/L
  - id: k_accion
    biomarcador: potassium
    condicion: ">= 5.5"
    unidad: mmol/L
  - id: muestra_confiable
    condicion: "sin hemólisis AND plasma separado en menos de 30 minutos (centrífuga en domicilio)"
regla_central: "k_alto AND muestra_confiable"
no_interpretable_si: ["hemólisis reportada", "resultado no procesado", "sin registro de centrifugado a tiempo"]
coincidencia:
  alta: "k_accion AND muestra_confiable AND (TFG < 60 OR medicamento que retiene potasio)"
  moderada: "k_alto AND muestra_confiable"
escalamiento:
  k_alto_menor_5_5: 1
  k_accion: 2
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
confusores: ["hemólisis", "demora en separar el plasma", "puño apretado durante la toma", "leucocitos o plaquetas muy altos", "IECA, ARA II, espironolactona, suplementos de potasio"]
guias: ["KDIGO 2024"]
reglas_especiales: ["nunca pedir suspender medicamentos desde la app"]
frase_permitida: "Tu potasio salió por encima del rango. Muchas veces es un efecto de la toma de la muestra, así que lo vamos a repetir antes de sacar conclusiones."
frases_prohibidas: ["tienes hiperpotasemia", "suspende tu medicamento", "riesgo de arritmia (sin bandera crítica del laboratorio)"]
recomendaciones_sugeridas: ["repetir el potasio", "no tomar suplementos de potasio sin indicación"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| No interpretable · PDF mujer 34 años | Potasio "No procesado", muestra hemolizada | No interpretable; pide nueva muestra; no activa |
| Leve | Potasio 5,3, centrifugado a tiempo | Activa, coincidencia moderada, escalamiento 1; repetir |
| Accionable | Potasio 5,8, sin hemólisis, TFG 48, toma losartán | Activa, coincidencia alta, escalamiento 2 |
| Crítico | Potasio 6,6 con bandera crítica del laboratorio | Escalamiento 3 |
| Negativo · PDF hombre 46 años | Potasio 4,3 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
