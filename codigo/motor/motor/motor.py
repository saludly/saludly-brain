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

def normalizar_contexto(contexto):
    """La pregunta "¿tomas biotina?" (MVP, 10 de octubre de 2026) cuenta como suplemento de biotina declarado."""
    ctx = dict(contexto)
    if ctx.get("toma_biotina") and not any("biotina" in str(s).lower() for s in ctx.get("suplementos", [])):
        ctx["suplementos"] = list(ctx.get("suplementos", [])) + ["biotina"]
    return ctx

def analizar_parte1(lectura, contexto):
    if lectura.get("estado") != "aceptado":
        return dict(estado="no_procesado", motivo=lectura.get("motivo"))
    ctx = normalizar_contexto(contexto)
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
    """Flujo completo: cálculos y clasificación, condiciones M1 a M6, relaciones, seguridad y ensamble.
    El panel sale del contexto ("solo_sangre" o "completo"); sin dato, se usa reglas_parte1.yaml > panel > modo_por_defecto."""
    import condiciones_m1m2 as C12, condiciones_m3m6 as C36, relaciones_seguridad as RS
    contexto = normalizar_contexto(contexto)
    panel = contexto.get("panel") or REGLAS["panel"]["modo_por_defecto"]
    pausa = REGLAS["panel"].get(panel) if panel != "completo" else None
    if pausa:
        # Orina y heces en pausa: si llegan en el PDF no se usan (quedan anotadas como duda)
        pausados, fuera_panel = set(pausa["biomarcadores_pausados"]), set(pausa.get("biomarcadores_fuera_del_panel", []))
        ids = {r.get("biomarker_id") for r in lectura.get("resultados", [])}
        quitados, sobrantes = sorted(ids & pausados), sorted(ids & fuera_panel)
        dudas = list(lectura.get("dudas", []))
        if quitados: dudas.append(f"Resultados no usados (panel {panel}): {', '.join(quitados)}")
        if sobrantes: dudas.append(f"Resultados fuera del panel del MVP, no se interpretan: {', '.join(sobrantes)}")
        lectura = dict(lectura, resultados=[r for r in lectura.get("resultados", []) if r.get("biomarker_id") not in pausados | fuera_panel], dudas=dudas)
    p1 = analizar_parte1(lectura, contexto)
    if p1.get("estado") != "parte1_completa":
        return p1
    m12 = C12.evaluar_m1m2(p1, contexto)
    m36 = C36.evaluar_m3m6(p1, contexto, m12)
    cond = {**m12, **m36}
    d = C12.Datos(p1, dict(contexto, _observaciones=p1.get("observaciones", [])))
    if pausa:
        for k in pausa["condiciones_pausadas"]:
            cond[k].update(estado="pausada_mvp", coincidencia=None, escalamiento=None, nota=f"no se evalúa: panel {panel}")
    rels = RS.evaluar_relaciones(d, cond)
    segs = RS.evaluar_seguridad(d, cond)
    if pausa:
        for k in pausa["relaciones_pausadas"]:
            rels[k].update(estado="pausada_mvp", miembros=[], nota=f"no se evalúa: panel {panel}")
        for k in pausa["seguridad_pausada"]:
            segs[k].update(estado="pausada_mvp", escalamiento=0, detalle=[f"no se evalúa: panel {panel}"])
    salida = RS.ensamblar(cond, rels, segs, p1, contexto)
    salida["panel"] = panel
    if contexto.get("toma_biotina") is None and not any("biotina" in str(x).lower() for x in contexto.get("suplementos", [])):
        salida["vista_medica"]["datos_faltantes"] = sorted(set(salida["vista_medica"]["datos_faltantes"]) | {"pregunta de biotina sin responder (tiroides, B12 y folato sin ese control)"})
    if pausa:
        salida["vista_medica"]["pausadas_mvp"] = pausa["condiciones_pausadas"] + pausa["relaciones_pausadas"] + pausa["seguridad_pausada"]
        salida["vista_medica"]["evaluadas_parcialmente"] = [dict(id=k, nota=n) for k, n in pausa["parciales"].items()]
    salida.update(condiciones=cond, relaciones=rels, seguridad=segs, resultados=p1["resultados"], observaciones=p1.get("observaciones", []))
    return salida
