import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { BotonGoogle } from "@/components/BotonGoogle";
import { Marca } from "@/components/Comunes";
import { Campo, claseEntrada } from "@/components/Formulario";
import { siguientePaso, supabase, useSesion } from "@/lib/sesion";

/** Crear la cuenta o entrar, con Google o con correo y contraseña (Supabase Auth). */
export function Entrar() {
  const s = useSesion();
  const navigate = useNavigate();
  const [modo, setModo] = useState<"crear" | "entrar">("crear");
  const [correo, setCorreo] = useState("");
  const [clave, setClave] = useState("");
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [aviso, setAviso] = useState<string | null>(null);

  useEffect(() => {
    if (!s.cargando && s.sesion) void navigate({ to: siguientePaso(s) });
  }, [s, navigate]);

  const conCorreo = async () => {
    setError(null);
    setAviso(null);
    if (!/^\S+@\S+\.\S+$/.test(correo)) return setError("Revisa tu correo electrónico.");
    if (clave.length < 8) return setError("La contraseña debe tener al menos 8 caracteres.");
    setOcupado(true);
    if (modo === "crear") {
      const { data, error } = await supabase.auth.signUp({ email: correo, password: clave, options: { emailRedirectTo: `${window.location.origin}/` } });
      if (error) setError(error.message.includes("registered") ? "Ese correo ya tiene cuenta. Elige «Ya tengo cuenta»." : "No pudimos crear la cuenta. Intenta de nuevo.");
      else if (!data.session) setAviso("Te enviamos un correo para confirmar tu cuenta. Ábrelo y toca el enlace para continuar.");
    } else {
      const { error } = await supabase.auth.signInWithPassword({ email: correo, password: clave });
      if (error) setError("El correo o la contraseña no coinciden.");
    }
    setOcupado(false);
  };

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-md flex-col px-6 py-8">
        <Marca />
        <section className="rise mt-14">
          <h1 className="text-3xl font-light tracking-tight text-ink">{modo === "crear" ? "Crea tu cuenta Saludly." : "Bienvenido de nuevo."}</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">
            {modo === "crear"
              ? "Con tu cuenta verás tus resultados, tu plan y te avisaremos por WhatsApp cuando todo esté listo."
              : "Entra con el correo con el que creaste tu cuenta."}
          </p>

          <div className="mt-8">
            <BotonGoogle alError={setError} />
          </div>

          <div className="my-7 flex items-center gap-3 text-[11px] uppercase tracking-[0.16em] text-ink-faint">
            <span className="h-px flex-1 bg-rule" />o con tu correo<span className="h-px flex-1 bg-rule" />
          </div>

          <div className="space-y-4">
            <Campo etiqueta="Correo electrónico">
              <input type="email" autoComplete="email" inputMode="email" value={correo} onChange={(e) => setCorreo(e.target.value.trim())} className={claseEntrada} placeholder="nombre@correo.com" />
            </Campo>
            <Campo etiqueta="Contraseña" ayuda={modo === "crear" ? "Mínimo 8 caracteres." : undefined}>
              <input type="password" autoComplete={modo === "crear" ? "new-password" : "current-password"} value={clave} onChange={(e) => setClave(e.target.value)} className={claseEntrada} />
            </Campo>
          </div>

          {error && <p className="mt-4 rounded-xl bg-critical-soft px-4 py-2 text-sm text-critical">{error}</p>}
          {aviso && <p className="mt-4 rounded-xl bg-optimal-soft px-4 py-3 text-sm text-ink">{aviso}</p>}

          <button
            type="button"
            onClick={conCorreo}
            disabled={ocupado}
            className="mt-6 w-full rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground transition-opacity disabled:opacity-40"
          >
            {ocupado ? "Un momento…" : modo === "crear" ? "Crear mi cuenta" : "Entrar"}
          </button>
          <button
            type="button"
            onClick={() => {
              setModo(modo === "crear" ? "entrar" : "crear");
              setError(null);
              setAviso(null);
            }}
            className="mt-4 w-full text-center text-sm text-optimal underline-offset-4 hover:underline"
          >
            {modo === "crear" ? "Ya tengo cuenta" : "Crear una cuenta nueva"}
          </button>
        </section>
      </div>
    </main>
  );
}
