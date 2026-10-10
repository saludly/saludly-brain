## COND-M6-MI-A02 · Edad biológica (PhenoAge) (apoyo)

**Qué detecta.** Estima la edad cuyo riesgo de mortalidad corresponde al de la persona, combinando la edad con 9 analitos que ya están en el panel. Es un modelo publicado (Levine y colaboradores, 2018), entrenado en población de EE. UU. y sin validación conocida en Colombia. Se muestra aparte del informe clínico, como indicador de bienestar para seguir en el tiempo.

```yaml
id: COND-M6-MI-A02
nombre: Edad biológica (PhenoAge)
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: apoyo
detectabilidad: D1
entradas_y_unidades_del_modelo:
  albumina: "g/L (g/dL x 10)"
  creatinina: "µmol/L (mg/dL x 88,4)"
  glucosa: "mmol/L (mg/dL / 18,016), en ayunas"
  pcr: "mg/dL (hs-CRP en mg/L / 10), en logaritmo natural"
  linfocitos: "%"
  vcm: "fL"
  rdw: "%"
  fosfatasa_alcalina: "U/L"
  leucocitos: "10^3/µL"
  edad: "años"
calculo:
  xb: "-19,907 - 0,0336 x albúmina + 0,0095 x creatinina + 0,1953 x glucosa + 0,0954 x ln(PCR) - 0,0120 x linfocitos + 0,0268 x VCM + 0,3306 x RDW + 0,00188 x fosfatasa alcalina + 0,0554 x leucocitos + 0,0804 x edad"
  mortalidad: "M = 1 - exp(-exp(xb) x (exp(120 x 0,0076927) - 1) / 0,0076927)"
  phenoage: "141,50225 + ln(-0,00553 x ln(1 - M)) / 0,090165"
se_calcula_si: ["los 9 analitos en estado medido", "glucosa en ayunas", "edad de 20 años o más"]
reglas_especiales:
  - "PCR menor que el límite de detección: se usa el límite y se marca en la vista médica"
  - "Anemia, infección reciente o hs-CRP > 10: se calcula, pero se advierte que el valor puede estar inflado temporalmente"
  - "No se calcula con embarazo"
escalamiento: 0
presentacion: ["pantalla aparte del informe clínico", "edad biológica, edad cronológica y diferencia", "explicación del modelo y su limitación poblacional", "tendencia cuando haya una segunda toma"]
guias: ["Levine et al. 2018, Aging 10(4):573-591"]
por_verificar: "Los coeficientes se tomaron de una implementación pública que cita el artículo; antes de producción, verificarlos contra el artículo original y su ejemplo publicado. Confirmar también el rango de edad del modelo."
frase_permitida: "Con 9 de tus resultados, un modelo científico estima tu edad biológica en {phenoage} años, frente a tus {edad} años. Es una estimación para seguir en el tiempo, no un diagnóstico."
frases_prohibidas: ["vas a vivir menos", "tu cuerpo tiene X años", "estás envejeciendo más rápido (sin una segunda medición)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Albúmina 4,6, creatinina 0,98, glucosa 112, hs-CRP 3,4, linfocitos 31,0 %, VCM 89,9, RDW 13,1, fosfatasa alcalina 88, leucocitos 7,8 | PhenoAge 44,3 años (1,7 menos que su edad) |
| PDF mujer 34 años | Albúmina 4,3, creatinina 0,72, glucosa 86, hs-CRP 0,8, linfocitos 35,0 %, VCM 78,2, RDW 16,4, fosfatasa alcalina 62, leucocitos 6,1 | PhenoAge 34,1 años; advertencia: la anemia sube el RDW y puede inflar el valor |
| Falta un analito | Sin fosfatasa alcalina | No se calcula; se dice qué falta |
| Sin ayuno | Ayuno de 4 horas | No se calcula |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
