"""
Valida el contenido de la Fase 5 (knowledge_base/fase5): redacción por hallazgo, recomendaciones y recetas.
Revisa el formato, que los identificadores existan, que los marcadores {biomarcador} sean válidos, que los
alimentos de cada receta estén en la tabla y que ningún texto para el paciente rompa el control de salida.

Uso:  python validar_fase5.py            # sale con código 1 si hay errores
"""
import glob, os, re, sys
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
F5 = os.path.join(RAIZ, "knowledge_base", "fase5")
sys.path.insert(0, os.path.join(RAIZ, "codigo", "informe"))
import control_salida as CS
import json

IDX = json.load(open(os.path.join(RAIZ, "knowledge_base", "00_INDEX.json"), encoding="utf-8"))
CALC_EXTRA = {"homa_ir", "egfr", "hemoglobina_ajustada", "calcio_corregido", "tyg_index", "fib4", "indice_androgenos_libres", "testosterone_free", "phenoage",
              "non_hdl_c", "transferrin_saturation", "mentzer_index", "nlr", "tg_hdl_ratio", "globulin", "ag_ratio", "remnant_cholesterol", "tc_hdl_ratio",
              "apob_apoa1_ratio", "bun_creatinine_ratio", "imc", "presion", "presion_sistolica", "presion_diastolica", "cintura_cm", "peso_kg", "talla_m", "psa_libre_porcentaje", "eosinofilos_abs", "egfr_creatinina_cistatina", "brecha_osmolar", "sodio_corregido"}
MARCADORES = set(IDX["biomarcadores"]) | CALC_EXTRA
IDS_HALLAZGO = set(IDX["condiciones"]) | set(IDX["relaciones"]) | set(IDX["seguridad"])
OBJETIVOS = {o["id"] for o in yaml.safe_load(open(os.path.join(F5, "objetivos.yaml"), encoding="utf-8"))}
FILTROS = yaml.safe_load(open(os.path.join(F5, "filtros.yaml"), encoding="utf-8"))
OPC_FILTROS = {k: {o["id"] for o in v["opciones"]} for k, v in FILTROS["preguntas"].items()}
TIPOS_REC = {"alimentacion", "hidratacion", "actividad", "sueno", "habitos", "actividades_saludables", "vitaminas_suplementos", "terapias", "controles"}
ESTADOS_HB = {"infeccion_activa", "infeccion_pasada_resuelta", "anti_hbc_aislado", "inmune_por_vacuna", "susceptible"}
CLASES = {"bajo", "alto", "limitrofe", "critico", "alterado", "en_rango"}
errores, avisos = [], []

def err(m): errores.append(m)

def textos_de(d, campos):
    for c in campos:
        v = d.get(c)
        if isinstance(v, str): yield c, v
        elif isinstance(v, list):
            for i, x in enumerate(v):
                if isinstance(x, str): yield f"{c}[{i}]", x
        elif isinstance(v, dict):
            for k, x in v.items():
                if isinstance(x, str): yield f"{c}.{k}", x

def control(ubic, texto):
    for p in CS.revisar(texto):
        err(f"{ubic}: {p['motivo']} → «{p['fragmento']}»")
    for m in re.findall(r"\{([^}]+)\}", texto):
        if m not in MARCADORES: err(f"{ubic}: marcador desconocido {{{m}}}")


def ref_valida(x):
    if x == "general": return True
    for pref, k in (("alergia:", "alergias"), ("dieta:", "dieta"), ("medicamento:", "medicamentos")):   # respuestas del perfil (filtros.yaml)
        if x.startswith(pref): return x.split(":", 1)[1] in OPC_FILTROS[k]
    if x in IDS_HALLAZGO: return True
    if "#" in x: return x.split("#", 1)[0] in IDS_HALLAZGO and x.split("#", 1)[1] in ESTADOS_HB
    if x.startswith("objetivo:"): return x.split(":", 1)[1] in OBJETIVOS
    if ":" in x:
        b, c = x.split(":", 1)
        return b in MARCADORES and c in CLASES
    return x.startswith("objetivo:") and x.split(":", 1)[1] in OBJETIVOS


# ---------------- redacción
red = {}
for f in sorted(glob.glob(os.path.join(F5, "redaccion", "*.yaml"))):
    nombre = os.path.basename(f)
    try: d = yaml.safe_load(open(f, encoding="utf-8"))
    except Exception as e: err(f"{nombre}: YAML inválido ({e})"); continue
    if nombre == "modulos.yaml":
        for g in d or []:
            for b in g.get("biomarcadores", []):
                if b not in MARCADORES: err(f"modulos.yaml/{g.get('id')}: biomarcador desconocido {b}")
            for c, t in textos_de(g, ["texto_bien"]): control(f"modulos.yaml/{g.get('id')}.{c}", t)
        continue
    for campo in ("id", "tipo", "titulo_paciente", "que_es", "por_que_te_aparece", "riesgo_claro", "ejemplo_simple", "incertidumbre"):
        if not d.get(campo): err(f"{nombre}: falta {campo}")
    if d.get("id") and d["id"] not in IDS_HALLAZGO: err(f"{nombre}: id desconocido {d['id']}")
    if d.get("id") and nombre != f"{d['id']}.yaml": err(f"{nombre}: el nombre del archivo no coincide con el id")
    if d.get("tipo") not in ("condicion", "patron", "seguridad", "informativa"): err(f"{nombre}: tipo inválido {d.get('tipo')}")
    for c, t in textos_de(d, ["titulo_paciente", "que_es", "por_que_te_aparece", "riesgo_claro", "ejemplo_simple", "incertidumbre", "cuando_consultar", "aviso_whatsapp"]):
        control(f"{nombre}.{c}", t)
        if len(t.split()) > 60: avisos.append(f"{nombre}.{c}: frase larga ({len(t.split())} palabras)")
    for est, var in (d.get("variantes") or {}).items():
        if est not in ESTADOS_HB: err(f"{nombre}: variante con estado desconocido {est}")
        for c, t in textos_de(var, ["titulo_paciente", "por_que_te_aparece", "riesgo_claro", "ejemplo_simple", "incertidumbre", "cuando_consultar"]):
            control(f"{nombre}.variantes.{est}.{c}", t)
    red[d.get("id")] = d

# ---------------- recomendaciones
recs = {}
for f in sorted(glob.glob(os.path.join(F5, "recomendaciones", "*.yaml"))):
    nombre = os.path.basename(f)
    try: lista = yaml.safe_load(open(f, encoding="utf-8")) or []
    except Exception as e: err(f"{nombre}: YAML inválido ({e})"); continue
    for r in lista:
        rid = r.get("id", "?")
        if rid in recs: err(f"{nombre}: id repetido {rid}")
        recs[rid] = r
        for campo in ("id", "tipo", "titulo", "texto_base", "por_que", "se_activa_con", "prioriza_objetivos", "whatsapp", "fuentes"):
            if r.get(campo) in (None, "", []) and campo not in ("prioriza_objetivos",): err(f"{nombre}/{rid}: falta {campo}")
        if r.get("tipo") not in TIPOS_REC: err(f"{nombre}/{rid}: tipo inválido {r.get('tipo')}")
        for x in (r.get("se_activa_con") or []) + (r.get("contraindicada_si") or []):
            if not ref_valida(x): err(f"{nombre}/{rid}: referencia desconocida {x}")
        for o in r.get("prioriza_objetivos") or []:
            if o not in OBJETIVOS: err(f"{nombre}/{rid}: objetivo desconocido {o}")
        for c, t in textos_de(r, ["titulo", "texto_base", "meta_concreta", "por_que", "whatsapp"]): control(f"{nombre}/{rid}.{c}", t)
        for sx, var in (r.get("por_sexo") or {}).items():           # variante por sexo: solo cambia texto_base y meta_concreta
            if sx not in ("hombre", "mujer"): err(f"{nombre}/{rid}: por_sexo con sexo inválido {sx}")
            if set(var) - {"texto_base", "meta_concreta"}: err(f"{nombre}/{rid}: por_sexo.{sx} solo admite texto_base y meta_concreta")
            for c, t in textos_de(var, ["texto_base", "meta_concreta"]): control(f"{nombre}/{rid}.por_sexo.{sx}.{c}", t)
        for dt, var in (r.get("por_dieta") or {}).items():          # variante por dieta: texto_base, meta_concreta y whatsapp
            if dt not in ("vegetariana", "vegana"): err(f"{nombre}/{rid}: por_dieta con dieta inválida {dt}")
            if set(var) - {"texto_base", "meta_concreta", "whatsapp"}: err(f"{nombre}/{rid}: por_dieta.{dt} solo admite texto_base, meta_concreta y whatsapp")
            for c, t in textos_de(var, ["texto_base", "meta_concreta", "whatsapp"]): control(f"{nombre}/{rid}.por_dieta.{dt}.{c}", t)
        if len(r.get("whatsapp") or "") > 400: err(f"{nombre}/{rid}: mensaje de WhatsApp de más de 400 caracteres")

# ---------------- alimentos y recetas
alimentos = {}
ruta_al = os.path.join(F5, "recetas", "alimentos.yaml")
if os.path.exists(ruta_al):
    for a in yaml.safe_load(open(ruta_al, encoding="utf-8")) or []:
        if a.get("id") in alimentos: err(f"alimentos.yaml: id repetido {a.get('id')}")
        alimentos[a.get("id")] = a
        for x in a.get("alergenos") or []:
            if x not in OPC_FILTROS["alergias"]: err(f"alimentos.yaml/{a.get('id')}: alérgeno desconocido {x}")
        if "alergenos" not in a: err(f"alimentos.yaml/{a.get('id')}: falta alergenos (puede ser [])")
        p = a.get("por_100g") or {}
        for k in ("kcal", "proteina_g", "grasa_g", "grasa_saturada_g", "carbohidratos_g", "fibra_g", "azucares_g", "sodio_mg", "potasio_mg", "hierro_mg", "calcio_mg"):
            if not isinstance(p.get(k), (int, float)): err(f"alimentos.yaml/{a.get('id')}: falta {k}")
        if p and isinstance(p.get("kcal"), (int, float)):
            est = 4 * (p.get("proteina_g") or 0) + 4 * (p.get("carbohidratos_g") or 0) + 9 * (p.get("grasa_g") or 0)
            # en verduras y frutas ácidas la fórmula 4-4-9 sobreestima (fibra y ácidos orgánicos): solo se revisa desde 50 kcal
            if p["kcal"] >= 50 and abs(est - p["kcal"]) / p["kcal"] > 0.25 and a.get("grupo") not in ("otros",):
                avisos.append(f"alimentos.yaml/{a.get('id')}: kcal {p['kcal']} no cuadra con los macronutrientes ({est:.0f})")
recetas = {}
for f in sorted(glob.glob(os.path.join(F5, "recetas", "*.yaml"))):
    nombre = os.path.basename(f)
    if nombre == "alimentos.yaml": continue
    try: lista = yaml.safe_load(open(f, encoding="utf-8")) or []
    except Exception as e: err(f"{nombre}: YAML inválido ({e})"); continue
    for r in lista:
        rid = r.get("id", "?")
        if rid in recetas: err(f"{nombre}: id repetido {rid}")
        recetas[rid] = r
        if r.get("tiempo_comida") not in ("desayuno", "almuerzo", "cena", "merienda"): err(f"{nombre}/{rid}: tiempo_comida inválido")
        if not r.get("ingredientes") or not r.get("pasos") or not r.get("porciones"): err(f"{nombre}/{rid}: faltan ingredientes, pasos o porciones")
        for i in r.get("ingredientes") or []:
            if i.get("alimento") not in alimentos: err(f"{nombre}/{rid}: alimento desconocido {i.get('alimento')}")
            if not isinstance(i.get("gramos"), (int, float)) or i["gramos"] <= 0: err(f"{nombre}/{rid}: gramos inválidos en {i.get('alimento')}")
        for c, t in textos_de(r, ["nombre", "pasos", "consejo"]): control(f"{nombre}/{rid}.{c}", t)

if __name__ == "__main__":
    try: sys.stdout.reconfigure(encoding="utf-8")   # la consola de Windows no imprime «→» sin esto
    except Exception: pass
    for a in avisos: print("AVISO:", a)
    for e in errores: print("ERROR:", e)
    print(f"Redacción: {len(red)} hallazgos · Recomendaciones: {len(recs)} · Alimentos: {len(alimentos)} · Recetas: {len(recetas)}")
    print(f"{len(errores)} errores, {len(avisos)} avisos")
    sys.exit(1 if errores else 0)
