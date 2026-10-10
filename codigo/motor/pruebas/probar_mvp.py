"""Pruebas del MVP solo sangre: orina y heces en pausa (decisión de Carlos, 10 de octubre de 2026)."""
import json, os, sys, copy
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(B), "motor"))
import lector, motor
IDX = json.load(open(f"{B}/00_INDEX.json", encoding="utf-8"))
LAB = {"transporte_vitamina_c_validado": True}
CASOS = {"E2E-01": ("Ejemplo_resultados_LCD-2026-100123_hombre.pdf", {"documento": "CC 0000000001", "orden": "LCD-2026-100123"}),
         "E2E-02": ("Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-100124"})}
P = motor.REGLAS["panel"]["solo_sangre"]
PAUSADOS = set(P["biomarcadores_pausados"])
fallos, pasan = [], 0
def chk(ok, msg):
    global pasan
    if ok: pasan += 1
    else: fallos.append(msg)

def correr(lect, ctx):
    return motor.analizar(copy.deepcopy(lect), ctx)

chk(motor.REGLAS["panel"]["modo_por_defecto"] == "solo_sangre", "el modo por defecto debía ser solo_sangre")
for k, (pdf, vis) in CASOS.items():
    lect = lector.leer(f"{B}/{pdf}", vis, IDX)
    e = json.load(open(f"{B}/{k}.json", encoding="utf-8"))
    ctx = dict(e["contexto"], laboratorio=LAB)
    mvp = correr(lect, ctx)                                # sin "panel": usa el modo por defecto
    full = correr(lect, dict(ctx, panel="completo"))
    solo_sangre = dict(lect, resultados=[r for r in lect["resultados"] if r.get("biomarker_id") not in PAUSADOS])
    pdf_sangre = correr(solo_sangre, ctx)                  # un PDF que ya no trae orina ni heces

    chk(mvp["panel"] == "solo_sangre" and full["panel"] == "completo", f"{k} panel reportado")
    for c in P["condiciones_pausadas"]:
        chk(mvp["condiciones"][c]["estado"] == "pausada_mvp", f"{k} {c} debía quedar pausada: {mvp['condiciones'][c]['estado']}")
    for r in P["relaciones_pausadas"]:
        chk(mvp["relaciones"][r]["estado"] == "pausada_mvp", f"{k} {r} debía quedar pausada")
    for s in P["seguridad_pausada"]:
        chk(mvp["seguridad"][s]["estado"] == "pausada_mvp" and mvp["seguridad"][s]["escalamiento"] == 0, f"{k} {s} debía quedar pausada")
    ids = {m for g in mvp["hallazgos_informe"] for m in ([g["id"]] + g.get("miembros", []))}
    chk(not ids & (set(P["condiciones_pausadas"]) | set(P["relaciones_pausadas"]) | set(P["seguridad_pausada"])), f"{k} hallazgo pausado en el informe: {ids}")
    chk(any("Resultados no usados" in x for x in mvp["vista_medica"]["dudas_lectura"]), f"{k} debía anotar los resultados de orina y heces no usados")
    chk(sorted(mvp["vista_medica"]["pausadas_mvp"]) == sorted(P["condiciones_pausadas"] + P["relaciones_pausadas"] + P["seguridad_pausada"]), f"{k} lista de pausadas en la vista médica")
    chk([x["id"] for x in mvp["vista_medica"]["evaluadas_parcialmente"]] == list(P["parciales"]), f"{k} lista de parciales en la vista médica")
    # Lo que no depende de orina ni heces sale igual que en el panel completo
    distintas = [c for c in full["condiciones"] if c not in P["condiciones_pausadas"] and c not in P["parciales"]
                 and (full["condiciones"][c]["estado"], full["condiciones"][c].get("escalamiento")) != (mvp["condiciones"][c]["estado"], mvp["condiciones"][c].get("escalamiento"))]
    chk(not distintas, f"{k} condiciones de sangre que cambiaron al pausar: {distintas}")
    distintas = [r for r in full["relaciones"] if r not in P["relaciones_pausadas"] and full["relaciones"][r]["estado"] != mvp["relaciones"][r]["estado"]]
    chk(not distintas, f"{k} relaciones de sangre que cambiaron al pausar: {distintas}")
    # Da lo mismo que el PDF traiga orina y heces o no
    chk([g["id"] for g in pdf_sangre["hallazgos_informe"]] == [g["id"] for g in mvp["hallazgos_informe"]], f"{k} un PDF solo de sangre debía dar el mismo informe")
    chk({c: v["estado"] for c, v in pdf_sangre["condiciones"].items()} == {c: v["estado"] for c, v in mvp["condiciones"].items()}, f"{k} un PDF solo de sangre debía dar los mismos estados")

    if k == "E2E-01":
        chk(full["hallazgos_informe"][0]["id"] == "COND-M4-GA-005", "hombre, panel completo: el primero sigue siendo H. pylori")
        chk(mvp["escalamiento_maximo"] == 1, f"hombre, solo sangre: sin H. pylori el escalamiento máximo baja a 1 ({mvp['escalamiento_maximo']})")
        chk(mvp["condiciones"]["COND-M2-NE-001"]["estado"] == full["condiciones"]["COND-M2-NE-001"]["estado"], "hombre: la ERC por TFG se sigue evaluando")
    else:
        chk(mvp["hallazgos_informe"][0]["id"] == "REL-013" and mvp["escalamiento_maximo"] == 2, "mujer, solo sangre: el déficit de hierro sigue primero con escalamiento 2")

for f in fallos: print("FALLA:", f)
print(f"Pasan {pasan} de {pasan + len(fallos)}")
