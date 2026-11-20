#!/usr/bin/env python3
"""Comprobaciones antes de cada push (sin dependencias).

Uso: python herramientas/comprobar.py

Revisa en todas las páginas publicables:
- <title> y meta description (presentes; longitud orientativa), lang, canonical = URL real.
- JSON-LD válido (json.loads), inLanguage coherente con lang.
- hreflang: cada pareja es/en se enlaza en los dos sentidos, con x-default, y apunta a URLs que existen.
- Enlaces internos (href/src relativos) que apuntan a archivos existentes.
- Sitemap: todas las páginas indexables están y no hay URLs que no existan.
- Anuncios: como mucho un hueco .ad por página y ninguno fuera de los artículos.
- ?v= de style.css y site.js iguales en todas las páginas.
Sale con código 1 si hay errores.
"""
import json, pathlib, re, sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://6estrellas.org/"
EXCL_DIRS = {".git", "auditoria", "herramientas"}
NO_INDEX = {"google178e73f6eb6598d4.html"}

errores, avisos = [], []


def err(m): errores.append(m)
def aviso(m): avisos.append(m)


def paginas():
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if set(rel.parts) & EXCL_DIRS or p.name in NO_INDEX:
            continue
        yield p


def url_de(rel):
    r = rel.as_posix()
    if r == "index.html":
        return BASE
    if r.endswith("/index.html"):
        return BASE + r[: -len("index.html")]
    return BASE + r


def archivo_de(url):
    if not url.startswith(BASE):
        return None
    r = url[len(BASE):]
    if r == "" or r.endswith("/"):
        r += "index.html"
    return ROOT / r


HAY_EN = (ROOT / "en").is_dir()
hreflangs = {}
noindex = set()
versiones = {}
for p in paginas():
    rel = p.relative_to(ROOT)
    s = p.read_text(encoding="utf-8")
    nombre = rel.as_posix()
    url = url_de(rel)
    lang = re.search(r'<html lang="([^"]+)"', s)
    lang = lang.group(1) if lang else None
    if not lang:
        err(f"{nombre}: falta lang en <html>")
    esperado = "en" if nombre.startswith("en/") else "es"
    if lang and lang != esperado:
        err(f"{nombre}: lang={lang}, se esperaba {esperado}")
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    if not t:
        err(f"{nombre}: sin <title>")
    elif len(t.group(1)) > 70:
        aviso(f"{nombre}: title de {len(t.group(1))} caracteres")
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not d:
        err(f"{nombre}: sin meta description")
    elif not 70 <= len(d.group(1)) <= 170:
        aviso(f"{nombre}: description de {len(d.group(1))} caracteres")
    robots = re.search(r'<meta name="robots" content="([^"]*)"', s)
    es_noindex = bool(robots and "noindex" in robots.group(1))
    if es_noindex:
        noindex.add(url)
    c = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    if not es_noindex and p.name != "404.html":
        if not c:
            err(f"{nombre}: sin canonical")
        elif c.group(1) != url:
            err(f"{nombre}: canonical {c.group(1)} != {url}")
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            j = json.loads(m.group(1))
        except Exception as e:
            err(f"{nombre}: JSON-LD inválido ({e})")
            continue
        il = j.get("inLanguage")
        if il and lang and il != lang:
            err(f"{nombre}: JSON-LD inLanguage={il} y lang={lang}")
        if j.get("@type") == "Article" and j.get("mainEntityOfPage") != url:
            err(f"{nombre}: mainEntityOfPage no coincide")
    hl = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', s))
    if hl:
        hreflangs[url] = hl
    elif HAY_EN and p.name != "404.html" and not es_noindex:
        err(f"{nombre}: sin hreflang")
    for m in re.finditer(r'(?:href|src)="([^"#?]+)(?:[?#][^"]*)?"', s):
        h = m.group(1)
        if re.match(r"^(https?:|mailto:|data:|//)", h):
            continue
        dest = (ROOT / h.lstrip("/")).resolve() if h.startswith("/") else (p.parent / h).resolve()
        if h.endswith("/"):
            dest = dest / "index.html"
        if not dest.exists():
            err(f"{nombre}: enlace roto {h}")
    for m in re.finditer(r'href="([^"]+)"[^>]*data-lang', s):
        pass
    # Imágenes: alt, dimensiones, srcset existente, crédito y og:image local.
    credito = "Image: Rockstar Games" if lang == "en" else "Imagen: Rockstar Games"
    for fm in re.finditer(r'<figure class="lead-img[^"]*">(.*?)</figure>', s, re.S):
        f = fm.group(1)
        im = re.search(r"<img ([^>]+)>", f)
        attrs = dict(re.findall(r'(\w[\w-]*)="([^"]*)"', im.group(1))) if im else {}
        if not attrs.get("alt"):
            err(f"{nombre}: imagen sin alt")
        if not (attrs.get("width") and attrs.get("height")):
            err(f"{nombre}: imagen sin width/height")
        for cand in re.findall(r"([^\s,]+) \d+w", attrs.get("srcset", "")):
            if not (p.parent / cand).resolve().exists():
                err(f"{nombre}: srcset roto {cand}")
        if credito not in f:
            err(f"{nombre}: imagen sin crédito «{credito}»")
    og = re.search(r'<meta property="og:image" content="([^"]+)"', s)
    if og and og.group(1).startswith(BASE):
        f = archivo_de(og.group(1))
        if not f or not f.exists():
            err(f"{nombre}: og:image no existe ({og.group(1)})")
    nads = len(re.findall(r'<aside class="ad"', s))
    es_articulo = '"@type": "Article"' in s
    if nads > 1:
        err(f"{nombre}: {nads} huecos de anuncio")
    if nads and not es_articulo:
        err(f"{nombre}: anuncio fuera de un artículo")
    if es_articulo and not nads:
        aviso(f"{nombre}: artículo sin hueco de anuncio")
    for a in ("style.css", "site.js"):
        v = re.search(a.replace(".", r"\.") + r"\?v=(\d+)", s)
        if v:
            versiones.setdefault(a, set()).add(v.group(1))
    # Selector de idioma: debe apuntar a la página equivalente.
    sel = re.search(r'<a class="lang-switch"[^>]*href="([^"]+)"', s)
    if HAY_EN and hl and not sel:
        err(f"{nombre}: sin selector de idioma")

for img in (ROOT / "assets" / "img").glob("*.webp"):
    if img.stat().st_size > 200 * 1024:
        err(f"{img.name}: pesa más de 200 KB")

for a, vs in versiones.items():
    if len(vs) > 1:
        err(f"{a}: versiones ?v= distintas {sorted(vs)}")

# hreflang recíprocos
for url, hl in hreflangs.items():
    if "x-default" not in hl:
        err(f"{url}: sin x-default")
    for code, dest in hl.items():
        f = archivo_de(dest)
        if f is None or not f.exists():
            err(f"{url}: hreflang {code} apunta a {dest}, que no existe")
            continue
        if code in ("es", "en"):
            otro = hreflangs.get(dest)
            if not otro:
                err(f"{url}: {dest} no tiene hreflang de vuelta")
            elif otro.get("es") != hl.get("es") or otro.get("en") != hl.get("en"):
                err(f"{url}: hreflang no recíproco con {dest}")
    if "es" not in hl or "en" not in hl:
        err(f"{url}: falta es o en en hreflang")
    elif url not in (hl["es"], hl["en"]):
        err(f"{url}: la página no se incluye a sí misma en hreflang")

# sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
for l in locs:
    f = archivo_de(l)
    if f is None or not f.exists():
        err(f"sitemap: {l} no existe")
    if l in noindex:
        err(f"sitemap: {l} es noindex")
for p in paginas():
    u = url_de(p.relative_to(ROOT))
    if p.name == "404.html" or u in noindex:
        continue
    if u not in locs:
        err(f"sitemap: falta {u}")
if len(set(locs)) != len(locs):
    err("sitemap: URLs repetidas")

for a in avisos:
    print("AVISO ", a)
for e in errores:
    print("ERROR ", e)
print(f"{len(errores)} errores, {len(avisos)} avisos")
sys.exit(1 if errores else 0)
