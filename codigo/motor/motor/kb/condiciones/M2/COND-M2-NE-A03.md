## COND-M2-NE-A03 · Bicarbonato bajo (apoyo)

**Qué detecta.** Bicarbonato bajo como complicación de la enfermedad renal crónica. Solo se interpreta si NE-001 o NE-003 están activas; sin ellas, se muestra como valor fuera de rango.

```yaml
id: COND-M2-NE-A03
nombre: Bicarbonato bajo
modulo: M2
especialidad: nefrologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: hco3_bajo
    biomarcador: bicarbonate
    condicion: "< 22"
    unidad: mmol/L
  - id: hco3_muy_bajo
    biomarcador: bicarbonate
    condicion: "< 18"
    unidad: mmol/L
regla_central: "hco3_bajo AND (COND-M2-NE-001 OR COND-M2-NE-003 activa)"
modifica: ["COND-M2-NE-001", "COND-M2-NE-003"]
efecto: "Vista médica: complicación metabólica de la enfermedad renal; si hco3_muy_bajo, se destaca."
confusores: ["demora en procesar la muestra (puede bajar el bicarbonato)", "diarrea reciente"]
guias: ["KDIGO 2024"]
por_verificar: "Corte de 18 mmol/L para destacar; confirmar en KDIGO 2024."
frase_permitida_medico: "Bicarbonato {valor} mmol/L en contexto de TFG baja: posible acidosis metabólica asociada a ERC."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Bicarbonato 19, NE-001 activa (G3b) | Activa como apoyo |
| Sin ERC | Bicarbonato 20, TFG 95 | No activa; valor fuera de rango |
| Negativo · PDF ejemplos | Bicarbonato 25 y 24 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
