"""
Saludly Brain · Lector del PDF de resultados (Fase 3) · versión 1

Lee el PDF del laboratorio, verifica que corresponda a la visita, extrae cada
resultado con sus metadatos, lo normaliza al identificador interno del
Knowledge Base y marca todo lo dudoso. Nunca inventa ni completa datos.

Uso:
    python lector.py ARCHIVO.pdf --visita visita.json --indice 00_INDEX.json [--salida salida.json]

El formato soportado es "saludly-demo-v1" (PDF de ejemplo). Cuando el
laboratorio aliado entregue su formato real, se ajustan las constantes de
FORMATO y se vuelven a correr las pruebas.
"""
import argparse, hashlib, json, re, sys, unicodedata
from datetime import datetime
import pdfplumber
import yaml

FORMATO = dict(
    nombre="saludly-demo-v1",
    etiquetas_encabezado=["Paciente", "Documento", "Sexo", "Nacimiento", "Edad", "Aseguradora",
                          "N.º de orden", "Programa", "Ayuno", "Toma", "Recepción", "Validación"],
    columnas=["Examen", "Resultado", "Ind.", "Unidad", "Valores", "Método"],
    margen_superior=128,     # puntos: por encima, encabezado repetido en cada página
    margen_inferior=60,      # puntos desde abajo: pie de página
)
CAMPOS_ORINA = {"color", "aspecto", "densidad", "ph", "proteinas", "glucosa", "cuerpos cetonicos", "sangre",
                "nitritos", "esterasa leucocitaria", "bilirrubina", "urobilinogeno"}


# ---------------------------------------------------------------- utilidades
def sin_tildes(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()

def norm_nombre(t):
    t = re.sub(r"\s*·\s*refleja.*$", "", t)
    t = sin_tildes(t).lower()
    t = re.sub(r"\(.*?\)", "", t)
    t = re.sub(r"[^a-z0-9%/+ -]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def num(t):
    """'1.120' -> 1120 ; '0,98' -> 0.98 ; '9,8' -> 9.8"""
    t = t.strip()
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", t):
        t = t.replace(".", "")
    t = t.replace(",", ".")
    return float(t)

def norm_unidad(u):
    return sin_tildes((u or "").replace("µ", "u").replace("μ", "u")).lower().replace(" ", "")


# ---------------------------------------------------------------- diccionario
class Diccionario:
    def __init__(self, indice):
        self.bio = indice["biomarcadores"]
        self.sin = {}
        for b, d in self.bio.items():
            for s in (d.get("sinonimos") or []) + [d.get("nombre") or ""]:
                if s:
                    self.sin.setdefault(norm_nombre(str(s)), b)

    def buscar(self, nombre):
        n = norm_nombre(nombre)
        if n.startswith("sedimento") or n in CAMPOS_ORINA:
            return "urinalysis", n
        if n.startswith("coprologico"):
            return "stool_exam", n
        if n in ("albumina en orina", "creatinina en orina"):
            return "uacr", n
        if n in self.sin:
            return self.sin[n], None
        # Sin coincidencia exacta no se adivina: un nombre parecido puede ser otra prueba (por ejemplo, "Lipoproteína X" no es Lp(a)).
        return None, None


# ---------------------------------------------------------------- análisis de valores
def leer_valor(r):
    r = (r or "").strip()
    low = sin_tildes(r).lower()
    if not r:
        return dict(valor=None, estado="no_medido")
    if low.startswith("no procesado") or low.startswith("muestra no apta"):
        return dict(valor=None, estado="invalido", texto=r)
    m = re.fullmatch(r"<\s*([\d.,]+)", r)
    if m:
        return dict(valor=num(m.group(1)), operador="<", estado="menor_que_limite")
    m = re.fullmatch(r">\s*([\d.,]+)", r)
    if m:
        return dict(valor=num(m.group(1)), operador=">", estado="mayor_que_limite")
    if re.fullmatch(r"\d{1,3}(\.\d{3})+|\d+([.,]\d+)?", r):
        return dict(valor=num(r), operador="=", estado="medido")
    m = re.match(r"(no reactivo|reactivo)\s*\(([\d.,]+)\)", low)
    if m:
        return dict(valor=m.group(1), indice=num(m.group(2)), estado="cualitativo")
    m = re.match(r"(positivo|negativo)\s*(\(?<?\s*1:(\d+)\)?)?", low)
    if m and m.group(3):
        return dict(valor=m.group(1), titulo=f"1:{m.group(3)}", estado="cualitativo")
    return dict(valor=r, estado="cualitativo")

def leer_intervalo(t):
    t = (t or "").strip()
    if not t:
        return None
    low = sin_tildes(t).lower()
    out = dict(texto=t)
    if low.startswith("no establecido"):
        out["sin_intervalo"] = True
        return out
    fase = re.match(r"(fase \w+)\s+(.*)", low)
    if fase:
        out["fase"] = fase.group(1)
        t = t[len(fase.group(1)):].strip()
    nota = re.search(r"\((.*?)\)", t)
    if nota:
        out["nota"] = nota.group(1)
        t = re.sub(r"\(.*?\)", "", t).strip()
    m = re.match(r"([\d.,]+)\s*[–-]\s*([\d.,]+)", t)
    if m:
        out.update(bajo=num(m.group(1)), alto=num(m.group(2)))
        return out
    m = re.match(r"(<|≤)\s*([\d.,]+)", t)
    if m:
        out.update(alto=num(m.group(2)), alto_inclusivo=m.group(1) == "≤")
        return out
    m = re.match(r"(>|≥)\s*([\d.,]+)", t)
    if m:
        out.update(bajo=num(m.group(2)), bajo_inclusivo=m.group(1) == "≥")
        return out
    out["esperado_texto"] = t
    return out


# ---------------------------------------------------------------- extracción
def palabras_en_linea(words, top, tol=2.5):
    return sorted([w for w in words if abs(w["top"] - top) <= tol], key=lambda w: w["x0"])

def leer_encabezado(page):
    words = [w for w in page.extract_words() if w["top"] < FORMATO["margen_superior"]]
    out = {}
    etiquetas = []
    for w in words:
        if w["text"].endswith(":"):
            etiquetas.append(w)
    # unir etiquetas de varias palabras ("N.º de orden:")
    for w in etiquetas:
        linea = palabras_en_linea(words, w["top"])
        idx = linea.index(w)
        j = idx
        while j > 0 and not linea[j - 1]["text"].endswith(":") and (linea[j]["x0"] - linea[j - 1]["x1"]) < 6:
            j -= 1
        etiqueta = " ".join(x["text"] for x in linea[j:idx + 1]).rstrip(":")
        valor = []
        for x in linea[idx + 1:]:
            if x["text"].endswith(":"):
                break
            valor.append(x)
        # quitar palabras que en realidad son el inicio de la siguiente etiqueta
        while valor:
            resto = " ".join(v["text"] for v in valor[-3:])
            if any(resto.endswith(e.split()[0]) for e in FORMATO["etiquetas_encabezado"] if " " in e):
                valor = valor[:-1]
            else:
                break
        out[etiqueta] = " ".join(v["text"] for v in valor).strip()
    return {k: v for k, v in out.items() if k in FORMATO["etiquetas_encabezado"]}

def columnas_desde(cabecera):
    xs = {}
    for w in cabecera:
        for c in FORMATO["columnas"]:
            if w["text"].startswith(c) and c not in xs:
                xs[c] = w["x0"]
    return [xs[c] for c in FORMATO["columnas"]] if len(xs) == len(FORMATO["columnas"]) else None

def leer_tablas(pdf):
    filas, observaciones = [], []
    seccion, muestra, cols = None, None, None
    for pnum, page in enumerate(pdf.pages, 1):
        h = page.height
        words = [w for w in page.extract_words(keep_blank_chars=False)
                 if FORMATO["margen_superior"] < w["top"] < h - FORMATO["margen_inferior"]]
        lineas = sorted({round(l["top"], 1) for l in page.lines if abs(l["top"] - l["bottom"]) < 0.5})
        obs = [w for w in words if w["text"] == "OBSERVACIONES"]
        lim_obs = obs[0]["top"] if obs else None
        tabla = [w for w in words if lim_obs is None or w["top"] < lim_obs - 1]
        bandas = {}
        for w in tabla:
            b = sum(1 for y in lineas if y <= w["top"] + 1)
            bandas.setdefault(b, []).append(w)
        for b in sorted(bandas):
            ws = sorted(bandas[b], key=lambda w: (round(w["top"]), w["x0"]))
            textos = [w["text"] for w in ws]
            if "INFORME" in textos and "RESULTADOS" in textos:
                y_inf = [w for w in ws if w["text"] == "INFORME"][0]["top"]
                ws = [w for w in ws if abs(w["top"] - y_inf) > 2]
                textos = [w["text"] for w in ws]
            if "Examen" in textos and "Resultado" in textos:
                y_cab = min(w["top"] for w in ws if w["text"] == "Examen")
                titulo = [w for w in ws if w["top"] < y_cab - 2]
                cab = [w for w in ws if abs(w["top"] - y_cab) < 12 and w["top"] >= y_cab - 2]
                cols = columnas_desde(cab)
                mw = [w for w in titulo if w["text"] == "Muestra:"]
                orden_lectura = lambda lst: " ".join(w["text"] for w in sorted(lst, key=lambda w: (round(w["top"]), w["x0"])))
                if mw:
                    xm = mw[0]["x0"]
                    seccion = orden_lectura([w for w in titulo if w["x0"] < xm - 2])
                    muestra = orden_lectura([w for w in titulo if w["x0"] >= xm - 2 and w["text"] != "Muestra:"])
                elif titulo:
                    seccion = orden_lectura(titulo)
                continue
            if cols is None or not ws:
                continue
            celdas = [""] * len(cols)
            for w in sorted(ws, key=lambda w: (round(w["top"]), w["x0"])):
                i = max(k for k, x in enumerate(cols) if w["x0"] >= x - 2) if w["x0"] >= cols[0] - 2 else 0
                celdas[i] = (celdas[i] + " " + w["text"]).strip()
            filas.append(dict(pagina=pnum, seccion=seccion, muestra=muestra, celdas=celdas))
        if lim_obs is not None:
            resto = [w for w in words if w["top"] > lim_obs + 1]
            texto = " ".join(w["text"] for w in sorted(resto, key=lambda w: (round(w["top"]), w["x0"])))
            observaciones += [o.strip() for o in texto.split("·") if o.strip()]
    return filas, observaciones


# ---------------------------------------------------------------- lectura completa
def leer(pdf_path, visita, indice, conversiones=None):
    dic = Diccionario(indice)
    conversiones = conversiones or {}
    raw = open(pdf_path, "rb").read()
    out = dict(archivo=pdf_path.split("/")[-1], sha256=hashlib.sha256(raw).hexdigest(), formato=FORMATO["nombre"],
               leido_en=datetime.now().isoformat(timespec="seconds"), estado="aceptado", motivo=None,
               encabezado={}, metadatos_pdf={}, resultados=[], observaciones=[], dudas=[])
    with pdfplumber.open(pdf_path) as pdf:
        meta = pdf.metadata or {}
        out["metadatos_pdf"] = {k: meta.get(k) for k in ("Title", "Subject", "Keywords", "Author", "Creator")}
        encabezados = [leer_encabezado(p) for p in pdf.pages]
        enc = encabezados[0]
        out["encabezado"] = enc
        # 1. identidad: documento y orden deben coincidir con la visita y en todas las páginas
        docs = {e.get("Documento") for e in encabezados}
        ords = {e.get("N.º de orden") for e in encabezados}
        if len(docs) > 1 or len(ords) > 1:
            out.update(estado="rechazado", motivo=f"Las páginas no son del mismo paciente u orden: documentos {sorted(docs)}, órdenes {sorted(ords)}")
            return out
        if enc.get("Documento") != visita.get("documento") or enc.get("N.º de orden") != visita.get("orden"):
            out.update(estado="rechazado", motivo=f"El PDF no coincide con la visita: PDF {enc.get('Documento')} / {enc.get('N.º de orden')}, visita {visita.get('documento')} / {visita.get('orden')}")
            return out
        kw = meta.get("Keywords") or ""
        if kw and (f"orden={visita.get('orden')}" not in kw or f"documento={visita.get('documento')}" not in kw):
            out["dudas"].append("Los metadatos del PDF no coinciden con el encabezado impreso.")
        filas, obs = leer_tablas(pdf)
    out["observaciones"] = obs
    vistos = {}
    for f in filas:
        examen, res, ind, uni, ref, met = (f["celdas"] + [""] * 6)[:6]
        bid, campo = dic.buscar(examen)
        v = leer_valor(res)
        r = dict(nombre_original=examen, biomarker_id=bid, campo=campo, valor_original=res, **v,
                 indicador_lab=ind or None, unidad=uni or None, intervalo_lab=leer_intervalo(ref), metodo=met or None,
                 seccion=f["seccion"], muestra=f["muestra"], pagina=f["pagina"],
                 refleja="refleja" in examen, activada_por=(examen.split("refleja por", 1)[1].strip() if "refleja por" in examen else None),
                 dudas=[])
        if bid is None:
            r["dudas"].append("Nombre no reconocido en el diccionario de sinónimos.")
        elif campo is None:
            canon = indice["biomarcadores"][bid].get("unidad")
            if uni and canon and norm_unidad(uni) != norm_unidad(canon) and not norm_unidad(canon).startswith(norm_unidad(uni)):
                key = f"{bid}:{norm_unidad(uni)}"
                if key in conversiones and isinstance(r.get("valor"), float):
                    r["valor_canonico"] = round(r["valor"] * conversiones[key], 4)
                    r["unidad_canonica"] = canon
                else:
                    r["dudas"].append(f"Unidad '{uni}' distinta de la canónica '{canon}' y sin regla de conversión.")
        if v.get("estado") == "invalido":
            r["dudas"].append("El laboratorio no entregó un resultado válido; requiere nueva muestra o revisión.")
        if ind == "*":
            r["dudas"].append("El laboratorio marcó este resultado con una observación (*).")
        clave = (bid, campo)
        if bid and clave in vistos:
            r["dudas"].append(f"Resultado duplicado (también en la página {vistos[clave]}).")
        vistos[clave] = f["pagina"]
        out["resultados"].append(r)
    out["dudas"] += [f"{r['nombre_original']}: {d}" for r in out["resultados"] for d in r["dudas"]]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--visita", required=True); ap.add_argument("--indice", required=True)
    ap.add_argument("--conversiones", default=None); ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    visita = json.load(open(a.visita, encoding="utf-8"))
    indice = json.load(open(a.indice, encoding="utf-8"))
    conv = yaml.safe_load(open(a.conversiones, encoding="utf-8")) if a.conversiones else {}
    res = leer(a.pdf, visita, indice, conv)
    txt = json.dumps(res, ensure_ascii=False, indent=1)
    if a.salida:
        open(a.salida, "w", encoding="utf-8").write(txt)
    else:
        print(txt)
    sys.exit(0 if res["estado"] == "aceptado" else 2)

if __name__ == "__main__":
    main()
