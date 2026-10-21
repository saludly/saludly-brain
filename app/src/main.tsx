import { StrictMode, useEffect } from "react";
import { createRoot } from "react-dom/client";
import { Link, Outlet, RouterProvider, createRootRoute, createRoute, createRouter, useNavigate } from "@tanstack/react-router";
import "./styles.css";
import { BarraDemo, NavFlotante } from "@/components/Comunes";
import { InformeProvider } from "@/lib/contexto";
import { Bienvenida } from "@/routes/Bienvenida";
import { Panel } from "@/routes/Panel";
import { Plan } from "@/routes/Plan";
import { Entrar } from "@/routes/Entrar";
import { Registro } from "@/routes/Registro";
import { Cuestionario } from "@/routes/Cuestionario";
import { Listo } from "@/routes/Listo";
import { SesionProvider, siguientePaso, useSesion } from "@/lib/sesion";

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
        <p className="mt-4 text-sm text-muted-foreground">La página que busca no existe.</p>
        <Link to="/panel" className="mt-6 inline-flex rounded-full bg-primary px-5 py-2 text-sm text-primary-foreground">
          Ir a mi panel
        </Link>
      </div>
    </div>
  );
}

const raiz = createRootRoute({
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
  createRoute({ getParentRoute: () => raiz, path: "/registro", component: Registro }),
  createRoute({ getParentRoute: () => raiz, path: "/cuestionario", component: Cuestionario }),
  createRoute({ getParentRoute: () => raiz, path: "/listo", component: Listo }),
  createRoute({ getParentRoute: () => raiz, path: "/recorrido", component: Bienvenida }),
  createRoute({ getParentRoute: () => raiz, path: "/panel", component: Panel }),
  createRoute({ getParentRoute: () => raiz, path: "/plan", component: Plan }),
];

const router = createRouter({ routeTree: raiz.addChildren(rutas), scrollRestoration: true });

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
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
