"""Pruebas del lector: compara la lectura de los PDF de ejemplo con la entrada de los casos de punta a punta
y verifica los rechazos por identidad."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lector
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = json.load(open(f"{BASE}/00_INDEX.json", encoding="utf-8"))
CAMPOS = ["nombre_original", "biomarker_id", "campo", "valor_original", "indicador_lab", "unidad", "intervalo", "metodo", "seccion", "muestra", "refleja"]
def cmp(caso, pdf, visita):
    esp = json.load(open(f"{BASE}/pruebas/{caso}.json", encoding="utf-8"))["entrada_resultados"]
    got = lector.leer(f"{BASE}/{pdf}", visita, IDX)["resultados"]
    errores = []; total = 0; ok = 0
    if len(esp) != len(got):
        errores.append(f"cantidad de resultados: esperados {len(esp)}, leídos {len(got)}")
    for e, g in zip(esp, got):
        e2 = dict(e, intervalo=e.get("intervalo_lab")); g2 = dict(g, intervalo=(g.get("intervalo_lab") or {}).get("texto"))
        for c in CAMPOS:
            total += 1
            a, b = e2.get(c), g2.get(c)
            if c == "valor_original": a, b = str(a), str(b)
            if a == b: ok += 1
            else: errores.append(f"{e['nombre_original']} · {c}: esperado {a!r}, leído {b!r}")
        if e.get("estado") == "medido":
            total += 1
            if abs((g.get("valor") or 0) - e["valor"]) < 1e-9: ok += 1
            else: errores.append(f"{e['nombre_original']} · valor numérico: esperado {e['valor']}, leído {g.get('valor')}")
    return total, ok, errores
res = {}
for caso, pdf, vis in [("E2E-01", "Ejemplo_resultados_LCD-2026-100123_hombre.pdf", {"documento": "CC 0000000001", "orden": "LCD-2026-100123"}),
                       ("E2E-02", "Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-100124"})]:
    t, o, err = cmp(caso, pdf, vis); res[caso] = (t, o, err)
    print(f"{caso}: {o}/{t} campos correctos ({100*o/t:.1f} %)"); [print("   ", x) for x in err[:15]]
# identidad
r = lector.leer(f"{BASE}/Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-999999"}, IDX)
print("Orden equivocada:", r["estado"], "·", r["motivo"])
r = lector.leer(f"{BASE}/Ejemplo_resultados_LCD-2026-100124_mujer.pdf", {"documento": "CC 0000000001", "orden": "LCD-2026-100124"}, IDX)
print("Documento equivocado:", r["estado"], "·", r["motivo"])
subprocess.run(["qpdf", "--empty", "--pages", f"{BASE}/Ejemplo_resultados_LCD-2026-100124_mujer.pdf", "1-2",
                f"{BASE}/Ejemplo_resultados_LCD-2026-100123_hombre.pdf", "3", "--", f"{BASE}/pruebas/mezclado.pdf"], check=True)
r = lector.leer(f"{BASE}/pruebas/mezclado.pdf", {"documento": "CC 0000000002", "orden": "LCD-2026-100124"}, IDX)
print("PDF con páginas de dos pacientes:", r["estado"], "·", r["motivo"])
json.dump({k: dict(total=v[0], correctos=v[1], errores=v[2]) for k, v in res.items()}, open(f"{BASE}/pruebas/resultado_pruebas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
