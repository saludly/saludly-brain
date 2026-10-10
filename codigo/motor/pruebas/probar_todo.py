"""Corre las cuatro partes de pruebas del motor y resume."""
import subprocess, sys, os, re
B = os.path.dirname(os.path.abspath(__file__)); total = ok = 0
for p in ("probar_parte1.py", "probar_parte2.py", "probar_parte3.py", "probar_parte4.py"):
    out = subprocess.run([sys.executable, os.path.join(B, p)], capture_output=True, text=True).stdout
    m = re.search(r"Pasan (\d+) de (\d+)", out); a, b = int(m.group(1)), int(m.group(2)); ok += a; total += b
    print(f"{p}: {a} de {b}"); [print("  ", l) for l in out.splitlines() if "FALLA" in l]
print(f"TOTAL: {ok} de {total}")
sys.exit(0 if ok == total else 1)
