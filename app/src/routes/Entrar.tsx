import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
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

  const conGoogle = async () => {
    setError(null);
    const { error } = await supabase.auth.signInWithOAuth({ provider: "google", options: { redirectTo: `${window.location.origin}/registro` } });
    if (error) setError("El ingreso con Google todavía no está activo. Por ahora, use su correo.");
  };

  const conCorreo = async () => {
    setError(null);
    setAviso(null);
    if (!/^\S+@\S+\.\S+$/.test(correo)) return setError("Revise su correo electrónico.");
    if (clave.length < 8) return setError("La contraseña debe tener al menos 8 caracteres.");
    setOcupado(true);
    if (modo === "crear") {
      const { data, error } = await supabase.auth.signUp({ email: correo, password: clave, options: { emailRedirectTo: `${window.location.origin}/registro` } });
      if (error) setError(error.message.includes("registered") ? "Ese correo ya tiene cuenta. Elija «Ya tengo cuenta»." : "No pudimos crear la cuenta. Intente de nuevo.");
      else if (!data.session) setAviso("Le enviamos un correo para confirmar su cuenta. Ábralo y toque el enlace para continuar.");
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
          <h1 className="text-3xl font-light tracking-tight text-ink">{modo === "crear" ? "Cree su cuenta Saludly." : "Bienvenido de nuevo."}</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">
            {modo === "crear"
              ? "Con su cuenta verá sus resultados, su plan y le avisaremos por WhatsApp cuando todo esté listo."
              : "Entre con el correo con el que creó su cuenta."}
          </p>

          <button
            type="button"
            onClick={conGoogle}
            className="mt-8 flex w-full items-center justify-center gap-3 rounded-full border border-rule px-6 py-4 text-sm text-ink transition-colors hover:border-ink/25"
          >
            <svg viewBox="0 0 24 24" className="h-5 w-5" aria-hidden>
              <path fill="#4285F4" d="M22.6 12.2c0-.8-.1-1.5-.2-2.2H12v4.2h5.9a5 5 0 0 1-2.2 3.3v2.7h3.6c2.1-1.9 3.3-4.8 3.3-8z" />
              <path fill="#34A853" d="M12 23c3 0 5.5-1 7.3-2.7l-3.6-2.7c-1 .7-2.2 1.1-3.7 1.1-2.9 0-5.3-1.9-6.2-4.5H2.1v2.8A11 11 0 0 0 12 23z" />
              <path fill="#FBBC05" d="M5.8 14.2a6.6 6.6 0 0 1 0-4.3V7.1H2.1a11 11 0 0 0 0 9.9l3.7-2.8z" />
              <path fill="#EA4335" d="M12 5.4c1.6 0 3.1.6 4.2 1.7l3.2-3.2A11 11 0 0 0 2.1 7.1l3.7 2.8C6.7 7.3 9.1 5.4 12 5.4z" />
            </svg>
            Continuar con Google
          </button>

          <div className="my-7 flex items-center gap-3 text-[11px] uppercase tracking-[0.16em] text-ink-faint">
            <span className="h-px flex-1 bg-rule" />o con su correo<span className="h-px flex-1 bg-rule" />
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
