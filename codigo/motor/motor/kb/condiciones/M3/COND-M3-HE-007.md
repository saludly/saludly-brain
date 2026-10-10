## COND-M3-HE-007 · Glóbulos rojos altos (eritrocitosis) ajustados por altitud

**Qué detecta.** Hemoglobina ajustada por la altitud de residencia (la misma resta de la OMS 2024 que usa la anemia) mayor de 16,5 g/dL en hombres o 16,0 g/dL en mujeres. En Bogotá la hemoglobina es más alta por la altura; sin ajustar, casi todos saldrían altos. El tabaquismo, la testosterona (endógena o en suplementos), la deshidratación y la apnea del sueño son las causas más comunes; la policitemia vera es rara.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M3-HE-007
nombre: Glóbulos rojos altos (eritrocitosis) ajustados por altitud
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: hb_alta
    biomarcador: hemoglobin
    condicion: "hemoglobina ajustada por altitud > 16,5 (hombres) o > 16,0 (mujeres)"
    unidad: g/dL
  - id: hct_alto
    biomarcador: hematocrit
    condicion: "> 49 (hombres) o > 48 (mujeres); solo refuerza, porque no se ajusta por altitud"
    unidad: "%"
  - id: hb_muy_alta
    biomarcador: hemoglobin
    condicion: "hemoglobina ajustada > 18,5 (hombres) o > 16,5 (mujeres)"
regla_central: "hb_alta"
contexto_obligatorio: ["ciudad o altitud de residencia", "sexo"]
no_aplica_si: ["embarazo", "menor de 15 años"]
coincidencia:
  alta: "hb_alta con hct_alto y tabaquismo conocido"
  moderada: "hb_alta sola, o con tabaquismo o testosterona alta como causa probable"
escalamiento:
  hb_alta: 1
  hb_muy_alta: 2
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
confusores: ["tabaquismo", "testosterona alta o en suplementos (REL-029)", "deshidratación", "diuréticos", "apnea del sueño", "eritropoyetina"]
guias: ["OMS 2024, cortes de hemoglobina y ajuste por altitud", "BSH 2019, investigación de la eritrocitosis", "OMS 2016, criterios de policitemia vera"]
por_verificar: "Cortes de la OMS 2016 para policitemia vera aplicados a la hemoglobina ajustada; el médico confirma."
frase_permitida: "Tu hemoglobina está más alta de lo esperado, aun teniendo en cuenta la altura de tu ciudad. Lo más común es que se deba al cigarrillo, a hormonas o a poca hidratación; conviene repetir el examen y revisarlo con tu médico."
frases_prohibidas: ["tienes policitemia", "tienes cáncer de la sangre", "tu sangre está espesa"]
recomendaciones_sugeridas: ["hidratación", "dejar de fumar", "repetir hemograma", "consulta si hay dolor de cabeza, mareo o enrojecimiento"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Hombre en Bogotá, Hb 19,0 (ajustada 17,2), Hct 54, no fuma | Activa, alta, escalamiento 1 |
| Muy alta | Hombre en Bogotá, Hb 20,6 (ajustada 18,8) | Activa, escalamiento 2 |
| Fumador | Hombre en Bogotá, Hb 18,6 (ajustada 16,8), fuma | Activa, moderada; tabaquismo como confusor |
| Negativo · PDF ejemplos | Hb 15,9 (hombre) y 11,2 (mujer) | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
