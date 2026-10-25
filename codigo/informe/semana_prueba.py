"""
Saludly · Semana de prueba de la preventa: los mensajes de WhatsApp de cada día para una persona del pre-registro.

Contenido en knowledge_base/fase5/semana_prueba.yaml y consejos_objetivos.yaml. Cada persona recibe su propia semana
con todos los consejos de sus objetivos (hasta 3), dos por objetivo al día, agrupados para no llenarla de notificaciones:
- 07:00 consejos de la mañana: uno por objetivo, en un solo mensaje;
- 09:00 la receta del catálogo aprobado, sin las que tienen sus alérgenos (nutricion.plan_recetas, con su código como
  semilla: dos personas con los mismos objetivos no reciben las mismas recetas), y una pregunta con botones;
- 13:00 los días 1, 3, 5 y 7, uno para bajarle al estrés (cortisol);
- 18:00 lo que solo responde el examen de sangre, con una pregunta con botones (el día 7, el cierre y el anticipo);
- 19:30 consejos de la tarde, días 1 a 6: uno por objetivo, en un solo mensaje.
Sin examen no hay hallazgos: no se diagnostica nada y todo pasa por el control de salida.

Uso:
  python codigo/informe/semana_prueba.py --validar            revisa el contenido (sale con 1 si hay errores)
  python codigo/informe/semana_prueba.py --vista salida.json  la semana de ejemplo de cada objetivo, para revisarla
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml
import contenido, control_salida, nutricion

ARCHIVO = os.path.join(contenido.F5, "semana_prueba.yaml")
CONSEJOS = os.path.join(contenido.F5, "consejos_objetivos.yaml")
DIAS = 7
MAX_OBJETIVOS = 3
# Espacios de consejos por objetivo: las 7 mañanas y las tardes de los días 1 a 6 (la del día 7 la ocupa el cierre)
ESPACIOS = [(d, "manana") for d in range(1, DIAS + 1)] + [(d, "tarde") for d in range(1, DIAS)]
CALCULADOS = {"egfr", "phenoage", "homa_ir", "tyg_index", "tg_hdl_ratio"}
# Nombre corto de cada alergia del pre-registro (mismos ids que filtros.yaml y los alérgenos de alimentos.yaml)
ALERGIA = {"mani": "maní", "frutos_secos": "frutos secos", "mariscos": "mariscos", "pescado": "pescado", "huevo": "huevo",
           "leche": "leche", "lactosa": "lactosa", "gluten": "gluten", "soya": "soya", "ajonjoli": "ajonjolí"}
# WhatsApp: botones de respuesta rápida por mensaje y largo de cada uno; texto máximo de un mensaje con botones
MAX_BOTONES, MAX_BOTON, MAX_BOTON_PLANTILLA, MAX_TEXTO_BOTONES, MAX_TEXTO = 3, 20, 25, 1024, 4096


def cargar():
    C = contenido.cargar()
    S = yaml.safe_load(open(ARCHIVO, encoding="utf-8"))
    S["por_objetivo"] = yaml.safe_load(open(CONSEJOS, encoding="utf-8"))["objetivos"]
    C["catalogo"] = nutricion.catalogo(C["recetas"], C["alimentos"])
    return C, S


def familia(S, objetivo):
    return next(f for f, objs in S["familias"].items() if objetivo in objs)


def objetivo_en_tu(nombre):
    """'Aumentar mi masa muscular' → 'aumentar tu masa muscular'."""
    t = nombre[0].lower() + nombre[1:]
    return re.sub(r"\bmi\b", "tu", t).replace("que ya tengo", "que ya tienes")


def frase_alergias(alergias):
    nombres = [ALERGIA.get(a, a) for a in alergias]
    if not nombres: return ""
    lista = nombres[0] if len(nombres) == 1 else ", ".join(nombres[:-1]) + " ni " + nombres[-1]
    return f" Ninguna receta lleva {lista}."


def objetivos_persona(C, objetivos):
    """Los que eligió en el pre-registro, en su orden y sin "Otro" (hasta 3); si no queda ninguno, salud general."""
    validos = list(dict.fromkeys(o for o in objetivos or [] if o in C["objetivos"]))[:MAX_OBJETIVOS]
    return validos or ["salud_general"]


def reparto(consejos):
    """{(día, turno): consejo} de un objetivo: los de turno fijo en su turno y los demás en los espacios libres, en orden."""
    libres, asignado = list(ESPACIOS), {}
    for turno in ("tarde", "manana"):
        for c in (c for c in consejos if c["turno"] == turno):
            e = next(e for e in libres if e[1] == turno); asignado[e] = c; libres.remove(e)
    libres.sort()
    for c in (c for c in consejos if c["turno"] == "cualquiera"):
        asignado[libres.pop(0)] = c
    return asignado


def lista_objetivos(C, objs):
    nombres = [objetivo_en_tu(C["objetivos"][o]["nombre"]) for o in objs]
    if len(nombres) == 1: return f"tu objetivo: {nombres[0]}"
    return "tus objetivos: " + ", ".join(nombres[:-1]) + " y " + nombres[-1]


def cortisol_del_dia(S, objs, dia):
    """El de cada objetivo y después los generales, sin repetir, en los días de cortisol."""
    if dia not in S["dias_cortisol"]: return None
    lista = list(dict.fromkeys([S["por_objetivo"][o]["cortisol"]["texto"] for o in objs] + S["cortisol_general"]))
    return lista[S["dias_cortisol"].index(dia)]


def plan(C, persona):
    restr = nutricion.restricciones({"condiciones": {}, "calculados": {}}, {"alergias": persona.get("alergias") or []})
    return nutricion.plan_recetas(C["catalogo"], restr, objetivos_persona(C, persona["objetivos"]), persona["codigo"], dias=DIAS)


def mensajes(C, S, persona, dia, recetas=None):
    """Envíos del día 1 a 7, en orden: [{envio, hora, texto, botones}]. persona: nombre, objetivos, alergias, codigo."""
    objs, nombre, h = objetivos_persona(C, persona["objetivos"]), persona["nombre"].split()[0], S["horarios"]
    recetas = recetas or plan(C, persona)["plan"]
    r = next(x for x in C["catalogo"] if x["id"] == recetas[dia - 1]["receta_id"])
    g = S["ganchos"][familia(S, objs[0])][dia - 1]
    pr = S["preguntas_receta"][dia]
    repartos = {o: reparto(S["por_objetivo"][o]["consejos"]) for o in objs}

    def consejos(turno, titulo):
        partes = [f"{S['por_objetivo'][o]['emoji']} *{C['objetivos'][o]['nombre']}*\n{repartos[o][(dia, turno)]['texto']}"
                  for o in objs if (dia, turno) in repartos[o]]
        return partes and f"*Día {dia} de {DIAS}* · {titulo}\n\n" + "\n\n".join(partes)

    if dia == 1:
        horas = dict(manana="al escribir hola", receta="2 horas después", cortisol=f"{h['cortisol']} o con la receta", examen=h["examen"], tarde=h["tarde"])
    else:
        horas = h
    out = []
    if dia == 1:
        out.append(dict(envio="manana", hora=horas["manana"], botones=[], texto=S["bienvenida"].format(
            nombre=nombre, objetivos=lista_objetivos(C, objs), sin_alergias=frase_alergias(persona.get("alergias") or []))))
    if (t := consejos("manana", "Tus consejos de la mañana")):
        out.append(dict(envio="manana", hora=horas["manana"], botones=[], texto=t))
    out.append(dict(envio="receta", hora=horas["receta"], botones=[], texto=nutricion.mensaje_receta(r, C["alimentos"], {})))
    out.append(dict(envio="receta", hora=horas["receta"], botones=pr["botones"], texto=pr["texto"]))
    if (c := cortisol_del_dia(S, objs, dia)):
        out.append(dict(envio="cortisol", hora=horas["cortisol"], botones=[], texto=f"🌿 *Bájale al estrés*\n\n{c}"))
    if dia < DIAS:
        out.append(dict(envio="examen", hora=horas["examen"], botones=g["botones"], texto=f"🩸 *Solo tu examen lo dice*\n\n{g['texto']}\n\n{g['pregunta']}"))
        if (t := consejos("tarde", "Tus consejos de la tarde")):
            out.append(dict(envio="tarde", hora=horas["tarde"], botones=[], texto=t))
    else:
        cierre = S["cierre"].format(nombre=nombre, valor=f"${S['anticipo_valor']:,}".replace(",", "."))
        if "condicion_existente" in objs: cierre += " " + S["aviso_condicion_existente"]
        out.append(dict(envio="examen", hora=horas["examen"], botones=S["cierre_botones"], texto=f"🩸 *Solo tu examen lo dice*\n\n{g['texto']}\n\n{cierre}"))
    return out


def _botones(donde, botones, errores, maximo=MAX_BOTON):
    if not 1 <= len(botones) <= MAX_BOTONES: errores.append(f"{donde}: necesita de 1 a {MAX_BOTONES} botones")
    if len(set(botones)) != len(botones): errores.append(f"{donde}: botones repetidos")
    for b in botones:
        if len(b) > maximo: errores.append(f"{donde}: el botón «{b}» pasa de {maximo} caracteres")


def validar(C, S):
    errores = []
    panel = {b for b, d in C["indice"]["biomarcadores"].items() if d.get("panel") == "estándar"} | CALCULADOS
    if len(S["dias_cortisol"]) > MAX_OBJETIVOS + len(S["cortisol_general"]) or len(S["cortisol_general"]) < len(S["dias_cortisol"]) - 1:
        errores.append("cortisol: no alcanzan los mensajes para los días de cortisol con un solo objetivo")
    for obj in C["objetivos"]:
        if not any(obj in o for o in S["familias"].values()): errores.append(f"{obj}: sin familia de ganchos")
        po = S["por_objetivo"].get(obj)
        if not po: errores.append(f"{obj}: sin consejos en consejos_objetivos.yaml"); continue
        cs = po["consejos"]
        if not DIAS <= len(cs) <= len(ESPACIOS): errores.append(f"{obj}: necesita de {DIAS} a {len(ESPACIOS)} consejos (tiene {len(cs)})")
        if len({c["id"] for c in cs}) != len(cs): errores.append(f"{obj}: ids de consejo repetidos")
        for turno in ("manana", "tarde"):
            cupo = sum(1 for e in ESPACIOS if e[1] == turno)
            if sum(1 for c in cs if c["turno"] == turno) > cupo: errores.append(f"{obj}: más de {cupo} consejos de turno {turno}")
        for c in cs:
            if c["turno"] not in ("manana", "tarde", "cualquiera"): errores.append(f"{obj} {c['id']}: turno desconocido")
            if re.search(r"este (domingo|s[aá]bado|fin de semana)|informe de saludly", c["texto"], re.I): errores.append(f"{obj} {c['id']}: depende del día o del informe")
            if len(c["texto"]) > 330: errores.append(f"{obj} {c['id']}: consejo muy largo para WhatsApp")
    for d in range(1, DIAS + 1):
        _botones(f"pregunta de la receta, día {d}", S["preguntas_receta"][d]["botones"], errores)
    _botones("cierre", S["cierre_botones"], errores)
    for fam, gs in S["ganchos"].items():
        if len(gs) != DIAS: errores.append(f"ganchos {fam}: hacen falta {DIAS}")
        for k, g in enumerate(gs):
            for b in g["biomarcadores"]:
                if b not in panel: errores.append(f"ganchos {fam}: {b} no está en el panel estándar")
            if k < DIAS - 1:
                if not g.get("pregunta"): errores.append(f"ganchos {fam} día {k + 1}: sin pregunta")
                _botones(f"ganchos {fam} día {k + 1}", g.get("botones") or [], errores)
    textos = [("bienvenida", S["bienvenida"]), ("cierre", S["cierre"]), ("aviso", S["aviso_condicion_existente"]),
              ("respuesta", S["respuesta_boton"]), ("respuesta de interés", S["respuesta_interes"]), ("respuesta día 7", S["respuesta_boton_dia7"]),
              ("hola en curso", S["respuesta_hola_en_curso"]), ("respuesta a otro", S["respuesta_otro"])]
    textos += [(f"cierre «{b}»", t) for b, t in S["respuestas_cierre"].items()] + [(f"recordatorio {k}", t) for k, t in S["recordatorio_que"].items()]
    for b in S["cierre_botones"] + [b for p in S["plantillas"] if p["nombre"] == "cierre_semana" for b in p["botones"]]:
        if b not in S["respuestas_cierre"] and b != "Quiero saber": errores.append(f"cierre: el botón «{b}» no tiene respuesta")
    textos += [(f"{obj} consejo {c['id']}", c["texto"]) for obj, po in S["por_objetivo"].items() for c in po["consejos"]]
    textos += [(f"{obj} cortisol", po["cortisol"]["texto"]) for obj, po in S["por_objetivo"].items()]
    textos += [(f"cortisol general {k + 1}", t) for k, t in enumerate(S["cortisol_general"])]
    textos += [(f"pregunta receta {d}", " ".join([p["texto"]] + p["botones"])) for d, p in S["preguntas_receta"].items()]
    textos += [(f"gancho {f} {k + 1}", " ".join([g["texto"], g.get("pregunta") or ""] + (g.get("botones") or []))) for f, gs in S["ganchos"].items() for k, g in enumerate(gs)]
    textos += [(f"plantilla {p['nombre']}", " ".join([p["cuerpo"]] + p["botones"])) for p in S["plantillas"]]
    for p in S["plantillas"]:
        n = len(set(re.findall(r"\{\{(\d+)\}\}", p["cuerpo"])))
        if n != len(p["ejemplo"]): errores.append(f"plantilla {p['nombre']}: {n} variables y {len(p['ejemplo'])} ejemplos")
        if len(p["cuerpo"]) > 1024: errores.append(f"plantilla {p['nombre']}: más de 1.024 caracteres")
        _botones(f"plantilla {p['nombre']}", p["botones"], errores, maximo=MAX_BOTON_PLANTILLA)
    # Siempre 7 recetas, con cualquier alergia sola o con todas juntas
    for obj in C["objetivos"]:
        for ale in [[]] + [[a] for a in ALERGIA] + [list(ALERGIA)]:
            p = plan(C, dict(objetivos=[obj], alergias=ale, codigo="prueba"))
            if len(p["plan"]) < DIAS: errores.append(f"{obj} sin {ale}: solo {len(p['plan'])} recetas")
            for d in p["plan"]:
                r = next(x for x in C["catalogo"] if x["id"] == d["receta_id"])
                if set(ale) & set(r["alergenos"]): errores.append(f"{d['receta_id']} tiene un alérgeno de {ale}")
    # Cada objetivo solo y en grupos de 3 que pasan por todos: salen todos sus consejos, una vez, y los mensajes caben
    objs = list(C["objetivos"])
    combos = [[o] for o in objs] + [objs[k:k + 3] for k in range(0, len(objs), 3)] + [[objs[-1], objs[0], objs[1]]]
    for combo in combos:
        enviados = {o: [] for o in combo}
        for d in range(1, DIAS + 1):
            ms = mensajes(C, S, dict(nombre="Ana", objetivos=combo, alergias=["mani"], codigo="prueba"), d)
            if sum(1 for m in ms if m["envio"] in ("manana", "tarde")) > 2 + (d == 1): errores.append(f"{combo} día {d}: más de dos envíos de consejos")
            for m in ms:
                textos.append((f"{'+'.join(combo)} día {d}", m["texto"]))
                if m["botones"] and len(m["texto"]) > MAX_TEXTO_BOTONES: errores.append(f"{combo} día {d}: un mensaje con botones pasa de {MAX_TEXTO_BOTONES} caracteres")
                if len(m["texto"]) > MAX_TEXTO: errores.append(f"{combo} día {d}: un mensaje pasa de {MAX_TEXTO} caracteres")
                for o in combo:
                    enviados[o] += [c["id"] for c in S["por_objetivo"][o]["consejos"] if c["texto"] in m["texto"]]
        for o in combo:
            if sorted(enviados[o]) != sorted(c["id"] for c in S["por_objetivo"][o]["consejos"]): errores.append(f"{combo}: no salen todos los consejos de {o}, o alguno sale dos veces")
    for ubic, p in control_salida.revisar_todo(textos):
        errores.append(f"control de salida, {ubic}: {p['motivo']} «{p['fragmento']}»")
    return errores


def vista(C, S):
    """Semanas de ejemplo con 3 objetivos (cada objetivo aparece en alguna), una con uno solo y una con alergias."""
    personas = [
        dict(nombre="Ana María", objetivos=["maraton", "masa_muscular", "energia_sueno"], alergias=[], codigo="ej0001"),
        dict(nombre="Carlos", objetivos=["bajar_peso", "prevenir", "salud_general"], alergias=[], codigo="ej0002"),
        dict(nombre="Lucía", objetivos=["envejecer_saludable", "condicion_existente", "atletico"], alergias=[], codigo="ej0003"),
        dict(nombre="Andrés", objetivos=["rendimiento", "energia_sueno", "bajar_peso"], alergias=[], codigo="ej0004"),
        dict(nombre="Valentina", objetivos=["maraton"], alergias=[], codigo="ej0005"),
        dict(nombre="Paula", objetivos=["bajar_peso", "energia_sueno", "salud_general"], alergias=["mani", "lactosa", "huevo"], codigo="ej0099"),
    ]
    semanas = []
    for p in personas:
        pl, objs = plan(C, p), objetivos_persona(C, p["objetivos"])
        dias = []
        for d in range(1, DIAS + 1):
            r = next(y for y in C["catalogo"] if y["id"] == pl["plan"][d - 1]["receta_id"])
            dias.append(dict(dia=d, receta=dict(id=r["id"], nombre=r["nombre"], tiempo_comida=r["tiempo_comida"], etiquetas=r["etiquetas_calculadas"], alergenos=r["alergenos"]),
                             mensajes=mensajes(C, S, p, d, pl["plan"])))
        semanas.append(dict(persona=p, objetivos_nombre=[C["objetivos"][o]["nombre"] for o in objs], familia=familia(S, objs[0]),
                            recetas_aptas=pl["aptas"], recetas_total=pl["total"], dias=dias))
    return dict(horarios=S["horarios"], dias_cortisol=S["dias_cortisol"], dia_1=S["dia_1"], anticipo_valor=S["anticipo_valor"], plantillas=S["plantillas"], semanas=semanas,
                consejos={k: [dict(id=c["id"], tema=c["tema"], respaldo=c["respaldo"], turno=c["turno"], texto=c["texto"]) for c in v["consejos"]] for k, v in S["por_objetivo"].items()},
                cortisol={k: v["cortisol"]["texto"] for k, v in S["por_objetivo"].items()}, cortisol_general=S["cortisol_general"],
                ganchos=S["ganchos"], preguntas_receta=S["preguntas_receta"], familias=S["familias"], cierre_botones=S["cierre_botones"],
                respuesta_boton=S["respuesta_boton"], respuesta_interes=S["respuesta_interes"], botones_interes=S["botones_interes"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--validar", action="store_true")
    ap.add_argument("--vista")
    a = ap.parse_args()
    C, S = cargar()
    if a.validar:
        errs = validar(C, S)
        for e in errs: print("✗", e)
        print(f"{len(errs)} errores")
        sys.exit(1 if errs else 0)
    if a.vista:
        json.dump(vista(C, S), open(a.vista, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("vista en", a.vista)
