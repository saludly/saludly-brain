"""Pruebas de la parte 3: condiciones M3 a M6."""
import json, os, sys, copy
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(B), "motor"))
import lector, motor, condiciones_m1m2 as C12, condiciones_m3m6 as C36
IDX = json.load(open(f"{B}/00_INDEX.json", encoding="utf-8"))
LAB = {"transporte_vitamina_c_validado": True}
CASOS = {"E2E-01": ("Ejemplo_resultados_LCD-2026-100123_hombre.pdf", {"documento": "CC 0000000001", "orden": "LCD-2026-100123"}),
         "E2E-02": ("Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-100124"})}
fallos, pasan = [], 0
def chk(ok, msg):
    global pasan
    if ok: pasan += 1
    else: fallos.append(msg)
BASES = {k: (lector.leer(f"{B}/{p}", v, IDX), json.load(open(f"{B}/{k}.json", encoding="utf-8"))) for k, (p, v) in CASOS.items()}

def correr(k, valores=None, ctx=None, campos=None, obs=None):
    lect, e = BASES[k]; l = copy.deepcopy(lect)
    for r in l["resultados"]:
        b = r.get("biomarker_id")
        if b in (valores or {}) and not r.get("campo"):
            nv = valores[b]
            if isinstance(nv, dict): r.update(nv)
            else: r.update(valor=float(nv), estado="medido", operador="=", valor_original=str(nv))
        if (b, r.get("campo")) in (campos or {}): r.update(campos[(b, r.get("campo"))])
    for b, v in (valores or {}).items():
        if isinstance(v, dict) and v.get("_nuevo"):
            l["resultados"].append(dict(biomarker_id=b, campo=None, nombre_original=b, valor=v["valor"], estado=v.get("estado", "medido"), operador="=",
                                        unidad=v.get("unidad"), intervalo_lab=v.get("intervalo"), metodo=v.get("metodo"), muestra="Suero", titulo=v.get("titulo"), dudas=[]))
    if obs: l["observaciones"] = l.get("observaciones", []) + obs
    c = dict(e["contexto"], laboratorio=LAB); c.update(ctx or {})
    p1 = motor.analizar_parte1(l, c)
    m12 = C12.evaluar_m1m2(p1, c)
    return C36.evaluar_m3m6(p1, c, m12)

MOD = ("COND-M3", "COND-M4", "COND-M5", "COND-M6")
for k in CASOS:
    e = BASES[k][1]; out = correr(k)
    json.dump(out, open(f"{B}/salida_parte3_{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for h in e["hallazgos_esperados"]:
        if not h["ficha"].startswith(MOD): continue
        o = out[h["ficha"]]
        chk(o["estado"] == h["estado"], f"{k} {h['ficha']} estado: esperado {h['estado']}, obtenido {o['estado']} ({o.get('nota')})")
        if h.get("coincidencia"): chk(o.get("coincidencia") == h["coincidencia"], f"{k} {h['ficha']} coincidencia: esperado {h['coincidencia']}, obtenido {o.get('coincidencia')}")
        if h.get("escalamiento") is not None: chk(o.get("escalamiento") == h["escalamiento"], f"{k} {h['ficha']} escalamiento: esperado {h['escalamiento']}, obtenido {o.get('escalamiento')}")
    for fid in e["no_activas"]:
        if fid.startswith(MOD): chk(out[fid]["estado"] in ("no_activa", "no_aplica"), f"{k} {fid} debía no activarse: {out[fid]['estado']} ({out[fid].get('nota')})")
    for h in e["incompletas_o_no_calculables"]:
        if h["ficha"].startswith(MOD): chk(out[h["ficha"]]["estado"] == h["estado"], f"{k} {h['ficha']}: esperado {h['estado']}, obtenido {out[h['ficha']]['estado']}")
    chk(out["COND-M6-MI-A02"].get("phenoage") == e["calculados_esperados"]["phenoage"], f"{k} PhenoAge {out['COND-M6-MI-A02'].get('phenoage')}")

H1, M = "E2E-01", "E2E-02"
U = [
 ("HE-001 oculta por altura", M, dict(hemoglobin=13.1, ferritin=60, transferrin_saturation=30, mcv=88, rdw=13), dict(tabaquismo=False), "COND-M3-HE-001", dict(estado="activa", escalamiento=1, coincidencia="alta")),
 ("HE-001 severa", H1, dict(hemoglobin=9.4), dict(tabaquismo=False), "COND-M3-HE-001", dict(estado="activa", escalamiento=3)),
 ("HE-001 embarazo 2.º trimestre", M, dict(hemoglobin=12.0, ferritin=60, transferrin_saturation=30, mcv=88, rdw=13), dict(embarazo=True, semana_gestacion=20, tabaquismo=False), "COND-M3-HE-001", dict(estado="activa", escalamiento=2)),
 ("HE-002 con inflamación", M, dict(ferritin=45, hs_crp=12, transferrin_saturation=12), {}, "COND-M3-HE-002", dict(estado="activa", coincidencia="alta")),
 ("HE-003 mujer", M, dict(hemoglobin=14.4, ferritin=11), {}, "COND-M3-HE-003", dict(estado="activa", escalamiento=1)),
 ("HE-003 hombre", H1, dict(ferritin=12, transferrin_saturation=25), {}, "COND-M3-HE-003", dict(estado="activa", escalamiento=2)),
 ("HE-003 vigilar", M, dict(hemoglobin=14.4, ferritin=22), {}, "COND-M3-HE-003", dict(estado="vigilar")),
 ("HE-004 B12", H1, dict(hemoglobin=10.5, mcv=108, vitamin_b12=140), {}, "COND-M3-HE-004", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("HE-004 folato", H1, dict(hemoglobin=10.5, mcv=103, folate=2.8), {}, "COND-M3-HE-004", dict(estado="activa")),
 ("HE-005 bajas", H1, dict(platelets=82), {}, "COND-M3-HE-005", dict(estado="activa", escalamiento=2)),
 ("HE-005 leves", H1, dict(platelets=128), {}, "COND-M3-HE-005", dict(estado="vigilar", escalamiento=1)),
 ("HE-005 agregados", H1, dict(platelets=64), {}, "COND-M3-HE-005", dict(estado="no_interpretable"), ["Se observan agregados plaquetarios en el frotis."]),
 ("HE-006 hombre", H1, dict(ferritin=640, transferrin_saturation=62, hs_crp=1, alt=30, ggt=40), {}, "COND-M3-HE-006", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("HE-A01", M, dict(ferritin=180, transferrin_saturation=14, hs_crp=22), {}, "COND-M3-HE-A01", dict(estado="apoyo")),
 ("HE-A01 sube escalamiento", M, dict(hemoglobin=13.0, ferritin=180, transferrin_saturation=14, hs_crp=22), dict(tabaquismo=False), "COND-M3-HE-001", dict(escalamiento=2)),
 ("HE-A02 varias líneas", H1, dict(wbc=2.9, platelets=95, hemoglobin=10.0), {}, "COND-M3-HE-A02", dict(estado="activa", escalamiento=2)),
 ("HE-A03 eosinofilia", H1, dict(eosinophils_pct=9), {}, "COND-M3-HE-A03", dict(estado="apoyo", escalamiento=1)),
 ("NU-001 metformina", H1, dict(vitamin_b12=150), dict(medicamentos=["Metformina"]), "COND-M3-NU-001", dict(estado="activa", coincidencia="alta", escalamiento=1)),
 ("NU-001 funcional", H1, dict(vitamin_b12=240, methylmalonic_acid={"valor": 0.62, "estado": "medido", "_nuevo": True, "unidad": "µmol/L", "intervalo": {"bajo": 0, "alto": 0.4, "texto": "0,00 – 0,40"}}), {}, "COND-M3-NU-001", dict(estado="activa", coincidencia="alta")),
 ("NU-001 indeterminada sin AMM", H1, dict(vitamin_b12=240), {}, "COND-M3-NU-001", dict(estado="vigilar")),
 ("NU-002 posible", H1, dict(folate=3.6), {}, "COND-M3-NU-002", dict(estado="activa", coincidencia="moderada")),
 ("NU-002 embarazo", M, dict(folate=3.2), dict(embarazo=True, semana_gestacion=8), "COND-M3-NU-002", dict(escalamiento=2)),
 ("NU-A01 refuerza", H1, dict(vitamin_b12=150, homocysteine=19), {}, "COND-M3-NU-A01", dict(estado="apoyo")),
 ("NU-A01 vigilar", H1, dict(homocysteine=17), {}, "COND-M3-NU-A01", dict(estado="vigilar")),
 ("NU-A03 alta", H1, dict(vitamin_d=140), {}, "COND-M3-NU-A03", dict(estado="activa", escalamiento=1)),
 ("NU-A04 biotina declarada", H1, {}, dict(suplementos=["Biotina para el cabello"]), "COND-M3-NU-A04", dict(estado="activa", escalamiento=1)),
 ("NU-A04 vitamina A alta", H1, dict(vitamin_a=112), {}, "COND-M3-NU-A04", dict(escalamiento=1)),
 ("NU-A04 tiamina con síntomas", H1, dict(vitamin_b1=45), dict(alcohol_consumo=True, sintomas_neurologicos=True), "COND-M3-NU-A04", dict(escalamiento=3)),
 ("GA-001 indeterminado", H1, dict(ast=48, alt=52, platelets=190, hba1c=6.6, glucose=130), dict(edad=58), "COND-M4-GA-001", dict(estado="activa", coincidencia="moderada", escalamiento=1)),
 ("GA-001 alto", H1, dict(ast=70, alt=45, platelets=140), dict(edad=62), "COND-M4-GA-001", dict(estado="activa", escalamiento=2)),
 ("GA-002 muy alta", H1, dict(alt=190), {}, "COND-M4-GA-002", dict(estado="activa", escalamiento=2)),
 ("GA-002 limítrofe", M, dict(alt=31), {}, "COND-M4-GA-002", dict(estado="vigilar")),
 ("GA-002 muscular", H1, dict(alt=48, ast=85, ck_cpk=2400, ldh=260), dict(ejercicio_intenso_48h=True), "COND-M4-GA-002", dict(estado="no_activa")),
 ("GA-003 colestasis", H1, dict(alp=260, ggt=180, alt=40), {}, "COND-M4-GA-003", dict(estado="activa", escalamiento=2)),
 ("GA-003 óseo", H1, dict(alp=170, ggt=30, alt=30), {}, "COND-M4-GA-003", dict(estado="vigilar")),
 ("GA-004 positivo", H1, dict(fit_stool={"valor": "positivo", "estado": "cualitativo"}), {}, "COND-M4-GA-004", dict(estado="activa", escalamiento=2)),
 ("GA-005 negativo con omeprazol", M, {}, dict(medicamentos=["Omeprazol"]), "COND-M4-GA-005", dict(estado="no_activa")),
 ("GA-006 positivo", M, dict(anti_ttg_iga=48), dict(dieta_sin_gluten=False), "COND-M4-GA-006", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("GA-006 déficit de IgA", M, dict(iga=5), {}, "COND-M4-GA-006", dict(estado="no_interpretable")),
 ("GA-006 pendiente por ALT", H1, {}, {}, "COND-M4-GA-006", dict(estado="pendiente_refleja")),
 ("GA-A01 aislada", M, dict(bilirubin_total=1.9, bilirubin_direct=0.3), {}, "COND-M4-GA-A01", dict(estado="activa", escalamiento=0)),
 ("GA-A02 alcohol", H1, dict(ast=92, alt=40, ggt=210), dict(alcohol_consumo=True), "COND-M4-GA-A02", dict(estado="apoyo")),
 ("IN-001 activa", H1, dict(anti_hcv={"valor": "reactivo", "estado": "cualitativo"}, hcv_rna={"valor": "detectable", "estado": "cualitativo", "_nuevo": True}), {}, "COND-M4-IN-001", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("IN-001 pendiente", H1, dict(anti_hcv={"valor": "reactivo", "estado": "cualitativo"}), {}, "COND-M4-IN-001", dict(estado="pendiente_refleja")),
 ("IN-002 activa", H1, dict(hbsag={"valor": "reactivo", "estado": "cualitativo"}), {}, "COND-M4-IN-002", dict(estado="activa", escalamiento=2)),
 ("IN-002 resuelta", H1, dict(anti_hbc={"valor": "reactivo", "estado": "cualitativo"}, anti_hbs=120), {}, "COND-M4-IN-002", dict(escalamiento=1)),
 ("IN-002 anti-HBc aislado", H1, dict(anti_hbc={"valor": "reactivo", "estado": "cualitativo"}, anti_hbs=3), {}, "COND-M4-IN-002", dict(escalamiento=2)),
 ("IN-003 positivo", H1, dict(chagas_elisa_total={"valor": "reactivo", "estado": "cualitativo"}, chagas_elisa_recombinante={"valor": "reactivo", "estado": "cualitativo", "_nuevo": True}), dict(procedencia_endemica=True), "COND-M4-IN-003", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("IN-003 discordante", H1, dict(chagas_elisa_total={"valor": "reactivo", "estado": "cualitativo"}, chagas_elisa_recombinante={"valor": "no reactivo", "estado": "cualitativo", "_nuevo": True}), {}, "COND-M4-IN-003", dict(estado="pendiente_refleja")),
 ("MU-001 positivo", M, dict(testosterone_total=72, shbg=22, tsh=2.0), {}, "COND-M5-MU-001", dict(estado="activa", coincidencia="alta", escalamiento=1)),
 ("MU-001 con TSH alta", M, dict(testosterone_total=72, shbg=22), {}, "COND-M5-MU-001", dict(estado="activa", coincidencia="moderada")),
 ("MU-001 muy alta", M, dict(testosterone_total=140, shbg=40), {}, "COND-M5-MU-001", dict(escalamiento=2)),
 ("MU-001 anticonceptivo", M, dict(testosterone_total=60), dict(anticonceptivo_hormonal=True), "COND-M5-MU-001", dict(estado="no_interpretable")),
 ("MU-002 positivo", M, dict(fsh=38), dict(edad=33), "COND-M5-MU-002", dict(estado="activa", coincidencia="moderada", escalamiento=2)),
 ("MU-002 edad 50", M, dict(fsh=60), dict(edad=50), "COND-M5-MU-002", dict(estado="no_aplica")),
 ("MU-003 pendiente", M, dict(prolactin=41), {}, "COND-M5-MU-003", dict(estado="pendiente_refleja")),
 ("MU-003 con risperidona", M, dict(prolactin=35, macroprolactin={"valor": 75.0, "estado": "medido", "_nuevo": True, "unidad": "%", "intervalo": {"bajo": 40, "alto": None, "texto": "> 40 %"}}), dict(medicamentos=["Risperidona"]), "COND-M5-MU-003", dict(estado="vigilar")),
 ("MU-003 macroprolactina", M, dict(prolactin=38, macroprolactin={"valor": 25.0, "estado": "medido", "_nuevo": True, "unidad": "%", "intervalo": {"bajo": 40, "alto": None, "texto": "> 40 %"}}), {}, "COND-M5-MU-003", dict(estado="activa", escalamiento=0)),
 ("MU-A01 anemia en embarazo", M, dict(hemoglobin=12.0, ferritin=60, transferrin_saturation=30, mcv=88, rdw=13), dict(embarazo=True, semana_gestacion=26, tabaquismo=False), "COND-M5-MU-A01", dict(estado="apoyo", escalamiento=2)),
 ("UR-001 tamizaje", H1, dict(psa_total=5.6), dict(edad=58), "COND-M5-UR-001", dict(estado="activa", escalamiento=2)),
 ("UR-001 fuera de edad", H1, dict(psa_total=4.8), {}, "COND-M5-UR-001", dict(estado="activa", escalamiento=1)),
 ("UR-001 finasterida", H1, dict(psa_total=2.6), dict(medicamentos=["Finasterida"]), "COND-M5-UR-001", dict(estado="activa")),
 ("UR-001 sin consentimiento", H1, dict(psa_total=5.6), dict(consentimientos={"psa": False}), "COND-M5-UR-001", dict(estado="no_aplica")),
 ("UR-002 sin certificación", H1, dict(testosterone_total=230), {}, "COND-M5-UR-002", dict(estado="vigilar")),
 ("UR-002 certificado muy baja", H1, dict(testosterone_total={"valor": 120.0, "estado": "medido", "metodo": "Quimioluminiscencia (certificado CDC HoST)"}), {}, "COND-M5-UR-002", dict(estado="activa", escalamiento=2)),
 ("UR-002 hora", H1, dict(testosterone_total=240), dict(hora_toma="15:00"), "COND-M5-UR-002", dict(estado="no_interpretable")),
 ("RE-001 diurético", H1, dict(uric_acid=8.2), dict(medicamentos=["Hidroclorotiazida"]), "COND-M6-RE-001", dict(estado="activa", escalamiento=1)),
 ("RE-A01 1:80 AC-2", H1, dict(ana_hep2={"valor": "positivo", "estado": "cualitativo", "titulo": "1:80"}), {}, "COND-M6-RE-A01", dict(estado="activa", escalamiento=1), ["ANA positivo 1:80, patrón moteado fino denso (AC-2)."]),
 ("RE-A01 sin título", H1, dict(ana_hep2={"valor": "positivo", "estado": "cualitativo", "titulo": None}), {}, "COND-M6-RE-A01", dict(estado="no_interpretable")),
 ("RE-A02 muy alta", H1, dict(esr=110), {}, "COND-M6-RE-A02", dict(escalamiento=2)),
 ("MI-001 mayor", H1, dict(hs_crp=9), dict(edad=74, peso_kg=58, talla_m=1.67), "COND-M6-MI-001", dict(estado="activa", escalamiento=2)),
 ("MI-001 vigilar", M, {}, dict(peso_kg=50, talla_m=1.62, ingesta_reducida=False), "COND-M6-MI-001", dict(estado="vigilar")),
 ("MI-A01 recordatorio", M, {}, {}, "COND-M6-MI-A01", dict(estado="apoyo", recordatorios=["tamizaje de cuello uterino"])),
 ("MI-A02 sin ayuno", H1, {}, dict(ayuno_horas=4), "COND-M6-MI-A02", dict(estado="no_calculable")),
]
for caso in U:
    nombre, base, vals, ctx, fid, esp = caso[:6]; obs = caso[6] if len(caso) > 6 else None
    o = correr(base, vals, ctx, obs=obs)[fid]
    for k2, v2 in esp.items():
        chk(o.get(k2) == v2, f"[{nombre}] {fid} {k2}: esperado {v2}, obtenido {o.get(k2)} · {o.get('nota')}")
print(f"Casos unitarios estructurados: {len(U)}")
print(f"Pasan {pasan} de {pasan + len(fallos)} comprobaciones")
for f in fallos: print("  FALLA:", f)
