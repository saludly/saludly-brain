"""
Saludly Brain · Motor de análisis · versión 1 · Parte 1: cálculos y clasificación

Entrada: la salida del lector del PDF (contrato 10.3) y el contexto de la visita.
Salida: cada resultado con su clase y el motivo, los valores calculados con su
trazabilidad y las dudas. Las partes 2 a 4 (condiciones, relaciones y seguridad)
se agregan sobre esta salida.
"""
import json, os, yaml
from calculos import calcular_todo
from clasificacion import clasificar

BASE = os.path.dirname(os.path.abspath(__file__))
REGLAS = yaml.safe_load(open(f"{BASE}/reglas_parte1.yaml", encoding="utf-8"))

def analizar_parte1(lectura, contexto):
    if lectura.get("estado") != "aceptado":
        return dict(estado="no_procesado", motivo=lectura.get("motivo"))
    ctx = dict(contexto)
    res = [dict(r) for r in lectura["resultados"]]
    # índice por biomarcador (campo None = analito principal)
    R = {r["biomarker_id"]: r for r in res if r.get("biomarker_id") and not r.get("campo")}
    dudas = list(lectura.get("dudas", []))
    for r in res:
        c = clasificar(r, ctx, REGLAS, R)
        r["clase"], r["motivo_clase"] = c["clase"], c["motivo"]
    hb = R.get("hemoglobin"); ctx["_anemia"] = bool(hb and hb.get("clase") == "bajo")
    calc = calcular_todo(R, ctx, REGLAS)
    for c in calc.values():
        if c.get("nota") and ("por verificar" in c["nota"] or "revisar" in c["nota"]):
            dudas.append(f"{c['id']}: {c['nota']}")
    resumen = {}
    for r in res:
        resumen[r.get("clase") or "solo_valor"] = resumen.get(r.get("clase") or "solo_valor", 0) + 1
    return dict(estado="parte1_completa", orden=lectura["encabezado"].get("N.º de orden"), resultados=res, observaciones=lectura.get("observaciones", []),
                calculados=calc, resumen_clases=resumen, dudas=dudas)

if __name__ == "__main__":
    import sys
    lect = json.load(open(sys.argv[1], encoding="utf-8")); ctx = json.load(open(sys.argv[2], encoding="utf-8"))
    print(json.dumps(analizar_parte1(lect, ctx), ensure_ascii=False, indent=1))


def analizar(lectura, contexto):
    """Flujo completo: cálculos y clasificación, condiciones M1 a M6, relaciones, seguridad y ensamble."""
    import condiciones_m1m2 as C12, condiciones_m3m6 as C36, relaciones_seguridad as RS
    p1 = analizar_parte1(lectura, contexto)
    if p1.get("estado") != "parte1_completa":
        return p1
    m12 = C12.evaluar_m1m2(p1, contexto)
    m36 = C36.evaluar_m3m6(p1, contexto, m12)
    cond = {**m12, **m36}
    d = C12.Datos(p1, dict(contexto, _observaciones=p1.get("observaciones", [])))
    rels = RS.evaluar_relaciones(d, cond)
    segs = RS.evaluar_seguridad(d, cond)
    salida = RS.ensamblar(cond, rels, segs, p1, contexto)
    salida.update(condiciones=cond, relaciones=rels, seguridad=segs)
    return salida
