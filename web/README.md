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
Los botones "Empezar" llevan a https://app.saludly.online/entrar (desde el 22 oct 2026, al pre-registro: /preregistro con el ?ref= de la visita o ref=web). Los cambios de ese día están en herramientas/ajustes_2026_10_21.py.

## Modo oscuro (desde el 22 de octubre de 2026)
La página se ve oscura solo en celulares y tabletas con el modo oscuro activo; en el computador siempre se ve clara
(condición OSCURO en el script: modo oscuro + pantalla táctil sin mouse). Cada color de los estilos es
`var(--o-…, <color claro>)`: en modo claro no hay variables y queda el color de siempre; en modo oscuro las define
un bloque al inicio de index.html. Los colores que pone el JS pasan por `slC()`. Todo lo genera
herramientas/ajustes_2026_10_22.py; si agregas una sección con colores nuevos, ponle también su color oscuro
(o vuelve a correr la conversión). La portada usa los videos de 1280 (claro y oscuro); los originales quedan en
assets/ solo como fuente y no se suben (.vercelignore).
