## COND-M2-NE-002 · Albuminuria con TFG normal

**Qué detecta.** Albúmina/creatinina en orina de 30 mg/g o más con TFG de 60 o más: posible daño renal temprano. KDIGO pide confirmar con primera orina de la mañana; un solo valor puede ser transitorio.

```yaml
id: COND-M2-NE-002
nombre: Albuminuria con TFG normal
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: a2
    biomarcador: uacr
    condicion: "30-300"
    unidad: mg/g
  - id: a3
    biomarcador: uacr
    condicion: "> 300"
    unidad: mg/g
  - id: tfg_normal
    biomarcador: egfr
    condicion: ">= 60"
regla_central: "(a2 OR a3) AND tfg_normal"
contexto_obligatorio: ["muestra de primera orina de la mañana"]
excluye_si: ["COND-M2-NE-003", "COND-M2-NE-001 (si la albuminuria ya está confirmada a 3 meses)"]
coincidencia:
  alta: "regla_central confirmada en una segunda muestra"
  moderada: "regla_central en una sola muestra (a confirmar)"
escalamiento:
  a2: 1
  a3: 2
nivel_lenguaje: patron_compatible
confusores: ["ejercicio intenso 48 h", "fiebre o infección reciente", "infección urinaria (nitritos o leucocitos en el uroanálisis)", "menstruación", "glucosa muy alta"]
guias: ["KDIGO 2024"]
frase_permitida: "En tu orina apareció más albúmina de lo esperado. Puede ser transitorio, así que hay que repetirlo; si se confirma, es una señal temprana que conviene cuidar."
frases_prohibidas: ["tienes daño renal", "tus riñones están fallando"]
recomendaciones_sugeridas: ["repetir albúmina/creatinina en primera orina de la mañana", "reducir sal", "control de presión y glucosa"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Albúmina/creatinina 45, TFG 96, una toma | Activa, coincidencia moderada, A2, escalamiento 1 |
| A3 | Albúmina/creatinina 420, TFG 88 | Activa, escalamiento 2 |
| Con confusor | Albúmina/creatinina 60, ejercicio intenso el día anterior | Activa con coincidencia baja; sugiere repetir |
| Negativo · PDF mujer 34 años | Albúmina/creatinina 8 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
