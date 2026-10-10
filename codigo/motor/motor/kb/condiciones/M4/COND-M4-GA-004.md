## COND-M4-GA-004 · Sangre oculta en heces positiva

**Qué detecta.** Prueba inmunoquímica (FIT) positiva. Exige colonoscopia; no es un diagnóstico de cáncer. Por decisión del equipo, un FIT positivo se remite a cualquier edad. El informe menciona que el tamizaje formal en Colombia es de 50 a 75 años cada 2 años (Res. 3280).

```yaml
id: COND-M4-GA-004
nombre: Sangre oculta en heces positiva
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: fit_positivo
    biomarcador: fit_stool
    condicion: "positivo"
regla_central: "fit_positivo"
coincidencia:
  alta: "fit_positivo"
escalamiento: 2
contexto_vista_medica: ["edad y si está en la franja de tamizaje 50-75", "colonoscopia previa", "antecedente familiar de cáncer colorrectal", "anemia o déficit de hierro (M3)"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["sangrado por hemorroides o menstruación (no anulan el resultado; se informan al médico)"]
guias: ["Res. 3280 de 2018", "USPSTF 2021"]
regla_seguridad: "no repetir el FIT para 'confirmar': un positivo va a colonoscopia"
frase_permitida: "En tu muestra de heces se encontró sangre que no se ve a simple vista. Tiene varias causas posibles, y la manera de saber cuál es una colonoscopia. Te recomendamos consulta médica en las próximas semanas para pedirla."
frases_prohibidas: ["tienes cáncer", "tienes un tumor", "tienes pólipos", "repite la prueba"]
recomendaciones_sugeridas: ["consulta médica para colonoscopia"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo en edad | Edad 58, FIT positivo | Activa, escalamiento 2 |
| Positivo joven | Edad 34, FIT positivo | Activa, escalamiento 2; la vista médica anota que está fuera de la franja formal |
| Con anemia | FIT positivo y anemia por déficit de hierro (M3) | Activa; la vista médica los cruza |
| Negativo · PDF ejemplos | FIT negativo | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
