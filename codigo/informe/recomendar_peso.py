"""
Saludly · Recomendaciones semanales de la línea GLP-1 (Fase 6B).

Para cada paciente con tratamiento (tabla tratamientos_peso) calcula los disparadores de la semana con sus registros,
su cuestionario y su último informe aprobado, elige los textos (knowledge_base/fase5/peso_glp1.yaml y las recomendaciones
ya aprobadas) y deja la semana como "borrador" en semanas_peso. La doctora la revisa y la publica en /doctora.
El código decide; el LLM no participa. Todo pasa por el control de salida.

Uso (en el PC de Saludly; lee SUPABASE_URL y SUPABASE_SERVICE_ROLE_KEY del .env):
  python codigo/informe/recomendar_peso.py               # la semana que empieza el próximo lunes
  python codigo/informe/recomendar_peso.py --semana 2026-11-02 --simular
Criterios: docs/07_linea_glp1/version_funcional.md.
"""
import argparse, glob, os, sys, urllib.parse
from datetime import date, timedelta

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "codigo", "pipeline"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import control_salida
from publicar import Supabase, leer_env

F5 = os.path.join(RAIZ, "knowledge_base", "fase5")
CONF = yaml.safe_load(open(os.path.join(F5, "peso_glp1.yaml"), encoding="utf-8"))
TEXTOS = {t["id"]: t for t in CONF["textos"]}
for f in glob.glob(os.path.join(F5, "recomendaciones", "*.yaml")):
    for r in yaml.safe_load(open(f, encoding="utf-8")) or []:
        if isinstance(r, dict) and r.get("id"):
            TEXTOS[r["id"]] = {"id": r["id"], "tipo": r.get("tipo"), "titulo": r["titulo"], "texto": r["texto_base"], "contraindicada_si": r.get("contraindicada_si") or []}
CONSEJOS = yaml.safe_load(open(os.path.join(F5, "consejos_objetivos.yaml"), encoding="utf-8"))["objetivos"]

ALARMA = {"dolor_abdominal_fuerte", "vomito_persistente", "no_retiene_liquidos"}
DIGESTIVOS = {"nauseas", "acidez", "poco_apetito"}
POR_QUE = {
    "nauseas": "Porque esta semana marcaste malestar después de comer.",
    "estrenimiento": "Porque esta semana marcaste estreñimiento.",
    "rapido": "Porque estás bajando más rápido de lo que recomienda tu doctora.",
    "meseta": "Porque tu peso lleva varias semanas sin cambiar.",
    "sin_registro": "Porque no has registrado tu peso en los últimos días.",
    "embarazo": "Por lo que respondiste en tus preguntas.",
    "base": "Para cuidar tu músculo y tu energía mientras bajas de peso.",
}


def lunes_siguiente(hoy=None):
    hoy = hoy or date.today()
    return hoy + timedelta(days=(7 - hoy.weekday()) % 7 or 7)


def serie(t, regs):
    """Peso al final de cada semana de tratamiento (semana 0 = peso al inicio)."""
    ini = date.fromisoformat(t["fecha_inicio"])
    por = {}
    for r in sorted(regs, key=lambda r: r["fecha"]):
        if r.get("peso") is None: continue
        s = max(1, -(-(date.fromisoformat(r["fecha"]) - ini).days // 7))
        por[s] = float(r["peso"])
    return [(0, float(t["peso_inicio"]))] + sorted(por.items())


def disparadores(t, regs, cuest, limite, meseta, hoy):
    """Lista de disparadores activos, en orden de prioridad. Si hay alarma, solo ["alarma"]."""
    recientes = [r for r in regs if (hoy - date.fromisoformat(r["fecha"])).days <= 7]
    sint = {s for r in recientes for s in (r.get("sintomas") or [])}
    if sint & ALARMA: return ["alarma"]
    if (cuest or {}).get("embarazo") in ("si", "no_se"): return ["embarazo"]
    out = []
    if sint & DIGESTIVOS: out.append("nauseas")
    if "estrenimiento" in sint: out.append("estrenimiento")
    sr = serie(t, regs)
    vel = [((sr[i - 1][1] - p) / sr[i - 1][1]) * 100 / max(1, s - sr[i - 1][0]) for i, (s, p) in enumerate(sr) if i]
    if len(vel) >= 2 and all(v > limite for v in vel[-2:]): out.append("rapido")
    if len(sr) > meseta:
        ult = sr[-(meseta + 1):]
        if ult[-1][0] - ult[0][0] >= meseta and max(p for _, p in ult) - min(p for _, p in ult) < 0.6: out.append("meseta")
    ultimo = max((date.fromisoformat(r["fecha"]) for r in regs if r.get("peso") is not None), default=None)
    if not ultimo or (hoy - ultimo).days >= 10: out.append("sin_registro")
    return out


def item(tid, por_que, fuente):
    x = TEXTOS[tid]
    return {"id": tid, "tipo": x.get("tipo") or "", "titulo": x["titulo"], "texto": x["texto"], "por_que": por_que, "fuente": fuente}


def armar(t, regs, cuest, informe, previas, limite, meseta, semana):
    """Elige hasta 3 recomendaciones para la semana. Devuelve (items, disparadores)."""
    hoy = semana - timedelta(days=1)
    usados = {i["id"] for p in previas for i in (p.get("items") or [])}
    ds = disparadores(t, regs, cuest, limite, meseta, hoy)
    if ds == ["alarma"]: return [], ds   # solo el mensaje de seguridad (sale en la app en el momento)
    maximo = CONF["limites"]["maximo_por_semana"]
    items, ya = [], set()

    def tomar(lista, por_que, fuente, permitir_repetido):
        for tid in lista:
            if tid in ya or tid not in TEXTOS or (tid in usados and not permitir_repetido): continue
            items.append(item(tid, por_que, fuente)); ya.add(tid)
            return True
        return False

    for d in ds:   # un disparador activo puede repetir texto: sigue siendo cierto
        if len(items) < maximo: tomar(CONF["disparadores"][d], POR_QUE[d], "semana", True)
    if ds == ["embarazo"]: return items, ds
    # Por sus exámenes: una recomendación del informe aprobado (ya filtrada por alergias, dieta y medicamentos).
    if informe and len(items) < maximo:
        for r in informe.get("paciente", {}).get("que_puedes_hacer", []):
            rid = r["recomendacion_id"]
            if rid in ya or rid in usados: continue
            items.append({"id": rid, "tipo": r.get("tipo") or "", "titulo": r["titulo"], "texto": r["texto"], "por_que": r.get("por_que") or "Por tus exámenes.", "fuente": "examenes"})
            ya.add(rid)
            break
    # Para sus objetivos: un consejo aprobado de uno de sus objetivos, rotando por semana.
    objetivos = [o for o in (cuest or {}).get("objetivos") or [] if o in CONSEJOS] or ["bajar_peso"]
    if len(items) < maximo:
        obj = objetivos[semana.isocalendar()[1] % len(objetivos)]
        for c in CONSEJOS[obj]["consejos"]:
            cid = f"OBJ-{obj}-{c['id']}"
            if cid in usados: continue
            items.append({"id": cid, "tipo": "objetivo", "titulo": c["tema"], "texto": c["texto"], "por_que": "Para tus objetivos.", "fuente": "objetivos"})
            break
    while len(items) < maximo and tomar(CONF["disparadores"]["base"], POR_QUE["base"], "semana", False): pass
    return items, ds


def main():
    ap = argparse.ArgumentParser(description="Arma el borrador de recomendaciones de la semana (línea GLP-1)")
    ap.add_argument("--semana", help="lunes de la semana, AAAA-MM-DD (por defecto, el próximo lunes)")
    ap.add_argument("--simular", action="store_true", help="muestra lo que haría sin escribir en Supabase")
    a = ap.parse_args()
    semana = date.fromisoformat(a.semana) if a.semana else lunes_siguiente()
    sb = Supabase(leer_env())
    doctoras = {d["codigo"]: d for d in sb.pedir("GET", "doctoras?select=codigo,limite_semanal,semanas_meseta") or []}
    hechas = 0
    for t in sb.pedir("GET", "tratamientos_peso?select=*") or []:
        pid = urllib.parse.quote(t["paciente_id"])
        existente = sb.uno("semanas_peso", f"paciente_id=eq.{pid}&semana=eq.{semana}&select=estado")
        if existente and existente["estado"] == "publicada":
            print(f"{t['paciente_id'][:8]}: la semana {semana} ya está publicada; no se toca."); continue
        d = doctoras.get(t.get("doctora_codigo") or "", {})
        regs = sb.pedir("GET", f"registros_peso?paciente_id=eq.{pid}&select=fecha,peso,cintura,sintomas&order=fecha") or []
        cuest = sb.uno("cuestionarios", f"paciente_id=eq.{pid}&select=objetivos,embarazo")
        inf = sb.uno("informes", f"paciente_id=eq.{pid}&estado=eq.aprobado&select=informe&order=creado.desc")
        previas = sb.pedir("GET", f"semanas_peso?paciente_id=eq.{pid}&semana=lt.{semana}&select=items&order=semana.desc&limit={CONF['limites']['no_repetir_semanas']}") or []
        items, ds = armar(t, regs, cuest, inf and inf["informe"], previas, float(d.get("limite_semanal", 1.5)), int(d.get("semanas_meseta", 4)), semana)
        problemas = control_salida.revisar_todo([(i["id"], f"{i['titulo']}. {i['texto']} {i['por_que']}") for i in items])
        if problemas:
            malos = {u for u, _ in problemas}
            print(f"{t['paciente_id'][:8]}: el control de salida quitó {', '.join(sorted(malos))}")
            items = [i for i in items if i["id"] not in malos]
        print(f"{t['paciente_id'][:8]}: disparadores {ds or ['ninguno']} → {[i['id'] for i in items]}")
        if not a.simular:
            sb.pedir("POST", "semanas_peso?on_conflict=paciente_id,semana",
                     {"paciente_id": t["paciente_id"], "semana": str(semana), "items": items, "estado": "borrador"},
                     {"Prefer": "resolution=merge-duplicates,return=minimal"})
        hechas += 1
    print(f"{'Simulado' if a.simular else 'Listo'}: {hechas} semanas en borrador para el {semana}. La doctora las publica en /doctora.")


if __name__ == "__main__":
    main()
