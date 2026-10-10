## COND-M3-HE-005 · Plaquetas bajas

**Qué detecta.** Plaquetas menores de 100 × 10³/µL, el corte del consenso internacional. Antes de escalar se descarta la pseudotrombocitopenia (agrupación de plaquetas en el tubo, que el laboratorio suele comentar) y se repite. Entre 100 y el límite inferior del laboratorio se muestra como valor fuera de rango.

```yaml
id: COND-M3-HE-005
nombre: Plaquetas bajas
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: plaquetas_bajas
    biomarcador: platelets
    condicion: "< 100"
    unidad: x10³/µL
  - id: plaquetas_leves
    biomarcador: platelets
    condicion: "100 a límite inferior del laboratorio"
regla_central: "plaquetas_bajas"
no_interpretable_si: ["comentario del laboratorio de agregados plaquetarios o coágulo en la muestra"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con infección reciente, alcohol o medicamentos que bajan plaquetas"
escalamiento:
  plaquetas_leves: 1
  plaquetas_bajas: 2
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
confusores: ["infección viral reciente", "alcohol", "heparina y otros medicamentos", "embarazo", "hígado (relación con FIB-4 en M4)"]
guias: ["Consenso internacional de PTI 2019"]
frase_permitida: "Tus plaquetas, las células que ayudan a coagular la sangre, están más bajas de lo esperado. Hay causas pasajeras; conviene repetir el examen y revisarlo con tu médico. Si tienes sangrados o moretones sin golpes, consulta antes."
frases_prohibidas: ["tienes púrpura", "tienes leucemia", "tienes una enfermedad autoinmune"]
recomendaciones_sugeridas: ["repetir hemograma", "evitar antiinflamatorios y aspirina sin indicación mientras se aclara"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Plaquetas 82 | Activa, escalamiento 2; repetir |
| Leve | Plaquetas 128 (laboratorio 150 a 450) | Valor fuera de rango, escalamiento 1 |
| Seudotrombocitopenia | Plaquetas 64 con comentario de agregados | No interpretable; repetir con citrato |
| Crítico | Plaquetas 14 con bandera crítica | Escalamiento 3 |
| Negativo · PDF ejemplos | Plaquetas 265 y 330 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
