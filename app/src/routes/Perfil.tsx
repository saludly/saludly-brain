import { useEffect, useState } from "react";
import { Link, useNavigate } from "@tanstack/react-router";
import { LogOut } from "lucide-react";
import { Marca } from "@/components/Comunes";
import { Campo, claseEntrada } from "@/components/Formulario";
import { supabase, useSesion } from "@/lib/sesion";

/**
 * Mi perfil: los datos de la cuenta, con edición de lo que no afecta la identificación de la muestra
 * (nombre, celular de WhatsApp y dirección) y el botón para cerrar sesión. Documento, fecha de nacimiento y sexo
 * se muestran pero no se editan aquí: el laboratorio los usa para identificar la muestra; se corrigen por WhatsApp.
 */
const DOC: Record<string, string> = { CC: "Cédula de ciudadanía", CE: "Cédula de extranjería", PPT: "PPT", PA: "Pasaporte" };

function Dato({ k, v }: { k: string; v: string }) {
  return (
    <div className="flex items-baseline justify-between gap-4 border-b border-rule py-3 last:border-0">
      <dt className="text-sm text-ink-muted">{k}</dt>
      <dd className="text-right text-sm text-ink">{v}</dd>
    </div>
  );
}

export function Perfil() {
  const s = useSesion();
  const navigate = useNavigate();
  const [nombre, setNombre] = useState("");
  const [celular, setCelular] = useState("");
  const [direccion, setDireccion] = useState("");
  const [ocupado, setOcupado] = useState(false);
  const [mensaje, setMensaje] = useState<{ ok: boolean; texto: string } | null>(null);

  useEffect(() => {
    if (s.cargando) return;
    if (!s.sesion) return void navigate({ to: "/entrar" });
    if (!s.paciente) return void navigate({ to: "/registro" });
    setNombre(s.paciente.nombre);
    setCelular(s.paciente.celular_whatsapp.slice(2));
    setDireccion(s.paciente.direccion);
  }, [s.cargando, s.sesion, s.paciente, navigate]);

  if (!s.paciente) return <main className="min-h-screen bg-background" />;
  const p = s.paciente;
  const cambios = nombre.trim() !== p.nombre || `57${celular}` !== p.celular_whatsapp || direccion.trim() !== p.direccion;
  const valido = nombre.trim().length >= 3 && /^3\d{9}$/.test(celular) && direccion.trim().length >= 5;

  const guardar = async () => {
    setOcupado(true);
    setMensaje(null);
    const { error } = await supabase
      .from("pacientes")
      .update({ nombre: nombre.trim(), celular_whatsapp: `57${celular}`, direccion: direccion.trim(), actualizado: new Date().toISOString() })
      .eq("id", p.id);
    await s.recargar();
    setOcupado(false);
    setMensaje(error ? { ok: false, texto: "No pudimos guardar tus cambios. Intenta de nuevo." } : { ok: true, texto: "Listo, guardamos tus datos." });
  };

  const salir = async () => {
    await s.salir();
    void navigate({ to: "/entrar" });
  };

  const fecha = p.fecha_nacimiento
    ? new Date(`${p.fecha_nacimiento}T12:00:00`).toLocaleDateString("es-CO", { day: "numeric", month: "long", year: "numeric" })
    : null;

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-xl px-6 pb-32 pt-8">
        <Marca derecha="Mi perfil" />
        <section className="rise mt-12">
          <h1 className="text-3xl font-light tracking-tight text-ink">{p.nombre.split(" ")[0]}, este es tu perfil.</h1>
          <p className="mt-2 text-sm text-ink-muted">{s.sesion?.user.email}</p>

          <div className="mt-8 space-y-5">
            <Campo etiqueta="Nombre completo">
              <input autoComplete="name" value={nombre} onChange={(e) => setNombre(e.target.value)} className={claseEntrada} />
            </Campo>
            <Campo etiqueta="Celular con WhatsApp" ayuda="Ahí te llegan los avisos, las recetas y los recordatorios.">
              <div className="flex gap-2">
                <span className="rounded-2xl border border-rule bg-surface px-4 py-3.5 text-base text-ink-muted">+57</span>
                <input inputMode="tel" autoComplete="tel-national" value={celular} onChange={(e) => setCelular(e.target.value.replace(/\D/g, "").slice(0, 10))} className={claseEntrada} />
              </div>
            </Campo>
            <Campo etiqueta="Dirección para la visita en Bogotá">
              <input autoComplete="street-address" value={direccion} onChange={(e) => setDireccion(e.target.value)} className={claseEntrada} />
            </Campo>
            <button type="button" disabled={!cambios || !valido || ocupado} onClick={() => void guardar()} className="w-full rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground disabled:opacity-40">
              {ocupado ? "Guardando…" : "Guardar cambios"}
            </button>
            {mensaje && <p className={`text-sm ${mensaje.ok ? "text-optimal" : "text-attention"}`}>{mensaje.texto}</p>}
          </div>

          <dl className="mt-10 rounded-3xl border border-rule px-5 py-2">
            <Dato k="Documento" v={`${DOC[p.tipo_documento] ?? p.tipo_documento} ${p.cedula}`} />
            {fecha && <Dato k="Fecha de nacimiento" v={fecha} />}
            <Dato k="Edad" v={`${p.edad} años`} />
            <Dato k="Sexo" v={p.sexo === "hombre" ? "Masculino" : "Femenino"} />
          </dl>
          <p className="mt-2 text-xs leading-relaxed text-ink-faint">
            El laboratorio usa estos datos para identificar tu muestra. Si hay que corregir alguno, escríbenos por WhatsApp.
          </p>

          <div className="mt-10 space-y-3 text-sm">
            {s.informe && (
              <Link to="/panel" className="block rounded-2xl border border-rule px-5 py-4 text-ink">
                Ver mi informe
              </Link>
            )}
            <a href="/privacidad" className="block rounded-2xl border border-rule px-5 py-4 text-ink">
              Política de tratamiento de datos
            </a>
          </div>

          <button type="button" onClick={() => void salir()} className="mt-10 flex w-full items-center justify-center gap-2 rounded-full border border-rule px-6 py-4 text-base text-ink">
            <LogOut className="h-4 w-4" />
            Cerrar sesión
          </button>
        </section>
      </div>
    </main>
  );
}
