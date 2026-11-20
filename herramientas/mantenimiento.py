#!/usr/bin/env python3
"""Mantenimiento de 6 Estrellas (sin dependencias).

Uso, desde la raíz del repositorio:
  python herramientas/mantenimiento.py indice   -> regenera assets/search-index.json
  python herramientas/mantenimiento.py fechas   -> sincroniza dateModified (JSON-LD) y lastmod (sitemap.xml)
                                                  con la fecha real del último cambio de cada página en git
  python herramientas/mantenimiento.py todo

Notas:
- "fechas" ignora los commits cuyo mensaje empieza por "Fechas:" (para no entrar en bucle) o por
  "Diseño:" (cambios de plantilla que no tocan el contenido).
  Haz primero el commit del contenido y después ejecuta "fechas" y commitea con "Fechas: ...".
- datePublished no se toca nunca.
"""
import html, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECCIONES = {"preguntas": "Preguntas", "dinero": "Dinero y vehículos", "problemas": "Problemas técnicos",
             "novedades": "PC y Online", "lugares": "Leonida"}
SECCIONES_EN = {"questions": "Questions", "money": "Money & Cars", "issues": "Fixes",
                "pc-online": "PC & Online", "leonida": "Leonida"}
NO_PAGINAS = {"404.html", "google178e73f6eb6598d4.html", "buscar.html", "search.html"}


def paginas():
    return [p for p in ROOT.rglob("*.html")
            if not set(p.relative_to(ROOT).parts) & {".git", "auditoria", "herramientas"} and p.name not in NO_PAGINAS]


def texto(fragmento):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragmento))).strip()


def indice():
    _indice("es")
    _indice("en")


def _indice(lang):
    """Índice del buscador por idioma. En inglés, las URLs son relativas a /en/."""
    secs, guia, nombre = ((SECCIONES, "guia-inicio.html", "Guía") if lang == "es" else
                          (SECCIONES_EN, "beginners-guide.html", "Guide"))
    items = []
    for p in sorted(paginas()):
        rel = p.relative_to(ROOT).as_posix()
        if lang == "en":
            if not rel.startswith("en/"):
                continue
            rel = rel[3:]
        elif rel.startswith("en/"):
            continue
        seccion = rel.split("/")[0]
        if seccion not in secs and rel != guia:
            continue
        if p.name == "index.html":
            continue
        s = p.read_text(encoding="utf-8")
        h1 = re.search(r"<h1>(.*?)</h1>", s, re.S)
        resp = re.search(r'<div class="answer">.*?<p class="answer-label">.*?</p>\s*<p>(.*?)</p>', s, re.S)
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        cuerpo = re.search(r'<div class="prose">(.*?)</div>\s*<section class="sources">', s, re.S)
        items.append({
            "u": rel,
            "t": texto(h1.group(1)) if h1 else rel,
            "s": secs.get(seccion, nombre),
            "r": texto(resp.group(1)) if resp else (texto(desc.group(1)) if desc else ""),
            "d": texto(desc.group(1)) if desc else "",
            "c": texto(cuerpo.group(1))[:1500] if cuerpo else "",
        })
    out = ROOT / "assets" / ("search-index.json" if lang == "es" else "search-index-en.json")
    out.write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8", newline="")
    print(f"índice {lang}: {len(items)} páginas, {out.stat().st_size} bytes")


def ultimo_cambio(rel):
    r = subprocess.run(["git", "log", "-1", "--format=%aI", "--invert-grep", "--grep=^Fechas:", "--grep=^Diseño:", "--", rel],
                       cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return r.stdout.strip()


def fechas():
    sm = ROOT / "sitemap.xml"
    xml = sm.read_text(encoding="utf-8")

    def lastmod(m):
        loc = m.group(1)
        ruta = loc.replace("https://6estrellas.org/", "")
        rel = (ruta + "index.html") if (ruta == "" or ruta.endswith("/")) else ruta
        f = ultimo_cambio(rel)
        return f"<url><loc>{loc}</loc><lastmod>{f}</lastmod></url>" if f else m.group(0)

    nuevo = re.sub(r"<url><loc>([^<]+)</loc><lastmod>[^<]*</lastmod></url>", lastmod, xml)
    if nuevo != xml:
        sm.write_text(nuevo, encoding="utf-8", newline="")
    cambiadas = 0
    for p in paginas():
        s = p.read_text(encoding="utf-8")
        if '"@type": "Article"' not in s:
            continue
        f = ultimo_cambio(p.relative_to(ROOT).as_posix())
        if not f:
            continue
        n = re.sub(r'("dateModified": ")[^"]*(")', r"\g<1>" + f + r"\g<2>", s, count=1)
        if n != s:
            p.write_text(n, encoding="utf-8", newline="")
            cambiadas += 1
    print(f"fechas: sitemap actualizado, {cambiadas} artículos con dateModified nuevo")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if cmd in ("indice", "todo"):
        indice()
    if cmd in ("fechas", "todo"):
        fechas()
