"""
Saludly Brain · Comando de punta a punta (MVP)

PDF del laboratorio → lector → motor → informe para el dashboard + mensajes de WhatsApp + resumen en Markdown.

Uso:
  python saludly.py --pdf resultado.pdf --documento "CC 0000000001" --orden LCD-2026-100123 \
                    --perfil perfil.json [--enfermera enfermera.json] [--salida carpeta] [--dias 7]

perfil.json (lo da el paciente en la PWA):
  {"objetivos": ["bajar_peso", "energia_sueno", "prevenir"], "toma_biotina": false, "nivel_actividad": "ligero"}
  nivel_actividad: sedentario | ligero | moderado | alto (si falta, se usa "ligero")
enfermera.json (datos complementarios de la visita; todos opcionales):
  {"presion_sistolica": 128, "presion_diastolica": 82, "cintura_cm": 94, "peso_kg": 82, "talla_m": 1.74,
   "tabaquismo": false, "medicamentos": [], "suplementos": [],
   "embarazo": false, "fecha_ultima_menstruacion": "2026-09-20", "anticonceptivo_hormonal": false, "ciudad": "Bogotá"}

Reglas:
- El PDF no se guarda: se lee y se descarta. Se guarda solo lo extraído, con el paciente seudonimizado (nunca nombre ni documento).
- Edad, sexo, horas de ayuno y hora de toma salen del PDF. La ciudad es Bogotá salvo que la enfermera diga otra.
- Código de salida: 0 informe generado, 2 PDF rechazado (no coincide con la visita), 3 datos del paciente inválidos.
"""
import argparse, hashlib, json, os, re, sys
from datetime import datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "codigo", "motor", "motor"))
sys.path.insert(0, os.path.join(RAIZ, "codigo", "informe"))
import lector, motor
import contenido, redactar

VERSION_REDACCION = "plantillas-v1"


def seudonimo(documento):
    sal = os.environ.get("SALUDLY_SAL_SEUDONIMO", "saludly-mvp")
    return "P-" + hashlib.sha256(f"{sal}|{documento}".encode()).hexdigest()[:8].upper()


def contexto_desde_pdf(encabezado):
    sexo = {"masculino": "hombre", "femenino": "mujer"}.get((encabezado.get("Sexo") or "").strip().lower())
    m = re.search(r"\d+", encabezado.get("Edad") or ""); edad = int(m.group(0)) if m else None
    m = re.search(r"\d+", encabezado.get("Ayuno") or ""); ayuno = int(m.group(0)) if m else None
    m = re.search(r"(\d{1,2}:\d{2})", encabezado.get("Toma") or ""); hora = m.group(1).zfill(5) if m else None
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", encabezado.get("Toma") or ""); fecha = f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else None
    return dict(sexo=sexo, edad=edad, ayuno_horas=ayuno, hora_toma=hora), fecha


def generar(pdf, documento, orden, perfil, enfermera=None, dias=7, panel=None):
    C = contenido.cargar()
    objetivos = perfil.get("objetivos") or []
    malos = [o for o in objetivos if o not in C["objetivos"]]
    if not (1 <= len(objetivos) <= 3) or malos:
        return 3, dict(estado="datos_invalidos", motivo=f"Se necesitan de 1 a 3 objetivos válidos; desconocidos: {malos}", objetivos_validos=list(C["objetivos"]))
    if perfil.get("toma_biotina") not in (True, False, None):
        return 3, dict(estado="datos_invalidos", motivo="toma_biotina debe ser true, false o null")
    if perfil.get("nivel_actividad") not in (None, "sedentario", "ligero", "moderado", "alto"):
        return 3, dict(estado="datos_invalidos", motivo="nivel_actividad debe ser sedentario, ligero, moderado o alto")
    fil = C.get("filtros", {}).get("preguntas", {})
    validos = {k: {o["id"] for o in (fil.get(k) or {}).get("opciones") or []} for k in ("alergias", "dieta", "medicamentos")}
    for k in ("alergias", "medicamentos"):
        malos = [x for x in perfil.get(k) or [] if x not in validos[k]]
        if malos: return 3, dict(estado="datos_invalidos", motivo=f"{k} desconocidos: {malos}", validos=sorted(validos[k]))
    if perfil.get("dieta") not in ({None} | validos["dieta"]):
        return 3, dict(estado="datos_invalidos", motivo=f"dieta debe ser una de {sorted(validos['dieta'])}")
    lect = lector.leer(pdf, dict(documento=documento, orden=orden), C["indice"])
    if lect.get("estado") != "aceptado":
        return 2, dict(estado="pdf_rechazado", motivo=lect.get("motivo"), sha256=lect.get("sha256"))
    ctx_pdf, fecha_toma = contexto_desde_pdf(lect["encabezado"])
    enf = dict(enfermera or {})
    ctx = dict(ciudad=enf.pop("ciudad", None) or "Bogotá", laboratorio={"transporte_vitamina_c_validado": False}, wearable={"activo": False})
    ctx.update({k: v for k, v in ctx_pdf.items() if v is not None})
    ctx.update(enf)
    ctx["toma_biotina"] = perfil.get("toma_biotina")
    if perfil.get("nivel_actividad"): ctx["nivel_actividad"] = perfil["nivel_actividad"]   # lo responde el paciente en la PWA
    for k in ("alergias", "alergias_otras", "dieta", "medicamentos"):                     # también de la PWA (filtros.yaml)
        if perfil.get(k): ctx[k] = perfil[k]
    ctx["objetivo"] = objetivos[0]
    if panel: ctx["panel"] = panel
    out = motor.analizar(lect, ctx)
    ref = seudonimo(documento)
    inf = redactar.armar(out, ctx, objetivos, C, ref, dias)
    informe = dict(
        informe_id=f"INF-{orden}-v1", paciente_ref=ref, orden=orden, fecha_toma=fecha_toma, generado=datetime.now().isoformat(timespec="seconds"),
        estado=inf["estado"], panel=out.get("panel"), escalamiento_maximo=out["escalamiento_maximo"], canal=out["canal"],
        objetivos=[dict(id=o, nombre=C["objetivos"][o]["nombre"]) for o in objetivos],
        perfil=dict(edad=ctx.get("edad"), sexo=ctx.get("sexo"), ciudad=ctx.get("ciudad"), toma_biotina=ctx.get("toma_biotina"), nivel_actividad=ctx.get("nivel_actividad") or "ligero (supuesto)",
                    medidas_enfermera={k: ctx.get(k) for k in ("presion_sistolica", "presion_diastolica", "cintura_cm", "peso_kg", "talla_m") if ctx.get(k) is not None}),
        wearable=dict(activo=False),
        paciente=inf["paciente"], resultados=inf["resultados"],
        edad_biologica=out.get("edad_biologica"), recordatorios=out.get("recordatorios"),
        nutricion=inf["nutricion"], whatsapp=inf["whatsapp"], medico=inf["medico"], control_salida=inf["control_salida"],
        trazabilidad=dict(sha256_pdf=lect.get("sha256"), version_kb=C["version_kb"], version_redaccion=VERSION_REDACCION, version_modelo=None,
                          calculados=out.get("calculados")))
    return 0, informe


def resumen_md(inf):
    p = inf["paciente"]
    L = [f"# Informe {inf['informe_id']}", "", f"- Paciente: {inf['paciente_ref']} · {inf['perfil'].get('sexo')} · {inf['perfil'].get('edad')} años · {inf['perfil'].get('ciudad')}",
         f"- Toma: {inf['fecha_toma']} · Estado: {inf['estado']} · Escalamiento máximo: {inf['escalamiento_maximo']} ({inf['canal']})",
         f"- Objetivos: {', '.join(o['nombre'] for o in inf['objetivos'])}", "", "## Resumen", "", p["resumen"], "", "## Lo que merece atención", ""]
    for a in p["lo_que_merece_atencion"]:
        L += [f"### {a['titulo']} · escalamiento {a['escalamiento']} ({a['referencia']})", "", a["que_es"], ""] + [f"- {x}" for x in a["por_que"]] + ["", f"*Ejemplo:* {a['ejemplo']}", ""]
    L += ["## Lo que está bien", ""] + [f"- {b['texto']}" for b in p["lo_que_esta_bien"]] + ["", "## Qué puedes hacer", ""]
    L += [f"- **{r['titulo']}** ({r['tipo']}): {r['texto']}" for r in p["que_puedes_hacer"]] + ["", "## Cuándo consultar", ""]
    L += [f"- Nivel {c['escalamiento']}: {c['texto']}" for c in p["cuando_consultar"]] + ["", "## Resultados", "", "| Biomarcador | Valor | Intervalo | Clase |", "| --- | --- | --- | --- |"]
    L += [f"| {r['nombre']} | {r['valor_original'] or ''} {r['unidad'] or ''} | {r['intervalo'] or ''} | {r['clase'] or ''} |" for r in inf["resultados"]]
    cs = inf["control_salida"]
    L += ["", "## Control de salida", "", "Sin problemas." if cs["ok"] else f"{len(cs['problemas'])} problemas; hallazgos sin texto: {cs['hallazgos_sin_texto']}"]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="PDF del laboratorio → informe de Saludly")
    ap.add_argument("--pdf", required=True); ap.add_argument("--documento", required=True); ap.add_argument("--orden", required=True)
    ap.add_argument("--perfil", required=True, help="JSON con objetivos (1 a 3) y toma_biotina")
    ap.add_argument("--enfermera", help="JSON con presión, cintura, peso, talla y demás datos de la visita")
    ap.add_argument("--salida", default="."); ap.add_argument("--dias", type=int, default=7); ap.add_argument("--panel", choices=["solo_sangre", "completo"])
    a = ap.parse_args()
    perfil = json.load(open(a.perfil, encoding="utf-8"))
    enf = json.load(open(a.enfermera, encoding="utf-8")) if a.enfermera else None
    codigo, inf = generar(a.pdf, a.documento, a.orden, perfil, enf, a.dias, a.panel)
    os.makedirs(a.salida, exist_ok=True)
    if codigo:
        print(json.dumps(inf, ensure_ascii=False, indent=1)); sys.exit(codigo)
    base = os.path.join(a.salida, inf["informe_id"])
    json.dump(inf, open(base + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(base + ".md", "w", encoding="utf-8").write(resumen_md(inf))
    cs = inf["control_salida"]
    print(f"{inf['informe_id']}: estado {inf['estado']}, escalamiento {inf['escalamiento_maximo']}, {len(inf['paciente']['lo_que_merece_atencion'])} hallazgos, "
          f"{len(inf['paciente']['que_puedes_hacer'])} recomendaciones, {len(inf['nutricion']['plan'])} recetas; control de salida: "
          f"{'ok' if cs['ok'] else str(len(cs['problemas'])) + ' problemas, sin texto: ' + str(cs['hallazgos_sin_texto'])}")
    print(f"→ {base}.json y {base}.md")


if __name__ == "__main__":
    main()
