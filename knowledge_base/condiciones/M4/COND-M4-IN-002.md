## COND-M4-IN-002 · Hepatitis B y estado frente a la vacuna

**Qué detecta.** Interpreta el panel triple (HBsAg, anti-HBc total y anti-HBs) en cinco estados, de infección activa a persona susceptible que necesita vacuna. Por decisión del equipo se mide a todos con el consentimiento de la visita. Los estados con infección los comunica el médico por llamada.

```yaml
id: COND-M4-IN-002
nombre: Hepatitis B y estado frente a la vacuna
modulo: M4
especialidad: infectologia
tipo: incluida
detectabilidad: D3
estados:
  infeccion_activa:
    regla: "HBsAg reactivo"
    escalamiento: 2
    canal: "llamada del médico"
  infeccion_pasada_resuelta:
    regla: "HBsAg no reactivo AND anti-HBc reactivo AND anti-HBs >= 10"
    escalamiento: 1
    nota: "riesgo de reactivación con inmunosupresión o quimioterapia; la vista médica lo destaca"
  anti_hbc_aislado:
    regla: "HBsAg no reactivo AND anti-HBc reactivo AND anti-HBs < 10"
    escalamiento: 2
    canal: "llamada del médico"
    nota: "varias interpretaciones posibles; el médico puede pedir carga viral"
  inmune_por_vacuna:
    regla: "HBsAg no reactivo AND anti-HBc no reactivo AND anti-HBs >= 10"
    escalamiento: 0
  susceptible:
    regla: "HBsAg no reactivo AND anti-HBc no reactivo AND anti-HBs < 10"
    escalamiento: 1
    nota: "recomendar vacuna; oferta de vacunación domiciliaria pendiente de validar con el esquema del PAI para adultos"
regla_central: "infeccion_activa OR anti_hbc_aislado OR infeccion_pasada_resuelta"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["CDC 2023, interpretación serológica de hepatitis B", "Res. 1314 de 2020"]
por_verificar: "Fuentes leídas solo por resultado de búsqueda; confirmar la tabla de interpretación y el esquema del PAI para adultos."
frase_permitida_activa: "Tu prueba de hepatitis B muestra una infección. Nuestro médico te va a llamar para explicarte qué significa y los siguientes pasos."
frase_permitida_susceptible: "No tienes defensas contra la hepatitis B. La buena noticia es que existe una vacuna segura y efectiva; pregúntale a tu médico o a nosotros cómo aplicártela."
frase_permitida_inmune: "Tienes defensas contra la hepatitis B, probablemente por la vacuna."
frases_prohibidas: ["tienes hepatitis crónica", "tienes cirrosis", "es incurable"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Susceptible · PDF hombre 46 años | HBsAg no reactivo, anti-HBc no reactivo, anti-HBs 4,2 | Estado susceptible, escalamiento 1, recomendación de vacuna |
| Inmune · PDF mujer 34 años | HBsAg y anti-HBc no reactivos, anti-HBs 85 | Inmune por vacuna, escalamiento 0 |
| Activa | HBsAg reactivo | Escalamiento 2, llamada |
| Resuelta | HBsAg no reactivo, anti-HBc reactivo, anti-HBs 120 | Escalamiento 1, nota de reactivación |
| Anti-HBc aislado | HBsAg no reactivo, anti-HBc reactivo, anti-HBs 3 | Escalamiento 2, llamada |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
