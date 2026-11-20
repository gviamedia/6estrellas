"""Piezas comunes de la plantilla de 6 Estrellas / Six Stars (cabecera, menú, pie, aviso de cookies).

Lo usan herramientas/rediseno.py (páginas en español ya escritas) y herramientas/generar_en.py
(versión en inglés). Si cambias algo aquí, vuelve a ejecutar los dos.
"""
import html

BASE = "https://6estrellas.org/"
CSS_V = 11
JS_V = 9
SEARCH_V = 3
THEME = "#f6f3ed"

SECCIONES = {
    "es": [("preguntas", "Preguntas"), ("dinero", "Dinero"), ("problemas", "Problemas"),
           ("novedades", "PC y Online"), ("lugares", "Leonida")],
    "en": [("questions", "Questions"), ("money", "Money"), ("issues", "Fixes"),
           ("pc-online", "PC & Online"), ("leonida", "Leonida")],
}
NOMBRE = {"es": "6 Estrellas", "en": "Six Stars"}
T = {
    "es": dict(skip="Saltar al contenido", secciones="Secciones", idioma="Idioma", buscar="Buscar",
               buscar_url="buscar.html", guia="Guía gratis", guia_url="guia-inicio.html",
               sobre=("sobre.html", "Quiénes somos y cómo trabajamos"), aviso=("aviso-legal.html", "Aviso legal"),
               priv=("privacidad.html", "Política de privacidad"), cookies=("cookies.html", "Política de cookies"),
               conf="Configurar cookies",
               disclaimer="<strong>Web no oficial.</strong> 6 Estrellas es una web independiente de aficionados. No está afiliada, patrocinada ni respaldada por Rockstar Games ni Take-Two Interactive. Grand Theft Auto, GTA y los nombres relacionados son marcas de sus respectivos propietarios y se citan solo para identificar el juego.",
               revision="Última revisión general: 20 de noviembre de 2026.",
               c_text='<strong>Cookies.</strong> Solo si aceptas, cargamos anuncios de Adsterra, que usa cookies. <a href="{p}cookies.html">Más información</a>.',
               c_aria="Aviso de cookies", c_tec="Técnicas: recordar tu elección. Siempre activas.",
               c_ads="Publicidad: anuncios de Adsterra y su medición.",
               c_btn=("Rechazar", "Configurar", "Aceptar", "Guardar")),
    "en": dict(skip="Skip to content", secciones="Sections", idioma="Language", buscar="Search",
               buscar_url="search.html", guia="Beginner's guide", guia_url="beginners-guide.html",
               sobre=("about.html", "About us and how we work"), aviso=("legal-notice.html", "Legal notice"),
               priv=("privacy.html", "Privacy policy"), cookies=("cookies.html", "Cookie policy"),
               conf="Cookie settings",
               disclaimer="<strong>Unofficial site.</strong> Six Stars is an independent fan site. It is not affiliated with, sponsored or endorsed by Rockstar Games or Take-Two Interactive. Grand Theft Auto, GTA and related names are trademarks of their respective owners and are used only to identify the game.",
               revision="Last site-wide review: November 20, 2026.",
               c_text='<strong>Cookies.</strong> We only load Adsterra ads, which use cookies, if you accept. <a href="{p}cookies.html">Learn more</a>.',
               c_aria="Cookie notice", c_tec="Essential: remember your choice. Always on.",
               c_ads="Advertising: Adsterra ads and ad measurement.",
               c_btn=("Reject", "Settings", "Accept", "Save")),
}


def esc(s):
    return html.escape(s, quote=True)


def consent(lang, p):
    t = T[lang]
    r, c, a, g = t["c_btn"]
    return (f'<div class="consent" id="consent" role="region" aria-label="{t["c_aria"]}" hidden>\n'
            f'<div class="consent-in">\n<p class="small">{t["c_text"].format(p=p)}</p>\n'
            f'<div class="consent-opts" id="consent-opts" hidden>\n'
            f'<label><input type="checkbox" checked disabled> <span>{t["c_tec"]}</span></label>\n'
            f'<label><input type="checkbox" id="c-ads"> <span>{t["c_ads"]}</span></label>\n</div>\n'
            f'<div class="consent-btns">\n<button type="button" class="btn" data-consent="reject">{r}</button>\n'
            f'<button type="button" class="btn" data-consent="config">{c}</button>\n'
            f'<button type="button" class="btn" data-consent="accept">{a}</button>\n'
            f'<button type="button" class="btn" data-consent="save" hidden>{g}</button>\n</div></div></div>')


def header(lang, p, actual=None, alt=None):
    """p: prefijo relativo hasta la raíz del idioma ('' , '../' o '/' o '/en/').
    actual: clave de la sección activa ('preguntas', 'buscar', 'guia'...).
    alt: URL relativa a la página equivalente en el otro idioma (None si no existe)."""
    t = T[lang]
    items = []
    for clave, nombre in SECCIONES[lang]:
        cur = ' aria-current="page"' if clave == actual else ""
        items.append(f'<li><a href="{p}{clave}/"{cur}>{nombre}</a></li>')
    cur = ' aria-current="page"' if actual == "buscar" else ""
    items.append(f'<li><a href="{p}{t["buscar_url"]}"{cur}>{t["buscar"]}</a></li>')
    cur = ' aria-current="page"' if actual == "guia" else ""
    items.append(f'<li><a href="{p}{t["guia_url"]}"{cur}>{t["guia"]}</a></li>')
    home = p if p else "./"
    lang_nav = ""
    if alt:
        otro = "en" if lang == "es" else "es"
        etiqueta = {"es": "Español", "en": "English"}
        actual_html = f'<span aria-current="true" title="{etiqueta[lang]}">{lang.upper()}</span>'
        otro_html = f'<a class="lang-switch" href="{alt}" hreflang="{otro}" lang="{otro}" title="{etiqueta[otro]}">{otro.upper()}</a>'
        # Siempre en el mismo orden: ES EN.
        pares = actual_html + otro_html if lang == "es" else otro_html + actual_html
        lang_nav = f'<nav class="lang" aria-label="{t["idioma"]}">{pares}</nav>'
    return (f'<header class="site-header"><div class="wrap">\n'
            f'<div class="masthead"><a class="brand" href="{home}">{NOMBRE[lang]}</a>{lang_nav}</div>\n'
            f'<nav class="sections" aria-label="{t["secciones"]}"><ul>\n' + "".join(items) + '\n</ul></nav>\n'
            f'</div></header>')


def footer(lang, p):
    t = T[lang]
    links = "".join(f'<li><a href="{p}{u}">{n}</a></li>\n' for u, n in (t["sobre"], t["aviso"], t["priv"], t["cookies"]))
    home = p if p else "./"
    return (f'<footer class="site-footer"><div class="wrap">\n'
            f'<a class="brand" href="{home}">{NOMBRE[lang]}</a>\n'
            f'<p class="disclaimer">{t["disclaimer"]}</p>\n'
            f'<ul class="foot-links">\n{links}<li><button type="button" class="linklike" data-open-consent>{t["conf"]}</button></li>\n</ul>\n'
            f'<p class="small">{t["revision"]}</p>\n</div></footer>')


def hreflang(es_url, en_url):
    return (f'<link rel="alternate" hreflang="es" href="{es_url}">\n'
            f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{es_url}">')


def preload(p_assets):
    return f'<link rel="preload" href="{p_assets}assets/fonts/oswald-latin-wght.woff2" as="font" type="font/woff2" crossorigin>'


# ---------------------------------------------------------------- imágenes (Rockstar Games)
from imagenes_datos import IMAGENES, PAGINAS as IMG_PAGINAS, SIN_RECORTE, GALERIAS

CREDITO = {"es": "Imagen: Rockstar Games", "en": "Image: Rockstar Games"}
SIZES = {"art": "(min-width: 700px) 640px, 100vw", "home": "(min-width: 900px) 660px, 100vw",
         "index": "(min-width: 1120px) 1088px, 100vw"}


def img_url(clave, w=1600):
    return f"{BASE}assets/img/{clave}-{w}.webp"


def alt(clave, lang):
    return IMAGENES[clave][2 if lang == "es" else 3]


def dims(clave, w=1600):
    if clave in SIN_RECORTE:
        ow, oh = SIN_RECORTE[clave]
        return w, round(w * oh / ow)
    return w, w * 9 // 16


AMPLIAR = {"es": "Ver el mapa a tamaño grande", "en": "View the map full size"}


def figura(clave, lang, a, tipo="art", prioridad=False):
    """a: prefijo relativo hasta la raíz del sitio. Es la primera (y única) imagen de cada página:
    sin loading="lazy"; fetchpriority="high" solo donde la imagen está arriba del todo (portada, índices)."""
    fp = ' fetchpriority="high"' if prioridad else ""
    clase = {"art": "lead-img", "home": "lead-img home-img", "index": "lead-img index-img"}[tipo]
    w, h = dims(clave)
    img = (f'<img src="{a}assets/img/{clave}-800.webp" '
           f'srcset="{a}assets/img/{clave}-800.webp 800w, {a}assets/img/{clave}-1600.webp 1600w" '
           f'sizes="{SIZES[tipo]}" width="{w}" height="{h}" alt="{esc(alt(clave, lang))}" decoding="async"{fp}>')
    cap = CREDITO[lang]
    if clave in SIN_RECORTE:  # mapa: proporción original y enlace a la versión grande
        clase += " map-img"
        img = f'<a href="{a}assets/img/{clave}-1600.webp">{img}</a>'
        cap += f' · <a href="{a}assets/img/{clave}-1600.webp">{AMPLIAR[lang]}</a>'
    return f'<figure class="{clase}">{img}<figcaption>{cap}</figcaption></figure>'


def og_imagen(clave, lang):
    return (f'<meta property="og:image" content="{img_url(clave)}">\n'
            f'<meta property="og:image:type" content="image/webp">\n'
            f'<meta property="og:image:width" content="{dims(clave)[0]}">\n'
            f'<meta property="og:image:height" content="{dims(clave)[1]}">\n'
            f'<meta property="og:image:alt" content="{esc(alt(clave, lang))}">')


def galeria(items, lang, a):
    """Imágenes dentro del texto (no son la primera de la página): loading="lazy" y pie descriptivo + crédito.
    Una sola imagen va a lo ancho; dos o más, en rejilla."""
    figs = []
    sizes = "(min-width: 700px) 640px, 100vw" if len(items) == 1 else "(min-width: 700px) 316px, 50vw"
    for clave, pie_es, pie_en in items:
        w, h = dims(clave)
        pie = pie_es if lang == "es" else pie_en
        figs.append(f'<figure class="body-img"><img src="{a}assets/img/{clave}-800.webp" '
                    f'srcset="{a}assets/img/{clave}-800.webp 800w, {a}assets/img/{clave}-1600.webp 1600w" '
                    f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt(clave, lang))}" loading="lazy" decoding="async">'
                    f'<figcaption><span class="pie">{esc(pie)}</span> {CREDITO[lang]}</figcaption></figure>')
    clase = "gallery" if len(items) > 1 else "gallery gallery-1"
    return f'<div class="{clase}">' + "".join(figs) + '</div>'


def con_galerias(html, es_rel, lang, a):
    """Inserta las galerías de GALERIAS[es_rel] en html. Idempotente (quita las anteriores)."""
    import re
    html = re.sub(r'<div class="gallery[^"]*">.*?</div>(?=\n|<)', "", html, flags=re.S)
    for pos, ancla_es, ancla_en, items in GALERIAS.get(es_rel, []):
        ancla = ancla_es if lang == "es" else ancla_en
        if ancla not in html:
            raise SystemExit(f"{es_rel} ({lang}): no encuentro el ancla {ancla!r}")
        g = galeria(items, lang, a)
        html = html.replace(ancla, (g + "\n" + ancla) if pos == "antes" else (ancla + "\n" + g), 1)
    return html
