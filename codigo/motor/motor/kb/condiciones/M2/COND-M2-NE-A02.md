## COND-M2-NE-A02 · Confirmación de TFG con cistatina C (apoyo)

**Qué detecta.** Cuando la TFG por creatinina está entre 45 y 59 sin albuminuria, o la creatinina es poco confiable por masa muscular extrema, KDIGO sugiere confirmar con la ecuación combinada creatinina-cistatina C. Si la combinada es de 60 o más, la enfermedad renal no se confirma.

```yaml
id: COND-M2-NE-A02
nombre: Confirmación de TFG con cistatina C
modulo: M2
especialidad: nefrologia
tipo: apoyo
detectabilidad: D1
activa_refleja_si:
  - "egfr 45-59 AND uacr < 30"
  - "obesidad clase 3 (IMC >= 40)"
  - "masa muscular extrema: objetivo de masa muscular o atleta declarado, amputación, desnutrición"
calculo: "CKD-EPI 2021 creatinina-cistatina C, coeficientes de la publicación original"
criterios:
  - id: tfg_combinada_baja
    condicion: "egfr_combinada < 60"
  - id: tfg_combinada_normal
    condicion: "egfr_combinada >= 60"
modifica: ["COND-M2-NE-001"]
efecto: "Si tfg_combinada_baja, NE-001 usa la TFG combinada para el estadio. Si tfg_combinada_normal, NE-001 baja a coincidencia baja."
guias: ["KDIGO 2024"]
frase_permitida_medico: "TFG combinada creatinina-cistatina C {valor}: {confirma | no confirma} enfermedad renal crónica."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| No confirma | TFG creatinina 54, albúmina/creatinina 10, TFG combinada 66 | NE-001 baja a vigilar |
| Confirma | TFG creatinina 52, TFG combinada 49 | NE-001 se mantiene con G3a |
| Masa muscular | Objetivo "aumentar mi masa muscular", creatinina 1,35, TFG 68 | Se pide cistatina C; se usa la combinada |
| No aplica | TFG 96 | No se pide |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
