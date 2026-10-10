## COND-M4-IN-001 · Hepatitis C

**Qué detecta.** Anti-VHC reactivo. El laboratorio corre ARN viral como refleja: detectable indica infección activa; no detectable indica infección resuelta o un falso positivo del anticuerpo. Por decisión del equipo se mide a todos con el consentimiento de la visita. Un reactivo lo comunica el médico por llamada.

```yaml
id: COND-M4-IN-001
nombre: Hepatitis C
modulo: M4
especialidad: infectologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: anti_vhc_reactivo
    biomarcador: anti_hcv
    condicion: "reactivo"
  - id: arn_detectable
    biomarcador: hcv_rna
    condicion: "detectable"
  - id: arn_no_detectable
    biomarcador: hcv_rna
    condicion: "no detectable"
regla_central: "anti_vhc_reactivo"
variantes:
  infeccion_activa: "anti_vhc_reactivo AND arn_detectable"
  resuelta_o_falso_positivo: "anti_vhc_reactivo AND arn_no_detectable"
  pendiente: "anti_vhc_reactivo AND ARN aún no reportado"
coincidencia:
  alta: "infeccion_activa"
  moderada: "pendiente"
  baja: "resuelta_o_falso_positivo"
escalamiento: 2
canal: "llamada del médico; el informe no se publica antes de la llamada; nunca por WhatsApp"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["Minsalud, tamización de hepatitis C", "USPSTF 2020"]
por_verificar: "Lineamiento del Ministerio leído solo por resultado de búsqueda."
frase_permitida_activa: "Tu prueba de hepatitis C salió positiva y el virus está activo. Hoy existe tratamiento que la cura en la mayoría de personas. Nuestro médico te explicará los pasos a seguir."
frase_permitida_resuelta: "Tu prueba de anticuerpos de hepatitis C salió reactiva, pero el virus no está activo. Puede ser una infección pasada ya resuelta; tu médico te explicará qué significa."
frases_prohibidas: ["tienes cirrosis", "es incurable", "contagias a tu familia"]
recomendaciones_sugeridas: ["consulta con el médico tratante para tratamiento", "no compartir objetos con sangre (cuchillas, cepillos)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Activa | Anti-VHC reactivo, ARN detectable | Activa, coincidencia alta, escalamiento 2, llamada |
| Resuelta | Anti-VHC reactivo, ARN no detectable | Activa, coincidencia baja, llamada con texto de resuelta |
| Pendiente | Anti-VHC reactivo, ARN en proceso | Informe en espera; llamada cuando llegue el ARN |
| Negativo · PDF ejemplos | Anti-VHC no reactivo | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
