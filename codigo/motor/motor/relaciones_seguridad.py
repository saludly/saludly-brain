"""
Saludly Brain · Motor · Parte 4: relaciones entre módulos, seguridad y salida final

- 27 relaciones (documento REL): patrones que agrupan condiciones, patrones propios,
  señales para vigilar y una relación "fuera de patrones".
- 15 fichas de seguridad (SEG-000 a SEG-014) para los biomarcadores sin condición propia.
- Ensamble final: lista ordenada de hallazgos para el informe del paciente, vista médica,
  escalamiento máximo y canal de comunicación.
"""
import glob, os, re, yaml
from condiciones_m1m2 import Datos
from condiciones_m3m6 import ferritina_corte, b12_baja, _reactivo, _campo

BASE = os.path.dirname(os.path.abspath(__file__))
REL = {}
for p in glob.glob(f"{BASE}/kb/relaciones/*.md"):
    s = open(p, encoding="utf-8").read()
    y = yaml.safe_load(re.search(r"```yaml\n(.*?)```", s, re.S).group(1)); REL[y["id"]] = y
SEGF = {}
for p in glob.glob(f"{BASE}/kb/seguridad/*.md"):
    s = open(p, encoding="utf-8").read()
    y = yaml.safe_load(re.search(r"```yaml\n(.*?)```", s, re.S).group(1)); SEGF[y["id"]] = y


def R(rid, estado, miembros=None, escalamiento=None, nota=None, senales=None):
    y = REL.get(rid, {})
    return dict(relacion=rid, nombre=y.get("nombre"), tipo=y.get("tipo"), estado=estado, miembros=miembros or [],
                escalamiento=escalamiento, senales=senales or [], nota=nota, fuerza_evidencia=y.get("fuerza_evidencia"),
                frase_permitida=y.get("frase_permitida"))

def _act(h, *ids): return [i for i in ids if h.get(i, {}).get("estado") in ("activa", "apoyo")]
def _alto(d, b): return d.clase(b) == "alto"
def _bajo(d, b): return d.clase(b) == "bajo"


# =============================================================== relaciones
def evaluar_relaciones(d, h):
    out = {}
    def put(r): out[r["relacion"]] = r
    glu = (d.v("glucose") or 0) >= 100 if d.interpretable("glucose") else False
    a1c = (d.v("hba1c") or 0) >= 5.7
    ins = _alto(d, "insulin") or (d.calc("homa_ir") or 0) > 2.5
    tg = (d.v("triglycerides") or 0) >= 150
    hdl = d.v("hdl_c") is not None and d.v("hdl_c") < (40 if d.hombre else 50)
    s1 = [k for k, ok in (("glucemico", glu or a1c), ("insulina", ins), ("trigliceridos", tg), ("hdl_bajo", hdl)) if ok]
    m1 = _act(h, "COND-M1-EM-001", "COND-M1-EM-002", "COND-M1-EM-003", "COND-M1-CA-003", "COND-M1-EM-A02")
    put(R("REL-001", "activa", m1, None, senales=s1) if ("glucemico" in s1 and len(s1) >= 2) else R("REL-001", "no_activa", senales=s1))
    crp = d.v("hs_crp") or 0
    put(R("REL-002", "vigilar", nota=f"hs-CRP {crp}") if out["REL-001"]["estado"] == "activa" and crp > 2 and not d.c("infeccion_reciente") else R("REL-002", "no_activa"))
    apob = _alto(d, "apob") or (d.v("apob") or 0) >= 130
    lipo = (d.v("ldl_c") or 0) >= 130 or (d.calc("non_hdl_c") or 0) >= 160
    m3 = _act(h, "COND-M1-CA-001", "COND-M1-CA-002", "COND-M1-CA-004", "COND-M1-CA-A01")
    put(R("REL-003", "activa", m3, senales=["apob_alta", "ldl_o_no_hdl_alto"]) if (apob and lipo) else R("REL-003", "no_activa"))
    s4 = [k for k, ok in (("hs_crp", crp > 2), ("fibrinogeno", _alto(d, "fibrinogen")), ("homocisteina", _alto(d, "homocysteine"))) if ok]
    put(R("REL-004", "vigilar", senales=s4) if len(s4) >= 2 else R("REL-004", "no_activa", senales=s4))
    alto_card = d.clase("hs_troponin") == "critico" or (d.v("nt_probnp") or 0) >= 125
    put(R("REL-005", "derivada_a_seguridad" if alto_card else "no_activa", nota="sigue su regla de seguridad" if alto_card else None))
    enz = _alto(d, "alt") or _alto(d, "ggt")
    meta = tg or (d.calc("homa_ir") or 0) > 2.5 or a1c
    m6 = _act(h, "COND-M4-GA-002", "COND-M4-GA-001", "COND-M1-EM-001", "COND-M1-CA-003")
    put(R("REL-006", "activa", m6, senales=["enzima_hepatica", "senal_metabolica"], nota=f"FIB-4 {d.calc('fib4')}") if (enz and meta) else R("REL-006", "no_activa"))
    s7 = [k for k, ok in (("hs_crp_>5", crp > 5), ("vsg", _alto(d, "esr")), ("fibrinogeno", _alto(d, "fibrinogen"))) if ok]
    put(R("REL-007", "vigilar", senales=s7) if len(s7) >= 2 else R("REL-007", "no_activa", senales=s7))
    musc = _alto(d, "ck_cpk") and (_alto(d, "ast") or _alto(d, "ldh"))
    put(R("REL-008", "activa", nota="AST y LDH de origen muscular probable: confusor de pruebas hepáticas") if musc else R("REL-008", "no_activa"))
    anemia = h.get("COND-M3-HE-001", {}).get("estado") == "activa"
    retic = _alto(d, "reticulocytes_pct") or _alto(d, "reticulocytes_abs")
    bi = _alto(d, "bilirubin_total") and not _alto(d, "bilirubin_direct")
    put(R("REL-009", "activa", ["COND-M3-HE-001"], 2, senales=["anemia", "reticulocitos_altos"] + (["bilirrubina_indirecta"] if bi else []) + (["ldh"] if _alto(d, "ldh") else []))
        if (anemia and retic and (bi or _alto(d, "ldh"))) else R("REL-009", "no_activa"))
    u, e = d.v("uacr"), d.calc("egfr")
    put(R("REL-010", "activa", _act(h, "COND-M2-NE-001", "COND-M2-NE-003"), senales=["albuminuria", "tfg_baja"]) if (u is not None and u >= 30 and e is not None and e < 60) else R("REL-010", "no_activa"))
    comb = d.C.get("egfr_creatinina_cistatina")
    cat = lambda x: None if x is None else (0 if x >= 90 else 1 if x >= 60 else 2 if x >= 45 else 3 if x >= 30 else 4 if x >= 15 else 5)
    put(R("REL-011", "activa", ["COND-M2-NE-A02"], nota=f"TFG creatinina {e} frente a combinada {comb['valor']}") if (comb and comb.get("calculado") and cat(e) != cat(comb["valor"])) else R("REL-011", "no_activa"))
    put(R("REL-012", "activa", ["COND-M2-NE-001"], nota="PTH alta dentro de enfermedad renal") if (_alto(d, "pth") and e is not None and e < 60) else R("REL-012", "no_activa"))
    fe = d.v("ferritin")
    fe_baja = fe is not None and fe < ferritina_corte(d); fe_lim = fe is not None and fe < 30
    s13 = [k for k, ok in (("saturacion_baja", (d.v("transferrin_saturation") or 99) < 20), ("rdw_alto", _alto(d, "rdw")), ("vcm_bajo", _bajo(d, "mcv"))) if ok]
    put(R("REL-013", "activa", _act(h, "COND-M3-HE-001", "COND-M3-HE-002", "COND-M3-HE-003"), senales=["ferritina_baja"] + s13) if ((fe_baja or fe_lim) and s13) else R("REL-013", "no_activa"))
    put(R("REL-014", "activa", ["COND-M3-HE-001", "COND-M3-HE-A01"], 2) if h.get("COND-M3-HE-A01", {}).get("estado") == "apoyo" else R("REL-014", "no_activa"))
    def_vit = b12_baja(d) or (d.v("folate") is not None and d.v("folate") < 4)
    put(R("REL-015", "activa", _act(h, "COND-M3-NU-001", "COND-M3-NU-002", "COND-M3-HE-004", "COND-M3-NU-A01")) if (def_vit and _alto(d, "homocysteine")) else R("REL-015", "no_activa"))
    ac = _alto(d, "anti_tpo") or _alto(d, "anti_tg")
    put(R("REL-016", "vigilar") if (fe_baja and ac) else R("REL-016", "no_activa"))
    t4, t4lo, t4hi = d.v("free_t4"), d.lo("free_t4"), d.hi("free_t4")
    t4_lim = t4 is not None and t4lo is not None and t4hi is not None and t4 < t4lo + 0.1 * (t4hi - t4lo)
    put(R("REL-017", "activa", _act(h, "COND-M2-TI-001", "COND-M2-TI-002", "COND-M2-TI-A01"), senales=["tsh_alta"] + (["t4l_baja_o_limite"] if t4_lim else []) + (["anticuerpos"] if ac else []))
        if (_alto(d, "tsh") and (t4_lim or ac)) else R("REL-017", "no_activa"))
    s18 = [k for k, ok in (("colesterol", _alto(d, "total_cholesterol") or _alto(d, "ldl_c")), ("ck", _alto(d, "ck_cpk")), ("homocisteina", _alto(d, "homocysteine"))) if ok]
    put(R("REL-018", "vigilar", senales=s18, nota="reevaluar lípidos tras corregir la tiroides") if (_alto(d, "tsh") and s18) else R("REL-018", "no_activa"))
    put(R("REL-019", "vigilar") if (d.clase("tsh") in ("alto", "bajo") and (fe_baja or (d.v("transferrin_saturation") or 99) < 20)) else R("REL-019", "no_activa"))
    vitd = _bajo(d, "vitamin_d")
    cc_alt = d.calc("calcio_corregido") is not None and d.hi("calcium") is not None and not (d.lo("calcium") <= d.calc("calcio_corregido") <= d.hi("calcium"))
    put(R("REL-020", "activa", ["COND-M3-NU-A02", "COND-M3-NU-A03"], 1) if (vitd and _alto(d, "pth") and (cc_alt or d.clase("phosphorus") in ("alto", "bajo"))) else R("REL-020", "no_activa"))
    put(R("REL-021", "vigilar") if (vitd and crp > 2) else R("REL-021", "no_activa"))
    put(R("REL-022", "vigilar") if (vitd and (fe_baja or anemia)) else R("REL-022", "no_activa"))
    w = d.c("wearable") or {}
    fc_alta = bool(w.get("activo") and w.get("fc_reposo_alta"))
    s23 = [k for k, ok in (("glucosa", _alto(d, "glucose") or _alto(d, "hba1c")), ("presion", (d.c("presion_sistolica") or 0) >= 130 or (d.c("presion_diastolica") or 0) >= 80), ("fc_reposo", fc_alta)) if ok]
    put(R("REL-023", "vigilar", senales=s23, nota="nunca se nombra hipercortisolismo") if (d.clase("cortisol") == "alto" and len(s23) >= 2) else R("REL-023", "no_activa"))
    tb = h.get("COND-M5-UR-002", {}).get("estado") in ("activa", "vigilar")
    put(R("REL-024", "activa", _act(h, "COND-M5-UR-002", "COND-M5-UR-A01")) if (tb and (d.clase("shbg") in ("alto", "bajo") or d.clase("lh") in ("alto", "bajo"))) else R("REL-024", "no_activa"))
    horm = any(d.clase(b) in ("alto", "bajo") for b in ("estradiol", "progesterone"))
    if not horm: put(R("REL-025", "no_activa"))
    elif not w.get("activo"): put(R("REL-025", "incompleta", nota="sin Apple Watch activo"))
    else: put(R("REL-025", "vigilar") if w.get("temperatura_alterada") else R("REL-025", "no_activa"))
    tsh_alt = d.clase("tsh") in ("alto", "bajo")
    if not tsh_alt: put(R("REL-026", "no_activa"))
    elif not w.get("activo"): put(R("REL-026", "incompleta", nota="sin Apple Watch activo"))
    else: put(R("REL-026", "vigilar") if (w.get("fc_reposo_alta") or w.get("sueno_alterado") or w.get("actividad_baja")) else R("REL-026", "no_activa"))
    mu3 = h.get("COND-M5-MU-003", {})
    put(R("REL-027", "activa", ["COND-M5-MU-003", "COND-M2-TI-001"]) if (mu3.get("estado") in ("activa", "vigilar") and mu3.get("escalamiento") != 0 and (_alto(d, "tsh") or mu3.get("confusores_aplicados"))) else R("REL-027", "no_activa"))
    return out


# =============================================================== seguridad
def S(sid, escalamiento, detalle, revision=False, canal=None):
    return dict(seguridad=sid, nombre=SEGF.get(sid, {}).get("nombre"), estado="activa" if escalamiento else "sin_hallazgo",
                escalamiento=escalamiento, detalle=detalle, revision_medica_obligatoria=revision, canal=canal)

def evaluar_seguridad(d, h):
    out = {}; meds = d.meds()
    def put(s): out[s["seguridad"]] = s
    # SEG-001 troponina
    c = d.clase("hs_troponin")
    put(S("SEG-001", 3 if c == "critico" else 0, ["troponina sobre el percentil 99: llamada el mismo día"] if c == "critico" else [], True, "llamada" if c == "critico" else None))
    # SEG-002 cortisol y ACTH
    det, esc = [], 0
    if d.clase("cortisol") == "bajo": det.append("cortisol bajo en la mañana"); esc = 2
    elif d.clase("cortisol") == "alto": det.append("cortisol alto"); esc = max(esc, 1)
    elif d.clase("cortisol") == "critico": det.append("cortisol con bandera crítica"); esc = 3
    if d.clase("acth") in ("alto", "bajo"): det.append("ACTH fuera de rango (interpretación solo para el médico)"); esc = max(esc, 1)
    if d.clase("cortisol") == "no_interpretable": det.append(f"cortisol no interpretable: {d.motivo_no('cortisol')}")
    put(S("SEG-002", esc, det, True))
    put(S("SEG-003", 1 if d.clase("igf1") in ("alto", "bajo") else 0, ["IGF-1 fuera del rango para la edad"] if d.clase("igf1") in ("alto", "bajo") else [], True))
    br = d.calc("brecha_osmolar")
    put(S("SEG-004", 2 if (br or 0) > 10 else 0, [f"brecha osmolar {br}"] if (br or 0) > 10 else [], True, "llamada" if (br or 0) > 10 else None))
    nr = d.v("nrbc") or 0
    if nr > 0:
        grave = h.get("COND-M3-HE-001", {}).get("severidad") == "severa" or (d.v("platelets") or 999) < 100
        e5 = 1 if d.c("esplenectomia") else 3 if grave else 2
        put(S("SEG-005", e5, [f"eritroblastos {nr}"], True, "llamada" if e5 >= 2 else None))
    else: put(S("SEG-005", 0, [], True))
    # SEG-006 coagulación
    det, esc = [], 0
    anticoag = any(m in meds for m in ("warfarina", "acenocumarol"))
    if _alto(d, "inr") and not anticoag: det.append("INR alto sin anticoagulante"); esc = 2
    if anticoag and d.v("inr") is not None: det.append("INR en tratamiento: control en la vista médica")
    if _bajo(d, "fibrinogen") and _alto(d, "pt") and (d.v("platelets") or 999) < 100: det.append("patrón de coagulopatía"); esc = 3
    if _alto(d, "fibrinogen"): det.append("fibrinógeno alto: relación de inflamación (vigilar)")
    put(S("SEG-006", esc, det))
    # SEG-007 CK y LDH
    det, esc = [], 0
    ck, ckhi = d.v("ck_cpk"), d.hi("ck_cpk")
    if ck is not None and ckhi and ck > ckhi:
        if ck > 5 * ckhi:
            if d.c("orina_oscura") or d.c("dolor_muscular_intenso"): esc = 3; det.append("CK muy alta con síntomas: urgencias")
            elif d.c("ejercicio_intenso_48h"): esc = 1; det.append("CK muy alta tras ejercicio: repetir")
            else: esc = 2; det.append("CK muy alta sin ejercicio")
        else: esc = 1; det.append("CK alta: repetir sin ejercicio")
    if _alto(d, "ldh") and not musc_o_hemol(d, h): esc = max(esc, 1); det.append("LDH alta aislada")
    put(S("SEG-007", esc, det))
    # SEG-008 electrolitos
    det, esc = [], 0
    if d.clase("magnesium") in ("alto", "bajo"):
        esc = 2 if (_bajo(d, "potassium") or (d.calc("calcio_corregido") or 99) < (d.lo("calcium") or 0)) else 1; det.append("magnesio fuera de rango")
    for b in ("chloride", "phosphorus"):
        if d.clase(b) in ("alto", "bajo") and not (b == "phosphorus" and (d.calc("egfr") or 99) < 60): esc = max(esc, 1); det.append(f"{b} fuera de rango")
    put(S("SEG-008", esc, det))
    # SEG-009 proteínas
    det, esc = [], 0
    ag = d.calc("ag_ratio")
    if ag is not None and ag < 1.0: esc = 1; det.append(f"relación A/G {ag}: considerar electroforesis")
    for b in ("igg", "igm"):
        v, hi = d.v(b), d.hi(b)
        if v is not None and hi and v > 2 * hi: esc = 2; det.append(f"{b} muy alta")
    if _bajo(d, "igg") and d.c("infecciones_repetidas"): esc = 2; det.append("IgG baja con infecciones repetidas")
    put(S("SEG-009", esc, det))
    # SEG-010 metabolismo
    det, esc = [], 0
    if d.clase("c_peptide") in ("alto", "bajo"): esc = 1; det.append("péptido C fuera de rango")
    if (d.v("albumin") or 9) < 3.0 and d.r("fructosamine"): det.append("fructosamina no interpretable: albúmina < 3,0")
    elif d.clase("fructosamine") in ("alto", "bajo"): esc = max(esc, 1); det.append("fructosamina fuera de rango")
    nt = d.v("nt_probnp")
    diab = d.c("diabetes_conocida") or (d.v("hba1c") or 0) >= 6.5
    if nt is not None and not diab and nt >= 125:
        edad = d.c("edad") or 0; corte = 450 if edad < 50 else 900 if edad <= 75 else 1800
        esc = max(esc, 2 if nt > corte else 1); det.append(f"NT-proBNP {nt} sin diabetes")
    put(S("SEG-010", esc, det))
    # SEG-011 hormonas sin condición
    det, esc = [], 0
    dh, dhhi = d.v("dhea_s"), d.hi("dhea_s")
    if dh is not None and dhhi and dh > dhhi:
        esc = 2 if (d.c("sexo") == "mujer" and dh > 2 * dhhi) else 1; det.append("DHEA-S alta")
    elif _bajo(d, "dhea_s"): esc = 1; det.append("DHEA-S baja")
    for b in ("estradiol", "lh", "progesterone"):
        if d.clase(b) in ("alto", "bajo"): esc = max(esc, 1); det.append(f"{b} fuera del rango de la fase")
    put(S("SEG-011", esc, det))
    # SEG-012 hemograma sin condición (lo que explica una anemia activa no se reporta aparte)
    det, esc = [], 0
    anemia = h.get("COND-M3-HE-001", {}).get("estado") == "activa"
    for b in ("monocytes_pct", "basophils_pct", "mpv", "mch", "mchc", "hematocrit", "erythrocytes"):
        if d.clase(b) in ("alto", "bajo"):
            if anemia and b in ("mch", "mchc", "hematocrit", "erythrocytes"): continue
            if b == "mpv" and d.clase("platelets") not in ("alto", "bajo"): continue
            esc = 1; det.append(f"{b} fuera de rango: repetir")
    put(S("SEG-012", esc, det))
    # SEG-013 orina y heces
    det, esc = [], 0
    pos = lambda c: str(_campo(d, "urinalysis", c).get("valor") or "").lower().startswith("positivo")
    if pos("proteinas") and (d.v("uacr") is None): esc = 1; det.append("proteína en tira sin relación albúmina/creatinina")
    if pos("glucosa"):
        if any(m in meds for m in ("empagliflozina", "dapagliflozina", "canagliflozina")): det.append("glucosa en orina esperada por iSGLT2")
        elif (d.v("glucose") or 0) < 126: esc = max(esc, 1); det.append("glucosa en orina con glucosa en sangre normal")
    if pos("cuerpos cetonicos") and ((d.v("glucose") or 0) >= 200 or d.c("diabetes_conocida")): esc = 2; det.append("cetonas con glucosa alta o diabetes")
    if pos("bilirrubina"): esc = max(esc, 2); det.append("bilirrubina en orina")
    uro = _campo(d, "urinalysis", "urobilinogeno")
    if uro.get("clase") == "alto": esc = max(esc, 1); det.append("urobilinógeno alto")
    if str(_campo(d, "stool_exam", "coprologico sangre").get("valor") or "").lower().startswith("positivo"): esc = max(esc, 2); det.append("sangre visible en heces")
    put(S("SEG-013", esc, det))
    # SEG-014 contexto
    det, esc = [], 0
    if d.r("zinc") and not (d.c("laboratorio") or {}).get("tubo_libre_de_zinc", True): det.append("zinc no interpretable: tubo estándar")
    elif _bajo(d, "zinc"): det.append("zinc bajo: recomendación alimentaria")
    if _alto(d, "bun") and not _alto(d, "creatinine"): det.append("BUN alto con creatinina normal: hidratación o dieta")
    if (d.calc("bun_creatinine_ratio") or 0) > 20: det.append("relación BUN/creatinina > 20: vigilar hidratación")
    put(S("SEG-014", 0, det))
    # SEG-000 regla general para el resto de solo valor y rango (críticos del laboratorio)
    crit = [r["biomarker_id"] for r in d.R.values() if r.get("clase") == "critico" and r["biomarker_id"] not in ("hs_troponin", "glucose")]
    put(S("SEG-000", 3 if crit else 0, [f"bandera crítica: {', '.join(crit)}"] if crit else [], canal="llamada" if crit else None))
    return out

def musc_o_hemol(d, h):
    return (_alto(d, "ck_cpk") and _alto(d, "ast")) or (h.get("COND-M3-HE-001", {}).get("estado") == "activa" and (_alto(d, "reticulocytes_pct") or _alto(d, "reticulocytes_abs")))


# =============================================================== ensamble final
ORDEN_COIN = {"alta": 0, "moderada": 1, "baja": 2, None: 3}
ORDEN_FUERZA = {"guia": 0, "guía": 0, "mecanismo bien establecido": 1, "metaanalisis": 1, "cohorte": 2, "asociacion": 3, "asociación": 3, None: 2}

def ensamblar(cond, rels, segs, p1, ctx):
    # La edad biológica va en una pantalla aparte (COND-M6-MI-A02), no en la lista de hallazgos
    activas = {k: v for k, v in cond.items() if v["estado"] == "activa" and not v.get("oculta_en_informe_paciente") and k != "COND-M6-MI-A02"}
    agrupadas, grupos, patrones_de = set(), [], {}
    for r in rels.values():
        if r["tipo"] != "patron" or r["estado"] != "activa": continue
        libres = [m for m in r["miembros"] if m in activas and m not in agrupadas]
        ya = [m for m in r["miembros"] if m in agrupadas]
        if len(libres) >= 2:
            esc = max([activas[m]["escalamiento"] or 0 for m in libres] + [r["escalamiento"] or 0])
            grupos.append(dict(tipo="patron", id=r["relacion"], nombre=r["nombre"], escalamiento=esc, coincidencia="alta",
                               miembros=libres, relacionado_con=ya, frase_permitida=r.get("frase_permitida"), fuerza=r.get("fuerza_evidencia")))
            agrupadas.update(libres)
        elif libres:
            for m in libres: patrones_de.setdefault(m, []).append(dict(id=r["relacion"], nombre=r["nombre"], relacionado_con=ya))
        elif r["relacion"] in ("REL-009", "REL-012", "REL-020") and r["escalamiento"]:
            grupos.append(dict(tipo="patron_propio", id=r["relacion"], nombre=r["nombre"], escalamiento=r["escalamiento"], coincidencia="alta",
                               miembros=r["miembros"], fuerza=r.get("fuerza_evidencia")))
    for k, v in activas.items():
        if k in agrupadas: continue
        grupos.append(dict(tipo="condicion", id=k, nombre=v["nombre"], escalamiento=v["escalamiento"] or 0, coincidencia=v.get("coincidencia"),
                           nivel_lenguaje=v.get("nivel_lenguaje"), nota=v.get("nota"), fuerza="guia", patrones=patrones_de.get(k, [])))
    for s in segs.values():
        if s["escalamiento"]:
            grupos.append(dict(tipo="seguridad", id=s["seguridad"], nombre=s["nombre"], escalamiento=s["escalamiento"], coincidencia=None, detalle=s["detalle"], fuerza="guia"))
    TIPO = {"seguridad": 0, "patron_propio": 1, "patron": 1, "condicion": 2}
    grupos.sort(key=lambda g: (-(g["escalamiento"] or 0), TIPO[g["tipo"]], ORDEN_COIN.get(g.get("coincidencia"), 3), ORDEN_FUERZA.get(g.get("fuerza"), 2), g["id"]))
    esc_max = max([g["escalamiento"] or 0 for g in grupos] + [0])
    llamadas = [g["id"] for g in grupos if g["escalamiento"] == 3] + [k for k, v in cond.items() if v["estado"] in ("activa", "pendiente_refleja") and (v.get("canal") == "llamada del médico")]
    vista = dict(
        vigilar=[dict(id=k, nombre=v["nombre"], nota=v.get("nota")) for k, v in cond.items() if v["estado"] == "vigilar"]
               + [dict(id=k, nombre=r["nombre"], nota=r.get("nota")) for k, r in rels.items() if r["estado"] == "vigilar"],
        apoyos=[dict(id=k, nombre=v["nombre"], nota=v.get("nota")) for k, v in cond.items() if v["estado"] == "apoyo"],
        control=[k for k, v in cond.items() if v["estado"] == "control"],
        pendientes_refleja=[dict(id=k, nota=v.get("nota")) for k, v in cond.items() if v["estado"] == "pendiente_refleja"],
        incompletas=[dict(id=k, faltan=v.get("datos_faltantes")) for k, v in cond.items() if v["estado"] == "incompleta"]
                    + [dict(id=k, nota=r.get("nota")) for k, r in rels.items() if r["estado"] == "incompleta"],
        no_interpretables=[dict(id=k, nota=v.get("nota")) for k, v in cond.items() if v["estado"] == "no_interpretable"],
        no_calculables=[dict(id=k, nota=v.get("nota")) for k, v in cond.items() if v["estado"] == "no_calculable"],
        revision_medica_obligatoria=sorted({b for s in segs.values() if s["revision_medica_obligatoria"] for b in (SEGF.get(s["seguridad"], {}).get("biomarcadores") or [SEGF.get(s["seguridad"], {}).get("biomarcador")]) if b}),
        datos_faltantes=sorted({x for v in cond.values() if v["estado"] in ("incompleta", "activa") for x in (v.get("datos_faltantes") or [])}),
        dudas_lectura=p1.get("dudas", []))
    canal = "llamada del equipo médico antes de publicar" if llamadas else ("revisión médica antes de publicar" if esc_max >= 2 else "revisión médica (piloto)")
    rec = cond.get("COND-M6-MI-A01", {}).get("recordatorios", [])
    pa = cond.get("COND-M6-MI-A02", {})
    return dict(orden=p1.get("orden"), estado="analisis_completo", escalamiento_maximo=esc_max, canal=canal, llamadas=sorted(set(llamadas)),
                hallazgos_informe=grupos, vista_medica=vista, recordatorios=rec,
                edad_biologica=dict(phenoage=pa.get("phenoage"), diferencia=pa.get("diferencia"), nota=pa.get("nota")) if pa.get("estado") == "activa" else None,
                calculados={k: (v["valor"] if v.get("calculado") else None) for k, v in p1["calculados"].items()})
