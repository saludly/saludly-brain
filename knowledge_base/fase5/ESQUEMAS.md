# Fase 5 · Formatos de redacción, recomendaciones y recetas

**10 de octubre de 2026.** Todo lo de esta carpeta es contenido para el paciente: lo lee el código (`codigo/informe/`) y lo revisa Carlos, que hace de médico. Se valida con `python codigo/herramientas/validar_fase5.py`.

## Reglas de lenguaje (valen para todo)

1. **Nunca diagnosticar.** Prohibido "tienes…", "padeces…", "sufres de…", "eres diabético", "estás enfermo". En su lugar: "tu resultado está en el rango que las guías usan para…", "este patrón es compatible con…", "conviene confirmarlo con tu médico".
2. **Idioma paciente.** Español de Colombia, de tú, frases cortas (máximo unas 25 palabras), sin jerga. Si un término importa, se explica en la misma frase ("la ferritina, que es la reserva de hierro de tu cuerpo").
3. **Riesgo claro, sin alarmismo y sin falsa tranquilidad.** Decir qué puede pasar si no se atiende, en general y sin porcentajes ("con los años puede dañar los vasos sanguíneos"). Nada de "es grave" ni "no es nada".
4. **Un ejemplo simple y cotidiano**, una analogía que entienda cualquier persona ("es como una tubería que se va tapando con grasa").
5. **Sin dosis, sin marcas, sin prescripciones.** Nada de "toma 2.000 UI", "mg", "tabletas". Los suplementos solo como opción general para hablar con el médico.
6. **Sin porcentajes de riesgo** que no vengan de un modelo validado.
7. **Sin nombres de enfermedades graves como conclusión** (cáncer, leucemia, mieloma, cirrosis, infarto…). Pueden aparecer solo en la vista médica.

## 1. Redacción por hallazgo · `redaccion/<ID>.yaml`

Un archivo por cada hallazgo que puede llegar al paciente: condiciones incluidas, apoyos informativos, patrones y reglas de seguridad.

```yaml
id: COND-M1-EM-001                  # igual al de la ficha
tipo: condicion                     # condicion | patron | seguridad | informativa
titulo_paciente: "Glucosa en zona de alerta"
que_es: "La glucosa es el azúcar que circula en tu sangre y le da energía al cuerpo."
por_que_te_aparece:                 # lista de frases; cada una puede usar {biomarker_id} y se omite si falta ese valor
  - "Tu glucosa en ayunas salió en {glucose}, por encima de 100 mg/dL."
  - "Tu hemoglobina glicada, que muestra el promedio de azúcar de los últimos 3 meses, salió en {hba1c}."
riesgo_claro: "Si se mantiene así durante años, aumenta la probabilidad de llegar a diabetes, que con el tiempo afecta el corazón, los riñones y la vista."
ejemplo_simple: "Es como una alarma de humo que suena antes del incendio: avisa a tiempo para actuar."
incertidumbre: "Un solo examen no basta para confirmarlo; tu médico puede pedir repetirlo."
cuando_consultar: null              # opcional: texto propio; si es null se usa el del nivel de escalamiento
aviso_whatsapp: null                # opcional: aviso general sin datos clínicos (solo escalamiento 0 o 1)
fuentes: ["ADA Standards of Care 2025"]
estado_revision: pendiente          # pendiente | aprobada (la aprueba Carlos)
```

- Los marcadores `{...}` solo pueden ser identificadores de biomarcador del Knowledge Base o de los calculados (`homa_ir`, `egfr`, `hemoglobina_ajustada`, `calcio_corregido`, `tyg_index`, `fib4`, `indice_androgenos_libres`, `testosterone_free`, `phenoage`, `non_hdl_c`, `transferrin_saturation`, `mentzer_index`, `nlr`, `tg_hdl_ratio`, `globulin`, `ag_ratio`, `imc`) y las medidas de la enfermera (`presion_sistolica`, `presion_diastolica`, `cintura_cm`, `peso_kg`, `talla_m`). El código los reemplaza por "valor unidad" y, cuando hay varias frases, deja solo las que nombran valores fuera de rango.
- `redaccion/modulos.yaml` tiene los textos de **lo que está bien**, por grupo de biomarcadores.

## 2. Recomendaciones · `recomendaciones/<tipo>.yaml`

Una lista por tipo: `alimentacion`, `hidratacion`, `actividad`, `sueno`, `habitos`, `actividades_saludables`, `vitaminas_suplementos`, `terapias`, `controles`.

```yaml
- id: REC-ALI-001
  tipo: alimentacion
  titulo: "Cambia las bebidas azucaradas por agua"
  texto_base: "Reemplaza gaseosas, jugos de caja y bebidas endulzadas por agua, agua con limón o aromáticas sin azúcar."
  meta_concreta: "Esta semana, cero bebidas azucaradas en el almuerzo."
  por_que: "Las bebidas azucaradas suben la glucosa rápido y no quitan el hambre."
  se_activa_con: ["COND-M1-EM-001", "COND-M1-EM-003", "COND-M1-EM-A04"]   # IDs de condición o relación, "ID#estado" (hepatitis B: COND-M4-IN-002#susceptible), "biomarcador:clase", "objetivo:<id>" o "general"
  prioriza_objetivos: ["bajar_peso", "prevenir", "salud_general"]
  contraindicada_si: []             # IDs o "biomarcador:clase" que la impiden
  requiere_consulta_previa: false   # true: el texto dice primero consultar (por ejemplo, ejercicio intenso con anemia)
  whatsapp: "💧 Hoy cambia la gaseosa del almuerzo por agua o limonada sin azúcar. Tu glucosa te lo agradece."
  fuentes: ["ADA Standards of Care 2025, sección 5"]
```

Objetivos válidos (`objetivos.yaml`): `salud_general`, `prevenir`, `condicion_existente`, `bajar_peso`, `masa_muscular`, `rendimiento`, `maraton`, `atletico`, `energia_sueno`, `envejecer_saludable`.

## 3. Recetas · `recetas/alimentos.yaml` y `recetas/<grupo>.yaml`

**Tabla de alimentos** (valores por 100 g de porción comestible, de la tabla del ICBF o de USDA FoodData Central):

```yaml
- id: arroz_blanco_cocido
  nombre: "Arroz blanco cocido"
  grupo: cereales                   # cereales | tuberculos_platanos | leguminosas | verduras | frutas | lacteos | huevos | carnes | pescados | grasas | frutos_secos | azucares | otros
  por_100g: {kcal: 130, proteina_g: 2.7, grasa_g: 0.3, grasa_saturada_g: 0.1, carbohidratos_g: 28.2, fibra_g: 0.4, azucares_g: 0.1, sodio_mg: 1, potasio_mg: 35, hierro_mg: 0.2, calcio_mg: 10}
  medida_casera: {nombre: "taza", gramos: 160}
  etiquetas: [vegano, sin_gluten, sin_lactosa]
  fuente: "USDA FDC SR Legacy 168878 (aproximado)"
```

**Receta** (los nutrientes NO se escriben: los calcula el código con la tabla):

```yaml
- id: RCT-DES-001
  nombre: "Calentado de fríjol con huevo"
  tiempo_comida: desayuno           # desayuno | almuerzo | cena | merienda
  porciones: 2
  tiempo_min: 20
  dificultad: facil                 # facil | media
  ingredientes:
    - {alimento: frijol_rojo_cocido, gramos: 200, medida: "1 taza"}
    - {alimento: huevo_entero, gramos: 100, medida: "2 huevos"}
  pasos:
    - "Calienta el fríjol cocido con un poco de cebolla y tomate picados."
    - "Revuelve los huevos y sírvelos encima."
  etiquetas: [colombiana, vegetariano]   # vegetariano | vegano | sin_lactosa | sin_gluten | colombiana | economica | rapida
  consejo: "Acompaña con una fruta con vitamina C para absorber mejor el hierro del fríjol."
```

- Las recetas son de Saludly: se escriben con palabras propias, no se copian de libros ni de sitios web.
- La sal y el azúcar que se agreguen van como ingredientes (`sal`, `azucar`, `panela`), para que el código las cuente.
- Las etiquetas nutricionales (alta en proteína, baja en sodio, sin azúcar añadida, fuente de hierro…) y las restricciones por condición las calcula el código.
