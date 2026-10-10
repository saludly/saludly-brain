## COND-M5-MU-004 · Transición a la menopausia

**Qué detecta.** Mujer de 45 años o más, sin embarazo ni anticonceptivo hormonal, con FSH de 25 UI/L o más; el estradiol bajo lo refuerza. Es una etapa, no una enfermedad: el objetivo es informar y orientar (hueso, corazón, síntomas). Se usa el valor de FSH aunque no haya fecha de última menstruación, porque en esta etapa los ciclos dejan de ser regulares.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M5-MU-004
nombre: Transición a la menopausia
modulo: M5
especialidad: salud_de_la_mujer
tipo: apoyo
detectabilidad: D2
criterios:
  - id: edad
    biomarcador: fsh
    condicion: "mujer de 45 años o más"
  - id: fsh_alta
    biomarcador: fsh
    condicion: ">= 25"
    unidad: UI/L
  - id: estradiol_bajo
    biomarcador: estradiol
    condicion: "bajo para la fase o menor de 30 pg/mL"
regla_central: "edad AND fsh_alta"
no_aplica_si: ["embarazo", "anticonceptivo hormonal", "terapia hormonal de reemplazo"]
coincidencia:
  alta: "fsh_alta con estradiol_bajo o menopausia declarada"
  moderada: "fsh_alta sola (un pico de mitad de ciclo también la sube)"
escalamiento: modifica
nivel_lenguaje: resultado_observado
confusores: ["pico de FSH de mitad de ciclo", "anticonceptivo hormonal"]
guias: ["STRAW+10 (2012), etapas del envejecimiento reproductivo", "NICE NG23, menopausia"]
por_verificar: "Corte de FSH de 25 UI/L (STRAW+10, transición tardía)."
frase_permitida: "Tus hormonas son compatibles con la transición a la menopausia, una etapa natural. Es un buen momento para cuidar tus huesos y tu corazón y hablar con tu médico sobre cómo te sientes."
frases_prohibidas: ["estás en la menopausia (sin confirmación médica)", "ya no puedes quedar embarazada"]
recomendaciones_sugeridas: ["ejercicio de fuerza", "calcio y vitamina D en la alimentación", "control de presión y lípidos"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Con estradiol bajo | Mujer de 51 años, FSH 68, estradiol 18 | Apoyo, alta |
| Solo FSH | Mujer de 47 años, FSH 31 | Apoyo, moderada |
| Con anticonceptivo | Mujer de 46 años, FSH 40, anticonceptivo | No aplica |
| Negativo · PDF ejemplos | Mujer de 34 años | No aplica |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
