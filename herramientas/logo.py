#!/usr/bin/env python3
"""Genera el logo de 6 Estrellas / Six Stars a partir de la tipografía de titulares (Oswald, OFL).

Concepto: «seis estrellas» es el nivel máximo de búsqueda policial. Monograma cuadrado en tinta con un «6»
en Oswald y una estrella magenta; al lado, el nombre en mayúsculas. Esquinas rectas, sin degradados.
No imita la marca ni el logo de GTA VI.

Uso (necesita fontTools, brotli y Pillow): python herramientas/logo.py
Salida en assets/: favicon.svg, logo-mark.svg, logo-es.svg, logo-en.svg, logo-512.png,
apple-touch-icon.png, og.png (español) y og-en.png (inglés).
"""
import io, math, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
A = ROOT / "assets"
INK, PAPER, ACCENT, MUTED = "#121110", "#f6f3ed", "#d1006a", "#56524b"

var = TTFont(A / "fonts" / "oswald-latin-wght.woff2")
font = instancer.instantiateVariableFont(var, {"wght": 700})
buf = io.BytesIO(); font.flavor = None; font.save(buf); TTF = buf.getvalue()
gs, cmap = font.getGlyphSet(), font.getBestCmap()
UPM = font["head"].unitsPerEm
CAP = font["OS/2"].sCapHeight or 0.7 * UPM


def glifo(ch):
    n = cmap[ord(ch)]
    pen = SVGPathPen(gs); gs[n].draw(pen)
    b = BoundsPen(gs); gs[n].draw(b)
    return pen.getCommands(), b.bounds, gs[n].width


def texto_path(txt, x, base, alto_cap, track=0.0):
    """Devuelve (paths, ancho) del texto con la altura de mayúscula indicada; y hacia abajo (SVG)."""
    s = alto_cap / CAP
    out, cx = [], x
    for ch in txt:
        if ch == " ":
            cx += gs[cmap[32]].width * s + track
            continue
        d, _, adv = glifo(ch)
        out.append(f'<path transform="translate({cx:.2f} {base:.2f}) scale({s:.5f} {-s:.5f})" d="{d}"/>')
        cx += adv * s + track
    return "".join(out), cx - x - track


def estrella(cx, cy, r, ri=None):
    ri = ri or r * 0.42
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else ri
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def marca_svg(size=64):
    """Monograma: cuadrado de tinta, «6» en papel, estrella magenta arriba a la derecha."""
    d, (x0, y0, x1, y1), _ = glifo("6")
    alto = 46.0
    s = alto / (y1 - y0)
    w = (x1 - x0) * s
    tx = 25 - w / 2 - x0 * s          # centrado algo a la izquierda para dejar sitio a la estrella
    ty = 32 + alto / 2 + y0 * s       # centrado vertical
    star = " ".join(f"{x:.2f},{y:.2f}" for x, y in estrella(50, 14.5, 9))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="{size}" height="{size}">'
            f'<rect width="64" height="64" fill="{INK}"/>'
            f'<path transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f} {-s:.5f})" fill="{PAPER}" d="{d}"/>'
            f'<polygon points="{star}" fill="{ACCENT}"/></svg>')


def lockup_svg(nombre):
    """Marca + nombre en una línea (para usar fuera de la web: prensa, redes)."""
    m = marca_svg().replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">', "").replace("</svg>", "")
    paths, w = texto_path(nombre, 80, 50, 36, track=1.5)
    total = 80 + w + 4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total:.0f} 64" role="img" aria-label="{nombre.title()}">'
            f'<g>{m}</g><g fill="{INK}">{paths}</g></svg>')


def marca_png(size):
    """Mismo monograma en PNG, dibujado con la fuente instanciada."""
    k = size / 64
    im = Image.new("RGB", (size, size), INK)
    dr = ImageDraw.Draw(im)
    d, (x0, y0, x1, y1), _ = glifo("6")
    alto = 46 * k
    f = ImageFont.truetype(io.BytesIO(TTF), size=int(alto * UPM / (y1 - y0)))
    bb = dr.textbbox((0, 0), "6", font=f)
    gw, gh = bb[2] - bb[0], bb[3] - bb[1]
    dr.text((25 * k - gw / 2 - bb[0], 32 * k - gh / 2 - bb[1]), "6", font=f, fill=PAPER)
    dr.polygon([(x * k, y * k) for x, y in estrella(50, 14.5, 9)], fill=ACCENT)
    return im


def og(nombre, lema, sub, ruta):
    W, H = 1200, 675
    im = Image.new("RGB", (W, H), PAPER)
    dr = ImageDraw.Draw(im)
    dr.rectangle([0, 0, W, 14], fill=INK)
    dr.rectangle([0, H - 6, W, H], fill=INK)
    m = marca_png(220)
    im.paste(m, (96, 150))
    fn = ImageFont.truetype(io.BytesIO(TTF), 132)
    dr.text((356, 140), nombre, font=fn, fill=INK)
    dr.rectangle([360, 318, 360 + 120, 326], fill=ACCENT)
    fl = ImageFont.truetype(io.BytesIO(TTF), 46)
    dr.text((360, 350), lema, font=fl, fill=INK)
    fs = ImageFont.truetype(io.BytesIO(TTF), 32)
    dr.text((362, 430), sub, font=fs, fill=MUTED)
    dr.text((96, 560), "6estrellas.org", font=fs, fill=INK)
    im.save(ruta, optimize=True)


(A / "favicon.svg").write_text(marca_svg(), encoding="utf-8")
(A / "logo-mark.svg").write_text(marca_svg(), encoding="utf-8")
(A / "logo-es.svg").write_text(lockup_svg("6 ESTRELLAS"), encoding="utf-8")
(A / "logo-en.svg").write_text(lockup_svg("SIX STARS"), encoding="utf-8")
marca_png(512).save(A / "logo-512.png", optimize=True)
marca_png(180).save(A / "apple-touch-icon.png", optimize=True)
og("6 ESTRELLAS", "Trucos, guías y respuestas sobre GTA 6", "Con fuentes enlazadas y fecha de revisión", A / "og.png")
og("SIX STARS", "GTA 6 cheats, guides and answers", "Every answer sourced and dated", A / "og-en.png")
print("logo generado")
