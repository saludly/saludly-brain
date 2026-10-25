import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Copy, Check } from "lucide-react";
import { Marca } from "@/components/Comunes";
import { siguientePaso, supabase, useSesion } from "@/lib/sesion";

/**
 * Pago por transferencia Bre-B (Fase 6). Después del registro: valor y llave (los edita Carlos en el panel),
 * botón para mandar la captura por WhatsApp con el código del pago y la opción de seguir con las preguntas
 * mientras Carlos lo confirma. Agendar la visita se abre solo con el pago confirmado (pantalla Listo).
 */
type Config = Record<string, string | null>;

export function Pago() {
  const s = useSesion();
  const navigate = useNavigate();
  const [config, setConfig] = useState<Config>({});
  const [copiado, setCopiado] = useState(false);

  useEffect(() => {
    if (s.cargando) return;
    const ir = siguientePaso(s);
    if (ir !== "/pago") return void navigate({ to: ir });
    // Primera vez aquí: se crea el pago (con su código) y sale el WhatsApp de registro completo.
    if (!s.pago && s.sesion)
      void supabase
        .from("pagos")
        .insert({ paciente_id: s.sesion.user.id })
        .then(() => s.recargar())
        .then(() => supabase.functions.invoke("avisar-registro"));
  }, [s, navigate]);

  // Si el WhatsApp de registro no salió (por ejemplo, la plantilla aún no estaba aprobada), se reintenta al volver aquí.
  // La función no lo repite si ya se envió.
  const pagoPendiente = s.pago?.estado === "pendiente";
  useEffect(() => {
    if (pagoPendiente) void supabase.functions.invoke("avisar-registro");
  }, [pagoPendiente]);

  useEffect(() => {
    void supabase
      .from("configuracion")
      .select("clave, valor")
      .then(({ data }) => setConfig(Object.fromEntries((data ?? []).map((x) => [x.clave, x.valor]))));
  }, []);

  const llave = config.pago_llave_breb;
  const codigo = s.pago?.codigo ?? "";
  const nombre = s.paciente?.nombre.split(" ")[0] ?? "";
  const mensaje = `Hola, soy ${s.paciente?.nombre ?? ""}. Envío el comprobante de mi pago en Saludly. Mi código es ${codigo}.`;
  const whatsapp = config.whatsapp_saludly ? `https://wa.me/${config.whatsapp_saludly}?text=${encodeURIComponent(mensaje)}` : null;
  const yaEnvio = s.pago?.estado === "comprobante";

  const copiar = async () => {
    if (!llave) return;
    try {
      await navigator.clipboard.writeText(llave);
      setCopiado(true);
    } catch {
      /* sin portapapeles: la llave queda visible para copiarla a mano */
    }
  };
  const seguir = () => {
    s.marcarPagoVisto();
    void navigate({ to: "/cuestionario" });
  };

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-xl flex-col px-6 py-8">
        <Marca derecha="Pago" />
        <section className="rise mt-12">
          <h1 className="text-3xl font-light tracking-tight text-ink">{nombre ? `${nombre}, tu` : "Tu"} registro está listo.</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">
            Para agendar la visita de la enfermera, transfiere el valor de tu paquete y envíanos la captura por WhatsApp.
          </p>

          {s.pago?.estado === "rechazado" && (
            <p className="mt-6 rounded-2xl bg-attention-soft p-4 text-sm text-ink">
              No pudimos confirmar tu pago{s.pago.nota ? `: ${s.pago.nota}` : "."} Revisa el comprobante y envíalo de nuevo.
            </p>
          )}

          <div className="mt-8 rounded-3xl border border-rule p-6">
            <dl className="space-y-5">
              <div>
                <dt className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">Valor</dt>
                <dd className="mt-1 text-2xl font-light tabular-nums text-ink">{config.pago_valor ?? "Te lo enviamos por WhatsApp"}</dd>
              </div>
              <div>
                <dt className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">Llave Bre-B</dt>
                <dd className="mt-1 flex items-center justify-between gap-3">
                  <span className="break-all font-mono text-lg text-ink">{llave ?? "Te la enviamos por WhatsApp"}</span>
                  {llave && (
                    <button type="button" onClick={() => void copiar()} className="flex shrink-0 items-center gap-1.5 rounded-full border border-rule px-3 py-1.5 text-xs text-ink">
                      {copiado ? <Check className="h-3.5 w-3.5" /> : <Copy className="h-3.5 w-3.5" />}
                      {copiado ? "Copiada" : "Copiar"}
                    </button>
                  )}
                </dd>
                {config.pago_titular && <p className="mt-1 text-xs text-ink-muted">A nombre de {config.pago_titular}</p>}
              </div>
              <div>
                <dt className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">Tu código de pago</dt>
                <dd className="mt-1 font-mono text-lg text-ink">{codigo || "…"}</dd>
              </div>
            </dl>
          </div>

          <ol className="mt-6 space-y-2 text-sm leading-relaxed text-ink-muted">
            <li>1. Transfiere desde tu banco o Nequi a la llave Bre-B.</li>
            <li>2. Toma una captura del comprobante.</li>
            <li>3. Envíanosla por WhatsApp. Te avisamos apenas la confirmemos.</li>
          </ol>

          {yaEnvio ? (
            <p className="mt-8 rounded-2xl bg-optimal-soft p-4 text-sm text-ink">✓ Recibimos tu comprobante. Lo estamos revisando.</p>
          ) : (
            whatsapp && (
              <a href={whatsapp} target="_blank" rel="noreferrer" className="mt-8 flex w-full items-center justify-center gap-2 rounded-full bg-whatsapp px-6 py-4 text-base text-white">
                Enviar comprobante por WhatsApp
              </a>
            )
          )}
          <button type="button" onClick={seguir} className="mt-4 w-full rounded-full border border-rule px-6 py-4 text-base text-ink">
            Seguir con mis preguntas mientras confirman
          </button>
        </section>
      </div>
    </main>
  );
}
