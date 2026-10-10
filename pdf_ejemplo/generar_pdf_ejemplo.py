from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Table,
                                TableStyle, Spacer, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('DV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

AZUL = colors.HexColor('#1f4fa8'); GRIS = colors.HexColor('#5e5d59'); LINEA = colors.HexColor('#b8b7ae')
FONDO = colors.HexColor('#eef2f9')
st_t = ParagraphStyle('t', fontName='DVB', fontSize=12, textColor=AZUL, leading=15)
st_s = ParagraphStyle('s', fontName='DVB', fontSize=9.5, textColor=colors.white, leading=12)
st_c = ParagraphStyle('c', fontName='DV', fontSize=7.6, leading=9.4)
st_cb = ParagraphStyle('cb', fontName='DVB', fontSize=7.6, leading=9.4)
st_n = ParagraphStyle('n', fontName='DV', fontSize=7.8, leading=10, textColor=GRIS)
st_obs = ParagraphStyle('o', fontName='DV', fontSize=8.2, leading=11)

LAB = {
    'nombre': 'LABORATORIO CLÍNICO DEMO S.A.S.',
    'nit': 'NIT 900.000.000-0',
    'habil': 'Código de habilitación REPS: 0000000000-01',
    'dir': 'Calle 00 # 00-00, Bogotá D.C. · Tel. (601) 000 0000',
}

def P(t, s=st_c): return Paragraph(t, s)

def build(case, path):
    doc = BaseDocTemplate(path, pagesize=letter, leftMargin=14*mm, rightMargin=14*mm,
                          topMargin=46*mm, bottomMargin=20*mm,
                          title=f"Resultados de laboratorio · Orden {case['orden']}",
                          author=LAB['nombre'],
                          subject=f"Paciente {case['doc']} · Orden {case['orden']} · Toma {case['toma']}",
                          keywords=f"saludly;ejemplo;ficticio;orden={case['orden']};documento={case['doc']};sexo={case['sexo']};formato=saludly-demo-v1",
                          creator='Saludly · PDF de ejemplo v1')
    W = letter[0] - 28*mm

    def header(c, d):
        c.saveState()
        x0 = 14*mm; top = letter[1] - 12*mm
        c.setFillColor(AZUL); c.rect(x0, top-11*mm, 11*mm, 11*mm, fill=1, stroke=0)
        c.setFillColor(colors.white); c.setFont('DVB', 9); c.drawCentredString(x0+5.5*mm, top-7*mm, 'LCD')
        c.setFillColor(colors.black); c.setFont('DVB', 11); c.drawString(x0+14*mm, top-4*mm, LAB['nombre'])
        c.setFont('DV', 7.5); c.setFillColor(GRIS)
        c.drawString(x0+14*mm, top-8*mm, f"{LAB['nit']} · {LAB['habil']}")
        c.drawString(x0+14*mm, top-11.5*mm, LAB['dir'])
        c.setFillColor(colors.HexColor('#b3261e')); c.setFont('DVB', 7.5)
        c.drawRightString(letter[0]-14*mm, top-4*mm, 'DOCUMENTO DE EJEMPLO · DATOS FICTICIOS')
        c.drawRightString(letter[0]-14*mm, top-8*mm, 'NO VÁLIDO PARA USO CLÍNICO')
        # bloque del paciente
        y = top - 15*mm
        c.setStrokeColor(LINEA); c.setFillColor(FONDO)
        c.rect(x0, y-17*mm, W, 17*mm, fill=1, stroke=1)
        campos = [
            ('Paciente', case['nombre']), ('Documento', case['doc']), ('Sexo', case['sexo_txt']),
            ('Nacimiento', case['nac']), ('Edad', case['edad']), ('Aseguradora', case['eps']),
            ('N.º de orden', case['orden']), ('Programa', case['medico']), ('Ayuno', case['ayuno']),
            ('Toma', case['toma']), ('Recepción', case['recep']), ('Validación', case['valid']),
        ]
        colw = W/3
        for i, (k, v) in enumerate(campos):
            cx = x0 + 2*mm + (i % 3)*colw; cy = y - 4*mm - (i // 3)*3.8*mm
            c.setFillColor(GRIS); c.setFont('DV', 6.8); c.drawString(cx, cy, k + ':')
            c.setFillColor(colors.black); c.setFont('DVB', 7.2); c.drawString(cx + 21*mm, cy, v)
        # pie
        c.setFont('DV', 6.8); c.setFillColor(GRIS)
        c.drawString(x0, 12*mm, 'Resultados validados por: Bacterióloga de ejemplo · T.P. 00000 · Firma electrónica de ejemplo')
        c.drawRightString(letter[0]-14*mm, 12*mm, f"Orden {case['orden']} · Página {d.page}")
        c.drawString(x0, 8.5*mm, 'Ind.: H = por encima del intervalo de referencia · L = por debajo · * = ver observación. '
                                 'Los intervalos de referencia dependen del método y de la población.')
        c.restoreState()

    frame = Frame(14*mm, 20*mm, W, letter[1]-66*mm, id='f', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=header)])

    story = [P('INFORME DE RESULTADOS', st_t), Spacer(1, 3*mm)]
    cw = [W*0.30, W*0.14, W*0.06, W*0.12, W*0.20, W*0.18]
    for sec in case['secciones']:
        titulo, muestra, filas = sec
        data = [[P(f"{titulo}", st_s), '', '', '', '', P(f"Muestra: {muestra}", ParagraphStyle('m', parent=st_s, fontName='DV', fontSize=7.4))],
                [P('Examen', st_cb), P('Resultado', st_cb), P('Ind.', st_cb), P('Unidad', st_cb),
                 P('Valores de referencia', st_cb), P('Método', st_cb)]]
        for f in filas:
            ex, res, ind, uni, ref, met = (list(f) + ['']*6)[:6]
            data.append([P(ex), P(f"<b>{res}</b>" if ind else res), P(f"<b>{ind}</b>"), P(uni), P(ref), P(met)])
        t = Table(data, colWidths=cw, repeatRows=2)
        t.setStyle(TableStyle([
            ('SPAN', (0, 0), (4, 0)), ('BACKGROUND', (0, 0), (-1, 0), AZUL),
            ('BACKGROUND', (0, 1), (-1, 1), FONDO),
            ('LINEBELOW', (0, 1), (-1, -1), 0.3, LINEA),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 1.6), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.6),
        ]))
        story += [t, Spacer(1, 3.5*mm)]
    story.append(KeepTogether([P('OBSERVACIONES', st_t), Spacer(1, 1.5*mm)] +
                              [P('· ' + o, st_obs) for o in case['obs']]))
    doc.build(story)

# ----------------------------------------------------------------------------
HEMA = 'Sangre total EDTA'; SUERO = 'Suero'; CIT = 'Plasma citrato'; ORINA = 'Orina (primera de la mañana)'; HECES = 'Heces'
ENZ = 'Enzimático'; QLA = 'Quimioluminiscencia'; CIT_F = 'Citometría de flujo'; ITB = 'Inmunoturbidimetría'

def hemograma(v):
    return ('HEMATOLOGÍA · HEMOGRAMA IV', HEMA, [
        ('Hemoglobina', *v['hb']), ('Hematocrito', *v['hto']), ('Recuento de eritrocitos', *v['gr']),
        ('VCM (volumen corpuscular medio)', *v['vcm']), ('HCM (hemoglobina corpuscular media)', *v['hcm']),
        ('CHCM', *v['chcm']), ('RDW-CV', *v['rdw']), ('Recuento de leucocitos', *v['gb']),
        ('Neutrófilos %', *v['neup']), ('Neutrófilos absolutos', *v['neua']), ('Linfocitos %', *v['linp']),
        ('Linfocitos absolutos', *v['lina']), ('Monocitos %', *v['mono']), ('Eosinófilos %', *v['eos']),
        ('Basófilos %', *v['baso']), ('Recuento de plaquetas', *v['plq']), ('VPM (volumen plaquetario medio)', *v['vpm']),
        ('Eritroblastos (NRBC)', *v['nrbc'])])

def r(res, ind, uni, ref, met): return (res, ind, uni, ref, met)

# ---------------- Caso 1: hombre 46 años ----------------
c1h = dict(
    hb=r('16,2', '', 'g/dL', '13,5 – 17,5', CIT_F), hto=r('48,1', '', '%', '41,0 – 53,0', CIT_F),
    gr=r('5,35', '', 'x10⁶/µL', '4,50 – 5,90', CIT_F), vcm=r('89,9', '', 'fL', '80,0 – 100,0', 'Calculado'),
    hcm=r('30,3', '', 'pg', '27,0 – 33,0', 'Calculado'), chcm=r('33,7', '', 'g/dL', '32,0 – 36,0', 'Calculado'),
    rdw=r('13,1', '', '%', '11,5 – 14,5', CIT_F), gb=r('7,80', '', 'x10³/µL', '4,50 – 11,00', CIT_F),
    neup=r('58,2', '', '%', '40,0 – 70,0', CIT_F), neua=r('4,54', '', 'x10³/µL', '1,80 – 7,70', 'Calculado'),
    linp=r('31,0', '', '%', '20,0 – 45,0', CIT_F), lina=r('2,42', '', 'x10³/µL', '1,00 – 4,80', 'Calculado'),
    mono=r('7,1', '', '%', '2,0 – 10,0', CIT_F), eos=r('3,2', '', '%', '0,0 – 6,0', CIT_F),
    baso=r('0,5', '', '%', '0,0 – 2,0', CIT_F), plq=r('265', '', 'x10³/µL', '150 – 450', CIT_F),
    vpm=r('9,8', '', 'fL', '7,5 – 11,5', CIT_F), nrbc=r('0,0', '', '/100 leucocitos', '0,0', CIT_F))

caso1 = dict(
    nombre='PACIENTE EJEMPLO UNO', doc='CC 0000000001', sexo='M', sexo_txt='Masculino', nac='14/03/1980', edad='46 años',
    eps='EPS EJEMPLO', orden='LCD-2026-100123', medico='Saludly · Preventivo', ayuno='11 horas',
    toma='01/10/2026 07:15', recep='01/10/2026 10:40', valid='02/10/2026 16:20',
    secciones=[
        hemograma(c1h),
        ('COAGULACIÓN', CIT, [
            ('Tiempo de protrombina (TP)', '12,1', '', 's', '10,5 – 13,5', 'Coagulométrico'),
            ('INR', '1,02', '', '', '0,85 – 1,15', 'Calculado (ISI)'),
            ('Fibrinógeno', '360', '', 'mg/dL', '200 – 400', 'Clauss')]),
        ('QUÍMICA SANGUÍNEA · METABOLISMO DE CARBOHIDRATOS', SUERO + ' / Plasma fluoruro', [
            ('Glucosa en ayunas', '112', 'H', 'mg/dL', '70 – 99', 'Hexoquinasa'),
            ('Hemoglobina glicosilada (HbA1c)', '6,0', 'H', '%', '4,0 – 5,6', 'HPLC (certificado NGSP)'),
            ('Insulina en ayunas', '19,8', '', 'µUI/mL', '2,6 – 24,9', QLA),
            ('Péptido C', '3,4', '', 'ng/mL', '1,1 – 4,4', QLA),
            ('Fructosamina', '268', '', 'µmol/L', '205 – 285', 'Colorimétrico'),
            ('Ácido úrico', '7,6', 'H', 'mg/dL', '3,4 – 7,0', 'Uricasa')]),
        ('PERFIL LIPÍDICO', SUERO, [
            ('Colesterol total', '228', 'H', 'mg/dL', '< 200', ENZ),
            ('Triglicéridos', '238', 'H', 'mg/dL', '< 150', ENZ),
            ('Colesterol HDL', '36', 'L', 'mg/dL', '> 40', 'Enzimático directo'),
            ('Colesterol LDL (medido)', '142', 'H', 'mg/dL', '< 130', 'Enzimático directo'),
            ('Apolipoproteína B', '118', 'H', 'mg/dL', '60 – 117', ITB),
            ('Apolipoproteína A1', '112', '', 'mg/dL', '104 – 202', ITB),
            ('Lipoproteína (a)', '18', '', 'mg/dL', '< 30', ITB)]),
        ('ELECTROLITOS Y MINERALES', SUERO, [
            ('Sodio', '140', '', 'mmol/L', '136 – 145', 'ISE indirecto'),
            ('Potasio', '4,3', '', 'mmol/L', '3,5 – 5,1', 'ISE indirecto'),
            ('Cloro', '103', '', 'mmol/L', '98 – 107', 'ISE indirecto'),
            ('Bicarbonato (CO₂ total)', '25', '', 'mmol/L', '22 – 29', ENZ),
            ('Calcio total', '9,5', '', 'mg/dL', '8,6 – 10,2', 'Arsenazo III'),
            ('Fósforo', '3,2', '', 'mg/dL', '2,5 – 4,5', 'Fosfomolibdato'),
            ('Magnesio', '2,0', '', 'mg/dL', '1,7 – 2,4', 'Azul de xilidilo'),
            ('Zinc', '82', '', 'µg/dL', '60 – 120', 'Colorimétrico'),
            ('Osmolalidad sérica', '292', '', 'mOsm/kg', '275 – 295', 'Descenso crioscópico')]),
        ('FUNCIÓN HEPÁTICA Y PROTEÍNAS', SUERO, [
            ('ALT (TGP)', '58', 'H', 'U/L', '10 – 50', 'IFCC sin P5P'),
            ('AST (TGO)', '39', '', 'U/L', '10 – 40', 'IFCC sin P5P'),
            ('Gamma glutamil transferasa (GGT)', '72', 'H', 'U/L', '10 – 71', 'IFCC'),
            ('Fosfatasa alcalina', '88', '', 'U/L', '40 – 129', 'IFCC'),
            ('Bilirrubina total', '0,80', '', 'mg/dL', '0,30 – 1,20', 'Diazo'),
            ('Bilirrubina directa', '0,20', '', 'mg/dL', '0,00 – 0,30', 'Diazo'),
            ('Proteínas totales', '7,3', '', 'g/dL', '6,4 – 8,3', 'Biuret'),
            ('Albúmina', '4,6', '', 'g/dL', '3,5 – 5,2', 'Verde de bromocresol'),
            ('Globulinas (calculado)', '2,7', '', 'g/dL', '2,0 – 3,5', 'Calculado'),
            ('Relación albúmina/globulina', '1,70', '', '', '1,10 – 2,50', 'Calculado'),
            ('Lactato deshidrogenasa (LDH)', '190', '', 'U/L', '135 – 225', 'IFCC'),
            ('Creatina quinasa (CK)', '165', '', 'U/L', '39 – 308', 'IFCC')]),
        ('FUNCIÓN RENAL', SUERO, [
            ('Creatinina', '0,98', '', 'mg/dL', '0,70 – 1,20', 'Jaffé compensado (trazable IDMS)'),
            ('TFG estimada (CKD-EPI 2021)', '96', '', 'mL/min/1,73 m²', '> 60', 'Calculado'),
            ('Nitrógeno ureico (BUN)', '15', '', 'mg/dL', '6 – 20', 'Ureasa'),
            ('Relación BUN/creatinina', '15,3', '', '', '10 – 20', 'Calculado')]),
        ('TIROIDES Y HORMONAS', SUERO, [
            ('TSH', '2,10', '', 'µUI/mL', '0,27 – 4,20', QLA),
            ('Testosterona total', '412', '', 'ng/dL', '264 – 916', QLA),
            ('SHBG', '28', '', 'nmol/L', '16,5 – 55,9', QLA),
            ('Estradiol', '28', '', 'pg/mL', '11 – 44', QLA),
            ('LH', '4,2', '', 'mUI/mL', '1,7 – 8,6', QLA),
            ('DHEA-S', '210', '', 'µg/dL', '89 – 427', QLA),
            ('Cortisol (toma 07:15)', '14,2', '', 'µg/dL', '6,2 – 19,4 (mañana)', QLA),
            ('ACTH', '24', '', 'pg/mL', '7,2 – 63,3 (mañana)', QLA),
            ('IGF-1', '168', '', 'ng/mL', '83 – 233 (45 – 49 años)', QLA),
            ('PSA total', '1,10', '', 'ng/mL', '< 4,00', QLA)]),
        ('MARCADORES CARDIOVASCULARES E INFLAMACIÓN', SUERO, [
            ('Proteína C reactiva ultrasensible', '3,4', 'H', 'mg/L', '< 3,0', ITB),
            ('Velocidad de sedimentación globular', '12', '', 'mm/h', '0 – 15', 'Westergren', ),
            ('Homocisteína', '11,8', '', 'µmol/L', '5,0 – 15,0', 'Enzimático'),
            ('Troponina I de alta sensibilidad', '< 3', '', 'ng/L', '< 14 (percentil 99)', QLA),
            ('Anticuerpos antinucleares (ANA)', 'Negativo (< 1:80)', '', '', 'Negativo', 'IFI en células HEp-2')]),
        ('INMUNOLOGÍA', SUERO, [
            ('Inmunoglobulina G (IgG)', '1120', '', 'mg/dL', '700 – 1600', ITB),
            ('Inmunoglobulina M (IgM)', '95', '', 'mg/dL', '40 – 230', ITB)]),
        ('METABOLISMO DEL HIERRO', SUERO, [
            ('Ferritina', '310', '', 'ng/mL', '30 – 400', QLA),
            ('Hierro sérico', '118', '', 'µg/dL', '65 – 175', 'Ferrozina'),
            ('Capacidad total de fijación de hierro (TIBC)', '320', '', 'µg/dL', '250 – 450', 'Directo'),
            ('Transferrina', '256', '', 'mg/dL', '200 – 360', ITB),
            ('Saturación de transferrina (calculado)', '37', '', '%', '20 – 50', 'Calculado')]),
        ('VITAMINAS', SUERO + ' / Plasma heparina (vitamina C)', [
            ('Vitamina B12', '410', '', 'pg/mL', '197 – 771', QLA),
            ('Ácido fólico', '9,8', '', 'ng/mL', '> 3,9', QLA),
            ('25-hidroxivitamina D', '21,4', 'L', 'ng/mL', '30 – 100', QLA),
            ('Vitamina B6 (piridoxal 5-fosfato)', '8,1', '', 'µg/L', '5,0 – 50,0', 'HPLC'),
            ('Vitamina B1 (tiamina)', '98', '', 'nmol/L', '70 – 180', 'HPLC'),
            ('Vitamina A (retinol)', '58', '', 'µg/dL', '30 – 80', 'HPLC'),
            ('Vitamina E (alfa-tocoferol)', '12,4', '', 'mg/L', '5,5 – 17,0', 'HPLC'),
            ('Vitamina K1 (filoquinona)', '0,62', '', 'ng/mL', '0,10 – 2,20', 'HPLC'),
            ('Vitamina C (ácido ascórbico)', '0,9', '', 'mg/dL', '0,4 – 2,0', 'HPLC'),
            ('Biotina (vitamina B7)', '410', '', 'ng/L', 'No establecido', 'Inmunoensayo'),
            ('Niacina (vitamina B3)', '5,1', '', 'µg/mL', 'No establecido', 'LC-MS/MS'),
            ('Índice omega-3', '4,1', '', '%', 'No establecido', 'Cromatografía de gases'),
            ('Relación omega-6/omega-3', '11,2', '', '', 'No establecido', 'Cromatografía de gases'),
            ('Coenzima Q10', '0,82', '', 'µg/mL', 'No establecido', 'HPLC')]),
        ('SEROLOGÍA E INFECCIOSAS', SUERO, [
            ('Anticuerpos contra hepatitis C (anti-VHC)', 'No reactivo (0,08)', '', 'índice', '< 1,00', QLA),
            ('Antígeno de superficie hepatitis B (HBsAg)', 'No reactivo (0,32)', '', 'índice', '< 1,00', QLA),
            ('Anticuerpos contra antígeno de superficie (anti-HBs)', '4,2', 'L', 'mUI/mL', '≥ 10 (inmunidad)', QLA),
            ('Anticuerpos totales contra core hepatitis B (anti-HBc)', 'No reactivo (0,11)', '', 'índice', '< 1,00', QLA),
            ('Anticuerpos IgG Trypanosoma cruzi (Chagas)', 'No reactivo (0,21)', '', 'índice', '< 0,90', 'ELISA')]),
        ('UROANÁLISIS', ORINA, [
            ('Color', 'Amarillo', '', '', 'Amarillo', 'Visual'), ('Aspecto', 'Claro', '', '', 'Claro', 'Visual'),
            ('Densidad', '1,020', '', '', '1,005 – 1,030', 'Tira reactiva'), ('pH', '6,0', '', '', '5,0 – 8,0', 'Tira reactiva'),
            ('Proteínas', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Glucosa', 'Negativo', '', '', 'Negativo', 'Tira reactiva'),
            ('Cuerpos cetónicos', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Sangre', 'Negativo', '', '', 'Negativo', 'Tira reactiva'),
            ('Nitritos', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Esterasa leucocitaria', 'Negativo', '', '', 'Negativo', 'Tira reactiva'),
            ('Bilirrubina', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Urobilinógeno', '0,2', '', 'mg/dL', '0,2 – 1,0', 'Tira reactiva'),
            ('Sedimento · leucocitos', '0 – 2', '', '/campo', '0 – 5', 'Microscopía'), ('Sedimento · hematíes', '0 – 2', '', '/campo', '0 – 3', 'Microscopía'),
            ('Sedimento · células epiteliales', 'Escasas', '', '', 'Escasas', 'Microscopía'), ('Sedimento · bacterias', 'Escasas', '', '', 'Escasas', 'Microscopía'),
            ('Sedimento · cilindros', 'No se observan', '', '', 'No se observan', 'Microscopía'),
            ('Sedimento · cristales', 'No se observan', '', '', 'No se observan', 'Microscopía'),
            ('Albúmina en orina', '41', '', 'mg/L', '', ITB), ('Creatinina en orina', '92', '', 'mg/dL', '', 'Jaffé'),
            ('Relación albúmina/creatinina (RAC)', '45', 'H', 'mg/g', '< 30', 'Calculado')]),
        ('COPROLÓGICO Y PRUEBAS EN HECES', HECES, [
            ('Sangre oculta en heces (inmunoquímica, FIT)', 'Negativo', '', '', 'Negativo', 'Inmunocromatografía'),
            ('Antígeno de Helicobacter pylori en heces', 'Positivo', '*', '', 'Negativo', 'Inmunoensayo monoclonal'),
            ('Coprológico · consistencia', 'Blanda', '', '', '', 'Macroscópico'),
            ('Coprológico · color', 'Café', '', '', '', 'Macroscópico'),
            ('Coprológico · moco', 'Negativo', '', '', 'Negativo', 'Macroscópico'),
            ('Coprológico · parásitos', 'No se observaron parásitos', '', '', '', 'Directo y lugol')]),
    ],
    obs=['Antígeno de H. pylori positivo por método monoclonal en heces. La prueba de aliento con urea C13 es la referencia no invasiva; se informa el resultado obtenido con la muestra disponible.',
         'Relación albúmina/creatinina elevada en una sola muestra. La albuminuria requiere confirmación con nuevas mediciones.',
         'Pruebas reflejas: ninguna activada en esta orden.',
         'Documento generado por Saludly como ejemplo de formato. Laboratorio, paciente, documento y resultados son ficticios.'])

# ---------------- Caso 2: mujer 34 años ----------------
c2h = dict(
    hb=r('11,2', 'L', 'g/dL', '12,0 – 16,0', CIT_F), hto=r('35,0', 'L', '%', '36,0 – 46,0', CIT_F),
    gr=r('4,30', '', 'x10⁶/µL', '4,00 – 5,20', CIT_F), vcm=r('78,2', 'L', 'fL', '80,0 – 100,0', 'Calculado'),
    hcm=r('26,0', 'L', 'pg', '27,0 – 33,0', 'Calculado'), chcm=r('32,0', '', 'g/dL', '32,0 – 36,0', 'Calculado'),
    rdw=r('16,4', 'H', '%', '11,5 – 14,5', CIT_F), gb=r('6,10', '', 'x10³/µL', '4,50 – 11,00', CIT_F),
    neup=r('55,0', '', '%', '40,0 – 70,0', CIT_F), neua=r('3,36', '', 'x10³/µL', '1,80 – 7,70', 'Calculado'),
    linp=r('35,0', '', '%', '20,0 – 45,0', CIT_F), lina=r('2,14', '', 'x10³/µL', '1,00 – 4,80', 'Calculado'),
    mono=r('6,0', '', '%', '2,0 – 10,0', CIT_F), eos=r('3,5', '', '%', '0,0 – 6,0', CIT_F),
    baso=r('0,5', '', '%', '0,0 – 2,0', CIT_F), plq=r('330', '', 'x10³/µL', '150 – 450', CIT_F),
    vpm=r('9,6', '', 'fL', '7,5 – 11,5', CIT_F), nrbc=r('0,0', '', '/100 leucocitos', '0,0', CIT_F))

caso2 = dict(
    nombre='PACIENTE EJEMPLO DOS', doc='CC 0000000002', sexo='F', sexo_txt='Femenino', nac='22/07/1992', edad='34 años',
    eps='EPS EJEMPLO', orden='LCD-2026-100124', medico='Saludly · Preventivo', ayuno='12 horas',
    toma='01/10/2026 07:40', recep='01/10/2026 10:40', valid='02/10/2026 17:05',
    secciones=[
        hemograma(c2h),
        ('COAGULACIÓN', CIT, [
            ('Tiempo de protrombina (TP)', '11,8', '', 's', '10,5 – 13,5', 'Coagulométrico'),
            ('INR', '0,98', '', '', '0,85 – 1,15', 'Calculado (ISI)'),
            ('Fibrinógeno', '310', '', 'mg/dL', '200 – 400', 'Clauss')]),
        ('QUÍMICA SANGUÍNEA · METABOLISMO DE CARBOHIDRATOS', SUERO + ' / Plasma fluoruro', [
            ('Glucosa en ayunas', '86', '', 'mg/dL', '70 – 99', 'Hexoquinasa'),
            ('Hemoglobina glicosilada (HbA1c)', '5,2', '', '%', '4,0 – 5,6', 'HPLC (certificado NGSP)'),
            ('Insulina en ayunas', '6,1', '', 'µUI/mL', '2,6 – 24,9', QLA),
            ('Péptido C', '1,8', '', 'ng/mL', '1,1 – 4,4', QLA),
            ('Fructosamina', '230', '', 'µmol/L', '205 – 285', 'Colorimétrico'),
            ('Ácido úrico', '4,1', '', 'mg/dL', '2,4 – 5,7', 'Uricasa')]),
        ('PERFIL LIPÍDICO', SUERO, [
            ('Colesterol total', '214', 'H', 'mg/dL', '< 200', ENZ),
            ('Triglicéridos', '98', '', 'mg/dL', '< 150', ENZ),
            ('Colesterol HDL', '58', '', 'mg/dL', '> 50', 'Enzimático directo'),
            ('Colesterol LDL (medido)', '136', 'H', 'mg/dL', '< 130', 'Enzimático directo'),
            ('Apolipoproteína B', '92', '', 'mg/dL', '60 – 117', ITB),
            ('Apolipoproteína A1', '158', '', 'mg/dL', '108 – 225', ITB),
            ('Lipoproteína (a)', '64', 'H', 'mg/dL', '< 30', ITB)]),
        ('ELECTROLITOS Y MINERALES', SUERO, [
            ('Sodio', '138', '', 'mmol/L', '136 – 145', 'ISE indirecto'),
            ('Potasio', 'No procesado', '*', 'mmol/L', '3,5 – 5,1', 'ISE indirecto'),
            ('Cloro', '104', '', 'mmol/L', '98 – 107', 'ISE indirecto'),
            ('Bicarbonato (CO₂ total)', '24', '', 'mmol/L', '22 – 29', ENZ),
            ('Calcio total', '9,2', '', 'mg/dL', '8,6 – 10,2', 'Arsenazo III'),
            ('Fósforo', '3,6', '', 'mg/dL', '2,5 – 4,5', 'Fosfomolibdato'),
            ('Magnesio', '1,9', '', 'mg/dL', '1,7 – 2,4', 'Azul de xilidilo'),
            ('Zinc', '71', '', 'µg/dL', '60 – 120', 'Colorimétrico'),
            ('Osmolalidad sérica', '286', '', 'mOsm/kg', '275 – 295', 'Descenso crioscópico')]),
        ('FUNCIÓN HEPÁTICA Y PROTEÍNAS', SUERO, [
            ('ALT (TGP)', '18', '', 'U/L', '10 – 35', 'IFCC sin P5P'),
            ('AST (TGO)', '20', '', 'U/L', '10 – 35', 'IFCC sin P5P'),
            ('Gamma glutamil transferasa (GGT)', '14', '', 'U/L', '6 – 42', 'IFCC'),
            ('Fosfatasa alcalina', '62', '', 'U/L', '35 – 104', 'IFCC'),
            ('Bilirrubina total', '0,50', '', 'mg/dL', '0,30 – 1,20', 'Diazo'),
            ('Bilirrubina directa', '0,10', '', 'mg/dL', '0,00 – 0,30', 'Diazo'),
            ('Proteínas totales', '7,0', '', 'g/dL', '6,4 – 8,3', 'Biuret'),
            ('Albúmina', '4,3', '', 'g/dL', '3,5 – 5,2', 'Verde de bromocresol'),
            ('Globulinas (calculado)', '2,7', '', 'g/dL', '2,0 – 3,5', 'Calculado'),
            ('Relación albúmina/globulina', '1,59', '', '', '1,10 – 2,50', 'Calculado'),
            ('Lactato deshidrogenasa (LDH)', '160', '', 'U/L', '135 – 214', 'IFCC'),
            ('Creatina quinasa (CK)', '82', '', 'U/L', '26 – 192', 'IFCC')]),
        ('FUNCIÓN RENAL', SUERO, [
            ('Creatinina', '0,72', '', 'mg/dL', '0,50 – 0,90', 'Jaffé compensado (trazable IDMS)'),
            ('TFG estimada (CKD-EPI 2021)', '112', '', 'mL/min/1,73 m²', '> 60', 'Calculado'),
            ('Nitrógeno ureico (BUN)', '10', '', 'mg/dL', '6 – 20', 'Ureasa'),
            ('Relación BUN/creatinina', '13,9', '', '', '10 – 20', 'Calculado')]),
        ('TIROIDES Y HORMONAS', SUERO, [
            ('TSH', '6,90', 'H', 'µUI/mL', '0,27 – 4,20', QLA),
            ('Testosterona total', '32', '', 'ng/dL', '8 – 48', QLA),
            ('SHBG', '62', '', 'nmol/L', '24,6 – 122,0', QLA),
            ('FSH', '6,1', '', 'mUI/mL', 'Fase folicular 3,5 – 12,5', QLA),
            ('LH', '5,4', '', 'mUI/mL', 'Fase folicular 2,4 – 12,6', QLA),
            ('Estradiol', '68', '', 'pg/mL', 'Fase folicular 12,5 – 166,0', QLA),
            ('Progesterona', '0,4', '', 'ng/mL', 'Fase folicular 0,06 – 0,89', QLA),
            ('Prolactina', '14,2', '', 'ng/mL', '4,8 – 23,3', QLA),
            ('DHEA-S', '180', '', 'µg/dL', '98,8 – 340,0', QLA),
            ('Cortisol (toma 07:40)', '11,6', '', 'µg/dL', '6,2 – 19,4 (mañana)', QLA),
            ('ACTH', '18', '', 'pg/mL', '7,2 – 63,3 (mañana)', QLA),
            ('IGF-1', '205', '', 'ng/mL', '115 – 307 (30 – 34 años)', QLA)]),
        ('PRUEBAS REFLEJAS', SUERO, [
            ('T4 libre · refleja por TSH fuera de rango', '1,02', '', 'ng/dL', '0,93 – 1,70', QLA),
            ('T3 libre · refleja por TSH fuera de rango', '3,0', '', 'pg/mL', '2,0 – 4,4', QLA),
            ('Anti-TPO · refleja por TSH alta', '186', 'H', 'UI/mL', '< 34', QLA),
            ('Reticulocitos % · refleja por anemia', '1,1', '', '%', '0,5 – 2,0', CIT_F),
            ('Reticulocitos absolutos · refleja por anemia', '47', '', 'x10³/µL', '25 – 75', 'Calculado'),
            ('IgA total · refleja por déficit de hierro', '210', '', 'mg/dL', '70 – 400', ITB),
            ('Anti-transglutaminasa IgA · refleja por déficit de hierro', '2,1', '', 'U/mL', '< 7,0 (negativo)', QLA),
            ('Ácido metilmalónico · refleja por B12 entre 180 y 350', '0,28', '', 'µmol/L', '0,00 – 0,40', 'LC-MS/MS')]),
        ('MARCADORES CARDIOVASCULARES E INFLAMACIÓN', SUERO, [
            ('Proteína C reactiva ultrasensible', '0,8', '', 'mg/L', '< 3,0', ITB),
            ('Velocidad de sedimentación globular', '18', '', 'mm/h', '0 – 20', 'Westergren'),
            ('Homocisteína', '13,9', '', 'µmol/L', '5,0 – 15,0', 'Enzimático'),
            ('Troponina I de alta sensibilidad', '< 3', '', 'ng/L', '< 14 (percentil 99)', QLA),
            ('Anticuerpos antinucleares (ANA)', 'Positivo 1:160', '*', '', 'Negativo (< 1:80)', 'IFI en células HEp-2')]),
        ('INMUNOLOGÍA', SUERO, [
            ('Inmunoglobulina G (IgG)', '1050', '', 'mg/dL', '700 – 1600', ITB),
            ('Inmunoglobulina M (IgM)', '140', '', 'mg/dL', '40 – 230', ITB)]),
        ('METABOLISMO DEL HIERRO', SUERO, [
            ('Ferritina', '7', 'L', 'ng/mL', '13 – 150', QLA),
            ('Hierro sérico', '38', 'L', 'µg/dL', '50 – 170', 'Ferrozina'),
            ('Capacidad total de fijación de hierro (TIBC)', '432', '', 'µg/dL', '250 – 450', 'Directo'),
            ('Transferrina', '346', '', 'mg/dL', '200 – 360', ITB),
            ('Saturación de transferrina (calculado)', '8,8', 'L', '%', '15 – 50', 'Calculado')]),
        ('VITAMINAS', SUERO + ' / Plasma heparina (vitamina C)', [
            ('Vitamina B12', '262', '', 'pg/mL', '197 – 771', QLA),
            ('Ácido fólico', '6,2', '', 'ng/mL', '> 3,9', QLA),
            ('25-hidroxivitamina D', '17,8', 'L', 'ng/mL', '30 – 100', QLA),
            ('Vitamina B6 (piridoxal 5-fosfato)', '6,0', '', 'µg/L', '5,0 – 50,0', 'HPLC'),
            ('Vitamina B1 (tiamina)', '102', '', 'nmol/L', '70 – 180', 'HPLC'),
            ('Vitamina A (retinol)', '41', '', 'µg/dL', '30 – 80', 'HPLC'),
            ('Vitamina E (alfa-tocoferol)', '9,8', '', 'mg/L', '5,5 – 17,0', 'HPLC'),
            ('Vitamina K1 (filoquinona)', '0,35', '', 'ng/mL', '0,10 – 2,20', 'HPLC'),
            ('Vitamina C (ácido ascórbico)', 'Muestra no apta', '*', 'mg/dL', '0,4 – 2,0', 'HPLC'),
            ('Biotina (vitamina B7)', '380', '', 'ng/L', 'No establecido', 'Inmunoensayo'),
            ('Niacina (vitamina B3)', '4,4', '', 'µg/mL', 'No establecido', 'LC-MS/MS'),
            ('Índice omega-3', '5,3', '', '%', 'No establecido', 'Cromatografía de gases'),
            ('Relación omega-6/omega-3', '8,9', '', '', 'No establecido', 'Cromatografía de gases'),
            ('Coenzima Q10', '0,64', '', 'µg/mL', 'No establecido', 'HPLC')]),
        ('SEROLOGÍA E INFECCIOSAS', SUERO, [
            ('Anticuerpos contra hepatitis C (anti-VHC)', 'No reactivo (0,05)', '', 'índice', '< 1,00', QLA),
            ('Antígeno de superficie hepatitis B (HBsAg)', 'No reactivo (0,28)', '', 'índice', '< 1,00', QLA),
            ('Anticuerpos contra antígeno de superficie (anti-HBs)', '85', '', 'mUI/mL', '≥ 10 (inmunidad)', QLA),
            ('Anticuerpos totales contra core hepatitis B (anti-HBc)', 'No reactivo (0,09)', '', 'índice', '< 1,00', QLA),
            ('Anticuerpos IgG Trypanosoma cruzi (Chagas)', 'No reactivo (0,18)', '', 'índice', '< 0,90', 'ELISA')]),
        ('UROANÁLISIS', ORINA, [
            ('Color', 'Amarillo', '', '', 'Amarillo', 'Visual'), ('Aspecto', 'Claro', '', '', 'Claro', 'Visual'),
            ('Densidad', '1,015', '', '', '1,005 – 1,030', 'Tira reactiva'), ('pH', '6,5', '', '', '5,0 – 8,0', 'Tira reactiva'),
            ('Proteínas', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Glucosa', 'Negativo', '', '', 'Negativo', 'Tira reactiva'),
            ('Cuerpos cetónicos', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Sangre', 'Negativo', '', '', 'Negativo', 'Tira reactiva'),
            ('Nitritos', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Esterasa leucocitaria', 'Negativo', '', '', 'Negativo', 'Tira reactiva'),
            ('Bilirrubina', 'Negativo', '', '', 'Negativo', 'Tira reactiva'), ('Urobilinógeno', '0,2', '', 'mg/dL', '0,2 – 1,0', 'Tira reactiva'),
            ('Sedimento · leucocitos', '0 – 2', '', '/campo', '0 – 5', 'Microscopía'), ('Sedimento · hematíes', '0 – 2', '', '/campo', '0 – 3', 'Microscopía'),
            ('Sedimento · células epiteliales', 'Escasas', '', '', 'Escasas', 'Microscopía'), ('Sedimento · bacterias', 'No se observan', '', '', 'Escasas', 'Microscopía'),
            ('Sedimento · cilindros', 'No se observan', '', '', 'No se observan', 'Microscopía'),
            ('Sedimento · cristales', 'No se observan', '', '', 'No se observan', 'Microscopía'),
            ('Albúmina en orina', '5', '', 'mg/L', '', ITB), ('Creatinina en orina', '65', '', 'mg/dL', '', 'Jaffé'),
            ('Relación albúmina/creatinina (RAC)', '8', '', 'mg/g', '< 30', 'Calculado')]),
        ('COPROLÓGICO Y PRUEBAS EN HECES', HECES, [
            ('Sangre oculta en heces (inmunoquímica, FIT)', 'Negativo', '', '', 'Negativo', 'Inmunocromatografía'),
            ('Antígeno de Helicobacter pylori en heces', 'Negativo', '', '', 'Negativo', 'Inmunoensayo monoclonal'),
            ('Coprológico · consistencia', 'Formada', '', '', '', 'Macroscópico'),
            ('Coprológico · color', 'Café', '', '', '', 'Macroscópico'),
            ('Coprológico · moco', 'Negativo', '', '', 'Negativo', 'Macroscópico'),
            ('Coprológico · parásitos', 'No se observaron parásitos', '', '', '', 'Directo y lugol')]),
    ],
    obs=['Potasio no procesado: muestra hemolizada. Se solicita nueva muestra; el resultado no se informa para evitar un valor falsamente alto.',
         'Vitamina C: muestra no apta, llegó refrigerada y la prueba exige plasma congelado protegido de la luz.',
         'ANA positivo 1:160, patrón moteado fino (AC-4). Un título bajo puede encontrarse en personas sanas; se informa título y patrón para interpretación clínica.',
         'Pruebas reflejas activadas: T4 libre, T3 libre y anti-TPO por TSH alta; reticulocitos por anemia; IgA total y anti-transglutaminasa IgA por déficit de hierro; ácido metilmalónico por vitamina B12 entre 180 y 350 pg/mL.',
         'Fecha de última menstruación informada: 23/09/2026 (día 9 del ciclo). Intervalos hormonales de fase folicular. Sin anticonceptivo hormonal.',
         'Documento generado por Saludly como ejemplo de formato. Laboratorio, paciente, documento y resultados son ficticios.'])

if __name__ == '__main__':
    build(caso1, '/home/claude/saludly/Ejemplo_resultados_LCD-2026-100123_hombre.pdf')
    build(caso2, '/home/claude/saludly/Ejemplo_resultados_LCD-2026-100124_mujer.pdf')
    print('ok')
