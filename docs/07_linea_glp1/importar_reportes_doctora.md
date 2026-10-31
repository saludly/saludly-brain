# Importar los reportes de la doctora (PDF) · propuesta

31 de octubre de 2026. Idea de Carlos: en vez de que la doctora o la paciente escriban a mano el peso al inicio, la meta, las medidas de cada control y los exámenes, leerlos del reporte que la doctora ya genera (historia clínica, software médico o PDF propio) y llenar la ficha de la paciente sola.

Estado: **idea por validar con la primera doctora.** No se construye hasta ver cómo documenta ella.

## Por qué vale la pena

- La doctora no escribe dos veces: lo que ya anotó en su historia llega a Saludly.
- Los datos de la paciente quedan con el respaldo de un documento clínico, no de memoria.
- Es la misma tecnología que ya tenemos: el lector del PDF del laboratorio (`codigo/lector_pdf/`) lee tablas, valores y fechas con reglas fijas.

## Qué se podría sacar de cada tipo de documento

| Documento | Datos que traería | Para qué en Saludly |
|---|---|---|
| Historia clínica o nota de control (PDF del software de la doctora) | Fecha, peso, talla, IMC, cintura, presión, medicamento y dosis, meta acordada | Llenar y confirmar el tratamiento y los registros de cada control |
| Orden de laboratorio | Exámenes que pidió | Mostrarle a la paciente solo esos exámenes (como pidió Carlos) |
| Resultado del laboratorio (ECOFAM u otro) | Valores, unidades, rangos, fecha de toma, número de orden | El análisis del motor (ya funciona con el PDF de ejemplo) |
| Fórmula médica | Medicamento, dosis, frecuencia | El recordatorio de aplicación (sin sugerir dosis) |
| Reporte de báscula de bioimpedancia, si la usa | Grasa, músculo, agua | Gráficas más precisas que la grasa estimada por cintura |

**Metadatos útiles del PDF:** fecha de creación, programa que lo generó y número de documento de la paciente. Sirven para saber de qué software viene, poner la fecha correcta y comprobar que el PDF es de esa paciente, igual que hoy con el laboratorio.

## Cómo funcionaría

```
Doctora sube el PDF en la ficha de la paciente (o lo reenvía por correo)
   → El lector identifica el formato (por el programa que lo generó y su encabezado)
   → Extrae los campos con reglas fijas de ese formato (nunca un LLM adivinando números)
   → Compara el documento de identidad con el de la paciente
   → Muestra a la doctora "Esto encontramos" con cada dato para confirmar o corregir
   → Al confirmar, se guarda en el tratamiento y en los registros (registrado_por = doctora)
   → El PDF se borra después de leerlo, como el del laboratorio
```

Reglas que se mantienen:

- **No se inventan datos.** Un campo que no se lee con seguridad queda vacío y marcado, nunca en cero.
- **La doctora confirma antes de guardar**: nada importado cambia la ficha sin su clic.
- **Datos sensibles** (Ley 1581): la doctora es la responsable de los datos de sus pacientes y Saludly es encargada. Hace falta el contrato de transmisión de datos y la autorización de la paciente (ya la pedimos en el registro).

## Qué hay que preguntarle a la doctora en el onboarding

1. ¿En qué programa lleva la historia clínica? (software médico, Excel, Word, papel)
2. ¿Ese programa exporta la nota de cada control en PDF? ¿También en Excel o CSV?
3. ¿Qué anota en cada control: peso, cintura, IMC, presión, bioimpedancia, dosis?
4. ¿Cada cuánto ve a la paciente y cada cuánto pide exámenes? ¿Cuáles pide?
5. ¿Nos puede dar 2 o 3 reportes de ejemplo **con los datos personales tapados** para armar el lector de su formato?
6. ¿Prefiere subir el PDF en el panel o reenviarlo a un correo de Saludly?

## Esfuerzo y orden

1. Con los ejemplos de la doctora, un lector para **su** formato (por programa: 1 a 2 días cada uno).
2. Pantalla "Esto encontramos" en la ficha para confirmar.
3. Después, el correo de Saludly que recibe los PDF reenviados (más cómodo para ella).

Si la doctora lleva la historia en papel o en Word sin estructura, esta idea no conviene: se queda el registro a mano en el panel, que ya funciona.
