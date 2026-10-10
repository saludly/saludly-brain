## COND-M3-HE-006 · Posible sobrecarga de hierro

**Qué detecta.** Saturación de transferrina mayor de 45 % con ferritina mayor de 200 ng/mL en mujeres premenopáusicas, o mayor de 50 % con ferritina mayor de 300 en hombres y mujeres posmenopáusicas (EASL 2022). Confirmar hemocromatosis exige una prueba genética. La ferritina alta sola es una alerta ("vigilar"), porque la inflamación, el alcohol y el hígado graso también la suben.

```yaml
id: COND-M3-HE-006
nombre: Posible sobrecarga de hierro
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: patron_mujer
    condicion: "mujer premenopáusica AND transferrin_saturation > 45 AND ferritin > 200"
  - id: patron_hombre
    condicion: "(hombre OR mujer posmenopáusica) AND transferrin_saturation > 50 AND ferritin > 300"
  - id: ferritina_sola
    condicion: "ferritin > 200 (mujer premenopáusica) o > 300 (resto) con saturación normal"
regla_central: "patron_mujer OR patron_hombre"
contexto_obligatorio: ["ayuno (el hierro sérico varía con la comida)"]
coincidencia:
  alta: "regla_central sin inflamación (hs_crp <= 5) y sin suplementos de hierro"
  moderada: "regla_central con hs_crp > 5, alcohol o patrón hepático metabólico"
  baja: "ferritina_sola (vigilar)"
escalamiento: 2
nivel_lenguaje: patron_compatible
confusores: ["inflamación", "alcohol", "hígado graso (relación hepática del documento 03)", "suplementos de hierro", "transfusiones"]
guias: ["EASL 2022, hemocromatosis", "OMS 2020, ferritina"]
frase_permitida: "Tu hierro y tus reservas de hierro están más altos de lo esperado. Puede deberse a varias causas; conviene revisarlo con tu médico, que puede pedir una prueba genética."
frase_vigilar: "Tu ferritina está alta. Muchas veces se debe a inflamación o al hígado más que a exceso de hierro; lo tenemos en cuenta junto con tus otros resultados."
frases_prohibidas: ["tienes hemocromatosis", "tienes exceso de hierro", "dona sangre"]
recomendaciones_sugeridas: ["no tomar suplementos de hierro ni vitamina C en dosis altas", "reducir alcohol", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Hombre, saturación 62 %, ferritina 640, hs-CRP 1 | Activa, coincidencia alta, escalamiento 2 |
| Vigilar · PDF hombre 46 años | Ferritina 310, saturación 37 %, patrón hepático metabólico | Coincidencia baja (vigilar); la vista médica liga la ferritina al patrón hepático |
| Mujer | Mujer 32 años, saturación 51 %, ferritina 260 | Activa |
| Negativo · PDF mujer 34 años | Ferritina 7 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
