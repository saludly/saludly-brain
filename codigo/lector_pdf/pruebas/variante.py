"""Genera un PDF variante con errores sembrados para probar las dudas del lector."""
import copy, sys, os, json
sys.path.insert(0, '/home/claude/saludly'); import pdf_ejemplo as P
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, BASE); import lector, yaml
c = copy.deepcopy(P.caso1)
for i,(t,m,filas) in enumerate(c['secciones']):
    filas=list(filas)
    for j,f in enumerate(filas):
        if f[0]=='Glucosa en ayunas': filas[j]=('Glucosa en ayunas','6,2','H','mmol/L','3,9 – 5,5','Hexoquinasa')
        if f[0]=='Ácido úrico': filas[j]=('Ácido úrico','450','H','µmol/L','200 – 420','Uricasa')
    if t.startswith('PERFIL'): filas.append(('Lipoproteína X','12','','mg/dL','< 5','Electroforesis')); filas.append(('Triglicéridos','240','H','mg/dL','< 150','Enzimático'))
    c['secciones'][i]=(t,m,filas)
P.build(c, f'{BASE}/pruebas/variante.pdf')
idx=json.load(open(f'{BASE}/00_INDEX.json',encoding='utf-8')); conv=yaml.safe_load(open(f'{BASE}/unidades.yaml',encoding='utf-8'))
r=lector.leer(f'{BASE}/pruebas/variante.pdf', {'documento':'CC 0000000001','orden':'LCD-2026-100123'}, idx, conv)
g=[x for x in r['resultados'] if x['nombre_original']=='Glucosa en ayunas'][0]
print('Glucosa en mmol/L:', g['valor'], g['unidad'], '->', g.get('valor_canonico'), g.get('unidad_canonica'))
for d in r['dudas']: print('  duda:', d)
