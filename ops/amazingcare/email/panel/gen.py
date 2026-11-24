import json, html, datetime as dt
E = html.escape
HEAD = open('head.html').read()
CSS = '''<style>
.tabs.main{position:sticky;top:0;z-index:20;background:var(--bg);padding-top:6px;margin-top:-6px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px}
.kpi{background:var(--surf2);border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:2px}
.kpi .v{font-family:'IBM Plex Mono',monospace;font-size:22px;font-weight:600;color:var(--ink);line-height:1.1}
.kpi .v.bad{color:var(--bad)}.kpi .v.ok{color:var(--ok)}.kpi .v.warn{color:var(--warn)}
.kpi .k{font-size:11px;color:var(--mut);line-height:1.25}.kpi .d{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--faint)}
.leg{display:flex;flex-wrap:wrap;gap:12px;font-size:11px;color:var(--mut)}
.leg span{display:inline-flex;align-items:center;gap:5px}.leg b{width:14px;height:3px;border-radius:2px;display:inline-block}
.tl{display:flex;gap:6px;overflow-x:auto;padding-bottom:4px}
.tl .d{flex:1 0 96px;border-radius:9px;padding:9px;background:var(--surf2);display:flex;flex-direction:column;gap:4px;min-width:96px}
.tl .d b{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--ink)}.tl .d span{font-size:11px;color:var(--text);line-height:1.25}
.tl .d.on{box-shadow:inset 0 0 0 2px var(--acc)}.tl .d.ev{background:color-mix(in srgb,var(--acc) 12%,transparent)}
.ans{display:grid;grid-template-columns:110px 1fr;gap:6px 12px;font-size:12.5px}
.ans dt{font-family:'IBM Plex Sans Condensed',sans-serif;font-weight:600;color:var(--ink)}.ans dd{margin:0;color:var(--text)}
@media(max-width:600px){.ans{grid-template-columns:1fr}}
svg text{font-family:'IBM Plex Mono',monospace}
</style>'''

def fmtM(v):  # CLP millions
    return f'{v/1e6:.1f}'.replace('.', ',') + 'M'
def fmtN(v):
    return f'{v:,.0f}'.replace(',', '.')

def line_chart(series, xlabels, ymax, yfmt, w=900, h=230, ytick=None, marks=None, aria=''):
    """series: list of (name,color,values[None allowed],dash). horizontal time axis."""
    L, R, T, B = 48, 12, 12, 34
    n = len(xlabels)
    X = lambda i: L + (w - L - R) * (i / (n - 1) if n > 1 else 0)
    Y = lambda v: T + (h - T - B) * (1 - v / ymax)
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(aria)}">']
    ticks = ytick or [ymax * k / 4 for k in range(5)]
    for t in ticks:
        out.append(f'<line x1="{L}" y1="{Y(t):.1f}" x2="{w-R}" y2="{Y(t):.1f}" stroke="var(--grid)"/>'
                   f'<text x="{L-6}" y="{Y(t)+3:.1f}" text-anchor="end" font-size="9" fill="var(--faint)">{yfmt(t)}</text>')
    step = max(1, n // 12)
    for i, lb in enumerate(xlabels):
        if i % step == 0 or i == n - 1:
            out.append(f'<text x="{X(i):.1f}" y="{h-14}" text-anchor="middle" font-size="9" fill="var(--faint)">{E(lb)}</text>')
    for (i, lab) in (marks or []):
        out.append(f'<line x1="{X(i):.1f}" y1="{T}" x2="{X(i):.1f}" y2="{h-B}" stroke="var(--line)" stroke-dasharray="3 3"/>'
                   f'<text x="{X(i)+3:.1f}" y="{T+9}" font-size="9" fill="var(--mut)">{E(lab)}</text>')
    for name, col, vals, dash in series:
        pts = [(X(i), Y(v), v, i) for i, v in enumerate(vals) if v is not None]
        if not pts: continue
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y, _, _ in pts)
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.2" stroke-linejoin="round" {"stroke-dasharray=\"5 4\"" if dash else ""}/>')
        for x, y, v, i in pts:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{col}"><title>{E(name)} · {E(xlabels[i])} · {yfmt(v)}</title></circle>')
    out.append('</svg>')
    return ''.join(out)

def legend(items):
    return '<div class="leg">' + ''.join(f'<span><b style="background:{c}{";height:0;border-top:2px dashed "+c if d else ""}"></b>{E(n)}</span>' for n, c, *rest in items for d in [rest[0] if rest else False]) + '</div>'

def hbars(rows, lw=130, maxv=None):
    """rows: (label, small, value, valtext, cls)"""
    m = maxv or max(r[2] for r in rows) or 1
    o = [f'<div class="bars" style="--lw:{lw}px">']
    for lb, sm, v, vt, cls in rows:
        wpct = max(0.8, 100 * v / m) if v else 0
        bar = f'<i class="{cls}" style="width:{wpct:.1f}%"></i>' if v else '<i class="z"></i>'
        vc = ' bad' if cls == 'bad' else (' ok' if cls == 'ok' else '')
        o.append(f'<div class="bar"><span class="lb">{E(lb)}{f"<small>{E(sm)}</small>" if sm else ""}</span><div class="trk">{bar}</div><span class="vl{vc}">{E(vt)}</span></div>')
    o.append('</div>')
    return ''.join(o)

def kpis(items):
    return '<div class="kpis">' + ''.join(f'<div class="kpi"><span class="v {c}">{E(v)}</span><span class="k">{E(k)}</span><span class="d">{E(d)}</span></div>' for v, k, d, c in items) + '</div>'

def card(cid, span, title, sub, body, verdict=''):
    v = f'<div class="verdict">{verdict}</div>' if verdict else ''
    return f'<div class="card c{span}" id="{cid}"><div class="ch"><h3>{E(title)}</h3><span class="sub">{E(sub)}</span></div>{body}{v}</div>'

def table(head, rows, minw=640):
    th = ''.join(f'<th class="{"r" if h.startswith(">") else ""}">{E(h.lstrip(">"))}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td class="{c}">{v}</td>' for v, c in r) + '</tr>' for r in rows)
    return f'<div class="sc"><table class="tb" style="min-width:{minw}px"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def chip(t, c): return f'<span class="chip {c}">{E(t)}</span>'

C1, C2, C3, C4, C5 = 'var(--s1)', 'var(--s2)', 'var(--warn)', 'var(--ok)', 'var(--bad)'
P = []  # panels

# ───────────── DATA ─────────────
# Eventos: venta neta diaria Shopify, día 0 = inicio del evento
EV = {
 'Black 2025':    ('27-nov-2025', [279746,3300479,4219808,3423958,3260856,2663345,572076,307342], 6.18e6),
 'Cyber oct 2026':('2-oct-2026', [322199,1490959,2489024,3261208,5541188,2922345,3839856,1661063], 6.69e6),
 'Cyber jun 2026':('29-may-2026',[209215,3140219,4264795,3856905,4887814,3376640,4027415,1268128], 8.72e6),
 'Cyber oct 2025':('4-oct-2025', [655453,2604484,2430359,3966444,3634301,3342773,1870836,949183], None),
 'Flash jul 2026':('30-jul-2026',[166024,1112103,1024058,1331895,2666935,290933,0,0], None),
}
dl = ['día −1'] + [f'día {i}' for i in range(1, 8)]

# ───────────── EVENTOS ─────────────
ev_chart = line_chart([
    ('Black 2025', C1, EV['Black 2025'][1], False),
    ('Cyber oct 2026', C2, EV['Cyber oct 2026'][1], False),
    ('Cyber jun 2026', C4, EV['Cyber jun 2026'][1], False),
    ('Cyber oct 2025', 'var(--faint)', EV['Cyber oct 2025'][1], True),
    ('Flash jul 2026', C3, EV['Flash jul 2026'][1][:6], True),
], dl, 6e6, lambda v: fmtM(v), aria='Venta diaria de cada evento alineada por día de inicio')
evcmp = table(['Evento', '>Días', '>Venta neta', '>Órdenes', '>Mejor día', '>Email atribuido', '>% email'], [
    [('<b>Black 2025</b>', ''), ('5', 'r'), ('16,9M', 'r'), ('480', 'r'), ('4,2M', 'r'), ('6,2M', 'r'), ('37%', 'r ok')],
    [('<b>Cyber oct 2026</b>', ''), ('7', 'r'), ('21,2M', 'r'), ('540', 'r'), ('5,5M', 'r'), ('6,7M', 'r'), ('32%', 'r')],
    [('<b>Cyber jun 2026</b>', ''), ('6', 'r'), ('23,6M', 'r'), ('639', 'r'), ('4,9M', 'r'), ('8,7M', 'r'), ('37%', 'r ok')],
    [('Cyber oct 2025', ''), ('6', 'r'), ('17,9M', 'r'), ('520', 'r'), ('4,0M', 'r'), ('—', 'r'), ('—', 'r')],
    [('Flash jul 2026', ''), ('4', 'r'), ('6,1M', 'r'), ('163', 'r'), ('2,7M', 'r'), ('—', 'r'), ('—', 'r')],
], 620)
# proyección: Black 2026 = Black 2025 × factor
base25 = EV['Black 2025'][1][1:6]

pl = ['jue 27', 'vie 28', 'sáb 29', 'dom 30', 'lun 1']
proj_chart = line_chart([
    ('Riesgo', C5, [v * 0.8 for v in base25], True),
    ('Piso = Black 2025', C3, [v * 1.0 for v in base25], False),
    ('Base', C1, [v * 1.11 for v in base25], False),
    ('Techo', C4, [v * 1.20 for v in base25], False),
], pl, 6e6, fmtM, h=200, aria='Proyección diaria Black 2026 en tres escenarios')
projtab = hbars([
    ('Techo', '+20%, lo que creció octubre', 20.2e6, '20,2M · email 7,1M', 'ok'),
    ('Base', '+11%, Cyber oct 8 días vs 8 días', 18.7e6, '18,7M · email 6,2M', ''),
    ('Piso', 'igual a Black 2025', 16.9e6, '16,9M · email 5,4M', 'warn'),
    ('Riesgo', '−20%: bandeja débil, sin precalentar', 13.5e6, '13,5M · email 3,4M', 'bad'),
], 150)
cal = '<div class="tl">' + ''.join(f'<div class="d {c}"><b>{d}</b><span>{t}</span>{chip(s, k)}</div>' for d, t, s, k, c in [
    ('lun 24', 'PreBlack 1 · «Se acabó la espera»', 'enviado', 'ok', 'on'),
    ('por programar', 'Correo 2', 'aprobado', 'ok', ''),
    ('jue 27 · grilla', 'Black Friday · hasta 40% off', 'por aprobar', 'warn', 'ev'),
    ('lun 30 · grilla', 'Últimas horas', 'por aprobar', 'warn', 'ev'),
    ('jue–lun', 'Carritos Black (flujo)', 'falta diseño', 'bad', 'ev'),
]) + '</div>'
pre = hbars([
    ('PreBlack 1 · 24-nov', '10.895 dest · primeras horas', 3.1, 'abre 3,1%', 'warn'),
    ('Black Friday aviso · 24-nov-2025', '8.972 dest · cerrado', 29.97, 'abre 30,0%', ''),
    ('Promedio campañas nov 2026', '4 envíos cerrados', 25.2, 'abre 25,2%', ''),
], 190, 32)
P.append(('ev', 'Eventos', 'bad', ''.join([
    card('ev-kpis', 12, 'Black 2026', '24-nov · Black Friday el viernes 27', kpis([
        ('1 de 4', 'Correos de Black enviados', '2 de 4 aprobados', 'warn'),
        ('hasta 40%', 'Mecánica', 'descuento de Black 2026', ''),
        ('18,7M', 'Proyección base (CLP)', 'piso 16,9M · techo 20,2M', ''),
        ('16,9M', 'Black 2025 (CLP)', '5 días · 480 órdenes', ''),
        ('37%', 'Peso del email en Black 2025', '6,2M atribuidos', 'ok'),
        ('3,1%', 'Apertura PreBlack 1', 'primeras horas', 'warn'),
    ])),
    card('ev-calendario', 12, 'Calendario de envíos', 'semana de Black', cal),
    card('ev-curvas', 8, 'Venta diaria por evento', 'Shopify · CLP · día 1 = inicio', ev_chart + legend([
        ('Black 2025', C1), ('Cyber oct 2026', C2), ('Cyber jun 2026', C4), ('Cyber oct 2025', 'var(--faint)', True), ('Flash jul 2026', C3, True)]),
        'En total, los dos Cyber de 2026 <b>superaron a Black 2025</b>. Por día, Cyber jun lo pasó (3,9M/día) y Cyber oct quedó cerca (3,0M/día contra 3,4M).'),
    card('ev-proyeccion', 4, 'Proyección Black 2026', 'CLP · 27-nov → 1-dic', projtab,
        'El email aporta 32–37% en los eventos. El escenario base exige <b>que salgan los 4 correos</b>.'),
    card('ev-proy-dias', 7, 'Proyección día a día', 'escenarios sobre la curva de Black 2025', proj_chart + legend([
        ('Riesgo', C5, True), ('Piso = Black 2025', C3), ('Base', C1), ('Techo', C4)])),
    card('ev-preblack', 5, 'PreBlack 1 contra la vara', 'apertura', pre,
        'Se lee a las 48 h. Si cierra bajo 20%, la bandeja ya está cobrando los envíos de noviembre.'),
    card('ev-comparativa', 12, 'Comparativa de eventos', 'Shopify + Klaviyo (Placed Order atribuido)', evcmp),
])))

# ───────────── ANUAL ─────────────
m25 = [8210011,12649725,16014227,12801087,7217812,15085839,14456875,8954367,10493393,25466692,21721671,13783302]
m26 = [16467526,13466878,21935928,9261508,17900998,17614046,9064380,13101557,13218380,30476007,7415146,None]
mes = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
em = [None,None,None,None,None,None,None,None,None,None,None,5063937]  # dic-25
em26 = [4208419,5344857,7225472,2554954,6344047,5914346,3194433,4032599,3827240,9979111,1587031,None]
share = [round(100*e/s) if e and s else None for e, s in zip(em26, m26)]
an_chart = line_chart([('2025', 'var(--faint)', m25, True), ('2026', C1, m26, False)], mes, 32e6, fmtM,
                      marks=[(5, 'Cyber jun'), (9, 'Cyber oct'), (10, 'Black')], aria='Venta neta mensual 2025 contra 2026')
sh_chart = line_chart([('% email', C2, share, False)], mes, 50, lambda v: f'{v:.0f}%', h=170, ytick=[0, 25, 50], aria='Porcentaje de la venta atribuido a email por mes 2026')
ytd25 = sum(m25[:10]) + 7.0e6
ytd26 = sum(v for v in m26 if v)
P.append(('an', 'Anual', 'ok', ''.join([
    card('an-kpis', 12, 'El año en números', 'ene → 24-nov · Shopify + Klaviyo', kpis([
        (fmtM(ytd26), 'Venta neta 2026 (CLP)', f'2025 a la misma fecha: {fmtM(ytd25)}', 'ok'),
        (f'+{100*(ytd26/ytd25-1):.0f}%', 'Contra 2025', 'mismo período', 'ok'),
        (fmtM(sum(em26[:11])), 'Atribuido a email 2026', 'ene → 24-nov', ''),
        (f'{100*sum(em26[:11])/ytd26:.0f}%', 'Peso del email', 'promedio 2026', ''),
        ('30,5M', 'Mejor mes', 'octubre 2026 (Cyber)', 'ok'),
    ])),
    card('an-venta', 12, 'Venta neta mensual', 'Shopify · CLP · 2025 punteado', an_chart + legend([('2025', 'var(--faint)', True), ('2026', C1)]),
         'Los meses con evento hacen 2–3× un mes normal. <b>Noviembre lleva 7,4M</b>; con Black base cerraría en ~26M.'),
    card('an-email', 12, 'Peso del email en la venta', '% atribuido a email · 2026', sh_chart,
         'Entre 26% y 40% todo el año. <b>Noviembre cae a 21%</b>: 8 días sin envíos antes de Black.'),
])))

# ───────────── CAMPAÑAS ─────────────
S = [('25-ago',4371,29.6,166),('28-ago',4023,28.1,56),('31-ago',4397,29.8,18),('02-sep',4427,27.8,87),('04-sep',6688,27.7,60),('08-sep',7286,28.1,14),('10-sep',6723,29.0,49),('13-sep',7197,28.7,51),('15-sep',7221,27.8,90),('16-sep',7878,26.0,30),('23-sep',7878,27.1,9),('25-sep',7874,27.5,6),('27-sep',7870,27.1,28),('01-oct',7876,26.8,188),('02-oct',3053,24.7,146),('03-oct',10867,26.7,166),('05-oct',10708,25.3,240),('10-oct',10547,26.8,42),('11-oct',10543,25.9,65),('14-oct',10505,25.9,35),('17-oct',9452,26.4,6),('19-oct',10313,25.9,68),('26-oct',10931,25.3,32),('29-oct',10971,24.9,19),('04-nov',10959,25.7,51),('10-nov',10885,25.3,26),('13-nov',10928,24.8,10),('16-nov',10928,25.1,13)]
labs = [s[0] for s in S]
rpr_chart = line_chart([('RPR', C1, [s[3] for s in S], False)], labs, 250, lambda v: f'{v:.0f}', h=200, ytick=[0, 50, 100, 150, 200, 250],
                       marks=[(13, 'Cyber'), ], aria='Venta por destinatario de cada campaña')
or_chart = line_chart([('Apertura', C2, [s[2] for s in S], False)], labs, 32, lambda v: f'{v:.0f}%', h=170, ytick=[20, 24, 28, 32], aria='Apertura por campaña')
mon = table(['Mes', '>Envíos', '>Destinatarios', '>Abre', '>Clic', '>CLP', '>RPR'], [
    [('ago (desde 25)', 'm'), ('4', 'r'), ('13.370', 'r'), ('28,7%', 'r'), ('0,49%', 'r'), ('1,07M', 'r'), ('80', 'r')],
    [('sep', 'm'), ('14', 'r'), ('72.661', 'r'), ('27,5%', 'r'), ('0,22%', 'r'), ('3,02M', 'r'), ('42', 'r')],
    [('oct', 'm'), ('17', 'r'), ('111.091', 'r bad'), ('25,6%', 'r'), ('0,38%', 'r'), ('9,20M', 'r ok'), ('83', 'r')],
    [('nov (al 24)', 'm'), ('5', 'r'), ('54.595', 'r'), ('25,2%', 'r'), ('0,24%', 'r'), ('1,09M', 'r bad'), ('20', 'r bad')],
], 560)
noncom = hbars([
    ('Contenido no comercial planificado', 'meme, us vs them, prueba social, humor, disculpas', 8, '8', ''),
    ('Enviado', 'N01–N08 de la grilla', 0, '0', 'bad'),
    ('Pushes de venta enviados en su lugar', 'a la base completa', 5, '5', 'warn'),
], 210)
P.append(('ca', 'Campañas', 'warn', ''.join([
    card('ca-kpis', 12, 'Campañas', 'Klaviyo · Placed Order', kpis([
        ('25,2%', 'Apertura nov', 'sep 27,5%', 'warn'), ('0,24%', 'Clic nov', 'objetivo 1,5%', 'bad'),
        ('CLP 20', 'Por destinatario nov', 'oct 83', 'bad'), ('0 de 8', 'Correos no comerciales enviados', 'N01–N08', 'bad'),
        ('111k', 'Destinatarios oct', 'tope 80k', 'bad'),
    ])),
    card('ca-rpr', 12, 'Venta por destinatario, envío a envío', 'CLP · 25-ago → 16-nov', rpr_chart,
         'Solo los envíos con <b>evento y oferta</b> pasan de CLP 100. Las pushes de producto quedan bajo 30.'),
    card('ca-apertura', 7, 'Apertura, envío a envío', '%', or_chart),
    card('ca-mes', 5, 'Mes a mes', 'envíos principales + reenvíos', mon),
    card('ca-nocomercial', 12, 'Lo que se planificó para enganchar a la base', 'grilla de noviembre · pedido de Nacho', noncom,
         'Las piezas pensadas para recuperar interacción <b>no salieron</b>; salieron pushes de venta, que son las que bajan la reputación.'),
])))

# ───────────── FLUJOS ─────────────
fl = table(['Flujo · mensaje', 'Estado', '>Dest.', '>Abre', '>Clic', '>Ventas', '>CLP', '>RPR'], [
    [('<b>Welcome AON</b>', ''), (chip('borrador', 'bad'), ''), ('0', 'r'), ('—', 'r'), ('—', 'r'), ('0', 'r'), ('0', 'r'), ('—', 'r')],
    [('<b>Carritos AON · SEC1</b>', ''), (chip('vivo', 'ok'), ''), ('103', 'r'), ('52,0%', 'r'), ('6,0%', 'r'), ('6', 'r'), ('280.920', 'r'), ('2.809', 'r ok')],
    [('Carritos AON · SEC1 variación', ''), (chip('flojo', 'warn'), ''), ('54', 'r'), ('15,1%', 'r'), ('1,9%', 'r'), ('0', 'r'), ('0', 'r'), ('0', 'r')],
    [('<b>Carritos AON · SEC2</b>', ''), (chip('vivo', 'ok'), ''), ('34', 'r'), ('88,2%', 'r'), ('8,8%', 'r'), ('2', 'r'), ('79.162', 'r'), ('2.328', 'r ok')],
    [('<b>Carritos AON · SEC3</b>', ''), (chip('roto', 'bad'), ''), ('47', 'r'), ('21,7%', 'r'), ('0%', 'r bad'), ('0', 'r'), ('0', 'r'), ('0', 'r')],
    [('Post-compra', ''), (chip('flojo', 'warn'), ''), ('107', 'r'), ('51,4%', 'r'), ('1,0%', 'r'), ('1', 'r'), ('14.980', 'r'), ('143', 'r')],
    [('Recompra · email 1', ''), (chip('flojo', 'warn'), ''), ('456', 'r'), ('37,8%', 'r'), ('0,7%', 'r'), ('1', 'r'), ('93.980', 'r'), ('207', 'r')],
    [('<b>Recompra · email 2</b>', ''), (chip('roto', 'bad'), ''), ('507', 'r'), ('33,9%', 'r'), ('0%', 'r bad'), ('0', 'r'), ('0', 'r'), ('0', 'r')],
    [('Carritos Black', ''), (chip('falta diseño', 'warn'), ''), ('—', 'r'), ('—', 'r'), ('—', 'r'), ('—', 'r'), ('—', 'r'), ('—', 'r')],
    [('Nutrikit «NO USAR»', ''), (chip('ensucia', 'bad'), ''), ('18', 'r'), ('94%', 'r'), ('100%', 'r'), ('17', 'r'), ('0', 'r'), ('0', 'r')],
], 700)
fl_val = hbars([('Carritos AON', 'vivo', 360082, '360k', 'ok'), ('Recompra', 'vivo', 93980, '94k', ''), ('Post-compra', 'vivo', 14980, '15k', 'warn'), ('Welcome', 'apagado · sep 278k', 0, '0', 'bad')], 120)
diag = '''<dl class="ans">
<dt>Carrito SEC3</dt><dd>Es una copia de SEC2 (la plantilla se llama «CARRITO_AON_SEC2»). Tiene 3 imágenes sin link y <b>ningún botón para volver al carrito</b>. Lo único clickeable es la fila del producto. Promete «último día para usar tu descuento» y el correo no lleva al checkout.<br><b>Arreglo:</b> botón «Volver a mi carrito» al link del checkout y links en las imágenes.</dd>
<dt>Recompra 2</dt><dd>Es la <b>plantilla por defecto de Klaviyo, en inglés</b>: «Since you've been gone, a lot has changed», con productos automáticos y un botón «Visit the store». Les llega a ~500 compradores al mes.<br><b>Arreglo:</b> pieza en español con el producto que compró, una razón para reponer y un código; y renombrarla, porque se llama «Día 45» y sale el día 35.</dd>
</dl>'''
P.append(('fl', 'Flujos', 'bad', ''.join([
    card('fl-kpis', 12, 'Flujos', '30 días · 25-oct → 24-nov', kpis([
        ('469k', 'CLP de flujos', 'Carritos AON 360k', ''), ('2', 'Correos rotos', 'SEC3 y Recompra 2', 'bad'),
        ('apagado', 'Welcome', 'desde el 4-oct', 'bad'), ('falta diseño', 'Carritos Black', 'para el 27', 'warn'),
    ])),
    card('fl-valor', 5, 'Cuánto aporta cada flujo', 'CLP · 30 días', fl_val),
    card('fl-diag', 7, 'Qué tienen Recompra 2 y Carrito SEC3', 'revisado en la plantilla', diag),
    card('fl-tabla', 12, 'Mensaje por mensaje', '30 días', fl),
])))

# ───────────── ENTREGA ─────────────
op_chart = line_chart([('Apertura', C1, [s[2] for s in S] + [None], False)], labs + ['24-nov'], 32, lambda v: f'{v:.0f}%', h=180, ytick=[20, 24, 28, 32], aria='Apertura por campaña')
prov = hbars([('Office 365', '191 → 88', 54, '−54%', 'bad'), ('Gsuite', '188 → 148', 21, '−21%', 'warn'), ('Gmail', '3.529 → 2.988', 15, '−15%', 'warn'), ('Hotmail / Outlook', '459 → 416', 9, '−9%', ''), ('Apple', '106 → 99', 7, '−7%', 'ok')], 130, 60)
rep = hbars([('Base de envío', 'recibe las campañas', 10895, '10.895', ''), ('Sin interacción 30 días', 'Klaviyo sugiere excluir', 8890, '81,6% · ~8.900', 'bad'), ('Con interacción', 'quedarían', 2005, '~2.000', 'ok')], 170)
P.append(('en', 'Entrega', 'warn', ''.join([
    card('en-kpis', 12, 'Entrega', 'Klaviyo', kpis([
        ('99,7%', 'Entregados', 'rebote 0,28%', 'ok'), ('0,007%', 'Spam', 'umbral 0,1%', 'ok'),
        ('81,6%', 'Sin interacción en 30 días', 'Klaviyo sugiere excluirlos', 'bad'),
        ('−54%', 'Aperturas Office 365', 'oct → nov', 'bad'), ('25%', 'Apertura nov', 'sep 28%', 'warn'),
    ])),
    card('en-reputacion', 6, 'La alerta de Klaviyo', 'Mejora de la reputación · 24-nov', rep,
         'Excluirlos deja ~2.000 personas. Seguir enviándoles baja la reputación con cada push de venta.'),
    card('en-proveedor', 6, 'Aperturas por proveedor', 'perfiles únicos · oct → nov', prov),
    card('en-apertura', 12, 'Apertura envío a envío', '25-ago → 16-nov', op_chart,
         'El correo llega al servidor (99,7%) pero <b>cada vez menos a la bandeja principal</b>.'),
])))

# ───────────── CAPTURA ─────────────
cap_chart = line_chart([('Vistas del pop-up', C1, [119, 9784, 33, 15], False)], ['ago', 'sep', 'oct', 'nov'], 10000, lambda v: fmtN(v), h=170, aria='Vistas del formulario por mes')
alt_chart = line_chart([('Altas', C4, [4, 641, 216, 32], False)], ['ago', 'sep', 'oct', 'nov'], 700, lambda v: fmtN(v), h=170, aria='Suscripciones nuevas por mes')
P.append(('cp', 'Captura', 'bad', ''.join([
    card('cp-kpis', 12, 'Captura', 'Klaviyo · formularios', kpis([
        ('15', 'Vistas del pop-up en nov', 'sep: 9.784', 'bad'), ('32', 'Altas en nov', 'sep: 641', 'bad'),
        ('−95%', 'Altas sep → nov', '', 'bad'), ('abierto', 'Pedido a CRO', 'desde el 29-oct', 'warn'),
    ])),
    card('cp-vistas', 6, 'Vistas del pop-up', 'por mes', cap_chart),
    card('cp-altas', 6, 'Suscripciones nuevas', 'por mes', alt_chart),
    card('cp-plan', 12, 'Plan de diciembre', 'Plan 2 de Patricio', hbars([
        ('Beneficio de adquisición más fuerte', 'más volumen de base nueva al mes', 3, 'dic', ''),
        ('Capitalizar a los nuevos en 30 días', 'Welcome encendido', 2, 'dic', ''),
        ('Borrar audiencia muerta', 'baja costo de Klaviyo', 1, 'dic', ''),
    ], 260), 'En evento el pop-up no rinde; el foco de captura es diciembre.'),
])))

# ───────────── BASE ─────────────
rec = [9634, 9808, 10030, 10431, 10518, 11114, 11203, 11154, 11510, 11132, 11464, 11193]
rmes = ['dic', 'ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov']
vol = [83991, 74940, 75654, 68937, 50121, 73614, 107955, 117432, 58564, 74213, 112654, 55357]
b_chart = line_chart([('Perfiles que recibieron', C1, rec, False)], rmes, 12000, lambda v: f'{v/1000:.1f}k', h=170, ytick=[0, 4000, 8000, 12000], aria='Perfiles únicos que recibieron correos por mes')
v_chart = line_chart([('Correos recibidos', C2, vol, False)], rmes, 120000, lambda v: f'{v/1000:.0f}k', h=170, ytick=[0, 40000, 80000, 120000], marks=[(6, 'Cyber jun'), (10, 'Cyber oct')], aria='Correos recibidos por mes')
P.append(('ba', 'Base', 'warn', ''.join([
    card('ba-kpis', 12, 'Base', 'Klaviyo', kpis([
        ('~11,2k', 'Perfiles que reciben', 'nov', ''), ('~2.000', 'Con interacción en 30 días', '18,4%', 'bad'),
        ('~2,7k', 'Abren cada envío', 'campañas nov', 'warn'), ('9,8', 'Correos por perfil al mes', 'oct', 'bad'),
    ])),
    card('ba-tamano', 6, 'Tamaño de la base de envío', 'perfiles únicos por mes', b_chart, 'Creció 16% en el año; los que abren, no.'),
    card('ba-volumen', 6, 'Correos enviados por mes', 'Received Email', v_chart),
    card('ba-plan', 12, 'Plan para la base', 'propuesta de Patricio · cierre de diciembre', hbars([
        ('Plan 1 · motivo no comercial para abrir', 'beneficios, premios, sorteos internos, concursos', 3, 'dic', 'ok'),
        ('Plan 2 · adquisición + 30 días + limpiar', 'base nueva capitalizada y audiencia muerta fuera', 2, 'dic', ''),
        ('Excluir al 81,6% sin interacción', 'sugerencia de Klaviyo · deja ~2.000', 1, 'evaluar', 'warn'),
    ], 280), 'Va al reporte de cierre para monitorear y ajustar.'),
])))

# ───────────── RETENCIÓN ─────────────
nw = [286,433,386,291,178,296,303,184,168,494,374,257,319,238,356,171,272,284,164,248,240,465,96]
rt = [1,26,70,102,59,142,130,83,130,248,244,149,187,162,258,113,226,230,121,146,136,330,94]
ml = [f'{m}-{y}' for y in ('25', '26') for m in mes][:23]
rr = [round(100 * r / (n + r)) for n, r in zip(nw, rt)]
ret_chart = line_chart([('Nuevos', C2, nw, False), ('Recurrentes', C1, rt, False)], ml, 500, lambda v: fmtN(v), h=200, ytick=[0, 125, 250, 375, 500], aria='Clientes nuevos y recurrentes por mes')
rr_chart = line_chart([('% recurrentes', C4, rr, False)], ml, 60, lambda v: f'{v:.0f}%', h=160, ytick=[0, 20, 40, 60], aria='Porcentaje de clientes recurrentes por mes')
P.append(('re', 'Retención', 'warn', ''.join([
    card('re-kpis', 12, 'Retención', 'Shopify + Klaviyo', kpis([
        ('49%', 'Clientes recurrentes nov', '2025 nov: 39%', 'ok'), ('41%', 'Recurrentes promedio 2026', '2025: 27%', 'ok'),
        ('108k', 'CLP de post-compra + recompra', '30 días', 'warn'), ('1', 'Correo roto en recompra', 'email 2 en inglés', 'bad'),
    ])),
    card('re-clientes', 12, 'Clientes nuevos y recurrentes', 'Shopify · por mes', ret_chart + legend([('Nuevos', C2), ('Recurrentes', C1)])),
    card('re-tasa', 12, 'Peso de los recurrentes', '% de clientes del mes', rr_chart,
         'La recompra crece sola; los flujos de retención todavía no la capturan.'),
])))

# ───────────── RESUMEN ─────────────
res = table(['Tab', 'Métrica clave', 'Estado', 'Pendiente del OS'], [
    [('<b>Eventos</b>', ''), ('1 de 4 correos de Black enviados · proyección base 18,7M', ''), (chip('urgente', 'bad'), ''), ('Programar los 2 aprobados; cerrar diseño de Black Friday, Últimas horas y Carritos Black', '')],
    [('<b>Anual</b>', ''), (f'{fmtM(ytd26)} en 2026 · +{100*(ytd26/ytd25-1):.0f}% vs 2025', ''), (chip('bien', 'ok'), ''), ('—', '')],
    [('<b>Campañas</b>', ''), ('RPR nov CLP 20 · 0 de 8 correos no comerciales', ''), (chip('mal', 'bad'), ''), ('Grilla de diciembre con piezas no comerciales', '')],
    [('<b>Flujos</b>', ''), ('469k en 30 días · 2 correos rotos · Welcome apagado', ''), (chip('mal', 'bad'), ''), ('Arreglar SEC3 y Recompra 2; encender Welcome (OK)', '')],
    [('<b>Entrega</b>', ''), ('81,6% sin interacción en 30 días', ''), (chip('alerta', 'warn'), ''), ('Decidir exclusión después de Black; revisar DMARC y Postmaster', '')],
    [('<b>Captura</b>', ''), ('32 altas en nov (sep 641)', ''), (chip('mal', 'bad'), ''), ('Beneficio de adquisición para diciembre; pedido a CRO', '')],
    [('<b>Base</b>', ''), ('~2.000 con interacción de ~11k', ''), (chip('alerta', 'warn'), ''), ('Plan 1 y 2 de Patricio al reporte de cierre', '')],
    [('<b>Retención</b>', ''), ('49% recurrentes en nov', ''), (chip('bien', 'ok'), ''), ('Recompra 2 en español con código', '')],
], 720)
P.insert(0, ('rs', 'Resumen', 'warn', ''.join([
    card('rs-kpis', 12, 'Resumen', 'AmazingCare · 24-nov-2026', kpis([
        ('1 de 4', 'Correos de Black enviados', '2 aprobados', 'warn'),
        ('18,7M', 'Proyección Black (CLP)', 'piso 16,9M · techo 20,2M', ''),
        ('7,4M', 'Venta nov al 24 (CLP)', '+6% vs nov 2025', ''),
        ('21%', 'Peso del email en nov', f'promedio 2026: {100*sum(em26[:11])/ytd26:.0f}%', 'bad'),
        ('25,2%', 'Apertura nov', 'sep 27,5%', 'warn'),
        ('81,6%', 'Base sin interacción', '30 días', 'bad'),
        ('469k', 'CLP de flujos', '30 días', ''),
        ('32', 'Altas en nov', 'sep 641', 'bad'),
    ])),
    card('rs-tabs', 12, 'Cada tab y lo que queda pendiente', 'tareas del Email OS', res),
])))

# ───────────── ARMADO ─────────────
tabs = '<div class="tabs main" role="tablist" aria-label="Panel">' + ''.join(
    f'<button class="tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="p-{k}" id="t-{k}"><i class="{dot}"></i>{E(n)}</button>'
    for i, (k, n, dot, _) in enumerate(P)) + '</div>'
panels = ''.join(f'<div class="grid" id="p-{k}" role="tabpanel" aria-labelledby="t-{k}"{"" if i == 0 else " hidden"}>{body}</div>' for i, (k, n, dot, body) in enumerate(P))
foot = '''<footer><b>Fuentes, 24-nov-2026.</b> Shopify: venta neta diaria y mensual, clientes nuevos y recurrentes. Klaviyo: campañas y flujos con Placed Order (ventana de atribución de Klaviyo, es un techo), venta atribuida a email por fecha de compra, Received Email, Opened por proveedor y formularios. Proyección Black 2026: curva diaria de Black 2025 × 0,80 / 1,00 / 1,11 / 1,20; 1,11 es lo que creció Cyber oct (8 días contra 8 días) y 1,20 lo que creció octubre completo contra 2025. «Sin interacción 30 días»: alerta de reputación de Klaviyo. PreBlack 1 se leyó horas después del envío. El Command Center de Black no fue accesible desde esta sesión.</footer>'''
script = '''<script>(function(){var t=[].slice.call(document.querySelectorAll('.tab'));function s(i){t.forEach(function(b,j){b.setAttribute('aria-selected',j===i?'true':'false');document.getElementById(b.getAttribute('aria-controls')).hidden=j!==i;});try{history.replaceState(null,'','#'+t[i].id.slice(2));}catch(e){}window.scrollTo(0,0);}t.forEach(function(b,i){b.addEventListener('click',function(){s(i);});b.addEventListener('keydown',function(e){var n=null;if(e.key==='ArrowRight')n=(i+1)%t.length;if(e.key==='ArrowLeft')n=(i-1+t.length)%t.length;if(n!==null){e.preventDefault();s(n);t[n].focus();}});});var h=location.hash.slice(1);t.forEach(function(b,i){if(b.id==='t-'+h)s(i);});})();</script>'''
page = HEAD + CSS + '''
<div class="wrap">
<header><div class="hrow"><span class="eyebrow">Email OS · AmazingCare</span><span class="meta">actualizado 24-nov-2026 · Klaviyo + Shopify</span></div><h1>Panel del Motor de Correo</h1></header>
''' + tabs + panels + foot + '</div>' + script + '\n</body></html>'
open('index.html', 'w').write(page)
print(len(page), [p[1] for p in P], fmtM(ytd26), fmtM(ytd25))
