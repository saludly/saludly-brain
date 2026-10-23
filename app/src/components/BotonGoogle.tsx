import { useEffect, useRef, useState } from "react";
import { supabase } from "@/lib/sesion";

/**
 * Botón "Continuar con Google" de Google Identity Services. Google pide la cuenta desde app.saludly.online
 * y le entrega a Supabase el token (signInWithIdToken), así la ventana de Google ya no muestra
 * "Ir a <proyecto>.supabase.co". Si el script de Google no carga, queda el ingreso de siempre (redirección).
 * En Google Cloud, el cliente debe tener app.saludly.online (y localhost:5173) en "Orígenes de JavaScript autorizados".
 */

declare global {
  interface Window {
    google?: {
      accounts: {
        id: {
          initialize: (o: Record<string, unknown>) => void;
          renderButton: (el: HTMLElement, o: Record<string, unknown>) => void;
        };
      };
    };
  }
}

const SCRIPT = "https://accounts.google.com/gsi/client";

function cargarScript() {
  return new Promise<void>((ok, falla) => {
    if (window.google?.accounts) return ok();
    const viejo = document.querySelector<HTMLScriptElement>(`script[src="${SCRIPT}"]`);
    const s = viejo ?? Object.assign(document.createElement("script"), { src: SCRIPT, async: true });
    s.addEventListener("load", () => ok());
    s.addEventListener("error", () => falla());
    if (!viejo) document.head.appendChild(s);
  });
}

/** Nonce: Google recibe el hash y Supabase el original, para que el token no se pueda reusar. */
async function nuevoNonce() {
  const crudo = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32))));
  const hash = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(crudo));
  return { crudo, hash: [...new Uint8Array(hash)].map((b) => b.toString(16).padStart(2, "0")).join("") };
}

export function BotonGoogle({ texto = "continue_with", alError }: { texto?: "continue_with" | "signup_with" | "signin_with"; alError: (m: string) => void }) {
  const caja = useRef<HTMLDivElement>(null);
  const [respaldo, setRespaldo] = useState(false);

  useEffect(() => {
    let vivo = true;
    const id = import.meta.env.VITE_GOOGLE_CLIENT_ID;
    if (!id) {
      setRespaldo(true);
      return;
    }
    void (async () => {
      try {
        const [nonce] = await Promise.all([nuevoNonce(), cargarScript()]);
        if (!vivo || !caja.current || !window.google) return;
        window.google.accounts.id.initialize({
          client_id: id,
          nonce: nonce.hash,
          use_fedcm_for_prompt: true,
          callback: async ({ credential }: { credential: string }) => {
            const { error } = await supabase.auth.signInWithIdToken({ provider: "google", token: credential, nonce: nonce.crudo });
            if (error) alError("No pudimos entrar con Google. Intenta de nuevo.");
          },
        });
        window.google.accounts.id.renderButton(caja.current, {
          type: "standard",
          theme: "filled_blue",
          size: "large",
          shape: "pill",
          text: texto,
          logo_alignment: "left",
          width: Math.min(caja.current.offsetWidth || 360, 400),
          locale: "es",
        });
      } catch {
        if (vivo) setRespaldo(true);
      }
    })();
    return () => {
      vivo = false;
    };
  }, [texto, alError]);

  const porRedireccion = async () => {
    const { error } = await supabase.auth.signInWithOAuth({ provider: "google", options: { redirectTo: `${window.location.origin}/`, queryParams: { prompt: "select_account" } } });
    if (error) alError("No pudimos abrir Google. Intenta de nuevo.");
  };

  if (respaldo)
    return (
      <button type="button" onClick={() => void porRedireccion()} className="flex w-full items-center justify-center gap-3 rounded-full bg-optimal px-6 py-4 text-base text-primary-foreground">
        Continuar con Google
      </button>
    );
  return <div ref={caja} className="flex min-h-[44px] w-full justify-center" />;
}
