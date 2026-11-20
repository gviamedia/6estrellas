#!/usr/bin/env python3
"""Actualización del 20/11/2026 (tarde) en las páginas en español, con lo publicado en los dos primeros días:
trucos (61 con requisitos y los 19 códigos conocidos), emisoras (22 + la secreta), atracos, misiones por capítulos
y página nueva de secretos. Idempotente: reescribe las secciones afectadas cada vez.
Uso: python herramientas/actualizar_20nov.py
"""
import html, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import trucos_datos
from paginas_lanzamiento import crear, HUB  # crea un artículo nuevo a partir de una plantilla existente

ROOT = pathlib.Path(__file__).resolve().parent.parent
FECHA = '<time datetime="2026-11-20">Revisado el 20 de noviembre de 2026</time>'


def leer(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def escribir(rel, s):
    (ROOT / rel).write_text(s, encoding="utf-8", newline="")
    print("ok", rel)


def articulo(rel, *, answer=None, body=None, sources=None, chip=None, title=None, h1=None, desc=None):
    s = leer(rel)
    s = re.sub(r'<time datetime="[^"]+">Revisado el [^<]+</time>', FECHA, s, count=1)
    if answer:
        s = re.sub(r'(<p class="answer-label">Respuesta corta</p><p>).*?(</p>)', lambda m: m.group(1) + answer + m.group(2), s, count=1, flags=re.S)
    if body is not None:
        s = re.sub(r'(<div class="prose">\n).*?(\n</div>\n<section class="sources">)', lambda m: m.group(1) + body + m.group(2), s, count=1, flags=re.S)
    if sources:
        li = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{html.escape(t)}</a></li>' for u, t in sources)
        s = re.sub(r'(<section class="sources"><h2>Fuentes</h2><ul>).*?(</ul>)', lambda m: m.group(1) + li + m.group(2), s, count=1, flags=re.S)
    if chip:
        s = re.sub(r'<span class="chip [a-z]+">[^<]*</span>', f'<span class="chip {chip[0]}">{chip[1]}</span>', s, count=1)
    if title:
        s = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>", s, count=1)
        s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + html.escape(h1 or title), s, count=1)
    if h1:
        s = re.sub(r"<h1>.*?</h1>", f"<h1>{html.escape(h1)}</h1>", s, count=1)
        s = re.sub(r'(<span aria-current="page">)[^<]*(</span></nav>)', lambda m: m.group(1) + html.escape(h1) + m.group(2), s, count=1)
        s = re.sub(r'("@type": "Article", "headline": ")[^"]*', lambda m: m.group(1) + h1.replace('"', '\\"'), s, count=1)
        s = re.sub(r'("position": 3, "name": ")[^"]*', lambda m: m.group(1) + h1.replace('"', '\\"'), s, count=1)
    if desc:
        s = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + html.escape(desc), s, count=1)
        s = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + html.escape(desc), s, count=1)
        s = re.sub(r'("@type": "Article", "headline": "[^"]*", "description": ")[^"]*', lambda m: m.group(1) + desc.replace('"', '\\"'), s, count=1)
    escribir(rel, s)


# ---------------------------------------------------------------- trucos
TRUCOS_BODY = f"""<p>Es el gran cambio respecto a otros GTA: los trucos no están disponibles desde el principio. PowerPyx, Red Bull y Vandal coinciden en que se desbloquean al completar la historia principal y en que cada uno exige además un requisito propio, que puedes consultar en el menú Progreso, apartado Trucos. Si introduces un código antes de desbloquearlo, no pasa nada.</p>
<p>Según Red Bull, el juego tiene en cuenta lo que ya hayas hecho durante la historia, así que algunos trucos pueden estar listos nada más ver los créditos. Merece la pena ir cumpliendo los requisitos mientras juegas.</p>
<h2>Cómo se introducen</h2>
<ol>
<li>Saca el teléfono con la cruceta hacia arriba.</li>
<li>Mantén L1 y pulsa R1 (en Xbox, mantén LB y pulsa RB).</li>
<li>Introduce la secuencia del truco con la cruceta.</li>
</ol>
<p>Los códigos solo usan la cruceta, así que son iguales en PS5 y Xbox. Algunos se parecen mucho (los de munición empiezan igual, y los de vehículos comienzan por ← ↑ → ↓): un fallo y obtienes otro truco o ninguno.</p>
<h2>Qué pierdes al usarlos</h2>
<ul>
<li>Se desactivan los trofeos o logros.</li>
<li>Se desactiva el guardado hasta que salgas y recargues la partida (ver <a href="guardar-partida.html">cómo guardar</a>). Guarda antes de usarlos.</li>
</ul>
<h2>Los 61 trucos y cómo se desbloquea cada uno</h2>
<p>Hay 10 de personaje, 11 de combate, 21 de vehículos, 3 de entorno y 16 filtros de pantalla. Las tres guías coinciden en los requisitos; a 20 de noviembre se conocen {trucos_datos.CONOCIDOS} códigos. Salvo que se indique, el código aparece en las tres. Los marcados como «Sin descubrir» ya tienen requisito oficial, pero nadie ha publicado aún su secuencia.</p>
{trucos_datos.tablas("es")}
<h2>Cuidado con las listas falsas</h2>
<ul>
<li><strong>No hay trucos por número de teléfono.</strong> Según Red Bull, las listas de «números de trucos de GTA 6» son los de GTA V con otra etiqueta: en GTA 6 no funcionan.</li>
<li><strong>Las combinaciones de las cajas fuertes no son trucos ni son fijas.</strong> Según GameSpot, cambian en cada partida, e incluso si robas la misma tienda dos veces; las listas de «códigos de cajas fuertes» no sirven. Mira cómo encontrarlas en <a href="../dinero/ganar-dinero.html">cómo ganar dinero</a>.</li>
</ul>
<p>Iremos añadiendo los códigos que falten cuando aparezcan en fuentes fiables.</p>"""

articulo("preguntas/trucos.html",
         answer=f"Sí, 61, con los mismos códigos en PS5 y Xbox. Solo funcionan después de terminar la historia y de cumplir el requisito de cada uno. A 20 de noviembre se conocen {trucos_datos.CONOCIDOS} códigos; abajo tienes los 61 trucos con su requisito.",
         body=TRUCOS_BODY, chip=("warn", "Parcialmente confirmado"),
         title="Trucos de GTA 6 para PS5 y Xbox: códigos y cómo desbloquearlos",
         desc=f"Los 61 trucos de GTA 6 con su requisito de desbloqueo y los {trucos_datos.CONOCIDOS} códigos ya conocidos para PS5 y Xbox: dinero, munición infinita, blindaje y más.",
         sources=[("https://www.powerpyx.com/gta-6-all-cheats/", "PowerPyx: todos los trucos de GTA 6 (18-11-2026)"),
                  ("https://www.redbull.com/int-en/gta-6-cheat-codes", "Red Bull: trucos de GTA 6 y cómo desbloquearlos (18-11-2026)"),
                  ("https://vandal.elespanol.com/guias/guia-grand-theft-auto-vi-trucos-consejos-y-secretos/trucos", "Vandal: trucos de GTA 6 (20-11-2026)"),
                  ("https://www.gamespot.com/articles/gta-6-safe-codes-and-robberies-guide/", "GameSpot: atracos y códigos de cajas fuertes (18-11-2026)")])

# ---------------------------------------------------------------- emisoras
EMISORAS = [
    ("Flash FM", "Pop", "Robyn y Alex Consani", True),
    ("Emotion 98.3", "Soft rock (vuelve del Vice City de 2002)", "—", False),
    ("Vice City FM", "Pop de los 80", "«Weird Al» Yankovic y Brigitte Nielsen", False),
    ("Stockyard FM", "Indie y dance", "PinkPantheress y The Dare", False),
    ("Dirty South Classics", "Rap del sur", "Trick Daddy y Trina", True),
    ("VCRR", "Rap actual", "JT y DJ Stevie J", False),
    ("Honey FM", "R&amp;B y soul de los 90", "Chilli y T-Boz", False),
    ("Cocoteo FM", "Música latina actual: reguetón, dembow, bachata", "Bad Bunny (El Martillo) y RaiNao (La Gata)", True),
    ("Radio La Ola", "Clásicos latinos", "Gloria y Emilio Estefan", False),
    ("Radio On-U", "Rock tranquilo", "—", False),
    ("V-Rock", "Rock clásico", "Lindsey Buckingham y Michael McDonald", False),
    ("The Chamber 106.6", "Metal", "Kerry King y Tom Araya", True),
    ("Back Country Radio", "Country", "Morgan Wallen (MW) y Delta Dawne", True),
    ("Gloriana Blues Radio", "Blues", "Keith Richards y Buddy Guy", False),
    ("Leonida Jazz Radio", "Jazz fusión de los 70", "—", False),
    ("Symphony FM", "Música clásica", "Yuja Wang", False),
    ("Worldwide FM", "Músicas del mundo y jazz (vuelve de GTA V)", "Gilles Peterson", False),
    ("CircoLoco Records Radio", "Música de club", "Seth Troxler y Antonio Carbonaro", False),
    ("AfroBank FM", "Música africana", "Burna Boy y Palms Trax", True),
    ("Kaleidoscope FM", "Versiones, pop global, disco finlandés", "Jeremy Irons", False),
    ("WKTT", "Tertulia (vuelve de GTA IV)", "Stavros Halkias", False),
    ("The Wipe", "Tertulia sobre lo raro de Leonida", "—", False),
]
filas = "".join(f'<tr><td>{n}{" ★" if o else ""}</td><td>{g}</td><td>{h}</td></tr>' for n, g, h, o in EMISORAS)
RADIO_BODY = f"""<h2>Las 22 emisoras</h2>
<p>GameSpot, que las ha ido escuchando en el juego desde el lanzamiento, cuenta 22 emisoras, la cifra más alta de la saga, más una secreta. Las marcadas con ★ son las seis que Rockstar presentó oficialmente el 8 de octubre de 2026; el resto procede de GameSpot, así que es una sola fuente.</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Tabla (desliza para ver más)"><table><thead><tr><th>Emisora</th><th>Estilo</th><th>Presentan (según GameSpot)</th></tr></thead><tbody>{filas}</tbody></table></div>
<h2>La emisora secreta: The Vault Radio</h2>
<p>Según GameSpot, se desbloquea al llegar a Vice City: ve a la discoteca The Vault, más o menos en el centro de la ciudad, busca dentro un póster con una máscara de gas rosa y escanéalo con el teléfono. A partir de ahí podrás escuchar la música dance y electrónica del club.</p>
<h2>Lo que anunció Rockstar</h2>
<p>En su presentación del 8 de octubre, Rockstar detalló seis emisoras con sus locutores y anunció que GTA 6 incluye por primera vez pódcasts a la carta, que se escuchan en el coche o a pie con auriculares conectados al teléfono, y un disco oficial, <em>Grand Theft Auto VI: The Album</em>, con 34 temas.</p>
<p>La base de datos de GTABase llegó a listar 21 emisoras antes del lanzamiento, pero sin separar las confirmadas de las filtradas; la lista de GameSpot ya sale del juego publicado.</p>"""
articulo("lugares/emisoras-radio.html",
         answer="GameSpot cuenta 22 emisoras escuchándolas en el juego, más una secreta, The Vault Radio. Rockstar presentó oficialmente seis: Flash FM, Cocoteo FM, Back Country Radio, AfroBank FM, The Chamber 106.6 y Dirty South Classics.",
         body=RADIO_BODY, chip=("warn", "Parcialmente confirmado"),
         title="Emisoras de radio de GTA 6: las 22 y la secreta The Vault",
         h1="¿Qué emisoras de radio tiene GTA 6? Las 22 y la secreta",
         desc="GTA 6 tiene 22 emisoras de radio, según GameSpot, más la secreta The Vault Radio. Estilos, locutores y cómo desbloquear la emisora oculta.",
         sources=[("https://www.gamespot.com/articles/all-gta-6-radio-stations-and-songs/", "GameSpot: todas las emisoras y canciones de GTA 6 (19-11-2026)"),
                  ("https://www.rockstargames.com/newswire/article/o3982oa93a23k4/the-music-of-grand-theft-auto-vi-in-game-radio-stations", "Rockstar Newswire: la música de GTA VI (08-10-2026)"),
                  ("https://www.gtabase.com/gta-6/radio-stations/", "GTABase: emisoras de radio de GTA 6")])

# ---------------------------------------------------------------- ganar dinero: atracos
s = leer("dinero/ganar-dinero.html")
ATRACOS = """<h2>Cómo atracar sin que salte la alarma</h2>
<p>Consejos de la guía de atracos de GameSpot:</p>
<ul>
<li><strong>Mira el mapa antes:</strong> cada negocio tiene un nivel de seguridad bajo, medio o alto. Casi todos tienen un empleado, una alarma y cámaras.</li>
<li><strong>Primero, el público; después, la alarma:</strong> romper vitrinas o puertas la dispara. Se apaga en un panel blanco, normalmente en la trastienda; el modo concentración (pulsar los dos sticks) lo resalta.</li>
<li><strong>Cámaras:</strong> si te graban, busca la sala de seguridad y destruye la grabación, o la policía os identificará al salir. También puedes dispararles antes, mejor con silenciador.</li>
<li><strong>Entra por detrás:</strong> la ganzúa automática (Snap Gun), que llega con la historia, abre cerraduras sin que salte la alarma. El mapa, dentro de un edificio, muestra las puertas traseras.</li>
<li><strong>Cajas fuertes:</strong> el código es aleatorio y cambia en cada atraco; búscalo en un guardia o por la zona. Las pequeñas se pueden forzar.</li>
<li><strong>Bancos y casas de préstamos:</strong> dan billetes marcados que hay que vender a un perista, y llevan bolsas de tinta que estallan si te alejas demasiado, salvo que tengas un inhibidor.</li>
<li><strong>Mejor en pareja:</strong> en los negocios grandes, el personaje que no controlas se ocupa del público.</li>
</ul>
"""
s = re.sub(r'<h2>Cómo atracar sin que salte la alarma</h2>.*?</ul>\n', "", s, flags=re.S)
s = s.replace("<h2>Otras opciones</h2>", ATRACOS + "<h2>Otras opciones</h2>", 1)
s = re.sub(r'<time datetime="[^"]+">Revisado el [^<]+</time>', FECHA, s, count=1)
if "gta-6-safe-codes-and-robberies-guide" not in s:
    s = s.replace('</a></li></ul>\n<p class="small">Resumen redactado',
                  '</a></li><li><a href="https://www.gamespot.com/articles/gta-6-safe-codes-and-robberies-guide/" rel="noopener" target="_blank">GameSpot: atracos y códigos de cajas fuertes (18-11-2026)</a></li></ul>\n<p class="small">Resumen redactado', 1)
escribir("dinero/ganar-dinero.html", s)

# ---------------------------------------------------------------- misiones: todos los capítulos
CAPS = [
    ("2", "Paradise Lost", ["What's in the Bag?", "Ambulance Chaser", "Play Nurse", "Overnight Charges", "Just Moved In", "Girls' Trip (opcional)", "Moses", "New Look", "How Do I Look?", "Got Pills?", "Daily Driver", "Behind on Payments", "Slam Dunk", "Breakfast Run", "Coffee Break (opcional)", "Prepare for Vice City", "Afternoon Delight", "Checking Out"]),
    ("3", "Tits Ass Drug Money", ["Welcome to Vice City", "Dealer's Choice", "Meet the Heders", "Dubious Provenance", "Mami Knows Best (opcional)", "South Leonida Real Estate", "Tyrone", "Here, Kitty Kitty", "Send Money to Lorena", "Encrypted Hard Drive", "Car Service", "Send More Money to Lorena", "Top Billing", "Boobie Time (opcional)", "First Impressions", "Caught Slipping", "Crosstown Traffic", "Credit Check", "Steal the Zorrusso for Randy", "Raul's Next Job (opcional, perdible)", "Sinfrontera National Bank", "Security Expert", "Heist Planning", "Ride or Die", "Company Property", "The Missing Link", "Safe Word", "Cooties", "Bricked Up", "Hidden Charges", "The Cartel Heist"]),
    ("4", "Vice City, Baby", ["Ocean Beach", "Another Life", "Pool Day", "Company Cars", "Lawyer Up", "It's a Date!", "Party Hard", "Heavy Lifting", "Pay Abe's Fee", "Photo/Shoot (opcional)", "Making Gainz", "Blood Sweat and Gear", "Watch It", "Call Nate", "Cash Injections", "Amateur Hour", "Dirty Work", "Nate Will Be in Touch", "Too Much Baggage", "Adventures in Babysitting", "Rafa", "Fresh Evidence", "Power Play", "Child's Play (opcional, perdible)", "Headliners", "Close Surveillance", "Delivery Method", "Team Building", "Fully Catered", "Heist Plans in Place", "VCIA Takedown", "Tie Up Loose Ends (opcional)", "Call Valentina Back", "Sunset", "Starting From Zero"]),
    ("5", "Top of the World, Ma", ["Bird in the Hand", "Taking Liberties", "VC Baby", "Doggie Bag", "Operation Savage Glory", "Honest Abe", "Unfinished Business", "Pay Abe's Fee", "Protective Custody", "The End of the Road"]),
]


def caps_html(lang):
    es = lang == "es"
    out = []
    for n, nombre, ms in CAPS:
        items = "".join(f"<li>{html.escape(m if es else m.replace('(opcional, perdible)', '(optional, missable)').replace('(opcional)', '(optional)'))}</li>" for m in ms)
        out.append(f'<details><summary>{"Capítulo" if es else "Chapter"} {n}: {html.escape(nombre)} ({len(ms)} {"misiones" if es else "missions"})</summary><ol>{items}</ol></details>')
    return "\n".join(out)


s = leer("preguntas/misiones-capitulo-1.html")
s = re.sub(r'<h2>Capítulos 2 a 5</h2>.*?(?=\n</div>\n<section class="sources">)',
           '<h2>Capítulos 2 a 5</h2>\n<p class="note">Contiene títulos de misiones de capítulos posteriores. Despliega cada capítulo solo si quieres verlos.</p>\n'
           '<p>Lista de GTABase, que pone nombre a cada capítulo y marca como perdibles otras dos misiones opcionales: «Raul\'s Next Job» (capítulo 3) y «Child\'s Play» (capítulo 4). Los títulos están en inglés; en la versión en español pueden cambiar.</p>\n'
           + caps_html("es"), s, count=1, flags=re.S)
escribir("preguntas/misiones-capitulo-1.html", s)
articulo("preguntas/misiones-capitulo-1.html",
         answer="La historia tiene un Prólogo y cinco capítulos. GTABase numera 122 misiones contando las opcionales; 27 son del Capítulo 1, entre ellas «Día de pesca» y «¡Oye, Arnold!». Cuatro misiones opcionales se pueden perder: dos del Capítulo 1, una del 3 y otra del 4.",
         title="Misiones de GTA 6: lista por capítulos y cuáles se pueden perder",
         h1="¿Cuáles son las misiones de GTA 6? Lista por capítulos y perdibles",
         desc="Las misiones de GTA 6 capítulo a capítulo según GTABase, con las cuatro opcionales que se pueden perder. Los capítulos 2 a 5 van plegados para evitar spoilers.")

# ---------------------------------------------------------------- página nueva: secretos
SECRETOS_BODY = """<p>Rockstar no confirma secretos, así que todo lo que sigue procede de prensa que lo ha comprobado o de vídeos de jugadores recogidos por ella. Cuando solo lo cuenta una fuente, lo decimos.</p>
<h2>Abducción alienígena (con trofeo)</h2>
<p>Según GameSpot, que detalla los pasos, y The Tab:</p>
<ol>
<li>Termina el Capítulo 1.</li>
<li>Ve, solo y después de las 2:00 de la madrugada del juego, al noroeste del Starlet Motel, en el condado de Kelly (cerca de Port Gellhorn).</li>
<li>Busca un coche parado con las luces parpadeando: apunta a un sendero que entra en el bosque, donde verás una luz azul.</li>
<li>Ofrécete a ayudar a la mujer a la que están abduciendo y recupera su coche. Entonces te abducen a ti.</li>
</ol>
<p>Desbloquea el trofeo o logro «The truth is out there».</p>
<h2>La continuación: la base secreta</h2>
<p>Según GameSpot, tiempo después el personaje abducido tiene un sueño en el que aparecen las pistas de una misión de rescate en South Point Airfield, en Hamlet: hay que entrar en el edificio de la torre de radio por el tejado y usar un teclado. GameSpot dice que el código «suele ser» 2134 y que se ve en el sueño; otras webs dan otra combinación, así que fíjate en el sueño de tu partida. Dentro hay radiación y gas tóxico, así que conviene ir rápido.</p>
<h2>Un huevo de Pascua de verdad</h2>
<p>En lo alto de la torre más alta de Vice City hay un nido. Según GameSpot y GamingBible, el jugador que lo encontró tardó unos siete minutos en subir; arriba puedes coger un huevo y lanzarlo, y lo que pasa después no lo destripamos. GamingBible lo sitúa en una torre de comunicaciones, así que la ubicación exacta varía según quién lo cuente.</p>
<h2>Bigfoot</h2>
<p>GameSpot lo sitúa en Gullet Marsh y dice que está ligado a una misión, así que es difícil perdérselo. The Tab habla de los humedales al sur de Hamlet.</p>
<h2>El apartamento de Dexter Morgan</h2>
<p>Está en Washington Island, en Vice City, cerca de la tienda Top Fun Drones de Vice Beach, según GameSpot. No se puede entrar. Algunos jugadores creen que el barco amarrado al lado se parece al Slice of Life de la serie.</p>
<h2>Guiños a Red Dead y a Liberty City</h2>
<ul>
<li>Una novela del oeste sobre un vaquero de New Austin, la región de Red Dead Redemption; GameSpot la vio en Jacob's Tavern, en Millport.</li>
<li>En la mesa de la casa de Jason, al principio del Capítulo 1, hay unas memorias de un antiguo mafioso de Liberty City que aluden a 2008, el año de GTA IV.</li>
</ul>
<p>En el juego se pueden leer fragmentos de libros y revistas.</p>
<h2>La emisora secreta</h2>
<p>The Vault Radio se desbloquea escaneando un póster en la discoteca The Vault de Vice City. Está explicado en <a href="../lugares/emisoras-radio.html">las emisoras de GTA 6</a>.</p>
<h2>Sin confirmar</h2>
<ul>
<li><strong>Un perro socorrista:</strong> un perro con gafas de sol en moto de agua que rescata a nadadores, en Partridge Bay y Gambit Bay según Playday. GameSpot también se ha hecho eco del perro.</li>
<li><strong>El barco de Michael:</strong> algunos jugadores creen que un barco aparcado junto a la casa de Jason es el de Michael en GTA V, según Game Rant. Rockstar no lo ha confirmado.</li>
</ul>
<p>Esta página está viva: la ampliaremos a medida que aparezcan más secretos con fuente.</p>"""

SECRETOS = dict(dir="preguntas", slug="secretos-easter-eggs",
    h1="¿Qué secretos y easter eggs tiene GTA 6? Los encontrados hasta ahora",
    desc="Los secretos de GTA 6 encontrados en los primeros días: la abducción alienígena con trofeo, el huevo en lo alto de Vice City, Bigfoot, el piso de Dexter y más.",
    chip=("warn", "Parcialmente confirmado"),
    answer="En los dos primeros días se han encontrado, entre otros, una abducción alienígena con su propio trofeo, un huevo de Pascua en lo alto de la torre más alta de Vice City, Bigfoot, el apartamento de Dexter Morgan y guiños a Red Dead Redemption. Rockstar no confirma secretos: todo procede de prensa y de jugadores.",
    body=SECRETOS_BODY,
    sources=[("https://www.gamespot.com/articles/gta-6-has-aliens-and-heres-how-to-find-them/", "GameSpot: GTA 6 tiene alienígenas y cómo encontrarlos (20-11-2026)"),
             ("https://www.gamespot.com/articles/gta-6-easter-eggs-list-and-locations/", "GameSpot: easter eggs de GTA 6 y dónde encontrarlos (18-11-2026)"),
             ("https://www.gamingbible.com/news/gta-6-secret-cutscene-seven-minute-tower-easter-egg-795530-20261119", "GamingBible: la escena secreta tras subir una torre (19-11-2026)"),
             ("https://thetab.com/2026/11/20/bigfoot-and-ufos-all-the-weird-and-wonderful-things-people-are-stumbling-upon-in-gta-6", "The Tab: Bigfoot, ovnis y otras rarezas de GTA 6 (20-11-2026)"),
             ("https://gamerant.com/grand-theft-auto-6-gta-5-easter-egg-michael-boat/", "Game Rant: ¿el barco de Michael de GTA V?"),
             ("https://playday.one/2026/11/19/gta-6-cool-dog-easter-egg/", "Playday: el perro de la moto de agua (19-11-2026)")],
    related=[("preguntas/trucos.html", "¿Hay trucos en GTA 6? Cómo se desbloquean"),
             ("lugares/mapa-leonida.html", "¿Cómo es el mapa de GTA 6? Las zonas de Leonida"),
             ("lugares/emisoras-radio.html", "¿Qué emisoras de radio tiene GTA 6?")])

nuevo = "preguntas/secretos-easter-eggs.html"
if not (ROOT / nuevo).exists():
    import paginas_lanzamiento
    paginas_lanzamiento.PUB = "2026-11-20T18:00:00+01:00"
    crear(SECRETOS, leer("preguntas/trucos.html"))
# índice de Preguntas (la portada la regenera rediseno.py)
idx = leer("preguntas/index.html")
if nuevo.split("/")[1] not in idx:
    li = f'<li class="item"><a href="../{nuevo}"><span class="item-t">{html.escape(SECRETOS["h1"])}</span><span class="item-d">{html.escape(SECRETOS["desc"])}</span></a></li>'
    idx = re.sub(r'(<ul class="list">.*?)(</ul>)', lambda m: m.group(1) + li + m.group(2), idx, count=1, flags=re.S)
    escribir("preguntas/index.html", idx)
# Títulos de las tarjetas que cambian
idx = leer("preguntas/index.html")
idx = idx.replace("¿Cuáles son las misiones del Capítulo 1 de GTA 6? Lista y cuáles se pueden perder", "¿Cuáles son las misiones de GTA 6? Lista por capítulos y perdibles")
escribir("preguntas/index.html", idx)
sm = leer("sitemap.xml")
loc = f"https://6estrellas.org/{nuevo}"
if loc not in sm:
    sm = sm.replace("  <url><loc>https://6estrellas.org/en/", f"  <url><loc>{loc}</loc><lastmod>2026-11-20T18:00:00+01:00</lastmod></url>\n  <url><loc>https://6estrellas.org/en/", 1)
    escribir("sitemap.xml", sm)
