"""Los 61 trucos de GTA 6: código conocido, requisito de desbloqueo y cuántas fuentes publican el código.

Fuentes (20/11/2026): PowerPyx (18/11), Red Bull (18/11) y Vandal (20/11, 13:49). Las tres coinciden en el
número de trucos, en los requisitos y en 17 códigos. «Subir nivel de búsqueda» lo publican Red Bull y Vandal;
«Borrachera», solo Vandal. Si un código no está en ninguna, se deja como «sin descubrir».
Lo usan herramientas/actualizar_trucos.py (página en español) y herramientas/paginas_en.py (inglés).
"""
U, D, L, R = "↑", "↓", "←", "→"


def c(s):
    return " ".join({"U": U, "D": D, "L": L, "R": R}[x] for x in s)


# (categoría, nombre_es, nombre_en, código o None, requisito_es, requisito_en, nº de fuentes del código)
TRUCOS = [
    ("pj", "Conseguir 250.000 $", "$250,000", c("URDLULDR"), "Termina la historia", "Finish the story", 3),
    ("pj", "Borrachera (tú y tu pareja)", "Drunk (you and your partner)", c("ULRUULRULR"), "Gasta 2.500 $ en alcohol", "Spend $2,500 on alcohol", 1),
    ("pj", "Subir el nivel de alerta en todo el mapa", "Raise Heat Level", c("LDRDUDU"), "Pierde 25 veces un nivel de búsqueda de 3 estrellas", "Lose a 3-star wanted level 25 times", 3),
    ("pj", "Subir el nivel de búsqueda en todo el mapa", "Raise Wanted Level", c("LDRDURU"), "Pierde 50 veces un nivel de búsqueda de 3 estrellas", "Lose a 3-star wanted level 50 times", 2),
    ("pj", "Concentración ilimitada", "Unlimited Focus", c("DUUDUDUDUR"), "Termina la historia", "Finish the story", 3),
    ("pj", "Sin daño por caídas", "No Fall Damage", None, "Sobrevive 20 veces a una caída libre de 40 pies (unos 12 m)", "Survive a 40 ft freefall 20 times", 0),
    ("pj", "Paracaídas", "Parachute", None, "Haz 50 saltos en paracaídas o BASE desde 300 pies (unos 90 m) o más", "Complete 50 skydives or BASE jumps from 300 ft or higher", 0),
    ("pj", "Blindaje", "Body Armor", c("DULUUUUUDD"), "Completa 100 entrenamientos", "Complete 100 workouts", 3),
    ("pj", "Reparar el vehículo", "Repair Vehicle", None, "Gana 10 carreras en Gellhorn Raceway, Thrillbilly Mud Club y Boone Speedway", "Finish 1st in 10 races at Gellhorn Raceway, Thrillbilly Mud Club and Boone Speedway", 0),
    ("pj", "Nitro y combustible ilimitados", "Unlimited Nitrous", None, "Completa 50 saltos acrobáticos", "Complete 50 stunt jumps", 0),
    ("cb", "Munición al máximo", "Max Ammo", c("DURDLLUUDL"), "Gana 25 medallas de bronce o mejores en campos de tiro", "Win 25 bronze medals or better at shooting ranges", 3),
    ("cb", "Munición infinita", "Infinite Ammo", c("DURDLLUDDD"), "Gana 25 medallas de plata o mejores en campos de tiro", "Win 25 silver medals or better at shooting ranges", 3),
    ("cb", "Sin recargar", "No Reload", c("DURDLLUDDU"), "Gana 25 medallas de oro en campos de tiro", "Win 25 gold medals at shooting ranges", 3),
    ("cb", "Todas las armas explosivas", "All Explosive Weapons", None, "Lanza 100 granadas", "Throw 100 grenades", 0),
    ("cb", "Munición incendiaria", "Incendiary Ammo", None, "Quema a 100 enemigos", "Burn 100 enemies with fire damage", 0),
    ("cb", "Botellas explosivas", "Exploding Bottles", None, "Lanza 100 cócteles molotov", "Throw 100 Molotovs", 0),
    ("cb", "Escopeta explosiva (Mason & Keen Shortstraw)", "Explosive Shotgun (Mason & Keen Shortstraw)", None, "Alcanza a 100 enemigos con daño explosivo", "Hit 100 enemies with explosive damage", 0),
    ("cb", "Lanzacohetes Hauners H-AT", "Hauners H-AT", None, "Haz explotar 100 vehículos", "Blow up 100 vehicles", 0),
    ("cb", "Fuerza de ataque (golpes y disparos lanzan por los aires)", "Attack Force (hits launch targets)", c("DULLRDDUD"), "Termina la historia", "Finish the story", 3),
    ("cb", "Pelotas explosivas", "Exploding Balls", c("DULLRDDUR"), "Alcanza a 20 enemigos con daño explosivo", "Hit 20 enemies with explosive damage", 3),
    ("cb", "Choques que lanzan por los aires", "Vehicle Force (collisions launch targets)", c("DULLRDLUD"), "Mata a 25 enemigos con un vehículo", "Kill 25 enemies with a vehicle", 3),
    ("ve", "Interstate Ambulance", "Interstate Ambulance", None, "Descúbrela (regístrala en Progreso / WAiNK)", "Discover it (Progress menu / WAiNK)", 0),
    ("ve", "Airboat 09", "Airboat 09", None, "Completa 5 desafíos de supervivencia", "Complete 5 survival challenges", 0),
    ("ve", "Bravado Banshee", "Bravado Banshee", None, "Completa todos los desafíos de combate", "Complete all combat challenges", 0),
    ("ve", "Tuff BMX", "Tuff BMX", None, "Completa 5 desafíos de fitness", "Complete 5 fitness challenges", 0),
    ("ve", "Maibatsu Boomazoom", "Maibatsu Boomazoom", c("LURDLLUL"), "Completa 5 desafíos de compras", "Complete 5 shopping challenges", 3),
    ("ve", "Nagasaki Carbon RS", "Nagasaki Carbon RS", None, "Completa todos los desafíos de exploración", "Complete all exploration challenges", 0),
    ("ve", "'65 Vapid Dominator", "'65 Vapid Dominator", None, "Completa todos los desafíos de fitness", "Complete all fitness challenges", 0),
    ("ve", "Progen Emerus", "Progen Emerus", None, "Completa todos los desafíos de vehículos", "Complete all vehicle challenges", 0),
    ("ve", "Flamenco hinchable", "Inflatable Flamingo", None, "Destruye 50 flamencos de cocaína", "Destroy 50 cocaine flamingos", 0),
    ("ve", "MTL Pumper (camión de bomberos)", "MTL Pumper (fire truck)", c("LURDLRRU"), "Descúbrelo (regístralo en Progreso / WAiNK)", "Discover it (Progress menu / WAiNK)", 3),
    ("ve", "Taxi Vapid Stanier G2", "Vapid Stanier G2 Taxi", None, "Completa 5 desafíos deportivos", "Complete 5 sports challenges", 0),
    ("ve", "Hauners P-996 Lazer (caza)", "Hauners P-996 Lazer (jet)", None, "Completa todos los desafíos", "Complete all challenges", 0),
    ("ve", "HVY Bulldozer", "HVY Bulldozer", c("LURDLRRD"), "Descúbrelo (regístralo en Progreso / WAiNK)", "Discover it (Progress menu / WAiNK)", 3),
    ("ve", "Lapwing Mallard (avioneta)", "Lapwing Mallard (plane)", None, "Completa 5 desafíos de vehículos", "Complete 5 vehicle challenges", 0),
    ("ve", "Brimstone Golfer (carrito de golf)", "Brimstone Golfer (golf cart)", None, "Completa todos los desafíos deportivos", "Complete all sports challenges", 0),
    ("ve", "Hauners Rhino (tanque)", "Hauners Rhino Tank", None, "Completa todos los desafíos de supervivencia", "Complete all survival challenges", 0),
    ("ve", "Maibatsu Sanchez (moto de cross)", "Maibatsu Sanchez (dirt bike)", None, "Completa 5 desafíos criminales", "Complete 5 criminal challenges", 0),
    ("ve", "Nagasaki Sea Sparrow (helicóptero)", "Nagasaki Sea Sparrow (helicopter)", None, "Completa 5 desafíos de exploración", "Complete 5 exploration challenges", 0),
    ("ve", "Speeder 700 GT (lancha)", "Speeder 700 GT (boat)", None, "Completa 5 desafíos de combate", "Complete 5 combat challenges", 0),
    ("ve", "Truffade Thrax", "Truffade Thrax", None, "Completa todos los desafíos de compras", "Complete all shopping challenges", 0),
    ("ve", "Western Zombie Bobber (moto)", "Western Zombie Bobber (motorcycle)", None, "Completa todos los desafíos criminales", "Complete all criminal challenges", 0),
    ("en", "Adelantar la hora", "Move Time Forward", None, "Encuentra 10 relojes coleccionables", "Find 10 collectible watches", 0),
    ("en", "Pausar la hora del día", "Pause Time of Day", None, "Encuentra 20 relojes coleccionables", "Find 20 collectible watches", 0),
    ("en", "Cambiar el clima", "Cycle Weather", c("DRUDRUR"), "Termina la historia", "Finish the story", 3),
    ("fi", "Hora dorada", "Golden Hour", None, "Pasa 4 horas cogidos de la mano", "Spend 4 hours holding hands", 0),
    ("fi", "Azúcar en polvo", "Powdered Sugar", None, "Escanea con WAiNK todos los restos espaciales", "Scan all space debris with WAiNK", 0),
    ("fi", "Estenopeica", "Pinhole", None, "Desmantela 25 operaciones de bandas con tu pareja", "Clear 25 gang operations with your partner", 0),
    ("fi", "Jungla de neón", "Neon Jungle", None, "Descubre los 16 vehículos Girlypop", "Discover all 16 Girlypop vehicles", 0),
    ("fi", "Antaño (tele CRT en blanco y negro)", "Yesteryear (black-and-white CRT)", None, "Descubre el Ridgeway", "Discover the Ridgeway", 0),
    ("fi", "Cataclismo (humo denso)", "Cataclysm (murky smoke)", c("DDURRULLRR"), "Descubre el Vamos de Martha", "Discover Martha's Vamos", 3),
    ("fi", "Cinta de vídeo", "Videotape", None, "Completa 50 actividades con tu pareja", "Complete 50 activities with your partner", 0),
    ("fi", "Espejo oscuro", "Dark Mirror", None, "Gana 500.000 $ vendiendo vehículos", "Make $500,000 selling vehicles", 0),
    ("fi", "Migraña", "Migraine", None, "Aguanta 6 minutos con 6 estrellas de búsqueda", "Survive 6 minutes with a 6-star wanted level", 0),
    ("fi", "Casa de muñecas", "Dollhouse", c("DDURRULLDR"), "Pasa 8 horas con tu pareja", "Spend 8 hours with your partner", 3),
    ("fi", "Chicle", "Bubblegum", None, "Encuentra los 24 cromos de los Vice City Flamingos", "Find all 24 Vice City Flamingos cards", 0),
    ("fi", "Avance rápido", "Fast Forward", None, "Completa 50 meditaciones", "Complete 50 meditations", 0),
    ("fi", "Ojo de pez", "Fisheye", None, "Pesca 100 peces", "Catch 100 fish", 0),
    ("fi", "Vieja gloria (tele CRT en color)", "Faded Glory (color CRT)", c("DDURRULLLR"), "Roba 50 tiendas con tu pareja", "Rob 50 stores with your partner", 3),
    ("fi", "Pixel art", "Pixel Art", None, "Gana 250.000 $ vendiendo coleccionables", "Make $250,000 selling collectibles", 0),
    ("fi", "Infierno", "Hellscape", None, "Roba 100 coches de policía", "Steal 100 cop vehicles", 0),
]

CAT = {"pj": ("Personaje", "Player"), "cb": ("Armas y combate", "Combat"), "ve": ("Vehículos", "Vehicle spawns"),
       "en": ("Entorno", "Environment"), "fi": ("Filtros de pantalla", "Screen filters")}

assert len(TRUCOS) == 61, len(TRUCOS)
CONOCIDOS = sum(1 for t in TRUCOS if t[3])


def tablas(lang):
    es = lang == "es"
    out = []
    for k, (n_es, n_en) in CAT.items():
        filas = [t for t in TRUCOS if t[0] == k]
        cab = ("Truco", "Código", "Cómo se desbloquea") if es else ("Cheat", "Code", "How to unlock")
        trs = []
        for _, nes, nen, cod, res, ren, nf in filas:
            if cod:
                nota = "" if nf >= 3 else (" <small>(2 fuentes)</small>" if nf == 2 else (" <small>(una sola fuente)</small>" if es else " <small>(single source)</small>"))
                if nf == 2 and not es:
                    nota = " <small>(2 sources)</small>"
                celda = f'<span class="code">{cod}</span>{nota}'
            else:
                celda = "Sin descubrir" if es else "Not found yet"
            trs.append(f"<tr><td>{nes if es else nen}</td><td>{celda}</td><td>{res if es else ren}</td></tr>")
        titulo = n_es if es else n_en
        out.append(f'<h3>{titulo} ({len(filas)})</h3>\n<div class="table-wrap" tabindex="0" role="region" aria-label="{"Tabla (desliza para ver más)" if es else "Table (scroll for more)"}"><table class="cheats"><thead><tr><th>{cab[0]}</th><th>{cab[1]}</th><th>{cab[2]}</th></tr></thead><tbody>'
                   + "".join(trs) + "</tbody></table></div>")
    return "\n".join(out)
