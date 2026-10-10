"""Pruebas de la parte 1 del motor: cálculos y clasificación."""
import json, os, sys, copy
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(B), "motor"))
import lector, motor
IDX = json.load(open(f"{B}/00_INDEX.json", encoding="utf-8"))
fallos = []; pasan = 0
def chk(cond, msg):
    global pasan
    if cond: pasan += 1
    else: fallos.append(msg)

LAB = {"transporte_vitamina_c_validado": True}   # el laboratorio de ejemplo declara transporte congelado validado
CASOS = {"E2E-01": ("Ejemplo_resultados_LCD-2026-100123_hombre.pdf", {"documento": "CC 0000000001", "orden": "LCD-2026-100123"}),
         "E2E-02": ("Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-100124"})}
CLASES = {
 "E2E-01": dict(glucose="alto", hba1c="alto", triglycerides="alto", hdl_c="bajo", ldl_c="alto", apob="alto", uric_acid="alto", alt="alto", ggt="alto",
                vitamin_d="bajo", hs_crp="alto", hs_troponin="en_rango", anti_hbs="bajo", hbsag="en_rango", anti_hcv="en_rango", hpylori_stool_ag="alterado",
                uacr="alto", ana_hep2="en_rango", fit_stool="en_rango", ferritin="en_rango", cortisol="en_rango", tsh="en_rango", biotin=None, vitamin_c="en_rango", hemoglobin="en_rango", psa_total="en_rango"),
 "E2E-02": dict(hemoglobin="bajo", mcv="bajo", rdw="alto", ferritin="bajo", transferrin_saturation="bajo", tsh="alto", free_t4="en_rango", anti_tpo="alto",
                lpa="alto", ldl_c="alto", vitamin_d="bajo", potassium="no_interpretable", vitamin_c="no_interpretable", ana_hep2="alterado", fsh="en_rango",
                progesterone="en_rango", anti_ttg_iga="en_rango", iga="en_rango", methylmalonic_acid="en_rango", vitamin_b12="en_rango", omega3_index=None, cortisol="en_rango", anti_hbs="en_rango")}
for k, (pdf, vis) in CASOS.items():
    e = json.load(open(f"{B}/{k}.json", encoding="utf-8"))
    lect = lector.leer(f"{B}/{pdf}", vis, IDX)
    out = motor.analizar_parte1(lect, dict(e["contexto"], laboratorio=LAB))
    R = {r["biomarker_id"]: r for r in out["resultados"] if r.get("biomarker_id") and not r.get("campo")}
    for b, c in CLASES[k].items():
        chk(R.get(b, {}).get("clase") == c, f"{k} clase {b}: esperado {c}, obtenido {R.get(b, {}).get('clase')} ({R.get(b, {}).get('motivo_clase')})")
    for cid, esp in e["calculados_esperados"].items():
        cc = out["calculados"].get({"hemoglobina_ajustada_altitud": "hemoglobina_ajustada"}.get(cid, cid))
        if isinstance(esp, str):
            chk(cc is not None and not cc["calculado"], f"{k} {cid}: esperado no calculado ({esp}), obtenido {cc}")
        else:
            tol = 0.15 if cid == "phenoage" else 0.051
            chk(cc is not None and cc["calculado"] and abs(cc["valor"] - esp) <= tol * (1 if cid in ("phenoage",) or abs(esp) < 50 else 2), f"{k} {cid}: esperado {esp}, obtenido {cc and cc.get('valor')} {cc and cc.get('motivo')}")
    print(k, "resumen de clases:", out["resumen_clases"])
    json.dump(out, open(f"{B}/salida_parte1_{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# Pruebas de contexto sobre una copia del caso de la mujer
e2 = json.load(open(f"{B}/E2E-02.json", encoding="utf-8"))
base = lector.leer(f"{B}/{CASOS['E2E-02'][0]}", CASOS["E2E-02"][1], IDX)
def con(cambios_valor=None, ctx_cambios=None):
    l = copy.deepcopy(base)
    for r in l["resultados"]:
        if r.get("biomarker_id") in (cambios_valor or {}) and not r.get("campo"):
            r.update(cambios_valor[r["biomarker_id"]])
    c = dict(e2["contexto"], laboratorio=LAB); c.update(ctx_cambios or {})
    o = motor.analizar_parte1(l, c)
    return {r["biomarker_id"]: r for r in o["resultados"] if r.get("biomarker_id") and not r.get("campo")}, o
R, _ = con({"alt": {"valor": 31.0}}); chk(R["alt"]["clase"] == "limitrofe", f"ALT 31 en mujer: {R['alt']['clase']}")
R, _ = con(ctx_cambios={"hora_toma": "11:20"}); chk(R["cortisol"]["clase"] == "no_interpretable", "cortisol a las 11:20")
R, o = con(ctx_cambios={"ayuno_horas": 4}); chk(R["glucose"]["clase"] == "no_interpretable" and not o["calculados"]["homa_ir"]["calculado"], "ayuno de 4 horas")
R, _ = con(ctx_cambios={"suplementos": ["Biotina para el cabello"]}); chk(R["tsh"]["clase"] == "no_interpretable" and R["vitamin_b12"]["clase"] == "no_interpretable", "biotina declarada")
R, _ = con(ctx_cambios={"anticonceptivo_hormonal": True}); chk(R["fsh"]["clase"] == "no_interpretable" and R["prolactin"]["clase"] != "no_interpretable", "anticonceptivo hormonal")
R, _ = con(ctx_cambios={"laboratorio": {"transporte_vitamina_c_validado": False}}); chk(R["vitamin_c"]["clase"] == "no_interpretable", "vitamina C sin transporte validado")
R, _ = con({"hs_troponin": {"valor": 31.0, "estado": "medido", "operador": "="}}); chk(R["hs_troponin"]["clase"] == "critico", f"troponina 31: {R['hs_troponin']['clase']}")
R, _ = con({"glucose": {"valor": 50.0}}); chk(R["glucose"]["clase"] == "critico", "glucosa 50")
R, _ = con({"hdl_c": {"valor": 50.0}}); chk(R["hdl_c"]["clase"] == "bajo", f"HDL 50 con intervalo '> 50': {R['hdl_c']['clase']}")
R, _ = con({"total_cholesterol": {"valor": 200.0}}); chk(R["total_cholesterol"]["clase"] == "alto", f"colesterol 200 con intervalo '< 200': {R['total_cholesterol']['clase']}")
R, _ = con({"ferritin": {"valor": 22.0}}); chk(R["ferritin"]["clase"] == "limitrofe", f"ferritina 22: {R['ferritin']['clase']}")
R, o = con(ctx_cambios={"ciudad": "Medellín"}); chk(o["calculados"]["hemoglobina_ajustada"]["valor"] == 11.2 and "por verificar" in (o["calculados"]["hemoglobina_ajustada"].get("nota") or ""), "Medellín sin franja de altitud escrita")
R, o = con(ctx_cambios={"embarazo": True}); chk(R["prolactin"]["clase"] == "no_interpretable" and not o["calculados"]["phenoage"]["calculado"], "embarazo")
R, o = con({"glucose": {"valor": 420.0}, "sodium": {"valor": 131.0}}); chk(o["calculados"]["sodio_corregido"]["valor"] == 136.1, f"sodio corregido {o['calculados']['sodio_corregido']}")
print(f"\nPasan {pasan} de {pasan + len(fallos)} comprobaciones")
for f in fallos: print("  FALLA:", f)
