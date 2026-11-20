#!/usr/bin/env python3
"""Convierte las imágenes oficiales de Rockstar a WebP y documenta su origen.

Uso: python herramientas/imagenes.py RUTA
  RUTA: carpeta donde se han extraído los ZIP oficiales (subcarpetas shots/ y ultimate/), ver
  herramientas/imagenes_datos.py. Los originales no se guardan en el repositorio.
Genera assets/img/<clave>-800.webp y -1600.webp (16:9, recorte centrado, cada una <= 200 KB)
y reescribe herramientas/imagenes.md. Requiere Pillow.
"""
import pathlib, sys
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from imagenes_datos import IMAGENES, PAGINAS, ZIPS, PAGINA_OFICIAL, SIN_RECORTE, GALERIAS

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"
MAX = 200 * 1024
TAMANOS = (800, 1600)


def recorte_16_9(im):
    w, h = im.size
    th = round(w * 9 / 16)
    if th <= h:
        top = (h - th) // 2
        return im.crop((0, top, w, top + th))
    tw = round(h * 16 / 9)
    left = (w - tw) // 2
    return im.crop((left, 0, left + tw, h))


def guardar(im, path):
    for q in (78, 72, 66, 60, 54, 48, 42, 36):
        im.save(path, "WEBP", quality=q, method=6)
        if path.stat().st_size <= MAX:
            return q
    raise SystemExit(f"{path.name} sigue por encima de 200 KB")


def main():
    src = pathlib.Path(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    en_galerias = {c for grupos in GALERIAS.values() for g in grupos for c, _, _ in g[3]}
    usadas = set(PAGINAS.values()) | en_galerias
    for viejo in OUT.glob("*.webp"):  # quita las que ya no usa ninguna página
        if viejo.name.rsplit("-", 1)[0] not in usadas:
            viejo.unlink()
    for clave in sorted(usadas):
        paquete, ruta, _, _ = IMAGENES[clave]
        im = Image.open(src / paquete / ruta).convert("RGB")
        if clave not in SIN_RECORTE:
            im = recorte_16_9(im)
        for w in TAMANOS:
            out = OUT / f"{clave}-{w}.webp"
            q = guardar(im.resize((w, round(w * im.height / im.width)), Image.LANCZOS), out)
            print(f"{out.name}: {out.stat().st_size // 1024} KB (q{q})")
    # Documentación del origen
    lineas = ["# Imágenes de la web", "",
              "Todas son capturas o artes oficiales de **Rockstar Games**, de los paquetes de descarga de la web oficial de GTA VI:",
              f"<{PAGINA_OFICIAL}>. Se muestran con el crédito «Imagen: Rockstar Games» / «Image: Rockstar Games».", "",
              "Paquetes de origen:", ""]
    lineas += [f"- `{k}`: <{v}>" for k, v in ZIPS.items()]
    lineas += ["", "Generadas con `python herramientas/imagenes.py RUTA_A_LOS_ZIP_EXTRAIDOS` (WebP 800 y 1600 px, 16:9, <= 200 KB).", "",
               "| Archivo | Origen (paquete / archivo) | Páginas |", "|---|---|---|"]
    for clave in sorted(usadas):
        paquete, ruta, _, _ = IMAGENES[clave]
        paginas = ", ".join([f"`{p}`" for p, c in PAGINAS.items() if c == clave] +
                            [f"`{p}` (en el texto)" for p, gs in GALERIAS.items() if any(c == clave for g in gs for c, _, _ in g[3])])
        lineas.append(f"| `assets/img/{clave}-{{800,1600}}.webp` | {ZIPS[paquete]} → `{ruta}` | {paginas} (y su versión en inglés) |")
    (ROOT / "herramientas" / "imagenes.md").write_text("\n".join(lineas) + "\n", encoding="utf-8", newline="")
    print(f"{len(usadas)} imágenes; herramientas/imagenes.md actualizado")


if __name__ == "__main__":
    main()
