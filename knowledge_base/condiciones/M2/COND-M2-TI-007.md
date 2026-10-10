## COND-M2-TI-007 · Hiperparatiroidismo primario

**Qué detecta.** Calcio corregido por albúmina alto con PTH alta o inapropiadamente normal (no suprimida). La guía pide confirmarlo en dos ocasiones separadas por 2 semanas o más; con una toma queda "a confirmar". La PTH es refleja: el laboratorio la corre si el calcio corregido sale alto.

```yaml
id: COND-M2-TI-007
nombre: Hiperparatiroidismo primario
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
calculo: "calcio corregido = calcio total + 0,8 x (4,0 - albúmina en g/dL)"
criterios:
  - id: calcio_alto
    condicion: "calcio corregido > límite superior del laboratorio"
  - id: pth_no_suprimida
    biomarcador: pth
    condicion: "> mitad del intervalo del laboratorio, o alta"
  - id: calcio_muy_alto
    condicion: "calcio corregido >= 12"
    unidad: mg/dL
regla_central: "calcio_alto AND pth_no_suprimida"
coincidencia:
  alta: "regla_central confirmada en dos ocasiones separadas 2 semanas o más"
  moderada: "regla_central en una sola toma"
escalamiento:
  base: 2
  si_calcio_muy_alto: 3
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["tiazidas", "litio", "suplementos de calcio o vitamina D en dosis altas", "deshidratación", "TFG < 60 (orienta a causa renal secundaria)"]
guias: ["Quinto Taller Internacional de hiperparatiroidismo primario 2022"]
por_verificar: "Definición operativa de PTH 'inapropiadamente normal' (mitad superior del intervalo) y el corte de 12 mg/dL para escalamiento 3."
frase_permitida: "Tu calcio está alto y la hormona que lo regula (PTH) no bajó como se esperaría. Ese patrón merece confirmarse y revisarse con tu médico en las próximas semanas."
frases_prohibidas: ["tienes un tumor en la paratiroides", "necesitas cirugía"]
recomendaciones_sugeridas: ["repetir calcio y PTH", "hidratación adecuada", "no tomar suplementos de calcio o vitamina D sin indicación mientras se aclara"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Calcio 10,9, albúmina 4,2 (corregido 10,7), PTH 78 (15 a 65) | Activa, coincidencia moderada, escalamiento 2 |
| Muy alto | Calcio corregido 12,4, PTH 140 | Activa, escalamiento 3 |
| Corregido normal | Calcio 10,4, albúmina 4,9 (corregido 9,7) | No activa; no se pide PTH |
| PTH suprimida | Calcio corregido 11,0, PTH 8 | No activa; vista médica: buscar otra causa de calcio alto |
| Negativo · PDF ejemplos | Calcio 9,5 y 9,2 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
