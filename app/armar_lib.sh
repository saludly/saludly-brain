#!/usr/bin/env bash
# Saludly · Copia en <destino>/saludly_lib/ el análisis que usa api/procesar.py: lector, motor, informe y la parte
# de knowledge_base que leen. Lo usan app/desplegar.sh y la publicación desde GitHub (vercel.json de la raíz).
# Uso, desde la raíz del proyecto: bash app/armar_lib.sh <destino>
set -euo pipefail
cd "$(dirname "$0")/.."
L="$1/saludly_lib"
rm -rf "$L"
mkdir -p "$L/codigo/motor" "$L/knowledge_base"
cp -r codigo/pipeline codigo/informe "$L/codigo/"
cp -r codigo/motor/motor "$L/codigo/motor/"
cp -r knowledge_base/fase5 knowledge_base/condiciones knowledge_base/00_INDEX.json "$L/knowledge_base/"
find "$L" -name "__pycache__" -prune -exec rm -rf {} +
rm -rf "$L/codigo/pipeline/pruebas" "$L/codigo/pipeline/ejemplos" "$L/codigo/pipeline/salida"
