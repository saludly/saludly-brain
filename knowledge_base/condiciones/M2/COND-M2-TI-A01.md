## COND-M2-TI-A01 · Autoinmunidad tiroidea (apoyo)

**Qué detecta.** Anti-TPO positivo, o anti-Tg positivo si anti-TPO sale negativo. Clasifica la causa de una TSH alta como autoinmune (tiroiditis de Hashimoto) y aumenta la probabilidad de progresar a hipotiroidismo. Las dos son reflejas: el laboratorio las corre si la TSH sale alta.

```yaml
id: COND-M2-TI-A01
nombre: Autoinmunidad tiroidea
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: apoyo
detectabilidad: D1
criterios:
  - id: anti_tpo_positivo
    biomarcador: anti_tpo
    condicion: "> límite superior del laboratorio"
  - id: anti_tg_positivo
    biomarcador: anti_tg
    condicion: "> límite superior del laboratorio (solo si anti-TPO negativo)"
regla_central: "anti_tpo_positivo OR anti_tg_positivo"
bloqueado_si: ["biotina alta o suplemento declarado"]
modifica: ["COND-M2-TI-001", "COND-M2-TI-002", "COND-M2-TI-006"]
efecto: "Agrega al texto que la causa probable es autoinmune; en TI-001 la vista médica recuerda que la guía AACE/ATA considera tratamiento con anti-TPO positivo."
relacion_vigilar: "hierro bajo + anticuerpos positivos: vigilar (documento 03, 03.7)"
guias: ["Consenso colombiano de hipotiroidismo 2023", "AACE/ATA"]
frase_permitida: "Tus anticuerpos tiroideos están positivos, lo que sugiere que la causa es autoinmune, es decir, que el propio sistema de defensa afecta a la tiroides. Es la causa más común y se maneja bien con seguimiento."
frases_prohibidas: ["tienes Hashimoto", "tienes una enfermedad autoinmune grave"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | Anti-TPO 186 (menor de 34), con TSH 6,90 | Refuerza TI-001; se marca relación vigilar con ferritina baja |
| Anti-Tg | Anti-TPO negativo, anti-Tg 210 (menor de 115), TSH 7,0 | Refuerza TI-001 |
| Negativo | Anti-TPO 12 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
