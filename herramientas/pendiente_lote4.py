import re, pathlib
root = pathlib.Path(r"C:\Users\marti\6 estrellas")
skip = {"google178e73f6eb6598d4.html"}
files = [p for p in root.rglob("*.html") if not set(p.relative_to(root).parts) & {".git", "auditoria", "herramientas"} and p.name not in skip]

# 0. buscar.html a partir de la plantilla de cookies.html
s = (root / "cookies.html").read_text(encoding="utf-8")
T = "Buscar en 6 Estrellas"
D = "Busca entre las respuestas de 6 Estrellas sobre GTA 6."
s = re.sub(r"<title>.*?</title>", f"<title>{T}</title>", s, count=1, flags=re.S)
s = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + D, s, count=1)
s = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + T, s, count=1)
s = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + D, s, count=1)
s = s.replace("https://6estrellas.org/cookies.html", "https://6estrellas.org/buscar.html")
main = '''<main id="main" class="wrap narrow"><h1>Buscar en 6 Estrellas</h1>
<form id="search-form" class="search-form" role="search" action="buscar.html" method="get">
<label for="q" class="sr">Buscar una pregunta sobre GTA 6</label>
<input id="q" name="q" type="search" autocomplete="off" placeholder="Ej.: trucos, dinero, PC, guardar partida" required>
<button type="submit" class="btn btn-primary">Buscar</button>
</form>
<p id="search-status" class="small" role="status" aria-live="polite"></p>
<ul id="search-results" class="cards"></ul>
<noscript><p>El buscador necesita JavaScript. Mientras tanto, usa las secciones del menú: <a href="preguntas/">Preguntas</a>, <a href="dinero/">Dinero y vehículos</a>, <a href="problemas/">Problemas técnicos</a>, <a href="novedades/">PC y Online</a> y <a href="lugares/">Leonida</a>.</p></noscript>
</main>'''
s, n = re.subn(r'<main id="main".*?</main>', lambda m: main, s, count=1, flags=re.S)
assert n == 1
s = s.replace('<script src="assets/site.js?v=7" defer></script>', '<script src="assets/site.js?v=7" defer></script>\n<script src="assets/search.js?v=1" defer></script>')
(root / "buscar.html").write_text(s, encoding="utf-8", newline="")
files.append(root / "buscar.html")

# 1. enlace "Buscar" en el menú de todas las páginas + versión del CSS
for p in files:
    t = p.read_text(encoding="utf-8")
    o = t
    if "buscar.html" not in t.split("</nav>")[0] or p.name == "buscar.html":
        m = re.search(r'<li><a class="nav-cta" href="((?:\.\./)?)guia-inicio\.html">', t)
        if m and 'Buscar</a>' not in t:
            pre = m.group(1)
            t = t.replace(m.group(0), f'<li><a href="{pre}buscar.html">Buscar</a></li>\n' + m.group(0), 1)
    t = re.sub(r'style\.css\?v=\d+', 'style.css?v=5', t)
    if p.name == "index.html" and p.parent == root and 'id="home-search"' not in t:
        form = ('<form class="search-form" id="home-search" role="search" action="buscar.html" method="get">'
                '<label for="q-home" class="sr">Buscar una pregunta sobre GTA 6</label>'
                '<input id="q-home" name="q" type="search" placeholder="Busca: trucos, dinero, PC, guardar partida…" required>'
                '<button type="submit" class="btn btn-primary">Buscar</button></form>')
        t, k = re.subn(r'(<p class="lead">.*?</p>)', lambda m: m.group(1) + "\n" + form, t, count=1, flags=re.S)
        assert k == 1
    if t != o:
        p.write_text(t, encoding="utf-8", newline="")

# 2. CSS del buscador
css = root / "assets" / "style.css"
c = css.read_text(encoding="utf-8")
if ".search-form" not in c:
    c += '''
/* Buscador interno */
.search-form{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 8px;max-width:560px}
.search-form input{flex:1 1 220px;min-width:0;font:inherit;padding:11px 12px;border:1px solid var(--field);border-radius:8px;background:var(--surface);color:var(--ink)}
.search-form input::placeholder{color:var(--muted)}
.result-s{font-size:.78rem;font-weight:600;color:var(--brand);text-transform:uppercase;letter-spacing:.06em}
#search-results{margin-top:12px}
'''
    css.write_text(c, encoding="utf-8", newline="")
print("ok", len(files))
