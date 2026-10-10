# Lector del PDF de resultados · Saludly Brain · Fase 3 · versión 1

Lee el PDF del laboratorio, verifica que corresponda a la visita, extrae cada resultado con sus metadatos,
lo normaliza al identificador del Knowledge Base y marca lo dudoso. No interpreta resultados ni inventa datos.

## Requisitos
Python 3.10 o superior, `pdfplumber` y `pyyaml`. Para la prueba del PDF mezclado, `qpdf`.

    pip install pdfplumber pyyaml

## Uso

    python lector.py ARCHIVO.pdf --visita visita.json --indice 00_INDEX.json --conversiones unidades.yaml --salida salida.json

- `visita.json`: documento y número de orden de la visita agendada, por ejemplo `{"documento": "CC 0000000002", "orden": "LCD-2026-100124"}`.
- `00_INDEX.json`: índice del Knowledge Base (trae los sinónimos y las unidades canónicas).
- `unidades.yaml`: conversiones permitidas hacia la unidad canónica. Ninguna conversión se hace fuera de esta tabla.
- Código de salida: 0 si el PDF se aceptó, 2 si se rechazó.

## Qué hace, en orden
1. Calcula la huella SHA-256 del archivo.
2. Lee el encabezado de **todas** las páginas y rechaza el PDF si el documento o la orden no coinciden con la visita, o si hay páginas de otro paciente.
3. Compara los metadatos del PDF con el encabezado impreso.
4. Detecta secciones, muestras y columnas, y lee cada fila: nombre, resultado, indicador, unidad, intervalo, método.
5. Normaliza el nombre con el diccionario de sinónimos. **Solo acepta coincidencias exactas**: un nombre parecido puede ser otra prueba.
6. Interpreta el resultado en uno de seis estados: medido, menor que el límite, mayor que el límite, cualitativo, inválido o no medido.
7. Interpreta el intervalo: bajo y alto, límites con < o ≥, fase del ciclo, notas y "No establecido".
8. Compara la unidad con la canónica; si difiere, convierte solo con una regla de `unidades.yaml` o deja la duda.
9. Marca dudas: nombre no reconocido, unidad sin regla, duplicados, resultado inválido y observaciones del laboratorio (*).
10. Extrae las observaciones del final del informe.

## Pruebas

    python pruebas/probar.py      # compara con los casos de punta a punta y prueba rechazos
    python pruebas/variante.py    # PDF con errores sembrados

## Formato soportado
`saludly-demo-v1`, el PDF de ejemplo de Saludly. Cuando el laboratorio aliado entregue su formato real,
se ajustan las constantes de `FORMATO` en `lector.py` y se repiten las pruebas.
