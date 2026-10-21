import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Link, Outlet, RouterProvider, createRootRoute, createRoute, createRouter } from "@tanstack/react-router";
import "./styles.css";
import { BarraDemo, NavFlotante } from "@/components/Comunes";
import { InformeProvider } from "@/lib/contexto";
import { Bienvenida } from "@/routes/Bienvenida";
import { Panel } from "@/routes/Panel";
import { Plan } from "@/routes/Plan";

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
  createRoute({ getParentRoute: () => raiz, path: "/", component: Bienvenida }),
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
    <InformeProvider>
      <RouterProvider router={router} />
    </InformeProvider>
  </StrictMode>,
);
