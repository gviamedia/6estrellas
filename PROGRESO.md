# Progreso de 6estrellas.org

Estado a 20/11/2026. Todo lo descrito como "hecho" está publicado en `main` y comprobado en vivo.

## Hecho
- **Actualización con lo publicado en los dos primeros días (20/11/2026, tarde), en los dos idiomas.** Búsqueda en guías, prensa y lo que la prensa recoge de foros y YouTube. Solo se publica con fuente; lo de una sola fuente o de jugadores va marcado.
  - `trucos` / `cheats`: los **61 trucos** con su requisito de desbloqueo y los **19 códigos** conocidos. 17 coinciden en PowerPyx, Red Bull y Vandal; «Subir el nivel de búsqueda» está en dos fuentes y «Borrachera» en una sola, y así se marca. Avisos: no hay trucos por número de teléfono (Red Bull) y los códigos de cajas fuertes son aleatorios (GameSpot). Datos en `herramientas/trucos_datos.py`; en móvil, cada truco es una ficha (nombre, código, requisito).
  - Página nueva `preguntas/secretos-easter-eggs.html` / `en/questions/secrets-easter-eggs.html`: abducción alienígena con trofeo y su continuación (GameSpot y The Tab), el huevo de la torre más alta de Vice City (GameSpot y GamingBible), Bigfoot, el piso de Dexter, guiños a Red Dead y Liberty City, The Vault Radio. El perro socorrista y el barco de Michael van en «Sin confirmar».
  - `emisoras-radio`: las **22 emisoras** según GameSpot (comprobadas en el juego) más la secreta The Vault Radio y cómo desbloquearla; las 6 oficiales de Rockstar van marcadas.
  - `misiones-capitulo-1`: ahora con los cinco capítulos (122 entradas de GTABase, nombres de capítulo y las cuatro perdibles). Los capítulos 2 a 5 van plegados con aviso de spoilers. Mismo slug; título y H1 nuevos.
  - `ganar-dinero`: cómo atracar sin que salte la alarma (GameSpot): niveles de seguridad, alarma, cámaras, ganzúa, cajas fuertes aleatorias, billetes marcados y bolsas de tinta.
  - Comprobado sin cambios: el ranking de coches de GTABase sigue sin velocidades medidas; Sony no ha dado la causa de la caída de PSN; no hay notas de parche ni versión nueva después de la 01.002.001.
  - Script de la tanda: `herramientas/actualizar_20nov.py` (idempotente).
- **Imágenes que aportan información (20/11/2026):** a petición del dueño, las imágenes enseñan aquello de lo que habla el texto.
  - `mapa-leonida`: la imagen principal es el **mapa oficial de Leonida** (póster de Rockstar, sin recortar, con enlace a tamaño grande) y hay una galería con las seis zonas. Con el mapa como fuente se ha añadido «Lo que muestra el mapa oficial»: cinco condados (Lummox, Kelly, Leonard, Vice-Dale y Mariana) y dónde queda cada zona.
  - `protagonistas`: retrato de Jason y de Lucia bajo su apartado, y los seis personajes oficiales que nombra la página, cada uno con su nombre.
  - `precio-ediciones`: en español se ha añadido «Qué añade la Ultimate Edition» (lista de Rockstar Support, que ya era fuente) y, en los dos idiomas, una galería con seis de esos extras.
  - `ganar-dinero`: atraco a una tienda y caza en Mount Kalaga (condado de Lummox, según el mapa oficial). `armas`: los revólveres Hawk & Little Morgan.
  - Las imágenes del texto llevan pie con lo que se ve, el crédito y `loading="lazy"` (no son la primera de la página). Datos en `GALERIAS` de `herramientas/imagenes_datos.py`; 62 imágenes en total (124 archivos), todas por debajo de 200 KB (el mapa grande, 191 KB, con el texto legible).
- **Imágenes oficiales (20/11/2026):** nueva regla del dueño: solo capturas y artes oficiales de Rockstar Games, con el crédito visible «Imagen: Rockstar Games» / «Image: Rockstar Games». 42 imágenes de los paquetes oficiales de descarga de <https://www.rockstargames.com/VI/media> (capturas por personaje y lugar, y ventajas de la Ultimate Edition): una por artículo, por índice de sección, por la portada y por la guía, elegidas por tema (Leonida en lugares, Grotti Cheetah en el coche más rápido, Jason y Lucia donde se habla de ellos…). Se descartaron las de contenido sexual explícito. No se usa el logo de GTA VI.
  - WebP en 800 y 1600 px (16:9), todas por debajo de 200 KB (`assets/img/`, 6,9 MB en total), con `srcset`, `width`/`height`, `alt` descriptivo en cada idioma y sin `loading="lazy"` porque cada página tiene una sola imagen (la primera). `fetchpriority="high"` en portada e índices, donde la imagen está arriba.
  - La imagen principal va también en `og:image` (con tipo, tamaño y alt) y en el `image` del JSON-LD de cada artículo.
  - En el diseño: proporción fija (16:9; 21:9 en los índices en escritorio), a sangre en móvil, sin esquinas ni sombras. En los artículos va justo después de la respuesta corta, para no retrasarla.
  - Origen de cada imagen en `herramientas/imagenes.md`; la asignación y los textos alternativos están en `herramientas/imagenes_datos.py`; `herramientas/imagenes.py RUTA` regenera los WebP desde los ZIP oficiales (los originales no se guardan en el repositorio). `comprobar.py` revisa alt, dimensiones, srcset, crédito, og:image y el límite de 200 KB.
  - «Quiénes somos»/«About» y el aviso legal explican el origen de las imágenes.
  - **Riesgo anotado:** la política de Rockstar/Take-Two sobre material de fans restringe el uso comercial, y la web lleva anuncios. Decisión del dueño; conviene revisarlo si llegan ingresos.
- **Versión en inglés «Six Stars» (20/11/2026):** 48 páginas en `/en/`: portada, 5 índices, 35 artículos, guía de inicio (`beginners-guide.html`), sobre (`about.html`), aviso legal, privacidad, cookies, buscador (`search.html`) y 404. Redactada para lectores de EE. UU. (títulos, H1, descripciones y slugs en inglés; términos de la comunidad: *Wasted/Busted*, *fences*, *wanted level*, *safehouse*), no traducida frase a frase. Firma «Six Stars Editorial Team». Fuentes originales en inglés cuando existen (Rockstar Newswire, Rockstar Support, Take-Two IR, prensa en inglés); las que solo existen en español o alemán se marcan como tales. Etiquetas de certeza traducidas y explicadas en `about.html`. Precio en dólares (Take-Two: 79,99 $ y 99,99 $) y horas en ET.
  - SEO: `lang="en"`, canonical propio, hreflang es/en/x-default recíprocos en las 47 parejas (x-default = español), JSON-LD con `inLanguage: "en"`, `og:locale en_US`, 43 URLs inglesas en el sitemap (las legales, el buscador y la 404 van con `noindex`, igual que en español).
  - Selector ES/EN en la cabecera de todas las páginas, que lleva a la página equivalente.
  - Mismo aviso de cookies y misma carga de Adsterra (un hueco por artículo, solo tras consentimiento), con textos en inglés. Buscador con su propio índice (`assets/search-index-en.json`) y sinónimos en inglés.
  - La 404 de la raíz manda las URLs inexistentes de `/en/` a `/en/404.html` (GitHub Pages solo sirve la 404 de la raíz).
  - Los huecos legales siguen pendientes, igual que en español; la versión española es el texto de referencia.
- **Rediseño (20/11/2026, publicado y comprobado en vivo en móvil y escritorio):** estilo de revista. Papel claro `#f6f3ed`, tinta `#121110`, un solo acento magenta `#d1006a` (contraste 4,7:1) solo en filetes, números, etiquetas y enlace activo. Oswald (titulares) y Source Serif 4 (cuerpo) alojadas en `assets/fonts/` con su licencia OFL; sin Google Fonts. Logo tipográfico, portada con pieza destacada + «Lo más consultado» + listas numeradas por sección, índices como listas de periódico con entradillas completas, respuesta corta con filete, fuentes numeradas, anuncio integrado y etiquetado. Sin modo oscuro, degradados, sombras ni esquinas redondeadas. Comprobado a 375 px sin desplazamiento horizontal; en producción, cero peticiones a Adsterra antes de aceptar.
- **Revisión independiente (20/11/2026):** ver «Correcciones de la revisión».
- **Lote 1:** `.gitignore`, formularios de email retirados, un solo anuncio por artículo, banner de cookies compacto y accesible, texto de cookies acorde al código.
- **Lote 2:** ficha «Redacción 6 Estrellas» en `sobre.html` (contacto `contacto@6estrellas.org`), firma en cada artículo, etiquetas de certeza sin «probado», correcciones de contenido, guía PDF huérfana retirada.
- **Lote 3:** enlaces internos a páginas poco enlazadas, H1 de la policía alineado con la consulta, atribución del mapa.
- **Lote 4:** buscador interno (`buscar.html`, `noindex`, fuera del sitemap), fechas reales (`dateModified` y `lastmod` desde git), declaración oficial de Take-Two en `gta-6-online`.
- **Páginas de lanzamiento (8):** trofeos y logros, parches (1.002), armas, mods, cooperativo, coche más rápido, misiones del Capítulo 1 y fallos de PSN.
- Ramas `mejoras/lote-3-contenido` y `mejoras/lote-4-buscador` borradas. Queda `mejoras/lote-1-quick-wins` (ya fusionada, se puede borrar).

## Correcciones de la revisión (20/11/2026)
Fuentes abiertas y leídas (GamesRadar y PC Gamer, que no se leen sin JavaScript, con navegador). Casi todo se sostenía; se corrigió esto:
- `xbox-one-ps4`: decía que hacía falta Game Pass «según la ficha de Xbox»; la ficha no lo dice. Ahora se apoya en el soporte de Rockstar (nube en Series X|S y Xbox One con ajustes de Series S; Remote Play) y dice que Rockstar no detalla la suscripción.
- `gta-plus` y `precio-ediciones`: el plazo «31/03/2027» atribuido a la PS Store no aparece en ella; retirado. El «10 % sin concretar» es, según Vandal, en la venta de vehículos. Añadido el Newswire de Rockstar (GTA+ ya incluye ventajas de GTA VI) y que las reservas físicas también traían el Pack Vintage Vice City.
- `cuanto-dura`: Nelson habló de una partida durante el desarrollo, no de una «versión previa»; la descripción ya no atribuye las 80 h a «Rockstar» en general; añadidas las 50 h de campaña (Demócrata/MeriStation), que respaldan el «50 a 80».
- `guardar-partida`: etiqueta «Una sola fuente» con dos fuentes; ahora con GamesRadar, Vandal y PowerPyx y cuándo no se puede guardar. `trucos`: tres fuentes coinciden; etiqueta corregida.
- `comprar-casas`: «Brian le deja la casa gratis» → sin alquiler a cambio de ayudarle (VICE); fuera «pendiente de verificar en el juego», que insinuaba pruebas propias.
- Índice de Preguntas: decía «99 en OpenCritic» sin fuente; retirado.
- `idioma-espanol`: añadida la PS Store (voz en inglés; «Español» y «Español (México)»). `coches-garajes`: el artículo de PC Games es del 8/09/2026, previo al lanzamiento, y ahora se dice. `ganar-dinero`: la nota de este archivo que decía que era de prelanzamiento era errónea (PC Gamer y GamesRadar son del 19/11); añadidos atracos por puerta trasera y Pilot Pete.
- Legales: la privacidad hablaba de una lista de correo que no existe y el aviso legal de una «guía en PDF» retirada; corregidos. Descripciones de las legales ampliadas; títulos largos (misiones, PSN) acortados.
- Técnico: código muerto del formulario de correo fuera de `site.js`; título accesible en el iframe del anuncio; orden de encabezados de la guía (h1 → h2); BreadcrumbList en los 5 índices; `mantenimiento.py` ya no cambia `dateModified` por commits de diseño («Diseño:»).

## Backlog de la auditoría (26 puntos) frente a lo hecho
- **Hecho:** 2, 3, 4, 5, 6, 7, 9, 11 (sustituido el 20/11 por la nueva regla: solo imágenes oficiales de Rockstar con crédito), 12, 13, 14, 19 (buscador), 21, 25. **8** en parte: etiquetas por artículo y explicación en `sobre.html`; no hay bloque «cómo lo hemos comprobado» por artículo porque repetiría la sección de fuentes. **15** en parte: 8 de 9 temas (falta lo de abajo). **10** en parte: `herramientas/sitio.py` (cabecera, menú, pie, aviso), `rediseno.py` y `generar_en.py` dan una plantilla común; el contenido en español sigue en los HTML.
- **Anulados por el dueño:** 16 (pruebas propias) y la puerta del gestor.
- **Dependen del dueño:** 1 (datos del titular: siguen pendientes por decisión suya), 17 (Search Console/Bing: no hay acceso), 23 (canal de distribución), 26 (registro de marca).
- **No se hacen, con motivo:**
  - 18 (Brevo y lista de correo): sin tráfico medido no compensa el trabajo legal y de mantenimiento; la privacidad ya dice que no hay lista.
  - 19 (RSS y «Actualizado hoy»): poco impacto con el tráfico actual; las fechas reales ya están en cada página y en el sitemap.
  - 20 (imágenes por página): hecho con imágenes oficiales de Rockstar, no propias (ver arriba).
  - 24 (aviso de spoilers): no hay spoilers publicados (las misiones van solo con títulos; finales sin detalles).
  - 15 restantes (descarga lenta, precios por país en Latinoamérica, GTA 6 frente a GTA V, DLC): no hay fuente fiable comprobada; precios por país exigirían revisar cada tienda.

## Falta, por orden
1. **Vigilar y actualizar** (páginas vivas, en los dos idiomas): `trucos` (42 códigos sin descubrir: actualizar `herramientas/trucos_datos.py`), `secretos-easter-eggs`, `emisoras-radio` (que Rockstar confirme las 22), `trofeos-logros` (lista oficial), `armas`, `coche-mas-rapido` (velocidades medidas), `psn-caido-inicio-sesion`, `actualizaciones-parches`. Revisión recomendada a los 7 días (27/11/2026) y a los 30 días (20/12/2026).
2. **Páginas sin fuente fiable posterior al lanzamiento:** localizaciones y secretos. No se han publicado.
3. Cuando se toque una página en español, actualizar también su equivalente en `herramientas/paginas_en.py` (y al revés).

## Cómo mantenerlo
- Cambio de contenido en español: editar el HTML, commit, `python herramientas/mantenimiento.py todo`, commit «Fechas: …», push.
- Cambio de contenido en inglés: editar `herramientas/paginas_en.py`, `python herramientas/generar_en.py`, commit, `mantenimiento.py todo`, commit «Fechas: …», push.
- Cambio de plantilla (cabecera, menú, pie, aviso, versiones `?v=`): editar `herramientas/sitio.py`, ejecutar `generar_en.py` y `rediseno.py`, commit con mensaje que empiece por «Diseño:».
- Antes de cada push: `python herramientas/comprobar.py` (enlaces, hreflang recíprocos, canonical, JSON-LD, sitemap, anuncios, versiones) y `node --check assets/site.js assets/search.js`.
- Páginas nuevas en español: `herramientas/paginas_lanzamiento.py`; su versión inglesa, una entrada más en `paginas_en.py`.

## Decisiones tomadas
- **Sin fuente, no se publica**, en ningún idioma.
- **Misiones:** solo títulos, sin trama. En inglés se usa la lista de GTABase (27 misiones en el Capítulo 1; GTABase se salta el número 24).
- **Coches:** ranking provisional de una sola fuente (GTABase); puntuaciones sobre 10, no velocidades.
- **PSN:** ninguna cifra de Downdetector (IBTimes y Digit discrepan).
- **Inglés:** x-default apunta al español (versión original). La 404 inglesa y los legales en inglés llevan `noindex`, como en español.
- `buscar.html` y `en/search.html` van con `noindex` y fuera del sitemap.
- `datePublished` no se modifica; `dateModified` usa el último commit de contenido (ni «Fechas:» ni «Diseño:»).
- Los commits usan el autor ya existente del repositorio.
