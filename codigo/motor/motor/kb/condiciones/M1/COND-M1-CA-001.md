## COND-M1-CA-001 · Dislipidemia aterogénica

**Qué detecta.** Colesterol LDL o no-HDL por encima de los cortes de tamizaje, con o sin HDL bajo y triglicéridos altos. Su importancia real depende del riesgo cardiovascular global (CA-005).

```yaml
id: COND-M1-CA-001
nombre: Dislipidemia aterogénica
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: ldl_alto
    biomarcador: ldl_c
    condicion: ">= 130"
    unidad: mg/dL
  - id: no_hdl_alto
    biomarcador: non_hdl_c
    condicion: ">= 160"
    unidad: mg/dL
  - id: hdl_bajo
    biomarcador: hdl_c
    condicion: "< 40 si hombre; < 50 si mujer"
    unidad: mg/dL
  - id: tg_alto
    biomarcador: triglycerides
    condicion: ">= 150"
    unidad: mg/dL
regla_central: "ldl_alto OR no_hdl_alto"
contexto_obligatorio: ["ayuno_horas >= 8 si el LDL es calculado", "embarazo == false"]
excluye_si: ["COND-M1-CA-002"]
coincidencia:
  alta: "ldl_alto AND no_hdl_alto"
  moderada: "ldl_alto XOR no_hdl_alto"
  baja: "hdl_bajo AND tg_alto AND NOT (ldl_alto OR no_hdl_alto)"
escalamiento: 1
modificado_por: ["COND-M1-CA-A01"]
nivel_lenguaje: riesgo_potencial
confusores: ["ayuno_insuficiente", "tsh_alta (causa secundaria posible)", "estatina_en_uso (se lee como control, no como detección)"]
guias: ["GPC Colombia dislipidemias 2014", "ACC/AHA 2026, manejo de dislipidemia"]
por_verificar: "Los cortes de 130 y 160 mg/dL son cortes operativos de tamizaje. Las guías fijan metas según el riesgo global, no un corte único."
frase_permitida: "Tu colesterol LDL está por encima del valor que usamos para tamizaje. Lo que significa para ti depende de tu riesgo cardiovascular global, que conviene revisar con tu médico."
frases_prohibidas: ["tienes dislipidemia", "tienes enfermedad cardiovascular", "debes tomar estatinas", "tu colesterol es peligroso"]
recomendaciones_sugeridas: ["fibra soluble y leguminosas", "menos grasa saturada y ultraprocesados", "actividad aeróbica la mayoría de días"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | LDL 142, colesterol total 228, HDL 36 (no-HDL 192), triglicéridos 238 | Activa, coincidencia alta, escalamiento 1 |
| Positivo moderado · PDF mujer 34 años | LDL 136, colesterol total 214, HDL 58 (no-HDL 156) | Activa, coincidencia moderada, escalamiento 1 |
| Negativo | LDL 110, colesterol total 185, HDL 50 (no-HDL 135) | No activa |
| Vigilar | LDL 120, no-HDL 150, HDL 35 (hombre), triglicéridos 210 | No activa como condición; se muestra como "vigilar" |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
