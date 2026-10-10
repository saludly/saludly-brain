"""
Saludly Brain · Motor · Cálculos derivados (documento 04, sección 04.5)

Cada cálculo solo se hace si están todas sus variables en estado medido y se
cumplen sus condiciones. Cada resultado guarda de qué valores salió.
Si no se calcula, se dice por qué.
"""
import math

def _v(R, b):
    """Valor numérico medido de un biomarcador, o None."""
    r = R.get(b)
    if r and r.get("estado") == "medido" and isinstance(r.get("valor"), (int, float)):
        return float(r["valor"])
    return None

def _ok(nombre, valor, formula, entradas, nota=None, unidad=None):
    d = dict(id=nombre, calculado=True, valor=valor, unidad=unidad, formula=formula, entradas=entradas)
    if nota: d["nota"] = nota
    return d

def _no(nombre, motivo):
    return dict(id=nombre, calculado=False, motivo=motivo)

def _faltan(R, ids):
    return [b for b in ids if _v(R, b) is None]


def homa_ir(R, ctx):
    f = _faltan(R, ["glucose", "insulin"])
    if f: return _no("homa_ir", f"faltan valores medidos: {', '.join(f)}")
    if (ctx.get("ayuno_horas") or 0) < 8: return _no("homa_ir", "ayuno menor de 8 horas")
    if "insulina" in [m.lower() for m in ctx.get("medicamentos", [])]: return _no("homa_ir", "la persona usa insulina")
    g, i = _v(R, "glucose"), _v(R, "insulin")
    return _ok("homa_ir", round(g * i / 405, 2), "glucosa (mg/dL) × insulina (µUI/mL) / 405", {"glucose": g, "insulin": i})

def non_hdl(R, ctx):
    f = _faltan(R, ["total_cholesterol", "hdl_c"])
    if f: return _no("non_hdl_c", f"faltan: {', '.join(f)}")
    ct, h = _v(R, "total_cholesterol"), _v(R, "hdl_c")
    return _ok("non_hdl_c", round(ct - h, 1), "colesterol total − HDL", {"total_cholesterol": ct, "hdl_c": h}, unidad="mg/dL")

def remanente(R, ctx):
    f = _faltan(R, ["total_cholesterol", "hdl_c", "ldl_c"])
    if f: return _no("remnant_cholesterol", f"faltan: {', '.join(f)}")
    ldl = R["ldl_c"]
    medido = "medido" in (ldl.get("nombre_original") or "").lower() or "directo" in (ldl.get("metodo") or "").lower()
    if not medido: return _no("remnant_cholesterol", "el LDL no es medido (con Friedewald el remanente no aporta información)")
    ct, h, l = _v(R, "total_cholesterol"), _v(R, "hdl_c"), _v(R, "ldl_c")
    return _ok("remnant_cholesterol", round(ct - h - l, 1), "colesterol total − HDL − LDL", {"total_cholesterol": ct, "hdl_c": h, "ldl_c": l}, unidad="mg/dL")

def ct_hdl(R, ctx):
    f = _faltan(R, ["total_cholesterol", "hdl_c"])
    if f: return _no("tc_hdl_ratio", f"faltan: {', '.join(f)}")
    ct, h = _v(R, "total_cholesterol"), _v(R, "hdl_c")
    return _ok("tc_hdl_ratio", round(ct / h, 2), "colesterol total / HDL", {"total_cholesterol": ct, "hdl_c": h})

def saturacion(R, ctx):
    lab = _v(R, "transferrin_saturation")
    if lab is not None:
        return _ok("transferrin_saturation", lab, "reportada por el laboratorio", {"transferrin_saturation": lab}, unidad="%")
    f = _faltan(R, ["serum_iron", "tibc"])
    if f: return _no("transferrin_saturation", f"faltan: {', '.join(f)}")
    fe, t = _v(R, "serum_iron"), _v(R, "tibc")
    return _ok("transferrin_saturation", round(fe / t * 100, 1), "hierro / TIBC × 100", {"serum_iron": fe, "tibc": t}, unidad="%")

def tfg(R, ctx):
    cr = _v(R, "creatinine"); edad = ctx.get("edad"); sexo = ctx.get("sexo")
    if cr is None or edad is None or sexo not in ("hombre", "mujer"):
        return _no("egfr", "faltan creatinina medida, edad o sexo")
    k, a = (0.7, -0.241) if sexo == "mujer" else (0.9, -0.302)
    v = 142 * min(cr / k, 1) ** a * max(cr / k, 1) ** -1.200 * 0.9938 ** edad * (1.012 if sexo == "mujer" else 1)
    calc = round(v)
    lab = _v(R, "egfr")
    nota = None
    if lab is not None:
        nota = f"El laboratorio reporta {lab:g}; se usa el del laboratorio." + (" Difiere del calculado en más de 2: revisar." if abs(lab - calc) > 2 else "")
    return _ok("egfr", lab if lab is not None else calc, "CKD-EPI 2021 con creatinina, sin coeficiente de raza",
               {"creatinine": cr, "edad": edad, "sexo": sexo, "calculado_por_saludly": calc}, nota, "mL/min/1,73 m²")

def testo_libre(R, ctx):
    if ctx.get("sexo") != "hombre": return _no("testosterone_free", "solo en hombres; en mujeres se usa el índice de andrógenos libres")
    f = _faltan(R, ["testosterone_total", "shbg", "albumin"])
    if f: return _no("testosterone_free", f"faltan: {', '.join(f)}")
    tt, sh, alb = _v(R, "testosterone_total"), _v(R, "shbg"), _v(R, "albumin")
    shbg_r = R["shbg"].get("intervalo_lab") or {}
    shbg_fuera = (shbg_r.get("bajo") is not None and sh < shbg_r["bajo"]) or (shbg_r.get("alto") is not None and sh > shbg_r["alto"])
    imc = ctx.get("imc")
    if not (200 <= tt <= 400 or shbg_fuera or (imc is not None and imc >= 30)):
        return _no("testosterone_free", f"no indicada: testosterona total {tt:g} ng/dL fuera de 200 a 400, SHBG en rango e IMC {'sin dato' if imc is None else imc}")
    TT = tt * 0.0347e-9; SH = sh * 1e-9; ALB = alb * 10 / 69000  # mol/L
    Ka, Kt = 3.6e4, 1e9
    N = 1 + Ka * ALB
    a = Kt * N; b = N + Kt * (SH - TT); c = -TT
    ft = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return _ok("testosterone_free", round(ft * 288.42 * 1e9, 1), "Vermeulen (1999): Ka albúmina 3,6×10⁴ L/mol, Kt SHBG 10⁹ L/mol",
               {"testosterone_total": tt, "shbg": sh, "albumin": alb}, unidad="pg/mL")

def fai(R, ctx):
    if ctx.get("sexo") != "mujer": return _no("indice_androgenos_libres", "solo en mujeres")
    f = _faltan(R, ["testosterone_total", "shbg"])
    if f: return _no("indice_androgenos_libres", f"faltan: {', '.join(f)}")
    tt, sh = _v(R, "testosterone_total"), _v(R, "shbg")
    return _ok("indice_androgenos_libres", round(tt * 0.0347 * 100 / sh, 2), "testosterona total (nmol/L) × 100 / SHBG (nmol/L)", {"testosterone_total": tt, "shbg": sh})

def globulinas(R, ctx):
    lab = _v(R, "globulin")
    if lab is not None: return _ok("globulin", lab, "reportada por el laboratorio", {"globulin": lab}, unidad="g/dL")
    f = _faltan(R, ["total_protein", "albumin"])
    if f: return _no("globulin", f"faltan: {', '.join(f)}")
    return _ok("globulin", round(_v(R, "total_protein") - _v(R, "albumin"), 1), "proteínas totales − albúmina", {"total_protein": _v(R, "total_protein"), "albumin": _v(R, "albumin")}, unidad="g/dL")

def ag(R, ctx):
    lab = _v(R, "ag_ratio")
    if lab is not None: return _ok("ag_ratio", lab, "reportada por el laboratorio", {"ag_ratio": lab})
    g = globulinas(R, ctx)
    if not g["calculado"] or _v(R, "albumin") is None: return _no("ag_ratio", "faltan albúmina o globulinas")
    return _ok("ag_ratio", round(_v(R, "albumin") / g["valor"], 2), "albúmina / globulinas", {"albumin": _v(R, "albumin"), "globulin": g["valor"]})

def bun_cr(R, ctx):
    lab = _v(R, "bun_creatinine_ratio")
    if lab is not None: return _ok("bun_creatinine_ratio", lab, "reportada por el laboratorio", {"bun_creatinine_ratio": lab})
    f = _faltan(R, ["bun", "creatinine"])
    if f: return _no("bun_creatinine_ratio", f"faltan: {', '.join(f)}")
    return _ok("bun_creatinine_ratio", round(_v(R, "bun") / _v(R, "creatinine"), 1), "BUN / creatinina", {"bun": _v(R, "bun"), "creatinine": _v(R, "creatinine")})

def apob_apoa1(R, ctx):
    f = _faltan(R, ["apob", "apoa1"])
    if f: return _no("apob_apoa1_ratio", f"faltan: {', '.join(f)}")
    return _ok("apob_apoa1_ratio", round(_v(R, "apob") / _v(R, "apoa1"), 2), "ApoB / ApoA1", {"apob": _v(R, "apob"), "apoa1": _v(R, "apoa1")})

def hb_ajustada(R, ctx, reglas):
    hb = _v(R, "hemoglobin")
    if hb is None: return _no("hemoglobina_ajustada", "falta hemoglobina medida")
    ciudad = ctx.get("ciudad")
    metros = ctx.get("altitud_m") or (reglas["altitud"]["ciudades_metros"].get(ciudad) if ciudad else None)
    if metros is None: return _no("hemoglobina_ajustada", "falta ciudad o altitud de residencia")
    restar = 0.0; nota = []
    franja = [t for t in reglas["altitud"]["tabla"] if t["desde"] <= metros <= t["hasta"]]
    if franja: restar = franja[0]["restar"]
    elif metros >= 1000: nota.append(f"Altitud {metros} m sin franja escrita: no se ajusta (por verificar).")
    if ctx.get("tabaquismo"): nota.append("Fumador: el ajuste por tabaquismo no está escrito; no se aplica (por verificar).")
    return _ok("hemoglobina_ajustada", round(hb - restar, 1), "hemoglobina − ajuste por altitud (OMS 2024)", {"hemoglobin": hb, "altitud_m": metros, "restado": restar}, " ".join(nota) or None, "g/dL")

def calcio_corregido(R, ctx):
    f = _faltan(R, ["calcium", "albumin"])
    if f: return _no("calcio_corregido", f"faltan: {', '.join(f)}")
    ca, alb = _v(R, "calcium"), _v(R, "albumin")
    return _ok("calcio_corregido", round(ca + 0.8 * (4.0 - alb), 2), "calcio + 0,8 × (4,0 − albúmina)", {"calcium": ca, "albumin": alb}, unidad="mg/dL")

def osmolalidad(R, ctx):
    f = _faltan(R, ["sodium", "glucose", "bun"])
    if f: return _no("brecha_osmolar", f"faltan: {', '.join(f)}")
    calc = 2 * _v(R, "sodium") + _v(R, "glucose") / 18 + _v(R, "bun") / 2.8
    med = _v(R, "osmolality")
    if med is None: return _ok("osmolalidad_calculada", round(calc, 1), "2 × sodio + glucosa / 18 + BUN / 2,8", {"sodium": _v(R, "sodium"), "glucose": _v(R, "glucose"), "bun": _v(R, "bun")}, unidad="mOsm/kg")
    return _ok("brecha_osmolar", round(med - calc, 1), "osmolalidad medida − (2 × sodio + glucosa / 18 + BUN / 2,8)",
               {"osmolality": med, "osmolalidad_calculada": round(calc, 1)}, unidad="mOsm/kg")

def sodio_corregido(R, ctx):
    na, g = _v(R, "sodium"), _v(R, "glucose")
    if na is None or g is None: return _no("sodio_corregido", "faltan sodio o glucosa")
    if g < 200: return _no("sodio_corregido", "glucosa menor de 200 mg/dL: no se corrige")
    return _ok("sodio_corregido", round(na + 1.6 * (g - 100) / 100, 1), "sodio + 1,6 × (glucosa − 100) / 100", {"sodium": na, "glucose": g}, unidad="mmol/L")

def eos_abs(R, ctx):
    f = _faltan(R, ["wbc", "eosinophils_pct"])
    if f: return _no("eosinofilos_abs", f"faltan: {', '.join(f)}")
    return _ok("eosinofilos_abs", round(_v(R, "wbc") * _v(R, "eosinophils_pct") / 100, 2), "leucocitos × eosinófilos % / 100", {"wbc": _v(R, "wbc"), "eosinophils_pct": _v(R, "eosinophils_pct")}, unidad="x10³/µL")

def fib4(R, ctx):
    f = _faltan(R, ["ast", "alt", "platelets"])
    edad = ctx.get("edad")
    if f or edad is None: return _no("fib4", f"faltan: {', '.join(f) or 'edad'}")
    alt_hi = (R["alt"].get("intervalo_lab") or {}).get("alto")
    ast_hi = (R["ast"].get("intervalo_lab") or {}).get("alto")
    ggt_hi = (R.get("ggt", {}).get("intervalo_lab") or {}).get("alto")
    sano = 33 if ctx.get("sexo") == "hombre" else 25
    enzimas = _v(R, "alt") > sano or (ast_hi and _v(R, "ast") > ast_hi) or (ggt_hi and _v(R, "ggt") and _v(R, "ggt") > ggt_hi)
    diabetes = ctx.get("diabetes_conocida") or (_v(R, "hba1c") or 0) >= 6.5 or (_v(R, "glucose") or 0) >= 126
    cintura = ctx.get("cintura_cm"); metab = cintura is not None and cintura >= (90 if ctx.get("sexo") == "hombre" else 80)
    if not (enzimas or diabetes or metab):
        return _no("fib4", "no aplica: sin enzimas alteradas, diabetes ni cintura alta con otro factor")
    a, l, p = _v(R, "ast"), _v(R, "alt"), _v(R, "platelets")
    nota = []
    if edad < 35: nota.append("Menor de 35 años: FIB-4 menos confiable.")
    if edad > 65 or diabetes: nota.append("Mayor de 65 o con diabetes: un valor bajo no descarta fibrosis.")
    return _ok("fib4", round(edad * a / (p * math.sqrt(l)), 2), "edad × AST / (plaquetas × raíz de ALT)", {"edad": edad, "ast": a, "alt": l, "platelets": p}, " ".join(nota) or None)

def phenoage(R, ctx):
    ids = ["albumin", "creatinine", "glucose", "hs_crp", "lymphocytes_pct", "mcv", "rdw", "alp", "wbc"]
    f = [b for b in ids if _v(R, b) is None and not (b == "hs_crp" and R.get(b, {}).get("estado") == "menor_que_limite")]
    edad = ctx.get("edad")
    if f: return _no("phenoage", f"faltan: {', '.join(f)}")
    if edad is None or edad < 20: return _no("phenoage", "edad menor de 20 o sin dato")
    if (ctx.get("ayuno_horas") or 0) < 8: return _no("phenoage", "glucosa sin ayuno de 8 horas")
    if ctx.get("embarazo"): return _no("phenoage", "no se calcula en embarazo")
    crp_mgl = R["hs_crp"]["valor"]
    alb = _v(R, "albumin") * 10; cr = _v(R, "creatinine") * 88.4; glu = _v(R, "glucose") / 18.016; crp = crp_mgl / 10
    xb = (-19.907 - 0.0336 * alb + 0.0095 * cr + 0.1953 * glu + 0.0954 * math.log(crp) - 0.0120 * _v(R, "lymphocytes_pct")
          + 0.0268 * _v(R, "mcv") + 0.3306 * _v(R, "rdw") + 0.00188 * _v(R, "alp") + 0.0554 * _v(R, "wbc") + 0.0804 * edad)
    g = 0.0076927
    M = 1 - math.exp(-math.exp(xb) * (math.exp(120 * g) - 1) / g)
    pa = 141.50225 + math.log(-0.00553 * math.log(1 - M)) / 0.090165
    nota = []
    if R.get("hs_crp", {}).get("estado") == "menor_que_limite": nota.append("PCR menor que el límite: se usó el límite.")
    if crp_mgl > 10: nota.append("hs-CRP mayor de 10: el valor puede estar inflado temporalmente.")
    rdw_hi = (R["rdw"].get("intervalo_lab") or {}).get("alto")
    if ctx.get("_anemia") or (rdw_hi and _v(R, "rdw") > rdw_hi): nota.append("Anemia o RDW alto: el valor puede estar inflado.")
    return _ok("phenoage", round(pa, 1), "Levine et al. 2018", {b: _v(R, b) if b != "hs_crp" else crp_mgl for b in ids} | {"edad": edad}, " ".join(nota) or None, "años")

def psa_porcentaje(R, ctx):
    f = _faltan(R, ["psa_free", "psa_total"])
    if f: return _no("psa_libre_porcentaje", "PSA libre no medido (solo se mide con PSA total entre 4 y 10)")
    return _ok("psa_libre_porcentaje", round(_v(R, "psa_free") / _v(R, "psa_total") * 100, 1), "PSA libre / PSA total × 100", {"psa_free": _v(R, "psa_free"), "psa_total": _v(R, "psa_total")}, unidad="%")

def imc(R, ctx):
    p, t = ctx.get("peso_kg"), ctx.get("talla_m")
    if p is None or t is None: return _no("imc", "faltan peso y talla de la enfermera")
    return _ok("imc", round(p / t ** 2, 1), "peso / talla²", {"peso_kg": p, "talla_m": t}, unidad="kg/m²")


def calcular_todo(R, ctx, reglas):
    out = {}
    c = imc(R, ctx); out[c["id"]] = c
    if c["calculado"]: ctx = dict(ctx, imc=c["valor"])
    for fn in [homa_ir, non_hdl, remanente, ct_hdl, saturacion, tfg, testo_libre, fai, globulinas, ag, bun_cr, apob_apoa1,
               calcio_corregido, osmolalidad, sodio_corregido, eos_abs, fib4, psa_porcentaje]:
        c = fn(R, ctx); out[c["id"]] = c
    c = hb_ajustada(R, ctx, reglas); out[c["id"]] = c
    c = phenoage(R, ctx); out[c["id"]] = c
    return out
