"""Arma las tablas del Command de un área a partir de las dos marcas.

Uso: python3 ops/_command/exportar.py <área>        (o "todas")
Lee ops/<área>/<marca>/os-data.json, CHANGELOG.md y ops/handoffs.md.
Escribe ops/<área>/command/{kpis,fugas,accesos,cambios,handoffs}.json:
arrays de filas con la columna `marca`, listas para subir como datasets
del Dashboard "<Área> OS · Command".
"""
import json
import re
import sys
from pathlib import Path

OPS = Path(__file__).resolve().parents[1]
MARCAS = {"advanz": "Advanz", "amazingcare": "AmazingCare"}
AREAS = ["email", "ads", "cro", "growth", "creative", "geo-seo"]


def os_data(area, g):
    p = OPS / area / g / "os-data.json"
    if p.exists():
        return json.loads(p.read_text())
    semilla = OPS / "growth" / "command-center" / "semillas" / f"{g}.{area}.json"
    return json.loads(semilla.read_text()) if semilla.exists() else {}


def cambios(area, g):
    p = OPS / area / g / "CHANGELOG.md"
    filas = []
    if not p.exists():
        return filas
    seccion = None  # formato alternativo: "## AAAA-MM-DD · motivo" seguido de viñetas
    for linea in p.read_text().splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) >= 4 and re.match(r"\d{4}-\d{2}-\d{2}", celdas[0]):
            filas.append({"marca": MARCAS[g], "fecha": celdas[0], "cambio": celdas[1],
                          "por_que": celdas[2], "revertir": celdas[3]})
            continue
        m = re.match(r"##\s+(\d{4}-\d{2}-\d{2})\s*·\s*(.*)", linea)
        if m:
            seccion = m.groups()
        elif linea.startswith("## "):
            seccion = None
        elif seccion and linea.startswith("- "):
            texto, _, revertir = linea[2:].partition("*Revertir:*")
            filas.append({"marca": MARCAS[g], "fecha": seccion[0], "cambio": texto.replace("**", "").strip(),
                          "por_que": seccion[1], "revertir": revertir.strip()})
    return filas


def handoffs(area):
    p = OPS / "handoffs.md"
    filas = []
    for linea in p.read_text().splitlines() if p.exists() else []:
        m = re.match(r"- \[( |x)\] (\d{4}-\d{2}-\d{2}) · de (\S+) → para (\S+?): (.*)", linea)
        if not m or m.group(1) == "x":
            continue
        para = m.group(4)
        if para.split("/")[0] != area and para.split("/")[-1] != area:
            continue
        marca = next((v for k, v in MARCAS.items() if k in para), "Ambas")
        filas.append({"marca": marca, "fecha": m.group(2), "de": m.group(3), "pedido": m.group(5)[:400]})
    return filas


def exportar(area):
    t = {"kpis": [], "fugas": [], "accesos": [], "cambios": [], "handoffs": handoffs(area)}
    for g, marca in MARCAS.items():
        d = os_data(area, g)
        fuente = d.get("fuente", "sin-datos")
        for k in d.get("kpis", []):
            t["kpis"].append({"marca": marca, "id": f"{g}.{k.get('id')}", "nombre": k.get("nombre"),
                              "valor": k.get("valor"), "unidad": k.get("unidad"), "periodo": k.get("periodo"),
                              "meta": k.get("meta"), "estado": k.get("estado"), "fuente": k.get("fuente"),
                              "actualizado": d.get("actualizado"), "origen": fuente})
        for f in d.get("fugas", []):
            a = f.get("accion", {})
            t["fugas"].append({"marca": marca, "id": f.get("id"), "titulo": f.get("titulo"),
                               "severidad": f.get("severidad"), "estado": f.get("estado"),
                               "punto_funnel": f.get("punto_funnel"), "evidencia": f.get("evidencia"),
                               "impacto": f.get("impacto_nota"), "accion": a.get("descripcion"),
                               "ejecuta": a.get("os_ejecutor"), "via": a.get("via"), "conector": a.get("conector"),
                               "requiere_ok": bool(a.get("requiere_ok")), "acceso": a.get("acceso")})
        for x in d.get("accesos", []):
            t["accesos"].append({"marca": marca, "conector": x.get("conector"), "estado": x.get("estado"),
                                 "nota": x.get("nota")})
        t["cambios"] += cambios(area, g)
    t["fugas"].sort(key=lambda f: (f["estado"] == "resuelta", -(f["severidad"] or 0)))
    t["cambios"].sort(key=lambda c: c["fecha"], reverse=True)
    out = OPS / area / "command"
    out.mkdir(exist_ok=True)
    for nombre, filas in t.items():
        (out / f"{nombre}.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n")
    print(f"{area}: " + " · ".join(f"{n} {len(v)}" for n, v in t.items()))


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "todas"
    for a in (AREAS if arg == "todas" else [arg]):
        exportar(a)
