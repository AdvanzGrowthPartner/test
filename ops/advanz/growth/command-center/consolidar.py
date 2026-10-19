"""Consolida los os-data.json de los 12 OS y arma las vistas del Command Center.

Uso: python3 ops/advanz/growth/command-center/consolidar.py
Lee ops/<grupo>/<área>/os-data.json; si un OS no lo tiene, usa su semilla.
Escribe consolidado/{fugas,oportunidades,accesos,cobertura,kpis}.json.
Contrato: CONTRATO.md (misma carpeta).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
OPS = AQUI.parents[2]
GRUPOS = ["advanz", "amazingcare"]
AREAS = ["email", "ads", "cro", "growth", "creative", "geo-seo"]
ETAPAS = ["foundations", "offer", "validation", "acquisition", "workflows", "retention", "feedback", "systems"]
PUNTOS = ["trafico", "captura", "pdp", "carrito", "checkout", "recompra", "lead", "agenda", "cierre", "medicion", "contenido"]
ACCESOS = ["ok", "sin-probar", "bloqueado", "sin-conector", "sin-plan"]
VIAS = ["mcp", "cowork", "manual"]


def cargar():
    datos, errores = [], []
    for g in GRUPOS:
        for a in AREAS:
            propio = OPS / g / a / "os-data.json"
            semilla = AQUI / "semillas" / f"{g}.{a}.json"
            ruta = propio if propio.exists() else semilla if semilla.exists() else None
            if ruta is None:
                errores.append(f"{g}.{a}: sin os-data.json ni semilla")
                continue
            d = json.loads(ruta.read_text())
            d["_ruta"] = str(ruta.relative_to(OPS.parent))
            errores += validar(d)
            datos.append(d)
    return datos, errores


def validar(d):
    e, oid = [], d.get("os_id", "?")
    for f in d.get("fugas", []):
        acc = f.get("accion", {})
        checks = [("etapa", f.get("etapa"), ETAPAS), ("punto_funnel", f.get("punto_funnel"), PUNTOS),
                  ("accion.via", acc.get("via"), VIAS), ("accion.acceso", acc.get("acceso"), ACCESOS),
                  ("accion.os_ejecutor", acc.get("os_ejecutor"), AREAS)]
        for campo, valor, permitidos in checks:
            if valor not in permitidos:
                e.append(f"{oid} {f.get('id')}: {campo}='{valor}' fuera del vocabulario")
        if not 1 <= int(f.get("severidad", 0)) <= 5:
            e.append(f"{oid} {f.get('id')}: severidad fuera de 1–5")
    return e


def oportunidades(fugas):
    """Une fugas abiertas de una marca cuando una depende de otra o le pega en el mismo punto del funnel."""
    padre = {f["id"]: f["id"] for f in fugas}

    def raiz(x):
        while padre[x] != x:
            padre[x] = padre[padre[x]]
            x = padre[x]
        return x

    def unir(a, b):
        if a in padre and b in padre:
            padre[raiz(a)] = raiz(b)

    for f in fugas:
        for dep in f["depende_de"]:
            unir(f["id"], dep)
    for f in fugas:  # f afecta a otra área que tiene su propia fuga en el mismo punto del funnel
        for g in fugas:
            if g["id"] != f["id"] and g["marca"] == f["marca"] and g["area"] in f["afecta_os"] \
                    and g["punto_funnel"] == f["punto_funnel"]:
                unir(f["id"], g["id"])

    grupos = defaultdict(list)
    for f in fugas:
        grupos[raiz(f["id"])].append(f)
    filas = []
    for miembros in grupos.values():
        oss = sorted({m["area"] for m in miembros} | {m["ejecutor"] for m in miembros}
                     | {a for m in miembros for a in m["afecta_os"]})
        if len(oss) < 2:
            continue
        miembros.sort(key=lambda m: -m["severidad"])
        lider = miembros[0]
        sev = sum(m["severidad"] for m in miembros)
        impacto = sum(m["impacto_clp_mes"] or 0 for m in miembros) or None
        bloqueos = sorted({m["conector"] for m in miembros if m["acceso"] not in ("ok", "sin-probar")})
        filas.append({
            "id": "OP-" + lider["id"],
            "marca": lider["marca"],
            "titulo": lider["titulo"],
            "punto_funnel": lider["punto_funnel"],
            "etapa": lider["etapa"],
            "os_involucrados": ", ".join(oss),
            "n_os": len(oss),
            "n_fugas": len(miembros),
            "severidad_total": sev,
            "puntaje": lider["severidad"] * 5 + len(oss) * 3 + (sev - lider["severidad"]),
            "impacto_clp_mes": impacto,
            "primer_paso": lider["accion"],
            "ejecutor": lider["ejecutor"],
            "via": lider["via"],
            "listo_para_ejecutar": "sí" if lider["acceso"] in ("ok", "sin-probar") else "no",
            "bloqueado_por": ", ".join(bloqueos) or "—",
            "fugas": " · ".join(m["id"] for m in miembros),
        })
    filas.sort(key=lambda r: (-r["puntaje"], r["marca"]))
    for i, r in enumerate(filas, 1):
        r["rank"] = i
    return filas


def main():
    datos, errores = cargar()
    fugas, accesos, cobertura, kpis = [], {}, [], []
    for d in datos:
        abiertas = [f for f in d["fugas"] if f.get("estado") != "resuelta"]
        cobertura.append({"os_id": d["os_id"], "marca": d["marca"], "area": d["area"], "fuente": d["fuente"],
                          "actualizado": d["actualizado"], "fugas_abiertas": len(abiertas),
                          "artifact_url": d.get("artifact_url") or "—", "archivo": d["_ruta"]})
        for k in d.get("kpis", []):
            kpis.append({"os_id": d["os_id"], "marca": d["marca"], "area": d["area"], **k})
        for f in abiertas:
            acc = f["accion"]
            fugas.append({"id": f["id"], "marca": d["marca"], "area": d["area"], "titulo": f["titulo"],
                          "etapa": f["etapa"], "punto_funnel": f["punto_funnel"], "severidad": f["severidad"],
                          "impacto_clp_mes": f.get("impacto_clp_mes"), "impacto_nota": f.get("impacto_nota") or "",
                          "evidencia": f.get("evidencia", ""), "estado": f["estado"],
                          "depende_de": f.get("depende_de", []), "afecta_os": f.get("afecta_os", []),
                          "accion": acc["descripcion"], "ejecutor": acc["os_ejecutor"], "via": acc["via"],
                          "conector": acc["conector"], "acceso": acc["acceso"], "requiere_ok": acc["requiere_ok"],
                          "fuente": d["fuente"]})
        for a in d.get("accesos", []):
            clave = (d["marca"], a["conector"])
            peor = accesos.get(clave, {}).get("estado")
            if peor is None or ACCESOS.index(a["estado"]) > ACCESOS.index(peor):
                accesos[clave] = {"marca": d["marca"], "conector": a["conector"], "estado": a["estado"], "nota": a.get("nota", "")}

    ops_ = oportunidades(fugas)
    for v in accesos.values():  # cuántas fugas abiertas cuelgan de cada conector
        colgadas = [f for f in fugas if f["marca"] == v["marca"] and f["conector"] == v["conector"]]
        v["fugas_que_usa"] = len(colgadas)
        v["severidad_en_juego"] = sum(f["severidad"] for f in colgadas)
        v["destrabar"] = "sí" if v["estado"] in ("bloqueado", "sin-conector", "sin-plan") and colgadas else "no"
    for f in fugas:  # conectores que las fugas usan y nadie declaró en accesos
        clave = (f["marca"], f["conector"])
        if clave not in accesos:
            accesos[clave] = {"marca": f["marca"], "conector": f["conector"], "estado": f["acceso"], "nota": "no declarado en accesos",
                              "fugas_que_usa": 0, "severidad_en_juego": 0, "destrabar": "no"}
    acc_filas = sorted(accesos.values(), key=lambda v: (v["destrabar"] != "sí", -v["severidad_en_juego"]))

    for f in fugas:  # listas a texto, para tablas
        f["depende_de"] = ", ".join(f["depende_de"]) or "—"
        f["afecta_os"] = ", ".join(f["afecta_os"]) or "—"
        f["requiere_ok"] = "sí" if f["requiere_ok"] else "no"
    fugas.sort(key=lambda f: (-f["severidad"], f["marca"], f["id"]))

    out = AQUI / "consolidado"
    out.mkdir(exist_ok=True)
    for nombre, filas in [("fugas", fugas), ("oportunidades", ops_), ("accesos", acc_filas),
                          ("cobertura", cobertura), ("kpis", kpis)]:
        (out / f"{nombre}.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n")
    print(f"{len(datos)} OS · {len(fugas)} fugas abiertas · {len(ops_)} oportunidades cruzadas · "
          f"{sum(1 for c in cobertura if c['fuente'] != 'os')} OS en semilla")
    for e in errores:
        print("AVISO:", e, file=sys.stderr)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
