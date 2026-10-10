"""
Saludly Brain · Motor · Parte 3: condiciones de los módulos M3 a M6

Misma estructura que condiciones_m1m2: un evaluador por ficha, umbrales citados de
la ficha, metadatos leídos del Knowledge Base. Recibe también los hallazgos de M1 y
M2 porque algunas condiciones dependen de ellos (por ejemplo, celiaquía con
condiciones tiroideas activas).
"""
import re
from condiciones_m1m2 import Datos, H, ni

def _txt(d, b):
    r = d.r(b); return str((r or {}).get("valor") or "").strip().lower()

def _reactivo(d, b):
    t = _txt(d, b)
    if not t: return None
    if t.startswith("no reactivo") or t.startswith("negativo"): return False
    if t.startswith("reactivo") or t.startswith("positivo") or t.startswith("detectable"): return True
    return None

def _meds(d, *nombres): return [n for n in nombres if n in d.meds()]

IBP = ("omeprazol", "esomeprazol", "pantoprazol", "lansoprazol", "rabeprazol")


# =============================================================== M3 · Hematología
def corte_anemia(d):
    sexo = d.c("sexo")
    if d.c("embarazo"):
        sem = d.c("semana_gestacion") or 0
        return 10.5 if 14 <= sem <= 27 else 11.0
    return 13.0 if sexo == "hombre" else 12.0

def he001(d):
    f = "COND-M3-HE-001"
    if (d.c("edad") or 0) < 15: return H(f, "no_aplica", nota="menor de 15 años")
    if not d.interpretable("hemoglobin"): return ni(f, d, "hemoglobin")
    hb = d.calc("hemoglobina_ajustada")
    if hb is None: return H(f, "incompleta", faltan=["ciudad de residencia"])
    corte = corte_anemia(d)
    if hb >= corte: return H(f, "no_activa", extra=dict(hemoglobina_ajustada=hb))
    if d.c("embarazo"): sev, esc = None, 2
    else:
        sev = "severa" if hb < 8 else "moderada" if hb < 11 else "leve"
        esc = 3 if sev == "severa" else 2 if sev == "moderada" else 1
    if d.clase("hemoglobin") == "critico": esc = 3
    coin = "alta" if d.c("tabaquismo") is not None else "moderada"
    return H(f, "activa", coin, esc, ["anemia"], [] if d.c("tabaquismo") is not None else ["tabaquismo"],
             extra=dict(hemoglobina_ajustada=hb, corte=corte, severidad=sev))

def ferritina_corte(d): return 70 if (d.v("hs_crp") or 0) > 5 else 15

def he002(d, ya):
    f = "COND-M3-HE-002"
    if ya["COND-M3-HE-001"]["estado"] != "activa": return H(f, "no_activa")
    fe = d.v("ferritin")
    if fe is None: return H(f, "incompleta", faltan=["ferritin"])
    sat, vcm, rdw = d.v("transferrin_saturation"), d.v("mcv"), d.v("rdw")
    apoyos = [k for k, ok in [("saturacion_baja", sat is not None and sat < 20), ("vcm_bajo", vcm is not None and d.lo("mcv") and vcm < d.lo("mcv")),
                              ("rdw_alto", rdw is not None and d.hi("rdw") and rdw > d.hi("rdw"))] if ok]
    corte = ferritina_corte(d)
    if fe < corte:
        causa = any(d.c(k) for k in ("menstruacion_abundante", "embarazo", "dieta_vegetariana", "cirugia_bariatrica", "dona_sangre"))
        return H(f, "activa", "alta" if apoyos else "moderada", 2, ["anemia", "ferritina_baja"] + apoyos,
                 extra=dict(dispara=[] if causa else ["iga", "anti_ttg_iga"], corte_ferritina=corte))
    if fe < 30 and "saturacion_baja" in apoyos and "vcm_bajo" in apoyos: return H(f, "vigilar", "baja", None, apoyos)
    return H(f, "no_activa")

def he003(d, ya):
    f = "COND-M3-HE-003"
    fe = d.v("ferritin")
    if fe is None: return H(f, "incompleta", faltan=["ferritin"])
    if ya["COND-M3-HE-001"]["estado"] == "activa": return H(f, "no_activa", nota="hay anemia: va por HE-002")
    corte = ferritina_corte(d)
    if fe < corte:
        alto = d.c("sexo") == "hombre" or d.c("menopausia")
        return H(f, "activa", "alta", 2 if alto else 1, ["ferritina_baja", "sin_anemia"])
    if corte == 15 and fe < 30: return H(f, "vigilar", "baja", nota="ferritina 15 a 29")
    return H(f, "no_activa")

def b12_baja(d):
    b, amm = d.v("vitamin_b12"), d.v("methylmalonic_acid")
    if b is None: return None
    if b < 180: return True
    if b <= 350 and amm is not None and d.hi("methylmalonic_acid") is not None and amm > d.hi("methylmalonic_acid"): return True
    return False

def he004(d, ya):
    f = "COND-M3-HE-004"
    if ya["COND-M3-HE-001"]["estado"] != "activa": return H(f, "no_activa")
    vcm_alto = d.v("mcv") is not None and d.hi("mcv") and d.v("mcv") > d.hi("mcv")
    bb = b12_baja(d); fol = d.v("folate"); fb = fol is not None and fol < 4
    if not (bb or fb): return H(f, "no_activa")
    vcm_bajo = d.v("mcv") is not None and d.lo("mcv") and d.v("mcv") < d.lo("mcv")
    if vcm_bajo: return H(f, "no_activa", nota="VCM bajo: la anemia no se explica por B12 o folato (ver déficit de hierro)")
    cum = [k for k, ok in [("vcm_alto", vcm_alto), ("b12_baja", bb), ("folato_bajo", fb)] if ok]
    return H(f, "activa", "alta" if vcm_alto else "moderada", 2, ["anemia"] + cum, extra=dict(por=[x for x, ok in (("b12", bb), ("folato", fb)) if ok]))

def he005(d):
    f = "COND-M3-HE-005"
    p, lo = d.v("platelets"), d.lo("platelets")
    if p is None: return H(f, "incompleta", faltan=["platelets"])
    obs = " ".join(d.ctx.get("_observaciones", [])).lower()
    if "agregado" in obs and "plaqueta" in obs: return H(f, "no_interpretable", nota="agregados plaquetarios: repetir con citrato")
    if d.clase("platelets") == "critico": return H(f, "activa", "alta", 3, ["bandera_critica"])
    if p < 100:
        conf = (["infección reciente"] if d.c("infeccion_reciente") else []) + _meds(d, "heparina") + (["alcohol"] if d.c("alcohol_consumo") else [])
        return H(f, "activa", "moderada" if conf else "alta", 2, ["plaquetas_bajas"], confusores=conf)
    if lo is not None and p < lo: return H(f, "vigilar", "baja", 1, ["plaquetas_leves"], nota="valor fuera de rango: repetir")
    return H(f, "no_activa")

def he006(d):
    f = "COND-M3-HE-006"
    fe, sat = d.v("ferritin"), d.v("transferrin_saturation")
    if fe is None or sat is None: return H(f, "incompleta", faltan=[x for x, v in (("ferritin", fe), ("transferrin_saturation", sat)) if v is None])
    premeno = d.c("sexo") == "mujer" and not d.c("menopausia")
    patron = (sat > 45 and fe > 200) if premeno else (sat > 50 and fe > 300)
    sola = fe > (200 if premeno else 300)
    if patron:
        conf = [x for x, ok in [("hs-CRP > 5", (d.v("hs_crp") or 0) > 5), ("alcohol", d.c("alcohol_consumo")),
                                ("enzimas hepáticas altas", d.clase("alt") == "alto" or d.clase("ggt") == "alto")] if ok]
        return H(f, "activa", "moderada" if conf else "alta", 2, ["patron_sobrecarga"], confusores=conf)
    if sola:
        ctx = "ligada a enzimas hepáticas altas" if (d.clase("alt") == "alto" or d.clase("ggt") == "alto") else "ferritina sola"
        return H(f, "vigilar", "baja", nota=f"ferritina alta con saturación normal; {ctx}")
    return H(f, "no_activa")

def he_a01(d, ya):
    f = "COND-M3-HE-A01"
    if ya["COND-M3-HE-001"]["estado"] != "activa": return H(f, "no_activa")
    fe, sat, crp = d.v("ferritin"), d.v("transferrin_saturation"), d.v("hs_crp")
    if None in (fe, sat, crp): return H(f, "incompleta")
    if fe >= 70 and crp > 5 and sat < 20:
        return H(f, "apoyo", nota="anemia con perfil inflamatorio: buscar causa, sin recomendaciones de hierro", extra=dict(modifica=["COND-M3-HE-001"]))
    return H(f, "no_activa")

def he_a02(d):
    f = "COND-M3-HE-A02"
    fuera = [b for b in ("wbc", "neutrophils_abs", "lymphocytes_abs") if d.clase(b) in ("alto", "bajo")]
    if any(d.clase(b) == "critico" for b in ("wbc", "neutrophils_abs", "lymphocytes_abs")): return H(f, "activa", "alta", 3, ["bandera_critica"])
    if not fuera: return H(f, "no_activa")
    otras = (d.clase("hemoglobin") == "bajo") or (d.clase("platelets") == "bajo")
    if otras and "wbc" in fuera: return H(f, "activa", "moderada", 2, fuera + ["otra_linea_alterada"])
    return H(f, "vigilar", "baja", 1, fuera, nota="valor fuera de rango: repetir")

def he_a03(d):
    f = "COND-M3-HE-A03"
    e = d.calc("eosinofilos_abs")
    if e is None: return H(f, "incompleta")
    if e < 0.5: return H(f, "no_activa")
    return H(f, "apoyo", escalamiento=2 if e > 1.5 else 1, nota=f"eosinófilos {e} x10³/µL", extra=dict(modifica=["COND-M4-IN-A02"]))

# =============================================================== M3 · Nutrición
def nu001(d, ya):
    f = "COND-M3-NU-001"
    he4 = ya["COND-M3-HE-004"]
    if he4["estado"] == "activa" and "b12" in he4.get("por", []): return H(f, "no_activa", nota="incluida en HE-004")
    b = d.v("vitamin_b12")
    if b is None: return ni(f, d, "vitamin_b12") if d.r("vitamin_b12") else H(f, "incompleta", faltan=["vitamin_b12"])
    amm = d.v("methylmalonic_acid")
    factor = bool(_meds(d, "metformina", *IBP, "ranitidina", "famotidina") or d.c("dieta_vegana") or d.c("cirugia_bariatrica"))
    esc = 2 if d.c("sintomas_neurologicos") else 1
    if b < 180:
        coin = "alta" if factor else "moderada"
        return H(f, "activa", coin, esc, ["b12_baja"] + (["factor_riesgo"] if factor else []),
                 confusores=["anticonceptivo oral"] if d.c("anticonceptivo_hormonal") else [])
    if b <= 350:
        if amm is None: return H(f, "vigilar", "baja", nota="B12 indeterminada sin ácido metilmalónico")
        if d.hi("methylmalonic_acid") is not None and amm > d.hi("methylmalonic_acid"):
            return H(f, "activa", "alta", esc, ["b12_indeterminada", "mma_alto"])
        return H(f, "no_activa", nota="ácido metilmalónico normal: sin déficit funcional")
    return H(f, "no_activa")

def nu002(d, ya):
    f = "COND-M3-NU-002"
    he4 = ya["COND-M3-HE-004"]
    if he4["estado"] == "activa" and "folato" in he4.get("por", []): return H(f, "no_activa", nota="incluida en HE-004")
    fo = d.v("folate")
    if fo is None: return H(f, "incompleta", faltan=["folate"])
    if (d.c("ayuno_horas") or 0) < 8: return H(f, "no_interpretable", nota="ayuno menor de 8 horas")
    if fo >= 4: return H(f, "no_activa")
    return H(f, "activa", "alta" if fo < 3 else "moderada", 2 if d.c("embarazo") else 1, ["folato_bajo" if fo < 3 else "folato_posible"])

def nu_a01(d, ya):
    f = "COND-M3-NU-A01"
    h, hi = d.v("homocysteine"), d.hi("homocysteine")
    if h is None or hi is None or h <= hi: return H(f, "no_activa")
    mods = [x for x in ("COND-M3-NU-001", "COND-M3-NU-002", "COND-M3-HE-004") if ya[x]["estado"] == "activa"]
    if mods: return H(f, "apoyo", extra=dict(modifica=mods))
    return H(f, "vigilar", "baja", nota="homocisteína alta sin déficit de B12 o folato: revisar TFG y TSH")

def nu_a02(d):
    f = "COND-M3-NU-A02"
    p = d.v("pth")
    if p is None: return H(f, "no_aplica", nota="PTH no medida (refleja solo con calcio corregido alto)")
    cc, hi = d.calc("calcio_corregido"), d.hi("calcium")
    if d.hi("pth") is None or p <= d.hi("pth") or cc is None or (hi is not None and cc > hi): return H(f, "no_activa")
    sec = [x for x, ok in [("vitamina D < 20", (d.v("vitamin_d") or 99) < 20), ("TFG < 60", (d.calc("egfr") or 99) < 60)] if ok] + _meds(d, "hidroclorotiazida", "litio")
    if sec: return H(f, "vigilar", "baja", nota=f"causa secundaria probable: {', '.join(sec)}")
    return H(f, "activa", "moderada", 1, ["pth_alta", "calcio_normal"], nota="posible hiperparatiroidismo normocalcémico (vista médica)")

def nu_a03(d):
    f = "COND-M3-NU-A03"
    if not d.interpretable("vitamin_d"): return ni(f, d, "vitamin_d")
    c = d.clase("vitamin_d")
    if c == "bajo": return H(f, "activa", None, 0, ["vitd_baja"], nota="recomendación alimentaria y de sol, sin dosis")
    if c == "alto": return H(f, "activa", None, 1, ["vitd_alta"], nota="preguntar por suplementos")
    return H(f, "no_activa") if d.v("vitamin_d") is not None else H(f, "incompleta", faltan=["vitamin_d"])

VIT_INFO = ["vitamin_b1", "vitamin_b6", "vitamin_a", "vitamin_e", "vitamin_k1", "vitamin_c", "biotin", "niacin", "omega3_index", "omega6_omega3_ratio", "coq10"]
def nu_a04(d):
    f = "COND-M3-NU-A04"
    det, esc = {}, 0
    for b in VIT_INFO:
        r = d.r(b)
        if not r: continue
        det[b] = r.get("clase") or "solo valor"
    biot = any("biotina" in s.lower() for s in d.ctx.get("suplementos", [])) or d.clase("biotin") == "alto"
    acciones = []
    if biot: acciones.append("biotina: repetir pruebas afectadas sin el suplemento"); esc = max(esc, 1)
    for b in ("vitamin_a", "vitamin_e"):
        if d.clase(b) == "alto": acciones.append(f"{b} alta: sugerir consulta"); esc = max(esc, 1)
    if d.clase("vitamin_b1") == "bajo":
        riesgo = d.c("alcohol_consumo") or d.c("cirugia_bariatrica") or d.c("desnutricion")
        if riesgo and d.c("sintomas_neurologicos"): acciones.append("tiamina baja con síntomas neurológicos y factor de riesgo"); esc = 3
        elif riesgo: acciones.append("tiamina baja con factor de riesgo"); esc = max(esc, 1)
    bajas = [b for b, c in det.items() if c == "bajo"]
    if bajas: acciones.append(f"recomendación alimentaria: {', '.join(bajas)}")
    if not acciones: return H(f, "no_activa", extra=dict(detalle=det))
    return H(f, "activa", None, esc, nota="; ".join(acciones), extra=dict(detalle=det))


# =============================================================== M4 · Gastroenterología
def patron_muscular(d):
    return d.clase("ck_cpk") == "alto" and (d.clase("ast") == "alto" or d.clase("ldh") == "alto")

def ga001(d):
    f = "COND-M4-GA-001"
    c = d.C.get("fib4") or {}
    if not c.get("calculado"): return H(f, "no_aplica", nota=c.get("motivo"))
    v = c["valor"]; nota = c.get("nota")
    if v < 1.3: return H(f, "no_activa", nota=f"FIB-4 {v}" + (f"; {nota}" if nota else ""), extra=dict(fib4=v))
    conf = (["ejercicio intenso 48 h"] if d.c("ejercicio_intenso_48h") else []) + (["patrón muscular"] if patron_muscular(d) else [])
    if v <= 2.67: return H(f, "activa", "moderada", 1, ["fib4_indeterminado"], confusores=conf, nota=nota, extra=dict(fib4=v))
    return H(f, "activa", "moderada" if conf else "alta", 2, ["fib4_alto"], confusores=conf, nota=nota, extra=dict(fib4=v))

def ga002(d):
    f = "COND-M4-GA-002"
    alt, ahi = d.v("alt"), d.hi("alt")
    if alt is None: return H(f, "incompleta", faltan=["alt"])
    musc = patron_muscular(d)
    alt_alta = ahi is not None and alt > ahi
    ast_alta = d.clase("ast") == "alto" and not musc
    if d.clase("alt") == "critico": return H(f, "activa", "alta", 3, ["bandera_critica"])
    if alt_alta or ast_alta:
        previo = (d.c("historial", {}) or {}).get("alt_alta_previa")
        esc = 2 if (ahi and alt > 3 * ahi) else 1
        conf = (["patrón muscular"] if musc else []) + (["ejercicio intenso 48 h"] if d.c("ejercicio_intenso_48h") else []) + (["alcohol"] if d.c("alcohol_consumo") else [])
        return H(f, "activa", "alta" if previo else "moderada", esc, [k for k, ok in (("alt_alta", alt_alta), ("ast_alta", ast_alta)) if ok],
                 [] if previo else ["segunda medición"], conf, extra=dict(dispara=["iga", "anti_ttg_iga"]))
    if d.clase("alt") == "limitrofe":
        if musc: return H(f, "no_activa", nota="ALT limítrofe con patrón muscular: no se lee como hepática")
        return H(f, "vigilar", "baja", nota=d.r("alt").get("motivo_clase"))
    return H(f, "no_activa", nota="patrón muscular: AST no se lee como hepática" if musc else None)

def ga003(d):
    f = "COND-M4-GA-003"
    alp, ggt, alt = d.v("alp"), d.v("ggt"), d.v("alt")
    if alp is None or d.hi("alp") is None: return H(f, "incompleta", faltan=["alp"])
    if alp <= d.hi("alp"): return H(f, "no_activa")
    ggt_alta = ggt is not None and d.hi("ggt") is not None and ggt > d.hi("ggt")
    if not ggt_alta: return H(f, "vigilar", "baja", nota="fosfatasa alcalina alta con GGT normal: origen óseo probable")
    R = (alt / d.hi("alt")) / (alp / d.hi("alp")) if (alt and d.hi("alt")) else 0
    if R >= 2: return H(f, "no_activa", nota=f"R {R:.1f}: patrón no colestásico")
    esc = 2 if (alp > 2 * d.hi("alp") or d.clase("bilirubin_direct") == "alto") else 1
    return H(f, "activa", "alta", esc, ["alp_alta", "ggt_alta", "patron_colestasico"], extra=dict(R=round(R, 2)))

def ga004(d):
    f = "COND-M4-GA-004"
    r = _reactivo(d, "fit_stool")
    if r is None: return H(f, "incompleta", faltan=["fit_stool"])
    if not r: return H(f, "no_activa")
    edad = d.c("edad") or 0
    return H(f, "activa", "alta", 2, ["fit_positivo"], nota=None if 50 <= edad <= 75 else "fuera de la franja formal de tamizaje (50 a 75)")

def ga005(d):
    f = "COND-M4-GA-005"
    r = _reactivo(d, "hpylori_stool_ag")
    if r is None: return H(f, "incompleta", faltan=["hpylori_stool_ag"])
    if r: return H(f, "activa", "alta", 2, ["antigeno_positivo"], nota="incluir la limitación del antígeno fecal frente a la prueba de aliento")
    meds = _meds(d, *IBP, "amoxicilina", "claritromicina", "metronidazol", "bismuto")
    return H(f, "no_activa", nota="negativo no concluyente por medicamentos recientes" if meds else None)

def ga006(d, ya):
    f = "COND-M4-GA-006"
    t, iga = d.v("anti_ttg_iga"), d.v("iga")
    if t is None or iga is None:
        motivos = [x for x in ("COND-M3-HE-002", "COND-M3-HE-003", "COND-M4-GA-002", "COND-M2-TI-001", "COND-M2-TI-002") if ya.get(x, {}).get("estado") == "activa"]
        if d.c("familiar_celiaco"): motivos.append("familiar celíaco")
        if motivos: return H(f, "pendiente_refleja", nota=f"el laboratorio debe correr IgA total y anti-tTG IgA ({', '.join(motivos)})")
        return H(f, "no_aplica")
    if d.lo("iga") is not None and iga < d.lo("iga"): return H(f, "no_interpretable", nota="déficit de IgA: sugerir pruebas basadas en IgG")
    if d.c("dieta_sin_gluten"): return H(f, "no_interpretable", nota="dieta sin gluten")
    if d.hi("anti_ttg_iga") is not None and t > d.hi("anti_ttg_iga"):
        return H(f, "activa", "alta" if d.c("dieta_sin_gluten") is False else "moderada", 2, ["ttg_positivo", "iga_normal"])
    return H(f, "no_activa", nota="sin señal de celiaquía")

def ga_a01(d):
    f = "COND-M4-GA-A01"
    if d.clase("bilirubin_total") != "alto": return H(f, "no_activa")
    if d.clase("bilirubin_direct") == "alto": return H(f, "no_activa", nota="bilirrubina directa alta: no es aislada")
    if any(d.clase(b) in ("alto",) for b in ("alt", "ast", "alp", "ggt")): return H(f, "no_activa", nota="otras pruebas hepáticas alteradas")
    hemol = d.clase("hemoglobin") == "bajo" and d.clase("ldh") == "alto" and (d.clase("reticulocytes_pct") == "alto" or d.clase("reticulocytes_abs") == "alto")
    if hemol: return H(f, "activa", "alta", 2, ["bilirrubina_indirecta", "signos_hemolisis"], nota="activa la relación de hemólisis")
    return H(f, "activa", None, 0, ["bilirrubina_indirecta_aislada"], nota="resultado observado; patrón frecuente y benigno")

def ga_a02(d, ya):
    f = "COND-M4-GA-A02"
    alc = d.c("alcohol_consumo")
    if alc is None: return H(f, "incompleta", faltan=["consumo de alcohol"])
    if not alc: return H(f, "no_activa")
    if d.clase("ggt") == "alto" or ya["COND-M4-GA-002"]["estado"] == "activa":
        ratio = (d.v("ast") or 0) / (d.v("alt") or 1)
        return H(f, "apoyo", nota=f"AST/ALT {ratio:.1f}" + (" (≥ 2)" if ratio >= 2 else ""), extra=dict(modifica=["COND-M4-GA-001", "COND-M4-GA-002", "COND-M1-CA-003"]))
    return H(f, "no_activa")

# =============================================================== M4 · Infectología
def in001(d):
    f = "COND-M4-IN-001"
    r = _reactivo(d, "anti_hcv")
    if r is None: return H(f, "incompleta", faltan=["anti_hcv"])
    if not r: return H(f, "no_activa")
    arn = _txt(d, "hcv_rna")
    if not arn: return H(f, "pendiente_refleja", nota="anti-VHC reactivo: falta ARN; informe en espera", extra=dict(canal="llamada del médico"))
    if arn.startswith("no detectable"): return H(f, "activa", "baja", 2, ["anti_vhc_reactivo", "arn_no_detectable"], nota="infección resuelta o falso positivo", extra=dict(canal="llamada del médico"))
    return H(f, "activa", "alta", 2, ["anti_vhc_reactivo", "arn_detectable"], extra=dict(canal="llamada del médico"))

def in002(d):
    f = "COND-M4-IN-002"
    s, c = _reactivo(d, "hbsag"), _reactivo(d, "anti_hbc")
    hbs = d.v("anti_hbs")
    if s is None or c is None or hbs is None: return H(f, "incompleta", faltan=[x for x, v in (("hbsag", s), ("anti_hbc", c), ("anti_hbs", hbs)) if v is None])
    if s: return H(f, "activa", "alta", 2, ["hbsag_reactivo"], extra=dict(estado_hb="infeccion_activa", canal="llamada del médico"))
    if c and hbs >= 10: return H(f, "activa", "alta", 1, ["anti_hbc", "anti_hbs"], nota="riesgo de reactivación con inmunosupresión", extra=dict(estado_hb="infeccion_pasada_resuelta"))
    if c: return H(f, "activa", "moderada", 2, ["anti_hbc_aislado"], extra=dict(estado_hb="anti_hbc_aislado", canal="llamada del médico"))
    if hbs >= 10: return H(f, "activa", "alta", 0, ["anti_hbs"], extra=dict(estado_hb="inmune_por_vacuna"))
    return H(f, "activa", "alta", 1, ["sin_anticuerpos_protectores"], nota="recomendar vacuna", extra=dict(estado_hb="susceptible"))

def in003(d):
    f = "COND-M4-IN-003"
    t = _reactivo(d, "chagas_elisa_total")
    if t is None: return H(f, "incompleta", faltan=["chagas_elisa_total"])
    if not t: return H(f, "no_activa")
    r = _reactivo(d, "chagas_elisa_recombinante")
    if r is None: return H(f, "pendiente_refleja", nota="primera ELISA reactiva: falta la segunda")
    if not r: return H(f, "pendiente_refleja", nota="ELISA discordantes: tercera prueba; informe en espera")
    return H(f, "activa", "alta" if d.c("procedencia_endemica") else "moderada", 2, ["elisa_1", "elisa_2"],
             nota="lineamiento del INS para adultos por verificar", extra=dict(canal="llamada del médico"))

def _campo(d, b, c): return d.campos.get((b, c)) or {}

def in_a01(d):
    f = "COND-M4-IN-A01"
    nit = str(_campo(d, "urinalysis", "nitritos").get("valor") or "").lower().startswith("positivo")
    est = str(_campo(d, "urinalysis", "esterasa leucocitaria").get("valor") or "").lower().startswith("positivo")
    leu = re.findall(r"\d+", str(_campo(d, "urinalysis", "sedimento leucocitos").get("valor_original") or ""))
    leu_alto = bool(leu) and max(map(int, leu)) > 5
    if not (nit or est or leu_alto): return H(f, "no_activa")
    sint = d.c("sintomas_urinarios")
    if sint: return H(f, "apoyo", escalamiento=1, nota="sugerir urocultivo", extra=dict(modifica=["COND-M2-NE-002", "COND-M2-NE-006"]))
    if d.c("embarazo"): return H(f, "vigilar", "baja", 1, nota="embarazo: requiere urocultivo")
    if sint is None: return H(f, "incompleta", faltan=["síntomas urinarios"])
    return H(f, "no_activa", nota="sin síntomas: no se reporta como infección (IDSA 2019)")

PATOGENOS = ("giardia", "histolytica", "ascaris", "trichuris", "uncinaria", "anquilostoma", "strongyloides", "hymenolepis", "taenia", "cryptosporidium", "cyclospora")
COMENSALES = ("entamoeba coli", "endolimax", "iodamoeba", "chilomastix")
def in_a02(d):
    f = "COND-M4-IN-A02"
    t = str(_campo(d, "stool_exam", "coprologico parasitos").get("valor") or "").lower()
    if not t: return H(f, "incompleta", faltan=["coprológico"])
    if "no se observ" in t: return H(f, "no_activa")
    if any(p in t for p in PATOGENOS):
        eos = (d.calc("eosinofilos_abs") or 0) >= 0.5
        return H(f, "apoyo", escalamiento=1, nota="parásito patógeno" + (" reforzado por eosinofilia" if eos else ""))
    if any(c in t for c in COMENSALES): return H(f, "apoyo", escalamiento=0, nota="comensal: no requiere tratamiento")
    return H(f, "vigilar", "baja", 0, nota="microorganismo no clasificado en la lista firmada (por ejemplo, Blastocystis)")


# =============================================================== M5 · Mujer y hombre
FAI_CORTE_PROVISIONAL = 5.0   # por verificar: la ficha pide el corte de la guía de SOP 2023 o del laboratorio

def mu001(d):
    f = "COND-M5-MU-001"
    if d.c("sexo") != "mujer": return H(f, "no_aplica")
    if d.c("anticonceptivo_hormonal") or d.c("embarazo") or d.c("menopausia"): return H(f, "no_interpretable", nota="anticonceptivo hormonal, embarazo o menopausia")
    t, hi = d.v("testosterone_total"), d.hi("testosterone_total")
    if t is None or hi is None: return H(f, "incompleta", faltan=["testosterone_total"])
    fai = d.calc("indice_androgenos_libres")
    ta, fa = t > hi, fai is not None and fai > FAI_CORTE_PROVISIONAL
    if not (ta or fa): return H(f, "no_activa", extra=dict(indice_androgenos_libres=fai))
    otras = [x for x, ok in (("TSH alterada", d.clase("tsh") in ("alto", "bajo")), ("prolactina alta", d.clase("prolactin") == "alto")) if ok]
    coin = "alta" if (ta and fa and not otras) else "moderada"
    return H(f, "activa", coin, 2 if t > 2 * hi else 1, [k for k, ok in (("testosterona_alta", ta), ("fai_alto", fa)) if ok], confusores=otras,
             nota=f"corte del índice de andrógenos libres provisional ({FAI_CORTE_PROVISIONAL}), por verificar", extra=dict(indice_androgenos_libres=fai))

def mu002(d):
    f = "COND-M5-MU-002"
    if d.c("sexo") != "mujer": return H(f, "no_aplica")
    edad = d.c("edad") or 0
    if edad >= 45: return H(f, "no_aplica", nota="desde los 45 no se usa para menopausia")
    if not d.interpretable("fsh"): return ni(f, d, "fsh")
    v = d.v("fsh")
    if v is None or v <= 25: return H(f, "no_activa")
    if edad >= 40: return H(f, "no_activa", nota="40 a 44 años: contexto en la vista médica")
    previo = (d.c("historial", {}) or {}).get("fsh_alta_previa_4_a_6_semanas")
    return H(f, "activa", "alta" if previo else "moderada", 2, ["fsh_alta", "edad_menor_40"], [] if previo else ["repetir en 4 a 6 semanas"])

ANTIDOP = ("risperidona", "haloperidol", "metoclopramida", "sulpirida", "domperidona", "olanzapina")
def mu003(d):
    f = "COND-M5-MU-003"
    if d.r("prolactin") is None: return H(f, "no_aplica")
    if d.c("embarazo") or d.c("lactancia"): return H(f, "no_interpretable", nota="embarazo o lactancia")
    p, hi = d.v("prolactin"), d.hi("prolactin")
    if p is None or hi is None or p <= hi: return H(f, "no_activa")
    m = d.r("macroprolactin")
    if m is None or d.v("macroprolactin") is None: return H(f, "pendiente_refleja", nota="prolactina alta: el laboratorio debe correr macroprolactina")
    mlo = d.lo("macroprolactin")
    if mlo is not None and d.v("macroprolactin") < mlo:
        return H(f, "activa", None, 0, ["macroprolactina_predominante"], nota="predomina macroprolactina: sin significado clínico habitual")
    causas = _meds(d, *ANTIDOP) + (["TSH alta"] if d.clase("tsh") == "alto" else [])
    if causas: return H(f, "vigilar", "baja", 1, ["prl_alta"], confusores=causas)
    previo = (d.c("historial", {}) or {}).get("prolactina_alta_previa")
    return H(f, "activa", "alta" if previo else "moderada", 2 if p > 100 else 1, ["prl_alta"], [] if previo else ["repetir"])

def mu_a01(d, ya):
    f = "COND-M5-MU-A01"
    if not d.c("embarazo"): return H(f, "no_aplica")
    if ya["COND-M3-HE-001"]["estado"] == "activa": return H(f, "apoyo", escalamiento=2, nota="ruta al control prenatal", extra=dict(modifica=["COND-M3-HE-001", "COND-M3-HE-002"]))
    return H(f, "no_activa")

def ur001(d):
    f = "COND-M5-UR-001"
    if d.c("sexo") != "hombre": return H(f, "no_aplica")
    if d.c("consentimientos", {}).get("psa") is False: return H(f, "no_aplica", nota="sin consentimiento de PSA: no se mide")
    v = d.v("psa_total")
    if v is None: return H(f, "incompleta", faltan=["psa_total"])
    nota = None
    if _meds(d, "finasterida", "dutasterida"): v = v * 2; nota = "PSA duplicado por inhibidor de 5-alfa reductasa"
    corte = min(4.0, d.hi("psa_total") or 4.0)
    if v <= corte: return H(f, "no_activa", nota=nota)
    edad = d.c("edad") or 0
    conf = [x for x, k in (("eyaculación 48 h", "eyaculacion_48h"), ("ciclismo 48 h", "ciclismo_48h"), ("infección urinaria", "sintomas_urinarios")) if d.c(k)]
    esc = 2 if (50 <= edad <= 75 or v > 10) else 1
    return H(f, "activa", "moderada" if conf else "alta", esc, ["psa_alto"] + (["zona_gris"] if v <= 10 else ["psa_muy_alto"]), confusores=conf, nota=nota,
             extra=dict(dispara=["psa_free"] if 4 <= v <= 10 else []))

def ur002(d):
    f = "COND-M5-UR-002"
    if d.c("sexo") != "hombre": return H(f, "no_aplica")
    t = d.v("testosterone_total")
    if t is None: return H(f, "incompleta", faltan=["testosterone_total"])
    if t >= 264: return H(f, "no_activa")
    h = d.c("hora_toma") or "00:00"; hh, mm = map(int, h.split(":"))
    if not (6 * 60 <= hh * 60 + mm <= 10 * 60): return H(f, "no_interpretable", nota=f"toma a las {h}, fuera de 6:00 a 10:00")
    metodo = ((d.r("testosterone_total") or {}).get("metodo") or "").lower()
    if "cdc" not in metodo and "certific" not in metodo:
        return H(f, "vigilar", "baja", 1, ["testosterona_baja"], nota="método sin certificación CDC declarada: resultado observado, sin etiqueta")
    conf = (["obesidad"] if (d.calc("imc") or 0) >= 30 else []) + _meds(d, "tramadol", "morfina", "oxicodona", "prednisona")
    return H(f, "activa", "moderada", 2 if t < 150 else 1, ["testosterona_baja", "metodo_certificado"], confusores=conf,
             nota="coincidencia alta requiere testosterona libre baja; su intervalo de referencia está pendiente")

def ur_a01(d):
    f = "COND-M5-UR-A01"
    c = d.C.get("testosterone_free") or {}
    if not c.get("calculado"): return H(f, "no_aplica", nota=c.get("motivo"))
    return H(f, "apoyo", nota=f"testosterona libre calculada {c['valor']} pg/mL; falta el intervalo de referencia para clasificarla", extra=dict(valor=c["valor"]))

def ur_a02(d):
    f = "COND-M5-UR-A02"
    c = d.C.get("psa_libre_porcentaje") or {}
    if not c.get("calculado"): return H(f, "no_aplica", nota=c.get("motivo"))
    return H(f, "apoyo", nota=f"PSA libre {c['valor']} % del total (cortes pendientes de fuente)", extra=dict(porcentaje=c["valor"]))


# =============================================================== M6 · Inmunidad y envejecimiento
def re001(d):
    f = "COND-M6-RE-001"
    u, hi = d.v("uric_acid"), d.hi("uric_acid")
    if u is None: return H(f, "incompleta", faltan=["uric_acid"])
    if hi is None or u <= hi: return H(f, "no_activa")
    return H(f, "activa", "alta", 1, ["urico_alto"], confusores=_meds(d, "hidroclorotiazida", "furosemida", "clortalidona"))

def re_a01(d):
    f = "COND-M6-RE-A01"
    r = d.r("ana_hep2")
    if not r: return H(f, "incompleta", faltan=["ana_hep2"])
    if _reactivo(d, "ana_hep2") is False: return H(f, "no_activa")
    tit = r.get("titulo")
    if not tit: return H(f, "no_interpretable", nota="positivo sin título o sin patrón")
    n = int(tit.split(":")[1])
    obs = " ".join(d.ctx.get("_observaciones", []))
    patron = re.search(r"AC-\d+", obs)
    notas = []
    if patron and patron.group(0) == "AC-2": notas.append("patrón AC-2: frecuente en personas sanas")
    if d.clase("anti_tpo") == "alto" or d.clase("tsh") == "alto": notas.append("autoinmunidad tiroidea asociada")
    return H(f, "activa", None, 2 if n >= 160 else 1, [f"titulo_{tit}"] + ([patron.group(0)] if patron else []), nota="; ".join(notas) or None)

def re_a02(d):
    f = "COND-M6-RE-A02"
    v, hi = d.v("esr"), d.hi("esr")
    if v is None or hi is None or v <= hi: return H(f, "no_activa")
    return H(f, "vigilar", "baja", 2 if v >= 100 else 1, ["vsg_alta"], nota="refuerza la relación de inflamación" if (d.v("hs_crp") or 0) > 5 else "repetir")

def mi001(d):
    f = "COND-M6-MI-001"
    imc = d.calc("imc"); edad = d.c("edad") or 0
    perdida = d.c("perdida_peso_no_intencional")
    if imc is None and perdida is None: return H(f, "incompleta", faltan=["peso_kg", "talla_m", "pérdida de peso"])
    feno = (imc is not None and imc < (22 if edad >= 70 else 20)) or bool(perdida)
    if not feno: return H(f, "no_activa") if imc is not None else H(f, "incompleta", faltan=["peso_kg", "talla_m"])
    etio = (d.v("hs_crp") or 0) > 5 or bool(d.c("ingesta_reducida"))
    if not etio: return H(f, "vigilar", "baja", nota="criterio fenotípico sin criterio etiológico")
    return H(f, "activa", "alta", 2 if edad >= 70 else 1, ["fenotipico", "etiologico"])

def mi_a01(d):
    f = "COND-M6-MI-A01"
    edad, sexo = d.c("edad") or 0, d.c("sexo")
    if edad < 18: return H(f, "no_aplica", nota="menor de 18 años: fuera del alcance de la versión 1")
    rec = []
    if sexo == "mujer" and 30 <= edad <= 65: rec.append("tamizaje de cuello uterino")
    if sexo == "mujer" and 50 <= edad <= 69: rec.append("mamografía cada 2 años")
    if 50 <= edad <= 75: rec.append("tamizaje colorrectal (la sangre oculta de hoy cuenta)")
    if sexo == "hombre" and 50 <= edad <= 75: rec.append("conversación sobre PSA")
    return H(f, "apoyo", extra=dict(recordatorios=rec))

def mi_a02(d):
    f = "COND-M6-MI-A02"
    c = d.C.get("phenoage") or {}
    if not c.get("calculado"): return H(f, "no_calculable", nota=c.get("motivo"))
    edad = d.c("edad")
    return H(f, "activa", None, 0, nota=c.get("nota"), extra=dict(phenoage=c["valor"], diferencia=round(c["valor"] - edad, 1)))


# =============================================================== orquestación
def evaluar_m3m6(p1, ctx, previos=None):
    ctx = dict(ctx, _observaciones=p1.get("observaciones", []))
    d = Datos(p1, ctx)
    ya = dict(previos or {})
    def put(h): ya[h["ficha"]] = h
    put(he001(d))
    for fn in (he002, he003, he004): put(fn(d, ya))
    put(he005(d)); put(he006(d)); put(he_a01(d, ya)); put(he_a02(d)); put(he_a03(d))
    put(nu001(d, ya)); put(nu002(d, ya)); put(nu_a01(d, ya)); put(nu_a02(d)); put(nu_a03(d)); put(nu_a04(d))
    put(ga001(d)); put(ga002(d)); put(ga003(d)); put(ga004(d)); put(ga005(d)); put(ga006(d, ya)); put(ga_a01(d)); put(ga_a02(d, ya))
    put(in001(d)); put(in002(d)); put(in003(d)); put(in_a01(d)); put(in_a02(d))
    put(mu001(d)); put(mu002(d)); put(mu003(d)); put(mu_a01(d, ya)); put(ur001(d)); put(ur002(d)); put(ur_a01(d)); put(ur_a02(d))
    put(re001(d)); put(re_a01(d)); put(re_a02(d)); put(mi001(d)); put(mi_a01(d)); put(mi_a02(d))
    # HE-A01 sube el escalamiento de la anemia a 2 y quita recomendaciones de hierro
    if ya["COND-M3-HE-A01"]["estado"] == "apoyo" and ya["COND-M3-HE-001"]["estado"] == "activa":
        ya["COND-M3-HE-001"]["escalamiento"] = max(2, ya["COND-M3-HE-001"]["escalamiento"] or 0)
    if ya["COND-M5-MU-A01"]["estado"] == "apoyo":
        ya["COND-M3-HE-001"]["escalamiento"] = max(2, ya["COND-M3-HE-001"]["escalamiento"] or 0)
    return {k: v for k, v in ya.items() if k.startswith(("COND-M3", "COND-M4", "COND-M5", "COND-M6"))}
