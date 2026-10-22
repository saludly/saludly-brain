"""
Genera el PDF "Solicitud de pruebas al laboratorio": la lista de pruebas que el laboratorio aliado
debe procesar (no incluye los valores que calcula Saludly). Sin precios: es para cotizar y negociar.

Uso:  python generar_solicitud_laboratorio.py [salida.pdf]
Lee knowledge_base/biomarcadores/ y verifica que cada biomarcador medido quede en alguna prueba.
"""
import glob, os, re, sys
from datetime import date
import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KB = os.path.join(RAIZ, "knowledge_base", "biomarcadores")
SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "docs", "02_plan_y_decisiones", "Solicitud_pruebas_laboratorio.pdf")

# ---------- fichas ----------
FICHAS = {}
for f in glob.glob(os.path.join(KB, "*.md")):
    t = open(f, encoding="utf-8").read()
    h = yaml.safe_load(re.search(r"^---\n(.*?)\n---", t, re.S).group(1))
    FICHAS[h["biomarker_id"]] = h
MEDIDOS = {k for k, h in FICHAS.items() if "calculado" not in str(h.get("panel"))}
CALCULADOS = sorted(set(FICHAS) - MEDIDOS)

# ---------- pruebas: (nombre, ids que cubre, muestra, aplica a, nota) ----------
T, M, H = "Todas las personas", "Solo mujeres", "Solo hombres"
ESTANDAR = [
    ("Hematología", [
        ("Hemograma automatizado completo", "hemoglobin hematocrit erythrocytes mcv mch mchc rdw wbc neutrophils_abs neutrophils_pct lymphocytes_abs lymphocytes_pct monocytes_pct eosinophils_pct basophils_pct platelets mpv nrbc",
         "Sangre total EDTA", T, "Hemoglobina, hematocrito, eritrocitos, VCM, HCM, CHCM, RDW, leucocitos con diferencial en % y absolutos, plaquetas, VPM y eritroblastos (NRBC)"),
        ("Velocidad de sedimentación globular (VSG)", "esr", "Sangre total (según el método)", T, ""),
        ("Hemoglobina glicosilada (HbA1c)", "hba1c", "Sangre total EDTA", T, "Método certificado NGSP"),
        ("Grupo sanguíneo ABO y factor Rh", "abo_rh", "Sangre total EDTA", T, "Una sola vez por paciente"),
    ]),
    ("Coagulación", [
        ("Tiempo de protrombina con INR", "pt", "Plasma citrato", T, "Tubo de citrato adicional"),
        ("Fibrinógeno", "fibrinogen", "Plasma citrato", T, ""),
    ]),
    ("Metabolismo", [
        ("Glucosa en ayunas", "glucose", "Suero", T, ""),
        ("Insulina en ayunas", "insulin", "Suero", T, "Basal, no curva"),
        ("Péptido C", "c_peptide", "Suero", T, ""),
        ("Fructosamina", "fructosamine", "Suero", T, ""),
        ("Ácido úrico", "uric_acid", "Suero", T, ""),
    ]),
    ("Lípidos", [
        ("Perfil lipídico", "total_cholesterol hdl_c ldl_c triglycerides", "Suero", T, "Colesterol total, HDL, LDL y triglicéridos"),
        ("Apolipoproteína B (ApoB)", "apob", "Suero", T, ""),
        ("Apolipoproteína A1 (ApoA1)", "apoa1", "Suero", T, ""),
        ("Lipoproteína(a)", "lpa", "Suero", T, "Indicar si reportan en mg/dL o nmol/L"),
    ]),
    ("Hígado, músculo y proteínas", [
        ("ALT", "alt", "Suero", T, ""),
        ("AST", "ast", "Suero", T, ""),
        ("Fosfatasa alcalina", "alp", "Suero", T, ""),
        ("GGT", "ggt", "Suero", T, ""),
        ("Bilirrubina total y directa", "bilirubin_total bilirubin_direct", "Suero", T, ""),
        ("Albúmina", "albumin", "Suero", T, ""),
        ("Proteínas totales", "total_protein", "Suero", T, ""),
        ("LDH", "ldh", "Suero", T, ""),
        ("CK total", "ck_cpk", "Suero", T, ""),
    ]),
    ("Riñón y electrolitos", [
        ("Creatinina", "creatinine", "Suero", T, "Método trazable a IDMS"),
        ("Nitrógeno ureico (BUN)", "bun", "Suero", T, ""),
        ("Sodio", "sodium", "Suero", T, "Centrifugar antes de refrigerar"),
        ("Potasio", "potassium", "Suero", T, "Centrifugar antes de refrigerar; reportar hemólisis"),
        ("Cloro", "chloride", "Suero", T, ""),
        ("Bicarbonato (CO2 total)", "bicarbonate", "Suero", T, ""),
        ("Calcio", "calcium", "Suero", T, ""),
        ("Magnesio", "magnesium", "Suero", T, ""),
        ("Osmolalidad sérica", "osmolality", "Suero", T, ""),
    ]),
    ("Hierro", [
        ("Hierro sérico", "serum_iron", "Suero", T, ""),
        ("Capacidad total de fijación de hierro (TIBC)", "tibc", "Suero", T, "Indicar si es directa o calculada"),
        ("Transferrina", "transferrin", "Suero", T, ""),
        ("Ferritina", "ferritin", "Suero", T, ""),
    ]),
    ("Inflamación e inmunidad", [
        ("Proteína C reactiva ultrasensible (hs-CRP)", "hs_crp", "Suero", T, "Ultrasensible, no PCR convencional"),
        ("Homocisteína", "homocysteine", "Suero", T, "Mantener en frío; procesar en 4 a 6 horas"),
        ("Inmunoglobulina G (IgG)", "igg", "Suero", T, ""),
        ("Inmunoglobulina M (IgM)", "igm", "Suero", T, ""),
        ("Anticuerpos antinucleares (ANA)", "ana_hep2", "Suero", T, "IFI en células HEp-2, con título y patrón"),
        ("Factor reumatoide", "rheumatoid_factor", "Suero", T, "Cuantitativo (nefelometría o turbidimetría)"),
    ]),
    ("Corazón", [
        ("Troponina de alta sensibilidad (I o T)", "hs_troponin", "Suero", T, "Alta sensibilidad, con su percentil 99"),
    ]),
    ("Tiroides y hormonas", [
        ("TSH", "tsh", "Suero", T, ""),
        # Carlos, 22 oct 2026: T4 libre y T3 total para todas las personas, ya no como reflejas.
        ("T4 libre", "free_t4", "Suero", T, "Siempre, junto con la TSH"),
        ("T3 total", "total_t3", "Suero", T, "Siempre, junto con la TSH. T3 total, no T3 libre"),
        ("Cortisol", "cortisol", "Suero", T, "Toma entre 6:00 y 10:00"),
        ("ACTH", "acth", "Plasma EDTA refrigerado", T, "Refrigerar de inmediato"),
        ("DHEA-S", "dhea_s", "Suero", T, ""),
        ("IGF-1", "igf1", "Suero", T, ""),
        ("Testosterona total", "testosterone_total", "Suero", T, "Método certificado por el CDC si es posible"),
        ("SHBG", "shbg", "Suero", T, ""),
        ("Estradiol", "estradiol", "Suero", T, "En mujeres, rango según la fase del ciclo"),
        ("LH", "lh", "Suero", T, "En mujeres, rango según la fase del ciclo"),
        ("FSH", "fsh", "Suero", M, "Rango según la fase del ciclo"),
        ("Prolactina", "prolactin", "Suero", M, ""),
        ("Progesterona", "progesterone", "Suero", M, "Rango según la fase del ciclo"),
        ("Antígeno prostático específico total (PSA)", "psa_total", "Suero", H, "Con consentimiento"),
    ]),
    ("Vitaminas y minerales", [
        ("Vitamina B12", "vitamin_b12", "Suero", T, ""),
        ("Folato sérico", "folate", "Suero", T, ""),
        ("Vitamina D (25-hidroxi)", "vitamin_d", "Suero", T, ""),
        ("Zinc", "zinc", "Suero", T, ""),
    ]),
    ("Serologías (con consentimiento)", [
        ("Anticuerpos contra hepatitis C (anti-VHC)", "anti_hcv", "Suero", T, ""),
        ("Antígeno de superficie de hepatitis B (HBsAg)", "hbsag", "Suero", T, ""),
        ("Anticuerpos contra el antígeno de superficie (anti-HBs)", "anti_hbs", "Suero", T, "Cuantitativo"),
        ("Anticuerpos contra el core de hepatitis B (anti-HBc total)", "anti_hbc", "Suero", T, ""),
        ("Chagas: ELISA de antígenos totales", "chagas_elisa_total", "Suero", T, "ELISA, no IFI"),
    ]),
]
# Orina y heces: en pausa en el MVP solo sangre (reglas_parte1.yaml > panel). Se conservan para cotizarlas después.
EN_PAUSA = [
    ("Orina", [
        ("Uroanálisis con sedimento", "urinalysis", "Primera orina de la mañana", T, ""),
        ("Relación albúmina/creatinina en orina", "uacr", "Primera orina de la mañana", T, "Albúmina y creatinina en la misma muestra"),
    ]),
    ("Heces", [
        ("Sangre oculta en heces inmunoquímica (FIT)", "fit_stool", "Heces", T, "Inmunoquímica (hemoglobina humana), no guayaco"),
        ("Antígeno de Helicobacter pylori en heces", "hpylori_stool_ag", "Heces", T, ""),
        ("Coprológico", "stool_exam", "Heces", T, ""),
    ]),
]
REFLEJAS = [
    ("Anticuerpos anti-TPO", "anti_tpo", "TSH alta", T),
    ("Anticuerpos antitiroglobulina", "anti_tg", "Anti-TPO negativo con TSH alta", T),
    ("PTH intacta", "pth", "Calcio corregido alto", T),
    ("Fósforo", "phosphorus", "Calcio corregido alto", T),
    ("Cistatina C", "cystatin_c", "TFG estimada en el límite", T),
    ("Reticulocitos (% y absolutos)", "reticulocytes_pct reticulocytes_abs", "Anemia", T),
    ("IgA total", "iga", "Déficit de hierro sin causa o ALT alta", T),
    ("Anti-transglutaminasa IgA", "anti_ttg_iga", "Déficit de hierro sin causa o ALT alta", T),
    ("NT-proBNP", "nt_probnp", "Glucosa o HbA1c en rango de diabetes", T),
    ("Aldosterona", "aldosterone", "Presión arterial de 130/80 mmHg o más", T),
    ("Renina", "renin", "Presión arterial de 130/80 mmHg o más", T),
    ("ARN de hepatitis C (carga viral)", "hcv_rna", "Anti-VHC reactivo", T),
    ("Chagas: ELISA de antígenos recombinantes", "chagas_elisa_recombinante", "Primera ELISA de Chagas reactiva", T),
    ("Macroprolactina", "macroprolactin", "Prolactina alta", M),
    ("PSA libre", "psa_free", "PSA total en zona gris", H),
    ("Ácido metilmalónico", "methylmalonic_acid", "Vitamina B12 entre 180 y 350 ng/L", T),
    ("Electroforesis de hemoglobina", "hb_electrophoresis", "VCM bajo con ferritina normal e índice de Mentzer menor de 13", T),
    ("Electroforesis de proteínas en suero", "serum_protein_electrophoresis", "Globulinas altas, relación A/G menor de 1 o IgG/IgM muy altas", T),
    ("17-hidroxiprogesterona", "hydroxyprogesterone_17", "Andrógenos altos en mujeres", M),
    ("Haptoglobina", "haptoglobin", "Anemia con reticulocitos altos (sospecha de hemólisis)", T),
    ("Anti-CCP (opcional)", "anti_ccp", "Factor reumatoide positivo; cotizar como opcional", T),
]

NO_SE_PIDEN = {k for k, h in FICHAS.items() if str(h.get("panel", "")).startswith(("fuera del panel base", "opcional"))}
PAUSADOS = set(yaml.safe_load(open(os.path.join(RAIZ, "codigo", "motor", "motor", "reglas_parte1.yaml"), encoding="utf-8"))["panel"]["solo_sangre"]["biomarcadores_pausados"])
assert {b for _, ps in EN_PAUSA for p in ps for b in p[1].split()} == PAUSADOS, "EN_PAUSA no coincide con el panel solo sangre del motor"

# ---------- verificación contra el Knowledge Base ----------
cubiertos = []
for _, pruebas in ESTANDAR:
    for p in pruebas: cubiertos += p[1].split()
for r in REFLEJAS: cubiertos += r[1].split()
assert len(cubiertos) == len(set(cubiertos)), "biomarcador repetido en dos pruebas"
assert set(cubiertos) | PAUSADOS | NO_SE_PIDEN == MEDIDOS and not set(cubiertos) & (PAUSADOS | NO_SE_PIDEN), (MEDIDOS - set(cubiertos) - PAUSADOS - NO_SE_PIDEN, set(cubiertos) - MEDIDOS)
N_EST = sum(len(p) for _, p in ESTANDAR)
N_REF = len(REFLEJAS)
N_MUJ = sum(1 for _, ps in ESTANDAR for p in ps if p[3] in (T, M))
N_HOM = sum(1 for _, ps in ESTANDAR for p in ps if p[3] in (T, H))
N_BIO_EST = sum(len(p[1].split()) for _, ps in ESTANDAR for p in ps)

# ---------- estilo ----------
for nombre, archivo in (("Arial", "arial.ttf"), ("Arial-Bold", "arialbd.ttf")):
    pdfmetrics.registerFont(TTFont(nombre, os.path.join(os.environ.get("WINDIR", "C:/Windows"), "Fonts", archivo)))
VERDE, VERDE_CLARO, GRIS, TINTA = colors.HexColor("#0F6E66"), colors.HexColor("#E6F2F0"), colors.HexColor("#5F6B6A"), colors.HexColor("#1D2626")
st = lambda **k: ParagraphStyle("s", **{**dict(fontName="Arial", fontSize=9.5, leading=13, textColor=TINTA, alignment=TA_LEFT), **k})
S = dict(titulo=st(fontName="Arial-Bold", fontSize=20, leading=24, textColor=VERDE), sub=st(fontSize=11, leading=15, textColor=GRIS),
         h1=st(fontName="Arial-Bold", fontSize=13, leading=17, textColor=VERDE, spaceBefore=10, spaceAfter=4),
         h2=st(fontName="Arial-Bold", fontSize=10.5, leading=14, textColor=TINTA, spaceBefore=8, spaceAfter=3),
         p=st(), celda=st(fontSize=8.3, leading=10.5), celda_b=st(fontName="Arial-Bold", fontSize=8.3, leading=10.5),
         cab=st(fontName="Arial-Bold", fontSize=8.3, leading=10.5, textColor=colors.white), num=st(fontName="Arial-Bold", fontSize=18, leading=21, textColor=VERDE),
         lbl=st(fontSize=8.3, leading=10.5, textColor=GRIS))

def tabla(filas, anchos, cab):
    datos = [[Paragraph(c, S["cab"]) for c in cab]] + filas
    t = Table(datos, colWidths=anchos, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), VERDE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, VERDE_CLARO]),
                           ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#C9D6D4")),
                           ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                           ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]))
    return t

def pie(c, doc):
    c.saveState(); c.setFont("Arial", 7.5); c.setFillColor(GRIS)
    c.drawString(18 * mm, 10 * mm, "Saludly · Solicitud de pruebas al laboratorio · Contacto: Carlos, CEO de Saludly")
    c.drawRightString(letter[0] - 18 * mm, 10 * mm, f"Página {doc.page}")
    c.restoreState()

# ---------- contenido ----------
F = []
F += [Paragraph("Solicitud de pruebas al laboratorio", S["titulo"]), Spacer(1, 3),
      Paragraph(f"Saludly · Bogotá · {date.today().strftime('%d/%m/%Y')}", S["sub"]), Spacer(1, 10),
      Paragraph("Saludly es una empresa de salud preventiva. Una enfermera toma <b>una sola muestra a domicilio</b>, "
                "en ayunas y en la mañana; el laboratorio aliado la procesa y nos envía los resultados en PDF. "
                "Este documento lista las pruebas que necesitamos que el laboratorio realice, para pedir su cotización. "
                "Los valores que Saludly calcula a partir de estos resultados no se incluyen.", S["p"]), Spacer(1, 10)]
cifras = [(str(N_EST), "pruebas de sangre del panel estándar"), (str(N_REF), "pruebas reflejas, solo si un resultado las activa"),
          (f"{N_MUJ} / {N_HOM}", "pruebas estándar por mujer / por hombre"), (str(len(MEDIDOS) - len(PAUSADOS) - len(NO_SE_PIDEN)), "biomarcadores medidos en total, con reflejas")]
kpi = Table([[Paragraph(n, S["num"]) for n, _ in cifras], [Paragraph(l, S["lbl"]) for _, l in cifras]], colWidths=[44 * mm] * 4)
kpi.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#C9D6D4")), ("BACKGROUND", (0, 0), (-1, -1), VERDE_CLARO),
                         ("LEFTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (0, -1), 6), ("BOTTOMPADDING", (0, 1), (-1, 1), 7)]))
F += [kpi, Spacer(1, 8)]

F += [Paragraph("Condiciones de la toma", S["h1"])]
for linea in ["Toma domiciliaria por enfermera, <b>en ayunas y entre las 6:00 y las 10:00</b>.",
              "Muestras: <b>solo sangre venosa</b> (suero, EDTA y citrato). En esta primera etapa no hay muestras de orina ni de heces.",
              "Centrífuga portátil en la visita; las muestras viajan refrigeradas. No hay pruebas que exijan transporte congelado.",
              "Las pruebas reflejas se corren sobre la <b>misma muestra retenida</b>; el paciente no repite la toma.",
              "Saludly entrega con cada orden la edad, el sexo y, en mujeres, la fecha de la última menstruación, para los rangos por fase del ciclo."]:
    F.append(Paragraph("•&nbsp;&nbsp;" + linea, S["p"]))

F += [Paragraph(f"1. Panel estándar ({N_EST} pruebas)", S["h1"]),
      Paragraph("Se realizan a todas las personas, salvo las marcadas como solo mujeres o solo hombres.", S["p"])]
ANCHOS = [8 * mm, 58 * mm, 36 * mm, 24 * mm, 54 * mm]
n = 0
for grupo, pruebas in ESTANDAR:
    filas = []
    for nombre, _, muestra, aplica, nota in pruebas:
        n += 1
        filas.append([Paragraph(str(n), S["celda"]), Paragraph(nombre, S["celda_b"]), Paragraph(muestra, S["celda"]),
                      Paragraph("Todas" if aplica == T else aplica.replace("Solo ", "Solo "), S["celda"]), Paragraph(nota, S["celda"])])
    F.append(KeepTogether([Paragraph(grupo, S["h2"]), tabla(filas, ANCHOS, ["#", "Prueba", "Muestra", "Aplica a", "Detalle o requisito"])]))

filas = [[Paragraph(str(i), S["celda"]), Paragraph(nom, S["celda_b"]), Paragraph(cond, S["celda"]),
          Paragraph("Todas" if ap == T else ap, S["celda"])] for i, (nom, _, cond, ap) in enumerate(REFLEJAS, 1)]
F.append(KeepTogether([Paragraph(f"2. Pruebas reflejas ({N_REF})", S["h1"]),
                       Paragraph("El laboratorio las corre automáticamente sobre la muestra retenida cuando se cumple la condición. "
                                 "No forman parte del costo fijo por persona; las cotizamos aparte.", S["p"]), Spacer(1, 4),
                       tabla(filas, [8 * mm, 62 * mm, 82 * mm, 28 * mm], ["#", "Prueba", "Se corre cuando", "Aplica a"])]))

F += [Paragraph("3. Lo que pedimos en la cotización", S["h1"])]
for i, linea in enumerate([
        f"<b>Precio del combo completo por persona:</b> el panel estándar de {N_EST} pruebas, para mujer y para hombre, "
        "y descuentos por volumen mensual.",
        "Precio por prueba y, si aplica, por paquete (por ejemplo hemograma, perfil lipídico o perfil hepático).",
        "Precio de cada prueba refleja y tiempo de retención de la muestra para correrlas.",
        "Costo de la toma a domicilio en Bogotá, insumos y transporte refrigerado.",
        "Pruebas que no realizan directamente y si las remiten a otro laboratorio, con su tiempo de entrega.",
        "Método de cada prueba, en especial: ANA en HEp-2 con título y patrón, troponina de alta sensibilidad, "
        "hs-CRP ultrasensible, testosterona y Lp(a).",
        "Tiempo de entrega de resultados y formato del informe (PDF, y si es posible un archivo estructurado).",
        "Validación de nuestro protocolo de toma domiciliaria (tubos, volúmenes, centrifugación y transporte)."], 1):
    F.append(Paragraph(f"{i}.&nbsp;&nbsp;{linea}", S["p"]))



SimpleDocTemplate(SALIDA, pagesize=letter, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=18 * mm,
                  title="Solicitud de pruebas al laboratorio · Saludly", author="Saludly").build(F, onFirstPage=pie, onLaterPages=pie)
print(f"{SALIDA}\nPanel estándar: {N_EST} pruebas ({N_BIO_EST} biomarcadores) · mujer {N_MUJ} · hombre {N_HOM} · reflejas: {N_REF} · "
      f"medidos: {len(MEDIDOS)} · calculados por Saludly: {len(CALCULADOS)}")
