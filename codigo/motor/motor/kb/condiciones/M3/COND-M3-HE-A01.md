## COND-M3-HE-A01 · Anemia con perfil inflamatorio (apoyo)

**Qué detecta.** Anemia con ferritina normal o alta, saturación de transferrina baja y hs-CRP alta. Orienta a una enfermedad de fondo, no a falta de hierro. Cuando se cumple, cambia el texto de HE-001: la recomendación es buscar la causa, no comer más hierro.

```yaml
id: COND-M3-HE-A01
nombre: Anemia con perfil inflamatorio
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D3
criterios:
  - id: anemia
    condicion: "COND-M3-HE-001 activa"
  - id: ferritina_no_baja
    condicion: "ferritin >= 70 con hs_crp > 5"
  - id: saturacion_baja
    condicion: "transferrin_saturation < 20"
  - id: inflamacion
    condicion: "hs_crp > 5"
regla_central: "anemia AND ferritina_no_baja AND saturacion_baja AND inflamacion"
modifica: ["COND-M3-HE-001"]
efecto: "HE-001 sube a escalamiento 2 y su texto cambia a 'buscar causa de fondo'; no se activan recomendaciones de hierro."
guias: ["OMS 2020, ferritina"]
frase_permitida: "Tu anemia no parece deberse a falta de hierro sino a una inflamación de fondo. Por eso es importante revisarla con tu médico."
frases_prohibidas: ["tienes una enfermedad crónica", "tienes cáncer"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Anemia, ferritina 180, saturación 14 %, hs-CRP 22 | Activa; HE-001 con escalamiento 2 y sin recomendaciones de hierro |
| Negativo · PDF mujer 34 años | Anemia, ferritina 7, hs-CRP 0,8 | No activa (manda HE-002) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
