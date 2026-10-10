## COND-M3-NU-A01 · Homocisteína alta (apoyo)

**Qué detecta.** Homocisteína por encima del intervalo del laboratorio como marcador funcional de déficit de B12 o folato. No se usa como riesgo cardiovascular aislado (descartado en el Lote 1). La función renal baja y el hipotiroidismo también la suben.

```yaml
id: COND-M3-NU-A01
nombre: Homocisteína alta
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D1
criterios:
  - id: hcy_alta
    biomarcador: homocysteine
    condicion: "> límite superior del laboratorio"
regla_central: "hcy_alta"
contexto_obligatorio: ["ayuno >= 8 horas", "muestra refrigerada y procesada en 4 a 6 horas"]
modifica: ["COND-M3-NU-001", "COND-M3-NU-002", "COND-M3-HE-004"]
efecto: "Sube la coincidencia de déficit de B12 o folato. Sin esos déficits, se muestra como vigilar y la vista médica sugiere revisar TFG y TSH."
confusores: ["TFG < 60", "hipotiroidismo", "suplementos de B12, folato o B6 recientes (la normalizan)"]
relacion_vigilar: "TSH alta + colesterol + CK + homocisteína (documento 03)"
guias: ["NICE NG239 2024"]
frase_permitida_medico: "Homocisteína {valor} µmol/L: apoyo funcional a déficit de B12 o folato; descartar TFG baja e hipotiroidismo."
frases_prohibidas: ["riesgo de infarto por homocisteína"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza | B12 220, homocisteína 19 | NU-001 sube a coincidencia alta |
| Vigilar | Homocisteína 17, B12 y folato normales, TFG 58 | Vigilar; vista médica menciona TFG |
| Negativo · PDF ejemplos | Homocisteína 11,8 y 13,9 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
