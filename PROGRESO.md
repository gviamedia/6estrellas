# Progreso de 6estrellas.org

Estado a 19/11/2026. Todo lo descrito como "hecho" está publicado en `main`.

## Hecho
- Lote 1: `.gitignore`, formularios de email retirados, un solo anuncio por artículo, banner de cookies compacto y accesible, texto de cookies acorde al código.
- Lote 2: ficha "Redacción 6 Estrellas" en `sobre.html` (contacto `contacto@6estrellas.org`), firma en cada artículo, etiquetas de certeza sin "probado", correcciones de contenido, guía PDF huérfana retirada.
- Lote 3: enlaces internos a páginas poco enlazadas, H1 de la policía alineado con la consulta, atribución del mapa.
- Rama `mejoras/lote-3-contenido` borrada.

## En curso (lote 4, sin publicar)
- `herramientas/mantenimiento.py`: genera `assets/search-index.json` (comando `indice`) y sincroniza `dateModified` y `lastmod` del sitemap con la fecha real del último cambio en git (comando `fechas`).
- `assets/search.js`: buscador en el navegador, con sinónimos España/Latinoamérica. Sin cookies ni servidor.
- `herramientas/pendiente_lote4.py`: script que crea `buscar.html`, añade "Buscar" al menú de todas las páginas, un formulario en la portada y el CSS (`style.css?v=5`). **Aún no se ha ejecutado.**

## Falta, por orden
1. Ejecutar `python herramientas/pendiente_lote4.py` y luego `python herramientas/mantenimiento.py indice`. Después comprobar enlaces, JSON-LD y `node --check assets/site.js`, y probar la búsqueda en el navegador.
2. Commit del contenido, `python herramientas/mantenimiento.py fechas`, commit "Fechas: …", push y comprobación en vivo.
3. Contenido de lanzamiento: mínimo 5 páginas nuevas (trucos, dinero, misiones, coches, armas, trofeos, errores y parches), con respuesta corta, fuentes, etiqueta de certeza, firma, enlaces internos, sitemap e índice de sección.
4. Revisar páginas existentes con datos que el lanzamiento haya confirmado o desmentido.
5. Generador de plantillas, si queda tiempo.

## Decisiones tomadas
- Declaración de Take-Two sobre GTA 6 Online: **no publicada**. Solo encontré fuentes secundarias (prensa) que la citan; hace falta el comunicado o la transcripción oficial de Take-Two.
- `buscar.html` irá con `noindex` y fuera del sitemap (páginas de búsqueda interna).
- `datePublished` no se modifica; `dateModified` usa la hora real del último commit de cada página.
- Los commits usan el autor ya existente del repositorio.
