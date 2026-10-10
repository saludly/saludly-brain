## COND-M1-EM-A02 · Resistencia a la insulina por HOMA-IR (apoyo)

**Qué detecta.** Insulina en ayunas alta o HOMA-IR elevado. Ninguna guía fija un umbral diagnóstico de HOMA-IR y los cortes publicados varían entre 1,6 y 3,0 según la población, así que solo refuerza prediabetes y síndrome metabólico. Al paciente nunca se le muestra un corte como si fuera consenso.

```yaml
id: COND-M1-EM-A02
nombre: Resistencia a la insulina por HOMA-IR
modulo: M1
especialidad: endocrinologia_metabolica
tipo: apoyo
detectabilidad: D1
calculo: "homa_ir = glucosa (mg/dL) x insulina (µUI/mL) / 405"
criterios:
  - id: insulina_alta
    biomarcador: insulin
    condicion: "> límite superior del laboratorio"
  - id: homa_elevado
    biomarcador: homa_ir
    condicion: "> 2.5"
    nota: "corte operativo provisional, a reemplazar por uno validado en población colombiana"
regla_central: "insulina_alta OR homa_elevado"
contexto_obligatorio: ["ayuno_horas >= 8", "no usa insulina"]
modifica: ["COND-M1-EM-001", "COND-M1-EM-003"]
efecto: "Solo refuerza condiciones activas. Sin EM-001 ni EM-003 activas, aparece como vigilar en la vista médica."
guias: ["Sin guía con umbral; ficha homa_ir del Knowledge Base"]
por_verificar: "El corte de 2,5 es una decisión operativa, no de guía. El médico puede cambiarlo o pedir que solo se use la insulina fuera de rango."
frase_permitida_medico: "HOMA-IR {valor}: compatible con resistencia a la insulina; no existe un corte universal validado."
frases_prohibidas: ["tienes resistencia a la insulina", "tu páncreas está fallando"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza · PDF hombre 46 años | Glucosa 112, insulina 19,8 (HOMA-IR 5,5) | Refuerza EM-001 y EM-003 |
| Vigilar | Glucosa 90, insulina 14 (HOMA-IR 3,1), sin condiciones activas | Vigilar en la vista médica |
| Negativo · PDF mujer 34 años | Glucosa 86, insulina 6,1 (HOMA-IR 1,3) | No activa |
| No calculable | Usa insulina | No se calcula |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
