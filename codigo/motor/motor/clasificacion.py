"""
Saludly Brain · Motor · Clasificación (documento 04, sección 04.4)

Clases: no_interpretable, critico, bajo, limitrofe, en_rango, alto, alterado
(alterado = resultado cualitativo distinto del esperado), o None si el
laboratorio no da intervalo ("No establecido").
"""
import re, unicodedata

def _n(t):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()).strip()

ESPERADOS_NORMALES = {"negativo", "no reactivo", "amarillo", "claro", "escasas", "escasos", "no se observan", "no se observaron parasitos"}


def bloqueos_de_contexto(bid, r, ctx, reglas, R):
    """Devuelve el motivo por el que el contexto impide interpretar, o None."""
    np = reglas["no_interpretable_por_contexto"]
    if bid in np["ayuno_minimo_8h"] and (ctx.get("ayuno_horas") is None or ctx["ayuno_horas"] < 8):
        return "ayuno menor de 8 horas o sin dato"
    if bid in np["cortisol_fuera_de_6_a_10"]:
        h = ctx.get("hora_toma")
        if not h: return "sin hora de toma"
        hh, mm = map(int, h.split(":"))
        if not (6 * 60 <= hh * 60 + mm <= 10 * 60): return f"toma a las {h}, fuera de 6:00 a 10:00"
    if bid in np["biotina"]:
        if any("biotina" in s.lower() for s in ctx.get("suplementos", [])):
            return "suplemento de biotina declarado: repetir sin el suplemento"
        bt = R.get("biotin"); hi = ((bt or {}).get("intervalo_lab") or {}).get("alto")
        if bt and hi and isinstance(bt.get("valor"), (int, float)) and bt["valor"] > hi:
            return "biotina alta: repetir sin el suplemento"
    if bid in np["hormonas_de_fase"] and ctx.get("sexo") == "mujer":
        if ctx.get("embarazo"): return "embarazo"
        if ctx.get("anticonceptivo_hormonal"): return "anticonceptivo hormonal: no interpretable por fase"
        if ctx.get("menopausia"): return "menopausia declarada: no interpretable por fase"
        if not ctx.get("fecha_ultima_menstruacion"): return "sin fecha de última menstruación: no interpretable por fase"
    if bid in np["embarazo"] and ctx.get("embarazo"):
        return "embarazo"
    if bid in np["vitamina_c_sin_transporte_validado"] and not ctx.get("laboratorio", {}).get("transporte_vitamina_c_validado"):
        return "el laboratorio no ha validado el transporte congelado de la vitamina C"
    if bid == "urinalysis" and ctx.get("menstruacion_actual") and r.get("campo") in ("sangre", "sedimento hematies"):
        return "menstruación actual"
    return None


def _num_de_rango_texto(v):
    m = re.fullmatch(r"\s*(\d+)\s*[–-]\s*(\d+)\s*", str(v))
    return float(m.group(2)) if m else None


def clasificar(r, ctx, reglas, R):
    bid = r.get("biomarker_id")
    out = dict(clase=None, motivo=None)
    if r.get("estado") in ("invalido", "no_medido"):
        return dict(clase="no_interpretable", motivo="resultado no válido según el laboratorio" if r.get("estado") == "invalido" else "no medido")
    if bid is None:
        return dict(clase="no_interpretable", motivo="biomarcador no reconocido")
    bloq = bloqueos_de_contexto(bid, r, ctx, reglas, R)
    if bloq:
        return dict(clase="no_interpretable", motivo=bloq)
    iv = r.get("intervalo_lab") or {}
    if iv.get("sin_intervalo"):
        return dict(clase=None, motivo="sin intervalo de referencia del laboratorio: solo valor")
    if r.get("indicador_lab") and "crit" in _n(r["indicador_lab"]):
        return dict(clase="critico", motivo="bandera crítica del laboratorio")
    lo, hi = iv.get("bajo"), iv.get("alto")
    est = r.get("estado")
    # Cualitativos
    if est == "cualitativo":
        if r.get("indice") is not None and hi is not None:
            v = r["indice"]
            return dict(clase="en_rango" if v < hi else "alterado", motivo=None)
        esperado = _n(iv.get("esperado_texto") or iv.get("texto") or "")
        val = _n(r.get("valor"))
        sup = _num_de_rango_texto(r.get("valor"))
        if sup is not None and hi is not None:
            return dict(clase="en_rango" if sup <= hi else "alto", motivo=None)
        if not esperado:
            return dict(clase=None, motivo="sin valor esperado: solo valor")
        if val == esperado or (val in ESPERADOS_NORMALES and esperado in ESPERADOS_NORMALES):
            return dict(clase="en_rango", motivo=None)
        if esperado.startswith("negativo") and val.startswith("negativo"):
            return dict(clase="en_rango", motivo=None)
        return dict(clase="alterado", motivo=f"esperado '{iv.get('texto')}'")
    v = r.get("valor")
    if not isinstance(v, (int, float)):
        return dict(clase=None, motivo="valor no numérico")
    # Críticos por guía
    cg = reglas["critico_por_guia"].get(bid)
    if cg:
        if "menor_que" in cg and est == "medido" and v < cg["menor_que"]:
            return dict(clase="critico", motivo=f"menor de {cg['menor_que']} ({cg['fuente']}); confirmar que la muestra sea confiable")
        if cg.get("mayor_que_limite_superior") and hi is not None and est != "menor_que_limite" and v > hi:
            return dict(clase="critico", motivo=f"sobre el percentil 99 ({cg['fuente']})")
    # Menor / mayor que el límite de detección
    if est == "menor_que_limite":
        if lo is not None and v <= lo: return dict(clase="bajo", motivo="menor que el límite de detección, bajo el intervalo")
        return dict(clase="en_rango", motivo="menor que el límite de detección")
    if est == "mayor_que_limite":
        return dict(clase="alto", motivo="mayor que el límite de medición")
    # Numéricos
    txt = iv.get("texto", "").strip()
    if lo is None and hi is None and re.fullmatch(r"\d+([.,]\d+)?", txt):
        esperado = float(txt.replace(",", "."))   # intervalo de un solo valor, por ejemplo eritroblastos "0,0"
        return dict(clase="en_rango" if v <= esperado else "alto", motivo=None)
    estricto_bajo = txt.startswith(">") and not iv.get("bajo_inclusivo")
    if lo is not None and (v <= lo if estricto_bajo else v < lo):
        clase = "bajo"
    elif hi is not None and (v >= hi if (iv.get("texto", "").strip().startswith("<") and not iv.get("alto_inclusivo")) else v > hi):
        clase = "alto"
    elif lo is None and hi is None:
        return dict(clase=None, motivo="intervalo no numérico: solo valor")
    else:
        clase = "en_rango"
    # Limítrofe definido por ficha
    lim = reglas["limitrofe"].get(bid)
    if clase == "en_rango" and lim:
        if bid == "alt":
            s = lim.get(ctx.get("sexo"), {}).get("sobre")
            if s is not None and v > s: return dict(clase="limitrofe", motivo=f"sobre el valor sano de la ACG ({s} UI/L), dentro del laboratorio")
        if "zona" in lim and lim["zona"]["desde"] <= v <= lim["zona"]["hasta"]:
            return dict(clase="limitrofe", motivo=f"zona de vigilancia {lim['zona']['desde']}-{int(lim['zona']['hasta'])} ({lim['fuente']})")
    return dict(clase=clase, motivo=None)
