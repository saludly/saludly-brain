## COND-M3-HE-010 · Dos o más líneas de la sangre bajas

**Qué detecta.** Al menos dos de estas tres: anemia ajustada por altitud (HE-001), neutrófilos menores de 1,5 × 10³/µL y plaquetas menores de 150 × 10³/µL. Por separado cada una puede ser pasajera; juntas sugieren un problema de la médula, del bazo o una deficiencia (B12, folato) y siempre se revisan.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M3-HE-010
nombre: Dos o más líneas de la sangre bajas
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: anemia
    biomarcador: hemoglobin
    condicion: "COND-M3-HE-001 activa"
  - id: neutrofilos_bajos
    biomarcador: neutrophils_abs
    condicion: "< 1,5"
    unidad: x10³/µL
  - id: plaquetas_bajas
    biomarcador: platelets
    condicion: "< 150"
    unidad: x10³/µL
regla_central: "al menos 2 de (anemia, neutrofilos_bajos, plaquetas_bajas)"
coincidencia:
  alta: "regla_central sin explicación por déficit de B12 o folato"
  moderada: "regla_central con déficit de B12 o folato (COND-M3-HE-004, NU-001 o NU-002)"
escalamiento:
  dos_lineas: 2
  tres_lineas_o_severa: 3
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["neutropenia étnica benigna (neutrófilos 1,0 a 1,5 sin otra alteración)", "infección viral reciente", "alcohol", "medicamentos (metotrexato, quimioterapia, antitiroideos)"]
guias: ["Criterio hematológico general de bicitopenia y pancitopenia"]
por_verificar: "Definir 'severa' con el médico: se propone neutrófilos < 0,5, plaquetas < 50 o anemia severa."
frase_permitida: "Dos tipos de células de tu sangre están más bajos de lo esperado. Puede tener causas tratables, como falta de vitaminas, pero conviene revisarlo con un médico en los próximos días."
frases_prohibidas: ["tienes leucemia", "tienes cáncer", "tu médula está fallando"]
recomendaciones_sugeridas: ["consulta médica en los próximos días", "repetir hemograma con frotis"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Dos líneas | Hb ajustada 11,0 (mujer), plaquetas 120 | Activa, escalamiento 2 |
| Tres líneas | Anemia, neutrófilos 1,1 y plaquetas 90 | Activa, escalamiento 3 |
| Con B12 baja | Anemia y plaquetas 130 con B12 baja | Activa, moderada |
| Negativo · PDF ejemplos | Solo anemia (mujer) | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
