#!/usr/bin/env python3
"""Avisa a los buscadores compatibles con IndexNow (Bing, Yandex, Seznam, Naver...) de las URLs del sitemap.
Google no usa IndexNow: para Google cuenta el sitemap (robots.txt) y Search Console.

Uso: python herramientas/indexnow.py           -> envía todas las URLs del sitemap
     python herramientas/indexnow.py URL ...   -> envía solo esas
La clave es el archivo <clave>.txt de la raíz (debe estar publicado antes de enviar).
"""
import json, pathlib, re, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "6estrellas.org"
claves = [p for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem) and p.read_text().strip() == p.stem]
if not claves:
    sys.exit("No hay archivo de clave IndexNow en la raíz")
key = claves[0].stem
urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
body = json.dumps({"host": HOST, "key": key, "keyLocation": f"https://{HOST}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, method="POST",
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow:", r.status, f"({len(urls)} URLs)")
except urllib.error.HTTPError as e:
    print("IndexNow: error", e.code, e.read()[:300])
