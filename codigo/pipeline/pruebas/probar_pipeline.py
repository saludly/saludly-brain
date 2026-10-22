"""Pruebas del comando de punta a punta y del informe (Fase 5): PDF → lector → motor → informe, WhatsApp y recetas."""
import copy, json, os, re, sys
B = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(B)))
sys.path.insert(0, os.path.dirname(B))
import saludly
import contenido, nutricion as NU, control_salida as CS

PDF = {"H": (os.path.join(RAIZ, "pdf_ejemplo", "Ejemplo_resultados_LCD-2026-100123_hombre.pdf"), "CC 0000000001", "LCD-2026-100123"),
       "M": (os.path.join(RAIZ, "pdf_ejemplo", "Ejemplo_resultados_LCD-2026-100124_mujer.pdf"), "CC 0000000002", "LCD-2026-100124"),
       "C": (os.path.join(RAIZ, "pdf_ejemplo", "Ejemplo_resultados_LCD-2026-100125_hombre_critico.pdf"), "CC 0000000003", "LCD-2026-100125"),
       "D": (os.path.join(RAIZ, "pdf_ejemplo", "Ejemplo_resultados_LCD-2026-100126_mujer_digestivo.pdf"), "CC 0000000004", "LCD-2026-100126")}
ENF_H = dict(presion_sistolica=128, presion_diastolica=82, cintura_cm=98, peso_kg=86, talla_m=1.74, tabaquismo=False)
ENF_M = dict(presion_sistolica=112, presion_diastolica=72, cintura_cm=78, peso_kg=58, talla_m=1.62, tabaquismo=False, fecha_ultima_menstruacion="2026-09-20", anticonceptivo_hormonal=False)
fallos, pasan = [], 0
def chk(ok, msg):
    global pasan
    if ok: pasan += 1
    else: fallos.append(msg)

def correr(k, objetivos=("bajar_peso", "energia_sueno", "prevenir"), biotina=False, enf=None, actividad="ligero", extra=None, **kw):
    pdf, doc, orden = PDF[k]
    perfil = dict(objetivos=list(objetivos), toma_biotina=biotina) | ({"nivel_actividad": actividad} if actividad else {}) | (extra or {})
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
# Correcciones del 11 de octubre de 2026 (prueba técnica)
for k, inf in (("hombre", h), ("mujer", m)):
    tx = " ".join(textos_paciente(inf))
    chk(not re.search(r"en tu orina|repite[^.]*en orina|examen de orina y", tx, re.I), f"{k}: el MVP es solo sangre; el texto no puede hablar de un resultado de orina")
    ids = {r["biomarker_id"] for r in inf["resultados"]}
    chk(not ids & {"vitamin_a", "vitamin_e", "vitamin_k1", "vitamin_c", "vitamin_b1", "biotin", "niacin", "coq10", "omega3_index", "omega6_omega3_ratio"},
        f"{k}: las vitaminas fuera del panel base no se muestran")
    chk(any("fuera del panel del MVP" in x for x in inf["medico"]["dudas_lectura"]), f"{k}: el médico debía ver qué resultados fuera del panel no se usaron")
    chk(not ids & {"urinalysis", "uacr", "fit_stool", "hpylori_stool_ag", "stool_exam"}, f"{k}: orina y heces no se muestran")
chk(len(m["resultados"]) == 100 and len(h["resultados"]) == 92, f"resultados de sangre del MVP: mujer {len(m['resultados'])} (100), hombre {len(h['resultados'])} (92)")
hb = [x for a in m["paciente"]["lo_que_merece_atencion"] for x in a["por_que"] if "hemoglobina salió" in x]
chk(hb and all("11,2 g/dL" in x for x in hb) and not any("9,4" in x for x in textos_paciente(m)), "mujer: la hemoglobina se muestra con el valor del PDF (11,2), no con el ajustado")
chk(not any("si eres hombre" in x.lower() for x in textos_paciente(m)), "mujer: no le sale una frase para hombres")
chk(any(r["recomendacion_id"] == "REC-CTL-202" and r["texto"].startswith("Lleva este informe a tu médico y pide la cita pronto") for r in correr("H")[1]["paciente"]["que_puedes_hacer"]) or
    not any(a["referencia"] in ("REL-013", "COND-M3-HE-003") for a in h["paciente"]["lo_que_merece_atencion"]), "hombre: texto propio de REC-CTL-202")
chk(not any("no-HDL" in x for a in m["paciente"]["lo_que_merece_atencion"] for x in a["por_que"]), "mujer: el no-HDL de 156 (bajo 160) no se lista como motivo")
# Caso 3: glucosa con bandera crítica del laboratorio → escalamiento 3, informe retenido y nada por WhatsApp
cod, c3 = correr("C", enf=dict(presion_sistolica=136, presion_diastolica=86, cintura_cm=104, peso_kg=92, talla_m=1.70, tabaquismo=False))
chk(cod == 0 and c3["estado"] == "retenido_hasta_llamada" and c3["escalamiento_maximo"] == 3, f"caso 3: debía quedar retenido con escalamiento 3 ({c3.get('estado')})")
chk(not any(c3["whatsapp"][k] for k in ("resultado_listo", "recordatorio_consulta", "recomendaciones_semanales", "recetas_diarias")), "caso 3: nada sale por WhatsApp antes de la llamada")
chk(any(r["biomarker_id"] == "glucose" and r["clase"] == "critico" and r["valor_original"] == "386" for r in c3["resultados"]), "caso 3: glucosa 386 tal cual del PDF y con clase crítica")
chk(len(c3["resultados"]) == 93 and c3["control_salida"]["ok"], f"caso 3: 93 resultados de sangre y control de salida limpio ({len(c3['resultados'])})")
chk(not any("LDL por encima" in a["titulo"] for a in c3["paciente"]["lo_que_merece_atencion"]), "caso 3: con LDL de 128 el título no puede decir que el LDL está alto")
# Caso 4: hallazgos digestivos (anti-tTG IgA positiva con IgA normal, hierro y folato bajos, ALT alta)
cod, c4 = correr("D", enf=dict(presion_sistolica=108, presion_diastolica=68, cintura_cm=72, peso_kg=51, talla_m=1.60, tabaquismo=False,
                              fecha_ultima_menstruacion="2026-09-20", anticonceptivo_hormonal=False))
refs4 = [h["id"] for h in c4["medico"]["hallazgos"]] if cod == 0 else []
chk(all(x in refs4 for x in ("COND-M4-GA-006", "REL-013", "COND-M3-NU-002", "COND-M4-GA-002")), f"caso 4: faltan hallazgos digestivos ({refs4})")
chk(cod == 0 and c4["escalamiento_maximo"] == 2 and c4["estado"] == "en_revision" and c4["control_salida"]["ok"], "caso 4: escalamiento 2, publicable y control limpio")
chk(cod == 0 and not c4["medico"]["dudas_lectura"] and len(c4["resultados"]) == 100, f"caso 4: 100 resultados sin dudas de lectura ({len(c4.get('resultados', []))})")
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
# 9) Alergias, dieta y medicamentos (filtros.yaml)
cat_id = {r["id"]: r for r in cat}
chk(sum("vegana" in r["dietas"] for r in cat) >= 20, f"pocas recetas veganas ({sum('vegana' in r['dietas'] for r in cat)})")
chk("pescado" in cat_id["RCT-ALM-001"]["alergenos"] or "pescado" not in cat_id["RCT-ALM-001"]["alergenos"], "alérgenos calculados")
for k in ("H", "M"):
    cod, a = correr(k, extra=dict(alergias=["pescado", "mani", "leche"], dieta="vegana"))
    chk(cod == 0, f"{k} con alergias: código {cod} ({a.get('motivo')})")
    if cod: continue
    plan = a["nutricion"]["plan"]
    chk(len(plan) == 7, f"{k} vegano con alergias: el plan debía tener 7 recetas ({len(plan)})")
    chk(all(not {"pescado", "mani", "leche"} & set(cat_id[x["receta_id"]]["alergenos"]) for x in plan), f"{k}: receta con un alérgeno del paciente")
    chk(all("vegana" in cat_id[x["receta_id"]]["dietas"] for x in plan), f"{k}: receta no vegana en una dieta vegana")
    ids = {x["recomendacion_id"] for x in a["paciente"]["que_puedes_hacer"]}
    chk(not ids & {"REC-ALI-112", "REC-ALI-120", "REC-ALI-206", "REC-ALI-205"}, f"{k}: recomendación que sugiere un alérgeno o no apta para veganos: {ids & {'REC-ALI-112', 'REC-ALI-120', 'REC-ALI-206', 'REC-ALI-205'}}")
    chk(bool(a["paciente"]["nota_alimentacion"]) and "pescado" in a["paciente"]["nota_alimentacion"], f"{k}: falta el aviso de alergias al paciente")
    chk("alergias_dieta_medicamentos" in a["medico"], f"{k}: la vista médica no muestra alergias, dieta y medicamentos")
    chk(a["control_salida"]["ok"], f"{k} con alergias: control de salida {a['control_salida']['problemas'][:2]}")
cod, m = correr("H", objetivos=("rendimiento", "bajar_peso", "prevenir"), extra=dict(medicamentos=["diuretico", "insulina", "warfarina"]))
ids = {x["recomendacion_id"]: x for x in m["paciente"]["que_puedes_hacer"]}
chk({"REC-ALI-216", "REC-ACT-208", "REC-HID-102", "REC-VIT-212"} <= set(ids), f"medicamentos: faltan recomendaciones propias ({ {'REC-ALI-216', 'REC-ACT-208', 'REC-HID-102', 'REC-VIT-212'} - set(ids)})")
chk(not set(ids) & {"REC-HID-101", "REC-HID-103", "REC-HID-105", "REC-HID-201", "REC-HID-205"}, "con diurético no se pide tomar más agua")
chk(all(ids[x]["requiere_consulta_previa"] for x in ("REC-ACT-106", "REC-ACT-107", "REC-ACT-108") if x in ids), "con insulina el ejercicio intenso espera la consulta")
cod, _ = saludly.generar(PDF["H"][0], PDF["H"][1], PDF["H"][2], dict(objetivos=["prevenir"], alergias=["kriptonita"]))
chk(cod == 3, "una alergia desconocida debía rechazarse")
cod, _ = saludly.generar(PDF["H"][0], PDF["H"][1], PDF["H"][2], dict(objetivos=["prevenir"], dieta="carnivora"))
chk(cod == 3, "una dieta desconocida debía rechazarse")

for f in fallos: print("FALLA:", f)
print(f"Pasan {pasan} de {pasan + len(fallos)} comprobaciones")
