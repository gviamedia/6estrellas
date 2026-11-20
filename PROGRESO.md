# Progreso de 6estrellas.org

Estado a 20/11/2026. Todo lo descrito como "hecho" está publicado en `main` y comprobado en vivo.

## Hecho
- **Rediseño (20/11/2026, publicado y comprobado en vivo en móvil y escritorio):** estilo de revista. Papel claro `#f6f3ed`, tinta `#121110`, un solo acento magenta `#d1006a` (contraste 4,7:1) solo en filetes, números, etiquetas y enlace activo. Oswald (titulares) y Source Serif 4 (cuerpo) alojadas en `assets/fonts/` con su licencia OFL; sin Google Fonts. Logo tipográfico, portada con pieza destacada + «Lo más consultado» + listas numeradas por sección, índices como listas de periódico con entradillas completas, respuesta corta con filete, fuentes numeradas, anuncio integrado y etiquetado. Sin modo oscuro, degradados, sombras ni esquinas redondeadas. Plantilla común en `herramientas/sitio.py`; `herramientas/rediseno.py` la aplica a las páginas en español (idempotente). Comprobado a 375 px sin desplazamiento horizontal; en producción, cero peticiones a Adsterra antes de aceptar.
- **Revisión independiente de contenido (20/11/2026):** ver «Correcciones de la revisión» más abajo.
- **Lote 1:** `.gitignore`, formularios de email retirados, un solo anuncio por artículo, banner de cookies compacto y accesible, texto de cookies acorde al código.
- **Lote 2:** ficha «Redacción 6 Estrellas» en `sobre.html` (contacto `contacto@6estrellas.org`), firma en cada artículo, etiquetas de certeza sin «probado», correcciones de contenido, guía PDF huérfana retirada.
- **Lote 3:** enlaces internos a páginas poco enlazadas, H1 de la policía alineado con la consulta, atribución del mapa.
- **Lote 4:** buscador interno (`buscar.html`, `noindex`, fuera del sitemap), fechas reales (`dateModified` y `lastmod` desde git), declaración oficial de Take-Two en `gta-6-online`.
- **Páginas de lanzamiento (8):** trofeos y logros, parches (1.002), armas, mods, cooperativo, coche más rápido, misiones del Capítulo 1 y fallos de PSN el día del lanzamiento. Todas en su índice, la portada, el sitemap y el buscador.
- **Revisión de páginas existentes con fuentes del 19-20/11/2026:**
  - `gta-6-pc`: añadido el comunicado oficial de Take-Two (19-11-2026), que solo cita PS5 y Xbox Series X|S y no menciona PC.
  - `emisoras-radio`: GTABase lista 21 emisoras pero dice que la lista completa no se ha revelado oficialmente; se mantienen las 6 confirmadas por Rockstar.
  - `trofeos-logros`: la guía de GTABase no ha cambiado (18-11-2026); añadido que 28 son ocultos.
  - `armas`: **no se ha vuelto a comprobar** (no apareció una fuente nueva); sigue con una sola fuente.
- Ramas `mejoras/lote-3-contenido` y `mejoras/lote-4-buscador` borradas. Queda `mejoras/lote-1-quick-wins` (ya fusionada, se puede borrar).

## Falta, por orden
1. **Vigilar y actualizar** (páginas vivas): `trofeos-logros` (lista oficial), `armas`, `coche-mas-rapido` (GTABase añadirá velocidades medidas), `misiones-capitulo-1` (capítulos 2 a 5, «en construcción» en Vandal el 19-11), `psn-caido-inicio-sesion` (si Sony confirma la causa), `actualizaciones-parches` (notas oficiales).
2. **Páginas que siguen sin fuente fiable posterior al lanzamiento:** dinero (cómo ganarlo, la página actual es de prelanzamiento), localizaciones y secretos. No se han publicado.
3. **Generador de plantillas:** `herramientas/paginas_lanzamiento.py` y `herramientas/mantenimiento.py` cubren páginas nuevas, índice del buscador y fechas, pero no hay un generador completo para cambios globales.

## Cómo mantenerlo
- Tras cambiar una página: commit del contenido, `python herramientas/mantenimiento.py todo`, commit con mensaje «Fechas: …», push.
- Páginas nuevas: añadir su definición a `herramientas/paginas_lanzamiento.py` y ejecutarlo.

## Decisiones tomadas
- **Sin fuente posterior al 19/11/2026, no se publica.** Las 3 páginas nuevas de esta tanda salen de fuentes del 19-11-2026 leídas completas: Vandal (misiones), GTABase (coches) e IBTimes, Digit y Endgame Tools (PSN).
- **Misiones:** solo se publican títulos, sin detalles de la trama. Las guías no coinciden en el orden exacto y la página lo dice. Dos misiones se marcan como opcionales y perdibles (GTABase).
- **Coches:** el ranking es provisional y de una sola fuente (GTABase). Son puntuaciones sobre 10, no km/h.
- **PSN:** no se da ninguna cifra de Downdetector porque IBTimes y Digit discrepan. Sony no ha vinculado el fallo con GTA 6. Las soluciones son recomendaciones de la prensa y así se indican.
- **No se ha publicado el estado de los servidores de Rockstar:** su página de soporte no se pudo leer (timeout).
- `buscar.html` va con `noindex` y fuera del sitemap.
- `datePublished` no se modifica; `dateModified` usa la hora del último commit de contenido.
- Los commits usan el autor ya existente del repositorio.
