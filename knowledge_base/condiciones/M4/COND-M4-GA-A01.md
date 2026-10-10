## COND-M4-GA-A01 · Bilirrubina indirecta elevada aislada (apoyo)

**Qué detecta.** Bilirrubina total alta con directa normal y el resto de pruebas hepáticas normales. Sin anemia ni signos de hemólisis, suele ser un patrón benigno y frecuente. Con anemia, reticulocitos altos y LDH alta, se lee junto con la relación de hemólisis del documento 03.

```yaml
id: COND-M4-GA-A01
nombre: Bilirrubina indirecta elevada aislada
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: apoyo
detectabilidad: D1
calculo: "bilirrubina indirecta = bilirrubina total - bilirrubina directa"
criterios:
  - id: bt_alta
    biomarcador: bilirubin_total
    condicion: "> límite superior"
  - id: bd_normal
    biomarcador: bilirubin_direct
    condicion: "dentro del intervalo"
  - id: resto_hepatico_normal
    condicion: "ALT, AST, ALP y GGT dentro del intervalo"
  - id: signos_hemolisis
    condicion: "anemia (HE-001) AND reticulocitos altos AND LDH alta"
regla_central: "bt_alta AND bd_normal AND resto_hepatico_normal"
efecto: "Sin signos_hemolisis: resultado observado, escalamiento 0. Con signos_hemolisis: activa la relación hemólisis (escalamiento 2)."
confusores: ["ayuno prolongado (sube la bilirrubina indirecta)", "hemólisis de la muestra"]
guias: ["ACG 2017"]
frase_permitida: "Tu bilirrubina está un poco alta, con el resto del hígado normal. Es un patrón frecuente y casi siempre benigno; puede subir con el ayuno."
frases_prohibidas: ["tienes síndrome de Gilbert", "tienes ictericia", "tienes una enfermedad del hígado"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Aislada | Bilirrubina total 1,9, directa 0,3, resto normal, hemoglobina normal | Resultado observado, escalamiento 0 |
| Con hemólisis | Bilirrubina total 2,4, directa 0,3, anemia, reticulocitos altos, LDH alta | Activa relación hemólisis, escalamiento 2 |
| Negativo · PDF ejemplos | Bilirrubina total 0,80 y 0,50 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
