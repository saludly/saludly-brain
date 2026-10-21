"""
Saludly Brain · Redacción del informe (Fase 5, versión con plantillas)

Toma la salida del motor y arma el informe para el dashboard (contrato del documento 10.5, ampliado) y los
mensajes de WhatsApp. Los textos salen de knowledge_base/fase5 (redacción por hallazgo, recomendaciones y
recetas) y pasan todos por el control de salida. Más adelante DeepSeek puede volverlos más naturales, pero
el contenido y las decisiones siguen siendo los del motor y de las plantillas.
"""
import hashlib, re
import control_salida as CS
import nutricion as NU
import recomendar as RE

PLAZOS = {3: "El equipo médico de Saludly te va a llamar hoy. Tu informe se publica después de esa llamada.",
          2: "Pide una consulta médica en las próximas 2 a 4 semanas y lleva este informe.",
          1: "Coméntalo con tu médico en tu próximo control, en los próximos 3 meses.",
          0: None}
NIVEL_TXT = {"resultado_observado": "Resultado observado", "patron_compatible": "Patrón compatible", "riesgo_potencial": "Riesgo potencial",
             "condicion_requiere_evaluacion": "Requiere evaluación médica"}
SEROLOGIAS = ("COND-M4-IN-001", "COND-M4-IN-002", "COND-M4-IN-003")


def _num(v):
    if isinstance(v, (int, float)):
        s = f"{v:.2f}".rstrip("0").rstrip(".") if not float(v).is_integer() else f"{int(v)}"
        return s.replace(".", ",")
    return str(v)


CONTEXTO_VISIBLE = {"presion_sistolica": "mmHg", "presion_diastolica": "mmHg", "cintura_cm": "cm", "peso_kg": "kg", "talla_m": "m"}


def valores(motor_out, indice, ctx=None):
    out = {}
    for k, uni in CONTEXTO_VISIBLE.items():            # medidas de la enfermera
        if (ctx or {}).get(k) is not None: out[k] = f"{_num(ctx[k])} {uni}"
    if (ctx or {}).get("presion_sistolica") is not None and (ctx or {}).get("presion_diastolica") is not None:
        out["presion"] = f"{_num(ctx['presion_sistolica'])}/{_num(ctx['presion_diastolica'])} mmHg"
    for r in motor_out.get("resultados", []):
        b = r.get("biomarker_id")
        if not b or r.get("campo") or r.get("valor") is None: continue
        op = {"<": "menor de ", ">": "mayor de "}.get(r.get("operador"), "")
        out[b] = f"{op}{_num(r['valor'])} {r.get('unidad') or ''}".strip()
    for k, v in (motor_out.get("calculados") or {}).items():
        if v is None: continue
        uni = (indice["biomarcadores"].get(k) or {}).get("unidad") or ""
        if k == "hemoglobina_ajustada": uni = "g/dL"
        if k == "egfr": uni = "mL/min/1,73 m²"
        if uni in ("sin unidad",) or "sin unidad" in uni: uni = ""
        out.setdefault(k, f"{_num(v)} {uni}".strip())
    return out


def rellenar(frases, vals, clases=None):
    """Reemplaza {biomarcador} por su valor y omite la frase si falta alguno.
    Con 'clases', descarta además las frases cuyos valores están todos en rango (por ejemplo, en una regla que cubre
    varios biomarcadores solo se nombran los alterados); si eso las quita todas, se dejan las originales."""
    completas = []
    for f in frases or []:
        marcas = re.findall(r"\{([^}]+)\}", f)
        if any(m not in vals for m in marcas): continue
        completas.append((f, marcas))
    if clases is not None:
        alteradas = [(f, m) for f, m in completas if not m or any(clases.get(x) not in ("en_rango",) for x in m)]
        if alteradas: completas = alteradas
    return [re.sub(r"\{([^}]+)\}", lambda m: vals[m.group(1)], f) for f, _ in completas]


def clases_con_criterios(clases, criterios, cnd):
    """Los valores calculados (no-HDL, HOMA-IR…) no traen clase del laboratorio: se toma la de la regla.
    Si el criterio de la ficha se cumplió, cuenta como alterado; si no, como en rango."""
    if not criterios or not cnd: return clases
    cumplidos = set(cnd.get("criterios_cumplidos") or [])
    alterados = {b for cid, b in criterios.items() if cid in cumplidos}
    extra = {b: ("alto" if b in alterados else "en_rango") for b in criterios.values() if b not in clases}
    return dict(clases, **extra) if extra else clases


def texto_de(red, hid, cond=None):
    """Texto del hallazgo; si la ficha trae variantes por estado (por ejemplo, hepatitis B), aplica la del estado del motor."""
    t = red.get(hid)
    if not t: return None
    est = (cond or {}).get("estado_hb")
    v = (t.get("variantes") or {}).get(est) if est else None
    return dict(t, **v) if v else t


def _ids_del_grupo(g): return [g["id"]] + [m for m in g.get("miembros") or []]


def armar(motor_out, ctx, objetivos, C, paciente_ref, dias_recetas=7):
    idx, red = C["indice"], C["redaccion"]
    vals = valores(motor_out, idx, ctx)
    clases = {r["biomarker_id"]: r.get("clase") for r in motor_out.get("resultados", []) if r.get("biomarker_id") and not r.get("campo")}
    hall = motor_out["hallazgos_informe"]
    faltan_textos = []

    # ---------- Lo que merece atención (y qué podría significar)
    atencion, significado, buenas_noticias = [], [], []
    for n, g in enumerate(hall, 1):
        cnd = motor_out["condiciones"].get(g["id"]) or {}
        t = texto_de(red, g["id"], cnd)
        if not t:
            faltan_textos.append(g["id"]); continue
        if cnd.get("estado_hb") == "inmune_por_vacuna":          # una buena noticia va en "lo que está bien"
            buenas_noticias.append(dict(grupo=g["id"], nombre=t["titulo_paciente"], texto=" ".join(rellenar(t.get("por_que_te_aparece"), vals)) or t["titulo_paciente"]))
            continue
        hid = f"H-{paciente_ref[-6:]}-{n:02d}"
        g["hallazgo_id"] = hid
        crit = C.get("criterios") or {}
        por_que = rellenar(t.get("por_que_te_aparece"), vals, clases_con_criterios(clases, crit.get(g["id"]), cnd))
        usados = set(re.findall(r"\{([^}]+)\}", " ".join(t.get("por_que_te_aparece") or [])))
        for m in g.get("miembros") or []:                       # un patrón también explica sus condiciones, sin repetir valores
            tm = red.get(m)
            if not tm: continue
            cm = clases_con_criterios(clases, crit.get(m), motor_out["condiciones"].get(m))
            for f in tm.get("por_que_te_aparece") or []:
                marcas = set(re.findall(r"\{([^}]+)\}", f))
                if marcas and marcas & usados: continue
                x = rellenar([f], vals, cm)
                if x and x[0] not in por_que:
                    por_que.append(x[0]); usados |= marcas; break
        atencion.append(dict(hallazgo_id=hid, referencia=g["id"], tipo=g["tipo"], titulo=t["titulo_paciente"], escalamiento=g.get("escalamiento") or 0,
                             nivel_lenguaje=NIVEL_TXT.get(g.get("nivel_lenguaje") or "", None), coincidencia=g.get("coincidencia"),
                             que_es=t["que_es"], por_que=por_que, ejemplo=t["ejemplo_simple"],
                             agrupa=[dict(referencia=m, titulo=(red.get(m) or {}).get("titulo_paciente")) for m in g.get("miembros") or []]))
        significado.append(dict(hallazgo_id=hid, texto=t["riesgo_claro"], incertidumbre=t["incertidumbre"]))

    # ---------- Informativos (por ejemplo, transición a la menopausia)
    informativos = []
    for x in motor_out.get("informativos_paciente") or []:
        t = red.get(x["id"])
        if t: informativos.append(dict(referencia=x["id"], titulo=t["titulo_paciente"], que_es=t["que_es"], por_que=rellenar(t.get("por_que_te_aparece"), vals), texto=t["riesgo_claro"]))
        else: faltan_textos.append(x["id"])

    # ---------- Lo que está bien
    bien = list(buenas_noticias)
    for m in C["modulos"]:
        medidos = [b for b in m.get("biomarcadores", []) if b in clases]
        if medidos and all(clases[b] in ("en_rango", None) for b in medidos) and any(clases[b] == "en_rango" for b in medidos):
            bien.append(dict(grupo=m["id"], nombre=m.get("nombre"), texto=m["texto_bien"]))

    # ---------- Qué puedes hacer
    perfil_fil = {k: (ctx or {}).get(k) for k in ("alergias", "dieta", "medicamentos")}
    recs = RE.seleccionar(C["recomendaciones"], motor_out, objetivos, sexo=(ctx or {}).get("sexo"), perfil=perfil_fil,
                          consulta_si=(C.get("filtros") or {}).get("consulta_previa_si"))

    # ---------- Cuándo consultar
    consultar = {}
    for a in atencion:
        e = a["escalamiento"]; t = texto_de(red, a["referencia"], motor_out["condiciones"].get(a["referencia"])) or {}
        texto = t.get("cuando_consultar") or PLAZOS.get(e)
        if not texto: continue
        c = consultar.setdefault(e, dict(escalamiento=e, texto=PLAZOS.get(e) or texto, hallazgos=[]))
        c["hallazgos"].append(dict(hallazgo_id=a["hallazgo_id"], titulo=a["titulo"], detalle=t.get("cuando_consultar")))
    cuando = [consultar[e] for e in sorted(consultar, reverse=True)]

    # ---------- Resumen
    esc_max = motor_out["escalamiento_maximo"]
    n_at = len(atencion)
    nombres_obj = [C["objetivos"][o]["nombre"].lower() for o in objetivos if o in C["objetivos"]]
    if n_at == 0:
        resumen = "Tus resultados están dentro de los rangos de referencia en lo que revisamos. Te dejamos ideas para mantenerte así."
    else:
        principal = atencion[0]["titulo"].lower()
        resumen = (f"Revisamos tus resultados y encontramos {n_at} {'punto' if n_at == 1 else 'puntos'} que vale la pena atender; "
                   f"el más importante es: {principal}. ")
        resumen += {3: "Nuestro equipo médico te va a llamar hoy para hablarlo.", 2: "Te recomendamos una consulta médica en las próximas semanas.",
                    1: "Nada requiere urgencia; son cosas para cuidar y comentar en tu próximo control.", 0: "Son cosas para cuidar con hábitos."}[min(esc_max, 3)]
    if bien: resumen += f" También hay buenas noticias: {len(bien)} {'grupo' if len(bien) == 1 else 'grupos'} de resultados están en rango."
    if nombres_obj: resumen += f" Ordenamos las recomendaciones pensando en tus metas: {', '.join(nombres_obj)}."

    # ---------- Nutrición y recetas
    cat = NU.catalogo(C["recetas"], C["alimentos"])
    restr = NU.restricciones(motor_out, ctx)
    meta = NU.metas(ctx, objetivos, motor_out)
    plan = NU.plan_recetas(cat, restr, objetivos, paciente_ref, dias_recetas)
    por_id = {r["id"]: r for r in cat}
    recetas_msg = [dict(dia=p["dia"], receta_id=p["receta_id"], texto=NU.mensaje_receta(por_id[p["receta_id"]], C["alimentos"], meta)) for p in plan["plan"]]

    # ---------- WhatsApp (documento 05.3 y 06.7)
    # Escalamiento 3 o serología reactiva (el motor las pone en "llamadas"): nada sale hasta que el equipo médico llame (documento 05.3)
    retenido = esc_max >= 3 or bool(motor_out.get("llamadas"))
    wa = dict(resultado_listo=None, recordatorio_consulta=None, recomendaciones_semanales=[], recetas_diarias=[] if retenido else recetas_msg)   # retenido: nada sale hasta la llamada
    if not retenido:
        wa["resultado_listo"] = "Hola 👋 Tus resultados de Saludly ya están listos en tu panel. Ábrelo cuando puedas: ahí te explicamos todo con calma."
        if esc_max == 2:
            wa["recordatorio_consulta"] = "Hola 👋 En tu informe de Saludly hay un resultado que conviene revisar con un médico en las próximas semanas. Abre tu panel para ver el detalle."
        wa["recomendaciones_semanales"] = [dict(semana=i + 1, recomendacion_id=r["recomendacion_id"], texto=r["whatsapp"]) for i, r in enumerate([r for r in recs if r.get("whatsapp") and not r["requiere_consulta_previa"]][:8])]

    # ---------- Vista médica
    vm = motor_out["vista_medica"]
    confirmar = [f"{(red.get(a['referencia']) or {}).get('titulo_paciente') or a['referencia']}: coincidencia {a['coincidencia']}, confirmar con una segunda medición."
                 for a in atencion if a.get("coincidencia") in ("moderada", "baja")]
    preguntas = [f"¿Conviene confirmar o descartar «{a['titulo']}» ({a['referencia']}) y en qué plazo?" for a in atencion if a["escalamiento"] >= 2]
    medico = dict(hallazgos=[dict(g, texto_paciente=(red.get(g["id"]) or {}).get("titulo_paciente")) for g in hall],
                  condiciones=motor_out["condiciones"], relaciones={k: v for k, v in motor_out["relaciones"].items() if v["estado"] != "no_activa"},
                  seguridad={k: v for k, v in motor_out["seguridad"].items() if v.get("escalamiento") or v.get("detalle")},
                  vigilar=vm.get("vigilar"), apoyos=vm.get("apoyos"), reflejas_pendientes=vm.get("pendientes_refleja"), incompletas=vm.get("incompletas"),
                  pausadas_mvp=vm.get("pausadas_mvp"), evaluadas_parcialmente=vm.get("evaluadas_parcialmente"), no_interpretables=vm.get("no_interpretables"),
                  datos_faltantes=vm.get("datos_faltantes"), dudas_lectura=vm.get("dudas_lectura"), revision_medica_obligatoria=vm.get("revision_medica_obligatoria"),
                  que_conviene_confirmar=confirmar, preguntas_para_el_profesional=preguntas, restricciones_nutricionales=restr,
                  alergias_dieta_medicamentos=dict(perfil_fil, alergias_otras=(ctx or {}).get("alergias_otras"),
                                                   hallazgos_sin_recomendacion=RE.hallazgos_sin_recomendacion(recs, motor_out)))

    # ---------- Todos mis resultados
    resultados = []
    for r in motor_out.get("resultados", []):
        b = r.get("biomarker_id")
        if not b or r.get("campo"): continue
        info = idx["biomarcadores"].get(b) or {}
        resultados.append(dict(biomarker_id=b, nombre=info.get("nombre") or r.get("nombre_original"), valor=r.get("valor"), valor_original=r.get("valor_original"),
                               unidad=r.get("unidad"), intervalo=(r.get("intervalo_lab") or {}).get("texto"), clase=r.get("clase"), estado=r.get("estado"),
                               motivo=r.get("motivo_clase") if r.get("clase") == "no_interpretable" else None, seccion=r.get("seccion"), refleja=r.get("refleja")))

    # ---------- Aviso de alergias y dieta
    nombres_ale = {o["id"]: o["texto"].split(" (")[0].lower() for o in ((C.get("filtros") or {}).get("preguntas", {}).get("alergias", {}).get("opciones") or [])}
    partes = [nombres_ale.get(a, a) for a in perfil_fil.get("alergias") or []]
    nota_alimentacion = None
    if partes or perfil_fil.get("dieta") in ("vegetariana", "vegana"):
        que = []
        if partes: que.append("tu alergia o intolerancia a " + ", ".join(partes))
        if perfil_fil.get("dieta") in ("vegetariana", "vegana"): que.append(f"tu alimentación {perfil_fil['dieta']}")
        nota_alimentacion = (f"Tus recetas ya tienen en cuenta {' y '.join(que)}. "
                             "Si alguna recomendación nombra un alimento que no comes entre varias opciones, elige otra de la lista.")

    paciente = dict(resumen=resumen, nota_alimentacion=nota_alimentacion, lo_que_esta_bien=bien, lo_que_merece_atencion=atencion, que_podria_significar=significado,
                    que_puedes_hacer=[{k: v for k, v in r.items() if k != "whatsapp"} for r in recs], cuando_consultar=cuando, informativos=informativos)

    # ---------- Control de salida sobre todo lo que ve o recibe el paciente
    textos = [("resumen", resumen)] + ([("nota_alimentacion", nota_alimentacion)] if nota_alimentacion else [])
    for sec in ("lo_que_esta_bien", "que_podria_significar", "que_puedes_hacer", "cuando_consultar", "informativos"):
        for i, x in enumerate(paciente[sec]):
            for k in ("texto", "incertidumbre", "titulo", "meta", "por_que", "que_es"):
                if isinstance(x.get(k), str): textos.append((f"{sec}[{i}].{k}", x[k]))
    for i, a in enumerate(atencion):
        for k in ("titulo", "que_es", "ejemplo"): textos.append((f"lo_que_merece_atencion[{i}].{k}", a[k]))
        for j, f in enumerate(a["por_que"]): textos.append((f"lo_que_merece_atencion[{i}].por_que[{j}]", f))
    for k in ("resultado_listo", "recordatorio_consulta"):
        if wa[k]: textos.append((f"whatsapp.{k}", wa[k]))
    for x in wa["recomendaciones_semanales"]: textos.append((f"whatsapp.semana{x['semana']}", x["texto"]))
    for x in wa["recetas_diarias"]: textos.append((f"whatsapp.receta_dia{x['dia']}", x["texto"]))
    problemas = [dict(ubicacion=u, **p) for u, p in CS.revisar_todo(textos)]

    estado = "retenido_hasta_llamada" if retenido else ("requiere_revision" if problemas or faltan_textos else "en_revision")
    return dict(paciente=paciente, medico=medico, resultados=resultados, informativos=informativos,
                nutricion=dict(meta_diaria=meta, restricciones=restr, recetas_aptas=plan["aptas"], recetas_total=plan["total"], plan=plan["plan"]),
                whatsapp=wa, control_salida=dict(ok=not problemas and not faltan_textos, problemas=problemas, hallazgos_sin_texto=faltan_textos),
                estado=estado)
