## COND-M6-RE-A02 · VSG alta (apoyo)

**Qué detecta.** Velocidad de sedimentación por encima del intervalo del laboratorio. Es una señal inflamatoria inespecífica que se lee siempre junto con la hs-CRP; la anemia, el embarazo y la edad la suben. Aislada, se sugiere repetir, sin asociarla a ninguna enfermedad.

```yaml
id: COND-M6-RE-A02
nombre: VSG alta
modulo: M6
especialidad: reumatologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: vsg_alta
    biomarcador: esr
    condicion: "> límite superior del laboratorio (por sexo y edad)"
    unidad: mm/h
  - id: vsg_muy_alta
    biomarcador: esr
    condicion: ">= 100"
    unidad: mm/h
  - id: hscrp_alta
    biomarcador: hs_crp
    condicion: "> 5"
    unidad: mg/L
regla_central: "vsg_alta"
efecto: "Con hscrp_alta, refuerza la relación de inflamación (vigilar, documento 03). Con anemia (M3), la vista médica anota que la anemia sube la VSG."
escalamiento:
  base: 1
  si_vsg_muy_alta: 2
confusores: ["anemia", "embarazo", "edad avanzada", "infección reciente", "obesidad"]
guias: ["ACR/EULAR 2010 (como reactante de fase aguda solo con sinovitis clínica)"]
por_verificar: "Escalamiento 2 con 100 mm/h o más es propuesta de Saludly."
frase_permitida: "Tu velocidad de sedimentación, una señal general de inflamación, está por encima del rango. Puede subir por muchas causas, incluso pasajeras; conviene repetirla."
frases_prohibidas: ["tienes artritis", "tienes una enfermedad reumática", "tienes cáncer"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Aislada | VSG 28 (hasta 15), hs-CRP 1,2 | Escalamiento 1, repetir |
| Con inflamación | VSG 35, hs-CRP 14 | Refuerza la relación de inflamación |
| Muy alta | VSG 110 | Escalamiento 2 |
| Negativo · PDF ejemplos | VSG 12 y 18 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
