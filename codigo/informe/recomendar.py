"""
Saludly Brain · Selección y orden de recomendaciones (documento 07, sección 07.4)

1. Primero las ligadas a hallazgos de escalamiento 2 o 3, sin importar el objetivo.
2. Después las que sirven al primer objetivo y a un hallazgo; luego las de los otros objetivos.
3. Al final los hábitos generales.
4. Si un objetivo deportivo choca con un hallazgo de escalamiento 2 o más, la actividad intensa espera a la consulta.
El objetivo nunca cambia hallazgos ni alertas: solo el orden.
5. Las alergias, el tipo de dieta y los medicamentos del perfil (knowledge_base/fase5/filtros.yaml) entran como
   referencias "alergia:x", "dieta:x" y "medicamento:x": activan o excluyen recomendaciones como cualquier hallazgo.
"""
DEPORTIVOS = ("masa_muscular", "rendimiento", "maraton", "atletico")


def referencias_activas(motor_out):
    """Hallazgos y valores que pueden activar recomendaciones."""
    refs, esc = set(), {}
    for k, v in motor_out["condiciones"].items():
        if v["estado"] in ("activa", "apoyo", "control", "vigilar"):
            refs.add(k); esc[k] = v.get("escalamiento") or 0
            if v.get("estado_hb"):                     # estado específico, por ejemplo COND-M4-IN-002#susceptible
                refs.add(f"{k}#{v['estado_hb']}"); esc[f"{k}#{v['estado_hb']}"] = v.get("escalamiento") or 0
    for k, v in motor_out["relaciones"].items():
        if v["estado"] in ("activa", "vigilar"):
            refs.add(k); esc[k] = v.get("escalamiento") or 0
    for k, v in motor_out["seguridad"].items():
        if v.get("escalamiento"):
            refs.add(k); esc[k] = v["escalamiento"]
    for r in motor_out.get("resultados", []):
        if r.get("biomarker_id") and not r.get("campo") and r.get("clase"):
            refs.add(f"{r['biomarker_id']}:{r['clase']}")
    for g in motor_out["hallazgos_informe"]:
        esc[g["id"]] = max(esc.get(g["id"], 0), g.get("escalamiento") or 0)
        for m in g.get("miembros") or []: esc[m] = max(esc.get(m, 0), g.get("escalamiento") or 0)
    return refs, esc


def referencias_perfil(perfil):
    """Respuestas de la PWA sobre alergias, dieta y medicamentos, como referencias."""
    p = perfil or {}
    refs = {f"alergia:{a}" for a in p.get("alergias") or []} | {f"medicamento:{m}" for m in p.get("medicamentos") or []}
    if p.get("dieta") in ("vegetariana", "vegana"): refs.add(f"dieta:{p['dieta']}")
    return refs


def seleccionar(catalogo, motor_out, objetivos, maximo=14, sexo=None, perfil=None, consulta_si=None):
    refs, esc = referencias_activas(motor_out)
    refs |= {"general"} | {f"objetivo:{o}" for o in objetivos} | referencias_perfil(perfil)
    dieta = (perfil or {}).get("dieta")
    esc_max = max([e for k, e in esc.items() if k.startswith(("COND", "REL", "SEG"))] + [0])
    elegidas = []
    for r in catalogo:
        activadores = [x for x in r.get("se_activa_con") or [] if x in refs]
        if not activadores: continue
        if any(x in refs for x in r.get("contraindicada_si") or []): continue
        e_hall = max([esc.get(x, 0) for x in activadores if x.startswith(("COND", "REL", "SEG"))] + [0])
        ligada = any(x.startswith(("COND", "REL", "SEG")) or ":" in x and not x.startswith("objetivo:") for x in activadores)
        prioridad = [o for o in r.get("prioriza_objetivos") or [] if o in objetivos]
        if e_hall >= 2 or any(x.startswith("medicamento:") for x in activadores): nivel = 0     # las de seguridad por medicamento van primero
        elif ligada and objetivos and objetivos[0] in prioridad: nivel = 1
        elif ligada: nivel = 2
        elif prioridad: nivel = 3 + min(objetivos.index(p) for p in prioridad)
        else: nivel = 6
        consulta = bool(r.get("requiere_consulta_previa"))
        choque = r.get("tipo") == "actividad" and esc_max >= 2 and any(o in DEPORTIVOS for o in (r.get("prioriza_objetivos") or [])) and any(o in DEPORTIVOS for o in objetivos)
        if choque: consulta = True
        if any(x in refs for x in (consulta_si or {}).get(r["id"]) or []): consulta = True     # por ejemplo, ejercicio intenso con insulina
        v = (r.get("por_sexo") or {}).get(sexo) or {}         # texto propio para hombre o mujer, si la recomendación lo trae
        v = {**v, **((r.get("por_dieta") or {}).get(dieta) or {})}     # y texto propio para la dieta vegana
        elegidas.append(dict(recomendacion_id=r["id"], tipo=r["tipo"], titulo=r["titulo"], texto=v.get("texto_base", r["texto_base"]), meta=v.get("meta_concreta", r.get("meta_concreta")),
                             por_que=r.get("por_que"), hallazgos=[x for x in activadores if x.startswith(("COND", "REL", "SEG"))],
                             objetivos=prioridad, requiere_consulta_previa=consulta, _activadores=activadores, whatsapp=v.get("whatsapp", r.get("whatsapp")),
                             _orden=(nivel, -e_hall, -len(activadores), r["id"])))
    elegidas.sort(key=lambda x: x["_orden"])
    # 1) Cada hallazgo del informe tiene al menos su mejor recomendación
    informe = [m for g in motor_out["hallazgos_informe"] for m in [g["id"]] + (g.get("miembros") or [])]
    final, vistos = [], set()
    for h in informe:
        # primero la recomendación del estado específico (por ejemplo, vacuna si es susceptible a hepatitis B)
        especifica = next((x for x in elegidas if any(y.startswith(h + "#") for y in x["hallazgos"])), None)
        if especifica and especifica["recomendacion_id"] not in vistos:
            final.append(especifica); vistos.add(especifica["recomendacion_id"]); continue
        if any(h in x["hallazgos"] or any(y.split("#")[0] == h for y in x["hallazgos"]) for x in final): continue
        mejor = next((x for x in elegidas if x["recomendacion_id"] not in vistos and any(y.split("#")[0] == h for y in x["hallazgos"])), None)
        if mejor: final.append(mejor); vistos.add(mejor["recomendacion_id"])
    # 1b) Las que activa un medicamento son de seguridad: entran siempre
    for x in elegidas:
        if x["recomendacion_id"] not in vistos and any(y.startswith("medicamento:") for y in x["_activadores"]):
            final.append(x); vistos.add(x["recomendacion_id"])
    # 2) Se completa en orden de prioridad, sin repetir el mismo tipo más de 4 veces fuera de las urgentes
    por_tipo = {}
    for x in final: por_tipo[x["tipo"]] = por_tipo.get(x["tipo"], 0) + 1
    limite = max(maximo, len(final) + 4)
    for x in elegidas:
        if len(final) >= limite: break
        if x["recomendacion_id"] in vistos: continue
        if por_tipo.get(x["tipo"], 0) >= 4 and x["_orden"][0] > 0: continue
        por_tipo[x["tipo"]] = por_tipo.get(x["tipo"], 0) + 1
        final.append(x); vistos.add(x["recomendacion_id"])
    final.sort(key=lambda x: x["_orden"])
    for x in final:
        x.pop("_orden"); x.pop("_activadores")
        if x["requiere_consulta_previa"] and not x["texto"].lower().startswith("antes"):
            x["texto"] = "Antes de empezar, coméntalo con tu médico. " + x["texto"]
    return final


def hallazgos_sin_recomendacion(final, motor_out):
    """Hallazgos del informe que se quedaron sin recomendación (por ejemplo, porque un filtro de alergia las quitó todas)."""
    cubiertos = {y.split("#")[0] for x in final for y in x["hallazgos"]}
    return [g["id"] for g in motor_out["hallazgos_informe"] if g["id"] not in cubiertos and not cubiertos & set(g.get("miembros") or [])]
