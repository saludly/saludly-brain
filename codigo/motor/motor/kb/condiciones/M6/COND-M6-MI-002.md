## COND-M6-MI-002 · Posible proteína anormal en la sangre (gammapatía)

**Qué detecta.** Globulinas mayores de 3,5 g/dL, relación albúmina/globulina menor de 1, o IgG o IgM más de 2 veces su límite superior. Con una señal más (anemia, calcio corregido alto o TFG menor de 60) se activa; sin ella, queda pendiente de la electroforesis de proteínas, que corre como refleja. La mayoría de las gammapatías son benignas (MGUS), pero se vigilan.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M6-MI-002
nombre: Posible proteína anormal en la sangre (gammapatía)
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: incluida
detectabilidad: D2
criterios:
  - id: proteinas_alteradas
    biomarcador: globulin
    condicion: "globulinas > 3,5 OR A/G < 1,0 OR IgG > 2 × límite superior OR IgM > 2 × límite superior"
  - id: senal_adicional
    biomarcador: calcium
    condicion: "anemia (HE-001) OR calcio corregido sobre el rango OR TFG < 60"
  - id: electroforesis
    biomarcador: serum_protein_electrophoresis
    condicion: "banda monoclonal presente"
regla_central: "proteinas_alteradas AND (senal_adicional OR electroforesis)"
estados: {solo_proteinas_sin_electroforesis: "pendiente_refleja", electroforesis_policlonal_o_normal: "no_activa"}
coincidencia:
  alta: "electroforesis con banda monoclonal"
  moderada: "proteinas_alteradas con senal_adicional, sin electroforesis"
  baja: "con hepatitis activa, ANA positivo o hs-CRP > 10 (probable aumento policlonal)"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["hepatitis B o C", "enfermedad autoinmune (ANA positivo)", "infección o inflamación crónica", "deshidratación"]
guias: ["IMWG (International Myeloma Working Group)", "NCCN, gammapatías monoclonales"]
reemplaza: "Las alertas de proteínas de SEG-009 no se repiten cuando esta condición está activa; mientras está pendiente de la electroforesis, SEG-009 sigue avisando."
frase_permitida: "En tu sangre apareció un patrón de proteínas que conviene estudiar. Casi siempre tiene una explicación benigna, pero necesita un examen adicional y una revisión médica."
frases_prohibidas: ["tienes mieloma", "tienes cáncer", "tienes un tumor"]
recomendaciones_sugeridas: ["consulta médica en las próximas semanas", "electroforesis de proteínas si no se hizo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Con señal adicional | Proteínas 9,0, albúmina 4,0 (globulinas 5,0), Hb ajustada 10,9 | Activa, moderada, escalamiento 2 |
| Solo proteínas | Globulinas 4,1, sin otra señal | Pendiente de refleja (electroforesis) |
| Electroforesis con banda | Globulinas 4,1 y banda monoclonal | Activa, alta, escalamiento 2 |
| Policlonal | Globulinas 4,1, electroforesis policlonal | No activa |
| Negativo · PDF ejemplos | Globulinas normales | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
