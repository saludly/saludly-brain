"""Pruebas del comando de punta a punta y del informe (Fase 5): PDF → lector → motor → informe, WhatsApp y recetas."""
import copy, json, os, sys
B = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(B)))
sys.path.insert(0, os.path.dirname(B))
import saludly
import contenido, nutricion as NU, control_salida as CS

PDF = {"H": (os.path.join(RAIZ, "pdf_ejemplo", "Ejemplo_resultados_LCD-2026-100123_hombre.pdf"), "CC 0000000001", "LCD-2026-100123"),
       "M": (os.path.join(RAIZ, "pdf_ejemplo", "Ejemplo_resultados_LCD-2026-100124_mujer.pdf"), "CC 0000000002", "LCD-2026-100124")}
ENF_H = dict(presion_sistolica=128, presion_diastolica=82, cintura_cm=98, peso_kg=86, talla_m=1.74, tabaquismo=False)
ENF_M = dict(presion_sistolica=112, presion_diastolica=72, cintura_cm=78, peso_kg=58, talla_m=1.62, tabaquismo=False, fecha_ultima_menstruacion="2026-09-20", anticonceptivo_hormonal=False)
fallos, pasan = [], 0
def chk(ok, msg):
    global pasan
    if ok: pasan += 1
    else: fallos.append(msg)

def correr(k, objetivos=("bajar_peso", "energia_sueno", "prevenir"), biotina=False, enf=None, actividad="ligero", **kw):
    pdf, doc, orden = PDF[k]
    perfil = dict(objetivos=list(objetivos), toma_biotina=biotina) | ({"nivel_actividad": actividad} if actividad else {})
    return saludly.generar(pdf, doc, orden, perfil, enf if enf is not None else (ENF_H if k == "H" else ENF_M), **kw)

def textos_paciente(inf):
    p = inf["paciente"]; t = [p["resumen"]]
    for a in p["lo_que_merece_atencion"]: t += [a["titulo"], a["que_es"], a["ejemplo"]] + a["por_que"]
    for s in ("que_podria_significar", "que_puedes_hacer", "cuando_consultar", "lo_que_esta_bien", "informativos"):
        for x in p[s]: t += [v for v in x.values() if isinstance(v, str)]
    w = inf["whatsapp"]; t += [x for x in (w["resultado_listo"], w["recordatorio_consulta"]) if x] + [x["texto"] for x in w["recomendaciones_semanales"] + w["recetas_diarias"]]
    return t

C = contenido.cargar()
# 1) Los dos PDF de ejemplo
for k in ("H", "M"):
    cod, inf = correr(k)
    chk(cod == 0, f"{k}: código {cod} ({inf.get('motivo')})")
    if cod: continue
    p = inf["paciente"]
    chk(all(s in p for s in ("resumen", "lo_que_esta_bien", "lo_que_merece_atencion", "que_podria_significar", "que_puedes_hacer", "cuando_consultar")), f"{k}: faltan secciones")
    chk(not inf["control_salida"]["hallazgos_sin_texto"], f"{k}: hallazgos sin texto {inf['control_salida']['hallazgos_sin_texto']}")
    chk(inf["control_salida"]["ok"], f"{k}: control de salida {inf['control_salida']['problemas'][:3]}")
    buenas = [b for b in p["lo_que_esta_bien"] if b["grupo"].startswith(("COND", "REL", "SEG"))]
    chk(len(p["lo_que_merece_atencion"]) + len(buenas) == len(inf["medico"]["hallazgos"]), f"{k}: cada hallazgo del motor debía tener su texto")
    sin_rec = [a["referencia"] for a in p["lo_que_merece_atencion"] if not any(a["referencia"] in r["hallazgos"] or any(x.split("#")[0] == a["referencia"] for x in r["hallazgos"]) or
               any(m["referencia"] in r["hallazgos"] for m in a["agrupa"]) for r in p["que_puedes_hacer"])]
    chk(not sin_rec, f"{k}: hallazgos sin ninguna recomendación: {sin_rec}")
    chk(all(a["por_que"] for a in p["lo_que_merece_atencion"]), f"{k}: hallazgo sin 'por qué' con valores")
    chk(not any("{" in x for x in textos_paciente(inf)), f"{k}: quedó un marcador sin reemplazar")
    chk(len(p["que_puedes_hacer"]) >= 5, f"{k}: muy pocas recomendaciones ({len(p['que_puedes_hacer'])})")
    chk(inf["nutricion"]["meta_diaria"]["personalizada"], f"{k}: meta nutricional no personalizada")
    chk(len(inf["nutricion"]["plan"]) == 7 and len(inf["whatsapp"]["recetas_diarias"]) == 7, f"{k}: el plan debía tener 7 recetas")
    chk(len({x["receta_id"] for x in inf["nutricion"]["plan"]}) == 7, f"{k}: recetas repetidas en la semana")
    chk(len(inf["whatsapp"]["recomendaciones_semanales"]) >= 4, f"{k}: pocas recomendaciones semanales")
    chk(all(len(x["texto"]) <= 4096 for x in inf["whatsapp"]["recetas_diarias"]), f"{k}: mensaje de receta muy largo para WhatsApp")
    s = json.dumps(inf, ensure_ascii=False) + saludly.resumen_md(inf)
    chk("PACIENTE EJEMPLO" not in s and PDF[k][1] not in s and "0000000001" not in s and "0000000002" not in s, f"{k}: el nombre o el documento aparecen en la salida")
    chk(inf["paciente_ref"].startswith("P-") and inf["estado"] in ("en_revision", "requiere_revision"), f"{k}: estado {inf['estado']}")

cod, h = correr("H")
chk(any(a["referencia"] == "COND-M1-EM-004" for a in h["paciente"]["lo_que_merece_atencion"]), "hombre: con peso y talla debía activarse obesidad o sobrepeso")
chk("sin_azucar_anadida" in h["nutricion"]["restricciones"]["exigir"] and all("sin_azucar_anadida" in x["etiquetas"] for x in h["nutricion"]["plan"]), "hombre con glucosa alta: recetas sin azúcar añadida")
chk(h["whatsapp"]["resultado_listo"] and h["estado"] != "retenido_hasta_llamada", "hombre: el informe no debía quedar retenido (la hepatitis B solo pide vacuna)")
# Hepatitis B: la vacunada va en "lo que está bien"; al susceptible se le recomienda la vacuna
_, m = correr("M")
chk(any(b["grupo"] == "COND-M4-IN-002" for b in m["paciente"]["lo_que_esta_bien"]) and not any(a["referencia"] == "COND-M4-IN-002" for a in m["paciente"]["lo_que_merece_atencion"]),
    "mujer vacunada: la hepatitis B debía ir en lo que está bien")
chk(any(a["referencia"] == "COND-M4-IN-002" and "falta protección" in a["titulo"] for a in h["paciente"]["lo_que_merece_atencion"]), "hombre susceptible: título por estado de la hepatitis B")
chk(any(r["recomendacion_id"] == "REC-CTL-215" for r in h["paciente"]["que_puedes_hacer"]) or any("REC-CTL-215" == x["recomendacion_id"] for x in h["whatsapp"]["recomendaciones_semanales"]),
    "hombre susceptible: debía recomendarse la vacuna de hepatitis B")
chk(not any("REC-CTL-215" == r["recomendacion_id"] for r in m["paciente"]["que_puedes_hacer"]), "mujer vacunada: no se le recomienda la vacuna")
# Un patrón no repite el mismo valor dos veces
for a in h["paciente"]["lo_que_merece_atencion"]:
    chk(len(a["por_que"]) == len(set(a["por_que"])), f"frases repetidas en {a['referencia']}")
chk(any("128/82 mmHg" in x for a in h["paciente"]["lo_que_merece_atencion"] for x in a["por_que"]), "la presión de la enfermera debía aparecer con su valor")
# Ingredientes sin palabras repetidas
chk(not any(" de limón" in x["texto"] and "limón de limón" in x["texto"] for x in h["whatsapp"]["recetas_diarias"] + m["whatsapp"]["recetas_diarias"]), "ingrediente con nombre repetido")
# Nivel de actividad del paciente (PWA): cambia las calorías, no los hallazgos
_, s1 = correr("H", actividad="sedentario"); _, s2 = correr("H", actividad="alto")
chk(s2["nutricion"]["meta_diaria"]["kcal"] > s1["nutricion"]["meta_diaria"]["kcal"], "más actividad debía dar más calorías")
chk([a["referencia"] for a in s1["paciente"]["lo_que_merece_atencion"]] == [a["referencia"] for a in s2["paciente"]["lo_que_merece_atencion"]], "la actividad no cambia los hallazgos")
_, s3 = correr("H", actividad=None)
chk(s3["perfil"]["nivel_actividad"] == "ligero (supuesto)", "sin respuesta se supone actividad ligera y se dice")
# Potasio alto: se nombra el corazón (decisión de Carlos)
import yaml
chk("corazón" in yaml.safe_load(open(os.path.join(RAIZ, "knowledge_base", "fase5", "redaccion", "COND-M2-NE-004.yaml"), encoding="utf-8"))["riesgo_claro"], "potasio alto debía nombrar el corazón")
# 2) Rechazos y datos inválidos
pdf, doc, orden = PDF["H"]
cod, r = saludly.generar(pdf, doc, "LCD-2026-999999", dict(objetivos=["prevenir"], toma_biotina=False))
chk(cod == 2 and r["estado"] == "pdf_rechazado", "orden equivocada: debía rechazarse")
cod, r = saludly.generar(pdf, doc, orden, dict(objetivos=["prevenir"], toma_biotina=False, nivel_actividad="muchisimo"))
chk(cod == 3, "nivel de actividad desconocido: debía rechazarse")
cod, r = saludly.generar(pdf, doc, orden, dict(objetivos=["volar"], toma_biotina=False))
chk(cod == 3, "objetivo desconocido: debía rechazarse")
cod, r = saludly.generar(pdf, doc, orden, dict(objetivos=["prevenir", "bajar_peso", "rendimiento", "maraton"], toma_biotina=False))
chk(cod == 3, "más de 3 objetivos: debía rechazarse")
# 3) El objetivo cambia el orden de las recomendaciones, nunca los hallazgos
_, a1 = correr("M", objetivos=("maraton", "rendimiento", "atletico"))
_, a2 = correr("M", objetivos=("salud_general", "energia_sueno", "envejecer_saludable"))
chk([x["referencia"] for x in a1["paciente"]["lo_que_merece_atencion"]] == [x["referencia"] for x in a2["paciente"]["lo_que_merece_atencion"]], "los objetivos no deben cambiar los hallazgos")
chk([x["recomendacion_id"] for x in a1["paciente"]["que_puedes_hacer"]] != [x["recomendacion_id"] for x in a2["paciente"]["que_puedes_hacer"]], "los objetivos deben cambiar el orden de las recomendaciones")
dep = [x for x in a1["paciente"]["que_puedes_hacer"] if x["tipo"] == "actividad" and set(x["objetivos"]) & {"maraton", "rendimiento", "atletico"}]
chk(all(x["requiere_consulta_previa"] for x in dep), "mujer con anemia y meta de maratón: el entrenamiento intenso debía esperar la consulta")
# 4) Biotina
_, b = correr("M", biotina=True)
chk(not any(x["referencia"] == "COND-M2-TI-001" for x in b["paciente"]["lo_que_merece_atencion"]), "con biotina no se informa la tiroides")
# 5) Sin medidas de la enfermera: sin meta personalizada
_, s = correr("M", enf={})
chk(not s["nutricion"]["meta_diaria"]["personalizada"], "sin peso ni talla la meta no se personaliza")
# 6) Metas: TFG baja limita la proteína
meta = NU.metas(dict(peso_kg=80, talla_m=1.75, edad=60, sexo="hombre"), ["masa_muscular"], dict(calculados=dict(egfr=45)))
chk(meta["proteina_g"] <= 64, f"con TFG 45 la proteína no debía pasar de 0,8 g/kg ({meta['proteina_g']} g)")
meta = NU.metas(dict(peso_kg=80, talla_m=1.75, edad=30, sexo="hombre"), ["masa_muscular"], dict(calculados=dict(egfr=100)))
chk(meta["proteina_g"] == 128, f"masa muscular: 1,6 g/kg ({meta['proteina_g']} g)")
# 7) Control de salida
for frase, mala in (("Tienes diabetes tipo 2.", True), ("Toma 2000 UI de vitamina D al día.", True), ("Tu riesgo de infarto es del 12 %.", True),
                    ("Tu glucosa está en el rango que las guías usan para diabetes; un médico debe confirmarlo.", False), ("Estás sano, no es nada.", True)):
    chk(bool(CS.revisar(frase)) == mala, f"control de salida con «{frase}»")
# 8) Catálogo de recetas: nutrientes calculados y restricciones
cat = NU.catalogo(C["recetas"], C["alimentos"])
chk(len(cat) >= 150, f"el catálogo debía tener al menos 150 recetas ({len(cat)})")
chk(all(r["nutrientes_porcion"]["kcal"] > 0 for r in cat), "receta con 0 kcal")
for e in ("sin_azucar_anadida", "baja_en_sodio", "alta_en_proteina", "fuente_de_hierro", "alta_en_fibra"):
    chk(sum(e in r["etiquetas_calculadas"] for r in cat) >= 10, f"pocas recetas con la etiqueta {e}")

for f in fallos: print("FALLA:", f)
print(f"Pasan {pasan} de {pasan + len(fallos)} comprobaciones")
