## COND-M3-NU-A02 · PTH alta con calcio normal (apoyo)

**Qué detecta.** PTH alta con calcio corregido normal. Antes de pensar en hiperparatiroidismo normocalcémico se descartan causas secundarias: vitamina D baja y TFG baja. Con la regla refleja actual (PTH solo cuando el calcio corregido sale alto), esta ficha solo se activa si el médico pide PTH o si el panel cambia.

```yaml
id: COND-M3-NU-A02
nombre: PTH alta con calcio normal
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D3
criterios:
  - id: pth_alta
    biomarcador: pth
    condicion: "> límite superior del laboratorio"
  - id: calcio_normal
    condicion: "calcio corregido dentro del intervalo"
  - id: secundaria
    condicion: "vitamin_d < 20 ng/mL OR egfr < 60 OR tiazidas OR litio"
regla_central: "pth_alta AND calcio_normal"
efecto: "Si secundaria: vigilar, con la causa probable en la vista médica. Si no: resultado observado para el médico (posible hiperparatiroidismo normocalcémico), escalamiento 1."
escalamiento: 1
relacion: "vitamina D baja + PTH alta + calcio o fósforo alterados (patrón, documento 03)"
guias: ["Quinto Taller Internacional de hiperparatiroidismo primario 2022"]
por_verificar: "Corte de vitamina D de 20 ng/mL para considerar causa secundaria."
frase_permitida_medico: "PTH alta con calcio corregido normal; {causa secundaria probable | sin causa secundaria evidente}."
frases_prohibidas: ["tienes hiperparatiroidismo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Secundaria | PTH 88, calcio corregido 9,4, vitamina D 14 | Vigilar; causa probable: vitamina D baja |
| Sin causa | PTH 82, calcio 9,8, vitamina D 34, TFG 95 | Resultado observado para el médico, escalamiento 1 |
| No aplica · PDF ejemplos | PTH no medida (calcio normal) | No aplica |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
