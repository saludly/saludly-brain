## COND-M5-MU-002 · FSH alta en menores de 40 años

**Qué detecta.** FSH alta en una mujer menor de 40 años, posible señal de insuficiencia ovárica prematura. Se repite en 4 a 6 semanas con el médico. Entre 40 y 45 años es solo contexto; desde los 45 la FSH no se usa para diagnosticar menopausia (NICE).

```yaml
id: COND-M5-MU-002
nombre: FSH alta en menores de 40 años
modulo: M5
especialidad: salud_de_la_mujer
tipo: incluida
detectabilidad: D3
criterios:
  - id: fsh_alta
    biomarcador: fsh
    condicion: "> 25"
    unidad: UI/L (mUI/mL)
  - id: edad
    condicion: "< 40"
regla_central: "sexo == mujer AND edad AND fsh_alta"
no_interpretable_si: ["anticonceptivo hormonal", "embarazo", "sin fecha de última menstruación"]
lectura_por_edad:
  "40 a 44": "contexto en la vista médica, sin condición"
  "45 o más": "no se interpreta para menopausia"
coincidencia:
  alta: "regla_central confirmada en una segunda medición a 4-6 semanas"
  moderada: "regla_central en una sola medición"
escalamiento: 2
nivel_lenguaje: patron_compatible
guias: ["NICE NG23, menopausia"]
por_verificar: "El corte de 25 UI/L viene de los criterios de insuficiencia ovárica prematura de ESHRE, no citados en el Lote 5; confirmar fuente antes de la firma."
frase_permitida: "Tu FSH, una hormona que regula los ovarios, salió más alta de lo esperado para tu edad. Hay que repetirla en unas semanas; coméntalo con tu médico, sobre todo si tus ciclos han cambiado o estás pensando en un embarazo."
frases_prohibidas: ["estás entrando en la menopausia", "no vas a poder tener hijos", "tienes falla ovárica"]
recomendaciones_sugeridas: ["consulta médica", "repetir FSH en 4 a 6 semanas"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Mujer 33 años, FSH 38, sin anticonceptivo | Activa, coincidencia moderada, escalamiento 2 |
| Edad 42 | FSH 30 | Sin condición; contexto en la vista médica |
| Edad 50 | FSH 60 | No se interpreta |
| Anticonceptivo | Mujer 30 años, FSH 2, anticonceptivo oral | No interpretable |
| Negativo · PDF mujer 34 años | FSH 6,1 en fase folicular | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
