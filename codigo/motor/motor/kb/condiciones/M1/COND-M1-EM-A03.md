## COND-M1-EM-A03 · Diabetes con posible falta de insulina

**Qué detecta.** Glucosa o HbA1c en rango de diabetes (o diabetes conocida) con péptido C bajo (menor de 0,6 ng/mL, por verificar). Sugiere que el páncreas produce poca insulina, como en la diabetes tipo 1 o la autoinmune del adulto (LADA). Cambia el tratamiento: el médico pide anticuerpos (anti-GAD).

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M1-EM-A03
nombre: Diabetes con posible falta de insulina
modulo: M1
especialidad: endocrinologia_metabolica
tipo: apoyo
detectabilidad: D2
criterios:
  - id: diabetes
    biomarcador: hba1c
    condicion: "COND-M1-EM-002 activa o en control, o diabetes conocida"
  - id: peptido_c_bajo
    biomarcador: c_peptide
    condicion: "< 0,6"
    unidad: ng/mL
regla_central: "diabetes AND peptido_c_bajo"
escalamiento: modifica
modifica: ["COND-M1-EM-002"]
nivel_lenguaje: patron_compatible
confusores: ["glucosa muy alta reciente (toxicidad por glucosa baja el péptido C)", "enfermedad renal (sube el péptido C)"]
guias: ["ADA, Standards of Care 2025, clasificación de la diabetes"]
por_verificar: "Corte de 0,6 ng/mL (unos 200 pmol/L) para péptido C bajo."
frase_permitida: "Un examen sugiere que tu páncreas produce poca insulina. Esto cambia cómo se trata la diabetes; revísalo con tu médico."
frases_prohibidas: ["tienes diabetes tipo 1", "necesitas insulina"]
recomendaciones_sugeridas: ["consulta médica para anticuerpos anti-GAD"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | HbA1c 8,1, péptido C 0,3 | Apoyo; modifica EM-002 |
| Péptido C normal | HbA1c 7,2, péptido C 2,1 | No activa |
| Sin diabetes | HbA1c 5,4, péptido C 0,4 | No aplica (va a SEG-010) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
