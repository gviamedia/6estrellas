#!/usr/bin/env python3
"""SEO del 20/11/2026 (páginas en español): títulos alineados con las búsquedas reales (Google Trends y
autocompletado) y páginas nuevas para las búsquedas sin cubrir. Idempotente.
Uso: python herramientas/actualizar_seo.py
"""
import html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from actualizar_20nov import articulo, leer, escribir  # noqa: E402 (reutiliza las utilidades; también reaplica la tanda anterior)
import paginas_lanzamiento
from paginas_lanzamiento import crear

ROOT = pathlib.Path(__file__).resolve().parent.parent
paginas_lanzamiento.PUB = "2026-11-20T20:00:00+01:00"
CREDITOS = ("https://www.rockstargames.com/VI/credits", "Rockstar Games: créditos oficiales de GTA VI")

# Reparto principal según los créditos oficiales de Rockstar (rockstargames.com/VI/credits).
REPARTO = [("Jason Duval", "Dylan Rourke"), ("Lucia Caminos", "Manni L. Perez"), ("Cal Hampton", "Bobby Moynihan"),
           ("Brian Heder", "Stephen Root"), ("Lori Heder", "Orlagh Cassidy"), ("Donnie", "Brad Carter"), ("Mandy", "Lexie Shoaibi"),
           ("Boobie Ike", "Mike Forbs"), ("Dre'Quan", "Naiqui Macabroad"), ("Raul Bautista", "Manny Perez"),
           ("Mia Caminos", "Roselyn Sanchez"), ("Bret Vogel", "Jariko Denman"), ("Moses «Mo» Watkins", "Aaron Morton"),
           ("Randy Kozlov", "Serge Didenko"), ("Pilot Pete", "Carl Palmer"), ("Vicki", "Taryn Manning"),
           ("Kordell Grant", "Michael Jai White"), ("DWNPLY", "Denzel Curry"), ("Arnold", "Caesar Samayoa"),
           ("Shirley Baker", "Carolee Carmello"), ("The Hitman", "Michael Hollick")]


def tabla_reparto(es=True):
    def nombre(p):
        return p if es else p.replace("«", "“").replace("»", "”")
    filas = "".join(f"<tr><td>{html.escape(nombre(p))}</td><td>{html.escape(a)}</td></tr>" for p, a in REPARTO)
    cab = ("Personaje", "Actor o actriz") if es else ("Character", "Actor")
    return (f'<div class="table-wrap" tabindex="0" role="region" aria-label="{"Tabla (desliza para ver más)" if es else "Table (scroll for more)"}">'
            f'<table><thead><tr><th>{cab[0]}</th><th>{cab[1]}</th></tr></thead><tbody>{filas}</tbody></table></div>')


NUEVAS = [
 dict(dir="lugares", slug="personajes-actores",
  h1="¿Quién pone voz a Jason y Lucia? Actores y personajes de GTA 6",
  desc="Los actores de GTA 6 según los créditos oficiales: Dylan Rourke es Jason, Manni L. Perez es Lucia y Lexie Shoaibi es Mandy. Y qué pasa con Niko Bellic.",
  chip=("ok", "Según las fuentes citadas"),
  answer="Según los créditos oficiales de Rockstar, Jason Duval es Dylan Rourke y Lucia Caminos es Manni L. Perez. En el reparto también están Stephen Root (Brian Heder), Bobby Moynihan (Cal) y Lexie Shoaibi (Mandy). Michael Hollick, el actor de Niko Bellic en GTA IV, aparece como «The Hitman».",
  body=f"""<p>Rockstar publicó los créditos completos de GTA 6 en su web oficial el día del lanzamiento. Las voces y las capturas de movimiento son de los mismos intérpretes, según Screen Rant.</p>
<h2>Jason y Lucia</h2>
<ul>
<li><strong>Jason Duval: Dylan Rourke.</strong> Según Screen Rant, es su primer videojuego; se le ha visto en series como <em>Station 19</em>, <em>Modern Family</em> o <em>9-1-1: Lone Star</em>.</li>
<li><strong>Lucia Caminos: Manni L. Perez.</strong> No es su debut en la saga: según Screen Rant, ya salió como clienta de discoteca en GTA V y GTA Online, y ha aparecido en <em>The Blacklist</em>, <em>Jessica Jones</em> o <em>Chicago P.D.</em></li>
</ul>
<p>Quiénes son en la historia: <a href="protagonistas.html">Jason y Lucia, los protagonistas</a>.</p>
<h2>Reparto principal</h2>
<p>Una selección de los créditos oficiales, con los personajes que aparecen en esta web:</p>
{tabla_reparto(True)}
<p>Los créditos incluyen también cameos de músicos como Kodak Black, que se interpreta a sí mismo.</p>
<h2>¿Sale Niko Bellic en GTA 6?</h2>
<p>No hay confirmación. Lo que sí hay: los créditos oficiales incluyen a <strong>Michael Hollick</strong>, el actor que dio vida a Niko Bellic en GTA IV, con el papel de «The Hitman» (el sicario). Rockstar no dice que ese personaje sea Niko, así que no lo damos por hecho. GameSpot, por su parte, ha encontrado en el juego unas memorias de un antiguo mafioso de Liberty City que aluden a 2008, el año de GTA IV.</p>
<h2>¿Y Mandy?</h2>
<p>La pone voz Lexie Shoaibi. Quién es y si se puede tener algo con ella: <a href="../preguntas/mandy.html">Mandy en GTA 6</a>.</p>""",
  sources=[CREDITOS, ("https://screenrant.com/gta-6-cast-voice-actors/", "Screen Rant: el reparto completo de GTA 6 (19-11-2026)"),
           ("https://www.gamespot.com/articles/gta-6-easter-eggs-list-and-locations/", "GameSpot: easter eggs de GTA 6 (18-11-2026)")],
  related=[("lugares/protagonistas.html", "¿Quiénes son Jason y Lucia, los protagonistas de GTA 6?"),
           ("preguntas/mandy.html", "¿Quién es Mandy en GTA 6? ¿Se puede ligar con ella?"),
           ("preguntas/finales-decisiones.html", "¿GTA 6 tiene varios finales? Decisiones que importan")]),
 dict(dir="preguntas", slug="mandy",
  h1="¿Quién es Mandy en GTA 6? ¿Se puede ligar con ella?",
  desc="Mandy es la inquilina de Brian en Key Lento que Jason conoce en la misión Pipework. No se puede tener una relación con ella. Quién la interpreta y qué se sabe.",
  chip=("ok", "Según las fuentes citadas"),
  answer="Mandy es una de las inquilinas de Brian Heder en Key Lento: Jason la conoce en «Pipework», una misión del Capítulo 1 en la que va a cobrarle el alquiler. Coquetea con Jason, pero no se puede tener una relación con ella. La interpreta Lexie Shoaibi.",
  body="""<h2>Quién es</h2>
<p>Es una de las inquilinas de Brian Heder en Key Lento, en los Leonida Keys. Jason la conoce en «Pipework», una misión del Capítulo 1 en la que Brian le manda cobrar alquileres atrasados y acaba arreglándole las tuberías, según GTABase y GameSpot. En los créditos oficiales la interpreta Lexie Shoaibi.</p>
<h2>¿Se puede tener una relación con ella?</h2>
<p>No. Según GameSpot, Mandy flirtea con Jason durante toda la misión, pero el diálogo nunca permite llevar la conversación hacia lo romántico y, al final, Jason se va sin que el jugador pueda decidir otra cosa. Puedes volver a pasar por su casa más adelante y retomar la situación, pero eso no la convierte en una opción romántica.</p>
<p>La única relación del juego es la de Jason y Lucia, y Rockstar ha dicho que es opcional: si quieres que funcione, tienes que cuidarla. Más en <a href="finales-decisiones.html">finales y decisiones</a>.</p>
<h2>¿Es una asesina en serie?</h2>
<p>Es una teoría de los jugadores, que se fijan en objetos de su casa y de su coche. No está confirmada. GameSpot menciona que en la misión Jason saca de las tuberías un objeto «curioso», pero no hay más.</p>""",
  sources=[("https://www.gamespot.com/articles/can-you-romance-mandy-in-gta-6/", "GameSpot: ¿se puede tener una relación con Mandy en GTA 6? (18-11-2026)"),
           ("https://www.gtabase.com/gta-6/missions/", "GTABase: lista de misiones (Pipework)"),
           CREDITOS,
           ("https://www.techradar.com/gaming/rockstar-says-if-you-want-gta-6s-romance-between-jason-and-lucia-to-flourish-you-have-to-nurture-it-but-its-completely-optional-its-not-something-that-we-want-to-foist-upon-players", "TechRadar: Rockstar dice que la relación de Jason y Lucia es opcional"),
           ("https://beebom.com/gta-6-mandy-serial-killer/", "Beebom: la teoría de que Mandy es una asesina")],
  related=[("lugares/personajes-actores.html", "¿Quién pone voz a Jason y Lucia? Actores y personajes de GTA 6"),
           ("preguntas/arreglos-casa-jason.html", "Cómo arreglar la barandilla y la casa de Jason en GTA 6"),
           ("preguntas/finales-decisiones.html", "¿GTA 6 tiene varios finales? Decisiones que importan")]),
 dict(dir="preguntas", slug="arreglos-casa-jason",
  h1="Cómo arreglar la barandilla y la casa de Jason en GTA 6",
  desc="Los cuatro arreglos de la casa de Jason en GTA 6 (escalones, tejado, barandilla y pared), dónde están y por qué hay que hacerlos antes de recoger a Lucia.",
  chip=("ok", "Según las fuentes citadas"),
  answer="Hay cuatro arreglos en la casa de Jason en Key Lento: los escalones, el tejado, la barandilla y la pared del dormitorio. Hazlos antes de recoger a Lucia: después ya no se pueden completar. La barandilla está detrás de la casa, junto al gimnasio al aire libre.",
  body="""<p>Al principio de la historia, Jason vive en una casa junto al agua en Key Lento que le deja Brian Heder. Está a medio hacer, y tienes un tiempo limitado para arreglarla antes de que Lucia salga y se mude, según GameSpot. Si los terminas, Lucia estará más contenta y la relación sale reforzada.</p>
<h2>Los cuatro arreglos</h2>
<ol>
<li><strong>Escalones:</strong> junto a las escaleras más cercanas al buzón y la entrada de coches hay unos tablones; interactúa con ellos (Triángulo / Y).</li>
<li><strong>Tejado con goteras:</strong> sube por la escalera amarilla del porche delantero e interactúa con las tejas.</li>
<li><strong>Barandilla:</strong> es la más difícil de encontrar. Sal por la puerta de atrás y baja al gimnasio al aire libre; mirando hacia la casa, verás un hueco en la barandilla junto a una escalera. Interactúa con el hueco.</li>
<li><strong>Pared:</strong> en el dormitorio, la pared de enfrente de la cama está a medio hacer. Interactúa con el armazón de madera: Jason pone placas de yeso y la pinta, y tú eliges el color.</li>
</ol>
<p class="note">Importante: cuando decidas ir a recoger a Lucia, ya no podrás volver a estos arreglos.</p>
<h2>Otras tareas antes de que llegue Lucia</h2>
<p>GTABase y GameSpot citan más tareas opcionales del Capítulo 1: hacer la compra, comprar flores, comprarle un collar a Lucia, recoger su ropa en casa de su amiga Andy y cortarte el pelo. Push Square añade que la reacción de Lucia cambia según hayas preparado la casa a tiempo o no.</p>
<p>Si quieres asegurarte, guarda en otra ranura antes: <a href="guardar-partida.html">cómo guardar la partida</a>. Lista de misiones en <a href="misiones-capitulo-1.html">las misiones de GTA 6</a>.</p>""",
  sources=[("https://www.gamespot.com/articles/how-to-fix-all-projects-at-jasons-house-in-gta-6/", "GameSpot: cómo hacer todos los arreglos de la casa de Jason (18-11-2026)"),
           ("https://www.gtabase.com/gta-6/missions/", "GTABase: misiones del Capítulo 1 (Feng Shui y tareas opcionales)"),
           ("https://www.pushsquare.com/reviews/ps5/grand-theft-auto-6", "Push Square: análisis de GTA 6")],
  related=[("preguntas/misiones-capitulo-1.html", "¿Cuáles son las misiones de GTA 6? Lista por capítulos y perdibles"),
           ("preguntas/mandy.html", "¿Quién es Mandy en GTA 6? ¿Se puede ligar con ella?"),
           ("preguntas/finales-decisiones.html", "¿GTA 6 tiene varios finales? Decisiones que importan")]),
 dict(dir="dinero", slug="codigos-cajas-fuertes",
  h1="Códigos de cajas fuertes de GTA 6: por qué no sirven las listas",
  desc="Los códigos de las cajas fuertes de GTA 6 son aleatorios: cambian en cada partida y en cada atraco. Cómo encontrar el tuyo y qué hacer si no lo encuentras.",
  chip=("warn", "Una sola fuente"),
  answer="No hay una lista que sirva: según GameSpot, los códigos de las cajas fuertes son aleatorios, cambian en cada partida e incluso si robas dos veces la misma tienda. El código está en un guardia o por la zona, y las cajas pequeñas se pueden forzar.",
  body="""<h2>Cómo encontrar el código</h2>
<ul>
<li>Algunas cajas piden código. Según GameSpot, suele llevarlo encima un guardia o estar apuntado cerca; el modo concentración (pulsar los dos sticks) ayuda a localizarlo.</li>
<li>Si no lo encuentras, las cajas pequeñas se pueden forzar y las cajas de seguridad, abrir con la ganzúa automática.</li>
<li>Casi todas se pueden abrir por la fuerza, pero eso suele hacer saltar la alarma.</li>
</ul>
<h2>¿Y los códigos de Brooks Boatworks o Kingpin Bowling?</h2>
<p>Son de los más buscados estos días. GameSpot no menciona excepciones a que los códigos sean aleatorios, así que el que veas en internet seguramente no coincida con el de tu partida: búscalo en el propio local.</p>
<h2>Antes de abrir la caja</h2>
<p>Ocúpate primero del público, apaga la alarma y destruye las grabaciones de las cámaras. Todos los pasos en <a href="ganar-dinero.html">cómo atracar sin que salte la alarma</a>.</p>
<p>Los códigos de cajas fuertes no son trucos: los <a href="../preguntas/trucos.html">trucos de GTA 6</a> se introducen con el teléfono y solo funcionan al terminar la historia.</p>""",
  sources=[("https://www.gamespot.com/articles/gta-6-safe-codes-and-robberies-guide/", "GameSpot: atracos y códigos de cajas fuertes en GTA 6 (18-11-2026)")],
  related=[("dinero/ganar-dinero.html", "¿Cómo ganar dinero al empezar GTA 6?"),
           ("preguntas/trucos.html", "¿Hay trucos en GTA 6? Cómo se desbloquean"),
           ("dinero/banco-y-ahorros.html", "¿Se pierde el dinero al morir en GTA 6? Banco y ahorros")]),
]


def anadir_a_indice(p):
    rel = f"{p['dir']}/{p['slug']}.html"
    idx = leer(f"{p['dir']}/index.html")
    if p["slug"] + ".html" not in idx:
        li = f'<li class="item"><a href="../{rel}"><span class="item-t">{html.escape(p["h1"])}</span><span class="item-d">{html.escape(p["desc"])}</span></a></li>'
        idx = re.sub(r'(<ul class="list">.*?)(</ul>)', lambda m: m.group(1) + li + m.group(2), idx, count=1, flags=re.S)
        escribir(f"{p['dir']}/index.html", idx)
    sm = leer("sitemap.xml")
    loc = f"https://6estrellas.org/{rel}"
    if loc not in sm:
        sm = sm.replace("  <url><loc>https://6estrellas.org/en/", f"  <url><loc>{loc}</loc><lastmod>{paginas_lanzamiento.PUB}</lastmod></url>\n  <url><loc>https://6estrellas.org/en/", 1)
        escribir("sitemap.xml", sm)


plantilla = leer("preguntas/trucos.html")
for p in NUEVAS:
    rel = f"{p['dir']}/{p['slug']}.html"
    if not (ROOT / rel).exists():
        crear(p, plantilla)
    else:  # reaplica el contenido por si ha cambiado
        articulo(rel, answer=p["answer"], body=p["body"], chip=p["chip"])
    anadir_a_indice(p)

# ---------------------------------------------------------------- títulos alineados con las búsquedas
articulo("preguntas/guardar-partida.html", title="¿GTA 6 tiene autoguardado? Cómo guardar partida (15 ranuras)",
         h1="¿Cómo se guarda la partida en GTA 6? ¿Tiene autoguardado?",
         desc="Sí, GTA 6 tiene autoguardado, además de 15 ranuras de guardado manual. Cómo guardar, cuándo no se puede y por qué los trucos bloquean el guardado.")
articulo("novedades/gta-6-pc.html", title="¿GTA 6 sale en PC o Steam? Fecha y lo que dice Take-Two",
         desc="GTA 6 no está en PC ni en Steam y no hay fecha. Lo que ha dicho Take-Two y cuánto tardaron GTA V y Red Dead Redemption 2 en llegar a PC.")
articulo("preguntas/misiones-capitulo-1.html", title="Misiones de GTA 6: cuántos capítulos tiene y lista completa")
articulo("novedades/precio-ediciones.html", title="¿Cuánto cuesta GTA 6? Precio en España: 79,99 € y Ultimate 99,99 €",
         desc="GTA 6 cuesta 79,99 € la Edición Estándar y 99,99 € la Ultimate en España. Qué añade la Ultimate frente a la Estándar, edición física y PEGI.")

# ---------------------------------------------------------------- secciones nuevas en páginas existentes
s = leer("problemas/ps5-pro-ps5-xbox.html")
BORROSO = """<h2>¿Por qué GTA 6 se ve borroso?</h2>
<p>Por la resolución interna. Según el análisis de Digital Foundry, en PS5 el juego se dibuja internamente a 1440p y se reescala, y en Series S parte de 720p para llegar a 1080p; por eso puede verse menos nítido que en PS5 Pro, que reescala con PSSR. No hay un ajuste en el juego que lo cambie, porque todas las consolas van a 30 fps.</p>
"""
s = re.sub(r'<h2>¿Por qué GTA 6 se ve borroso\?</h2>.*?</p>\n', "", s, flags=re.S)
s = s.replace("<h2>¿Merece la pena comprar una PS5 Pro solo por esto?</h2>", BORROSO + "<h2>¿Merece la pena comprar una PS5 Pro solo por esto?</h2>", 1)
escribir("problemas/ps5-pro-ps5-xbox.html", s)

s = leer("problemas/xbox-one-ps4.html")
OTRAS = """<h2>¿Y en Nintendo Switch 2, Steam o Game Pass?</h2>
<p>Rockstar solo ha lanzado GTA 6 en PS5 y Xbox Series X|S. No hay versión de Nintendo Switch 2 ni de PC, así que tampoco está en Steam (más en <a href="../novedades/gta-6-pc.html">GTA 6 en PC</a>). Rockstar no ha anunciado que el juego esté en Game Pass.</p>
"""
s = re.sub(r'<h2>¿Y en Nintendo Switch 2, Steam o Game Pass\?</h2>.*?</p>\n', "", s, flags=re.S)
s = re.sub(r'(<h2>PS4</h2>\n<p>.*?</p>\n)', lambda m: m.group(1) + OTRAS, s, count=1, flags=re.S)
escribir("problemas/xbox-one-ps4.html", s)

s = leer("lugares/protagonistas.html")
TACON = """<h2>Quién les pone voz</h2>
<p>Según los créditos oficiales, Jason es Dylan Rourke y Lucia es Manni L. Perez. El reparto completo está en <a href="personajes-actores.html">actores y personajes de GTA 6</a>.</p>
<h2>La escena del tacón</h2>
<p>Es una de las más comentadas del avance extendido de agosto: en un tiroteo durante una fiesta, Lucia se defiende de un atacante con un tacón, según Digital Trends en español.</p>
"""
s = re.sub(r'<h2>Quién les pone voz</h2>.*?(?=<h2>Otros personajes oficiales</h2>)', "", s, flags=re.S)
s = s.replace("<h2>Otros personajes oficiales</h2>", TACON + "<h2>Otros personajes oficiales</h2>", 1)
if "es.digitaltrends.com/?p=1105084" not in s:
    s = s.replace('</a></li></ul>\n<p class="small">Resumen redactado',
                  '</a></li><li><a href="https://www.rockstargames.com/VI/credits" rel="noopener" target="_blank">Rockstar Games: créditos oficiales de GTA VI</a></li>'
                  '<li><a href="https://es.digitaltrends.com/?p=1105084" rel="noopener" target="_blank">Digital Trends: el avance extendido de GTA 6</a></li></ul>\n<p class="small">Resumen redactado', 1)
escribir("lugares/protagonistas.html", s)

# Portada: H1 y título con la palabra clave principal
s = leer("index.html")
s = re.sub(r"<title>.*?</title>", "<title>GTA 6: trucos, guías y respuestas cortas | 6 Estrellas</title>", s, count=1)
s = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\1GTA 6: trucos, guías y respuestas cortas | 6 Estrellas", s, count=1)
escribir("index.html", s)
