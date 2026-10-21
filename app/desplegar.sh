#!/usr/bin/env bash
# Saludly · Publica la app en Vercel (app.saludly.online): la PWA compilada + la función que analiza el PDF.
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
mkdir -p "$D/saludly_lib/codigo/motor" "$D/saludly_lib/knowledge_base"
cp -r app/dist "$D/public"
rm -f "$D"/public/assets/*.map
cp -r app/api "$D/api"
cp -r codigo/pipeline codigo/informe "$D/saludly_lib/codigo/"
cp -r codigo/motor/motor "$D/saludly_lib/codigo/motor/"
cp -r knowledge_base/fase5 knowledge_base/condiciones knowledge_base/00_INDEX.json "$D/saludly_lib/knowledge_base/"
find "$D/saludly_lib" -name "__pycache__" -prune -exec rm -rf {} +
rm -rf "$D/saludly_lib/codigo/pipeline/pruebas" "$D/saludly_lib/codigo/pipeline/ejemplos" "$D/saludly_lib/codigo/pipeline/salida"
printf 'pdfplumber\npyyaml\n' > "$D/requirements.txt"
cp app/vercel.json "$D/"
cp -r app/.vercel "$D/"
[ "${1:-}" = "--sin-publicar" ] && exit 0
(cd "$D" && vercel deploy --prod --yes)
