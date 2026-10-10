"""
SCORE2 recalibrado para Colombia (SCORE2-PURE), riesgo a 10 años de enfermedad cardiovascular
fatal y no fatal, para personas de 40 a 69 años sin enfermedad cardiovascular ni diabetes.

Fuentes:
- Coeficientes, supervivencia basal y escalas regionales: SCORE2 working group, Eur Heart J 2021;42:2439-54
  (material suplementario), tal como los implementa el paquete RiskScorescvd (CRAN). Verificado contra el
  ejemplo publicado del artículo: hombre/mujer de 50 años, fumador, PAS 140, CT 5,5 y HDL 1,3 mmol/L
  -> región baja 5,9 % / 4,2 % y región muy alta 14,0 % / 13,7 %.
- Recalibración para Colombia: Lopez-Lopez et al., PURE-Colombia, Eur J Prev Cardiol 2025;32:564-72.
  Se usa el algoritmo de la región de riesgo ALTO y se multiplica el resultado por 0,75 (mujeres) o 0,61 (hombres).
  Es la calculadora que adopta la GPC colombiana de hipertensión 2025 (Lote 1).
"""
import math

COEF = {
    "hombre": dict(edad=0.3742, fuma=0.6012, pas=0.2777, ct=0.1458, hdl=-0.2698,
                   edad_fuma=-0.0755, edad_pas=-0.0255, edad_ct=-0.0281, edad_hdl=0.0426, s0=0.9605),
    "mujer": dict(edad=0.4648, fuma=0.7744, pas=0.3131, ct=0.1002, hdl=-0.2606,
                  edad_fuma=-0.1088, edad_pas=-0.0277, edad_ct=-0.0226, edad_hdl=0.0613, s0=0.9776),
}
ESCALAS = {
    "baja": {"hombre": (-0.5699, 0.7476), "mujer": (-0.7380, 0.7019)},
    "moderada": {"hombre": (-0.1565, 0.8009), "mujer": (-0.3143, 0.7701)},
    "alta": {"hombre": (0.3207, 0.9360), "mujer": (0.5710, 0.9369)},
    "muy_alta": {"hombre": (0.5836, 0.8294), "mujer": (0.9412, 0.8329)},
}
FACTOR_COLOMBIA = {"mujer": 0.75, "hombre": 0.61}
REGION_COLOMBIA = "alta"
MGDL_A_MMOL = 38.67

def score2(sexo, edad, fumador, pas, ct_mmol, hdl_mmol, region):
    c = COEF[sexo]
    a = (edad - 60) / 5; b = (pas - 120) / 20; t = ct_mmol - 6; h = (hdl_mmol - 1.3) / 0.5; f = 1 if fumador else 0
    x = (c["edad"] * a + c["fuma"] * f + c["pas"] * b + c["ct"] * t + c["hdl"] * h
         + c["edad_fuma"] * a * f + c["edad_pas"] * a * b + c["edad_ct"] * a * t + c["edad_hdl"] * a * h)
    sin_calibrar = 1 - c["s0"] ** math.exp(x)
    s1, s2 = ESCALAS[region][sexo]
    return 1 - math.exp(-math.exp(s1 + s2 * math.log(-math.log(1 - sin_calibrar))))

def score2_colombia(sexo, edad, fumador, pas, ct_mgdl, hdl_mgdl):
    base = score2(sexo, edad, fumador, pas, ct_mgdl / MGDL_A_MMOL, hdl_mgdl / MGDL_A_MMOL, REGION_COLOMBIA)
    return base * FACTOR_COLOMBIA[sexo], base

def categoria(edad, riesgo_pct):
    """Categorías por edad de la ESC 2021 (provisionales hasta confirmar las de la GPC HTA 2025)."""
    if edad < 50:
        return "bajo_moderado" if riesgo_pct < 2.5 else "alto" if riesgo_pct < 7.5 else "muy_alto"
    return "bajo_moderado" if riesgo_pct < 5 else "alto" if riesgo_pct < 10 else "muy_alto"
