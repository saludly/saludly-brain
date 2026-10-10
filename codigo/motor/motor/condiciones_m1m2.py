"""
Saludly Brain · Motor · Parte 2: condiciones de los módulos M1 y M2

Cada ficha de condición del Knowledge Base tiene aquí su evaluador. Los
umbrales son los de la ficha (se cita el campo); los metadatos (nombre, nivel de
lenguaje, guías) se leen de la ficha misma. Estados posibles:
  activa · apoyo · vigilar · no_activa · incompleta · no_calculable ·
  no_interpretable · no_aplica · control · pendiente_refleja
"""
import glob, math, os, re, yaml
import score2 as S2

BASE = os.path.dirname(os.path.abspath(__file__))
FICHAS = {}
for p in glob.glob(f"{BASE}/kb/condiciones/*/*.md"):
    s = open(p, encoding="utf-8").read()
    y = yaml.safe_load(re.search(r"```yaml\n(.*?)```", s, re.S).group(1))
    FICHAS[y["id"]] = y


class Datos:
    """Acceso cómodo a la salida de la parte 1 y al contexto."""
    def __init__(self, p1, ctx):
        self.R = {r["biomarker_id"]: r for r in p1["resultados"] if r.get("biomarker_id") and not r.get("campo")}
        self.campos = {(r["biomarker_id"], r["campo"]): r for r in p1["resultados"] if r.get("campo")}
        self.C = p1["calculados"]; self.ctx = ctx
    def r(self, b): return self.R.get(b)
    def v(self, b):
        r = self.R.get(b)
        if r and r.get("clase") != "no_interpretable" and r.get("estado") in ("medido", "menor_que_limite", "mayor_que_limite") and isinstance(r.get("valor"), (int, float)):
            return float(r["valor"])
        return None
    def interpretable(self, b):
        r = self.R.get(b); return bool(r) and r.get("clase") != "no_interpretable"
    def motivo_no(self, b):
        r = self.R.get(b); return (r or {}).get("motivo_clase") if r else "no medido"
    def clase(self, b): return (self.R.get(b) or {}).get("clase")
    def lo(self, b): return ((self.R.get(b) or {}).get("intervalo_lab") or {}).get("bajo")
    def hi(self, b): return ((self.R.get(b) or {}).get("intervalo_lab") or {}).get("alto")
    def calc(self, c):
        x = self.C.get(c); return x["valor"] if x and x.get("calculado") else None
    def c(self, k, d=None): return self.ctx.get(k, d)
    def meds(self): return " ".join(m.lower() for m in self.ctx.get("medicamentos", []))
    @property
    def hombre(self): return self.ctx.get("sexo") == "hombre"


def H(fid, estado, coincidencia=None, escalamiento=None, cumplidos=None, faltan=None, confusores=None, nota=None, extra=None):
    f = FICHAS.get(fid, {})
    d = dict(ficha=fid, nombre=f.get("nombre"), modulo=f.get("modulo"), tipo=f.get("tipo"), estado=estado,
             coincidencia=coincidencia, escalamiento=escalamiento, nivel_lenguaje=f.get("nivel_lenguaje"),
             criterios_cumplidos=cumplidos or [], datos_faltantes=faltan or [], confusores_aplicados=confusores or [],
             nota=nota, guias=f.get("guias"))
    if extra: d.update(extra)
    return d

def ni(fid, d, b): return H(fid, "no_interpretable", nota=f"{b}: {d.motivo_no(b)}")


# =============================================================== M1 · Cardiología
def ca001(d):
    f = "COND-M1-CA-001"
    if d.c("embarazo"): return H(f, "no_interpretable", nota="embarazo")
    ldl, nh, hdl, tg = d.v("ldl_c"), d.calc("non_hdl_c"), d.v("hdl_c"), d.v("triglycerides")
    if ldl is None and nh is None: return H(f, "incompleta", faltan=["ldl_c", "non_hdl_c"])
    c = dict(ldl_alto=ldl is not None and ldl >= 130, no_hdl_alto=nh is not None and nh >= 160,
             hdl_bajo=hdl is not None and hdl < (40 if d.hombre else 50), tg_alto=tg is not None and tg >= 150)
    cum = [k for k, v in c.items() if v]
    control = "estatina" in d.meds() or "atorvastatina" in d.meds() or "rosuvastatina" in d.meds()
    if c["ldl_alto"] or c["no_hdl_alto"]:
        if control: return H(f, "control", cumplidos=cum, nota="en tratamiento con estatina: se lee como control")
        return H(f, "activa", "alta" if (c["ldl_alto"] and c["no_hdl_alto"]) else "moderada", 1, cum)
    if c["hdl_bajo"] and c["tg_alto"]: return H(f, "vigilar", "baja", None, cum)
    return H(f, "no_activa", cumplidos=cum)

def ca002(d):
    f = "COND-M1-CA-002"
    ldl = d.v("ldl_c")
    if ldl is None: return H(f, "incompleta", faltan=["ldl_c"])
    if ldl < 190: return H(f, "no_activa")
    fam = d.c("antecedente_familiar_cv_temprano")
    conf = ["TSH alta: posible causa secundaria"] if d.clase("tsh") == "alto" else []
    return H(f, "activa", "alta" if fam else "moderada", 2, ["ldl_muy_alto"] + (["antecedente_familiar"] if fam else []),
             [] if fam is not None else ["antecedente_familiar_cv_temprano"], conf)

def ca003(d):
    f = "COND-M1-CA-003"
    if not d.interpretable("triglycerides"): return ni(f, d, "triglycerides")
    tg = d.v("triglycerides")
    if tg is None: return H(f, "incompleta", faltan=["triglycerides"])
    if tg < 150: return H(f, "no_activa")
    alc = d.c("alcohol_48h")
    coin = "alta" if alc is False else "moderada"
    esc = 3 if d.clase("triglycerides") == "critico" else 2 if tg >= 500 else 1
    nota = "triglicéridos de 1.000 o más: mencionar prevención de pancreatitis" if tg >= 1000 else None
    return H(f, "activa", coin, esc, ["tg_alto"] + (["tg_muy_alto"] if tg >= 500 else []), [] if alc is not None else ["alcohol_48h"],
             ["alcohol en 48 horas"] if alc else [], nota)

def ca004(d):
    f = "COND-M1-CA-004"
    r = d.r("lpa")
    if not r or d.v("lpa") is None: return H(f, "incompleta", faltan=["lpa"])
    u = (r.get("unidad") or "").lower().replace(" ", "")
    if u not in ("mg/dl", "nmol/l"): return H(f, "no_interpretable", nota="sin unidad declarada; no se convierte entre mg/dL y nmol/L")
    v = d.v("lpa"); alta = v > 50 if u == "mg/dl" else v > 105
    nota = "también supera el corte ACC/AHA de 125 nmol/L" if u == "nmol/l" and v >= 125 else None
    return H(f, "activa", "alta", 1, ["lpa_alta"], nota=nota) if alta else H(f, "no_activa")

def ca005(d):
    f = "COND-M1-CA-005"
    edad = d.c("edad")
    if edad is None or not (40 <= edad <= 69): return H(f, "no_calculable", nota="solo se calcula entre 40 y 69 años; se muestran los factores de riesgo")
    if d.c("diabetes_conocida") or d.v("hba1c") is not None and d.v("hba1c") >= 6.5 or d.c("enfermedad_cv_establecida") or d.c("embarazo") or (d.v("ldl_c") or 0) >= 190:
        return H(f, "no_calculable", nota="diabetes, enfermedad cardiovascular establecida, LDL ≥ 190 o embarazo: la calculadora no aplica; decide el médico")
    faltan = [k for k, v in dict(presion_sistolica=d.c("presion_sistolica"), tabaquismo=d.c("tabaquismo"),
                                 total_cholesterol=d.v("total_cholesterol"), hdl_c=d.v("hdl_c")).items() if v is None]
    if faltan: return H(f, "incompleta", faltan=faltan, nota="sin todas las entradas no se calcula porcentaje")
    sexo = d.c("sexo")
    riesgo, base = S2.score2_colombia(sexo, edad, bool(d.c("tabaquismo")), d.c("presion_sistolica"), d.v("total_cholesterol"), d.v("hdl_c"))
    pct = round(100 * riesgo, 1); cat = S2.categoria(edad, pct)
    extra = dict(riesgo_10_anos_pct=pct, categoria=cat, riesgo_sin_recalibrar_pct=round(100 * base, 1),
                 calculadora="SCORE2 región de riesgo alto × factor PURE-Colombia (0,61 hombres; 0,75 mujeres)",
                 modificadores_a_revisar=["COND-M1-CA-004 Lp(a)", "COND-M1-CA-A01 ApoB", "COND-M1-CA-A02 hs-CRP"])
    nota = "categorías por edad de la ESC 2021, provisionales hasta confirmar las de la GPC HTA 2025"
    if cat == "bajo_moderado": return H(f, "no_activa", nota=f"riesgo {pct} %: {nota}", extra=extra)
    return H(f, "activa", "alta", 2 if cat == "muy_alto" else 1, ["edad", "sexo", "presion_sistolica", "tabaquismo", "total_cholesterol", "hdl_c"], nota=nota, extra=extra)

def ca006(d):
    f = "COND-M1-CA-006"
    pas, pad = d.c("presion_sistolica"), d.c("presion_diastolica")
    if pas is None or pad is None: return H(f, "incompleta", faltan=["presion_enfermera"])
    if d.c("hipertension_conocida") or "antihipertensivo" in d.meds():
        return H(f, "control", nota="hipertensión conocida o en tratamiento: se lee como control")
    if not (pas >= 130 or pad >= 80): return H(f, "no_activa")
    ampa = d.c("ampa_promedio")  # dict(sistolica, diastolica, dias) desde Apple Health
    confirma = bool(ampa and ampa.get("dias", 0) >= 7 and (ampa["sistolica"] >= 130 or ampa["diastolica"] >= 80))
    esc = 3 if (pas >= 180 or pad >= 120) else 2 if (pas >= 140 or pad >= 90) else 1
    nota = []
    if d.c("notificacion_hipertension_apple"): nota.append("notificación de hipertensión del Apple Watch como contexto")
    return H(f, "activa", "alta" if confirma else "moderada", esc, ["pa_elevada"] + (["ampa_confirma"] if confirma else []),
             [] if ampa else ["automonitoreo de 7 días"], nota=" ".join(nota) or None,
             extra=dict(dispara=["aldosterone", "renin"]))

def ca007(d):
    f = "COND-M1-CA-007"
    diabetes = d.c("diabetes_conocida") or (d.v("hba1c") or 0) >= 6.5 or (d.v("glucose") or 0) >= 126
    if not diabetes: return H(f, "no_aplica", nota="sin diabetes: el NT-proBNP no se mide")
    n = d.v("nt_probnp")
    if n is None: return H(f, "pendiente_refleja", nota="diabetes en rango: el laboratorio debe correr NT-proBNP")
    if n < 125: return H(f, "no_activa")
    conf = [x for x, ok in [("TFG < 60", (d.calc("egfr") or 99) < 60), ("fibrilación auricular", d.c("fibrilacion_auricular")), ("edad ≥ 75", (d.c("edad") or 0) >= 75)] if ok]
    return H(f, "activa", "moderada" if conf else "alta", 2, ["ntprobnp_alto", "diabetes"], confusores=conf)

def ca_a01(d):
    f = "COND-M1-CA-A01"
    apob, ldl = d.v("apob"), d.v("ldl_c")
    if apob is None or ldl is None: return H(f, "incompleta", faltan=[x for x, v in [("apob", apob), ("ldl_c", ldl)] if v is None])
    if apob >= 130 and ldl < 130:
        util = (d.v("triglycerides") or 0) > 200 or d.c("diabetes_conocida")
        return H(f, "apoyo", nota="destacado: triglicéridos > 200 o diabetes" if util else None, extra=dict(modifica=["COND-M1-CA-001", "COND-M1-CA-005"]))
    return H(f, "no_activa")

def ca_a02(d):
    f = "COND-M1-CA-A02"
    c = d.v("hs_crp")
    if c is None: return H(f, "incompleta", faltan=["hs_crp"])
    if c > 10: return H(f, "no_activa", nota="hs-CRP > 10: proceso agudo probable; repetir")
    if c > 2:
        if d.c("infeccion_reciente"): return H(f, "no_activa", confusores=["infección reciente"], nota="repetir sin infección")
        return H(f, "apoyo", nota="a confirmar con una segunda medición", extra=dict(modifica=["COND-M1-CA-005"]))
    return H(f, "no_activa")

# =============================================================== M1 · Endocrinología metabólica
def em002(d):
    f = "COND-M1-EM-002"
    if d.c("embarazo"): return H(f, "no_interpretable", nota="embarazo")
    g = d.v("glucose") if d.interpretable("glucose") else None
    a = d.v("hba1c")
    if g is None and a is None: return H(f, "incompleta", faltan=["glucose", "hba1c"])
    cg, ca = g is not None and g >= 126, a is not None and a >= 6.5
    if not (cg or ca): return H(f, "no_activa")
    if d.c("diabetes_conocida"): return H(f, "control", nota="diabetes conocida: control en la vista médica")
    esc = 3 if d.clase("glucose") == "critico" else 2
    return H(f, "activa", "alta" if (cg and ca) else "moderada", esc, [k for k, v in [("glucosa_dm", cg), ("hba1c_dm", ca)] if v],
             extra=dict(dispara=["nt_probnp"]))

def em001(d, ya):
    f = "COND-M1-EM-001"
    if d.c("embarazo"): return H(f, "no_interpretable", nota="embarazo")
    if ya.get("COND-M1-EM-002", {}).get("estado") in ("activa", "control") or d.c("diabetes_conocida"):
        return H(f, "no_activa", nota="excluida: diabetes en rango o conocida")
    g = d.v("glucose") if d.interpretable("glucose") else None
    a = d.v("hba1c")
    cg = g is not None and 100 <= g <= 125
    ca = a is not None and 5.7 <= a <= 6.4
    if not (cg or ca):
        return H(f, "no_activa") if (g is not None or a is not None) else H(f, "incompleta", faltan=["glucose", "hba1c"])
    anemia = d.clase("hemoglobin") == "bajo"
    conf = ["anemia: baja la confianza de la HbA1c"] if anemia and ca else []
    if anemia and ca and not cg: return H(f, "vigilar", "baja", 1, ["hba1c"], confusores=conf)
    if "prednisona" in d.meds() or "corticoide" in d.meds(): conf.append("corticoides")
    return H(f, "activa", "alta" if (cg and ca) else "moderada", 1, [k for k, v in [("glucosa", cg), ("hba1c", ca)] if v], confusores=conf)

def em003(d):
    f = "COND-M1-EM-003"
    if not d.interpretable("glucose") or not d.interpretable("triglycerides"):
        return H(f, "no_interpretable", nota="ayuno insuficiente")
    meds = d.meds(); hombre = d.hombre
    comp = {}
    cin = d.c("cintura_cm"); comp["cintura"] = None if cin is None else cin >= (90 if hombre else 80)
    tg = d.v("triglycerides"); comp["trigliceridos"] = None if tg is None else (tg >= 150 or "fibrato" in meds)
    hdl = d.v("hdl_c"); comp["hdl"] = None if hdl is None else (hdl < (40 if hombre else 50))
    pas, pad = d.c("presion_sistolica"), d.c("presion_diastolica")
    comp["presion"] = None if pas is None else (pas >= 130 or (pad or 0) >= 85 or "antihipertensivo" in meds)
    g = d.v("glucose"); comp["glucosa"] = None if g is None else (g >= 100 or "metformina" in meds)
    si = [k for k, v in comp.items() if v]; faltan = [k for k, v in comp.items() if v is None]
    n = len(si)
    if n >= 3: return H(f, "activa", "alta" if not faltan else "moderada", 1, si, faltan, extra=dict(componentes=f"{n} de 5"))
    if n + len(faltan) >= 3: return H(f, "incompleta", cumplidos=si, faltan=faltan, extra=dict(componentes=f"{n} de 5 con {len(faltan)} sin medir"))
    return H(f, "no_activa", cumplidos=si)

def em004(d):
    f = "COND-M1-EM-004"
    if d.c("embarazo"): return H(f, "no_interpretable", nota="embarazo")
    imc = d.calc("imc")
    if imc is None: return H(f, "incompleta", faltan=["peso_kg", "talla_m"])
    cin = d.c("cintura_cm"); central = cin is not None and cin >= (90 if d.hombre else 80)
    if imc >= 30: return H(f, "activa", "alta", 2 if imc >= 40 else 1, ["obesidad"] + (["adiposidad_central"] if central else []), extra=dict(categoria="obesidad", imc=imc))
    if imc >= 25: return H(f, "activa", "alta", 1, ["sobrepeso"] + (["adiposidad_central"] if central else []), extra=dict(categoria="sobrepeso", imc=imc))
    return H(f, "no_activa", extra=dict(imc=imc))

def em005(d):
    f = "COND-M1-EM-005"
    g = d.v("glucose")
    if g is None or g >= 70: return H(f, "no_activa") if g is not None else H(f, "incompleta", faltan=["glucose"])
    lab = d.c("laboratorio", {})
    muestra = (d.r("glucose") or {}).get("muestra") or ""
    confiable = ("fluoruro" in muestra.lower()) and (lab.get("horas_toma_a_proceso") is None or lab["horas_toma_a_proceso"] <= lab.get("limite_horas_glucosa", 4))
    riesgo = any(m in d.meds() for m in ("insulina", "glibenclamida", "glimepirida", "sulfonilurea"))
    if g < 54: esc = 3 if confiable else 2
    else: esc = 2 if riesgo else 1
    return H(f, "activa", "alta" if confiable else "moderada", esc, ["glucosa_baja"] + (["glucosa_muy_baja"] if g < 54 else []),
             confusores=[] if confiable else ["muestra posiblemente no confiable: repetir"])

def em_a01(d, ya):
    f = "COND-M1-EM-A01"
    fr = d.c("findrisc_puntaje")
    if fr is None: return H(f, "incompleta", faltan=["findrisc_puntaje"])
    if fr < 12: return H(f, "no_activa")
    if ya.get("COND-M1-EM-001", {}).get("estado") == "activa": return H(f, "apoyo", nota="refuerza prediabetes", extra=dict(modifica=["COND-M1-EM-001"]))
    return H(f, "vigilar", "baja", nota="glucosa normal con riesgo alto: repetir tamizaje cuando indique el médico")

def em_a02(d, ya):
    f = "COND-M1-EM-A02"
    if "insulina" in d.meds(): return H(f, "no_aplica", nota="usa insulina")
    ins, hi, homa = d.v("insulin"), d.hi("insulin"), d.calc("homa_ir")
    si = (ins is not None and hi is not None and ins > hi) or (homa is not None and homa > 2.5)
    if not si: return H(f, "no_activa") if (ins is not None or homa is not None) else H(f, "incompleta", faltan=["insulin"])
    activas = [x for x in ("COND-M1-EM-001", "COND-M1-EM-003") if ya.get(x, {}).get("estado") == "activa"]
    if activas: return H(f, "apoyo", nota=f"HOMA-IR {homa}: refuerza {', '.join(activas)}", extra=dict(modifica=activas))
    return H(f, "vigilar", "baja", nota=f"HOMA-IR {homa} sin prediabetes ni síndrome metabólico")


# =============================================================== M2 · Nefrología
def estadio(egfr, uacr):
    g = None if egfr is None else "G1" if egfr >= 90 else "G2" if egfr >= 60 else "G3a" if egfr >= 45 else "G3b" if egfr >= 30 else "G4" if egfr >= 15 else "G5"
    a = None if uacr is None else "A1" if uacr < 30 else "A2" if uacr <= 300 else "A3"
    return g, a

def tfg_efectiva(d):
    comb = d.C.get("egfr_creatinina_cistatina")
    return comb["valor"] if comb and comb.get("calculado") else d.calc("egfr")

def ne001(d):
    f = "COND-M2-NE-001"
    e, u = d.calc("egfr"), d.v("uacr")
    if e is None: return H(f, "incompleta", faltan=["egfr"])
    previo = d.c("historial", {}) or {}
    alb_pers = u is not None and u >= 30 and (previo.get("uacr_hace_3_meses") or 0) >= 30
    tfg_baja = e < 60
    g, a = estadio(e, u)
    if not (tfg_baja or alb_pers):
        return H(f, "no_activa", extra=dict(estadio=f"{g}{' ' + a if a else ''}"))
    comb = d.C.get("egfr_creatinina_cistatina")
    if comb and comb.get("calculado") and comb["valor"] >= 60 and tfg_baja and not alb_pers:
        return H(f, "vigilar", "baja", nota=f"la TFG combinada con cistatina C ({comb['valor']}) no confirma", extra=dict(estadio=f"{g} {a or ''}".strip()))
    if comb and comb.get("calculado"):
        e = comb["valor"]; g, a = estadio(e, u); tfg_baja = e < 60
    confirmada = alb_pers or (tfg_baja and (previo.get("egfr_hace_3_meses") or 99) < 60)
    esc = 3 if g in ("G4", "G5") else 2 if g == "G3b" or (g == "G3a" and a in ("A2", "A3")) else 1 if g == "G3a" else 2 if a == "A3" else 1
    if d.clase("creatinine") == "critico": esc = 3
    return H(f, "activa", "alta" if confirmada else "moderada", esc, [k for k, v in [("tfg_baja", tfg_baja), ("albuminuria_persistente", alb_pers)] if v],
             [] if confirmada else ["confirmación a 3 meses"], extra=dict(estadio=f"{g} {a or ''}".strip(),
             dispara=["cystatin_c"] if (45 <= (d.calc('egfr') or 0) < 60 and (u is None or u < 30)) else []))

def ne002(d):
    f = "COND-M2-NE-002"
    u, e = d.v("uacr"), d.calc("egfr")
    if u is None: return H(f, "incompleta", faltan=["uacr"])
    if u < 30 or e is None or e < 60: return H(f, "no_activa")
    previo = (d.c("historial", {}) or {}).get("uacr_hace_3_meses")
    conf = [x for x, ok in [("ejercicio intenso 48 h", d.c("ejercicio_intenso_48h")), ("infección reciente", d.c("infeccion_reciente")),
                            ("menstruación", d.c("menstruacion_actual")),
                            ("infección urinaria en el uroanálisis", any((d.campos.get(("urinalysis", c)) or {}).get("clase") == "alterado" for c in ("nitritos", "esterasa leucocitaria")))] if ok]
    coin = "baja" if conf else ("alta" if (previo or 0) >= 30 else "moderada")
    return H(f, "activa" if coin != "baja" else "vigilar", coin, 2 if u > 300 else 1, ["a3" if u > 300 else "a2", "tfg_normal"],
             [] if previo is not None else ["segunda muestra"], conf, extra=dict(estadio=" ".join(x for x in estadio(e, u) if x)))

def ne003(d, ya):
    f = "COND-M2-NE-003"
    renal = [x for x in ("COND-M2-NE-001", "COND-M2-NE-002") if ya.get(x, {}).get("estado") in ("activa",)]
    if not renal: return H(f, "no_activa")
    diab = d.c("diabetes_conocida") or ya.get("COND-M1-EM-002", {}).get("estado") in ("activa", "control")
    ca6 = ya.get("COND-M1-CA-006", {})
    hta = d.c("hipertension_conocida") or ca6.get("estado") == "control" or (ca6.get("estado") == "activa" and ca6.get("coincidencia") == "alta")
    if diab or hta:
        base = ya[renal[0]]
        return H(f, "activa", base.get("coincidencia"), 2, [*renal, "diabetes" if diab else "hipertension"], extra=dict(estadio=base.get("estadio"), reemplaza=renal))
    if ca6.get("estado") == "activa": return H(f, "vigilar", "baja", nota="hallazgo renal con presión elevada sin confirmar")
    return H(f, "no_activa")

def ne004(d):
    f = "COND-M2-NE-004"
    if not d.interpretable("potassium"): return ni(f, d, "potassium")
    k, hi = d.v("potassium"), d.hi("potassium")
    if k is None: return H(f, "incompleta", faltan=["potassium"])
    if hi is None or k <= hi: return H(f, "no_activa")
    if d.c("laboratorio", {}).get("centrifugado_a_tiempo") is False:
        return H(f, "no_interpretable", nota="plasma no separado a tiempo: repetir")
    if d.clase("potassium") == "critico": return H(f, "activa", "alta", 3, ["k_alto", "bandera_critica"])
    retiene = any(m in d.meds() for m in ("losartan", "enalapril", "espironolactona", "potasio", "ieca", "ara ii"))
    if k >= 5.5:
        return H(f, "activa", "alta" if ((d.calc("egfr") or 99) < 60 or retiene) else "moderada", 2, ["k_accion"])
    return H(f, "activa", "moderada", 1, ["k_alto"], nota="repetir antes de concluir")

def ne005(d):
    f = "COND-M2-NE-005"
    na = d.v("sodium")
    if na is None: return H(f, "incompleta", faltan=["sodium"])
    ise = "ise indirecto" in ((d.r("sodium") or {}).get("metodo") or "").lower()
    if ise and ((d.v("triglycerides") or 0) >= 1000 or (d.v("total_protein") or 0) > 10):
        return H(f, "no_interpretable", nota="posible pseudohiponatremia con electrodo indirecto")
    corr = d.calc("sodio_corregido"); nae = corr if corr is not None else na
    if nae >= 135: return H(f, "no_activa", nota=f"sodio corregido {corr}" if corr is not None else None)
    esc = 3 if nae < 125 else 2 if nae < 130 else 1
    conf = [m for m in ("hidroclorotiazida", "clortalidona", "sertralina", "fluoxetina") if m in d.meds()]
    return H(f, "activa", "alta", esc, ["na_profundo" if nae < 125 else "na_moderado" if nae < 130 else "na_leve"], confusores=conf)

def ne006(d):
    f = "COND-M2-NE-006"
    r = d.campos.get(("urinalysis", "sedimento hematies"))
    if not r: return H(f, "incompleta", faltan=["sedimento urinario"])
    if r.get("clase") == "no_interpretable": return H(f, "no_interpretable", nota=r.get("motivo_clase"))
    m = re.findall(r"\d+", str(r.get("valor_original")))
    n = max(map(int, m)) if m else None
    if n is None or n <= 3: return H(f, "no_activa")
    glom = (d.v("uacr") or 0) >= 30 or (d.calc("egfr") or 99) < 60
    conf = [x for x, ok in [("ejercicio intenso 48 h", d.c("ejercicio_intenso_48h")), ("infección urinaria", any((d.campos.get(("urinalysis", c)) or {}).get("clase") == "alterado" for c in ("nitritos", "esterasa leucocitaria")))] if ok]
    return H(f, "activa", "moderada" if conf else "alta", 2 if (glom or n > 25) else 1, ["hematies"] + (["marcador_glomerular"] if glom else []), confusores=conf)

def ne_a01(d):
    f = "COND-M2-NE-A01"
    if d.r("potassium") and not d.interpretable("potassium"): return ni(f, d, "potassium")
    k, lo = d.v("potassium"), d.lo("potassium")
    if k is None or lo is None or k >= lo: return H(f, "no_activa") if k is not None else H(f, "incompleta", faltan=["potassium"])
    if k < 3.0: return H(f, "activa", "alta", 2, ["k_muy_bajo"], nota="mostrado como resultado observado")
    return H(f, "apoyo", extra=dict(modifica=["COND-M2-TI-008", "COND-M1-CA-006"]))

def egfr_cr_cys(d):
    """CKD-EPI 2021 creatinina-cistatina C (por verificar contra la publicación)."""
    cr, cys, edad, sexo = d.v("creatinine"), d.v("cystatin_c"), d.c("edad"), d.c("sexo")
    if None in (cr, cys, edad) or sexo not in ("hombre", "mujer"): return None
    k, a = (0.7, -0.219) if sexo == "mujer" else (0.9, -0.144)
    v = 135 * min(cr / k, 1) ** a * max(cr / k, 1) ** -0.544 * min(cys / 0.8, 1) ** -0.323 * max(cys / 0.8, 1) ** -0.778 * 0.9961 ** edad * (0.963 if sexo == "mujer" else 1)
    return round(v)

def ne_a02(d):
    f = "COND-M2-NE-A02"
    e, u = d.calc("egfr"), d.v("uacr")
    imc = d.calc("imc")
    indicada = (e is not None and 45 <= e < 60 and (u is None or u < 30)) or (imc is not None and imc >= 40) or d.c("objetivo") == "aumentar_masa_muscular"
    if not indicada: return H(f, "no_aplica")
    comb = egfr_cr_cys(d)
    if comb is None: return H(f, "pendiente_refleja", nota="el laboratorio debe correr cistatina C")
    return H(f, "apoyo", nota=f"TFG combinada {comb}: {'confirma' if comb < 60 else 'no confirma'} enfermedad renal", extra=dict(egfr_combinada=comb, modifica=["COND-M2-NE-001"]))

def ne_a03(d, ya):
    f = "COND-M2-NE-A03"
    b = d.v("bicarbonate")
    if b is None or b >= 22: return H(f, "no_activa")
    if ya.get("COND-M2-NE-001", {}).get("estado") == "activa" or ya.get("COND-M2-NE-003", {}).get("estado") == "activa":
        return H(f, "apoyo", nota="destacado: bicarbonato < 18" if b < 18 else None, extra=dict(modifica=["COND-M2-NE-001", "COND-M2-NE-003"]))
    return H(f, "no_activa", nota="bicarbonato bajo sin enfermedad renal: valor fuera de rango")


# =============================================================== M2 · Tiroides, paratiroides y suprarrenal
def _tiro_bloqueo(d, fid):
    if not d.interpretable("tsh"): return ni(fid, d, "tsh")
    if "levotiroxina" in d.meds(): return H(fid, "control", nota="toma levotiroxina: se lee como control")
    return None

def ti001(d):
    f = "COND-M2-TI-001"
    if d.c("embarazo"): return H(f, "no_aplica", nota="embarazo: va por TI-006")
    b = _tiro_bloqueo(d, f)
    if b: return b
    t, hi = d.v("tsh"), d.hi("tsh")
    if t is None or hi is None or t <= hi: return H(f, "no_activa")
    t4, t4lo, t4hi = d.v("free_t4"), d.lo("free_t4"), d.hi("free_t4")
    if t4 is None: return H(f, "pendiente_refleja", nota="TSH alta: el laboratorio debe correr T4 libre")
    if t4lo is not None and t4 < t4lo: return H(f, "no_activa", nota="T4 libre baja: va por TI-002")
    corte = 6.0 if (d.c("edad") or 0) > 60 else 5.0
    conf = [m for m in ("amiodarona", "litio") if m in d.meds()] + (["enfermedad aguda reciente"] if d.c("enfermedad_aguda_reciente") else [])
    if t <= corte: return H(f, "vigilar", "baja", None, ["tsh_sobre_lab"], nota=f"TSH sobre el laboratorio pero bajo el corte del consenso ({corte})")
    nota = "Si busca embarazo, comentarlo pronto con el médico." if (d.c("sexo") == "mujer" and 18 <= (d.c("edad") or 0) <= 45) else None
    return H(f, "activa", "moderada" if conf else "alta", 2 if t >= 10 else 1, ["tsh_sobre_consenso", "t4l_normal"], confusores=conf, nota=nota)

def ti002(d):
    f = "COND-M2-TI-002"
    if d.c("embarazo"): return H(f, "no_aplica", nota="embarazo: va por TI-006")
    b = _tiro_bloqueo(d, f)
    if b: return b
    t, hi, t4, lo = d.v("tsh"), d.hi("tsh"), d.v("free_t4"), d.lo("free_t4")
    if None in (t, hi) or t <= hi: return H(f, "no_activa")
    if t4 is None: return H(f, "pendiente_refleja")
    if lo is not None and t4 < lo:
        conf = [m for m in ("amiodarona", "litio") if m in d.meds()]
        return H(f, "activa", "moderada" if conf else "alta", 2, ["tsh_alta", "t4l_baja"], confusores=conf, extra=dict(excluye=["COND-M2-TI-001"]))
    return H(f, "no_activa")

def ti003(d):
    f = "COND-M2-TI-003"
    if d.c("embarazo"): return H(f, "no_aplica")
    b = _tiro_bloqueo(d, f)
    if b: return b
    t4, lo, t, hi = d.v("free_t4"), d.lo("free_t4"), d.v("tsh"), d.hi("tsh")
    if t4 is None: return H(f, "no_activa") if t is not None else H(f, "incompleta", faltan=["tsh"])
    if lo is not None and t4 < lo and t is not None and hi is not None and t <= hi:
        conf = (["corticoides"] if ("prednisona" in d.meds() or "corticoide" in d.meds()) else []) + (["enfermedad aguda reciente"] if d.c("enfermedad_aguda_reciente") else [])
        return H(f, "activa", "moderada" if conf else "alta", 2, ["t4l_baja", "tsh_no_alta"], confusores=conf)
    return H(f, "no_activa")

def ti004(d):
    f = "COND-M2-TI-004"
    if d.c("embarazo"): return H(f, "no_aplica")
    b = _tiro_bloqueo(d, f)
    if b: return b
    t, lo = d.v("tsh"), d.lo("tsh")
    if t is None or lo is None or t >= lo: return H(f, "no_activa")
    t4, t3 = d.v("free_t4"), d.v("free_t3")
    if t4 is None or t3 is None: return H(f, "pendiente_refleja", nota="TSH baja: el laboratorio debe correr T4 y T3 libres")
    if t4 > (d.hi("free_t4") or 99) or t3 > (d.hi("free_t3") or 99): return H(f, "no_activa", nota="hormonas altas: va por TI-005")
    conf = (["corticoides"] if "prednisona" in d.meds() else []) + (["enfermedad aguda reciente"] if d.c("enfermedad_aguda_reciente") else [])
    return H(f, "activa", "moderada" if conf else "alta", 2 if t < 0.1 else 1, ["tsh_baja", "t4l_normal", "t3l_normal"], confusores=conf)

def ti005(d):
    f = "COND-M2-TI-005"
    if d.c("embarazo"): return H(f, "no_aplica")
    b = _tiro_bloqueo(d, f)
    if b: return b
    t, lo = d.v("tsh"), d.lo("tsh")
    if t is None or lo is None or t >= lo: return H(f, "no_activa")
    t4, t3 = d.v("free_t4"), d.v("free_t3")
    a4, a3 = t4 is not None and t4 > (d.hi("free_t4") or 99), t3 is not None and t3 > (d.hi("free_t3") or 99)
    if not (a4 or a3): return H(f, "no_activa")
    esc = 3 if any(d.clase(x) == "critico" for x in ("free_t4", "free_t3")) else 2
    return H(f, "activa", "alta", esc, [k for k, v in [("t4l_alta", a4), ("t3l_alta", a3)] if v],
             extra=dict(variante="T3-toxicosis" if (a3 and not a4) else None, excluye=["COND-M2-TI-004"]))

def ti006(d):
    f = "COND-M2-TI-006"
    if not d.c("embarazo"): return H(f, "no_aplica")
    if not d.interpretable("tsh"): return ni(f, d, "tsh")
    t = d.v("tsh")
    if t is None: return H(f, "incompleta", faltan=["tsh"])
    if t > 4.0:
        sem = d.c("semana_gestacion")
        return H(f, "activa", "alta" if sem else "moderada", 2, ["tsh_alta_embarazo"] + (["t4l_baja"] if (d.v("free_t4") or 99) < (d.lo("free_t4") or 0) else []))
    if t < (d.lo("tsh") or 0): return H(f, "no_activa", nota="TSH baja en embarazo: resultado observado para el médico")
    return H(f, "no_activa")

def ti007(d):
    f = "COND-M2-TI-007"
    cc = d.calc("calcio_corregido"); hi = d.hi("calcium")
    if cc is None or hi is None: return H(f, "incompleta", faltan=["calcium", "albumin"])
    if cc <= hi: return H(f, "no_activa", nota=f"calcio corregido {cc}")
    p, plo, phi = d.v("pth"), d.lo("pth"), d.hi("pth")
    if p is None: return H(f, "pendiente_refleja", nota=f"calcio corregido {cc} alto: el laboratorio debe correr PTH")
    no_supr = (phi is not None and p > phi) or (plo is not None and phi is not None and p > (plo + phi) / 2)
    if not no_supr: return H(f, "no_activa", nota="PTH suprimida: buscar otra causa de calcio alto")
    previo = (d.c("historial", {}) or {}).get("calcio_corregido_alto_previo_2_semanas")
    conf = [m for m in ("hidroclorotiazida", "litio") if m in d.meds()] + (["TFG < 60"] if (d.calc("egfr") or 99) < 60 else [])
    return H(f, "activa", "alta" if previo else "moderada", 3 if cc >= 12 else 2, ["calcio_alto", "pth_no_suprimida"], confusores=conf)

def ti008(d, ya):
    f = "COND-M2-TI-008"
    ca6 = ya.get("COND-M1-CA-006", {})
    if not (ca6.get("estado") in ("activa", "control") or d.c("hipertension_conocida")):
        return H(f, "no_aplica", nota="sin presión ≥ 130/80 ni hipertensión conocida: no se piden aldosterona y renina")
    al, re_ = d.r("aldosterone"), d.r("renin")
    if not al or not re_ or d.v("aldosterone") is None or d.v("renin") is None:
        return H(f, "pendiente_refleja", nota="el laboratorio debe correr aldosterona y renina")
    lc = "lc-ms" in (al.get("metodo") or "").lower()
    a_ng = d.v("aldosterone") if (al.get("unidad") or "").lower().startswith("ng") else d.v("aldosterone") / 27.7
    ru = (re_.get("unidad") or "").lower().replace(" ", "")
    rv = d.v("renin")
    if "ng/ml/h" in ru: sup = rv <= 1.0; arr = a_ng / rv if rv else math.inf; arr_corte = 20
    elif "mu/l" in ru or "µui/ml" in ru or "uui/ml" in ru: sup = rv <= 8.2; arr = (a_ng * 27.7) / rv if rv else math.inf; arr_corte = 70
    else: return H(f, "no_interpretable", nota="tipo de renina no declarado (actividad o concentración)")
    if lc: arr_corte *= 0.75
    aldo_alta = a_ng >= (7.5 if lc else 10)
    meds = d.meds()
    conf = [m for m in ("metoprolol", "propranolol", "atenolol", "bisoprolol", "clonidina", "metildopa", "losartan", "enalapril", "espironolactona", "eplerenona", "hidroclorotiazida") if m in meds]
    if (d.calc("egfr") or 99) < 60: conf.append("TFG < 60")
    if sup and aldo_alta and arr > arr_corte:
        nota = None
        if any(m in meds for m in ("metoprolol", "propranolol", "atenolol", "bisoprolol")) and a_ng < 15:
            nota = "betabloqueador con aldosterona de 10 a 15 ng/dL: posible falso positivo"
        return H(f, "activa", "moderada" if conf else "alta", 2, ["renina_suprimida", "aldosterona_alta", "arr_alta"], confusores=conf, nota=nota, extra=dict(relacion=round(arr, 1)))
    if sup and 5 <= a_ng < 10 and not lc: return H(f, "no_activa", nota="zona para repetir otro día", extra=dict(relacion=round(arr, 1)))
    return H(f, "no_activa", extra=dict(relacion=round(arr, 1)))

def ti_a01(d, ya):
    f = "COND-M2-TI-A01"
    if not d.interpretable("anti_tpo") and d.r("anti_tpo"): return ni(f, d, "anti_tpo")
    tpo, tg = d.v("anti_tpo"), d.v("anti_tg")
    pos_tpo = tpo is not None and d.hi("anti_tpo") is not None and tpo > d.hi("anti_tpo")
    pos_tg = (not pos_tpo) and tg is not None and d.hi("anti_tg") is not None and tg > d.hi("anti_tg")
    if not (pos_tpo or pos_tg): return H(f, "no_activa") if (tpo is not None or tg is not None) else H(f, "no_aplica", nota="anticuerpos no medidos")
    mods = [x for x in ("COND-M2-TI-001", "COND-M2-TI-002", "COND-M2-TI-006") if ya.get(x, {}).get("estado") in ("activa", "vigilar")]
    return H(f, "apoyo", nota="causa autoinmune probable", extra=dict(modifica=mods))


# =============================================================== orquestación
# =============================================================== Aprobadas el 10 de octubre de 2026
PEPTIDO_C_BAJO = 0.6   # ng/mL, por verificar (ADA 2025)
TYG_CORTE, TG_HDL_CORTE = 8.8, 3.0   # provisionales, por verificar
CORTICOIDES = ("prednisolona", "prednisona", "dexametasona", "betametasona", "hidrocortisona", "metilprednisolona", "deflazacort",
               "budesonida", "fluticasona", "beclometasona", "mometasona", "clobetasol", "triamcinolona")

def em_a03(d, ya):
    f = "COND-M1-EM-A03"
    diab = ya.get("COND-M1-EM-002", {}).get("estado") in ("activa", "control") or d.c("diabetes_conocida")
    if not diab: return H(f, "no_aplica", nota="sin diabetes en rango ni conocida")
    cp = d.v("c_peptide")
    if cp is None: return H(f, "incompleta", faltan=["c_peptide"])
    if cp >= PEPTIDO_C_BAJO: return H(f, "no_activa")
    conf = ["glucosa muy alta (puede bajar el péptido C de forma pasajera)"] if (d.v("glucose") or 0) >= 250 else []
    return H(f, "apoyo", cumplidos=["diabetes", "peptido_c_bajo"], confusores=conf,
             nota=f"péptido C {cp:g} ng/mL: posible falta de insulina (tipo 1 o LADA); corte {PEPTIDO_C_BAJO} por verificar",
             extra=dict(modifica=["COND-M1-EM-002"]))

def em_a04(d, ya):
    f = "COND-M1-EM-A04"
    if ya.get("COND-M1-EM-002", {}).get("estado") in ("activa", "control") or d.c("diabetes_conocida"):
        return H(f, "no_aplica", nota="en diabetes no aporta")
    t, r = d.calc("tyg_index"), d.calc("tg_hdl_ratio")
    if t is None and r is None: return H(f, "incompleta", faltan=["tyg_index", "tg_hdl_ratio"])
    cum = [k for k, ok in (("tyg_alto", t is not None and t > TYG_CORTE), ("tg_hdl_alta", r is not None and r > TG_HDL_CORTE)) if ok]
    if not cum: return H(f, "no_activa", extra=dict(tyg_index=t, tg_hdl_ratio=r))
    return H(f, "apoyo", cumplidos=cum, nota=f"TyG {t}, TG/HDL {r}; cortes provisionales {TYG_CORTE} y {TG_HDL_CORTE}",
             extra=dict(modifica=["COND-M1-EM-001", "COND-M1-EM-003"], tyg_index=t, tg_hdl_ratio=r))

def ti009(d):
    f = "COND-M2-TI-009"
    if not d.r("cortisol"): return H(f, "incompleta", faltan=["cortisol"])
    if not d.interpretable("cortisol"): return ni(f, d, "cortisol")
    cort = [m for m in CORTICOIDES if m in d.meds()]
    if cort: return H(f, "no_interpretable", nota=f"corticoide declarado ({', '.join(cort)}): suprime el cortisol")
    v = d.v("cortisol")
    if v is None or v >= 5: return H(f, "no_activa")
    refuerzo = [k for k, ok in (("acth_alta", d.clase("acth") == "alto"), ("sodio_bajo", d.clase("sodium") == "bajo"), ("potasio_alto", d.clase("potassium") == "alto")) if ok]
    return H(f, "activa", "alta" if refuerzo else "moderada", 2, ["cortisol_bajo"] + refuerzo, nota="corte de 5 µg/dL por verificar (Endocrine Society 2016)")


def evaluar_m1m2(p1, ctx):
    d = Datos(p1, ctx)
    comb = egfr_cr_cys(d)
    if comb is not None:
        p1["calculados"]["egfr_creatinina_cistatina"] = dict(id="egfr_creatinina_cistatina", calculado=True, valor=comb,
            formula="CKD-EPI 2021 creatinina-cistatina C (por verificar)", entradas=dict(creatinine=d.v("creatinine"), cystatin_c=d.v("cystatin_c")))
        d = Datos(p1, ctx)
    ya = {}
    def put(h): ya[h["ficha"]] = h
    for fn in (ca001, ca002, ca003, ca004, ca005, ca006, ca007, ca_a01, ca_a02, em002): put(fn(d))
    put(em001(d, ya)); put(em003(d)); put(em004(d)); put(em005(d)); put(em_a01(d, ya)); put(em_a02(d, ya))
    for fn in (ne001, ne002): put(fn(d))
    put(ne003(d, ya))
    for fn in (ne004, ne005, ne006, ne_a01, ne_a02): put(fn(d))
    put(ne_a03(d, ya))
    for fn in (ti001, ti002, ti003, ti004, ti005, ti006, ti007): put(fn(d))
    put(ti008(d, ya)); put(ti_a01(d, ya))
    put(em_a03(d, ya)); put(em_a04(d, ya)); put(ti009(d))
    # exclusiones entre condiciones
    if ya["COND-M1-CA-002"]["estado"] == "activa" and ya["COND-M1-CA-001"]["estado"] == "activa":
        ya["COND-M1-CA-001"].update(estado="no_activa", nota="excluida: manda CA-002")
    if ya["COND-M2-TI-002"]["estado"] == "activa": ya["COND-M2-TI-001"].update(estado="no_activa", nota="excluida: manda TI-002")
    if ya["COND-M2-NE-003"]["estado"] == "activa":
        for x in ya["COND-M2-NE-003"].get("reemplaza", []):
            ya[x]["oculta_en_informe_paciente"] = True
    return ya
