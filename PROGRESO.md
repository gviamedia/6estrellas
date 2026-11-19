# Progreso de 6estrellas.org

Estado a 20/11/2026. Todo lo descrito como "hecho" está publicado en `main` y comprobado en vivo.

## Hecho
- **Lote 1:** `.gitignore`, formularios de email retirados, un solo anuncio por artículo, banner de cookies compacto y accesible, texto de cookies acorde al código.
- **Lote 2:** ficha «Redacción 6 Estrellas» en `sobre.html` (contacto `contacto@6estrellas.org`), firma en cada artículo, etiquetas de certeza sin «probado», correcciones de contenido, guía PDF huérfana retirada.
- **Lote 3:** enlaces internos a páginas poco enlazadas, H1 de la policía alineado con la consulta, atribución del mapa.
- **Lote 4:**
  - Buscador interno: `buscar.html` (con `noindex`, fuera del sitemap), `assets/search.js` y `assets/search-index.json`. Enlace «Buscar» en el menú de todas las páginas y formulario en la portada.
  - Fechas reales: `dateModified` de cada artículo y `lastmod` del `sitemap.xml` salen del último commit de contenido de la página.
  - Declaración oficial de Take-Two en `gta-6-online` (comunicado de reservas del 24-06-2026: «features a single-player experience»). Quitado el texto que mandaba a un formulario de email que ya no existe.
- **Contenido de lanzamiento (5 páginas nuevas):** trofeos y logros, parches (actualización 1.002), armas, mods y cooperativo. En su índice, la portada, el sitemap y el buscador.
- Rama `mejoras/lote-3-contenido` borrada.

## Falta, por orden
1. **Más páginas de lanzamiento** cuando haya fuentes fiables posteriores al lanzamiento: coches más rápidos, primera misión y guía de misiones, errores de servidor y códigos. La búsqueda web solo devolvió material anterior al lanzamiento o de baja calidad, así que no se publicó nada de eso.
2. **Revisar las páginas con datos que el lanzamiento confirme o desmienta**, sobre todo `trofeos-logros` (lista oficial), `armas`, `gta-6-pc` y `emisoras-radio`. Se actualizó solo `gta-6-online`.
3. **Generador de plantillas.** `herramientas/paginas_lanzamiento.py` y `herramientas/mantenimiento.py` cubren páginas nuevas, índice del buscador y fechas, pero no hay un generador completo para cambios globales.
4. Rama antigua `mejoras/lote-4-buscador` (obsoleta, sin uso): se puede borrar.

## Cómo mantenerlo
- Tras cambiar una página: commit del contenido, `python herramientas/mantenimiento.py todo`, commit con mensaje «Fechas: …», push.
- Páginas nuevas: añadir su definición a `herramientas/paginas_lanzamiento.py` y ejecutarlo.

## Decisiones tomadas
- **Sin fuente, no se publica:** por eso no hay página de coches, misiones ni errores. Las tres páginas con una sola fuente llevan la etiqueta «Una sola fuente» o «Parcialmente confirmado».
- **Trofeos y logros:** la cifra de 55 viene de GTABase (actualizada el 18-11-2026) y de una filtración recogida por Notebookcheck e Insider Gaming. No hay lista oficial de Rockstar en lo que hemos revisado, y así se dice.
- **Armas:** se cita solo GTABase (205 armas listadas). No se afirma ningún «mejor arma».
- **`buscar.html` con `noindex`** y fuera del sitemap, porque son resultados de búsqueda interna.
- **`datePublished` no se modifica.** `dateModified` usa la hora del último commit de contenido. Ojo: el commit que añadió «Buscar» al menú tocó todas las páginas, así que todas muestran la misma hora de modificación del 20-11-2026.
- Los commits usan el autor ya existente del repositorio.
