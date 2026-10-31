import { StrictMode, useEffect } from "react";
import { createRoot } from "react-dom/client";
import { Link, Outlet, RouterProvider, createRootRoute, createRoute, createRouter, useNavigate, type ErrorComponentProps } from "@tanstack/react-router";
import "./styles.css";
import { BarraDemo, NavFlotante } from "@/components/Comunes";
import { InformeProvider } from "@/lib/contexto";
import { Bienvenida } from "@/routes/Bienvenida";
import { Panel } from "@/routes/Panel";
import { Plan } from "@/routes/Plan";
import { Entrar } from "@/routes/Entrar";
import { Registro } from "@/routes/Registro";
import { Preregistro } from "@/routes/Preregistro";
import { Pago } from "@/routes/Pago";
import { Perfil } from "@/routes/Perfil";
import { Cuestionario } from "@/routes/Cuestionario";
import { Listo } from "@/routes/Listo";
import { Visita } from "@/routes/Visita";
import { Medico } from "@/routes/Medico";
import { Privacidad } from "@/routes/Privacidad";
import { VistaMedico } from "@/routes/VistaMedico";
import { Peso } from "@/routes/Peso";
import { PesoEmpezar } from "@/routes/PesoEmpezar";
import { Doctora } from "@/routes/Doctora";
import { SesionProvider, siguientePaso, useSesion } from "@/lib/sesion";
import { guardarOrigen } from "@/lib/origen";
import { marcarLineaPeso } from "@/lib/peso";

/** Entrada de la PWA: lleva al paciente al paso que le falta. */
function Inicio() {
  const s = useSesion();
  const navigate = useNavigate();
  useEffect(() => {
    if (!s.cargando) void navigate({ to: siguientePaso(s), replace: true });
  }, [s, navigate]);
  return <div className="min-h-screen bg-background" />;
}

function NoEncontrada() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background px-4">
      <div className="max-w-md text-center">
        <h1 className="text-7xl font-bold text-foreground">404</h1>
        <p className="mt-4 text-sm text-muted-foreground">La página que buscas no existe.</p>
        <Link to="/panel" className="mt-6 inline-flex rounded-full bg-primary px-5 py-2 text-sm text-primary-foreground">
          Ir a mi panel
        </Link>
      </div>
    </div>
  );
}

/** Si una pantalla falla: el mensaje en español, el detalle para mandárselo a Saludly y un botón para reintentar. */
function ErrorPantalla({ error }: ErrorComponentProps) {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background px-6">
      <div className="max-w-md text-center">
        <h1 className="text-2xl font-light text-ink">Algo salió mal al abrir esta pantalla.</h1>
        <p className="mt-3 text-sm text-ink-muted">Toca "Volver a intentar". Si sigue pasando, mándale a Saludly una captura de esta pantalla.</p>
        <p className="mt-4 whitespace-pre-wrap break-words rounded-2xl bg-surface p-3 text-left font-mono text-xs text-ink-faint">{error instanceof Error ? (error.stack ?? error.message).split("\n").slice(0, 5).join("\n") : String(error)}</p>
        <button type="button" onClick={() => window.location.assign("/")} className="mt-6 inline-flex rounded-full bg-primary px-5 py-2 text-sm text-primary-foreground">
          Volver a intentar
        </button>
      </div>
    </div>
  );
}

const raiz = createRootRoute({
  errorComponent: ErrorPantalla,
  component: () => (
    <>
      <BarraDemo />
      <NavFlotante />
      <Outlet />
    </>
  ),
  notFoundComponent: NoEncontrada,
});

const rutas = [
  createRoute({ getParentRoute: () => raiz, path: "/", component: Inicio }),
  createRoute({ getParentRoute: () => raiz, path: "/entrar", component: Entrar }),
  createRoute({ getParentRoute: () => raiz, path: "/preregistro", component: Preregistro }),
  createRoute({ getParentRoute: () => raiz, path: "/registro", component: Registro }),
  createRoute({ getParentRoute: () => raiz, path: "/pago", component: Pago }),
  createRoute({ getParentRoute: () => raiz, path: "/cuestionario", component: Cuestionario }),
  createRoute({ getParentRoute: () => raiz, path: "/listo", component: Listo }),
  createRoute({ getParentRoute: () => raiz, path: "/visita", component: Visita }),
  createRoute({ getParentRoute: () => raiz, path: "/medico", component: Medico }),
  createRoute({ getParentRoute: () => raiz, path: "/privacidad", component: Privacidad }),
  createRoute({ getParentRoute: () => raiz, path: "/perfil", component: Perfil }),
  createRoute({ getParentRoute: () => raiz, path: "/m/$slug", component: VistaMedico }),
  createRoute({ getParentRoute: () => raiz, path: "/recorrido", component: Bienvenida }),
  createRoute({ getParentRoute: () => raiz, path: "/panel", component: Panel }),
  createRoute({ getParentRoute: () => raiz, path: "/plan", component: Plan }),
  // Línea GLP-1 (Fase 6B): la paciente que llega por su doctora y el panel de la doctora.
  createRoute({ getParentRoute: () => raiz, path: "/peso", component: Peso }),
  createRoute({ getParentRoute: () => raiz, path: "/peso/empezar", component: PesoEmpezar }),
  createRoute({ getParentRoute: () => raiz, path: "/doctora", component: Doctora }),
];

const router = createRouter({ routeTree: raiz.addChildren(rutas), scrollRestoration: true });

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

guardarOrigen();
// Enlace de una doctora aliada (…/?dra=CODIGO o ?linea=peso): la paciente entra a la línea GLP-1.
{
  const q = new URLSearchParams(window.location.search);
  const dra = q.get("dra")?.toUpperCase().replace(/[^A-Z0-9]/g, "").slice(0, 20);
  if (dra || q.get("linea") === "peso") marcarLineaPeso(dra);
}

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <SesionProvider>
      <InformeProvider>
        <RouterProvider router={router} />
      </InformeProvider>
    </SesionProvider>
  </StrictMode>,
);

// PWA: solo en producción, para que el desarrollo no quede con archivos guardados.
if (import.meta.env.PROD && "serviceWorker" in navigator) {
  window.addEventListener("load", () => void navigator.serviceWorker.register("/sw.js"));
}
