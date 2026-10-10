## COND-M2-TI-009 · Cortisol de la mañana bajo (posible insuficiencia suprarrenal)

**Qué detecta.** Cortisol tomado entre las 6:00 y las 10:00 menor de 5 µg/dL. ACTH alta, sodio bajo o potasio alto lo refuerzan. Los corticoides en cualquier forma (pastillas, inyecciones, inhaladores o cremas potentes) suprimen el cortisol: con corticoide declarado no se interpreta. Antes estaba solo en la regla de seguridad SEG-002.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M2-TI-009
nombre: Cortisol de la mañana bajo (posible insuficiencia suprarrenal)
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D2
criterios:
  - id: cortisol_bajo
    biomarcador: cortisol
    condicion: "< 5 (toma entre 6:00 y 10:00)"
    unidad: µg/dL
  - id: acth_alta
    biomarcador: acth
    condicion: "sobre el rango del laboratorio"
  - id: electrolitos
    biomarcador: sodium
    condicion: "sodio bajo o potasio alto"
regla_central: "cortisol_bajo"
no_interpretable_si: ["toma fuera de 6:00 a 10:00", "corticoide declarado (oral, inyectado, inhalado o tópico potente)"]
coincidencia:
  alta: "cortisol_bajo con acth_alta o electrolitos"
  moderada: "cortisol_bajo sola"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["corticoides", "toma tardía", "embarazo o anticonceptivos (cambian la proteína transportadora)"]
guias: ["Endocrine Society 2016, insuficiencia suprarrenal primaria"]
por_verificar: "Corte de 5 µg/dL de cortisol matutino (Endocrine Society 2016); el médico confirma."
reemplaza: "La alerta de cortisol bajo de SEG-002 no se repite cuando esta condición está activa."
frase_permitida: "Tu cortisol de la mañana, una hormona del estrés, salió bajo. Puede deberse a medicamentos o a la hora de la toma, pero conviene revisarlo con un médico en los próximos días."
frases_prohibidas: ["tienes enfermedad de Addison", "tus glándulas no funcionan"]
recomendaciones_sugeridas: ["consulta médica en los próximos días", "consulta urgente si hay vómito, mareo intenso o desmayo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Con ACTH alta | Cortisol 3,2 a las 7:30, ACTH 180 | Activa, alta, escalamiento 2 |
| Sola | Cortisol 4,1 a las 8:00 | Activa, moderada |
| Con prednisolona | Cortisol 2,0 y prednisolona declarada | No interpretable |
| Negativo · PDF ejemplos | Cortisol normal | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
