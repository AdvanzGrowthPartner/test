#!/usr/bin/env python3
"""Clasifica un export de Search Console en cubos de acción.

Uso:
  python3 gsc_cubos.py Páginas.csv            # export de Rendimiento → pestaña Páginas (o Consultas)
  python3 gsc_cubos.py Páginas.csv --min-imp 100

Cubos (en orden de prioridad para operar):
  GANA      pos ≤ 3 con clics            → proteger: enlazar a PDP/oferta, no tocar el título
  CASI      pos 4–15 y muchas impresiones → empujar: ampliar contenido, enlaces internos, FAQ
  CTR_BAJO  pos ≤ 10 y CTR bajo lo esperado → snippet: meta description, schema FAQ, fecha
  NO_RINDE  pos > 15 o casi sin impresiones → consolidar, redirigir o reescribir
"""
import csv, sys, argparse

# CTR esperado aproximado por posición (curva conservadora); bajo la mitad = CTR_BAJO
CTR_ESPERADO = {1: .25, 2: .13, 3: .09, 4: .06, 5: .045, 6: .035, 7: .028, 8: .023, 9: .019, 10: .016}

def num(s):
    s = (s or '').strip().replace('%', '').replace(' ', '')
    if s.count(',') == 1 and s.count('.') == 0:
        s = s.replace(',', '.')
    else:
        s = s.replace(',', '')
    try:
        return float(s)
    except ValueError:
        return 0.0

def leer(path):
    with open(path, encoding='utf-8-sig') as f:
        r = csv.reader(f)
        head = next(r)
        for row in r:
            if row:
                yield dict(zip(head, row))

def campo(d, *nombres):
    for k in d:
        if k.strip().lower() in nombres:
            return d[k]
    return ''

def cubo(pos, clics, imp, ctr, min_imp):
    if pos <= 3 and clics > 0:
        return 'GANA'
    if pos <= 10 and imp >= min_imp and ctr < CTR_ESPERADO.get(max(1, round(pos)), .016) / 2:
        return 'CTR_BAJO'
    if 4 <= pos <= 15 and imp >= min_imp:
        return 'CASI'
    return 'NO_RINDE'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('csv')
    ap.add_argument('--min-imp', type=int, default=100)
    a = ap.parse_args()
    filas = []
    for d in leer(a.csv):
        url = campo(d, 'páginas principales', 'top pages', 'consultas principales', 'top queries', 'página', 'consulta')
        clics, imp = num(campo(d, 'clics', 'clicks')), num(campo(d, 'impresiones', 'impressions'))
        ctr, pos = num(campo(d, 'ctr')) / 100, num(campo(d, 'posición', 'position'))
        filas.append((cubo(pos, clics, imp, ctr, a.min_imp), url, clics, imp, ctr, pos))
    orden = ['GANA', 'CASI', 'CTR_BAJO', 'NO_RINDE']
    for c in orden:
        sel = sorted([f for f in filas if f[0] == c], key=lambda f: -f[3])
        print(f'\n## {c} ({len(sel)})\n')
        print('| URL / consulta | Clics | Impresiones | CTR | Posición |\n|---|---:|---:|---:|---:|')
        for _, u, cl, im, ct, po in sel[:25]:
            print(f'| {u} | {cl:,.0f} | {im:,.0f} | {ct:.1%} | {po:.1f} |')

if __name__ == '__main__':
    main()
