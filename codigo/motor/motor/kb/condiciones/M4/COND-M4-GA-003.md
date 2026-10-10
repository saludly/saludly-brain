## COND-M4-GA-003 · Alteración colestásica

**Qué detecta.** Fosfatasa alcalina alta de forma desproporcionada frente a las transaminasas, con GGT alta que confirma el origen hepático. Si la fosfatasa alcalina sube sola con GGT normal, el origen probable es óseo y no se activa.

```yaml
id: COND-M4-GA-003
nombre: Alteración colestásica
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D1
calculo: "R = (ALT / límite superior de ALT) / (ALP / límite superior de ALP)"
criterios:
  - id: alp_alta
    biomarcador: alp
    condicion: "> límite superior del laboratorio"
  - id: ggt_alta
    biomarcador: ggt
    condicion: "> límite superior del laboratorio"
  - id: patron_colestasico
    condicion: "R < 2"
  - id: bilirrubina_directa_alta
    biomarcador: bilirubin_direct
    condicion: "> límite superior"
  - id: alp_doble
    biomarcador: alp
    condicion: "> 2 veces el límite superior"
regla_central: "alp_alta AND ggt_alta AND patron_colestasico"
coincidencia:
  alta: "regla_central"
  baja: "alp_alta con GGT normal (origen óseo probable; vigilar)"
escalamiento:
  base: 1
  si_alp_doble_o_bilirrubina_directa_alta: 2
nivel_lenguaje: patron_compatible
confusores: ["embarazo (la fosfatasa alcalina sube por la placenta)", "crecimiento óseo en menores de 25", "medicamentos"]
guias: ["ACG 2017"]
por_verificar: "Uso del factor R y de 2 veces el límite para escalar; confirmar en la guía completa."
frase_permitida: "Algunas pruebas del hígado relacionadas con la bilis (fosfatasa alcalina y GGT) están altas. Conviene revisarlas con tu médico."
frases_prohibidas: ["tienes cálculos en la vesícula", "tienes un tumor", "tienes cirrosis biliar"]
recomendaciones_sugeridas: ["consulta médica", "revisar medicamentos y suplementos"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | ALP 260 (hasta 129), GGT 180, ALT 40 (R 0,4) | Activa, escalamiento 2 (más del doble) |
| Leve | ALP 160, GGT 95, ALT 35 | Activa, escalamiento 1 |
| Óseo | ALP 170, GGT 30 | Vigilar; origen óseo probable |
| Negativo · PDF hombre 46 años | ALP 88, GGT 72 (hasta 71) | No activa (falta ALP alta) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
