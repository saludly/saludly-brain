## COND-M3-HE-003 · Déficit de hierro sin anemia

**Qué detecta.** Ferritina baja con hemoglobina ajustada normal. La OMS indica usar la ferritina para detectar el déficit en personas aparentemente sanas: es la etapa en que se puede corregir antes de que aparezca la anemia.

```yaml
id: COND-M3-HE-003
nombre: Déficit de hierro sin anemia
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: incluida
detectabilidad: D1
criterios:
  - id: ferritina_baja
    biomarcador: ferritin
    condicion: "< 15 si hs_crp <= 5; < 70 si hs_crp > 5"
    unidad: ng/mL
  - id: ferritina_limite
    biomarcador: ferritin
    condicion: "15-29 con hs_crp <= 5"
  - id: sin_anemia
    condicion: "COND-M3-HE-001 no activa"
regla_central: "ferritina_baja AND sin_anemia"
coincidencia:
  alta: "regla_central"
  baja: "ferritina_limite AND sin_anemia (vigilar)"
escalamiento:
  base: 1
  hombre_o_mujer_posmenopausica: 2
nivel_lenguaje: resultado_observado
contexto_objetivo: "objetivos de maratón, rendimiento y energía: se destaca en 'Qué puedes hacer'"
guias: ["OMS 2020, ferritina"]
por_verificar: "Escalamiento 2 en hombres y mujeres posmenopáusicas (para buscar pérdida digestiva) es propuesta de Saludly."
frase_permitida: "Tus reservas de hierro están bajas, aunque todavía no tienes anemia. Es un buen momento para corregirlo con la alimentación y revisar con tu médico por qué pasa."
frases_prohibidas: ["tienes deficiencia de hierro", "toma hierro"]
recomendaciones_sugeridas: ["alimentos ricos en hierro con vitamina C", "evitar té o café con las comidas", "consulta si es hombre o mujer posmenopáusica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Mujer 28 años, hemoglobina ajustada 12,6, ferritina 11 | Activa, escalamiento 1 |
| Hombre | Hombre 50 años, hemoglobina ajustada 13,8, ferritina 12 | Activa, escalamiento 2 |
| Vigilar | Mujer, ferritina 22, hs-CRP 1 | Coincidencia baja (vigilar) |
| Con anemia · PDF mujer 34 años | Ferritina 7 con anemia | No activa (manda HE-002) |
| Negativo · PDF hombre 46 años | Ferritina 310 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
