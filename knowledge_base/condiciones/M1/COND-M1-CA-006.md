## COND-M1-CA-006 · Hipertensión arterial o presión elevada (sospecha)

**Qué detecta.** Presión de 130/80 mmHg o más en la toma de la enfermera. Siempre es sospecha: la guía colombiana pide confirmar con automonitoreo en casa o con monitoreo ambulatorio. Si el paciente registra su presión con tensiómetro en Apple Health, esos registros cuentan como automonitoreo para el médico.

```yaml
id: COND-M1-CA-006
nombre: Hipertensión arterial o presión elevada (sospecha)
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: pa_elevada
    contexto: presion_enfermera
    condicion: "sistólica >= 130 OR diastólica >= 80"
    unidad: mmHg
    medicion: "promedio de las 2 últimas de 3 tomas, sentado, tras 5 minutos de reposo, tensiómetro validado"
  - id: pa_grado_2
    contexto: presion_enfermera
    condicion: "sistólica >= 140 OR diastólica >= 90"
  - id: pa_severa
    contexto: presion_enfermera
    condicion: "sistólica >= 180 OR diastólica >= 120"
  - id: ampa_confirma
    contexto: apple_health_presion
    condicion: "promedio de al menos 7 días de registros >= 130/80"
regla_central: "pa_elevada"
contexto_obligatorio: ["presión medida por la enfermera"]
excluye_si: ["hipertensión diagnosticada declarada (se lee como control, no como detección)"]
coincidencia:
  alta: "pa_elevada AND ampa_confirma"
  moderada: "pa_elevada sin automonitoreo"
escalamiento:
  base: 1
  si_pa_grado_2: 2
  si_pa_severa: 3
dispara: ["reflejas aldosterona y renina", "revisión del estudio inicial: creatinina, TFG, uroanálisis, albúmina/creatinina, sodio, potasio, TSH y ácido úrico (ya en el panel)"]
contexto_adicional: ["notificación de hipertensión del Apple Watch: refuerza la recomendación de confirmar, no cambia la coincidencia"]
nivel_lenguaje: patron_compatible
confusores: ["dolor, ansiedad o esfuerzo antes de la toma", "café o cigarrillo 30 minutos antes", "manguito de tamaño inadecuado"]
guias: ["GPC Colombia HTA 2025 (Minsalud e IETS)", "AHA/ACC 2025, presión arterial alta"]
por_verificar: "El umbral de 180/120 como presión severa sale de AHA/ACC 2025, leída solo por resultado de búsqueda. Leer la guía completa antes de la firma."
frase_permitida: "Tu presión en la visita estuvo en {valor}, por encima de 130/80. Una sola toma no confirma hipertensión: conviene medirla en casa varios días con un tensiómetro validado y revisarlo con tu médico."
frase_permitida_severa: "Tu presión estuvo muy alta en la visita. Nuestro equipo médico te va a llamar hoy. Si tienes dolor de pecho, dolor de cabeza intenso, dificultad para hablar o falta de aire, ve a urgencias."
frases_prohibidas: ["eres hipertenso", "tienes hipertensión", "el reloj detectó hipertensión"]
recomendaciones_sugeridas: ["automonitoreo 7 días, mañana y noche", "reducir sal", "actividad física", "reducir alcohol"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo grado 1 | Promedio 134/84, sin automonitoreo | Activa, coincidencia moderada, escalamiento 1; activa aldosterona y renina |
| Positivo grado 2 con confirmación | Promedio 146/92; Apple Health con promedio de 7 días 141/89 | Activa, coincidencia alta, escalamiento 2 |
| Severa | Promedio 184/112 | Activa, escalamiento 3, llamada el mismo día |
| Negativo | Promedio 118/76 | No activa |
| Hipertensión conocida | Promedio 138/86, toma antihipertensivo | No activa como detección; la vista médica muestra control |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
