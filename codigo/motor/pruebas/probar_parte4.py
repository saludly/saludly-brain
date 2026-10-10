"""Pruebas de la parte 4: relaciones, seguridad y salida final."""
import json, os, sys, copy
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(B), "motor"))
import lector, motor
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

def correr(k, valores=None, ctx=None, campos=None):
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
                                        unidad=v.get("unidad"), intervalo_lab=v.get("intervalo"), metodo=v.get("metodo"), muestra="Suero", dudas=[]))
    c = dict(e["contexto"], laboratorio=LAB); c.update(ctx or {})
    return motor.analizar(l, c)

# 1) Casos de punta a punta
for k in CASOS:
    e = BASES[k][1]; o = correr(k)
    json.dump({x: o[x] for x in ("orden", "estado", "escalamiento_maximo", "canal", "llamadas", "hallazgos_informe", "vista_medica", "recordatorios", "edad_biologica", "calculados")},
              open(f"{B}/salida_final_{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    re_ = e["relaciones_esperadas"]
    for rid in re_["activas"]: chk(o["relaciones"][rid]["estado"] == "activa", f"{k} {rid} debía estar activa: {o['relaciones'][rid]['estado']}")
    for rid in re_["vigilar"]: chk(o["relaciones"][rid]["estado"] == "vigilar", f"{k} {rid} debía ser vigilar: {o['relaciones'][rid]['estado']}")
    for rid in re_["incompletas"]: chk(o["relaciones"][rid]["estado"] == "incompleta", f"{k} {rid} debía ser incompleta")
    for rid in re_["no_activas"]: chk(o["relaciones"][rid]["estado"] == "no_activa", f"{k} {rid} debía no activarse: {o['relaciones'][rid]['estado']}")
    chk(o["escalamiento_maximo"] == e["escalamiento_maximo"], f"{k} escalamiento máximo {o['escalamiento_maximo']}")
    chk(all(s["escalamiento"] == e["seguridad"]["escalamiento"] for s in o["seguridad"].values()), f"{k} seguridad con escalamiento distinto de 0")
    chk(sorted(o["vista_medica"]["revision_medica_obligatoria"]) == sorted(e["seguridad"]["revision_medica_obligatoria"]), f"{k} revisión obligatoria {o['vista_medica']['revision_medica_obligatoria']}")
    ids = [m for g in o["hallazgos_informe"] for m in ([g["id"]] if g["tipo"] == "condicion" else g.get("miembros", []))]
    chk(len(ids) == len(set(ids)), f"{k} condiciones repetidas en el informe")
    chk(o["recordatorios"] == e["recordatorios"], f"{k} recordatorios {o['recordatorios']}")
    chk("COND-M6-MI-A02" not in ids and o["edad_biologica"]["phenoage"] == e["calculados_esperados"]["phenoage"], f"{k} edad biológica fuera de la lista y en su pantalla")
o1 = json.load(open(f"{B}/salida_final_E2E-01.json", encoding="utf-8")); o2 = json.load(open(f"{B}/salida_final_E2E-02.json", encoding="utf-8"))
chk(o1["hallazgos_informe"][0]["id"] == "COND-M4-GA-005", "hombre: el primer hallazgo debía ser H. pylori (escalamiento 2)")
chk(o2["hallazgos_informe"][0]["id"] == "REL-013", "mujer: el primer hallazgo debía ser el patrón de déficit de hierro")

H1, M = "E2E-01", "E2E-02"
# 2) Relaciones unitarias: (nombre, base, valores, contexto, relación, estado esperado)
RU = [
 ("REL-004 inflamación", H1, dict(hs_crp=4.0, fibrinogen=520, homocysteine=18), {}, "REL-004", "vigilar"),
 ("REL-007 sistémica", H1, dict(hs_crp=14, esr=35), {}, "REL-007", "vigilar"),
 ("REL-008 muscular", H1, dict(ck_cpk=2400, ast=85, ldh=260), {}, "REL-008", "activa"),
 ("REL-009 hemólisis", M, dict(hemoglobin=11.9, reticulocytes_pct=4.2, bilirubin_total=2.3, bilirubin_direct=0.3, ldh=410), dict(tabaquismo=False), "REL-009", "activa"),
 ("REL-010 renal", H1, dict(creatinine=2.0, egfr=38, uacr=80), {}, "REL-010", "activa"),
 ("REL-012 PTH con TFG baja", H1, dict(creatinine=2.0, egfr=38, pth={"valor": 140.0, "_nuevo": True, "unidad": "pg/mL", "intervalo": {"bajo": 15, "alto": 65, "texto": "15 – 65"}}), {}, "REL-012", "activa"),
 ("REL-014 inflamatoria", M, dict(ferritin=180, transferrin_saturation=14, hs_crp=22), {}, "REL-014", "activa"),
 ("REL-015 B12", H1, dict(vitamin_b12=150, homocysteine=21), {}, "REL-015", "activa"),
 ("REL-020 vitamina D y PTH", H1, dict(vitamin_d=12, calcium=10.9, albumin=4.2, pth={"valor": 90.0, "_nuevo": True, "unidad": "pg/mL", "intervalo": {"bajo": 15, "alto": 65, "texto": "15 – 65"}}), {}, "REL-020", "activa"),
 ("REL-023 cortisol", H1, dict(cortisol=24.0), dict(presion_sistolica=140, presion_diastolica=90), "REL-023", "vigilar"),
 ("REL-026 con reloj", M, {}, dict(wearable={"activo": True, "fc_reposo_alta": True}), "REL-026", "vigilar"),
 ("REL-027 prolactina y TSH", M, dict(prolactin=41, macroprolactin={"valor": 75.0, "_nuevo": True, "unidad": "%", "intervalo": {"bajo": 40, "alto": None, "texto": "> 40 %"}}), {}, "REL-027", "activa"),
 ("REL-005 troponina", H1, dict(hs_troponin={"valor": 31.0, "estado": "medido", "operador": "="}), {}, "REL-005", "derivada_a_seguridad"),
]
for nombre, base, vals, ctx, rid, est in RU:
    o = correr(base, vals, ctx)["relaciones"][rid]
    chk(o["estado"] == est, f"[{nombre}] {rid}: esperado {est}, obtenido {o['estado']} ({o.get('senales')})")
# 3) Seguridad unitaria: (nombre, base, valores, contexto, ficha, escalamiento esperado)
SU = [
 ("SEG-001 troponina", H1, dict(hs_troponin={"valor": 31.0, "estado": "medido", "operador": "="}), {}, "SEG-001", 3),
 ("SEG-002 cortisol bajo", H1, dict(cortisol=4.1), {}, "SEG-002", 2),
 ("SEG-002 fuera de horario", H1, dict(cortisol=9.0), dict(hora_toma="11:20"), "SEG-002", 0),
 ("SEG-004 brecha", H1, dict(osmolality=312), {}, "SEG-004", 2),
 ("SEG-005 eritroblastos", H1, dict(nrbc=1.5), {}, "SEG-005", 2),
 ("SEG-005 esplenectomía", H1, dict(nrbc=0.8), dict(esplenectomia=True), "SEG-005", 1),
 ("SEG-006 INR alto", H1, dict(inr=1.6), {}, "SEG-006", 2),
 ("SEG-006 coagulopatía", H1, dict(fibrinogen=120, pt=19, platelets=60), {}, "SEG-006", 3),
 ("SEG-006 warfarina", H1, dict(inr=2.6), dict(medicamentos=["Warfarina"]), "SEG-006", 0),
 ("SEG-007 CK tras ejercicio", H1, dict(ck_cpk=1600), dict(ejercicio_intenso_48h=True), "SEG-007", 1),
 ("SEG-007 CK sin ejercicio", H1, dict(ck_cpk=2000), {}, "SEG-007", 2),
 ("SEG-007 CK con orina oscura", H1, dict(ck_cpk=9000), dict(orina_oscura=True), "SEG-007", 3),
 ("SEG-008 magnesio con potasio bajo", H1, dict(magnesium=1.4, potassium=3.1), {}, "SEG-008", 2),
 ("SEG-009 relación A/G invertida", H1, dict(ag_ratio=0.86), {}, "SEG-009", 1),
 ("SEG-009 IgG muy alta", H1, dict(igg=3600), {}, "SEG-009", 2),
 ("SEG-010 NT-proBNP sin diabetes", H1, dict(nt_probnp={"valor": 520.0, "_nuevo": True, "unidad": "pg/mL"}), {}, "SEG-010", 2),
 ("SEG-011 DHEA-S muy alta", M, dict(dhea_s=820), {}, "SEG-011", 2),
 ("SEG-012 basófilos", H1, dict(basophils_pct=3.5), {}, "SEG-012", 1),
 ("SEG-012 explicado por anemia", M, {}, {}, "SEG-012", 0),
]
for nombre, base, vals, ctx, sid, esc in SU:
    o = correr(base, vals, ctx)["seguridad"][sid]
    chk(o["escalamiento"] == esc, f"[{nombre}] {sid}: esperado {esc}, obtenido {o['escalamiento']} ({o['detalle']})")
# 4) Salida final con urgencia
o = correr(H1, dict(hs_troponin={"valor": 31.0, "estado": "medido", "operador": "="}))
chk(o["escalamiento_maximo"] == 3 and o["hallazgos_informe"][0]["id"] == "SEG-001" and o["canal"].startswith("llamada"), f"urgencia: {o['escalamiento_maximo']} {o['canal']} {o['hallazgos_informe'][0]['id']}")
o = correr(H1, dict(hbsag={"valor": "reactivo", "estado": "cualitativo"}))
chk("COND-M4-IN-002" in o["llamadas"] and o["canal"].startswith("llamada"), f"serología reactiva debe ir por llamada: {o['llamadas']}")
print(f"Relaciones unitarias: {len(RU)} · Seguridad unitaria: {len(SU)}")
print(f"Pasan {pasan} de {pasan + len(fallos)} comprobaciones")
for f in fallos: print("  FALLA:", f)
