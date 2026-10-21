"""
Saludly Brain · Nutrición: nutrientes de cada receta, metas diarias orientativas y la receta del día.

- Los nutrientes de las recetas se calculan con la tabla de alimentos (nunca se escriben a mano).
- Las metas son orientativas, no una prescripción: Mifflin-St Jeor con el peso y la talla que toma la enfermera,
  ajustadas por el objetivo y limitadas por los hallazgos (por ejemplo, sin dieta alta en proteína con TFG baja).
- Las restricciones salen de los hallazgos del motor: con glucosa alta, sin azúcar añadida; con presión o riñón,
  bajas en sodio; con potasio alto, sin recetas altas en potasio; etc.
- Las alergias y el tipo de dieta del paciente excluyen recetas por sus ingredientes (knowledge_base/fase5/filtros.yaml).
"""
import hashlib, re

NUTR = ("kcal", "proteina_g", "grasa_g", "grasa_saturada_g", "carbohidratos_g", "fibra_g", "azucares_g", "sodio_mg", "potasio_mg", "hierro_mg", "calcio_mg")
AZUCARES_ANADIDOS = ("azucar", "panela", "miel")
PURINAS_ALTAS = ("higado_res_crudo", "sardinas_lata_tomate")
FACTOR_ACTIVIDAD = {"sedentario": 1.2, "ligero": 1.375, "moderado": 1.55, "alto": 1.725}


def nutrientes(receta, alimentos):
    tot = {k: 0.0 for k in NUTR}
    for i in receta["ingredientes"]:
        a = alimentos.get(i["alimento"])
        if not a: continue
        for k in NUTR: tot[k] += (a["por_100g"].get(k) or 0) * i["gramos"] / 100
    por = max(1, receta.get("porciones") or 1)
    return {k: round(v / por, 1) for k, v in tot.items()}


def etiquetas(receta, n):
    principal = receta.get("tiempo_comida") in ("desayuno", "almuerzo", "cena")
    ids = [i["alimento"] for i in receta["ingredientes"]]
    e = set(receta.get("etiquetas") or [])
    if not any(a in ids for a in AZUCARES_ANADIDOS): e.add("sin_azucar_anadida")
    if n["sodio_mg"] <= (600 if principal else 140): e.add("baja_en_sodio")          # FDA: comida baja en sodio ≤ 600 mg; porción ≤ 140 mg
    if n["proteina_g"] >= (20 if principal else 10): e.add("alta_en_proteina")
    if n["fibra_g"] >= 5: e.add("alta_en_fibra")                                     # FDA: alta en fibra ≥ 5 g por porción
    if n["hierro_mg"] >= 2.7: e.add("fuente_de_hierro")                               # 15 % del valor diario (18 mg)
    if n["kcal"] and n["grasa_saturada_g"] * 9 / n["kcal"] <= 0.10: e.add("baja_en_grasa_saturada")
    if n["potasio_mg"] >= 700: e.add("alta_en_potasio")
    if any(a in ids for a in PURINAS_ALTAS): e.add("alta_en_purinas")
    return sorted(e)


def alergenos_y_dietas(receta, alimentos):
    """Alérgenos de la receta (unión de sus ingredientes) y dietas para las que sirve (todos los ingredientes aptos)."""
    ings = [alimentos.get(i["alimento"]) or {} for i in receta["ingredientes"]]
    ale = sorted({a for x in ings for a in x.get("alergenos") or []})
    dietas = [d for d, et in (("vegetariana", "vegetariano"), ("vegana", "vegano")) if all(et in (x.get("etiquetas") or []) for x in ings)]
    return ale, dietas


def catalogo(recetas, alimentos):
    out = []
    for r in recetas:
        n = nutrientes(r, alimentos)
        ale, dietas = alergenos_y_dietas(r, alimentos)
        out.append(dict(r, nutrientes_porcion=n, etiquetas_calculadas=etiquetas(r, n), alergenos=ale, dietas=dietas))
    return out


def _act(cond, *ids): return any(cond.get(i, {}).get("estado") in ("activa", "apoyo", "control") for i in ids)


def restricciones(motor_out, ctx):
    """Reglas de selección de recetas a partir de los hallazgos. 'exigir': etiquetas obligatorias; 'excluir': etiquetas prohibidas; 'preferir': suman puntos."""
    c = motor_out["condiciones"]; exigir, excluir, preferir, motivos = set(), set(), set(), []
    if _act(c, "COND-M1-EM-001", "COND-M1-EM-002", "COND-M1-EM-003", "COND-M1-EM-A02", "COND-M1-EM-A04") or ctx.get("diabetes_conocida"):
        exigir.add("sin_azucar_anadida"); preferir.add("alta_en_fibra"); motivos.append("glucosa: sin azúcar añadida y con fibra")
    if _act(c, "COND-M1-CA-006", "COND-M2-NE-001", "COND-M2-NE-003", "COND-M2-NE-002") or ctx.get("hipertension_conocida"):
        exigir.add("baja_en_sodio"); motivos.append("presión o riñón: bajas en sodio")
    if _act(c, "COND-M2-NE-004") or (motor_out.get("calculados", {}).get("egfr") or 99) < 30:
        excluir.add("alta_en_potasio"); motivos.append("potasio alto o TFG muy baja: sin recetas altas en potasio")
    if _act(c, "COND-M1-CA-001", "COND-M1-CA-002", "COND-M1-CA-003", "COND-M1-CA-004", "COND-M4-GA-001", "COND-M4-GA-002"):
        exigir.add("baja_en_grasa_saturada"); preferir.add("alta_en_fibra"); motivos.append("lípidos o hígado: poca grasa saturada y más fibra")
    if _act(c, "COND-M3-HE-001", "COND-M3-HE-002", "COND-M3-HE-003") and not _act(c, "COND-M3-HE-006", "COND-M3-HE-A04"):
        preferir.add("fuente_de_hierro"); motivos.append("reservas de hierro bajas: fuentes de hierro")
    if _act(c, "COND-M3-HE-006"):
        excluir.add("alta_en_purinas"); motivos.append("posible sobrecarga de hierro: sin hígado")
    if _act(c, "COND-M6-RE-001"):
        excluir.add("alta_en_purinas"); motivos.append("ácido úrico alto: sin vísceras ni sardinas")
    alergias = sorted(ctx.get("alergias") or [])
    dieta = ctx.get("dieta") if ctx.get("dieta") in ("vegetariana", "vegana") else None
    if alergias: motivos.append(f"alergias o intolerancias: sin recetas con {', '.join(alergias)}")
    if dieta: motivos.append(f"dieta {dieta}: solo recetas aptas")
    return dict(exigir=sorted(exigir), excluir=sorted(excluir), preferir=sorted(preferir), motivos=motivos, alergias=alergias, dieta=dieta)


def metas(ctx, objetivos, motor_out):
    """Metas diarias orientativas. Sin peso o talla no se personaliza."""
    peso, talla, edad, sexo = ctx.get("peso_kg"), ctx.get("talla_m"), ctx.get("edad"), ctx.get("sexo")
    egfr = (motor_out.get("calculados") or {}).get("egfr")
    notas = ["Meta orientativa, no una prescripción: un nutricionista la ajusta a tu caso."]
    if not (peso and talla and edad and sexo in ("hombre", "mujer")):
        return dict(personalizada=False, motivo="faltan peso y talla de la enfermera", notas=notas,
                    sodio_mg_max=2000, azucar_anadida_g_max=None, fibra_g_min=25 if sexo == "mujer" else 30)
    ree = 10 * peso + 6.25 * talla * 100 - 5 * edad + (5 if sexo == "hombre" else -161)
    factor = FACTOR_ACTIVIDAD.get(ctx.get("nivel_actividad") or "ligero", 1.375)
    kcal = ree * factor
    imc = peso / talla ** 2
    if "bajar_peso" in objetivos and imc >= 20:
        kcal *= 0.85; kcal = max(kcal, 1500 if sexo == "hombre" else 1200); notas.append("Con un déficit moderado para bajar de peso sin pasar hambre.")
    elif any(o in objetivos for o in ("masa_muscular", "maraton", "rendimiento", "atletico")):
        kcal *= 1.10; notas.append("Con un poco más de energía para tu entrenamiento.")
    g_kg = 1.0
    if any(o in objetivos for o in ("masa_muscular", "atletico")): g_kg = 1.6
    elif any(o in objetivos for o in ("rendimiento", "maraton")): g_kg = 1.4
    elif "bajar_peso" in objetivos or "envejecer_saludable" in objetivos or edad >= 65: g_kg = 1.2
    if egfr is not None and egfr < 60:
        g_kg = min(g_kg, 0.8); notas.append("Con la función de tu riñón, la proteína no se aumenta: consúltalo con un nutricionista.")
    prot = g_kg * peso
    grasa = kcal * 0.28 / 9
    carb = (kcal - prot * 4 - grasa * 9) / 4
    return dict(personalizada=True, kcal=round(kcal), proteina_g=round(prot), grasa_g=round(grasa), grasa_saturada_g_max=round(kcal * 0.10 / 9),
                carbohidratos_g=round(max(carb, 0)), fibra_g_min=25 if sexo == "mujer" else 30, sodio_mg_max=2000, azucar_anadida_g_max=round(kcal * 0.10 / 4),
                formula="Mifflin-St Jeor × actividad, ajustado por objetivo; proteína en g/kg según objetivo", notas=notas)


def plan_recetas(cat, restr, objetivos, semilla, dias=7):
    """Una receta por día, alternando el momento del día, sin repetir y respetando las restricciones."""
    aptas = [r for r in cat if all(e in r["etiquetas_calculadas"] for e in restr["exigir"]) and not any(e in r["etiquetas_calculadas"] for e in restr["excluir"])
             and not set(restr.get("alergias") or []) & set(r.get("alergenos") or []) and (not restr.get("dieta") or restr["dieta"] in (r.get("dietas") or []))]
    pref = set(restr["preferir"])
    if any(o in objetivos for o in ("masa_muscular", "atletico", "rendimiento", "maraton")) and "alta_en_proteina" not in restr["excluir"]: pref.add("alta_en_proteina")
    if "bajar_peso" in objetivos: pref.update({"alta_en_fibra", "sin_azucar_anadida"})
    orden_tiempos = ["almuerzo", "desayuno", "cena", "almuerzo", "merienda", "cena", "desayuno"]
    def puntaje(r):
        h = int(hashlib.sha256(f"{semilla}{r['id']}".encode()).hexdigest()[:8], 16) / 0xFFFFFFFF   # desempate estable por paciente
        return -(len(pref & set(r["etiquetas_calculadas"])) + h)
    plan, usadas = [], set()
    for d in range(dias):
        t = orden_tiempos[d % len(orden_tiempos)]
        cand = sorted([r for r in aptas if r["tiempo_comida"] == t and r["id"] not in usadas], key=puntaje) or \
               sorted([r for r in aptas if r["id"] not in usadas], key=puntaje)
        if not cand: break
        r = cand[0]; usadas.add(r["id"])
        plan.append(dict(dia=d + 1, receta_id=r["id"], nombre=r["nombre"], tiempo_comida=r["tiempo_comida"], porciones=r["porciones"],
                         tiempo_min=r.get("tiempo_min"), nutrientes_porcion=r["nutrientes_porcion"], etiquetas=r["etiquetas_calculadas"]))
    return dict(aptas=len(aptas), total=len(cat), plan=plan)


def _num(x, dec=0):
    s = f"{x:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s


def _ingrediente(i, nombre):
    """'1 diente' + 'Ajo' → '1 diente de ajo'; '1 limón' + 'Limón' → '1 limón'; '2 tomates' + 'Tomate chonto' → '2 tomates (tomate chonto)'."""
    medida, nombre = (i.get("medida") or f"{i['gramos']} g").strip(), nombre.lower()
    palabras = re.findall(r"[a-záéíóúñü]{4,}", nombre)
    if not any(p[:5] in medida.lower() for p in palabras):
        return f"{medida} de {nombre}"
    extra = [p for p in palabras if p[:5] not in medida.lower()]
    return f"{medida} ({nombre})" if extra else medida


def mensaje_receta(r, alimentos_cat, meta):
    n = r["nutrientes_porcion"]
    ing = "\n".join(f"• {_ingrediente(i, alimentos_cat[i['alimento']]['nombre'])}" for i in r["ingredientes"] if i["alimento"] in alimentos_cat and i["alimento"] not in ("agua", "sal"))
    sal = [i for i in r["ingredientes"] if i["alimento"] == "sal"]
    if sal: ing += "\n• una pizca de sal"
    pasos = "\n".join(f"{k + 1}. {p}" for k, p in enumerate(r["pasos"]))
    aporte = ""
    if meta.get("personalizada") and meta.get("proteina_g"):
        aporte = f"\nCubre cerca del {round(100 * n['proteina_g'] / meta['proteina_g'])} % de tu proteína del día."
    texto = (f"🍽️ *Receta del día: {r['nombre']}*\n{r['tiempo_comida'].capitalize()} · {r.get('tiempo_min') or '—'} min · {r['porciones']} porciones\n\n"
             f"*Por porción:* {_num(n['kcal'])} kcal · proteína {_num(n['proteina_g'])} g · carbohidratos {_num(n['carbohidratos_g'])} g · "
             f"grasa {_num(n['grasa_g'])} g · fibra {_num(n['fibra_g'])} g · sodio {_num(n['sodio_mg'])} mg{aporte}\n\n"
             f"*Ingredientes*\n{ing}\n\n*Preparación*\n{pasos}")
    if r.get("consejo"): texto += f"\n\n💡 {r['consejo']}"
    return texto
