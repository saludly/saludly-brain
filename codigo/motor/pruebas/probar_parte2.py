"""Pruebas de la parte 2: condiciones M1 y M2."""
import json, os, sys, copy
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(B), "motor"))
import lector, motor, condiciones_m1m2 as C
IDX = json.load(open(f"{B}/00_INDEX.json", encoding="utf-8"))
LAB = {"transporte_vitamina_c_validado": True}
CASOS = {"E2E-01": ("Ejemplo_resultados_LCD-2026-100123_hombre.pdf", {"documento": "CC 0000000001", "orden": "LCD-2026-100123"}),
         "E2E-02": ("Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-100124"})}
fallos, pasan = [], 0
def chk(ok, msg):
    global pasan
    if ok: pasan += 1
    else: fallos.append(msg)
BASES = {}
for k, (pdf, vis) in CASOS.items():
    BASES[k] = (lector.leer(f"{B}/{pdf}", vis, IDX), json.load(open(f"{B}/{k}.json", encoding="utf-8")))

def correr(k, valores=None, ctx=None):
    lect, e = BASES[k]; l = copy.deepcopy(lect)
    for r in l["resultados"]:
        b = r.get("biomarker_id")
        if b in (valores or {}) and not r.get("campo"):
            nv = valores[b]
            if isinstance(nv, dict): r.update(nv)
            else: r.update(valor=float(nv), estado="medido", operador="=", valor_original=str(nv))
    extra = [dict(biomarker_id=b, campo=None, nombre_original=b, valor=float(v["valor"]), estado="medido", operador="=", unidad=v.get("unidad"),
                  intervalo_lab=v.get("intervalo"), metodo=v.get("metodo"), muestra="Suero", dudas=[]) for b, v in (valores or {}).items()
             if isinstance(v, dict) and v.get("_nuevo")]
    l["resultados"] += extra
    c = dict(e["contexto"], laboratorio=LAB); c.update(ctx or {})
    p1 = motor.analizar_parte1(l, c)
    return C.evaluar_m1m2(p1, c)

# 1) Casos de punta a punta, filtrados a M1 y M2
for k in CASOS:
    e = BASES[k][1]; out = correr(k)
    json.dump(out, open(f"{B}/salida_parte2_{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for h in e["hallazgos_esperados"]:
        if not h["ficha"].startswith(("COND-M1", "COND-M2")): continue
        o = out[h["ficha"]]
        chk(o["estado"] == h["estado"], f"{k} {h['ficha']} estado: esperado {h['estado']}, obtenido {o['estado']} ({o.get('nota')})")
        if h.get("coincidencia"): chk(o.get("coincidencia") == h["coincidencia"], f"{k} {h['ficha']} coincidencia: esperado {h['coincidencia']}, obtenido {o.get('coincidencia')}")
        if h.get("escalamiento") is not None: chk(o.get("escalamiento") == h["escalamiento"], f"{k} {h['ficha']} escalamiento: esperado {h['escalamiento']}, obtenido {o.get('escalamiento')}")
    for fid in e["no_activas"]:
        if fid.startswith(("COND-M1", "COND-M2")):
            chk(out[fid]["estado"] in ("no_activa", "no_aplica"), f"{k} {fid} debía no activarse: {out[fid]['estado']} ({out[fid].get('nota')})")
    for h in e["incompletas_o_no_calculables"]:
        if h["ficha"].startswith(("COND-M1", "COND-M2")):
            chk(out[h["ficha"]]["estado"] == h["estado"], f"{k} {h['ficha']}: esperado {h['estado']}, obtenido {out[h['ficha']]['estado']}")

# 2) Casos unitarios estructurados (de las fichas M1 y M2)
H1, M2_ = "E2E-01", "E2E-02"   # base hombre 46 / mujer 34
U = [
 ("CA-001 vigilar", H1, dict(ldl_c=120, total_cholesterol=155, hdl_c=35, triglycerides=210), {}, "COND-M1-CA-001", dict(estado="vigilar")),
 ("CA-001 negativo", H1, dict(ldl_c=110, total_cholesterol=185, hdl_c=50, triglycerides=120), {}, "COND-M1-CA-001", dict(estado="no_activa")),
 ("CA-001 con estatina", H1, {}, dict(medicamentos=["Atorvastatina"]), "COND-M1-CA-001", dict(estado="control")),
 ("CA-002 alto", H1, dict(ldl_c=205, total_cholesterol=280), dict(antecedente_familiar_cv_temprano=True), "COND-M1-CA-002", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("CA-002 excluye CA-001", H1, dict(ldl_c=205, total_cholesterol=280), {}, "COND-M1-CA-001", dict(estado="no_activa")),
 ("CA-003 muy alto", H1, dict(triglycerides=620), dict(alcohol_48h=False), "COND-M1-CA-003", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("CA-003 sin ayuno", H1, dict(triglycerides=260), dict(ayuno_horas=4), "COND-M1-CA-003", dict(estado="no_interpretable")),
 ("CA-004 nmol", H1, dict(lpa={"valor": 140.0, "unidad": "nmol/L", "estado": "medido"}), {}, "COND-M1-CA-004", dict(estado="activa")),
 ("CA-004 sin unidad", H1, dict(lpa={"valor": 70.0, "unidad": "", "estado": "medido"}), {}, "COND-M1-CA-004", dict(estado="no_interpretable")),
 ("CA-005 con diabetes", H1, dict(hba1c=7.1), dict(edad=58, presion_sistolica=130, tabaquismo=False), "COND-M1-CA-005", dict(estado="no_calculable")),
 ("CA-005 muy alto", H1, dict(total_cholesterol=245, hdl_c=38), dict(edad=62, presion_sistolica=152, tabaquismo=True), "COND-M1-CA-005", dict(estado="activa", coincidencia="alta", escalamiento=2, categoria="muy_alto", riesgo_10_anos_pct=13.1)),
 ("CA-005 bajo", H1, {}, dict(presion_sistolica=128, presion_diastolica=80, tabaquismo=False), "COND-M1-CA-005", dict(estado="no_activa", riesgo_10_anos_pct=2.2)),
 ("CA-005 fuera de edad", M2_, {}, dict(presion_sistolica=120, tabaquismo=False), "COND-M1-CA-005", dict(estado="no_calculable")),
 ("CA-006 grado 1", H1, {}, dict(presion_sistolica=134, presion_diastolica=84), "COND-M1-CA-006", dict(estado="activa", coincidencia="moderada", escalamiento=1)),
 ("CA-006 grado 2 con automonitoreo", H1, {}, dict(presion_sistolica=146, presion_diastolica=92, ampa_promedio={"sistolica": 141, "diastolica": 89, "dias": 7}), "COND-M1-CA-006", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("CA-006 severa", H1, {}, dict(presion_sistolica=184, presion_diastolica=112), "COND-M1-CA-006", dict(escalamiento=3)),
 ("CA-006 conocida", H1, {}, dict(presion_sistolica=138, presion_diastolica=86, hipertension_conocida=True), "COND-M1-CA-006", dict(estado="control")),
 ("CA-007 positivo", H1, dict(hba1c=7.2, glucose=148, nt_probnp={"valor": 210.0, "estado": "medido", "_nuevo": True, "unidad": "pg/mL"}), {}, "COND-M1-CA-007", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("CA-007 pendiente", H1, dict(hba1c=7.2, glucose=148), {}, "COND-M1-CA-007", dict(estado="pendiente_refleja")),
 ("CA-A01 discordancia", H1, dict(apob=138, ldl_c=118, total_cholesterol=200, triglycerides=240), {}, "COND-M1-CA-A01", dict(estado="apoyo")),
 ("CA-A02 infección", H1, dict(hs_crp=4.1), dict(infeccion_reciente=True), "COND-M1-CA-A02", dict(estado="no_activa")),
 ("CA-A02 aguda", H1, dict(hs_crp=18), {}, "COND-M1-CA-A02", dict(estado="no_activa")),
 ("EM-001 moderada", M2_, dict(glucose=94, hba1c=5.9), dict(), "COND-M1-EM-001", dict(estado="vigilar")),   # mujer con anemia: HbA1c sola pierde confianza
 ("EM-001 moderada sin anemia", H1, dict(glucose=94, hba1c=5.9), {}, "COND-M1-EM-001", dict(estado="activa", coincidencia="moderada")),
 ("EM-002 alta", H1, dict(glucose=138, hba1c=6.9), {}, "COND-M1-EM-002", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("EM-002 excluye EM-001", H1, dict(glucose=138, hba1c=6.9), {}, "COND-M1-EM-001", dict(estado="no_activa")),
 ("EM-002 conocida", H1, dict(glucose=150, hba1c=7.4), dict(diabetes_conocida=True, medicamentos=["Metformina"]), "COND-M1-EM-002", dict(estado="control")),
 ("EM-003 alta 4 de 5", H1, {}, dict(cintura_cm=98, presion_sistolica=128, presion_diastolica=82), "COND-M1-EM-003", dict(estado="activa", coincidencia="alta")),
 ("EM-003 incompleta", H1, dict(triglycerides=170, hdl_c=52, glucose=92, hba1c=5.4), {}, "COND-M1-EM-003", dict(estado="incompleta")),
 ("EM-004 obesidad", H1, {}, dict(peso_kg=92, talla_m=1.75, cintura_cm=104), "COND-M1-EM-004", dict(estado="activa", escalamiento=1)),
 ("EM-004 clase 3", H1, {}, dict(peso_kg=118, talla_m=1.68), "COND-M1-EM-004", dict(escalamiento=2)),
 ("EM-005 significativa confiable", H1, dict(glucose=50), {}, "COND-M1-EM-005", dict(estado="activa", escalamiento=3)),
 ("EM-005 con sulfonilurea", H1, dict(glucose=66), dict(medicamentos=["Glibenclamida"]), "COND-M1-EM-005", dict(escalamiento=2)),
 ("EM-A01 vigilar", M2_, {}, dict(findrisc_puntaje=13), "COND-M1-EM-A01", dict(estado="vigilar")),
 ("EM-A02 vigilar", M2_, dict(glucose=90, insulin=14), {}, "COND-M1-EM-A02", dict(estado="vigilar")),
 ("NE-001 G3a", H1, dict(creatinine=1.55, egfr=52, uacr=12), {}, "COND-M2-NE-001", dict(estado="activa", coincidencia="moderada", escalamiento=1)),
 ("NE-001 G3b A2", H1, dict(creatinine=2.0, egfr=38, uacr=80), {}, "COND-M2-NE-001", dict(estado="activa", escalamiento=2)),
 ("NE-001 G4", H1, dict(creatinine=3.2, egfr=22), {}, "COND-M2-NE-001", dict(escalamiento=3)),
 ("NE-001 no confirma con cistatina", H1, dict(creatinine=1.5, egfr=55, uacr=10, cystatin_c={"valor": 0.85, "estado": "medido", "_nuevo": True, "unidad": "mg/L"}), {}, "COND-M2-NE-001", dict(estado="vigilar")),
 ("NE-002 A3", H1, dict(uacr=420), {}, "COND-M2-NE-002", dict(estado="activa", escalamiento=2)),
 ("NE-002 con ejercicio", H1, dict(uacr=60), dict(ejercicio_intenso_48h=True), "COND-M2-NE-002", dict(estado="vigilar")),
 ("NE-003 diabetes", H1, dict(uacr=85), dict(diabetes_conocida=True), "COND-M2-NE-003", dict(estado="activa", escalamiento=2)),
 ("NE-003 vigilar con presión sin confirmar", H1, {}, dict(presion_sistolica=134, presion_diastolica=84), "COND-M2-NE-003", dict(estado="vigilar")),
 ("NE-004 leve", H1, dict(potassium=5.3), {}, "COND-M2-NE-004", dict(estado="activa", escalamiento=1)),
 ("NE-004 accionable", H1, dict(potassium=5.8, creatinine=1.6, egfr=48), dict(medicamentos=["Losartan"]), "COND-M2-NE-004", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("NE-004 hemolizado", M2_, {}, {}, "COND-M2-NE-004", dict(estado="no_interpretable")),
 ("NE-005 leve", H1, dict(sodium=132), {}, "COND-M2-NE-005", dict(estado="activa", escalamiento=1)),
 ("NE-005 profundo", H1, dict(sodium=121), {}, "COND-M2-NE-005", dict(escalamiento=3)),
 ("NE-005 corregido", H1, dict(sodium=131, glucose=420), {}, "COND-M2-NE-005", dict(estado="no_activa")),
 ("NE-005 pseudo", H1, dict(sodium=129, triglycerides=1400), {}, "COND-M2-NE-005", dict(estado="no_interpretable")),
 ("NE-A01 muy bajo", H1, dict(potassium=2.8), {}, "COND-M2-NE-A01", dict(estado="activa", escalamiento=2)),
 ("TI-001 positivo", M2_, {}, {}, "COND-M2-TI-001", dict(estado="activa", coincidencia="alta", escalamiento=1)),
 ("TI-001 TSH ≥ 10", M2_, dict(tsh=11.4), {}, "COND-M2-TI-001", dict(escalamiento=2)),
 ("TI-001 vigilar", M2_, dict(tsh=4.6), {}, "COND-M2-TI-001", dict(estado="vigilar")),
 ("TI-001 mayor de 60", M2_, dict(tsh=5.6), dict(edad=68), "COND-M2-TI-001", dict(estado="vigilar")),
 ("TI-001 biotina", M2_, dict(tsh=7.2), dict(suplementos=["Biotina"]), "COND-M2-TI-001", dict(estado="no_interpretable")),
 ("TI-002", M2_, dict(tsh=14.2, free_t4=0.71), {}, "COND-M2-TI-002", dict(estado="activa", escalamiento=2)),
 ("TI-002 excluye TI-001", M2_, dict(tsh=14.2, free_t4=0.71), {}, "COND-M2-TI-001", dict(estado="no_activa")),
 ("TI-003", M2_, dict(tsh=1.4, free_t4=0.68), {}, "COND-M2-TI-003", dict(estado="activa", escalamiento=2)),
 ("TI-004 suprimida", M2_, dict(tsh=0.05, free_t4=1.3, free_t3=3.2), {}, "COND-M2-TI-004", dict(estado="activa", escalamiento=2)),
 ("TI-005 T3-toxicosis", M2_, dict(tsh=0.02, free_t4=1.5, free_t3=6.1), {}, "COND-M2-TI-005", dict(estado="activa", escalamiento=2)),
 ("TI-006 embarazo", M2_, dict(tsh=4.8), dict(embarazo=True, semana_gestacion=10), "COND-M2-TI-006", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("TI-007 positivo", H1, dict(calcium=10.9, albumin=4.2, pth={"valor": 78.0, "estado": "medido", "_nuevo": True, "unidad": "pg/mL", "intervalo": {"bajo": 15, "alto": 65, "texto": "15 – 65"}}), {}, "COND-M2-TI-007", dict(estado="activa", coincidencia="moderada", escalamiento=2)),
 ("TI-007 pendiente", H1, dict(calcium=10.9, albumin=4.2), {}, "COND-M2-TI-007", dict(estado="pendiente_refleja")),
 ("TI-008 positivo", H1, dict(potassium=3.3, aldosterone={"valor": 18.0, "estado": "medido", "_nuevo": True, "unidad": "ng/dL", "metodo": "Quimioluminiscencia"},
     renin={"valor": 0.4, "estado": "medido", "_nuevo": True, "unidad": "ng/mL/h"}), dict(presion_sistolica=148, presion_diastolica=94), "COND-M2-TI-008", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("TI-008 betabloqueador", H1, dict(aldosterone={"valor": 12.0, "estado": "medido", "_nuevo": True, "unidad": "ng/dL"}, renin={"valor": 0.5, "estado": "medido", "_nuevo": True, "unidad": "ng/mL/h"}),
     dict(presion_sistolica=146, presion_diastolica=90, medicamentos=["Metoprolol"]), "COND-M2-TI-008", dict(estado="activa", coincidencia="moderada")),
 ("TI-008 concentración", H1, dict(aldosterone={"valor": 450.0, "estado": "medido", "_nuevo": True, "unidad": "pmol/L"}, renin={"valor": 4.0, "estado": "medido", "_nuevo": True, "unidad": "mU/L"}),
     dict(presion_sistolica=150, presion_diastolica=95), "COND-M2-TI-008", dict(estado="activa")),
 ("TI-008 sin presión", H1, {}, {}, "COND-M2-TI-008", dict(estado="no_aplica")),
 ("TI-A01 refuerza", M2_, {}, {}, "COND-M2-TI-A01", dict(estado="apoyo")),
]
for nombre, base, vals, ctx, fid, esp in U:
    o = correr(base, vals, ctx)[fid]
    for k2, v2 in esp.items():
        chk(o.get(k2) == v2, f"[{nombre}] {fid} {k2}: esperado {v2}, obtenido {o.get(k2)} · {o.get('nota')}")
import score2 as S2
for sexo, region, esp in (("hombre", "baja", 5.9), ("hombre", "muy_alta", 14.0), ("mujer", "baja", 4.2), ("mujer", "muy_alta", 13.7)):
    v = round(100 * S2.score2(sexo, 50, 1, 140, 5.5, 1.3, region), 1)
    chk(v == esp, f"SCORE2 ejemplo publicado {sexo} {region}: esperado {esp}, obtenido {v}")
print(f"Casos unitarios estructurados: {len(U)} + 4 validaciones de SCORE2 contra el artículo")
print(f"Pasan {pasan} de {pasan + len(fallos)} comprobaciones")
for f in fallos: print("  FALLA:", f)
