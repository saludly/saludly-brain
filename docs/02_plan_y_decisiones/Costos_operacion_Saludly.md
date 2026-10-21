# Costo de operar Saludly (estimación técnica)

Estimación del 12 de octubre de 2026. **Todos los precios son provisionales.** Antes de presupuestar hay que confirmarlos en la página oficial de cada proveedor y actualizar este documento.

Tasa de cambio supuesta: **$4.000 COP por dólar** (provisional).

## 1. Costos fijos mensuales (no dependen del número de pacientes)

| Componente | Para qué | Estimado (USD/mes) | Estado |
|---|---|---|---|
| VPS DonWeb (4 vCPU, 8 GB de RAM) | OpenClaw, motor, pipeline y Ollama (bge-m3) | 30 – 60 | Precio por confirmar en donweb.com |
| Segundo servidor o respaldo (pruebas y recuperación) | Para no caerse en producción | 15 – 60 | Recomendado |
| Supabase Pro | Base vectorial de la KB y datos de la app | 25 – 75 | Confirmar región (habeas data, Ley 1581) |
| Hosting del dashboard y la PWA (p. ej. Vercel Pro) | Dashboard del médico y app del paciente | 0 – 20 | Depende de dónde se publique |
| Correo transaccional (envío del informe) | Correos al paciente | 0 – 20 | |
| Monitoreo y registro de errores | Saber cuándo algo falla | 0 – 26 | |
| Copias de seguridad y almacenamiento | Respaldos cifrados | 5 – 20 | |
| Dominio y certificado | saludly… | ~2 | |
| **Total fijo** | | **~80 – 300 (≈ $0,3 a $1,2 millones COP)** | Se usa 200 USD como punto medio |

## 2. Costos variables por paciente

### DeepSeek (`deepseek-v4-pro`)

Tarifa de lista reportada en 2026 (por confirmar en la página oficial): **US$1,74 por millón de tokens de entrada, US$0,0145 si están en caché y US$3,48 por millón de salida.** La promoción del 75% terminó el 31 de mayo de 2026.

| Uso | Tokens supuestos | Costo |
|---|---|---|
| Redactar un informe (paciente, vista médica y resumen de WhatsApp) | ~10.000 de entrada nuevos + ~15.000 en caché (instrucciones fijas) + ~6.000 de salida | ~US$0,04 |
| Reintentos por el control de salida (30% más) | | ~US$0,01 |
| Preguntas del paciente al agente (5 conversaciones al año) | ~8.000 de entrada + ~1.000 de salida cada una | ~US$0,09 |
| **Total al año por paciente** | | **~US$0,05 a 0,15 ≈ $200 a $600 COP** |

Los embeddings del RAG se hacen con Ollama en el VPS, así que no tienen costo por uso.

### WhatsApp Business Platform

Meta cobra por mensaje de plantilla. Tarifa de referencia en Colombia para mensajes de **marketing: ~US$0,0125** (fuente de un proveedor; confirmar en la tabla oficial de Meta). Los mensajes de **utilidad** (avisos, "tu informe está listo") son más baratos. Las respuestas dentro de las 24 horas siguientes a un mensaje del paciente son gratis.

| Envío | Mensajes al año | Costo al año por paciente |
|---|---|---|
| Receta diaria (si Meta la clasifica como marketing) | 365 | **~US$4,6 ≈ $18.250 COP** |
| Receta 3 veces por semana | 156 | ~US$2,0 ≈ $7.800 COP |
| Receta semanal | 52 | ~US$0,65 ≈ $2.600 COP |
| Avisos del informe y recordatorios (utilidad) | ~5 | ~$200 COP |

**La receta diaria por WhatsApp es, de lejos, el gasto técnico más grande por paciente.**

## 3. Costo técnico por paciente al año

Con 200 USD/mes de costos fijos y un informe al año por paciente:

| Pacientes al año | Fijo por paciente | Con receta diaria | Con receta semanal |
|---|---|---|---|
| 1.000 | $9.600 | **~$28.500** | ~$12.800 |
| 10.000 | $960 | **~$19.800** | ~$4.200 |
| 100.000 | $96 | **~$18.900** | ~$3.300 |

## 4. Costos que no son técnicos (no están sumados arriba)

- **Revisión médica:** si un médico dedica unos 3 minutos a cada informe, a unos $80.000 la hora, son ~$4.000 por informe. Es el costo humano más probable.
- Soporte al paciente y a la EPS.
- Asesoría legal: INVIMA (software como dispositivo médico), habeas data y contratos con EPS.
- Seguro de responsabilidad.
- La toma de presión, cintura, peso y talla por la enfermera: hay que definir quién la paga.
- Ventas y gestión comercial.

## 5. Conclusión

- La infraestructura y DeepSeek cuestan poco: menos de $1.000 por paciente al año cuando hay volumen.
- Lo que mueve el costo es **WhatsApp**: la receta diaria por sí sola cuesta unos $18.000 por paciente al año. Frente a una tarifa a la EPS de $25.000 a $40.000, se come la mitad o más del ingreso.
- Opciones: receta semanal o 3 veces por semana; mostrar la receta en la PWA y usar WhatsApp solo para avisar; o cobrar la receta diaria como servicio aparte.
- Con receta semanal y 10.000 pacientes, el costo técnico es de ~$4.000, y con revisión médica ~$8.000 por paciente al año.

## Pendiente de confirmar

- Precio real del plan de DonWeb, en dólares o pesos colombianos.
- Tarifa vigente de DeepSeek en su página oficial.
- Tarifa de Meta para Colombia y en qué categoría queda la receta diaria (marketing o utilidad).
- Región de Supabase y si es necesario aplicar el régimen de transferencia internacional de datos (Ley 1581).
- Tasa de cambio del momento.
