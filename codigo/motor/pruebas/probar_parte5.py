"""Pruebas de la parte 5: ampliación solo con sangre aprobada por Carlos el 10 de octubre de 2026.
10 condiciones nuevas, 4 relaciones nuevas, 4 índices calculados, la refleja de haptoglobina y la pregunta de biotina.
Cada condición tiene al menos un caso positivo y uno negativo (criterio de la primera puerta del plan)."""
import json, math, os, sys, copy
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

def nuevo(valor, alto=None, bajo=None, unidad=None, estado="medido"):
    txt = f"{bajo} a {alto}" if (alto is not None and bajo is not None) else (f"< {alto}" if alto is not None else (f"> {bajo}" if bajo is not None else None))
    return {"valor": valor, "estado": estado, "_nuevo": True, "unidad": unidad, "intervalo": {"bajo": bajo, "alto": alto, "texto": txt} if txt else None}

def correr(k, valores=None, ctx=None):
    lect, e = BASES[k]; l = copy.deepcopy(lect)
    presentes = set()
    for r in l["resultados"]:
        b = r.get("biomarker_id")
        if b in (valores or {}) and not r.get("campo"):
            presentes.add(b); nv = valores[b]
            if isinstance(nv, dict): r.update({x: y for x, y in nv.items() if not x.startswith("_") and x != "intervalo"})
            else: r.update(valor=float(nv), estado="medido", operador="=", valor_original=str(nv))
    for b, v in (valores or {}).items():
        if isinstance(v, dict) and v.get("_nuevo") and b not in presentes:
            l["resultados"].append(dict(biomarker_id=b, campo=None, nombre_original=b, valor=v["valor"], estado=v.get("estado", "medido"), operador="=",
                                        unidad=v.get("unidad"), intervalo_lab=v.get("intervalo"), metodo=None, muestra="Suero", dudas=[]))
    c = dict(e["contexto"], laboratorio=LAB); c.update(ctx or {})
    return motor.analizar(l, c)

H1, M = "E2E-01", "E2E-02"
NO = ("no_activa", "no_aplica")
# (nombre, base, valores, contexto, ficha, comprobaciones)
U = [
 # COND-M3-HE-007 eritrocitosis
 ("HE-007 positivo", H1, dict(hemoglobin=19.0, hematocrit=54), dict(tabaquismo=False), "COND-M3-HE-007", dict(estado="activa", coincidencia="alta", escalamiento=1)),
 ("HE-007 muy alta", H1, dict(hemoglobin=20.6, hematocrit=58), dict(tabaquismo=False), "COND-M3-HE-007", dict(estado="activa", escalamiento=2)),
 ("HE-007 fumador", H1, dict(hemoglobin=18.6, hematocrit=50), dict(tabaquismo=True), "COND-M3-HE-007", dict(estado="activa", coincidencia="moderada")),
 ("HE-007 normal en Bogotá", H1, dict(hemoglobin=17.9), dict(tabaquismo=False), "COND-M3-HE-007", dict(estado=NO)),
 ("HE-007 embarazo", M, dict(hemoglobin=18.5), dict(embarazo=True), "COND-M3-HE-007", dict(estado="no_aplica")),
 # COND-M3-HE-008 trombocitosis
 ("HE-008 reactiva", M, dict(platelets=520), {}, "COND-M3-HE-008", dict(estado="activa", coincidencia="moderada", escalamiento=1)),
 ("HE-008 sin causa", H1, dict(platelets=610, ferritin=120, hs_crp=1.0), {}, "COND-M3-HE-008", dict(estado="activa", coincidencia="alta", escalamiento=1)),
 ("HE-008 extrema", H1, dict(platelets=1150), {}, "COND-M3-HE-008", dict(estado="activa", escalamiento=2)),
 ("HE-008 negativo", H1, {}, {}, "COND-M3-HE-008", dict(estado=NO)),
 # COND-M3-HE-A04 rasgo talasémico
 ("HE-A04 sin electroforesis", M, dict(mcv=68, erythrocytes=6.1, ferritin=80, transferrin_saturation=30), {}, "COND-M3-HE-A04", dict(estado="pendiente_refleja")),
 ("HE-A04 confirmado", M, dict(mcv=68, erythrocytes=6.1, ferritin=80, transferrin_saturation=30, hb_electrophoresis=nuevo(5.1, unidad="%")), {}, "COND-M3-HE-A04", dict(estado="apoyo", coincidencia="alta")),
 ("HE-A04 déficit de hierro", M, dict(mcv=72, erythrocytes=4.1, ferritin=7), {}, "COND-M3-HE-A04", dict(estado=NO)),
 ("HE-A04 Mentzer alto", M, dict(mcv=74, erythrocytes=4.0, ferritin=80), {}, "COND-M3-HE-A04", dict(estado=NO)),
 # COND-M3-HE-009 macrocitosis sin anemia
 ("HE-009 con alcohol", H1, dict(mcv=104, ggt=140), {}, "COND-M3-HE-009", dict(estado="activa", coincidencia="alta", escalamiento=1)),
 ("HE-009 sin explicación", H1, dict(mcv=103, ggt=25, alt=20, ast=20), {}, "COND-M3-HE-009", dict(estado="activa", coincidencia="moderada")),
 ("HE-009 con anemia", H1, dict(mcv=108, hemoglobin=10.5), dict(tabaquismo=False), "COND-M3-HE-009", dict(estado="no_aplica")),
 ("HE-009 negativo", H1, {}, {}, "COND-M3-HE-009", dict(estado=NO)),
 # COND-M3-HE-010 dos o más líneas bajas
 ("HE-010 dos líneas", M, dict(platelets=120), dict(tabaquismo=False), "COND-M3-HE-010", dict(estado="activa", escalamiento=2)),
 ("HE-010 tres líneas", M, dict(platelets=90, neutrophils_abs=1.1), dict(tabaquismo=False), "COND-M3-HE-010", dict(estado="activa", escalamiento=3)),
 ("HE-010 solo anemia", M, {}, dict(tabaquismo=False), "COND-M3-HE-010", dict(estado=NO)),
 # COND-M6-MI-002 gammapatía
 ("MI-002 con anemia", H1, dict(total_protein=9.0, albumin=4.0, globulin=5.0, ag_ratio=0.8, hemoglobin=10.5), dict(tabaquismo=False), "COND-M6-MI-002", dict(estado="activa", coincidencia="moderada", escalamiento=2)),
 ("MI-002 solo proteínas", H1, dict(total_protein=8.3, albumin=4.2, globulin=4.1, ag_ratio=1.02), {}, "COND-M6-MI-002", dict(estado="pendiente_refleja")),
 ("MI-002 banda monoclonal", H1, dict(total_protein=8.3, albumin=4.2, globulin=4.1, ag_ratio=1.02, serum_protein_electrophoresis=nuevo("Banda monoclonal en región gamma", estado="cualitativo")), {}, "COND-M6-MI-002", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("MI-002 policlonal", H1, dict(total_protein=8.3, albumin=4.2, globulin=4.1, ag_ratio=1.02, serum_protein_electrophoresis=nuevo("Aumento policlonal de gammaglobulinas", estado="cualitativo")), {}, "COND-M6-MI-002", dict(estado=NO)),
 ("MI-002 negativo", H1, {}, {}, "COND-M6-MI-002", dict(estado=NO)),
 # COND-M2-TI-009 cortisol bajo
 ("TI-009 con ACTH alta", H1, dict(cortisol=3.2, acth=180), {}, "COND-M2-TI-009", dict(estado="activa", coincidencia="alta", escalamiento=2)),
 ("TI-009 sola", H1, dict(cortisol=4.1), {}, "COND-M2-TI-009", dict(estado="activa", coincidencia="moderada")),
 ("TI-009 con prednisolona", H1, dict(cortisol=2.0), dict(medicamentos=["prednisolona 5 mg"]), "COND-M2-TI-009", dict(estado="no_interpretable")),
 ("TI-009 fuera de horario", H1, dict(cortisol=3.0), dict(hora_toma="11:20"), "COND-M2-TI-009", dict(estado="no_interpretable")),
 ("TI-009 negativo", H1, {}, {}, "COND-M2-TI-009", dict(estado=NO)),
 # COND-M1-EM-A03 diabetes con posible falta de insulina
 ("EM-A03 positivo", H1, dict(hba1c=8.1, glucose=160, c_peptide=0.3), {}, "COND-M1-EM-A03", dict(estado="apoyo")),
 ("EM-A03 péptido C normal", H1, dict(hba1c=7.2, glucose=148, c_peptide=2.1), {}, "COND-M1-EM-A03", dict(estado=NO)),
 ("EM-A03 sin diabetes", H1, dict(c_peptide=0.4), {}, "COND-M1-EM-A03", dict(estado="no_aplica")),
 # COND-M1-EM-A04 TyG y TG/HDL
 ("EM-A04 hombre del ejemplo", H1, {}, {}, "COND-M1-EM-A04", dict(estado="apoyo")),
 ("EM-A04 negativo", H1, dict(triglycerides=90, glucose=85, hdl_c=60, hba1c=5.2), {}, "COND-M1-EM-A04", dict(estado=NO)),
 ("EM-A04 en diabetes", H1, dict(hba1c=7.5, glucose=150), {}, "COND-M1-EM-A04", dict(estado="no_aplica")),
 ("EM-A04 sin ayuno", H1, {}, dict(ayuno_horas=4), "COND-M1-EM-A04", dict(estado="incompleta")),
 # COND-M5-MU-004 transición a la menopausia
 ("MU-004 con estradiol bajo", M, dict(fsh=68, estradiol=18), dict(edad=51), "COND-M5-MU-004", dict(estado="apoyo", coincidencia="alta")),
 ("MU-004 solo FSH", M, dict(fsh=31, estradiol=95), dict(edad=47), "COND-M5-MU-004", dict(estado="apoyo", coincidencia="moderada")),
 ("MU-004 con anticonceptivo", M, dict(fsh=40), dict(edad=46, anticonceptivo_hormonal=True), "COND-M5-MU-004", dict(estado="no_aplica")),
 ("MU-004 joven", M, {}, {}, "COND-M5-MU-004", dict(estado="no_aplica")),
 ("MU-004 hombre", H1, {}, {}, "COND-M5-MU-004", dict(estado="no_aplica")),
]
for nombre, base, vals, ctx, fid, esp in U:
    o = correr(base, vals, ctx)["condiciones"][fid]
    for campo, valor in esp.items():
        ok = o.get(campo) in valor if isinstance(valor, tuple) else o.get(campo) == valor
        chk(ok, f"[{nombre}] {fid} {campo}: esperado {valor}, obtenido {o.get(campo)} ({o.get('nota')})")

# Relaciones nuevas y REL-009 con haptoglobina: (nombre, base, valores, contexto, relación, estado)
RU = [
 ("REL-028 SOP metabólico", M, dict(testosterone_total=120, insulin=25, glucose=95), dict(tabaquismo=False), "REL-028", "activa"),
 ("REL-028 sin metabolismo", M, dict(testosterone_total=120, insulin=5, glucose=80, triglycerides=70, ldl_c=100, total_cholesterol=170, hdl_c=60), {}, "REL-028", "no_activa"),
 ("REL-029 testosterona alta", H1, dict(hemoglobin=19.0, hematocrit=54, testosterone_total=1150), dict(tabaquismo=False), "REL-029", "activa"),
 ("REL-029 testosterona declarada", H1, dict(hemoglobin=19.0, hematocrit=54), dict(tabaquismo=False, suplementos=["testosterona en gel"]), "REL-029", "activa"),
 ("REL-029 sin eritrocitosis", H1, dict(testosterone_total=1150), {}, "REL-029", "no_activa"),
 ("REL-030 NLR con PCR", H1, dict(neutrophils_abs=6.0, lymphocytes_abs=1.5, hs_crp=4.0), {}, "REL-030", "vigilar"),
 ("REL-030 con infección", H1, dict(neutrophils_abs=6.0, lymphocytes_abs=1.5, hs_crp=4.0), dict(infeccion_reciente=True), "REL-030", "no_activa"),
 ("REL-030 negativo", H1, {}, {}, "REL-030", "no_activa"),
 ("REL-031 FR alto", H1, dict(rheumatoid_factor=nuevo(48.0, alto=14, unidad="UI/mL")), {}, "REL-031", "vigilar"),
 ("REL-031 FR normal", H1, dict(rheumatoid_factor=nuevo(8.0, alto=14, unidad="UI/mL")), {}, "REL-031", "no_activa"),
 ("REL-031 sin FR", H1, {}, {}, "REL-031", "no_activa"),
 ("REL-009 con haptoglobina", M, dict(hemoglobin=11.9, reticulocytes_pct=4.2, haptoglobin=nuevo(10.0, alto=200, bajo=30, unidad="mg/dL")), dict(tabaquismo=False), "REL-009", "activa"),
]
for nombre, base, vals, ctx, rid, esp in RU:
    o = correr(base, vals, ctx)["relaciones"][rid]
    chk(o["estado"] == esp, f"[{nombre}] {rid}: esperado {esp}, obtenido {o['estado']} ({o.get('nota')})")

# Detalles que no caben en la tabla
o = correr(H1, dict(rheumatoid_factor=nuevo(48.0, alto=14), anti_ccp=nuevo(85.0, alto=17)))
chk("anti_ccp" in o["relaciones"]["REL-031"]["senales"], "REL-031: el anti-CCP positivo debía reforzar la señal")
o = correr(H1, dict(hemoglobin=19.0, hematocrit=54, testosterone_total=1150), dict(tabaquismo=False))
g = [x for x in o["hallazgos_informe"] if x["id"] == "COND-M3-HE-007"]
chk(g and any(p["id"] == "REL-029" for p in g[0].get("patrones", [])), "REL-029 debía salir como contexto de la eritrocitosis en el informe")
o = correr(M, dict(testosterone_total=120, insulin=25, glucose=95), dict(tabaquismo=False))
chk(o["condiciones"]["COND-M5-MU-001"].get("pendiente_refleja") == ["hydroxyprogesterone_17"], "MU-001 activa debía pedir la 17-OHP como refleja")
o = correr(M, dict(testosterone_total=120, insulin=25, glucose=95, hydroxyprogesterone_17=nuevo(3.5, alto=2.0, unidad="ng/mL")), dict(tabaquismo=False))
chk(o["condiciones"]["COND-M5-MU-001"]["coincidencia"] == "baja", "MU-001 con 17-OHP alta debía bajar la coincidencia")
o = correr(M, dict(fsh=68, estradiol=18), dict(edad=51))
chk([x["id"] for x in o["informativos_paciente"]] == ["COND-M5-MU-004"], f"la transición a la menopausia debía llegar al paciente como informativa: {o['informativos_paciente']}")
o = correr(M, dict(mcv=68, erythrocytes=6.1, ferritin=80, transferrin_saturation=30))
chk(any(x["id"] == "COND-M3-HE-A04" for x in o["vista_medica"]["pendientes_refleja"]), "el rasgo talasémico pendiente debía ir a la vista médica")
chk(o["condiciones"]["COND-M3-HE-A04"].get("quita_recomendacion_hierro") is True, "el rasgo talasémico debía quitar las recomendaciones de hierro")
# La gammapatía pendiente no calla la alerta de SEG-009; la activa sí
o = correr(H1, dict(total_protein=8.3, albumin=4.2, globulin=4.1, ag_ratio=0.86))
chk(o["condiciones"]["COND-M6-MI-002"]["estado"] == "pendiente_refleja" and o["seguridad"]["SEG-009"]["escalamiento"] == 1, "SEG-009 debía seguir avisando mientras la gammapatía espera la electroforesis")
o = correr(H1, dict(total_protein=9.0, albumin=4.0, globulin=5.0, ag_ratio=0.8, hemoglobin=10.5), dict(tabaquismo=False))
chk(o["condiciones"]["COND-M6-MI-002"]["estado"] == "activa" and o["seguridad"]["SEG-009"]["escalamiento"] == 0, "con la gammapatía activa, SEG-009 no repite la alerta")

# Índices calculados
o = correr(H1)
c, e = o["calculados"], BASES[H1][0]
v = {r["biomarker_id"]: r["valor"] for r in e["resultados"] if r.get("biomarker_id") and not r.get("campo") and isinstance(r.get("valor"), (int, float))}
chk(c["tyg_index"] == round(math.log(v["triglycerides"] * v["glucose"] / 2), 2), f"TyG {c['tyg_index']}")
chk(c["tg_hdl_ratio"] == round(v["triglycerides"] / v["hdl_c"], 2), f"TG/HDL {c['tg_hdl_ratio']}")
chk(c["nlr"] == round(v["neutrophils_abs"] / v["lymphocytes_abs"], 2), f"NLR {c['nlr']}")
chk(c["mentzer_index"] is None, "Mentzer no se calcula con VCM normal")
chk(correr(M)["calculados"]["mentzer_index"] is not None, "Mentzer se calcula con VCM bajo")

# Pregunta de biotina (MVP)
o = correr(M, ctx=dict(toma_biotina=True))
chk(o["condiciones"]["COND-M2-TI-001"]["estado"] not in ("activa",), f"con biotina, el hipotiroidismo subclínico no debía activarse: {o['condiciones']['COND-M2-TI-001']['estado']}")
chk(not any("biotina" in x for x in o["vista_medica"]["datos_faltantes"]), "con la pregunta respondida no debía faltar el dato")
o = correr(M, ctx=dict(toma_biotina=False))
chk(o["condiciones"]["COND-M2-TI-001"]["estado"] == "activa", "sin biotina, el hipotiroidismo subclínico de la mujer sigue activo")
o = correr(M)
chk(any("biotina" in x for x in o["vista_medica"]["datos_faltantes"]), "sin responder la pregunta de biotina debía quedar como dato faltante")

# El índice del Knowledge Base reconoce las pruebas nuevas (lo usa el lector)
for b, sin in (("rheumatoid_factor", "Factor reumatoide"), ("abo_rh", "Hemoclasificación"), ("hb_electrophoresis", "Electroforesis de hemoglobina"),
               ("serum_protein_electrophoresis", "Proteinograma"), ("hydroxyprogesterone_17", "17-OH progesterona"), ("haptoglobin", "Haptoglobina"), ("anti_ccp", "Anti-CCP")):
    chk(sin in IDX["biomarcadores"].get(b, {}).get("sinonimos", []), f"índice: falta el sinónimo '{sin}' de {b}")
for b in ("vitamin_a", "vitamin_e", "vitamin_k1", "vitamin_c", "vitamin_b1", "biotin", "niacin", "coq10", "omega3_index", "omega6_omega3_ratio"):
    chk(IDX["biomarcadores"][b]["panel"] == "fuera del panel base", f"{b} debía quedar fuera del panel base")
chk(IDX["biomarcadores"]["vitamin_b6"]["panel"] == "opcional", "la B6 debía quedar opcional")

for f in fallos: print("FALLA:", f)
print(f"Casos de condición: {len(U)} · relaciones: {len(RU)}")
print(f"Pasan {pasan} de {pasan + len(fallos)} comprobaciones")
