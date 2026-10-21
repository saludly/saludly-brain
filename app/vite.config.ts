import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath } from "node:url";

// La app lee los informes de ejemplo de codigo/pipeline/ejemplos (un nivel arriba de app/).
const raiz = fileURLToPath(new URL("..", import.meta.url));

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: { alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) } },
  server: { port: 5173, fs: { allow: [raiz] } },
  // Mapas ocultos: se generan para traducir un error del celular a nuestro código, pero no se publican (.vercelignore).
  build: { sourcemap: "hidden" },
});
