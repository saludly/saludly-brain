## COND-M3-NU-A03 · Vitamina D baja (apoyo)

**Qué detecta.** 25-OH vitamina D por debajo del intervalo del laboratorio. Por la regla de vitaminas aprobada, se marca como baja y genera recomendaciones alimentarias y de sol, sin dosis. No se etiqueta como deficiencia, porque la Endocrine Society 2024 no fija un nivel de suficiencia ni respalda medirla de rutina; el texto de la recomendación lo aprueba el médico.

```yaml
id: COND-M3-NU-A03
nombre: Vitamina D baja
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D1
criterios:
  - id: vitd_baja
    biomarcador: vitamin_d
    condicion: "< límite inferior del laboratorio"
  - id: vitd_alta
    biomarcador: vitamin_d
    condicion: "> límite superior del laboratorio"
regla_central: "vitd_baja"
escalamiento:
  vitd_baja: 0
  vitd_alta: 1
efecto: "Recomendación alimentaria y de sol. Participa en relaciones: con PTH alta y calcio o fósforo alterados (patrón); con hs-CRP alta o con ferritina o hemoglobina bajas (vigilar)."
modulo_reglas: "regla de vitaminas, documento 07"
guias: ["Endocrine Society 2024"]
por_verificar: "Texto de recomendación sujeto a aprobación médica; ¿mencionar suplemento general o solo alimentos y sol?"
frase_permitida: "Tu vitamina D está por debajo del rango del laboratorio. Puedes mejorarla con alimentos como pescados grasos, huevo y lácteos fortificados, y con exposición prudente al sol. Si quieres suplementarla, consúltalo con tu médico."
frase_alta: "Tu vitamina D está por encima del rango. Si tomas suplementos, coméntalo con tu médico."
frases_prohibidas: ["tienes deficiencia de vitamina D", "toma 2.000 UI", "toma vitamina D3"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Baja · PDF hombre 46 años | Vitamina D 21,4 (laboratorio 30 a 100) | Marcada baja, escalamiento 0, recomendación alimentaria |
| Baja · PDF mujer 34 años | Vitamina D 17,8 | Marcada baja; relación vigilar con ferritina y hemoglobina bajas |
| Alta | Vitamina D 140 | Marcada alta, escalamiento 1 |
| En rango | Vitamina D 42 | Sin recomendación específica |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
