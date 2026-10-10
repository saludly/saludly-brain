# Fase 5: decisiones clínicas para que Carlos revise

**10 de octubre de 2026.** Al escribir los textos para el paciente, las recomendaciones y las recetas se tomaron estas decisiones, que no estaban escritas en las fichas. Todas quedaron marcadas `estado_revision: pendiente` y se pueden cambiar en `knowledge_base/fase5/` sin tocar código.

## Textos para el paciente (`knowledge_base/fase5/redaccion/`)

1. **Hepatitis C:** la ficha decía que el tratamiento "la cura", pero el control de salida prohíbe "cura". Quedó "hoy existen tratamientos muy efectivos".
2. **Hepatitis B:** ahora hay un texto por estado (vacunado, susceptible, infección pasada, anti-HBc aislado e infección activa). El vacunado aparece en "Lo que está bien". La frase de la ficha "No tienes defensas…" choca con una frase prohibida de la misma ficha y no se usó.
3. **Homocisteína (NU-A01) y PTH alta con calcio normal (NU-A02):** las fichas solo tenían texto para el médico; el texto para el paciente es propuesta.
4. ✅ **Potasio alto (NE-004), aprobado por Carlos (10 de octubre):** se nombra el corazón ("podría alterar el ritmo del corazón y la fuerza de los músculos"). Sigue prohibido "riesgo de arritmia" como conclusión sin bandera crítica.
5. **Hipotiroidismo subclínico (TI-001):** la frase extra para mujeres que buscan embarazo no tiene lugar todavía (el formato no tiene textos por sexo o edad).
6. **Niveles severos** (triglicéridos muy altos, glucosa muy baja, presión muy alta): las fichas tienen frases propias para ellos; hoy se usa el texto general más el plazo del escalamiento. Solo el cortisol bajo trae los signos de urgencia.
7. **Valores que no se pueden insertar todavía:** el porcentaje de SCORE2, la cantidad de componentes del síndrome metabólico, el puntaje FINDRISC y la relación aldosterona/renina. Los textos los mencionan de forma general.
8. **Apoyos que solo ve el médico** (lectura por edad, edad biológica, testosterona libre, PSA libre/total) tienen texto de paciente por si un día se muestran.
9. **Ficha de parasitosis (IN-A02):** usa el biomarcador `stool_parasites`, que no existe en el índice (el que existe es `stool_exam`). Está en pausa en el MVP.

## Recomendaciones (`knowledge_base/fase5/recomendaciones/`, 189)

10. ✅ **Aprobado por Carlos (10 de octubre).** **Ejercicio intenso:** con riesgo cardiovascular, sospecha de presión alta, hipertiroidismo, cortisol bajo, anemia, plaquetas bajas o dos líneas bajas, se pide consulta antes de entrenar fuerte, en cualquier nivel de escalamiento (conservador para el nivel 1).
11. **Sal y agua:** con sodio bajo, cortisol bajo o riesgo de insuficiencia cardíaca no se recomienda "reducir sal" ni "tomar más agua". Con enfermedad renal solo "sigue la indicación de tu médico".
12. **Magnesio:** los alimentos ricos en magnesio quedan contraindicados con potasio alto (también traen potasio), y el suplemento, con enfermedad renal.
13. **Elastografía hepática:** se sugiere hablarla con el médico cuando el FIB-4 está alto o indeterminado (EASL 2024, AASLD 2023); no está en la ficha.
14. **Plazos de cita** ("pide la cita en N semanas"): son propuesta; los de repetir exámenes salen de las fichas.
15. **Fuentes por verificar:** GPC Colombia de HTA 2025, ESHRE de insuficiencia ovárica 2024, Lancet Commission on Dementia 2024, consenso de hiponatremia por ejercicio 2015, Wilderness Medical Society, AASM/SRS 2015 y CDC ACIP 2022.

## Nutrición y recetas (`knowledge_base/fase5/recetas/`)

16. ✅ **Tabla de alimentos (140), verificada el 10 de octubre a pedido de Carlos.** 112 vienen de USDA FoodData Central. De los 27 aproximados, 25 se verificaron: 15 con la Tabla de Composición de Alimentos Colombianos del ICBF (TCAC 2015) y 10 con USDA SR Legacy. Quedan aproximadas la granola sin azúcar (no está en la TCAC) y la arracacha cocida (la TCAC solo trae la cruda). Decisiones tomadas al verificar, escritas en la `fuente` de cada alimento: pollo y res magra con USDA, porque los valores de la TCAC no parecen crudos ni magros; merluza con el potasio anterior (la TCAC da 34 mg, que no es creíble, y analiza otra especie); yuca y caldo con el sodio anterior (los valores de las tablas parecen cocidos con sal); tomate de árbol con el potasio del segundo análisis de la TCAC (280 mg, en vez de 94 mg); feijoa completa con USDA; la TCAC no trae azúcares, así que esos valores siguen aproximados. Cambios grandes: la gelatina sin azúcar baja de 55 a 15,7 g de proteína por 100 g de polvo y la mayonesa light sube de 9 a 32 g de carbohidratos.
17. **Recetas (190):** 45 desayunos, 35 meriendas, 60 almuerzos y 50 cenas, escritas por Saludly. Solo dos llevan panela.
18. **Metas diarias:** Mifflin-St Jeor × actividad (ligera por defecto), −15 % para bajar de peso, +10 % para objetivos deportivos; proteína de 1,0 g/kg (general), 1,2 (bajar de peso, envejecer, mayores de 65), 1,4 (rendimiento y maratón) o 1,6 (masa muscular y atlético), con tope de 0,8 g/kg si la TFG es menor de 60. Grasa al 28 %, grasa saturada por debajo del 10 %, sodio por debajo de 2.000 mg y azúcar añadido por debajo del 10 % de las calorías (OMS).
19. **Restricciones por hallazgo:** glucosa alta → sin azúcar añadida; presión o riñón → bajas en sodio (≤ 600 mg por comida); potasio alto o TFG < 30 → sin recetas altas en potasio; lípidos o hígado → poca grasa saturada; hierro bajo → se prefieren fuentes de hierro; sobrecarga de hierro o ácido úrico alto → sin vísceras ni sardinas.
20. ✅ **Nivel de actividad, decisión de Carlos (10 de octubre):** lo responde el **paciente en la PWA** (sedentario, ligero, moderado o alto) junto con sus objetivos y la biotina. Si no responde, se asume "ligero" y el informe lo dice.
