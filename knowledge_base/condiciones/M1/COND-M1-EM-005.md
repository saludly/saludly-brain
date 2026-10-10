## COND-M1-EM-005 · Glucosa baja en ayunas

**Qué detecta.** Glucosa menor de 70 mg/dL (alerta) o menor de 54 mg/dL (significativa). En toma domiciliaria puede ser un falso bajo si la muestra no fue en tubo con fluoruro o tardó en procesarse; por eso el motor revisa el tubo y el tiempo antes de escalar.

```yaml
id: COND-M1-EM-005
nombre: Glucosa baja en ayunas
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D3
criterios:
  - id: glucosa_baja
    biomarcador: glucose
    condicion: "< 70"
    unidad: mg/dL
  - id: glucosa_muy_baja
    biomarcador: glucose
    condicion: "< 54"
    unidad: mg/dL
  - id: muestra_confiable
    condicion: "tubo con fluoruro AND tiempo de toma a recepción dentro del límite del protocolo"
  - id: medicamento_de_riesgo
    contexto: medicamentos
    condicion: "insulina OR sulfonilurea"
regla_central: "glucosa_baja"
contexto_obligatorio: ["ayuno_horas declarado"]
excluye_si: []
coincidencia:
  alta: "glucosa_baja AND muestra_confiable"
  moderada: "glucosa_baja AND NOT muestra_confiable (posible falso bajo)"
escalamiento:
  base: 1
  si_medicamento_de_riesgo: 2
  si_glucosa_muy_baja_y_muestra_confiable: 3
  si_glucosa_muy_baja_y_muestra_no_confiable: 2
nivel_lenguaje: resultado_observado
confusores: ["demora en el procesamiento", "tubo sin fluoruro", "ayuno muy prolongado"]
guias: ["Clasificación ADA de hipoglucemia (Standards 2024, tabla 6.4)"]
frase_permitida: "Tu glucosa en ayunas salió más baja de lo esperado. Puede deberse a cómo se procesó la muestra, así que conviene repetirla. Si has tenido mareo, sudor frío o temblor en ayunas, coméntalo con tu médico."
frase_permitida_muy_baja: "Tu glucosa salió muy baja. Nuestro equipo médico te va a llamar hoy."
frases_prohibidas: ["tienes hipoglucemia", "tienes un tumor", "tienes diabetes"]
recomendaciones_sugeridas: ["repetir la medición", "no saltarse comidas mientras se aclara"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Alerta | Glucosa 64, tubo con fluoruro, procesada a tiempo | Activa, coincidencia alta, escalamiento 1 |
| Significativa confiable | Glucosa 50, tubo con fluoruro, a tiempo | Activa, escalamiento 3 |
| Significativa dudosa | Glucosa 50, demora de 7 horas sin fluoruro | Activa, coincidencia moderada, escalamiento 2, pide repetir |
| Con medicamento | Glucosa 66, usa glibenclamida | Activa, escalamiento 2 |
| Negativo | Glucosa 86 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
