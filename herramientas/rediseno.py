#!/usr/bin/env python3
"""Aplica la plantilla común (herramientas/sitio.py) a las páginas en español ya escritas.
Idempotente: se puede ejecutar varias veces.

Uso: python herramientas/rediseno.py
- Sustituye cabecera, pie y aviso de cookies por los de sitio.py.
- Un solo theme-color, precarga de la fuente de titulares, versiones ?v= de sitio.py.
- Listas de periódico (clases list/item) en índices y buscador.
- Índices de sección: cabecera con antetítulo y BreadcrumbList.
- Si existe la versión inglesa (en/), añade hreflang y el selector ES/EN.
- Regenera la portada (index.html) a partir de los índices de sección.
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import sitio
from sitio import BASE, esc

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXCL = {".git", "auditoria", "herramientas", "en"}
NO = {"google178e73f6eb6598d4.html"}
SEC = dict(sitio.SECCIONES["es"])
SEC_LARGO = {"preguntas": "Preguntas", "dinero": "Dinero y vehículos", "problemas": "Problemas técnicos",
             "novedades": "PC y Online", "lugares": "Leonida"}


def mapa():
    try:
        sys.path.insert(0, str(ROOT / "herramientas"))
        from paginas_en import MAPA  # {ruta_es: ruta_en}
        return MAPA
    except ImportError:
        return {}


def url_de(rel):
    r = rel if isinstance(rel, str) else rel.as_posix()
    if r == "index.html":
        return BASE
    if r.endswith("/index.html"):
        return BASE + r[:-10]
    return BASE + r


def items_de_indice(sec):
    s = (ROOT / sec / "index.html").read_text(encoding="utf-8")
    return re.findall(r'<li class="(?:card|item)"><a href="\.\./([^"]+)"><span class="(?:card|item)-t">(.*?)</span><span class="(?:card|item)-d">(.*?)</span></a></li>', s)


def descripcion(rel):
    if rel.endswith("/"):  # páginas en carpeta propia (p. ej. guias/antes-de-jugar/)
        rel += "index.html"
    s = (ROOT / rel).read_text(encoding="utf-8")
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    return m.group(1) if m else ""


def entradillas(s):
    """En los índices, la entradilla de cada pieza es la descripción completa del artículo (sin cortes)."""
    def r(m):
        return f'<li class="item"><a href="../{m.group(1)}"><span class="item-t">{m.group(2)}</span><span class="item-d">{descripcion(m.group(1))}</span></a></li>'
    return re.sub(r'<li class="item"><a href="\.\./([^"]+)"><span class="item-t">(.*?)</span><span class="item-d">.*?</span></a></li>', r, s)


def portada():
    bloques = []
    for sec, corto in sitio.SECCIONES["es"]:
        its = items_de_indice(sec)
        # Jerarquía: la primera pieza de cada sección lleva entradilla; el resto, solo titular.
        lis = "".join((f'<li class="item"><a href="{u}"><span class="item-t">{t}</span><span class="item-d">{descripcion(u)}</span></a></li>' if i == 0 else
                       f'<li class="item item-s"><a href="{u}"><span class="item-t">{t}</span></a></li>')
                      for i, (u, t, d) in enumerate(its[:6]))
        mas = f'Ver las {len(its)} →' if len(its) > 6 else 'Ver sección →'
        bloques.append(f'<section class="sec-block" aria-labelledby="h-{sec}"><div class="sec-head"><h2 id="h-{sec}"><a href="{sec}/">{SEC_LARGO[sec]}</a></h2>'
                       f'<a class="more" href="{sec}/">{mas}</a></div><ul class="list">{lis}</ul></section>')
    tops = [("novedades/gta-6-online.html", "¿GTA 6 tiene modo online? Estado actual"),
            ("problemas/no-carga-errores.html", "GTA 6 no carga o no arranca: qué hacer"),
            ("preguntas/trucos.html", "Trucos de GTA 6: todos los códigos"),
            ("preguntas/secretos-easter-eggs.html", "Secretos y easter eggs encontrados"),
            ("novedades/gta-6-pc.html", "¿Cuándo sale GTA 6 en PC?")]
    tops_html = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in tops)
    return f'''<main id="main">
<div class="wrap">
<section class="hero">
<h1 class="tagline">GTA 6: trucos, guías y respuestas cortas</h1>
<p class="lead">Con fuente enlazada y fecha de revisión. PS5 y Xbox Series · revisado el 20 de noviembre de 2026.</p>
</section>
<div class="lead-story">
<article class="lead-main">
<p class="kicker">Guía de inicio</p>
<h2><a href="guia-inicio.html">12 cosas que conviene saber antes de empezar GTA 6</a></h2>
<p class="dek">Guarda en ranuras distintas, protege tu dinero en el banco, registra los coches que quieras conservar y no cuentes con los trucos hasta terminar la historia.</p>
<p class="small">Resumen de análisis y guías del lanzamiento. Cada punto enlaza a su página con fuentes.</p>
</article>
<aside class="lead-side" aria-labelledby="h-tops"><h2 id="h-tops" class="side-h">Lo más consultado</h2><ul class="tops">{tops_html}</ul></aside>
</div>
<div class="home-search">
<form class="search-form" id="home-search" role="search" action="buscar.html" method="get"><label for="q-home" class="sr">Buscar una pregunta sobre GTA 6</label><input id="q-home" name="q" type="search" placeholder="Busca: trucos, dinero, PC, guardar partida…" required><button type="submit" class="btn btn-primary">Buscar</button></form>
</div>
<div class="grid-secs">{"".join(bloques)}</div>
</div>
</main>'''


def imagen(rel, s, pre):
    """Imagen principal (Rockstar Games): figura, og:image y JSON-LD. Idempotente."""
    clave = sitio.IMG_PAGINAS.get(rel)
    if not clave:
        return s
    s = re.sub(r'<figure class="lead-img[^"]*">.*?</figure>\n?', "", s, flags=re.S)
    s = re.sub(r'<meta property="og:image[^>]*>\n?', "", s)
    s = s.replace('<meta name="twitter:card"', sitio.og_imagen(clave, "es") + '\n<meta name="twitter:card"', 1)
    s = re.sub(r'"image": \[[^\]]*\]', lambda m: f'"image": ["{sitio.img_url(clave)}"]', s)
    partes = rel.split("/")
    if rel == "index.html":
        s = s.replace('<article class="lead-main">\n', '<article class="lead-main">\n' + sitio.figura(clave, "es", pre, "home", True) + "\n", 1)
    elif len(partes) == 2 and partes[1] == "index.html":
        s = re.sub(r'(<div class="index-head">.*?<p class="lead">.*?</p>)(</div>)',
                   lambda m: m.group(1) + sitio.figura(clave, "es", pre, "index", True) + m.group(2), s, count=1, flags=re.S)
    else:
        s = re.sub(r'(<div class="answer">.*?</div>)', lambda m: m.group(1) + sitio.figura(clave, "es", pre, "art"), s, count=1, flags=re.S)
    return s


def procesar(p, MAPA):
    rel = p.relative_to(ROOT).as_posix()
    s = p.read_text(encoding="utf-8")
    o = s
    es404 = p.name == "404.html"
    depth = len(p.relative_to(ROOT).parts) - 1
    pre = "/" if es404 else "../" * depth
    partes = rel.split("/")
    actual = partes[0] if len(partes) > 1 and partes[0] in SEC else {"buscar.html": "buscar", "guia-inicio.html": "guia"}.get(rel)
    en = MAPA.get(rel)
    alt = None
    if en:
        alt = ("/" + en) if es404 else (pre + en)
    s = re.sub(r'<div class="consent" id="consent".*?</div></div></div>', lambda m: sitio.consent("es", pre), s, count=1, flags=re.S)
    s = re.sub(r'<header class="site-header">.*?</header>', lambda m: sitio.header("es", pre, actual, alt), s, count=1, flags=re.S)
    s = re.sub(r'<footer class="site-footer">.*?</footer>', lambda m: sitio.footer("es", pre), s, count=1, flags=re.S)
    s = re.sub(r'<meta name="theme-color"[^>]*>\n?', "", s)
    s = s.replace('<meta name="twitter:card"', f'<meta name="theme-color" content="{sitio.THEME}">\n<meta name="twitter:card"', 1) if 'name="theme-color"' not in s else s
    s = re.sub(r'style\.css\?v=\d+', f"style.css?v={sitio.CSS_V}", s)
    s = re.sub(r'favicon\.svg(\?v=\d+)?"', 'favicon.svg?v=2"', s)
    if 'rel="apple-touch-icon"' not in s:
        pa = "https://6estrellas.org/" if es404 else pre
        s = re.sub(r'(<link rel="icon" [^>]*>)', lambda m: m.group(1) + f'\n<link rel="apple-touch-icon" href="{pa}assets/apple-touch-icon.png">', s, count=1)
    s = re.sub(r'site\.js\?v=\d+', f"site.js?v={sitio.JS_V}", s)
    s = re.sub(r'search\.js\?v=\d+', f"search.js?v={sitio.SEARCH_V}", s)
    if "oswald-latin-wght.woff2" not in s:
        pa = "https://6estrellas.org/" if es404 else pre
        s = re.sub(r'(<link rel="stylesheet" href="[^"]*style\.css[^"]*">)', lambda m: sitio.preload(pa) + "\n" + m.group(1), s, count=1)
    s = s.replace('class="cards"', 'class="list"').replace('class="card"', 'class="item"')
    s = s.replace('class="card-t"', 'class="item-t"').replace('class="card-d"', 'class="item-d"')
    # Guía: los puntos pasan de h3 a h2 (orden de encabezados).
    if rel == "guia-inicio.html":
        s = re.sub(r'<li><h3>(.*?)</h3>', r'<li><h2>\1</h2>', s)
    # hreflang
    s = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n?', "", s)
    if en and not es404:
        s = s.replace('<meta property="og:type"', sitio.hreflang(url_de(rel), BASE + en) + '\n<meta property="og:type"', 1)
    # Índices de sección
    if len(partes) == 2 and partes[1] == "index.html" and partes[0] in SEC:
        sec = partes[0]
        if 'class="index-head"' not in s:
            s = re.sub(r'<h1>(.*?)</h1><p class="lead">(.*?)</p>',
                       lambda m: f'<div class="index-head"><p class="kicker">Sección</p><h1>{m.group(1)}</h1><p class="lead">{m.group(2)}</p></div>', s, count=1)
        if '"BreadcrumbList"' not in s:
            bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": SEC_LARGO[sec], "item": f"{BASE}{sec}/"}]}
            s = s.replace("</head>", f'<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>\n</head>', 1)
    if len(partes) == 2 and partes[1] == "index.html" and partes[0] in SEC:
        s = entradillas(s)
        n = s.count('<li class="item">')
        s = re.sub(r'<p class="kicker">[^<]*</p><h1>', f'<p class="kicker">{n} respuestas</p><h1>', s, count=1)
    # GitHub Pages solo sirve la 404 de la raíz: las URLs inexistentes de /en/ pasan a la 404 inglesa.
    if es404 and MAPA and "location.replace('/en/404.html')" not in s:
        s = s.replace("</head>", "<script>if(location.pathname.indexOf('/en/')===0&&location.pathname!=='/en/404.html')location.replace('/en/404.html');</script>\n</head>", 1)
    if rel == "index.html":
        s = re.sub(r'<main id="main">.*?</main>', lambda m: portada(), s, count=1, flags=re.S)
    s = imagen(rel, s, pre)
    s = re.sub(r'\n?<div class="gallery[^"]*">.*?</div>(?=\n)', "", s, flags=re.S)
    s = sitio.con_galerias(s, rel, "es", pre)
    if s != o:
        p.write_text(s, encoding="utf-8", newline="")
        return True
    return False


def main():
    MAPA = mapa()
    n = 0
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if set(rel.parts) & EXCL or p.name in NO:
            continue
        n += procesar(p, MAPA)
    print(f"rediseño: {n} páginas cambiadas; versión inglesa enlazada: {'sí' if MAPA else 'no'}")


if __name__ == "__main__":
    main()
