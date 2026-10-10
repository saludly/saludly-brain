## COND-M5-MU-A01 · Anemia en el embarazo (apoyo)

**Qué detecta.** Cuando el perfil dice embarazo, HE-001 (módulo M3) ya usa los cortes OMS de gestante (11,0 g/dL en primer y tercer trimestre, 10,5 en el segundo) con el ajuste por altitud. Esta ficha agrega la ruta: el hallazgo va al control prenatal con escalamiento 2.

```yaml
id: COND-M5-MU-A01
nombre: Anemia en el embarazo
modulo: M5
especialidad: salud_de_la_mujer
tipo: apoyo
detectabilidad: D2
criterios:
  - id: anemia_gestante
    condicion: "COND-M3-HE-001 activa AND embarazo == true"
regla_central: "anemia_gestante"
modifica: ["COND-M3-HE-001", "COND-M3-HE-002"]
efecto: "Escalamiento mínimo 2; el texto remite al control prenatal; las recomendaciones de hierro son solo alimentarias y el suplemento lo define el control prenatal."
guias: ["OMS 2024, cortes de hemoglobina"]
frase_permitida: "Tu hemoglobina está por debajo de lo recomendado para el embarazo. Es importante comentarlo pronto en tu control prenatal."
frases_prohibidas: ["tu bebé está en riesgo", "toma hierro"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Embarazo de 26 semanas, hemoglobina 12,0 (ajustada 10,2) | Activa, escalamiento 2, ruta prenatal |
| Negativo | Embarazo de 12 semanas, hemoglobina 13,5 (ajustada 11,7) | No activa |
| No aplica · PDF mujer 34 años | No embarazada | No aplica (va por HE-001) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
