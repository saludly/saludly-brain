#!/usr/bin/env bash
# Saludly · Publica la app en Vercel (app.saludly.online) desde este computador: la PWA compilada + la función que analiza el PDF.
# Vercel también publica solo desde GitHub con el vercel.json de la raíz; este script queda de respaldo.
# Uso, desde la raíz del proyecto: bash app/desplegar.sh
# Arma app/despliegue/ así:
#   public/        la PWA (app/dist): lo único que se sirve como archivos
#   api/           funciones de Vercel (procesar.py)
#   saludly_lib/   el análisis (lector, motor, informe) y la parte de knowledge_base que lee; no queda público
set -euo pipefail
cd "$(dirname "$0")/.."

npm --prefix app run build
D=app/despliegue
rm -rf "$D"
mkdir -p "$D"
cp -r app/dist "$D/public"
rm -f "$D"/public/assets/*.map
cp -r api "$D/api"
bash app/armar_lib.sh "$D"
cp requirements.txt "$D/"
cp app/vercel.json "$D/"
cp -r app/.vercel "$D/"
[ "${1:-}" = "--sin-publicar" ] && exit 0
(cd "$D" && vercel deploy --prod --yes)
