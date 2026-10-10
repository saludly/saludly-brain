## COND-M3-HE-004 · Anemia por déficit de B12 o folato

**Qué detecta.** Anemia (HE-001) con glóbulos rojos grandes (VCM alto) y B12 menor de 180 ng/L o folato menor de 4 ng/mL. Si la B12 está entre 180 y 350, decide el ácido metilmalónico.

```yaml
id: COND-M3-HE-004
nombre: Anemia por déficit de B12 o folato
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: anemia
    condicion: "COND-M3-HE-001 activa"
  - id: vcm_alto
    biomarcador: mcv
    condicion: "> límite superior"
  - id: b12_baja
    biomarcador: vitamin_b12
    condicion: "< 180, o 180-350 con ácido metilmalónico sobre el límite"
    unidad: ng/L (pg/mL)
  - id: folato_bajo
    biomarcador: folate
    condicion: "< 4"
    unidad: ng/mL
regla_central: "anemia AND vcm_alto AND (b12_baja OR folato_bajo)"
excluye_si: []
excluye_a: ["COND-M3-NU-001 y COND-M3-NU-002 en el informe del paciente (quedan en la vista médica)"]
coincidencia:
  alta: "regla_central"
  moderada: "anemia AND (b12_baja OR folato_bajo) con VCM normal (déficit combinado posible)"
modificado_por: ["COND-M3-NU-A01"]
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["suplementos de B12 o folato recientes", "alcohol (sube el VCM)", "hipotiroidismo (sube el VCM)", "metformina o inhibidores de bomba de protones (factor de riesgo, no confusor)"]
guias: ["NICE NG239 2024", "OMS, folato"]
frase_permitida: "Tu hemoglobina está baja, tus glóbulos rojos son más grandes de lo normal y tu {B12 o folato} está bajo. Ese patrón merece una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes anemia perniciosa", "toma B12", "inyéctate B12"]
recomendaciones_sugeridas: ["consulta médica", "alimentos de origen animal (B12) u hojas verdes y leguminosas (folato)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| B12 | Anemia, VCM 108, B12 140 | Activa, coincidencia alta, escalamiento 2 |
| Indeterminada | Anemia, VCM 104, B12 260, ácido metilmalónico alto | Activa |
| Folato | Anemia, VCM 103, folato 2,8 | Activa |
| Negativo · PDF mujer 34 años | Anemia con VCM 78,2; B12 262 con ácido metilmalónico normal | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
