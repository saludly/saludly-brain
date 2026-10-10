**SALUDLY BRAIN**

**05 — Seguridad, límites y escalamiento**

*Qué nunca hace Saludly Brain, cómo escala y cómo protege los datos · versión 1 · 6 de octubre de 2026*

> Las reglas clínicas de este documento las definió Claude por encargo del equipo de Saludly. Antes de usarse con pacientes reales necesitan la firma de un médico.

# **05.1 — Límites del producto**

1. No diagnostica: ningún texto dice "tienes", "padeces" o "eres" seguido de una enfermedad.
2. No prescribe: no nombra medicamentos para tomar ni da dosis de suplementos.
3. No reemplaza al médico tratante ni sugiere suspender un tratamiento.
4. No usa el wearable como prueba: el reloj aporta contexto, no detecta enfermedades.
5. No calcula porcentajes de riesgo sin un modelo clínico validado (SCORE2-PURE solo entre 40 y 69 años).
6. No inventa umbrales de urgencia: lo crítico sale del laboratorio o de una guía escrita.
7. No responde preguntas fuera de los resultados del paciente y sus recomendaciones.

# **05.2 — Lenguaje**

| Prohibido | En su lugar |
| :---- | :---- |
| "Tienes diabetes" | "Tus resultados de glucosa están en el rango que las guías usan para diagnosticar diabetes. Un médico debe confirmarlo." |
| "Tienes hígado graso" | "El conjunto de resultados es compatible con una alteración hepática de origen metabólico. Conviene confirmarlo con tu médico." |
| "Tienes Hashimoto" | "Tu TSH está alta y tus anticuerpos tiroideos son positivos. Ese patrón merece una consulta." |
| "Tienes deficiencia de hierro" | "Tus reservas de hierro están bajas." |
| "Toma 2.000 UI de vitamina D" | "Tu vitamina D está por debajo del rango. Te contamos qué alimentos la aportan; si quieres suplementarla, consúltalo con tu médico." |
| "El reloj detectó una enfermedad" | "Tu reloj registra una frecuencia en reposo más alta que tu promedio; lo tenemos en cuenta como contexto." |
| "Tu riesgo de infarto es del 12 %" (sin modelo validado) | Los factores de riesgo, sin porcentaje |
| "Todo está normal, estás sano" | "Estos resultados están dentro de los rangos de referencia." |
| "Es grave" / "no es nada" | El nivel de escalamiento y el paso siguiente |

La lista completa de frases prohibidas vive en el Knowledge Base y la usa el control de salida.

# **05.3 — Protocolo de escalamiento**

| Nivel | Quién actúa | Cómo se comunica | Plazo |
| :---- | :---- | :---- | :---- |
| 0 | Nadie | Dashboard y WhatsApp | — |
| 1 | El paciente, en su próximo control | Dashboard y WhatsApp, con sugerencia de comentarlo | Próximos 3 meses |
| 2 | Médico de Saludly revisa; el paciente pide consulta | Dashboard con explicación; WhatsApp solo con aviso general ("hay un resultado que conviene revisar con un médico") | Próximas 2 a 4 semanas |
| 3 | Equipo médico de Saludly | Llamada telefónica; el informe no se publica hasta que el médico hable con el paciente | Mismo día hábil |

Ningún resultado de nivel 3 ni ninguna serología reactiva (hepatitis B, hepatitis C, Chagas) llega primero por WhatsApp.

# **05.4 — Reglas especiales**

| Situación | Regla |
| :---- | :---- |
| Bandera crítica del laboratorio | Nivel 3 |
| Troponina de alta sensibilidad por encima del percentil 99 | Nivel 3, siempre; con dolor de pecho o falta de aire, indicar urgencias |
| Glucosa menor de 54 mg/dL | Nivel 3 si la muestra se procesó a tiempo; si hubo demora, repetir (posible falso bajo) |
| Potasio alto | Nunca escalar con un valor hemolizado o aislado; repetir, salvo bandera crítica |
| Biotina alta o suplemento declarado | No interpretar TSH, T4 libre, B12 ni folato; repetir sin el suplemento |
| Cortisol y ACTH | Sin patrones propios; no se nombran Cushing ni Addison; interpretación de ACTH solo para el médico |
| Hormonas del ciclo | Solo con fecha de última menstruación y sin anticonceptivo hormonal ni embarazo |
| PSA | Requiere consentimiento en la visita; fuera de 50 a 75 años, "valor a revisar con tu médico" |
| Prolactina alta | Siempre se repite; nunca se habla de tumor |
| ANA | Título y patrón obligatorios; desde 1:160 o patrón distinto del moteado fino, nivel 2 |
| Serologías reactivas | Nivel 2 con llamada del médico |
| Sangre oculta positiva | Nivel 2: remisión para colonoscopia |
| Embarazo declarado | Solo reglas validadas para embarazo; el resto, "no interpretable" |
| Paciente menor de 18 años | Fuera del alcance de la versión 1 |
| Vitaminas A y E altas | Sugerir consulta y revisar suplementos |
| Vitamina C sin transporte congelado validado | No se clasifica |

# **05.5 — Privacidad y datos**

- **Consentimiento.** La enfermera recoge en la visita la autorización expresa para tratar datos de salud (Ley 1581 de 2012), la autorización para enviar datos seudonimizados a proveedores de IA fuera de Colombia (aprobada por el abogado de Saludly), el consentimiento del PSA y el de wearables cuando aplique.
- **Seudonimización.** Al modelo de lenguaje solo viajan edad, sexo, objetivo, valores y contexto, con un identificador interno. Nombre, documento, teléfono y dirección nunca salen del servidor de Saludly.
- **Mínimo necesario.** Cada rol ve solo lo que necesita: el paciente su informe; la enfermera su formulario; operaciones el estado de los PDF; el médico la vista clínica.
- **Registro.** Toda lectura y cambio queda registrado: quién, qué y cuándo.
- **Retención.** PDF y resultados se conservan según la normativa de historia clínica; los datos de wearables, mientras el consentimiento esté vigente.
- **Revocación.** Si el paciente desconecta Apple Health o revoca un consentimiento, el uso se detiene desde ese momento.

# **05.6 — Seguridad técnica**

- Servidor en Hostinger con SSH solo por llave, firewall, Fail2Ban y panel de OpenClaw sin exposición pública.
- Cifrado en tránsito (HTTPS) y en reposo para la base de datos y los PDF.
- Llaves de API en variables de entorno o gestor de secretos, nunca en el código.
- Ninguna skill de OpenClaw de terceros sin revisión.
- Copias de seguridad diarias, probadas una vez al mes.
- Ambientes separados: desarrollo y pruebas solo con datos sintéticos (como los PDF de ejemplo); producción con datos reales.

# **05.7 — Supervisión humana**

- En el piloto, el médico aprueba el 100 % de los informes y mensajes.
- Después del piloto, el médico aprueba todo nivel 2 y 3; el resto se audita por muestreo.
- Cada desacuerdo del médico con el motor se registra y vuelve como caso de prueba.

# **05.8 — Incidentes**

Un incidente es cualquier resultado entregado al paciente equivocado, un hallazgo falso de nivel 2 o 3, un nivel 3 no comunicado a tiempo o una fuga de datos. Ante un incidente: se detiene el envío automático, se avisa al médico responsable y al paciente afectado, se corrige, se agrega el caso a las pruebas y se registra la causa.

# **05.9 — Pendiente regulatorio**

Si el INVIMA clasificaría a Saludly Brain como dispositivo médico (software) sigue sin consultarse. Debe resolverse antes del piloto.
