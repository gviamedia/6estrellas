#!/usr/bin/env python3
"""Genera la versión en inglés (Six Stars) en /en/ a partir de herramientas/paginas_en.py.

Uso: python herramientas/generar_en.py
Después: python herramientas/rediseno.py (añade hreflang y selector en las páginas en español)
         python herramientas/mantenimiento.py todo
Regenera todas las páginas de /en/ y las URLs inglesas del sitemap. datePublished se conserva
si la página ya existía.
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import sitio
from sitio import BASE, esc
from paginas_en import ARTICULOS, SECCIONES_EN, MAPA

ROOT = pathlib.Path(__file__).resolve().parent.parent
EN = ROOT / "en"
PUB = "2026-11-20T03:00:00+01:00"
REVIEW = ("2026-11-20", "Reviewed November 20, 2026")
AD = dict(key="158c978735c70c7880dc5557f51a12d1", src="https://bauval.org/22/158c978735c70c7880dc5557f51a12d1")
LOGO = {"@type": "ImageObject", "url": BASE + "assets/logo-512.png", "width": 512, "height": 512}
PUBLISHER = {"@type": "Organization", "name": "Six Stars", "url": BASE + "en/", "logo": LOGO}
AUTHOR = {"@type": "Organization", "name": "Six Stars Editorial Team", "url": BASE + "en/about.html"}
POR_EN = {a["en"]: a for a in ARTICULOS}


def url(en_rel):
    """en_rel relativo a /en/ ('' para la portada, 'questions/' para un índice)."""
    return BASE + "en/" + en_rel


def es_de(en_rel):
    inv = {v: k for k, v in MAPA.items()}
    return inv.get("en/" + en_rel)


def es_url(es_rel):
    if es_rel == "index.html":
        return BASE
    if es_rel.endswith("/index.html"):
        return BASE + es_rel[:-10]
    return BASE + es_rel


def depth(en_rel):
    return en_rel.count("/") if not en_rel.endswith("/") else en_rel.count("/")


def prefijos(en_rel):
    d = en_rel.count("/")
    return "../" * d, "../" * (d + 1)  # (raíz del idioma, raíz del sitio)


def pub_anterior(path):
    if path.exists():
        m = re.search(r'"datePublished": "([^"]+)"', path.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return PUB


def clave_img(en_rel):
    return sitio.IMG_PAGINAS.get(es_de(en_rel) or "")


def fig(en_rel, tipo="art", prioridad=False):
    c = clave_img(en_rel)
    return sitio.figura(c, "en", prefijos(en_rel)[1], tipo, prioridad) if c else ""


def head(en_rel, title, desc, otype="article", robots="index, follow, max-image-preview:large", ld=(), alt=True):
    p, a = prefijos(en_rel)
    es_rel = es_de(en_rel)
    hl = sitio.hreflang(es_url(es_rel), url(en_rel)) + "\n" if (alt and es_rel) else ""
    canon = f'<link rel="canonical" href="{url(en_rel)}">\n' if "noindex" not in robots else ""
    c = clave_img(en_rel)
    og_img = sitio.og_imagen(c, "en") if c else f'<meta property="og:image" content="{BASE}assets/og.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="675">'
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
{canon}{hl}<meta property="og:type" content="{otype}">
<meta property="og:site_name" content="Six Stars">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url(en_rel)}">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="es_ES">
{og_img}
<meta name="theme-color" content="{sitio.THEME}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{a}assets/favicon.svg" type="image/svg+xml">
{sitio.preload(a)}
<link rel="stylesheet" href="{a}assets/style.css?v={sitio.CSS_V}">
{lds}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def chrome(en_rel, actual):
    p, a = prefijos(en_rel)
    es_rel = es_de(en_rel)
    alt = None
    if es_rel:
        alt = a + ("" if es_rel == "index.html" else (es_rel[:-10] if es_rel.endswith("/index.html") else es_rel))
        if alt == "":
            alt = "../"
    return sitio.consent("en", p) + "\n" + sitio.header("en", p, actual, alt) + "\n"


def tail(en_rel, extra_js=""):
    p, a = prefijos(en_rel)
    return f'{sitio.footer("en", p)}\n<script src="{a}assets/site.js?v={sitio.JS_V}" defer></script>\n{extra_js}</body></html>\n'


def crumbs(en_rel, sec, current):
    p, _ = prefijos(en_rel)
    parts = [f'<a href="{p}">Home</a>']
    if sec:
        parts.append(f'<a href="{p}{sec}/">{SECCIONES_EN[sec]["name"]}</a>')
    parts.append(f'<span aria-current="page">{current}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ' <span aria-hidden="true">›</span> '.join(parts) + '</nav>'


def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def articulo(a):
    en_rel = a["en"]
    sec = en_rel.split("/")[0]
    p, s = prefijos(en_rel)
    path = EN / en_rel
    pub = pub_anterior(path)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"],
           "image": [sitio.img_url(clave_img(en_rel))], "datePublished": pub, "dateModified": pub, "inLanguage": "en",
           "author": AUTHOR, "publisher": PUBLISHER, "mainEntityOfPage": url(en_rel)}
    if path.exists():
        m = re.search(r'"dateModified": "([^"]+)"', path.read_text(encoding="utf-8"))
        if m:
            art["dateModified"] = m.group(1)
    bc = breadcrumb_ld([("Home", url("")), (SECCIONES_EN[sec]["name"], url(sec + "/")), (a["h1"], url(en_rel))])
    cls, label = a["chip"]
    src = "".join(f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(t)}</a></li>' for u, t in a["sources"])
    rel = "".join(f'<li><a href="{p}{r}">{esc(POR_EN[r]["h1"])}</a></li>' for r in a["related"])
    html = head(en_rel, a["title"], a["desc"], ld=[art, bc]) + chrome(en_rel, sec) + f'''
<main id="main" class="wrap narrow">
{crumbs(en_rel, sec, esc(a["h1"]))}
<article>
<h1>{esc(a["h1"])}</h1>
<p class="meta"><time datetime="{REVIEW[0]}">{REVIEW[1]}</time><span>By <a href="{p}about.html">Six Stars Editorial Team</a></span><span class="chip {cls}">{label}</span></p>
<div class="answer"><p class="answer-label">Short answer</p><p>{esc(a["answer"])}</p></div>{fig(en_rel)}
<div class="prose">
{sitio.con_galerias(a["body"], a["es"], "en", s)}
</div>
<section class="sources"><h2>Sources</h2><ul>{src}</ul>
<p class="small">Written by Six Stars from the sources above, checked on November 20, 2026. Spot a mistake? Tell us via <a href="{p}about.html">About us</a>.</p></section>
</article>

<section class="related" aria-labelledby="rel-t"><h2 id="rel-t">Related questions</h2><ul>{rel}</ul></section>
<aside class="ad" aria-label="Advertisement" data-ad="{AD["key"]}" data-src="{AD["src"]}" data-w="300" data-h="250" data-house="{p}beginners-guide.html"><span class="ad-label" aria-hidden="true">Advertisement</span><div class="ad-box" style="--ad-w:300px;--ad-h:250px"></div></aside>
</main>
''' + tail(en_rel)
    return path, html


def indice(sec):
    d = SECCIONES_EN[sec]
    en_rel = sec + "/"
    arts = [a for a in ARTICULOS if a["en"].startswith(sec + "/")]
    lis = "".join(f'<li class="item"><a href="../{a["en"]}"><span class="item-t">{esc(a["h1"])}</span><span class="item-d">{esc(a["desc"])}</span></a></li>' for a in arts)
    bc = breadcrumb_ld([("Home", url("")), (d["name"], url(en_rel))])
    html = head(en_rel, d["title"], d["desc"], otype="website", ld=[bc]) + chrome(en_rel, sec) + f'''
<main id="main" class="wrap">
{crumbs(en_rel, None, d["name"])}
<div class="index-head"><p class="kicker">{len(arts)} answers</p><h1>{esc(d["h1"])}</h1><p class="lead">{esc(d["lead"])}</p>{fig(en_rel, "index", True)}</div>
<ul class="list">{lis}</ul>
</main>
''' + tail(en_rel)
    return EN / sec / "index.html", html


TOPS = [("pc-online/gta-6-online.html", "Does GTA 6 have online? Current status"),
        ("issues/not-loading-fixes.html", "GTA 6 won't load: what to try"),
        ("questions/cheats.html", "GTA 6 cheats: every known code"),
        ("questions/secrets-easter-eggs.html", "Secrets and Easter eggs found so far"),
        ("pc-online/gta-6-pc.html", "When is GTA 6 coming to PC?")]


def portada():
    en_rel = ""
    bloques = []
    for sec, d in SECCIONES_EN.items():
        arts = [a for a in ARTICULOS if a["en"].startswith(sec + "/")]
        lis = "".join((f'<li class="item"><a href="{a["en"]}"><span class="item-t">{esc(a["h1"])}</span><span class="item-d">{esc(a["desc"])}</span></a></li>' if i == 0 else
                       f'<li class="item item-s"><a href="{a["en"]}"><span class="item-t">{esc(a["h1"])}</span></a></li>') for i, a in enumerate(arts[:6]))
        mas = f"See all {len(arts)} →" if len(arts) > 6 else "See section →"
        bloques.append(f'<section class="sec-block" aria-labelledby="h-{sec}"><div class="sec-head"><h2 id="h-{sec}"><a href="{sec}/">{d["name"]}</a></h2><a class="more" href="{sec}/">{mas}</a></div><ul class="list">{lis}</ul></section>')
    tops = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in TOPS)
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Six Stars", "url": url(""), "inLanguage": "en", "publisher": PUBLISHER}
    html = head(en_rel, "GTA 6 Cheats, Guides and Answers | Six Stars",
                "Quick, sourced answers to the GTA 6 questions players are asking: missions, saving, cheats, money, PC, online, fixes and the map of Leonida.",
                otype="website", ld=[site]) + chrome(en_rel, None) + f'''
<main id="main">
<div class="wrap">
<section class="hero">
<h1 class="tagline">GTA 6 cheats, guides and quick answers</h1>
<p class="lead">Every answer links its sources and shows when we last checked it. PS5 and Xbox Series · reviewed November 20, 2026.</p>
</section>
<div class="lead-story">
<article class="lead-main">
{fig(en_rel, "home", True)}
<p class="kicker">Beginner's guide</p>
<h2><a href="beginners-guide.html">12 things to know before you start GTA 6</a></h2>
<p class="dek">Save to separate slots, bank your cash, register the cars you want to keep and don't count on cheats until you've beaten the story.</p>
<p class="small">Compiled from launch-week reviews and guides. Every point links to a page with sources.</p>
</article>
<aside class="lead-side" aria-labelledby="h-tops"><h2 id="h-tops" class="side-h">Most read</h2><ul class="tops">{tops}</ul></aside>
</div>
<div class="home-search">
<form class="search-form" id="home-search" role="search" action="search.html" method="get"><label for="q-home" class="sr">Search GTA 6 questions</label><input id="q-home" name="q" type="search" placeholder="Search: cheats, money, PC, saving…" required><button type="submit" class="btn btn-primary">Search</button></form>
</div>
<div class="grid-secs">{"".join(bloques)}</div>
</div>
</main>
''' + tail(en_rel)
    return EN / "index.html", html


GUIA = [
    ("You can't replay missions", "Save to a new slot before every mission with a choice. GamesRadar reports 15 manual slots, with autosave kept separate.", "questions/replay-missions.html"),
    ("Switching between Jason and Lucia unlocks around Chapters 2 and 3", "Until then, the game decides who you play. After that, you can switch freely unless the other character is busy.", "questions/switch-characters.html"),
    ("Cheats unlock after the story", "Most also need a challenge, and using them turns off trophies and saving.", "questions/cheats.html"),
    ("You lose your cash when you die", "Move money into your BuckMe account. Don't put anything you'll need into Family Savings: it can't come back out.", "money/buckme-bank.html"),
    ("Register the cars you want to keep", "Stolen cars are registered at Pay 'n' Spray. You start with room for three.", "money/keep-cars-garages.html"),
    ("First money: other criminals, fences, Bret and the derby", "Robbing crooks mid-crime, selling stolen cars, hunting and the Ambrosia demolition derby pay best early on.", "money/make-money.html"),
    ("The cops remember your clothes", "Changing your outfit and getaway car helps you shake them. Non-lethal shots keep your criminal profile cleaner.", "questions/lose-wanted-level.html"),
    ("There's more than one ending", "Your choices matter, including Jason and Lucia's relationship.", "questions/endings-choices.html"),
    ("English voices, subtitles in other languages", "Voice acting is English only. Turn up subtitle size if you drive a lot.", "questions/languages.html"),
    ("30fps on every console", "No 40 or 60fps mode. PS5 Pro wins on sharpness and stability, not frame rate.", "issues/ps5-pro-vs-ps5-vs-xbox.html"),
    ("No online or PC version yet", "Neither has a date. Any “PC download” is a scam.", "pc-online/gta-6-pc.html"),
    ("Won't start? Check the network first", "Check PSN or Xbox status, update your console and make sure you have up to 212 GB free.", "issues/not-loading-fixes.html"),
]


def guia():
    en_rel = "beginners-guide.html"
    lis = "".join(f'<li><h2>{esc(t)}</h2><p>{esc(d)}</p><p class="small"><a href="{u}">More details</a></p></li>' for t, d, u in GUIA)
    html = head(en_rel, "GTA 6 Beginner's Guide: 12 Things to Know | Six Stars",
                "A free GTA 6 beginner's guide: 12 things to know before you start, from saving and money to cars, cheats, police and endings.",
                otype="article") + chrome(en_rel, "guia") + f'''
<main id="main" class="wrap narrow">
<h1>GTA 6 beginner's guide: 12 things to know before you start</h1>
<p class="meta"><time datetime="{REVIEW[0]}">Version of November 20, 2026</time><span class="chip ok">Free</span></p>
<div class="answer"><p class="answer-label">In short</p><p>Save to separate slots often, keep your money in the bank, register the cars you want to keep and don't count on cheats until you've beaten the story.</p></div>{fig(en_rel)}

<ol class="guide">{lis}</ol>
<p class="small">Compiled from reviews and guides published at launch. Every point links to a page with its sources. We'll keep adding to it.</p>
</main>
''' + tail(en_rel)
    return EN / en_rel, html


def pagina(en_rel, title, desc, h1, cuerpo, robots="index, follow, max-image-preview:large", actual=None, extra_js="", otype="website"):
    html = head(en_rel, title, desc, otype=otype, robots=robots) + chrome(en_rel, actual) + f'''<main id="main" class="wrap narrow prose"><h1>{h1}</h1>
{cuerpo}
</main>
''' + tail(en_rel, extra_js)
    return EN / en_rel, html


ABOUT = '''<p>Six Stars is an independent, English-language companion to 6 Estrellas, a Spanish site that answers the specific questions players run into in GTA 6, in a few lines. <strong>Six Stars Editorial Team</strong> is the byline we publish everything under: we don't sign articles with personal names.</p>
<h2>Who writes this</h2>
<p>Every article is published under the “Six Stars Editorial Team” byline. We have no connection to Rockstar Games or Take-Two Interactive.</p>
<p><strong>We don't run our own tests in the game.</strong> Everything we publish is based on cited sources: Rockstar's announcements and support pages, the PlayStation and Xbox stores, and established outlets. We never present anything as checked by us in-game.</p>
<h2>How we verify information</h2>
<ul>
<li><strong>Answer first.</strong> Every page opens with the short answer, with the details below.</li>
<li><strong>Sources in plain sight.</strong> Every page links its sources and shows when it was last reviewed. We prefer official sources; when only the press has reported something, we say so.</li>
<li><strong>In our own words.</strong> We don't copy other sites: we summarize and link the source.</li>
<li><strong>Doubts flagged.</strong> We separate what's confirmed from what isn't, and when two sources disagree, we say so.</li>
</ul>
<h2>What the labels mean</h2>
<p>Each article carries a label next to its date:</p>
<ul>
<li><strong>Per cited sources:</strong> the linked sources agree with what we say.</li>
<li><strong>Partly confirmed:</strong> part of the answer isn't confirmed yet; the page says which.</li>
<li><strong>Single source:</strong> the claim rests on one source and we haven't found a second.</li>
<li><strong>Figure may change:</strong> the number changes over time (review scores, download sizes). Check the date.</li>
<li><strong>Rough estimate:</strong> an approximate figure from the sources, not official data.</li>
</ul>
<h2>Corrections</h2>
<p>If something is wrong or a question is missing, email <a href="mailto:contacto@6estrellas.org">contacto@6estrellas.org</a>. When we fix something, we update the page's review date.</p>
<h2>How the site is funded</h2>
<p>The site shows Adsterra ads only if you accept advertising cookies. We don't charge for content and we aren't paid by Rockstar or by the stores we cite.</p>
<h2>Contact</h2>
<p>Email: <a href="mailto:contacto@6estrellas.org">contacto@6estrellas.org</a>.</p>
<h2>Images</h2>
<p>Game images are official screenshots and artwork published by Rockstar Games on the official GTA VI site, shown with the credit \u201cImage: Rockstar Games.\u201d We don't use images from other sites, watermarked images or leaks, and we don't use the GTA VI logo as this site's brand.</p>
<h2>Unofficial site</h2>
<p>This site is not affiliated with, sponsored or endorsed by Rockstar Games or Take-Two Interactive. Grand Theft Auto and GTA are trademarks of their owners and are mentioned only to identify the game.</p>'''

LEGAL = '''<p class="note">Draft prepared to comply with Spanish Law 34/2002 on information society services (LSSI). The highlighted fields must be filled in with the owner's real details. This is not legal advice.</p>
<h2>1. Site owner</h2>
<p>Under Article 10 of Spanish Law 34/2002:</p>
<ul>
<li>Owner: <mark class="fill">[Full name or company name]</mark></li>
<li>Tax ID (NIF/CIF): <mark class="fill">[NIF or CIF]</mark></li>
<li>Address: <mark class="fill">[Full postal address]</mark></li>
<li>Contact email: <mark class="fill">[contact email]</mark></li>
<li>Registry details (companies only): <mark class="fill">[Commercial Registry details]</mark></li>
</ul>
<h2>2. Purpose</h2>
<p>Six Stars (6 Estrellas in Spanish) is an informational site about the video game Grand Theft Auto VI. It is an <strong>unofficial</strong>, independent site with no connection to Rockstar Games or Take-Two Interactive.</p>
<h2>3. Intellectual property</h2>
<p>The text, the beginner's guide and the design of this site are the work of <mark class="fill">[Owner]</mark>. Reproduction in whole or in part without permission is prohibited, except for quotation with a link to the source.</p>
<p>Game trademarks, names and elements belong to their owners and are mentioned for informational purposes only. Game screenshots and artwork are official material published by Rockstar Games, shown with credit, and belong to their owners. If you hold rights and believe they are being infringed, write to the contact email and we'll review it.</p>
<h2>4. Liability</h2>
<p>The information is based on public sources cited on each page and may change with game updates. We review the content but can't guarantee it is error-free. External links lead to third-party sites we are not responsible for.</p>
<h2>5. Advertising and affiliate links</h2>
<p>This site may show advertising and affiliate links. Ads are labeled “Advertisement” and served by Adsterra Network. Affiliate links, if any, will be identified as such.</p>
<h2>6. Governing law</h2>
<p>This notice is governed by Spanish law. The Spanish version is the reference text.</p>
<p class="small">Last updated: November 20, 2026.</p>'''

PRIVACY = '''<p class="note">Draft under the EU General Data Protection Regulation (GDPR, Regulation 2016/679) and Spain's data protection law (LOPDGDD, Organic Law 3/2018). The highlighted fields are still to be completed. This is not legal advice.</p>
<h2>Data controller</h2>
<p><mark class="fill">[Full name or company name]</mark>, Tax ID <mark class="fill">[NIF]</mark>, <mark class="fill">[address]</mark>. Contact: <mark class="fill">[contact email]</mark>.</p>
<h2>What data we process, why and on what legal basis</h2>
<ul>
<li><strong>Mailing list:</strong> there is currently no mailing list and no forms on the site. If we start one, we'll update this policy first and ask for your consent.</li>
<li><strong>Messages you send us:</strong> whatever you include, so we can reply. Legal basis: your consent.</li>
<li><strong>Hosting logs:</strong> the hosting provider may log IP addresses to keep the service secure. Legal basis: legitimate interest (Art. 6(1)(f) GDPR).</li>
<li><strong>Cookies:</strong> see the <a href="cookies.html">cookie policy</a>.</li>
</ul>
<p>We don't make automated decisions or build profiles with your data.</p>
<h2>Processors</h2>
<ul>
<li>Hosting: <mark class="fill">[GitHub Pages (GitHub Inc., USA) or another provider]</mark>. Transfers to the US rely on the EU-US Data Privacy Framework or standard contractual clauses.</li>
</ul>
<h2>Advertising</h2>
<p>If you accept it in the cookie notice, Adsterra Network, as an independent controller, processes online identifiers and device data to show and measure ads. Legal basis: your consent (Art. 6(1)(a) GDPR and Art. 22(2) LSSI), which you can withdraw at any time from “Cookie settings.” International transfers may occur; see <a href="https://adsterra.com/privacy-policy/" rel="noopener" target="_blank">Adsterra's privacy policy</a>.</p>
<h2>How long we keep it</h2>
<p>Messages you send us, as long as needed to reply. Your cookie choice is stored in your browser for 12 months.</p>
<h2>Your rights</h2>
<p>You can request access, rectification, erasure, objection, restriction and portability by writing to <mark class="fill">[contact email]</mark>. You can withdraw your consent to advertising at any time from “Cookie settings”; withdrawal doesn't affect what happened before. If you're not satisfied, you can complain to the Spanish Data Protection Agency (aepd.es) or your local authority.</p>
<h2>Age</h2>
<p>The game is rated for adults (PEGI 18 in Europe) and this site is intended for adults.</p>
<p class="small">Last updated: November 20, 2026. The Spanish version is the reference text.</p>'''

COOKIES = '''<h2>What they are</h2>
<p>Cookies and similar technologies (such as your browser's local storage) save information on your device.</p>
<h2>Who manages them</h2>
<p>The site owner (see the <a href="legal-notice.html">legal notice</a>). If you accept advertising, also Adsterra, as an independent third party.</p>
<h2>What we use</h2>
<div class="table-wrap" tabindex="0" role="region" aria-label="Table (scroll for more)"><table><thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead>
<tbody><tr><td>seisestrellas_consent</td><td>Essential (local storage, first party)</td><td>Remember your cookie choice</td><td>12 months</td></tr><tr><td>Adsterra cookies (Adsterra Network)</td><td>Advertising (third party)</td><td>Show ads, limit repetition, measure impressions and prevent fraud. Only loaded if you accept “Advertising.”</td><td>Per <a href="https://adsterra.com/privacy-policy/" rel="noopener" target="_blank">Adsterra's policy</a>; data may be transferred outside the EEA</td></tr></tbody></table></div>
<p>Ads come from Adsterra. If you accept advertising, your browser loads a script from the <code>bauval.org</code> domain, which Adsterra uses to serve ads; that script runs on this page and the ad may set third-party cookies. <strong>None of this loads unless you accept advertising</strong>: instead you'll see a link to our free guide. We don't use analytics cookies or any statistics tools. Third-party cookies can't be deleted from our notice: do it from your browser. If we add new providers, we'll ask for your permission again.</p>
<h2>How to change your choice</h2>
<p>Click “Cookie settings” at the bottom of any page. Withdrawing consent doesn't affect earlier use. You can also clear site data in your browser:</p>
<ul>
<li><a href="https://support.google.com/chrome/answer/95647?hl=en" rel="noopener" target="_blank">Chrome</a></li>
<li><a href="https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox" rel="noopener" target="_blank">Firefox</a></li>
<li><a href="https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac" rel="noopener" target="_blank">Safari</a></li>
<li><a href="https://support.microsoft.com/en-us/microsoft-edge" rel="noopener" target="_blank">Edge</a></li>
</ul>
<p class="small">Last updated: November 20, 2026.</p>'''

SEARCH = '''<form id="search-form" class="search-form" role="search" action="search.html" method="get" data-index="../assets/search-index-en.json">
<label for="q" class="sr">Search GTA 6 questions</label>
<input id="q" name="q" type="search" autocomplete="off" placeholder="E.g. cheats, money, PC, saving" required>
<button type="submit" class="btn btn-primary">Search</button>
</form>
<p id="search-status" class="small" role="status" aria-live="polite"></p>
<ul id="search-results" class="list"></ul>
<noscript><p>Search needs JavaScript. Meanwhile, use the sections in the menu: <a href="questions/">Questions</a>, <a href="money/">Money</a>, <a href="issues/">Fixes</a>, <a href="pc-online/">PC &amp; Online</a> and <a href="leonida/">Leonida</a>.</p></noscript>'''


def pagina_404():
    """Página 404 en inglés: rutas absolutas porque GitHub Pages la sirve desde cualquier URL."""
    t = "Page not found | Six Stars"
    d = "The page you're looking for doesn't exist on Six Stars."
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="{sitio.THEME}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{sitio.preload("/")}
<link rel="stylesheet" href="/assets/style.css?v={sitio.CSS_V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{sitio.consent("en", "/en/")}
{sitio.header("en", "/en/", None, "/404.html")}
<main id="main" class="wrap narrow"><h1>This page doesn't exist</h1><p>It may have moved. Go back to the <a href="/en/">home page</a>, browse the <a href="/en/questions/">questions</a> or try the <a href="/en/search.html">search</a>.</p></main>
{sitio.footer("en", "/en/")}
<script src="/assets/site.js?v={sitio.JS_V}" defer></script>
</body></html>
'''
    return EN / "404.html", html


def sitemap(urls):
    sm = ROOT / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    # Conserva el lastmod que ya tuviera cada URL (lo mantiene mantenimiento.py fechas).
    previas = dict(re.findall(r'<url><loc>(https://6estrellas\.org/en/[^<]*)</loc><lastmod>([^<]*)</lastmod></url>', s))
    s = re.sub(r'  <url><loc>https://6estrellas\.org/en/[^<]*</loc><lastmod>[^<]*</lastmod></url>\n', "", s)
    nuevas = "".join(f'  <url><loc>{u}</loc><lastmod>{previas.get(u, PUB)}</lastmod></url>\n' for u in urls)
    s = s.replace("</urlset>", nuevas + "</urlset>")
    sm.write_text(s, encoding="utf-8", newline="")


def main():
    salida = [portada(), guia()]
    salida += [indice(s) for s in SECCIONES_EN]
    salida += [articulo(a) for a in ARTICULOS]
    NI = "noindex, follow"
    salida += [
        pagina("about.html", "About Six Stars: Who Writes This and How We Verify | Six Stars",
               "Who writes Six Stars, how we check every GTA 6 answer against cited sources, what our labels mean and how to reach us.",
               "Six Stars Editorial Team", ABOUT),
        pagina("legal-notice.html", "Legal Notice | Six Stars",
               "Legal notice for Six Stars: site owner, purpose, intellectual property, liability for the content and advertising.",
               "Legal notice", LEGAL, robots=NI),
        pagina("privacy.html", "Privacy Policy | Six Stars",
               "How Six Stars handles your data: no mailing list or analytics, and Adsterra advertising only if you give your consent.",
               "Privacy policy", PRIVACY, robots=NI),
        pagina("cookies.html", "Cookie Policy | Six Stars",
               "Which cookies Six Stars uses: one essential first-party item and, only if you accept advertising, Adsterra's. How to change your choice.",
               "Cookie policy", COOKIES, robots=NI),
        pagina("search.html", "Search Six Stars", "Search Six Stars' answers about GTA 6 by keyword: cheats, money, PC, saving and more.",
               "Search Six Stars", SEARCH, robots=NI, actual="buscar",
               extra_js=f'<script src="../assets/search.js?v={sitio.SEARCH_V}" defer></script>\n'),
        pagina_404(),
    ]
    for path, html in salida:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8", newline="")
    urls = [url("")] + [url(s + "/") for s in SECCIONES_EN] + [url("beginners-guide.html"), url("about.html")] + [url(a["en"]) for a in ARTICULOS]
    sitemap(urls)
    print(f"en: {len(salida)} páginas, {len(urls)} URLs en el sitemap")


if __name__ == "__main__":
    main()
