## COND-M1-CA-004 · Lipoproteína(a) elevada

**Qué detecta.** Lp(a) por encima de 50 mg/dL o de 105 nmol/L (ESC/EAS). Es un factor de riesgo heredado y estable: se mide una vez en la vida. La unidad del laboratorio es obligatoria, porque mg/dL y nmol/L no se convierten de forma confiable entre sí.

```yaml
id: COND-M1-CA-004
nombre: Lipoproteína(a) elevada
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: lpa_alta_mg
    biomarcador: lpa
    condicion: "> 50"
    unidad: mg/dL
  - id: lpa_alta_nmol
    biomarcador: lpa
    condicion: "> 105"
    unidad: nmol/L
  - id: lpa_alta_acc
    biomarcador: lpa
    condicion: ">= 125"
    unidad: nmol/L
    nota: "corte ACC/AHA 2026; se menciona en la vista médica"
regla_central: "lpa_alta_mg OR lpa_alta_nmol"
contexto_obligatorio: ["unidad declarada por el laboratorio"]
excluye_si: []
coincidencia:
  alta: "regla_central con unidad declarada"
escalamiento: 1
nivel_lenguaje: riesgo_potencial
confusores: []
reglas_especiales: ["no convertir entre mg/dL y nmol/L", "no repetir en tomas futuras salvo indicación médica"]
guias: ["ESC/EAS 2025, actualización de dislipidemias", "ACC/AHA 2026"]
frase_permitida: "Tu lipoproteína(a) está alta. Es un factor que se hereda y que suma al riesgo cardiovascular; conviene comentarlo con tu médico y que tus familiares cercanos se la midan una vez."
frases_prohibidas: ["vas a tener un infarto", "tienes enfermedad cardiovascular", "esto se cura con dieta"]
recomendaciones_sugeridas: ["controlar los demás factores de riesgo (LDL, presión, tabaco)", "medición en familiares de primer grado"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | Lp(a) 64 mg/dL | Activa, coincidencia alta, escalamiento 1 |
| Negativo · PDF hombre 46 años | Lp(a) 18 mg/dL | No activa |
| Unidad nmol/L | Lp(a) 140 nmol/L | Activa; la vista médica menciona también el corte ACC/AHA |
| Sin unidad | Lp(a) 70, unidad vacía | No interpretable; no activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
