**SALUDLY BRAIN**

**07 — Recomendaciones y personalización**

*Cómo se generan, se ordenan y se entregan las recomendaciones · versión 1 · 6 de octubre de 2026*

> Las reglas de este documento las definió Claude por encargo del equipo de Saludly. Antes de usarse con pacientes reales necesitan la firma de un médico.

# **07.1 — Principio**

Cada recomendación está atada a un hallazgo o a un valor clasificado, es concreta, es de bajo riesgo y se ordena según el objetivo del paciente. Sin hallazgo no hay recomendación, y ninguna recomendación es una prescripción.

# **07.2 — Tipos de recomendación**

| Tipo | Ejemplos | Límite |
| :---- | :---- | :---- |
| Alimentación | Más fibra, menos ultraprocesados y azúcar, alimentos ricos en hierro con vitamina C | Se adapta a función renal, embarazo y diabetes |
| Hidratación | Agua a lo largo del día, más en días de entrenamiento | Con enfermedad renal o restricción de líquidos, solo "sigue la indicación de tu médico" |
| Actividad física y caminatas | Minutos semanales de actividad moderada, caminatas después de comer, fuerza dos veces por semana | Con hallazgos cardiovasculares de nivel 2 o 3, primero la consulta |
| Sueño | Horario regular, rutina antes de dormir | — |
| Hábitos | Dejar de fumar, reducir alcohol, manejo del estrés | — |
| Actividades saludables | Lectura, tiempo al aire libre, actividades sociales | Siempre como bienestar general |
| Vitaminas y suplementos | Según la regla de vitaminas: alimentos primero; suplemento como opción general para hablar con el médico | Sin dosis, sin marcas |
| Terapias | Servicios no farmacológicos sugeridos: nutricionista, actividad física guiada, fisioterapia, apoyo psicológico | Siempre como sugerencia de consulta, nunca como tratamiento |

# **07.3 — Regla de vitaminas (aprobada)**

1. Se compara con el intervalo del laboratorio: bajo, limítrofe, en rango, alto o no interpretable. Sin intervalo, solo el valor.
2. **Bajo:** alimentos que la aportan; el suplemento se menciona como opción general para consultar con el médico, sin dosis.
3. **Alto:** pregunta por suplementos; si es vitamina A o E, sugerir consulta.
4. **Biotina alta:** no interpretar TSH, T4 libre, B12 ni folato hasta repetir sin el suplemento.
5. **Vitamina C:** solo se clasifica con transporte congelado validado.
6. **Vitamina D baja:** alimentos y exposición solar prudente; sin dosis.
7. **B12 y folato:** además alimentan las condiciones de déficit, con guía y escalamiento.

# **07.4 — Cómo se ordena según el objetivo**

El objetivo nunca cambia hallazgos ni alertas; cambia el orden de "Qué puedes hacer" y el tono.

1. Primero, recomendaciones ligadas a hallazgos de escalamiento 2 o 3, sin importar el objetivo.
2. Después, las que sirven al objetivo principal y a la vez a un hallazgo.
3. Después, las del objetivo secundario.
4. Al final, hábitos generales.
5. Si el objetivo choca con un hallazgo (maratón con anemia, ganar masa muscular con TFG baja), el informe lo dice y la recomendación de entrenamiento o de proteína espera a la consulta.

| Objetivo | Biomarcadores que el agente destaca | Enfoque |
| :---- | :---- | :---- |
| Mejorar mi salud en general | Panorama completo | Equilibrio |
| Prevenir enfermedades | Riesgo cardiovascular, glucosa, riñón, hígado | Hábitos de prevención y controles |
| Cuidar una condición que ya tengo | Los ligados al diagnóstico y medicamentos | Seguimiento con el médico tratante |
| Bajar de peso | Glucosa, HbA1c, insulina, HOMA-IR, lípidos, TSH, ALT, GGT, medidas | Alimentación, actividad, sueño |
| Aumentar mi masa muscular | Proteínas, albúmina, testosterona, SHBG, CK, vitamina D, creatinina con cistatina C | Proteína, fuerza, recuperación |
| Mejorar mi rendimiento o entrenamiento | Hemoglobina ajustada por altitud, ferritina, hierro, B12, folato, magnesio, CK | Recuperación, alimentación e hidratación |
| Correr una maratón | Lo anterior, con más peso en hierro, ferritina y sodio | Hidratación y sales, hierro, progresión |
| Ser más atlético | Masa muscular y rendimiento | Fuerza, resistencia, descanso |
| Tener más energía y dormir mejor | Hemoglobina, ferritina, TSH, B12, folato, glucosa, vitamina D | Sueño, horarios, actividad |
| Envejecer de forma saludable | Edad biológica, riesgo cardiovascular, riñón, B12, desnutrición | Fuerza, alimentación, controles |

# **07.5 — Personalización con Apple Watch**

Si el paciente conectó Apple Health y los datos son recientes:

- **Pasos y minutos de actividad:** la meta parte de lo que ya hace, no de una cifra genérica ("pasar de tus 4.200 pasos diarios a 6.000").
- **Sueño:** la recomendación usa su propio promedio de horas.
- **Frecuencia cardíaca en reposo y variabilidad:** contexto de recuperación para objetivos de rendimiento.
- **Presión arterial registrada con tensiómetro en Apple Health:** se muestra como automonitoreo; el médico decide si la acepta para confirmar la sospecha de hipertensión.
- **Notificación de hipertensión del reloj:** si el paciente la reporta, se trata como contexto y refuerza la recomendación de consultar; no es un diagnóstico.

Sin Apple Watch, las recomendaciones usan rangos generales y no se menciona el reloj.

# **07.6 — Catálogo y redacción**

Las recomendaciones viven en el Knowledge Base con identificador, tipo, hallazgos que la activan, objetivos que la priorizan, contraindicaciones y texto base:

```yaml
id: REC-ALI-021
tipo: alimentacion
se_activa_con: ["COND-M3-HE-002", "ferritin:bajo"]
prioriza_objetivos: ["maraton", "rendimiento", "energia_sueno"]
contraindicada_si: ["COND-M3-HE-006"]     # posible sobrecarga de hierro
texto_base: "Incluye en tus comidas fuentes de hierro como lentejas, fríjoles, carnes magras o hígado, y acompáñalas con una fruta rica en vitamina C."
```

El agente adapta el texto base al tono y al objetivo, pero no cambia su contenido.

# **07.7 — Ejemplos por hallazgo**

| Hallazgo | Recomendación principal | Recomendación de apoyo |
| :---- | :---- | :---- |
| Prediabetes | Caminata de 15 minutos después de las comidas principales | Cambiar bebidas azucaradas por agua |
| Dislipidemia aterogénica | Más fibra soluble (avena, leguminosas) y menos grasas saturadas | Actividad aeróbica la mayoría de días de la semana |
| Déficit de hierro con anemia | Consulta médica; mientras tanto, alimentos ricos en hierro con vitamina C | Evitar té o café con las comidas principales |
| Vitamina D baja | Alimentos como pescados grasos y huevo; sol prudente | Consultar con el médico si quiere suplementar |
| Albuminuria a confirmar | Repetir la medición; reducir sal | Hidratación normal, sin excesos de proteína |
| Patrón hepático metabólico | Reducir alcohol, azúcar y ultraprocesados | Actividad física regular |
| H. pylori positivo | Consulta médica para decidir tratamiento | — |
| Anti-HBs no protector | Preguntar por la vacuna de hepatitis B | — |

# **07.8 — Entrega**

- **Dashboard:** todas las recomendaciones, agrupadas por tipo.
- **WhatsApp:** una por semana durante 8 semanas, empezando por la de mayor prioridad. En el piloto, el médico aprueba cada mensaje.
- **Seguimiento:** si hay Apple Watch, se mide si cambian pasos y sueño; si no, se pregunta una vez por mensaje si la pudo aplicar.
