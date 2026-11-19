#!/usr/bin/env python3
"""Crea las páginas de lanzamiento (20/11/2026) a partir de la plantilla de un artículo existente,
las enlaza en su índice de sección, en la portada y en el sitemap, y regenera el índice del buscador.
Idempotente: si la página ya existe, no la vuelve a crear."""
import json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = "2026-11-20T01:00:00+01:00"
HUB = {"preguntas": "Preguntas", "novedades": "PC y Online", "dinero": "Dinero y vehículos", "problemas": "Problemas técnicos", "lugares": "Leonida"}

PAGINAS = [
    dict(dir="preguntas", slug="trofeos-logros",
         h1="¿Cuántos trofeos y logros tiene GTA 6? Lista y Platino",
         desc="Las fuentes hablan de 55 trofeos y logros, con un Platino en PS5. Lo que se sabe y lo que Rockstar no ha confirmado.",
         card="Las fuentes hablan de 55 trofeos y logros, con un Platino en PS5. Rockstar no ha publicado la lista.",
         chip=("warn", "Parcialmente confirmado"),
         answer="Según GTABase, hay 55 trofeos en PS5 y 55 logros en Xbox, con un Platino llamado «Vice Got a Price!». Varias webs atribuyen esa cifra a una filtración de datos y no hemos encontrado una lista publicada por Rockstar.",
         body="""<h2>Lo que dicen las fuentes</h2>
<ul>
<li><strong>PS5:</strong> 55 trofeos: 1 Platino, 2 de oro, 6 de plata y 46 de bronce.</li>
<li><strong>Xbox Series X|S:</strong> 55 logros que suman 1.000 de Gamerscore. El Platino de PlayStation equivale a un logro «Mythic» que no da puntos.</li>
<li><strong>Platino:</strong> se llama «Vice Got a Price!» y se consigue al desbloquear todos los demás.</li>
</ul>
<p>Estos datos son de la guía de GTABase, actualizada el 18 de noviembre de 2026.</p>
<h2>Lo que no está confirmado</h2>
<p>Notebookcheck e Insider Gaming recogieron la cifra de 55 como una filtración de datos del juego, y la propia guía de GTABase marca como «no confirmados» los pasos exactos de varios logros. No hemos encontrado una lista oficial publicada por Rockstar, así que el total y los nombres pueden cambiar.</p>
<h2>Trucos y trofeos</h2>
<p>Según GTABase, usar trucos desactiva los trofeos y logros. Mira cómo se desbloquean en <a href="trucos.html">trucos de GTA 6</a>.</p>""",
         sources=[("https://www.gtabase.com/articles/gta-6/gta-6-achievements-trophies-list-ps5-xbox-series", "GTABase: guía de trofeos y logros de GTA 6 (actualizada el 18-11-2026)"),
                  ("https://notebookcheck.net/GTA-6-leak-reveals-more-PS5-trophies-and-Xbox-achievements-on-release-date-than-GTA-5.1445073.0.html", "Notebookcheck: la filtración de trofeos y logros"),
                  ("https://insider-gaming.com/app/post/gta-6-55-trophies-achievements-mythic-platinum", "Insider Gaming: 55 trofeos y logros")],
         related=[("preguntas/trucos.html", "¿Hay trucos en GTA 6? Cómo se desbloquean"), ("preguntas/cuanto-dura.html", "¿Cuánto dura GTA 6? Horas de historia y del 100 %"), ("preguntas/finales-decisiones.html", "¿GTA 6 tiene varios finales? Decisiones que importan")]),

    dict(dir="novedades", slug="actualizaciones-parches",
         h1="¿Hay parches de GTA 6? Qué se sabe de la actualización 1.002",
         desc="La actualización 1.002.000 salió antes del lanzamiento. Tamaño en PS5 y Xbox, si es obligatoria y por qué no se sabe qué cambia.",
         card="Salió la actualización 1.002.000 antes del lanzamiento. Rockstar no ha publicado notas del parche.",
         chip=("warn", "Parcialmente confirmado"),
         answer="Sí. Antes del lanzamiento salió la actualización 1.002.000, marcada como obligatoria en PS5 (unos 1,07 GB) y de unos 2,18 GB en Xbox. Rockstar no ha publicado notas, así que no se sabe qué cambia.",
         body="""<h2>Lo que se sabe</h2>
<ul>
<li><strong>Versión:</strong> 1.002.000, citada para PS5.</li>
<li><strong>Tamaño:</strong> unos 1,07 GB en PS5 y unos 2,18 GB en Xbox Series X|S.</li>
<li><strong>Obligatoria:</strong> KeenGamer dice que es una descarga obligatoria; en PS5 aparece marcada como tal.</li>
<li><strong>Notas del parche:</strong> Rockstar no las ha publicado ni ha confirmado que sea un «parche de día uno».</li>
</ul>
<h2>Otras actualizaciones</h2>
<p>Según la prensa de videojuegos, hubo una actualización posterior, la 01.002.001, a mediados de noviembre, más pequeña en PS5. Tampoco se conocen sus cambios. Si ves listas detalladas de «arreglos», tómalas con cautela: son suposiciones, no notas de Rockstar.</p>
<h2>Qué hacer</h2>
<p>Instala las actualizaciones pendientes antes de jugar. Si el juego no arranca, mira <a href="../problemas/no-carga-errores.html">GTA 6 no carga o no arranca</a>, y para el espacio que necesitas, <a href="../problemas/tamano-descarga.html">cuánto ocupa GTA 6</a>.</p>""",
         sources=[("https://www.keengamer.com/articles/news/gta-6-update-1-002-starts-rolling-out-on-ps5-and-xbox-ahead-of-launch/", "KeenGamer: la actualización 1.002 empieza a llegar a PS5 y Xbox (13-11-2026)"),
                  ("https://mp1st.com/?p=318409", "MP1st: GTA 6 recibe la actualización 1.002"),
                  ("https://www.ggrecon.com/articles/gta-6-update-1-002-before-launch/", "GGRecon: GTA 6 recibe una actualización de 1 GB antes del lanzamiento"),
                  ("https://beatcopgame.com/gta-6-patch-notes-and-updates-tracker/", "BeatCop: seguimiento de parches de GTA 6")],
         related=[("problemas/tamano-descarga.html", "¿Cuánto ocupa GTA 6 en PS5 y Xbox?"), ("problemas/no-carga-errores.html", "GTA 6 no carga o no arranca: soluciones en PS5 y Xbox"), ("novedades/gta-6-online.html", "¿GTA 6 tiene modo online? Estado actual")]),

    dict(dir="preguntas", slug="armas",
         h1="¿Qué armas hay en GTA 6? Categorías y dónde se guardan",
         desc="GTABase lista 205 armas confirmadas y más por descubrir. Categorías, munición y cómo recuperarlas en Ammu-Nation o en tu vehículo.",
         card="GTABase lista 205 armas confirmadas, con más por descubrir. Categorías y dónde se guardan.",
         chip=("warn", "Una sola fuente"),
         answer="Según GTABase, hay 205 armas confirmadas, además de 24 objetos de equipo y 5 tipos de munición, y avisa de que quedan más por descubrir. Las armas compradas se recuperan en las taquillas de Ammu-Nation o en tu vehículo personal.",
         body="""<h2>Categorías</h2>
<p>La base de datos de GTABase agrupa las armas en estas categorías: rifles de asalto, pistolas, escopetas, subfusiles, cuerpo a cuerpo, rifles de francotirador, rifles tácticos, ametralladoras ligeras, lanzadores y armas arrojadizas.</p>
<p>Tipos de munición listados: pesada, de escopeta, de pistola, de lanza y cohetes.</p>
<h2>Dónde se guardan</h2>
<ul>
<li>Según GTABase, las armas compradas o que ya posees no se pierden de forma permanente y se recuperan en cualquier taquilla de Ammu-Nation o en tu vehículo personal.</li>
<li>Hay armas regionales únicas en sucursales concretas de Ammu-Nation.</li>
</ul>
<h2>¿Cuál es la mejor arma?</h2>
<p>No hemos encontrado un ranking fiable hecho con el juego ya a la venta: los que circulan son anteriores al lanzamiento. Esta es una sola fuente, y la propia GTABase dice que su lista es de las armas conocidas «hasta ahora» y que hay más sin descubrir.</p>
<p>Si buscas cómo te afecta la policía al usar armas, mira <a href="perder-a-la-policia.html">cómo funciona la policía</a>.</p>""",
         sources=[("https://www.gtabase.com/weapons/gta-6/", "GTABase: base de datos de armas de GTA 6 (actualizada en noviembre de 2026)")],
         related=[("preguntas/perder-a-la-policia.html", "¿Cómo perder a la policía en GTA 6? Así funciona el perfil criminal"), ("preguntas/trucos.html", "¿Hay trucos en GTA 6? Cómo se desbloquean"), ("dinero/ganar-dinero.html", "¿Cómo ganar dinero al empezar GTA 6?")]),

    dict(dir="novedades", slug="mods",
         h1="¿Habrá mods en GTA 6? Lo que dicen las normas de Rockstar",
         desc="Rockstar ha publicado normas de mods para todos sus juegos. Qué toleran, qué restringen y por qué no hay mods oficiales anunciados para GTA 6.",
         card="Rockstar ha publicado normas de mods para todos sus juegos. Qué toleran y qué restringen.",
         chip=("warn", "Parcialmente confirmado"),
         answer="Rockstar ha publicado normas de mods para todos sus juegos, GTA 6 incluido: toleran los mods de un jugador, sin conexión y sin ánimo de lucro, y restringen ampliar la historia, portar juegos o mezclar títulos. No hay versión de PC anunciada ni herramientas oficiales de mods.",
         body="""<h2>Qué permiten</h2>
<p>Según la prensa, las normas aceptan los proyectos de un jugador, sin conexión y sin ánimo de lucro que respeten la propiedad intelectual de terceros. Take-Two ha dicho que, en general, no emprende acciones legales contra ese tipo de proyectos en sus juegos de PC.</p>
<h2>Qué restringen</h2>
<ul>
<li>Ampliar o sustituir las misiones y la historia oficiales.</li>
<li>Portes no oficiales y mezclas entre juegos de la saga.</li>
<li>Mods de pago y multijugador: se dirigen a la plataforma oficial para creadores, basada en FiveM.</li>
</ul>
<h2>¿Y en GTA 6?</h2>
<p>Las normas son para toda la compañía y no son un anuncio de herramientas de mods para GTA 6. El juego solo está en PS5 y Xbox Series X|S; para PC, mira <a href="gta-6-pc.html">cuándo sale GTA 6 en PC</a>. No hemos encontrado un texto de Rockstar específico para mods de GTA 6.</p>""",
         sources=[("https://www.invenglobal.com/articles/26384/no-exception-for-gta-6-rockstar-releases-mod-guidelines-across-all-titles", "Inven Global: Rockstar publica normas de mods para todos sus títulos"),
                  ("https://games.gg/news/rockstar-tightens-mod-rules-gta-6/", "games.gg: Rockstar endurece las normas de mods"),
                  ("https://www.pcgamer.com/au/rockstar-is-talking-with-openiv-developer-issues-new-statement-on-mods", "PC Gamer: Rockstar habla con el desarrollador de OpenIV y aclara su postura sobre los mods")],
         related=[("novedades/gta-6-pc.html", "¿Cuándo sale GTA 6 en PC?"), ("novedades/gta-6-online.html", "¿GTA 6 tiene modo online? Estado actual"), ("preguntas/trucos.html", "¿Hay trucos en GTA 6? Cómo se desbloquean")]),

    dict(dir="preguntas", slug="cooperativo",
         h1="¿GTA 6 tiene cooperativo? Qué hay de multijugador",
         desc="No hay modo cooperativo confirmado para la historia de GTA 6. Qué ha dicho Rockstar, qué son rumores y qué pasa con el online.",
         card="No hay cooperativo confirmado para la historia. Lo único parecido es alternar entre Jason y Lucia.",
         chip=("warn", "Parcialmente confirmado"),
         answer="No hay cooperativo confirmado. Rockstar no ha anunciado un modo cooperativo para la historia y el juego salió como experiencia para un jugador, sin modo online.",
         body="""<h2>Lo único parecido al cooperativo</h2>
<p>Lo más cercano que se ha mostrado en la presentación oficial es alternar entre los dos protagonistas, Jason y Lucia, a medida que avanza la historia. Los detalles están en <a href="cambiar-jason-lucia.html">cambiar entre Jason y Lucia</a>.</p>
<h2>Rumores</h2>
<p>Algunos filtradores han hablado de una campaña para dos jugadores. Rockstar no lo ha confirmado, así que lo tratamos como rumor.</p>
<h2>Y el online</h2>
<p>GTA 6 salió como experiencia para un jugador y Rockstar no ha anunciado un modo online ni fecha. Consulta el <a href="../novedades/gta-6-online.html">estado actual del modo online</a>.</p>""",
         sources=[("https://www.svg.com/2245882/gta-6-online-multiplayer-rockstar-updates/", "SVG: lo que Rockstar ha dicho (y no) sobre el multijugador de GTA 6"),
                  ("https://beebom.com/gta-6-single-player-game/", "Beebom: ¿es GTA 6 solo para un jugador al lanzamiento?")],
         related=[("preguntas/cambiar-jason-lucia.html", "¿Se puede cambiar entre Jason y Lucia cuando quieras?"), ("novedades/gta-6-online.html", "¿GTA 6 tiene modo online? Estado actual"), ("preguntas/jugar-sin-internet.html", "¿Se puede jugar a GTA 6 sin internet?")]),
    dict(dir="dinero", slug="coche-mas-rapido",
         h1="¿Cuál es el coche más rápido de GTA 6? Ranking provisional",
         desc="GTABase aún no ha terminado de medir las velocidades. Su ranking provisional pone al Infernus '96, al Cheetah '95 y al Comet '88 en cabeza.",
         card="Aún no hay velocidades medidas. El ranking provisional de GTABase pone en cabeza al Infernus '96.",
         chip=("warn", "Una sola fuente"),
         answer="Todavía no se puede decir con seguridad. GTABase, que prueba los coches en el juego, no ha terminado sus mediciones; su ranking provisional del 19 de noviembre pone en cabeza al Pegassi Infernus '96, seguido del Grotti Cheetah '95 y el Pfister Comet '88.",
         body="""<h2>Ranking provisional por velocidad máxima</h2>
<ol>
<li><strong>Pegassi Infernus '96:</strong> 7,1 sobre 10.</li>
<li><strong>Grotti Cheetah '95:</strong> 6,6 sobre 10.</li>
<li><strong>Pfister Comet '88:</strong> 6,1 sobre 10.</li>
</ol>
<p>Son puntuaciones sobre 10, no kilómetros por hora. GTABase lista 30 coches y avisa de que el orden no es definitivo: añadirá posiciones y cifras cuando termine de probar cada coche en el juego.</p>
<h2>Otro ranking de la misma web</h2>
<p>En su lista de superdeportivos, ordenada por estadísticas generales, GTABase pone arriba al Pfister Comet '88, al Obey 8F Drafter y al Annis Elegy '90, y dice que está probando todos los vehículos en el juego. Esa lista no muestra fecha.</p>
<h2>Cómo conseguirlos</h2>
<p>GTABase aún marca como «próximamente» el modo de conseguir casi todos los coches, y no hemos encontrado una segunda fuente fiable. Para quedarte con un coche que ya tienes, mira <a href="coches-garajes.html">garajes y Pay 'n' Spray</a>.</p>""",
         sources=[("https://www.gtabase.com/articles/gta-6/gta-6-fastest-cars-ranked-list-by-top-speed", "GTABase: coches más rápidos de GTA 6, ranking por velocidad máxima (actualizado el 19-11-2026)"),
                  ("https://www.gtabase.com/gta-6/vehicles/best-vehicles/", "GTABase: lista de superdeportivos de GTA 6 por estadísticas")],
         related=[("dinero/coches-garajes.html", "¿Cómo quedarte un coche en GTA 6? Garajes y Pay 'n' Spray"), ("dinero/ganar-dinero.html", "¿Cómo ganar dinero al empezar GTA 6?"), ("preguntas/perder-a-la-policia.html", "¿Cómo perder a la policía en GTA 6? Así funciona el perfil criminal")]),

    dict(dir="preguntas", slug="misiones-capitulo-1",
         h1="¿Cuáles son las misiones del Capítulo 1 de GTA 6? Lista y cuáles se pueden perder",
         desc="Las misiones del Prólogo y del Capítulo 1 de GTA 6 según las guías del día del lanzamiento, y cuáles son opcionales y perdibles.",
         card="Las misiones del Capítulo 1 según las guías del día del lanzamiento, y cuáles se pueden perder.",
         chip=("warn", "Parcialmente confirmado"),
         answer="La historia tiene un Prólogo y cinco capítulos, según GTABase. En el Capítulo 1, la guía de Vandal del 19 de noviembre enumera nueve misiones, entre ellas «Día de pesca» y «¡Oye, Arnold!». Dos de ellas son opcionales y se pueden perder.",
         body="""<h2>Prólogo</h2>
<p>Según Vandal, el Prólogo consta de una única misión, que se llama igual que el capítulo.</p>
<h2>Capítulo 1</h2>
<p>Las misiones que enumera la guía de Vandal (solo títulos, sin detalles de la trama):</p>
<ul>
<li>Día de pesca</li>
<li>Equípate</li>
<li>Es solo un rasguño</li>
<li>Costes de laboratorio</li>
<li>Fontanería</li>
<li>Atención no deseada</li>
<li>Consigue el ron de Shirley (opcional)</li>
<li>Roba la scooter (opcional)</li>
<li>¡Oye, Arnold!</li>
</ul>
<p>GTABase, en inglés, sigue un orden algo distinto y añade más misiones del capítulo, como «Island Dreams». Las guías aún no coinciden en el orden exacto, así que no lo damos por cerrado.</p>
<h2>Cuáles se pueden perder</h2>
<p>GTABase marca como opcionales y perdibles «Get Shirley's Rum» y «Steal the Scooter», que corresponden a «Consigue el ron de Shirley» y «Roba la scooter». Vandal también avisa de que su guía señala el contenido que se puede perder. Como <a href="repetir-misiones.html">no se pueden repetir misiones</a>, conviene guardar antes: mira <a href="guardar-partida.html">cómo se guarda la partida</a>.</p>
<h2>Capítulos 2 a 5</h2>
<p>El 19 de noviembre, Vandal tenía los capítulos 2 a 5 marcados como «en construcción». Ampliaremos esta página cuando haya guías publicadas.</p>""",
         sources=[("https://vandal.elespanol.com/guias/guia-grand-theft-auto-vi-trucos-consejos-y-secretos/historia-y-misiones", "Vandal: historia y misiones en GTA 6 al 100 % (19-11-2026)"),
                  ("https://vandal.elespanol.com/guias/guia-grand-theft-auto-vi-trucos-consejos-y-secretos/prologo", "Vandal: todas las misiones del Prólogo y cómo completarlas (19-11-2026)"),
                  ("https://www.gtabase.com/gta-6/missions/", "GTABase: guía de misiones de la historia de GTA 6")],
         related=[("preguntas/repetir-misiones.html", "¿Se pueden repetir las misiones en GTA 6?"), ("preguntas/guardar-partida.html", "¿Cómo se guarda la partida en GTA 6?"), ("preguntas/cuanto-dura.html", "¿Cuánto dura GTA 6? Horas de historia y del 100 %")]),

    dict(dir="problemas", slug="psn-caido-inicio-sesion",
         h1="¿PSN caído en el lanzamiento de GTA 6? Qué se sabe de los problemas de inicio de sesión",
         desc="Miles de reportes de fallos de inicio de sesión y conexión en PSN el día del lanzamiento. Qué dicen las fuentes, qué no está confirmado y qué probar.",
         card="Hubo miles de reportes de fallos en PSN el día del lanzamiento. Sony no ha vinculado la causa con GTA 6.",
         chip=("warn", "Parcialmente confirmado"),
         answer="El día del lanzamiento hubo miles de reportes de problemas de inicio de sesión y de conexión en PlayStation Network. Sony no ha dicho cuál fue la causa ni la ha vinculado con GTA 6, y no hay confirmación de Rockstar ni de Microsoft.",
         body="""<h2>Lo que se sabe</h2>
<ul>
<li><strong>Reportes:</strong> el 19 de noviembre, Downdetector registró picos de miles de reportes. IBTimes y Digit dan cifras distintas, así que no damos un número.</li>
<li><strong>Síntomas:</strong> problemas de inicio de sesión y de conexión con los servidores. Según Digit, quien intentaba entrar veía un mensaje de «services are busy» (los servicios están ocupados).</li>
<li><strong>Estado de Sony:</strong> según Endgame Tools, la página de estado de Sony avisó de juegos y funciones sociales degradados en más de 60 países desde las 05:33 hasta las 06:04 UTC, y a las 11:40 UTC no mostraba incidencias.</li>
</ul>
<h2>Lo que no está confirmado</h2>
<p>La causa. Digit apunta a que podría deberse a la demanda de GTA 6, pero IBTimes dice que no hay evidencia que lo vincule. Sony no ha hecho declaraciones sobre ello en las fuentes que hemos revisado. Estas cifras y horas son del día del lanzamiento y la situación puede haber cambiado.</p>
<h2>Qué puedes probar</h2>
<p>Recomendaciones de la prensa, no oficiales: reinicia la consola, instala la actualización que pida el juego y espera un rato antes de reintentar. Mira antes la página de estado de PlayStation. Endgame Tools añade que en PS5 el juego puede estar esperando a una versión del software del sistema, la 26.07-14.23.00; es una sola fuente, compruébalo en tu consola.</p>
<p>Si el problema es que el juego no arranca, mira <a href="no-carga-errores.html">GTA 6 no carga o no arranca</a>.</p>""",
         sources=[("https://www.ibtimes.co.uk/gta-vi-launch-psn-login-connection-problems-1833330", "IBTimes UK: problemas de PSN el día del lanzamiento de GTA VI (19-11-2026)"),
                  ("https://www.digit.in/news/general/playstation-network-down-thousands-of-users-report-login-issues-amid-gta-6-launch.html", "Digit: PSN caído, miles de usuarios con problemas de inicio de sesión (19-11-2026)"),
                  ("https://endgametools.com/en/gta-6/news/gta-6-launch-day", "Endgame Tools: GTA 6 el día del lanzamiento, servidores, problemas conocidos y actualizaciones (19-11-2026)")],
         related=[("problemas/no-carga-errores.html", "GTA 6 no carga o no arranca: soluciones en PS5 y Xbox"), ("problemas/tamano-descarga.html", "¿Cuánto ocupa GTA 6 en PS5 y Xbox?"), ("novedades/actualizaciones-parches.html", "¿Hay parches de GTA 6? Qué se sabe de la actualización 1.002")]),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def crear(p, tpl):
    rel = f"{p['dir']}/{p['slug']}.html"
    url = f"https://6estrellas.org/{rel}"
    dest = ROOT / rel
    if dest.exists():
        print("ya existe:", rel)
        return False
    s = tpl
    s = re.sub(r"<title>.*?</title>", f"<title>{esc(p['h1'])}</title>", s, count=1, flags=re.S)
    s = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + esc(p["desc"]), s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + esc(p["h1"]), s, count=1)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + esc(p["desc"]), s, count=1)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, s, count=1)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + url, s, count=1)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"],
           "image": ["https://6estrellas.org/assets/og.png"], "datePublished": PUB, "dateModified": PUB, "inLanguage": "es",
           "author": {"@type": "Organization", "name": "Redacción 6 Estrellas", "url": "https://6estrellas.org/sobre.html"},
           "publisher": {"@type": "Organization", "name": "6 Estrellas", "url": "https://6estrellas.org/",
                         "logo": {"@type": "ImageObject", "url": "https://6estrellas.org/assets/logo-512.png", "width": 512, "height": 512}},
           "mainEntityOfPage": url}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://6estrellas.org/"},
        {"@type": "ListItem", "position": 2, "name": HUB[p["dir"]], "item": f"https://6estrellas.org/{p['dir']}/"},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}]}
    s, n = re.subn(r'<script type="application/ld\+json">.*?</script>\s*<script type="application/ld\+json">.*?</script>',
                   lambda m: jsonld(art) + "\n" + jsonld(bc), s, count=1, flags=re.S)
    assert n == 1
    crumbs = (f'<nav class="crumbs" aria-label="Migas de pan"><a href="../">Inicio</a> <span aria-hidden="true">›</span> '
              f'<a href="../{p["dir"]}/">{HUB[p["dir"]]}</a> <span aria-hidden="true">›</span> <span aria-current="page">{esc(p["h1"])}</span></nav>')
    s, n = re.subn(r'<nav class="crumbs".*?</nav>', lambda m: crumbs, s, count=1, flags=re.S)
    assert n == 1
    cls, chip = p["chip"]
    src = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{esc(t)}</a></li>' for u, t in p["sources"])
    article = f'''<article>
<h1>{esc(p["h1"])}</h1>
<p class="meta"><time datetime="2026-11-20">Revisado el 20 de noviembre de 2026</time><span>Por <a href="../sobre.html">Redacción 6 Estrellas</a></span><span class="chip {cls}">{chip}</span></p>
<div class="answer"><p class="answer-label">Respuesta corta</p><p>{p["answer"]}</p></div>
<div class="prose">
{p["body"]}
</div>
<section class="sources"><h2>Fuentes</h2><ul>{src}</ul>
<p class="small">Resumen redactado por 6 Estrellas a partir de las fuentes citadas, revisadas el 20 de noviembre de 2026. Si ves un error, cuéntanoslo desde <a href="../sobre.html">Quiénes somos</a>.</p></section>
</article>'''
    s, n = re.subn(r"<article>.*?</article>", lambda m: article, s, count=1, flags=re.S)
    assert n == 1
    rel_li = "".join(f'<li><a href="../{r}">{esc(t)}</a></li>' for r, t in p["related"])
    related = f'<section class="related" aria-labelledby="rel-t"><h2 id="rel-t">También te puede interesar</h2><ul>{rel_li}</ul></section>'
    s, n = re.subn(r'<section class="related".*?</section>', lambda m: related, s, count=1, flags=re.S)
    assert n == 1
    dest.write_text(s, encoding="utf-8", newline="")
    print("creada:", rel)
    return True


def enlazar(p):
    rel = f"{p['dir']}/{p['slug']}.html"
    # índice de sección
    idx = ROOT / p["dir"] / "index.html"
    t = idx.read_text(encoding="utf-8")
    if rel not in t:
        li = f'<li class="card"><a href="../{rel}"><span class="card-t">{esc(p["h1"])}</span><span class="card-d">{esc(p["card"])}</span></a></li>'
        t, n = re.subn(r'(<ul class="cards">.*?)(</ul>)', lambda m: m.group(1) + li + m.group(2), t, count=1, flags=re.S)
        assert n == 1
        idx.write_text(t, encoding="utf-8", newline="")
    # portada
    home = ROOT / "index.html"
    t = home.read_text(encoding="utf-8")
    if rel not in t:
        li = f'<li><a href="{rel}">{esc(p["h1"])}</a></li>'
        pat = rf'(<h2><a href="{p["dir"]}/">[^<]*</a></h2><p class="small">[^<]*</p><ul>.*?)(</ul>)'
        t, n = re.subn(pat, lambda m: m.group(1) + li + m.group(2), t, count=1, flags=re.S)
        assert n == 1
        home.write_text(t, encoding="utf-8", newline="")
    # sitemap
    sm = ROOT / "sitemap.xml"
    t = sm.read_text(encoding="utf-8")
    loc = f"https://6estrellas.org/{rel}"
    if loc not in t:
        t = t.replace("</urlset>", f"  <url><loc>{loc}</loc><lastmod>{PUB}</lastmod></url>\n</urlset>")
        sm.write_text(t, encoding="utf-8", newline="")


if __name__ == "__main__":
    tpl = (ROOT / "preguntas" / "cuanto-dura.html").read_text(encoding="utf-8")
    for p in PAGINAS:
        crear(p, tpl)
        enlazar(p)
    subprocess.run([sys.executable, "-I", str(ROOT / "herramientas" / "mantenimiento.py"), "indice"], check=True)
