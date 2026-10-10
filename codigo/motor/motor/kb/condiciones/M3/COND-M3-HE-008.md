## COND-M3-HE-008 · Plaquetas altas (trombocitosis)

**Qué detecta.** Plaquetas mayores de 450 × 10³/µL. La gran mayoría son reactivas: déficit de hierro, inflamación o infección recientes. Más de 1.000 × 10³/µL es trombocitosis extrema y se revisa pronto.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M3-HE-008
nombre: Plaquetas altas (trombocitosis)
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: plaquetas_altas
    biomarcador: platelets
    condicion: "> 450"
    unidad: x10³/µL
  - id: plaquetas_extremas
    biomarcador: platelets
    condicion: "> 1000"
    unidad: x10³/µL
  - id: causa_reactiva
    biomarcador: ferritin
    condicion: "ferritina baja (HE-002 o HE-003) o hs-CRP > 5 o infección reciente"
regla_central: "plaquetas_altas"
coincidencia:
  alta: "plaquetas_altas sin causa reactiva"
  moderada: "plaquetas_altas con causa reactiva (probablemente reactiva)"
escalamiento:
  plaquetas_altas: 1
  plaquetas_extremas: 2
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
confusores: ["déficit de hierro", "infección o inflamación reciente", "esplenectomía", "ejercicio intenso"]
guias: ["BSH, investigación de la trombocitosis", "OMS, criterios de trombocitemia esencial"]
por_verificar: "Corte de 1.000 para trombocitosis extrema (BSH)."
frase_permitida: "Tus plaquetas están por encima del rango. Casi siempre es una reacción a algo pasajero, como falta de hierro o una inflamación; conviene repetir el examen y revisarlo con tu médico."
frases_prohibidas: ["tienes trombocitemia", "tienes leucemia", "vas a hacer un trombo"]
recomendaciones_sugeridas: ["repetir hemograma en 4 a 6 semanas", "corregir el hierro si está bajo, con indicación médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Reactiva | Plaquetas 520, ferritina 9 | Activa, moderada, escalamiento 1 |
| Sin causa | Plaquetas 610, ferritina y PCR normales | Activa, alta, escalamiento 1 |
| Extrema | Plaquetas 1.150 | Activa, escalamiento 2 |
| Negativo · PDF ejemplos | Plaquetas 265 y 330 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
