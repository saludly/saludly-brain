## COND-M1-CA-003 · Hipertrigliceridemia

**Qué detecta.** Triglicéridos en ayunas mayores o iguales a 150 mg/dL. Desde 500 mg/dL sube el escalamiento; desde 1.000 mg/dL la guía añade la prevención de pancreatitis. La urgencia solo sale de una bandera crítica del laboratorio o de síntomas.

```yaml
id: COND-M1-CA-003
nombre: Hipertrigliceridemia
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: tg_alto
    biomarcador: triglycerides
    condicion: ">= 150"
    unidad: mg/dL
  - id: tg_muy_alto
    biomarcador: triglycerides
    condicion: ">= 500"
    unidad: mg/dL
  - id: tg_severo
    biomarcador: triglycerides
    condicion: ">= 1000"
    unidad: mg/dL
regla_central: "tg_alto"
contexto_obligatorio: ["ayuno_horas >= 8"]
excluye_si: []
coincidencia:
  alta: "tg_alto AND ayuno confirmado AND NOT alcohol_48h"
  moderada: "tg_alto AND (alcohol_48h OR dato de alcohol faltante)"
escalamiento:
  base: 1
  si_tg_muy_alto: 2
  si_bandera_critica_laboratorio: 3
nivel_lenguaje: riesgo_potencial
confusores: ["ayuno_insuficiente (no interpretable)", "alcohol_48h", "diabetes descontrolada", "corticoides"]
guias: ["ACC/AHA 2026, manejo de dislipidemia"]
por_verificar: "Una sola medición no demuestra persistencia; el texto lo dice y sugiere repetir."
frase_permitida: "Tus triglicéridos están por encima del rango deseable en esta medición. Conviene repetirlos y revisar alimentación y alcohol."
frase_permitida_tg_severo: "Tus triglicéridos están muy altos. Las guías piden atención médica en este nivel para prevenir complicaciones como la inflamación del páncreas."
frases_prohibidas: ["tienes pancreatitis", "tienes enfermedad cardiovascular"]
recomendaciones_sugeridas: ["reducir azúcar, harinas refinadas y alcohol", "actividad física regular", "repetir la medición"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Triglicéridos 238, ayuno 11 h | Activa, coincidencia alta, escalamiento 1 |
| Muy alto | Triglicéridos 620, ayuno 10 h | Activa, escalamiento 2 |
| Severo | Triglicéridos 1.150 | Activa, escalamiento 2, frase de triglicéridos severos |
| Sin ayuno | Triglicéridos 260, ayuno 4 h | No interpretable; no activa |
| Negativo · PDF mujer 34 años | Triglicéridos 98 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
