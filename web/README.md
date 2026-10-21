# Saludly · Landing

Sitio estático. No necesita build.

## Publicar en Vercel

Opción A · Terminal (la más rápida)
    cd saludly-landing
    npx vercel          # primera vez: inicia sesión y acepta los valores por defecto
    npx vercel --prod   # publica en producción

Opción B · GitHub
1. Sube esta carpeta a un repositorio nuevo en GitHub.
2. En https://vercel.com/new importa el repositorio.
3. Framework Preset: "Other". Build Command: vacío. Output Directory: vacío (raíz).
4. Deploy.

## Ver en local
    python3 -m http.server 8080   # y abre http://localhost:8080
No abras index.html con doble clic: el navegador bloquea las animaciones por file://.

## Dónde vive (desde el 21 de octubre de 2026)
Esta carpeta `web/` del proyecto es la fuente de saludly.online (proyecto `saludlyia` en Vercel; la copia vieja estaba en
el escritorio, en "Pagina web de saludly"). Para publicar: `cd web && vercel deploy --prod`.
Los botones "Empezar" llevan a https://app.saludly.online/entrar. Los cambios de ese día están en herramientas/ajustes_2026_10_21.py.
