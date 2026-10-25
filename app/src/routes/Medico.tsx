import { useCallback, useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Marca } from "@/components/Comunes";
import { Preregistros } from "@/components/Preregistros";
import { Conversaciones } from "@/components/Conversaciones";
import { PLAZO, SUAVE, estadoDeEscalamiento, fechaLarga } from "@/lib/datos";
import { useInforme } from "@/lib/contexto";
import { supabase, useSesion } from "@/lib/sesion";
import type { Informe } from "@/lib/informe";

/**
 * Vista del médico revisor y de administración (solo para correos en la tabla `equipo`).
 * Lista los pacientes del piloto con su avance; abre cada informe para revisarlo, verlo como el paciente y aprobarlo.
 * "Subir resultado" manda el PDF del laboratorio a /api/procesar (función de Vercel: lector → motor → informe en revisión).
 * Aprobar avisa al paciente por WhatsApp con la función avisar-resultados de Supabase.
 */
interface Fila {
  id: string;
  nombre: string;
  edad: number;
  sexo: string;
  celular_whatsapp: string;
  cuestionario: boolean;
  visita: boolean;
  informe: { id: number; orden: string; estado: string; creado: string; aprobado: string | null; avisado: string | null } | null;
  pago: { codigo: string; estado: string; comprobante: string | null; comprobante_recibido: string | null } | null;
}

const PAGO: Record<string, string> = { pendiente: "Pago pendiente", comprobante: "Pago por confirmar", confirmado: "Pago confirmado", rechazado: "Pago rechazado" };

const ESTADO: Record<string, string> = { en_revision: "En revisión", aprobado: "Aprobado", retenido: "Retenido: llamar" };

function Chip({ ok, texto }: { ok: boolean; texto: string }) {
  return <span className={`rounded-full px-2 py-0.5 text-[10px] uppercase tracking-[0.1em] ${ok ? "bg-optimal-soft text-optimal" : "bg-surface text-ink-faint"}`}>{texto}</span>;
}

/** Lista de la vista médica: acepta textos u objetos (se muestran como texto legible). */
function Lista({ titulo, items }: { titulo: string; items: unknown }) {
  const arr = Array.isArray(items) ? items : items && typeof items === "object" ? Object.entries(items as object).map(([k, v]) => `${k}: ${typeof v === "string" ? v : JSON.stringify(v)}`) : [];
  if (!arr.length) return null;
  return (
    <section className="mt-6">
      <h3 className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">{titulo}</h3>
      <ul className="mt-2 space-y-1.5 text-sm leading-relaxed text-ink">
        {arr.map((x, i) => (
          <li key={i}>· {typeof x === "string" ? x : JSON.stringify(x)}</li>
        ))}
      </ul>
    </section>
  );
}

/**
 * Subir el PDF del laboratorio: se analiza en el servidor y queda "en revisión". El PDF no se guarda.
 * La orden y el documento se leen del PDF; sin `fila`, el servidor busca al paciente por el documento.
 */
function SubirResultado({ fila, alTerminar }: { fila?: Fila; alTerminar: () => void }) {
  const s = useSesion();
  const [archivo, setArchivo] = useState<File | null>(null);
  const [forzar, setForzar] = useState(false);
  const [documentoPrueba, setDocumentoPrueba] = useState("");
  const [ocupado, setOcupado] = useState(false);
  const [mensaje, setMensaje] = useState<{ ok: boolean; texto: string } | null>(null);

  const enviar = async () => {
    if (!archivo) return;
    setOcupado(true);
    setMensaje(null);
    const bytes = new Uint8Array(await archivo.arrayBuffer());
    let binario = "";
    for (let i = 0; i < bytes.length; i += 0x8000) binario += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
    try {
      const r = await fetch("/api/procesar", {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${s.sesion?.access_token}` },
        body: JSON.stringify({ paciente_id: fila?.id ?? null, pdf_base64: btoa(binario), forzar, documento_pdf: documentoPrueba.trim() || null }),
      });
      const d = (await r.json().catch(() => ({}))) as { error?: string; estado?: string; avisos?: string[] };
      if (!r.ok) setMensaje({ ok: false, texto: d.error ?? "No se pudo analizar el PDF." });
      else {
        setMensaje({ ok: true, texto: `Listo: el informe quedó ${ESTADO[d.estado ?? ""]?.toLowerCase() ?? d.estado}.${d.avisos?.length ? ` Avisos: ${d.avisos.join(" ")}` : ""}` });
        alTerminar();
      }
    } catch {
      setMensaje({ ok: false, texto: "No hubo conexión con el servidor. Intenta de nuevo." });
    }
    setOcupado(false);
  };

  return (
    <div className="mt-4 w-full space-y-3 rounded-2xl bg-surface p-4">
      <label className="block text-xs text-ink-muted">
        PDF del laboratorio
        <input type="file" accept="application/pdf" onChange={(e) => setArchivo(e.target.files?.[0] ?? null)} className="mt-1 block w-full text-sm text-ink" />
      </label>
      <p className="text-xs text-ink-faint">El número de orden y el documento se leen del PDF{fila ? " y se comparan con este paciente" : "; el paciente se busca por su documento"}.</p>
      {(!fila || !fila.cuestionario || !fila.visita) && (
        <label className="flex items-center gap-2 text-xs text-ink-muted">
          <input type="checkbox" checked={forzar} onChange={(e) => setForzar(e.target.checked)} /> Publicar igual (falta el cuestionario o la visita)
        </label>
      )}
      <details className="text-xs text-ink-faint">
        <summary className="cursor-pointer">Solo para pruebas con PDF de ejemplo</summary>
        <input value={documentoPrueba} onChange={(e) => setDocumentoPrueba(e.target.value)} placeholder="Documento que trae el PDF, p. ej. CC 0000000005" className="mt-2 block w-full rounded-xl border border-rule bg-background px-3 py-2 text-sm text-ink" />
      </details>
      <button type="button" onClick={() => void enviar()} disabled={!archivo || ocupado} className="rounded-full bg-optimal px-5 py-2.5 text-sm text-primary-foreground disabled:opacity-40">
        {ocupado ? "Analizando…" : "Analizar resultado"}
      </button>
      {mensaje && <p className={`text-sm ${mensaje.ok ? "text-optimal" : "text-attention"}`}>{mensaje.texto}</p>}
    </div>
  );
}

/** Comprobantes que llegaron por WhatsApp: se ven aquí y se confirman o rechazan (sale el WhatsApp al paciente). */
function PagosPorConfirmar({ filas, alCambiar }: { filas: Fila[]; alCambiar: () => void }) {
  const pendientes = filas.filter((f) => f.pago?.estado === "comprobante");
  const [urls, setUrls] = useState<Record<string, string>>({});
  const [ocupado, setOcupado] = useState<string | null>(null);
  const [rechazando, setRechazando] = useState<string | null>(null);
  const [nota, setNota] = useState("");

  const rutas = pendientes.map((f) => `${f.id}|${f.pago?.comprobante ?? ""}`).join(",");
  useEffect(() => {
    for (const par of rutas.split(",").filter(Boolean)) {
      const [id, ruta] = par.split("|");
      if (ruta)
        void supabase.storage
          .from("comprobantes")
          .createSignedUrl(ruta, 600)
          .then(({ data }) => data && setUrls((u) => ({ ...u, [id!]: data.signedUrl })));
    }
  }, [rutas]);

  const decidir = async (f: Fila, confirmar: boolean) => {
    setOcupado(f.id);
    await supabase.functions.invoke("confirmar-pago", { body: { paciente_id: f.id, confirmar, nota: confirmar ? null : nota } });
    setOcupado(null);
    setRechazando(null);
    setNota("");
    alCambiar();
  };

  if (!pendientes.length) return null;
  return (
    <section className="mt-6 rounded-3xl border border-attention/40 bg-attention-soft p-5">
      <h2 className="text-lg font-light text-ink">Pagos por confirmar ({pendientes.length})</h2>
      <div className="mt-4 space-y-4">
        {pendientes.map((f) => (
          <article key={f.id} className="flex flex-wrap items-start gap-4 rounded-2xl bg-background p-4">
            {urls[f.id] ? (
              f.pago?.comprobante?.endsWith(".pdf") ? (
                <a href={urls[f.id]} target="_blank" rel="noreferrer" className="rounded-xl border border-rule px-4 py-6 text-sm text-optimal">
                  Ver PDF del comprobante
                </a>
              ) : (
                <a href={urls[f.id]} target="_blank" rel="noreferrer">
                  <img src={urls[f.id]} alt={`Comprobante de ${f.nombre}`} className="h-40 w-auto rounded-xl border border-rule object-contain" />
                </a>
              )
            ) : (
              <div className="h-40 w-28 rounded-xl bg-surface" />
            )}
            <div className="min-w-0 flex-1">
              <p className="text-base text-ink">{f.nombre}</p>
              <p className="text-xs text-ink-muted">
                Código {f.pago?.codigo} · WhatsApp …{f.celular_whatsapp.slice(-4)}
              </p>
              {rechazando === f.id ? (
                <div className="mt-3 flex flex-wrap gap-2">
                  <input value={nota} onChange={(e) => setNota(e.target.value)} placeholder="Motivo (lo verá el paciente)" className="min-w-0 flex-1 rounded-xl border border-rule px-3 py-2 text-sm text-ink" />
                  <button type="button" disabled={ocupado === f.id} onClick={() => void decidir(f, false)} className="rounded-full border border-rule px-5 py-2 text-sm text-ink disabled:opacity-40">
                    Rechazar
                  </button>
                </div>
              ) : (
                <div className="mt-3 flex flex-wrap gap-2">
                  <button type="button" disabled={ocupado === f.id} onClick={() => void decidir(f, true)} className="rounded-full bg-optimal px-5 py-2 text-sm text-primary-foreground disabled:opacity-40">
                    Confirmar pago
                  </button>
                  <button type="button" onClick={() => setRechazando(f.id)} className="rounded-full border border-rule px-5 py-2 text-sm text-ink">
                    Rechazar
                  </button>
                </div>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

/** Datos del pago que ve el paciente (llave Bre-B, valor, titular, WhatsApp de Saludly): se cambian aquí, sin tocar código. */
function ConfigPago() {
  const [abierta, setAbierta] = useState(false);
  const [valores, setValores] = useState<Record<string, string>>({});
  const [guardado, setGuardado] = useState(false);
  const CAMPOS: [string, string, string][] = [
    ["pago_llave_breb", "Llave Bre-B", "Celular, cédula o correo de la llave"],
    ["pago_valor", "Valor del paquete", "$000.000"],
    ["pago_titular", "Titular de la cuenta", "Nombre que verá el paciente"],
    ["whatsapp_saludly", "WhatsApp de Saludly", "Con indicativo, sin +: 57300…"],
    ["anticipo_valor", "Anticipo de la preventa", "$50.000"],
    ["preventa", "Pre-registro activo (si / no)", "si"],
  ];

  useEffect(() => {
    if (abierta)
      void supabase
        .from("configuracion")
        .select("clave, valor")
        .then(({ data }) => setValores(Object.fromEntries((data ?? []).map((x) => [x.clave, x.valor ?? ""]))));
  }, [abierta]);

  const guardar = async () => {
    for (const [k] of CAMPOS) await supabase.from("configuracion").update({ valor: valores[k]?.trim() || null, actualizado: new Date().toISOString() }).eq("clave", k);
    setGuardado(true);
  };

  return (
    <section className="mt-4">
      <button type="button" onClick={() => setAbierta((x) => !x)} className="text-sm text-optimal underline-offset-4 hover:underline">
        {abierta ? "Cerrar datos de pago" : "Datos de pago y preventa (llave Bre-B, valores)"}
      </button>
      {abierta && (
        <div className="mt-3 grid gap-3 rounded-2xl bg-surface p-4 sm:grid-cols-2">
          {CAMPOS.map(([k, l, ph]) => (
            <label key={k} className="block text-xs text-ink-muted">
              {l}
              <input
                value={valores[k] ?? ""}
                placeholder={ph}
                onChange={(e) => {
                  setGuardado(false);
                  setValores((v) => ({ ...v, [k]: e.target.value }));
                }}
                className="mt-1 block w-full rounded-xl border border-rule bg-background px-3 py-2 text-sm text-ink"
              />
            </label>
          ))}
          <div className="flex items-center gap-3 sm:col-span-2">
            <button type="button" onClick={() => void guardar()} className="rounded-full bg-optimal px-5 py-2 text-sm text-primary-foreground">
              Guardar
            </button>
            {guardado && <span className="text-xs text-optimal">Guardado. El paciente ya ve los datos nuevos.</span>}
          </div>
        </div>
      )}
    </section>
  );
}

function Revision({ fila, alVolver }: { fila: Fila; alVolver: () => void }) {
  const s = useSesion();
  const { revisar } = useInforme();
  const navigate = useNavigate();
  const [inf, setInf] = useState<Informe | null>(null);
  const [estado, setEstado] = useState(fila.informe?.estado ?? "");
  const [ocupado, setOcupado] = useState(false);

  useEffect(() => {
    if (!fila.informe) return;
    void supabase.from("informes").select("informe").eq("id", fila.informe.id).single().then(({ data }) => setInf((data?.informe as Informe) ?? null));
  }, [fila]);

  const aprobar = async () => {
    setOcupado(true);
    const { error } = await supabase
      .from("informes")
      .update({ estado: "aprobado", aprobado: new Date().toISOString(), aprobado_por: s.sesion?.user.email })
      .eq("id", fila.informe!.id);
    if (!error) {
      setEstado("aprobado");
      // Aviso por WhatsApp con la plantilla resultados_listos (la función revisa que el paciente aceptó WhatsApp).
      await supabase.functions.invoke("avisar-resultados", { body: { informe_id: fila.informe!.id } });
    }
    setOcupado(false);
  };

  if (!inf) return <p className="mt-10 text-sm text-ink-muted">Cargando el informe…</p>;
  const m = inf.medico as Record<string, unknown>;
  const adm = (m.alergias_dieta_medicamentos ?? {}) as Record<string, unknown>;

  return (
    <div className="mt-8">
      <button type="button" onClick={alVolver} className="text-sm text-optimal underline-offset-4 hover:underline">
        ← Todos los pacientes
      </button>
      <div className="mt-4 flex flex-wrap items-baseline justify-between gap-3">
        <h2 className="text-2xl font-light tracking-tight text-ink">
          {fila.nombre} · {inf.perfil.edad ?? fila.edad} años · {inf.perfil.sexo ?? fila.sexo}
        </h2>
        <span className={`rounded-full px-3 py-1 text-[10px] uppercase tracking-[0.14em] ${SUAVE[estadoDeEscalamiento(inf.escalamiento_maximo)]}`}>
          {PLAZO[inf.escalamiento_maximo]}
        </span>
      </div>
      <p className="mt-1 text-sm text-ink-muted">
        Orden {inf.orden} · toma {fechaLarga(inf.fecha_toma)} · {inf.paciente_ref} · {ESTADO[estado] ?? estado}
      </p>

      <Lista titulo="Avisos de la publicación" items={m.avisos_publicacion} />

      <section className="mt-6">
        <h3 className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">Lo que verá como «merece atención»</h3>
        <div className="mt-2 space-y-2">
          {inf.paciente.lo_que_merece_atencion.map((h) => (
            <div key={h.hallazgo_id} className="rounded-xl border border-rule p-3 text-sm">
              <span className="font-mono text-[11px] text-ink-faint">{h.referencia}</span> · <span className="text-ink">{h.titulo}</span>
              <span className="ml-2 text-xs text-ink-muted">
                escalamiento {h.escalamiento}
                {h.nivel_lenguaje ? ` · ${h.nivel_lenguaje}` : ""}
                {h.coincidencia ? ` · coincidencia ${h.coincidencia}` : ""}
              </span>
            </div>
          ))}
        </div>
      </section>

      <Lista titulo="Datos faltantes" items={m.datos_faltantes} />
      <Lista titulo="Dudas de lectura del PDF" items={m.dudas_lectura} />
      <Lista titulo="Qué conviene confirmar" items={m.que_conviene_confirmar} />
      <Lista titulo="Preguntas para el profesional" items={m.preguntas_para_el_profesional} />
      <Lista
        titulo="Alergias, dieta y medicamentos"
        items={[
          `Alergias: ${(adm.alergias as string[] | null)?.join(", ") || "ninguna"}${adm.alergias_otras ? ` · otras: ${adm.alergias_otras}` : ""}`,
          `Dieta: ${adm.dieta ?? "normal"}`,
          `Medicamentos: ${(adm.medicamentos as string[] | null)?.join(", ") || "ninguno de la lista"}`,
          ...(((adm.hallazgos_sin_recomendacion as string[]) ?? []).length ? [`Hallazgos sin recomendación por los filtros: ${(adm.hallazgos_sin_recomendacion as string[]).join(", ")}`] : []),
        ]}
      />
      <Lista
        titulo="Control de salida"
        items={inf.control_salida.ok ? ["Sin problemas en los textos para el paciente."] : inf.control_salida.problemas.map((p) => `${p.ubicacion}: ${p.motivo} («${p.fragmento}»)`)}
      />

      <div className="mt-10 flex flex-wrap gap-3">
        <button
          type="button"
          onClick={() => {
            revisar(inf);
            void navigate({ to: "/recorrido" });
          }}
          className="rounded-full border border-rule px-5 py-3 text-sm text-ink hover:border-ink/25"
        >
          Ver como lo verá el paciente
        </button>
        {estado !== "aprobado" ? (
          <button type="button" onClick={aprobar} disabled={ocupado} className="rounded-full bg-optimal px-6 py-3 text-sm text-primary-foreground disabled:opacity-40">
            {estado === "retenido" ? "Ya lo llamé: aprobar" : "Aprobar informe"}
          </button>
        ) : (
          <span className="rounded-full bg-optimal-soft px-5 py-3 text-sm text-optimal">
            ✓ Aprobado. Para avisarle por WhatsApp: <code className="font-mono">python codigo/whatsapp/avisar.py</code>
          </span>
        )}
      </div>
    </div>
  );
}

export function Medico() {
  const s = useSesion();
  const navigate = useNavigate();
  const [filas, setFilas] = useState<Fila[] | null>(null);
  const [abierta, setAbierta] = useState<Fila | null>(null);
  const [subiendo, setSubiendo] = useState<string | null>(null);  // id del paciente, o "todos" para la carga general
  const [vista, setVista] = useState<"pacientes" | "preregistros" | "conversaciones">("preregistros");

  const cargar = useCallback(async () => {
    const [p, c, v, i, g] = await Promise.all([
      supabase.from("pacientes").select("id,nombre,edad,sexo,celular_whatsapp").order("creado"),
      supabase.from("cuestionarios").select("paciente_id,completo"),
      supabase.from("visitas").select("paciente_id"),
      supabase.from("informes").select("id,paciente_id,orden,estado,creado,aprobado,avisado").order("creado", { ascending: false }),
      supabase.from("pagos").select("paciente_id,codigo,estado,comprobante,comprobante_recibido"),
    ]);
    setFilas(
      (p.data ?? []).map((x) => ({
        ...(x as Omit<Fila, "cuestionario" | "visita" | "informe" | "pago">),
        pago: (g.data?.find((y) => y.paciente_id === x.id) as Fila["pago"]) ?? null,
        cuestionario: !!c.data?.find((y) => y.paciente_id === x.id && y.completo),
        visita: !!v.data?.find((y) => y.paciente_id === x.id),
        informe: (i.data?.find((y) => y.paciente_id === x.id) as Fila["informe"]) ?? null,
      })),
    );
  }, []);

  useEffect(() => {
    if (s.cargando) return;
    if (!s.sesion) void navigate({ to: "/entrar" });
    else if (s.esEquipo) void cargar();
  }, [s.cargando, s.sesion, s.esEquipo, navigate, cargar]);

  // Entró con una cuenta que no es del equipo (por ejemplo, una de prueba): se lo decimos y le dejamos cambiarla.
  if (!s.cargando && s.sesion && !s.esEquipo)
    return (
      <main className="flex min-h-screen items-center justify-center bg-background px-6">
        <div className="max-w-sm text-center">
          <h1 className="text-2xl font-light text-ink">Esta cuenta no tiene acceso al panel.</h1>
          <p className="mt-3 text-sm text-ink-muted">Entraste como {s.sesion.user.email}. El panel es solo para el equipo de Saludly.</p>
          <button type="button" onClick={() => void s.salir().then(() => navigate({ to: "/entrar" }))} className="mt-6 rounded-full bg-optimal px-5 py-2.5 text-sm text-primary-foreground">
            Entrar con otra cuenta
          </button>
        </div>
      </main>
    );

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-5xl px-6 py-8 sm:px-10">
        <Marca derecha="Administración" />
        {!abierta && (
          <nav className="mt-8 flex gap-2">
            {(
              [
                ["preregistros", "Pre-registros"],
                ["conversaciones", "Conversaciones"],
                ["pacientes", "Pacientes del piloto"],
              ] as const
            ).map(([k, t]) => (
              <button
                key={k}
                type="button"
                onClick={() => setVista(k)}
                className={`rounded-full px-4 py-2 text-sm transition-colors ${vista === k ? "bg-ink text-background" : "border border-rule text-ink-muted hover:text-ink"}`}
              >
                {t}
              </button>
            ))}
          </nav>
        )}
        {!abierta && vista === "preregistros" ? (
          <Preregistros />
        ) : !abierta && vista === "conversaciones" ? (
          <Conversaciones />
        ) : abierta ? (
          <Revision
            fila={abierta}
            alVolver={() => {
              setAbierta(null);
              void cargar();
            }}
          />
        ) : (
          <section className="mt-10">
            <h1 className="text-3xl font-light tracking-tight text-ink">Pacientes del piloto</h1>
            <p className="mt-2 text-sm text-ink-muted">
              Cuando llegue el PDF del laboratorio, toca «Subir resultado» en el paciente: se analiza solo y queda para que lo revises y apruebes.
            </p>
            <PagosPorConfirmar filas={filas ?? []} alCambiar={() => void cargar()} />
            <ConfigPago />
            <button type="button" onClick={() => setSubiendo(subiendo === "todos" ? null : "todos")} className="mt-5 rounded-full bg-optimal px-5 py-2.5 text-sm text-primary-foreground">
              Subir resultado del laboratorio
            </button>
            {subiendo === "todos" && <SubirResultado alTerminar={() => void cargar()} />}
            <div className="mt-6 space-y-3">
              {filas === null && <p className="text-sm text-ink-muted">Cargando…</p>}
              {filas?.length === 0 && <p className="text-sm text-ink-muted">Todavía no hay pacientes registrados.</p>}
              {filas?.map((f) => (
                <div key={f.id} className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-rule p-5">
                  <div>
                    <p className="text-base text-ink">{f.nombre}</p>
                    <p className="text-xs text-ink-muted">
                      {f.edad} años · {f.sexo} · WhatsApp …{f.celular_whatsapp.slice(-4)}
                    </p>
                    <p className="mt-0.5 font-mono text-[10px] text-ink-faint">id {f.id}</p>
                    <div className="mt-2 flex flex-wrap gap-1.5">
                      <Chip ok={f.cuestionario} texto={f.cuestionario ? "Cuestionario completo" : "Cuestionario pendiente"} />
                      <Chip ok={f.visita} texto={f.visita ? "Visita hecha" : "Sin visita"} />
                      {f.pago && <Chip ok={f.pago.estado === "confirmado"} texto={`${PAGO[f.pago.estado]} · ${f.pago.codigo}`} />}
                      {f.informe && <Chip ok={f.informe.estado === "aprobado"} texto={`Informe: ${ESTADO[f.informe.estado]}${f.informe.avisado ? " · avisado" : ""}`} />}
                    </div>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    <button
                      type="button"
                      onClick={() => setSubiendo(subiendo === f.id ? null : f.id)}
                      className="rounded-full border border-rule px-5 py-2.5 text-sm text-ink"
                    >
                      Subir resultado
                    </button>
                    {f.informe && (
                      <button type="button" onClick={() => setAbierta(f)} className="rounded-full bg-optimal px-5 py-2.5 text-sm text-primary-foreground">
                        Revisar informe
                      </button>
                    )}
                  </div>
                  {subiendo === f.id && <SubirResultado fila={f} alTerminar={() => void cargar()} />}
                </div>
              ))}
            </div>
          </section>
        )}
      </div>
    </main>
  );
}
