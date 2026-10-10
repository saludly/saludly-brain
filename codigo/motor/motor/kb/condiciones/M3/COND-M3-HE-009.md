## COND-M3-HE-009 · Glóbulos rojos grandes sin anemia (macrocitosis)

**Qué detecta.** VCM mayor de 100 fL sin anemia. El patrón busca la explicación entre módulos: alcohol (GGT alta o consumo declarado), déficit de B12 o folato, tiroides (TSH alta), hígado y medicamentos (metformina, metotrexato, hidroxiurea, anticonvulsivantes). Con anemia, manda COND-M3-HE-004.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M3-HE-009
nombre: Glóbulos rojos grandes sin anemia (macrocitosis)
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: macrocitosis
    biomarcador: mcv
    condicion: "> 100"
    unidad: fL
  - id: sin_anemia
    biomarcador: hemoglobin
    condicion: "COND-M3-HE-001 no activa"
  - id: explicacion
    biomarcador: ggt
    condicion: "GGT alta o alcohol declarado; B12 o folato bajos; TSH alta; ALT o AST altas; medicamento que la explica"
regla_central: "macrocitosis AND sin_anemia"
excluye_si: ["COND-M3-HE-001 activa (manda HE-004)"]
coincidencia:
  alta: "macrocitosis con al menos una explicación"
  moderada: "macrocitosis sin explicación en el panel"
escalamiento: 1
nivel_lenguaje: patron_compatible
confusores: ["reticulocitos altos", "hipotiroidismo", "embarazo"]
guias: ["BSH, evaluación de la macrocitosis"]
frase_permitida: "Tus glóbulos rojos son más grandes de lo normal, aunque no tienes anemia. Puede tener que ver con el alcohol, la vitamina B12 o la tiroides; conviene revisarlo con tu médico."
frases_prohibidas: ["tienes alcoholismo", "tienes leucemia", "tienes mielodisplasia"]
recomendaciones_sugeridas: ["reducir el alcohol si lo consumes", "repetir hemograma con B12 y folato"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Con alcohol | VCM 104, GGT 140, Hb normal | Activa, alta; explicación: alcohol |
| Sin explicación | VCM 103, todo lo demás normal | Activa, moderada |
| Con anemia | VCM 108, Hb 10,5 | No aplica (manda HE-004) |
| Negativo · PDF ejemplos | VCM normal | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
