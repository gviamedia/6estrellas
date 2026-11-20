"""Contenido de la versión en inglés (Six Stars). Lo usa herramientas/generar_en.py.

MAPA: ruta de la página en español -> ruta de su equivalente en inglés (para hreflang y el selector ES/EN).
ARTICULOS: una entrada por artículo. Campos:
  es, en: rutas; title (<title>), h1, desc (meta description), chip (clase, etiqueta),
  answer (respuesta corta), body (HTML), sources [(url, texto)], related [rutas en inglés].
Reglas: nada sin fuente, etiquetas de certeza traducidas, fuentes en inglés cuando existen.
"""

SECCIONES_EN = {
    "questions": dict(es="preguntas", name="Questions",
                      h1="GTA 6 questions: how the game works",
                      lead="Straight answers about how GTA 6 plays: missions, saving, cheats, endings and more.",
                      title="GTA 6 Questions: How the Game Works | Six Stars",
                      desc="Short, sourced answers to common GTA 6 questions: replaying missions, saving, cheats, endings, first-person mode, co-op and more."),
    "money": dict(es="dinero", name="Money & Cars",
                  h1="GTA 6 money and cars: earn it, bank it, keep it",
                  lead="How to make money early, where to keep it and how to hold on to the cars you steal.",
                  title="GTA 6 Money and Cars Guides | Six Stars",
                  desc="How to make money fast in GTA 6, how the BuckMe bank works, how to keep stolen cars and which car is fastest so far."),
    "issues": dict(es="problemas", name="Fixes",
                   h1="GTA 6 fixes: errors, download size and consoles",
                   lead="Launch problems, download size, physical copies and how each console runs the game.",
                   title="GTA 6 Fixes, Errors and Download Size | Six Stars",
                   desc="What to do when GTA 6 won't load, how big the download is, PSN outages, PS5 Pro vs Xbox and whether it runs on PS4 or Xbox One."),
    "pc-online": dict(es="novedades", name="PC & Online",
                      h1="GTA 6 on PC, GTA 6 Online, GTA+ and editions",
                      lead="What is known about a PC version, online multiplayer, GTA+, prices, patches and mods.",
                      title="GTA 6 PC, Online, GTA+ and Editions | Six Stars",
                      desc="Is GTA 6 coming to PC? Does it have online? What GTA+ includes, Standard vs Ultimate pricing, patch 1.002 and Rockstar's mod rules."),
    "leonida": dict(es="lugares", name="Leonida",
                    h1="GTA 6 map, characters and radio",
                    lead="The state of Leonida, its regions, the two protagonists and the radio stations Rockstar has revealed.",
                    title="GTA 6 Map, Characters and Radio | Six Stars",
                    desc="The six regions of Leonida, who Jason Duval and Lucia Caminos are, and the GTA 6 radio stations Rockstar has officially revealed."),
}

OK = ("ok", "Per cited sources")
PART = ("warn", "Partly confirmed")
ONE = ("warn", "Single source")
VAR = ("warn", "Figure may change")
EST = ("warn", "Rough estimate")

TK = "https://kotaku.com/grand-theft-auto-6-the-kotaku-review-2000757842"
PSQ = "https://www.pushsquare.com/reviews/ps5/grand-theft-auto-6"
RS_ED = "https://support.rockstargames.com/articles/4QfG4FmZCf5W1gS8jy4UVT/grand-theft-auto-vi-platform-editions-and-versions"
RS_INST = "https://support.rockstargames.com/articles/M6h7B5fJZMwG1dnzQkt4Z/grand-theft-auto-vi-installation-requirements"
RS_TIMES = "https://support.rockstargames.com/articles/29jV3Cv2cCgvwM1XgtMO5o/grand-theft-auto-vi-regional-pre-load-and-release-times-on-playstation-5-and-xbox-series-x-or-s"
NW_LAUNCH = "https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available"
VANDAL_LIVE = "https://vandal.elespanol.com/noticia/2026322031/gta-6-en-directo-ltimas-noticias-reacciones-y-todo-sobre-el-lanzamiento-del-juego-de-rockstar/"
FORBES = "https://www.forbes.com/sites/erikkain/2026/11/16/gta-6-release-date-time-ps5-xbox-series-x-download-size-day-one-update/"

ARTICULOS = [
# ---------------------------------------------------------------- QUESTIONS
dict(es="preguntas/repetir-misiones.html", en="questions/replay-missions.html",
 title="Can You Replay Missions in GTA 6? No — Here's the Workaround",
 h1="Can you replay missions in GTA 6?",
 desc="GTA 6 has no mission replay. The only workaround is keeping an older save in a separate slot before each mission. Here's how.",
 chip=OK,
 answer="No. Unlike GTA V, GTA 6 has no option to replay a mission once you've finished it. The only way back is to load an older save.",
 body="""<p>This is one of the biggest surprises for GTA V players, who could replay any mission from the pause menu to chase better scores. GamesRadar, Vandal (citing Eurogamer) and GTABase all report that GTA 6 has no mission replay, and GamesRadar thinks it is unlikely to be added later.</p>
<h2>What happened to gold medals?</h2>
<p>GTA 6 drops per-mission Gold Medal objectives, according to GTABase. GamesRadar says the old skill challenges now live in their own section of the Progress menu, are much broader, and are mainly used to unlock <a href="cheats.html">cheats</a> after you finish the story.</p>
<h2>The workaround: multiple save slots</h2>
<p>GTA 6 gives you 15 manual save slots. If you want to revisit a specific moment, save to a fresh slot before the mission starts and don't overwrite it. Always do this before missions with choices.</p>
<p>See <a href="how-to-save.html">how saving and autosave work</a>. If Rockstar ever adds mission replay in an update, we'll update this page.</p>""",
 sources=[("https://www.gamesradar.com/games/grand-theft-auto/gta-6-replay-missions-how-to/", "GamesRadar: Can you replay missions in GTA 6?"),
          ("https://www.gtabase.com/gta-6/missions/", "GTABase: GTA 6 story missions list"),
          ("https://vandal.elespanol.com/noticia/2026322036/gta-6-cambia-un-aspecto-clave-respecto-a-gta-5-la-nueva-entrega-de-la-saga-no-permite-rejugar-misiones/", "Vandal (Spanish): GTA 6 doesn't let you replay missions, citing Eurogamer")],
 related=["questions/how-to-save.html", "questions/endings-choices.html", "questions/chapter-1-missions.html"]),

dict(es="preguntas/cambiar-jason-lucia.html", en="questions/switch-characters.html",
 title="How to Switch Between Jason and Lucia in GTA 6 (and When It Unlocks)",
 h1="How do you switch between Jason and Lucia in GTA 6?",
 desc="Free switching between Jason and Lucia unlocks around Chapters 2 and 3. How to switch, and when the game won't let you.",
 chip=PART,
 answer="Not at first. Free switching between Jason and Lucia unlocks somewhere around Chapters 2 and 3 (guides disagree on the exact point). Until then, the story decides who you play.",
 body="""<p>You can't swap at the start. VGC and GamesRadar say you first take Lucia into the open world after Chapter 1 and that free switching turns on at a set point in Chapter 2. Spanish outlet 3DJuegos instead places it in Chapter 3, after a Chapter 2 played only as Lucia. Either way, it arrives early in the story.</p>
<h2>How to switch</h2>
<p>It's on the d-pad, but guides describe the input differently: VGC says press right on the d-pad, while GamesRadar says hold right and press R1 (RB on Xbox). Check the controls menu in your own game.</p>
<h2>When you can't switch</h2>
<ul>
<li>If the other character is busy (for example, riding in a RydeMe), their portrait is grayed out.</li>
<li>Missions marked with a J or an L on the map can only be played by that character.</li>
<li>When you're together, your partner can drive, cover you during robberies or head off on their own.</li>
</ul>
<p>Kotaku adds that your partner's life carries on off-screen while you aren't controlling them.</p>""",
 sources=[("https://www.videogameschronicle.com/guide/how-to-change-characters-in-gta-6/", "VGC: How to change characters in GTA 6"),
          ("https://www.gamesradar.com/games/grand-theft-auto/gta-6-switch-characters-command/", "GamesRadar: How to switch characters in GTA 6"),
          (TK, "Kotaku: Grand Theft Auto 6 review"),
          ("https://www.3djuegos.com/juegos/grand-theft-auto-vi/analisis/analisis-gta-vi-videojuego-perfecto", "3DJuegos (Spanish): GTA VI review")],
 related=["questions/endings-choices.html", "leonida/characters.html", "questions/co-op.html"]),

dict(es="preguntas/cuanto-dura.html", en="questions/how-long-to-beat.html",
 title="How Long Is GTA 6? Story Length and 100% Completion Time",
 h1="How long is GTA 6?",
 desc="Rockstar's Rob Nelson put the main story at about 80 hours; reviewers report 50 to 70. What reviews say about 100% completion.",
 chip=EST,
 answer="The main story takes roughly 50 to 80 hours depending on who's counting and how much you wander. Estimates for 100% completion run from about 200 to 300+ hours.",
 body="""<h2>What Rockstar said</h2>
<p>Rob Nelson of Rockstar North told The New York Times that a full run of the main story took him about 80 hours, roughly double GTA V. He was describing a playthrough during development in February, as reported by Spanish outlet Vandal in August 2026, so the final game may differ.</p>
<h2>What reviewers measured</h2>
<ul>
<li><strong>Push Square:</strong> a roughly 60-hour storyline that will likely take the average player around 80 hours. The reviewer played over 150 hours.</li>
<li><strong>Kotaku:</strong> 152 hours played, main campaign finished and two endings seen.</li>
<li><strong>3DJuegos (Spanish):</strong> about 55 hours if you stick to the story.</li>
<li><strong>MeriStation (Spanish), via Demócrata:</strong> 70 hours for the five chapters and 95 story missions, including some exploration; about 50 hours for the campaign alone.</li>
</ul>
<h2>What about 100%?</h2>
<p>MeriStation's figure is about 200 hours. Push Square says a 100% save could take up to 300 hours or more; that's a single reviewer's estimate and depends on whether you use guides. Treat both as rough.</p>
<p>Worried about missing something? Read up on <a href="endings-choices.html">endings and choices</a>. We'll update this page when player data is available.</p>""",
 sources=[(PSQ, "Push Square: Grand Theft Auto 6 review"),
          (TK, "Kotaku: Grand Theft Auto 6 review"),
          ("https://vandal.elespanol.com/noticia/2026240004/cuanto-durara-gta-6-rockstar-habla-de-la-duracion-de-su-historia-y-apunta-al-doble-de-horas-que-gta-v/", "Vandal (Spanish): Rockstar on GTA 6's story length (Aug 28, 2026)"),
          ("https://www.3djuegos.com/juegos/grand-theft-auto-vi/analisis/analisis-gta-vi-videojuego-perfecto", "3DJuegos (Spanish): GTA VI review"),
          ("https://www.democrata.es/cultura/gta-vi-nota-10-analisis-cuanto-dura-historia/", "Demócrata (Spanish): MeriStation's review, 70 hours and 95 missions")],
 related=["questions/endings-choices.html", "questions/chapter-1-missions.html", "questions/trophies-achievements.html"]),

dict(es="preguntas/guardar-partida.html", en="questions/how-to-save.html",
 title="How to Save in GTA 6: 15 Save Slots and How Autosave Works",
 h1="How do you save your game in GTA 6?",
 desc="GTA 6 has 15 manual save slots plus a separate autosave. How to save, when you can't, and why cheats block saving.",
 chip=OK,
 answer="From the pause menu, almost any time. GamesRadar and Vandal report 15 manual save slots, and GamesRadar adds a separate autosave slot. Rockstar hasn't detailed this itself in what we've checked.",
 body="""<h2>How to save</h2>
<ol>
<li>Press Start to open the game menu.</li>
<li>Select <strong>Game</strong>.</li>
<li>Pick a slot.</li>
<li>Choose <strong>Save Game</strong>.</li>
</ol>
<p>That's the process as described by GamesRadar. You can overwrite or load any of the 15 manual slots.</p>
<h2>How autosave works</h2>
<p>GamesRadar describes a separate, 16th slot reserved for autosave. It's overwritten after missions, when you're Wasted or Busted, and after major open-world encounters.</p>
<h2>When you can't save</h2>
<ul>
<li><strong>During a mission:</strong> you rely on autosave, though you can restart from the beginning or a checkpoint.</li>
<li><strong>Right after a call or objective:</strong> if free roam won't let you save, leave the building or vehicle and try again.</li>
<li><strong>With cheats on:</strong> GamesRadar, PowerPyx and Vandal all say any cheat disables saving until you quit and reload.</li>
</ul>
<p>There's also no in-game quit option, per GamesRadar: if you close the app from the console home screen without saving, you're back to your last autosave.</p>
<h2>Tip</h2>
<p>Since you <a href="replay-missions.html">can't replay missions</a>, keep one slot for your main run and save to a new one before any mission with a choice.</p>""",
 sources=[("https://www.gamesradar.com/games/grand-theft-auto/gta-6-how-to-save/", "GamesRadar: How to save your game in GTA 6"),
          ("https://www.pcgamer.com/games/grand-theft-auto/gta-6-save-game/", "PC Gamer: Saving in GTA 6"),
          ("https://www.powerpyx.com/gta-6-all-cheats/", "PowerPyx: cheats disable trophies and saving"),
          ("https://vandal.elespanol.com/noticia/2026322036/gta-6-cambia-un-aspecto-clave-respecto-a-gta-5-la-nueva-entrega-de-la-saga-no-permite-rejugar-misiones/", "Vandal (Spanish): no mission replay, 15 save slots")],
 related=["questions/replay-missions.html", "questions/cheats.html", "questions/endings-choices.html"]),

dict(es="preguntas/comprar-casas.html", en="questions/buy-houses.html",
 title="Can You Buy Houses in GTA 6? Safehouses, Garages and Businesses",
 h1="Can you buy houses or businesses in GTA 6?",
 desc="What's confirmed about buying property in GTA 6: homes come with the story, garages can be bought, and businesses are unconfirmed.",
 chip=PART,
 answer="There's no reliable confirmation yet that you can buy houses or businesses. Homes come through the story. What you can buy is garages.",
 body="""<h2>Homes</h2>
<p>The homes we know about come with the story. Jason, for example, lives rent-free in one of Brian Heder's properties in the Leonida Keys in exchange for helping with local shakedowns, according to VICE, which also says Rockstar hasn't confirmed whether houses can be bought. Push Square mentions a beach house and the pair's Vice City penthouse.</p>
<p>At a safehouse you can grab something from the fridge, trim or shave your hair (a new style needs a barber or salon) and switch characters when the story allows it, per VICE.</p>
<h2>Garages</h2>
<p>You start with room for just three personal vehicles and can buy garages for more space, according to German site PC Games in a pre-launch article citing a Famitsu interview with Rockstar. More in <a href="../money/keep-cars-garages.html">how to keep a car</a>.</p>
<h2>What about businesses?</h2>
<p>We haven't found a reliable post-launch source confirming businesses you can buy. GTA+ members get a Crosstown garage with an armory and a place to sell stolen goods, according to Vandal's launch coverage (see <a href="../pc-online/gta-plus.html">what GTA+ includes</a>).</p>
<p class="note">Still unconfirmed by reliable sources: whether houses or businesses can be bought. We'll update this page as soon as that changes.</p>""",
 sources=[("https://www.vice.com/en/article/gta-6-can-you-buy-a-house-safehouses/", "VICE: Can you buy a house in GTA 6? (Nov 17, 2026)"),
          (PSQ, "Push Square: Grand Theft Auto 6 review"),
          ("https://www.pcgames.de/GTA-6-Spiel-55239/News/Garage-Diebstahl-Autos-Fahrzeuge-1553128/", "PC Games (German): garages and vehicles in GTA 6 (Sept 8, 2026)"),
          (VANDAL_LIVE, "Vandal (Spanish): GTA 6 launch live coverage")],
 related=["money/keep-cars-garages.html", "money/buckme-bank.html", "pc-online/gta-plus.html"]),

dict(es="preguntas/trucos.html", en="questions/cheats.html",
 title="GTA 6 Cheats for PS5 and Xbox: How to Unlock and Enter Them",
 h1="Does GTA 6 have cheats? How to unlock them",
 desc="GTA 6 has 61 cheats, but they only unlock after you beat the story. How to enter them and what they turn off.",
 chip=OK,
 answer="Yes, 61 of them, with the same inputs on PS5 and Xbox. But they only work after you beat the main story, and most also require completing a challenge.",
 body="""<p>This is the big change from earlier GTA games: cheats aren't available from the start. PowerPyx, Red Bull and Vandal all say they unlock after you complete the main story, and most also need a specific challenge (Progress menu &gt; Cheats). Enter a code before that and nothing happens.</p>
<h2>How to enter a cheat</h2>
<ol>
<li>Press up on the d-pad to pull out your phone.</li>
<li>Hold L1 and press R1 (on Xbox, hold LB and press RB).</li>
<li>Enter the cheat's d-pad sequence.</li>
</ol>
<h2>What you give up</h2>
<ul>
<li>Trophies and achievements are disabled.</li>
<li>Saving is disabled until you quit and reload (see <a href="how-to-save.html">how to save</a>).</li>
</ul>
<p>The 61 figure is the number of cheats; many of the actual codes were still undiscovered on launch day. We'll only list codes once reliable sources confirm them.</p>""",
 sources=[("https://www.powerpyx.com/gta-6-all-cheats/", "PowerPyx: All GTA 6 cheats (Nov 18, 2026)"),
          ("https://www.redbull.com/int-en/gta-6-cheat-codes", "Red Bull: GTA 6 cheat codes (Nov 18, 2026)"),
          ("https://vandal.elespanol.com/guias/guia-grand-theft-auto-vi-trucos-consejos-y-secretos/trucos", "Vandal (Spanish): GTA 6 cheats guide")],
 related=["questions/trophies-achievements.html", "questions/how-to-save.html", "questions/replay-missions.html"]),

dict(es="preguntas/primera-persona.html", en="questions/first-person-mode.html",
 title="Does GTA 6 Have a First-Person Mode? Not at Launch",
 h1="Does GTA 6 have a first-person mode?",
 desc="GTA 6 doesn't have a full first-person mode at launch. You only get a first-person view when aiming certain weapons.",
 chip=OK,
 answer="Not a full one at launch. You only switch to first person while aiming with certain weapons.",
 body="""<p>GTA V lets you play the whole game in first person on its newer versions. GTA 6 doesn't at launch. Rob Nelson of Rockstar North said so in an interview with YouTuber Davy Jones, as reported by VICE before release.</p>
<p>What you do get is a first-person perspective while aiming with certain weapons.</p>
<h2>Will it come later?</h2>
<p>Nothing has been announced. In GTA V, first-person mode arrived with the PS4 and Xbox One release in November 2014, more than a year after the original 2013 launch, but that guarantees nothing for GTA 6.</p>""",
 sources=[("https://www.vice.com/en/article/will-gta-6-have-first-person-mode/", "VICE: Will GTA 6 have a first-person mode? (Aug 28, 2026)")],
 related=["issues/ps5-pro-vs-ps5-vs-xbox.html", "questions/switch-characters.html", "pc-online/gta-6-pc.html"]),

dict(es="preguntas/finales-decisiones.html", en="questions/endings-choices.html",
 title="How Many Endings Does GTA 6 Have? Choices and Missable Content",
 h1="How many endings does GTA 6 have?",
 desc="GTA 6 has multiple endings and your choices matter. What reviewers say about Jason and Lucia's relationship and missable content.",
 chip=PART,
 answer="More than one, and your choices matter. Kotaku saw two endings; the total hasn't been confirmed.",
 body="""<h2>What's confirmed</h2>
<p>There is more than one ending: Kotaku saw two in its review. Jason and Lucia's relationship can be platonic or romantic depending on your choices, also per Kotaku. Push Square cautions that some decisions feel more like an illusion than something truly meaningful.</p>
<h2>An early example</h2>
<p>Early on you can decorate the beach house. It's optional, and according to Push Square, finishing it in time brings the couple closer, while skipping it means Lucia notices you didn't go the extra mile. It isn't clear whether it can be missed for good.</p>
<h2>How to protect your run</h2>
<p>Because <a href="replay-missions.html">missions can't be replayed</a>, save to a new slot before any mission with a choice. It's the only safe way to try the other option.</p>
<p class="note">Still unconfirmed: the exact number of endings and whether you can redo an ending from the same save.</p>""",
 sources=[(TK, "Kotaku: Grand Theft Auto 6 review (Nov 18, 2026)"),
          (PSQ, "Push Square: Grand Theft Auto 6 review")],
 related=["questions/how-to-save.html", "questions/how-long-to-beat.html", "leonida/characters.html"]),

dict(es="preguntas/idioma-espanol.html", en="questions/languages.html",
 title="GTA 6 Languages: Voice Acting and Subtitle Options",
 h1="What languages is GTA 6 in?",
 desc="GTA 6's voice acting is English only, with subtitles and menus in other languages. What the PlayStation and Xbox store listings show.",
 chip=OK,
 answer="Voices are English only, as in previous GTA games. Menus and subtitles come in several languages, including Spanish for Spain and for Mexico.",
 body="""<p>GTA 6 sticks with series tradition: no dubbed versions. The PlayStation Store lists the voice language as English only.</p>
<h2>Text and subtitles</h2>
<ul>
<li>The Xbox Store listing says 13 languages are supported, without naming them.</li>
<li>The PlayStation Store lists 12 screen languages, including Spanish and Spanish (Mexico).</li>
</ul>
<p>Spanish outlet Vandal, reading the store listing back in June, reported the same: English audio only, with Spanish text for Spain and Mexico.</p>
<h2>Tip</h2>
<p>If it's hard to follow dialogue while driving, increase the subtitle size in the game's display or accessibility settings.</p>""",
 sources=[("https://store.playstation.com/es-es/product/EP1004-PPSA01547_00-GTAVISTANDARD001/", "PlayStation Store listing for GTA VI (Spain)"),
          ("https://www.xbox.com/es-es/games/store/grand-theft-auto-vi/9p3h4968grsm", "Xbox Store listing for GTA VI (Spain)"),
          ("https://vandal.elespanol.com/noticia/1350791241/sin-doblaje-espanol-gta-6-confirma-que-mantiene-la-tradicion-y-solo-llegara-con-voces-en-ingles/", "Vandal (Spanish): GTA 6 keeps English-only voices (June 29, 2026)")],
 related=["questions/play-offline.html", "pc-online/price-editions.html", "questions/first-person-mode.html"]),

dict(es="preguntas/jugar-sin-internet.html", en="questions/play-offline.html",
 title="Can You Play GTA 6 Offline? Yes, After the Download",
 h1="Can you play GTA 6 offline?",
 desc="GTA 6 is single-player and supports offline play, but you need internet to download it, even if you buy the physical edition.",
 chip=PART,
 answer="Yes. It's a single-player game and the PlayStation Store lists it as supporting offline play. But you need internet to download it, even with the physical edition.",
 body="""<h2>Playing offline</h2>
<p>The PlayStation Store listing marks GTA 6 as compatible with offline play. The Xbox Store notes that some features may require an internet connection and signing up for a Rockstar Games account.</p>
<h2>Downloading requires internet</h2>
<p>The physical edition has no disc: the box contains a download code, according to Rockstar. You always have to download the full game, and Rockstar says it needs up to 212 GB of free space depending on your console. See <a href="../issues/download-size.html">GTA 6 download size</a>.</p>
<h2>If PlayStation Network is down</h2>
<p>If the game won't start because of a network problem, check <a href="../issues/not-loading-fixes.html">what to do when GTA 6 won't load</a>. Looking for multiplayer? Here's the <a href="../pc-online/gta-6-online.html">status of GTA 6 Online</a>.</p>""",
 sources=[("https://store.playstation.com/es-es/product/EP1004-PPSA01547_00-GTAVISTANDARD001/", "PlayStation Store listing for GTA VI (Spain)"),
          ("https://www.xbox.com/es-es/games/store/grand-theft-auto-vi/9p3h4968grsm", "Xbox Store listing for GTA VI (Spain)"),
          (RS_ED, "Rockstar Support: GTA VI platforms, editions and versions"),
          (RS_INST, "Rockstar Support: GTA VI installation requirements")],
 related=["issues/physical-edition-no-disc.html", "issues/download-size.html", "pc-online/gta-6-online.html"]),

dict(es="preguntas/notas-analisis.html", en="questions/review-scores.html",
 title="GTA 6 Metacritic Score: 99 — Review Roundup",
 h1="What is GTA 6's review score?",
 desc="GTA 6 holds a 99 on Metacritic based on launch-day reviews. A roundup of major outlets' scores and how the average may change.",
 chip=VAR,
 answer="A 99 on Metacritic, based on launch-day data. The average shifts as new reviews come in.",
 body="""<h2>The average</h2>
<p>TheWrap reported a 99 on Metacritic based on 147 reviews on November 18, 2026. Tom's Guide's live roundup also cites 99 after about 150 reviews, and Spanish outlet Vandal counted 153 reviews on PS5 the next day, noting that the score ties The Legend of Zelda: Ocarina of Time.</p>
<p>We haven't found a reliable source for an OpenCritic score, so we don't list one.</p>
<h2>Some scores</h2>
<ul>
<li><strong>10/10:</strong> IGN (per TheWrap), Push Square and Vandal.</li>
<li><strong>No score:</strong> Kotaku, which doesn't score games.</li>
</ul>
<p>Averages move as more reviews are published. These figures are from launch week.</p>""",
 sources=[("https://www.thewrap.com/industry-news/tech/gta-vi-review-roundup/", "TheWrap: GTA VI review roundup (Nov 18, 2026)"),
          ("https://www.tomsguide.com/news/live/gta-6-review-roundup-live-updates", "Tom's Guide: GTA 6 review roundup, live"),
          (PSQ, "Push Square: Grand Theft Auto 6 review"),
          (VANDAL_LIVE, "Vandal (Spanish): GTA 6 launch live coverage")],
 related=["questions/how-long-to-beat.html", "questions/endings-choices.html", "issues/ps5-pro-vs-ps5-vs-xbox.html"]),

dict(es="preguntas/perder-a-la-policia.html", en="questions/lose-wanted-level.html",
 title="How to Lose the Cops in GTA 6: Wanted Level and Criminal Profile",
 h1="How do you lose the cops in GTA 6?",
 desc="GTA 6 police remember what you look like and track a criminal profile. Changing clothes and your getaway car helps you slip away.",
 chip=OK,
 answer="Police remember what you look like: they share your description over the radio and the game keeps a criminal profile of how you behave. Changing your clothes and your getaway car helps you slip past them.",
 body="""<h2>What's new compared with GTA V</h2>
<ul>
<li><strong>Criminal profile:</strong> the game tracks how you behave, and that changes how police and the wider world treat you (Push Square, Kotaku).</li>
<li><strong>Radio descriptions:</strong> officers share details about Jason and Lucia with each other over the radio, so your look matters (Kotaku).</li>
<li><strong>Clothes:</strong> Kotaku says you can change clothes if you have heat, and Push Square says a change of clothes and getaway car can let you slip past the police undetected.</li>
<li><strong>Non-lethal shots:</strong> you can target non-vital areas to incapacitate people without killing them (Push Square). Kotaku notes that a violent streak can get you labeled a psycho by the criminal profile system.</li>
</ul>
<h2>What follows from that</h2>
<p>Getting out of sight and changing your look works better than fleeing at full speed in the same car and outfit. This page summarizes what reviews describe; we'll expand it as reliable guides cover the wanted system in more detail.</p>""",
 sources=[(TK, "Kotaku: Grand Theft Auto 6 review"),
          (PSQ, "Push Square: Grand Theft Auto 6 review")],
 related=["questions/weapons.html", "money/make-money.html", "questions/cheats.html"]),

dict(es="preguntas/trofeos-logros.html", en="questions/trophies-achievements.html",
 title="GTA 6 Trophies and Achievements: How Many and the Platinum",
 h1="How many trophies and achievements does GTA 6 have?",
 desc="Sources point to 55 trophies and achievements, with a Platinum on PS5. What's known and what Rockstar hasn't confirmed.",
 chip=PART,
 answer="According to GTABase, 55 trophies on PS5 and 55 achievements on Xbox, with a Platinum called “Vice Got a Price!” Several outlets trace the count to a data leak, and we haven't found a list published by Rockstar.",
 body="""<h2>What the sources say</h2>
<ul>
<li><strong>PS5:</strong> 55 trophies: 1 Platinum, 2 Gold, 6 Silver and 46 Bronze.</li>
<li><strong>Xbox Series X|S:</strong> 55 achievements worth 1,000 Gamerscore. The PlayStation Platinum maps to a “Mythic” achievement that awards no points.</li>
<li><strong>Platinum:</strong> “Vice Got a Price!”, unlocked by earning everything else.</li>
</ul>
<p>These details come from GTABase's guide, last updated November 18, 2026. According to that guide, 28 of them are hidden.</p>
<h2>What isn't confirmed</h2>
<p>Notebookcheck and Insider Gaming reported the 55 figure as a data leak, and GTABase itself marks the exact steps for several achievements as unconfirmed. We haven't found an official list from Rockstar, so the total and names could change.</p>
<h2>Cheats and trophies</h2>
<p>Using cheats disables trophies and achievements. See <a href="cheats.html">how GTA 6 cheats unlock</a>.</p>""",
 sources=[("https://www.gtabase.com/articles/gta-6/gta-6-achievements-trophies-list-ps5-xbox-series", "GTABase: GTA 6 trophies and achievements guide (updated Nov 18, 2026)"),
          ("https://notebookcheck.net/GTA-6-leak-reveals-more-PS5-trophies-and-Xbox-achievements-on-release-date-than-GTA-5.1445073.0.html", "Notebookcheck: the trophy and achievement leak"),
          ("https://insider-gaming.com/app/post/gta-6-55-trophies-achievements-mythic-platinum", "Insider Gaming: 55 trophies and achievements")],
 related=["questions/cheats.html", "questions/how-long-to-beat.html", "questions/endings-choices.html"]),

dict(es="preguntas/armas.html", en="questions/weapons.html",
 title="GTA 6 Weapons List: Categories and Where Guns Are Stored",
 h1="What weapons are in GTA 6?",
 desc="GTABase lists 205 confirmed weapons with more to find. Weapon categories, ammo types and how to get guns back at Ammu-Nation.",
 chip=ONE,
 answer="GTABase lists 205 confirmed weapons plus 24 equipment items and 5 ammo types, and says more are still to be found. Guns you've bought can be retrieved from Ammu-Nation lockers or your personal vehicle.",
 body="""<h2>Categories</h2>
<p>GTABase's database groups weapons into assault rifles, pistols, shotguns, SMGs, melee, sniper rifles, tactical rifles, light machine guns, launchers and throwables.</p>
<p>Ammo types listed: heavy, shotgun, pistol, spear and rockets.</p>
<h2>Where your guns are stored</h2>
<ul>
<li>According to GTABase, weapons you've bought or own aren't lost for good and can be picked up from any Ammu-Nation locker or your personal vehicle.</li>
<li>Some Ammu-Nation locations carry unique regional weapons.</li>
</ul>
<h2>What's the best gun?</h2>
<p>We haven't found a reliable ranking made with the released game; the ones circulating predate launch. This is a single source, and GTABase itself says its list covers weapons known “so far.”</p>
<p>For how gunplay affects police attention, see <a href="lose-wanted-level.html">how to lose the cops</a>.</p>""",
 sources=[("https://www.gtabase.com/weapons/gta-6/", "GTABase: GTA 6 weapons database (November 2026)")],
 related=["questions/lose-wanted-level.html", "questions/cheats.html", "money/make-money.html"]),

dict(es="preguntas/cooperativo.html", en="questions/co-op.html",
 title="Does GTA 6 Have Co-op? Multiplayer Status Explained",
 h1="Does GTA 6 have co-op?",
 desc="There's no confirmed co-op for GTA 6's story. What Rockstar has said, what's rumor, and where online multiplayer stands.",
 chip=PART,
 answer="No co-op has been confirmed. Rockstar hasn't announced a co-op mode for the story, and the game launched as a single-player experience with no online mode.",
 body="""<h2>The closest thing to co-op</h2>
<p>The closest thing shown officially is switching between the two protagonists, Jason and Lucia, as the story progresses. Details in <a href="switch-characters.html">how to switch characters</a>.</p>
<h2>Rumors</h2>
<p>Some leakers have talked about a two-player campaign. Rockstar hasn't confirmed it, so we treat it as a rumor.</p>
<h2>And online?</h2>
<p>GTA 6 launched as a single-player experience and Rockstar hasn't announced an online mode or a date. See the <a href="../pc-online/gta-6-online.html">current status of GTA 6 Online</a>.</p>""",
 sources=[("https://www.svg.com/2245882/gta-6-online-multiplayer-rockstar-updates/", "SVG: What Rockstar has (and hasn't) said about GTA 6 multiplayer"),
          ("https://beebom.com/gta-6-single-player-game/", "Beebom: Is GTA 6 single-player only at launch?")],
 related=["pc-online/gta-6-online.html", "questions/switch-characters.html", "questions/play-offline.html"]),

dict(es="preguntas/misiones-capitulo-1.html", en="questions/chapter-1-missions.html",
 title="GTA 6 Chapter 1 Missions List (No Spoilers) and Missables",
 h1="What are the Chapter 1 missions in GTA 6?",
 desc="Every GTA 6 Chapter 1 mission title in order, per GTABase, with the optional missions and the two you can miss. Titles only, no story spoilers.",
 chip=PART,
 answer="GTA 6's story has a Prologue and five chapters. GTABase's launch-week list puts 27 missions in Chapter 1, from “Gone Fishing” to “Discharge Time.” Two optional missions can be missed for good.",
 body="""<h2>Prologue</h2>
<p>A single mission, also called “Prologue.”</p>
<h2>Chapter 1 story missions</h2>
<p>Titles only, in GTABase's order (it skips number 24):</p>
<ol start="2">
<li>Gone Fishing</li><li>Gear Up</li><li>Unwanted Attention</li><li>Pipework</li><li>Lab Fees</li><li>Just a Scratch</li>
<li>Get Shirley's Rum <em>(optional, missable)</em></li><li>Steal the Scooter <em>(optional, missable)</em></li>
<li>Hey Arnold!</li><li>Island Dreams</li><li>Feng Shui</li><li>Coming Home</li><li>Clean Up After Donnie</li><li>Buck Me</li>
<li>Down to Earth</li><li>Deposit Cash Into BuckMe</li><li>Save for the Future</li><li>Day Release</li><li>Clear Skies</li>
<li>Building a Life</li><li>Swamped</li><li>Don Gone</li>
</ol>
<ol start="25"><li>Recalibration</li><li>Tourist Trap</li><li>Home Sweet Home</li><li>Discharge Time</li></ol>
<h2>Optional activities</h2>
<p>GTABase also lists optional tasks in Chapter 1, not marked as missable: Pick Up Groceries, Buy Flowers, Buy Lucia a Necklace, Get The Chop, Get Lucia's Clothes, Find the Lost Drugs, Clock Out and Donnie's Lost Drugs.</p>
<h2>Which ones can you miss?</h2>
<p>GTABase flags “Get Shirley's Rum” and “Steal the Scooter” as optional and missable. Spanish outlet Vandal's guide, which also lists them, orders the chapter slightly differently, so treat the exact order as provisional. Since <a href="replay-missions.html">missions can't be replayed</a>, save first: see <a href="how-to-save.html">how to save</a>.</p>""",
 sources=[("https://www.gtabase.com/gta-6/missions/", "GTABase: GTA 6 story missions list"),
          ("https://vandal.elespanol.com/guias/guia-grand-theft-auto-vi-trucos-consejos-y-secretos/historia-y-misiones", "Vandal (Spanish): GTA 6 story and missions guide (Nov 19, 2026)")],
 related=["questions/replay-missions.html", "questions/how-to-save.html", "questions/how-long-to-beat.html"]),

# ---------------------------------------------------------------- MONEY
dict(es="dinero/ganar-dinero.html", en="money/make-money.html",
 title="How to Make Money Fast in GTA 6: Best Early-Game Methods",
 h1="How do you make money fast in GTA 6?",
 desc="The best ways to make money early in GTA 6: robbing other criminals, stealing cars for fences, Bret's hunts and the Ambrosia demolition derby.",
 chip=OK,
 answer="Early on, the best earners are robbing other criminals mid-crime, stealing cars for fences like Moses, hunting for Bret and the demolition derby at Ambrosia Raceway.",
 body="""<h2>Early-game methods</h2>
<p>Summarized from PC Gamer and GamesRadar (in-game dollars):</p>
<ul>
<li><strong>Rob other criminals mid-crime:</strong> $1,000 to $15,000. PC Gamer calls it the best advice for making money.</li>
<li><strong>Steal cars for fences</strong> (from Chapter 2): $1,000 to $20,000 depending on the model and fence. Moses usually pays one to a few thousand per car; Randy, from Chapter 3, pays more for high-end cars.</li>
<li><strong>Hunting for Bret</strong> (Chapter 2, Jason only): from hundreds to thousands per kill; PC Gamer got $2,500 for a large boar.</li>
<li><strong>Demolition derby at Ambrosia Raceway:</strong> $3,800 to $6,300 per win, and you can repeat it.</li>
<li><strong>Store robberies through the back door</strong> (from Chapter 3): the snap gun lets you pick locks and skip alarms; PC Gamer puts the take at $6,000 to $15,000.</li>
<li><strong>Pilot Pete's drops</strong> (Chapter 4): timed package drops from his plane for $10,000 to $20,000, per PC Gamer.</li>
</ul>
<h2>Other options</h2>
<ul>
<li>Mug people or hold up cashiers, and once you can afford a winch from a Mod Shop, rip out ATMs (GamesRadar).</li>
<li>Sell cars at Pay 'n' Spray (more in <a href="keep-cars-garages.html">how to keep or sell a car</a>).</li>
<li>Check the Robberies section of the map index, which shows the potential score of each target (GamesRadar).</li>
</ul>
<p>Cash in your pocket isn't safe: see <a href="buckme-bank.html">how the BuckMe bank works</a>.</p>""",
 sources=[("https://www.pcgamer.com/games/grand-theft-auto/gta-6-how-to-make-money/", "PC Gamer: GTA 6, the fastest ways to make money"),
          ("https://www.gamesradar.com/games/grand-theft-auto/gta-6-make-money-fast/", "GamesRadar: How to farm money in GTA 6 and make cash fast")],
 related=["money/buckme-bank.html", "money/keep-cars-garages.html", "questions/lose-wanted-level.html"]),

dict(es="dinero/banco-y-ahorros.html", en="money/buckme-bank.html",
 title="GTA 6 BuckMe Bank: Do You Lose Money When You Die?",
 h1="Do you lose money when you die in GTA 6?",
 desc="In GTA 6 you lose all pocket cash when Wasted or Busted. How the BuckMe checking account works and why Family Savings is a one-way trip.",
 chip=ONE,
 answer="Yes: all the cash you're carrying is lost if you're Wasted or Busted. Move it into your BuckMe checking account. And be careful: money put into Family Savings can never come back out.",
 body="""<h2>Pocket cash</h2>
<p>Jason and Lucia can each carry up to $20,000 in cash. Most businesses take it for purchases up to $1,000. If you're Wasted or Busted, you lose all of it.</p>
<h2>BuckMe checking account</h2>
<p>It unlocks during Chapter 1 and handles every purchase over $1,000. Open the BuckMe app from your phone (d-pad up). Each character has their own account, and balance limits rise as the story goes on, with upgrades flagged in Chapters 2, 3 and 4. If you hit the limit, incoming payments sit as pending until there's room.</p>
<h2>Family Savings: one-way only</h2>
<p>Family Savings is shared between Jason and Lucia and has five savings goals. Once money goes in, it can never be transferred out, though bigger balances earn more interest when the limit rises. Think before you transfer.</p>
<p>All of the above comes from GamesRadar's guide; we haven't found a second source yet.</p>""",
 sources=[("https://www.gamesradar.com/games/grand-theft-auto/gta-6-money-buckme-bank-account-manage/", "GamesRadar: How to manage money in GTA 6 and use BuckMe bank")],
 related=["money/make-money.html", "money/keep-cars-garages.html", "questions/how-to-save.html"]),

dict(es="dinero/coches-garajes.html", en="money/keep-cars-garages.html",
 title="How to Keep Stolen Cars in GTA 6: Pay 'n' Spray and Garages",
 h1="How do you keep a car in GTA 6?",
 desc="To keep a stolen car in GTA 6 you register it at a Pay 'n' Spray. You start with space for three vehicles and can buy garages.",
 chip=OK,
 answer="Register it at a Pay 'n' Spray. You start with room for only three personal vehicles; buy garages for more.",
 body="""<h2>Registering stolen cars</h2>
<p>According to German site PC Games, stolen cars can be repaired, resprayed and re-registered at a Pay 'n' Spray so you can keep them. Unregistered cars show up gray on the radar and disappear after a restart.</p>
<h2>Space</h2>
<p>You start with space for three vehicles and can buy garages to expand, per PC Games in a pre-launch article (September 8, 2026) citing a Famitsu interview with Rockstar.</p>
<h2>Getting your car delivered</h2>
<p>A quick request to Scooter Bros gets your car delivered, according to Push Square.</p>
<h2>Sell instead of keep</h2>
<p>Don't want it? Pay 'n' Spray will buy it, per GamesRadar. It's one of the ways to <a href="make-money.html">make money early</a>.</p>""",
 sources=[("https://www.pcgames.de/GTA-6-Spiel-55239/News/Garage-Diebstahl-Autos-Fahrzeuge-1553128/", "PC Games (German): garages and vehicles in GTA 6 (Sept 8, 2026)"),
          (PSQ, "Push Square: Grand Theft Auto 6 review"),
          ("https://www.gamesradar.com/games/grand-theft-auto/gta-6-make-money-fast/", "GamesRadar: How to make money in GTA 6")],
 related=["money/make-money.html", "money/fastest-car.html", "questions/buy-houses.html"]),

dict(es="dinero/coche-mas-rapido.html", en="money/fastest-car.html",
 title="Fastest Car in GTA 6: Provisional Top Speed Ranking",
 h1="What's the fastest car in GTA 6?",
 desc="GTABase hasn't finished measuring top speeds. Its provisional ranking puts the Infernus '96, Cheetah '95 and Comet '88 on top.",
 chip=ONE,
 answer="It can't be said for sure yet. GTABase, which tests cars in-game, hasn't finished its measurements; its provisional November 19 ranking puts the Pegassi Infernus '96 first, followed by the Grotti Cheetah '95 and the Pfister Comet '88.",
 body="""<h2>Provisional ranking by top speed</h2>
<ol>
<li>Pegassi Infernus '96: 7.1 out of 10</li>
<li>Grotti Cheetah '95: 6.6 out of 10</li>
<li>Pfister Comet '88: 6.1 out of 10</li>
</ol>
<p>These are scores out of 10, not mph. GTABase lists 30 cars and warns the order isn't final: it will add positions and figures as it finishes testing each car.</p>
<h2>Another ranking from the same site</h2>
<p>In its supercar list, sorted by overall stats, GTABase puts the Pfister Comet '88, the Obey 8F Drafter and the Annis Elegy '90 on top, and says it's testing every vehicle in-game. That list shows no date.</p>
<h2>How to get them</h2>
<p>GTABase still marks how to get almost every car as “coming soon,” and we haven't found a second reliable source. To hold on to a car you already have, see <a href="keep-cars-garages.html">garages and Pay 'n' Spray</a>. The Grotti Cheetah '95 is also part of the Ultimate Edition, per Rockstar (see <a href="../pc-online/price-editions.html">editions</a>).</p>""",
 sources=[("https://www.gtabase.com/articles/gta-6/gta-6-fastest-cars-ranked-list-by-top-speed", "GTABase: GTA 6 fastest cars ranked by top speed (updated Nov 19, 2026)"),
          ("https://www.gtabase.com/gta-6/vehicles/best-vehicles/", "GTABase: GTA 6 supercars by stats"),
          (RS_ED, "Rockstar Support: GTA VI editions (Ultimate Edition contents)")],
 related=["money/keep-cars-garages.html", "money/make-money.html", "pc-online/price-editions.html"]),

# ---------------------------------------------------------------- ISSUES
dict(es="problemas/no-carga-errores.html", en="issues/not-loading-fixes.html",
 title="GTA 6 Not Loading or Won't Start on PS5 or Xbox? What to Try",
 h1="GTA 6 won't load or start: what to try on PS5 and Xbox",
 desc="What to do if GTA 6 won't start: check PSN and Xbox status, update your console, free up space, and what error WS-116449-5 means.",
 chip=PART,
 answer="First check PlayStation Network or Xbox status: PSN had sign-in trouble the day before launch. Then update your console software and make sure you have enough space and the license downloaded.",
 body="""<h2>1. Check whether the service is down</h2>
<p>On November 18, roughly 1 to 3:15 p.m. ET, PlayStation Network had sign-in problems, according to Newsweek and XDA, and its status page warned of trouble launching games. Before changing anything, check:</p>
<ul>
<li><a href="https://status.playstation.com/" rel="noopener" target="_blank">PlayStation Network status</a></li>
<li><a href="https://support.xbox.com/en-US/xbox-live-status" rel="noopener" target="_blank">Xbox status</a></li>
</ul>
<p>Launch-day PSN problems have their own page: <a href="psn-down.html">PSN down at GTA 6 launch</a>.</p>
<h2>2. Update your console</h2>
<p>Make sure you're on the latest system software. On Xbox, check for console updates too.</p>
<h2>3. Check space and the download</h2>
<p>Rockstar says you need up to 212 GB free depending on your console. The physical edition has no disc: you redeem the code and download the full game. PlayStation codes are region-locked; Xbox codes aren't.</p>
<h2>4. Error WS-116449-5 on PS5</h2>
<p>PlayStation's error code list says it means the service is currently under maintenance. Wait a while, check your connection and restart your router.</p>
<h2>5. If nothing works</h2>
<p>Rockstar's <a href="https://support.rockstargames.com/VI" rel="noopener" target="_blank">GTA VI help center</a> lets you submit a request. For store or console problems, use PlayStation or Xbox support. Forbes reported updates on November 13 and 16, and no day-one patch had been announced as of November 16. See <a href="../pc-online/patch-notes-updates.html">GTA 6 patches</a>.</p>""",
 sources=[("https://www.newsweek.com/playstation-users-report-access-issues-hours-before-gta-vi-launch-12736310", "Newsweek: PlayStation users report access issues hours before GTA VI launch"),
          ("https://www.xda-developers.com/playstation-network-is-down-right-now-as-gta-6s-worldwide-launch-is-underway/", "XDA: PlayStation Network is down as GTA 6 launches"),
          ("https://www.playstation.com/en-us/support/error-codes/ps5/", "PlayStation: PS5 error codes"),
          (FORBES, "Forbes: GTA 6 release time, download size and updates (Nov 16, 2026)"),
          (RS_INST, "Rockstar Support: GTA VI installation requirements"),
          (RS_ED, "Rockstar Support: GTA VI platforms, editions and versions"),
          ("https://support.rockstargames.com/VI", "Rockstar Support: GTA VI help center")],
 related=["issues/psn-down.html", "issues/download-size.html", "pc-online/patch-notes-updates.html"]),

dict(es="problemas/tamano-descarga.html", en="issues/download-size.html",
 title="GTA 6 Download Size: Up to 212 GB on PS5 and Xbox",
 h1="How big is the GTA 6 download?",
 desc="GTA 6 needs up to 212 GB of free space. Preload dates, unlock time in the US and the pre-launch updates on PS5 and Xbox.",
 chip=VAR,
 answer="Up to 212 GB of free space, depending on your console. The game unlocked at midnight local time on November 19 on PS5 and Xbox.",
 body="""<h2>Space</h2>
<p>Rockstar says GTA 6 requires up to 212 GB of available space depending on your device. Forbes also reported updates before launch:</p>
<ul>
<li><strong>November 13:</strong> about 1 GB on PS5 and 2.2 GB on Xbox.</li>
<li><strong>November 16:</strong> about 600 MB on PS5 and 1.6 GB on Xbox.</li>
</ul>
<h2>Preload</h2>
<p>Digital preload began on November 10: at midnight local time on PS5, and globally at 12 a.m. GMT on Xbox (7 p.m. ET on November 9).</p>
<h2>Unlock time</h2>
<p>Rockstar released the game at midnight local time on November 19 in all regions, on both PS5 and Xbox Series X|S. If a store showed November 18, that's a time zone conversion.</p>
<p>No disc in the box: see <a href="physical-edition-no-disc.html">the physical edition</a>.</p>""",
 sources=[(RS_INST, "Rockstar Support: GTA VI installation requirements"),
          (RS_TIMES, "Rockstar Support: GTA VI pre-load and release times"),
          (FORBES, "Forbes: GTA 6 release time, download size and updates (Nov 16, 2026)")],
 related=["issues/physical-edition-no-disc.html", "issues/not-loading-fixes.html", "pc-online/patch-notes-updates.html"]),

dict(es="problemas/edicion-fisica-sin-disco.html", en="issues/physical-edition-no-disc.html",
 title="Does GTA 6 Physical Edition Have a Disc? No, Just a Code",
 h1="Does the GTA 6 physical edition come with a disc?",
 desc="The GTA 6 physical edition has no disc, only a download code. What that means, region locks, and what's in the box.",
 chip=OK,
 answer="No. The physical edition is a box with a download code. You still have to download the whole game.",
 body="""<p>Rockstar's support site says the physical version contains a download code and that no disc is included. It was expected in stores for shipping and pickup from November 12, and codes could be redeemed right away to preload.</p>
<h2>What that means</h2>
<ul>
<li>You need internet and up to 212 GB free.</li>
<li>Only the Standard Edition is sold physically; the Ultimate Edition is digital only, though Standard owners can buy the Ultimate upgrade.</li>
<li>Physical pre-orders included the Vintage Vice City Pack.</li>
<li>PlayStation codes are region-locked to your account's region; Xbox codes aren't.</li>
</ul>
<h2>Buying it as a gift?</h2>
<p>If it's for someone whose PlayStation account is registered in another country, check the code's region first. Xbox doesn't have that problem.</p>""",
 sources=[(RS_ED, "Rockstar Support: GTA VI platforms, editions and versions (updated Nov 18, 2026)"),
          (RS_INST, "Rockstar Support: GTA VI installation requirements")],
 related=["issues/download-size.html", "pc-online/price-editions.html", "questions/play-offline.html"]),

dict(es="problemas/ps5-pro-ps5-xbox.html", en="issues/ps5-pro-vs-ps5-vs-xbox.html",
 title="GTA 6 PS5 Pro vs PS5 vs Xbox Series X|S: Which Runs It Best?",
 h1="GTA 6 on PS5 Pro vs PS5 vs Xbox: where does it look best?",
 desc="GTA 6 runs at 30fps on every console. Resolution and stability differences between PS5 Pro, PS5, Series X and Series S.",
 chip=OK,
 answer="It targets 30fps on every console, with no performance mode. Digital Foundry rates PS5 Pro as the best option and Series S as the hardest to recommend.",
 body="""<h2>What's confirmed</h2>
<ul>
<li>Rockstar says the game targets 30 frames per second (Kotaku).</li>
<li>There's no 40fps mode on any console, PS5 Pro included (Vandal).</li>
<li>On PS5 Pro, the game uses PSSR upscaling and ray tracing (Kotaku).</li>
</ul>
<h2>What Digital Foundry measured</h2>
<p>As summarized by AltChar and Pure Xbox:</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Table (scroll for more)"><table><thead><tr><th>Console</th><th>Image</th><th>Stability</th></tr></thead><tbody>
<tr><td>PS5 Pro</td><td>Upscaled from 1440p with PSSR; looks like native 4K</td><td>Near-perfect 30fps</td></tr>
<tr><td>PS5</td><td>1440p internal, upscaled</td><td>Dips to 23fps in explosions</td></tr>
<tr><td>Xbox Series X</td><td>Similar to PS5</td><td>Dips in chases and explosions</td></tr>
<tr><td>Xbox Series S</td><td>720p internal, upscaled to 1080p</td><td>Often 25 to 30fps, with drops to 20</td></tr>
</tbody></table></div>
<p>Digital Foundry calls Series S the hardest version to recommend. On Xbox One, see <a href="ps4-xbox-one.html">cloud play</a>.</p>
<h2>Is a PS5 Pro worth it just for this?</h2>
<p>You gain sharpness and stability, not frame rate: the target is still 30. If you already own a PS5 or Series X, the game holds up well.</p>""",
 sources=[("https://kotaku.com/gta-6-30-fps-confirmed-ps5-pro-pssr-xbox-cloud-streaming-2000755517", "Kotaku: GTA 6 targets 30fps, PS5 Pro PSSR and Xbox Cloud (Nov 10, 2026)"),
          ("https://www.altchar.com/game-news/gta-vi-dips-as-low-as-23fps-on-base-ps5-in-heavy-action-digital-foundry-finds-aJybE7x7IsZa", "AltChar: Digital Foundry's PS5 analysis"),
          ("https://www.purexbox.com/news/2026/11/three-big-takeaways-from-digital-foundrys-gta-6-analysis-for-xbox-series-xs", "Pure Xbox: Digital Foundry on Xbox Series X|S"),
          (VANDAL_LIVE, "Vandal (Spanish): GTA 6 launch live coverage")],
 related=["issues/ps4-xbox-one.html", "issues/download-size.html", "pc-online/gta-6-pc.html"]),

dict(es="problemas/xbox-one-ps4.html", en="issues/ps4-xbox-one.html",
 title="Can You Play GTA 6 on PS4 or Xbox One? Cloud Gaming Explained",
 h1="Can you play GTA 6 on PS4 or Xbox One?",
 desc="GTA 6 has no PS4 or Xbox One version. Xbox One owners can stream it with Xbox Cloud Gaming; PS4 has no option.",
 chip=OK,
 answer="There's no PS4 or Xbox One version. On Xbox One you can stream it through Xbox Cloud Gaming; on PS4 there's no option.",
 body="""<h2>Official platforms</h2>
<p>GTA 6 is out only on PS5 and Xbox Series X|S, as Rockstar's launch announcement says.</p>
<h2>Xbox One: through the cloud</h2>
<p>Rockstar's support site confirms GTA 6 is available through Xbox Cloud Gaming on Xbox Series X|S and Xbox One consoles, using Series S graphics settings. Rockstar only mentions Xbox consoles, not PC or phones, and warns that connection speed can affect performance.</p>
<p>Rockstar doesn't spell out which subscription or purchase is required, and the Xbox Store listing only says “Cloud Gaming on Xbox consoles.” Check on your console before paying.</p>
<h2>PS4</h2>
<p>There's no PS4 version and no cloud option for PS4. Rockstar says the game supports Remote Play, but Remote Play streams from a PS5 you own, so it doesn't help if you only have a PS4.</p>""",
 sources=[(RS_ED, "Rockstar Support: GTA VI platforms, editions and versions"),
          (NW_LAUNCH, "Rockstar Newswire: Grand Theft Auto VI Now Available (Nov 19, 2026)"),
          ("https://kotaku.com/gta-6-30-fps-confirmed-ps5-pro-pssr-xbox-cloud-streaming-2000755517", "Kotaku: 30fps, PSSR and Xbox Cloud")],
 related=["issues/ps5-pro-vs-ps5-vs-xbox.html", "pc-online/gta-6-pc.html", "issues/download-size.html"]),

dict(es="problemas/psn-caido-inicio-sesion.html", en="issues/psn-down.html",
 title="Is PSN Down for GTA 6? Launch-Day Sign-In Problems Explained",
 h1="Was PSN down at GTA 6 launch? What we know about the sign-in problems",
 desc="Thousands of PSN sign-in and connection reports on GTA 6 launch day. What sources say, what isn't confirmed and what to try.",
 chip=PART,
 answer="On launch day there were thousands of reports of PlayStation Network sign-in and connection problems. Sony hasn't given a cause or linked it to GTA 6, and neither Rockstar nor Microsoft has commented.",
 body="""<h2>What we know</h2>
<ul>
<li><strong>Reports:</strong> on November 19, Downdetector showed spikes of thousands of reports. IBTimes and Digit give different numbers, so we don't quote one.</li>
<li><strong>Symptoms:</strong> sign-in and server connection problems. According to Digit, people trying to sign in saw a “services are busy” message.</li>
<li><strong>Sony's status page:</strong> according to Endgame Tools, it reported degraded gaming and social features in more than 60 countries from 05:33 to 06:04 UTC, and showed no incidents by 11:40 UTC.</li>
</ul>
<h2>What isn't confirmed</h2>
<p>The cause. Digit suggests GTA 6 demand may be behind it, but IBTimes says there's no evidence linking the two. Sony hadn't commented in the sources we checked. These figures and times are from launch day; things may have changed.</p>
<h2>What to try</h2>
<p>These are press recommendations, not official advice: restart your console, install any update the game asks for and wait a while before retrying. Check PlayStation's status page first. Endgame Tools adds that on PS5 the game may be waiting for system software version 26.07-14.23.00; that's a single source, so check your console.</p>
<p>If the game itself won't start, see <a href="not-loading-fixes.html">GTA 6 won't load</a>.</p>""",
 sources=[("https://www.ibtimes.co.uk/gta-vi-launch-psn-login-connection-problems-1833330", "IBTimes UK: PSN sign-in problems on GTA VI launch day (Nov 19, 2026)"),
          ("https://www.digit.in/news/general/playstation-network-down-thousands-of-users-report-login-issues-amid-gta-6-launch.html", "Digit: PSN down, thousands report sign-in issues (Nov 19, 2026)"),
          ("https://endgametools.com/en/gta-6/news/gta-6-launch-day", "Endgame Tools: GTA 6 launch day servers, known issues and updates (Nov 19, 2026)")],
 related=["issues/not-loading-fixes.html", "issues/download-size.html", "questions/play-offline.html"]),

# ---------------------------------------------------------------- PC & ONLINE
dict(es="novedades/gta-6-online.html", en="pc-online/gta-6-online.html",
 title="Does GTA 6 Have Online? Not at Launch — What We Know",
 h1="Does GTA 6 have an online mode?",
 desc="GTA 6 launched without online multiplayer. What Rockstar and Take-Two have said, what happens to GTA Online, and why a 2027 date is a rumor.",
 chip=OK,
 answer="No. GTA 6 launched as a single-player experience and Rockstar hasn't announced an online mode or a date.",
 body="""<h2>What's confirmed</h2>
<ul>
<li>Take-Two's official pre-order announcement (June 24, 2026) says: “Grand Theft Auto VI features a single-player experience.”</li>
<li>The PlayStation Store describes GTA 6 as a single-player experience.</li>
<li>Rockstar hasn't mentioned any online mode, Push Square noted on November 13, 2026.</li>
<li>GTA Online (the GTA V one) carries on: Take-Two CEO Strauss Zelnick said in May 2026 that it will remain on sale.</li>
</ul>
<h2>What's rumor</h2>
<p>The most specific claim is unofficial: in September 2026, Twitch CEO Dan Clancy told Bloomberg that multiplayer would launch “next year,” meaning 2027, as reported by VGC. Rockstar hasn't confirmed it.</p>
<h2>Change log</h2>
<p>Nov 20, 2026: added Take-Two's official single-player statement. Nov 19, 2026: the game launches without online.</p>
<p>We'll update this page when there's an official announcement.</p>""",
 sources=[("https://ir.take2games.com/node/32311", "Take-Two: Rockstar Games announces Grand Theft Auto VI pre-orders (June 24, 2026)"),
          ("https://www.videogameschronicle.com/news/twitch-ceo-says-grand-theft-auto-6s-multiplayer-mode-will-launch-next-year/", "VGC: Twitch CEO says GTA 6 multiplayer will launch next year"),
          ("https://www.pushsquare.com/news/2026/11/psa-gta-6-does-not-have-online-multiplayer-at-launch", "Push Square: GTA 6 doesn't have online multiplayer at launch"),
          ("https://wccftech.com/gta-6-november-19-date-holds-take-two-beats-earnings-zelnick-pc-port/", "Wccftech: Take-Two holds the date; Zelnick on PC"),
          ("https://store.playstation.com/es-es/product/EP1004-PPSA01547_00-GTAVISTANDARD001/", "PlayStation Store listing for GTA VI (Spain)")],
 related=["questions/co-op.html", "pc-online/gta-6-pc.html", "pc-online/gta-plus.html"]),

dict(es="novedades/gta-6-pc.html", en="pc-online/gta-6-pc.html",
 title="GTA 6 PC Release Date: What Take-Two Has Said and Past Precedent",
 h1="When is GTA 6 coming to PC?",
 desc="GTA 6 has no announced PC version. What Take-Two has said, and how long GTA IV, GTA V and Red Dead Redemption 2 took to reach PC.",
 chip=OK,
 answer="There's no date or announcement. Take-Two has only said the game is announced for consoles and that its big titles tend to reach every platform eventually.",
 body="""<h2>What Take-Two has said</h2>
<p>In May 2026, Strauss Zelnick explained that Rockstar had only announced GTA 6 for consoles. He also said PC is a big market and that most of the company's hits end up on all platforms over time.</p>
<h2>What the launch announcements say</h2>
<p>Take-Two's November 19, 2026 release and Rockstar's Newswire both announce the game for PlayStation 5 and Xbox Series X|S only, with no mention of PC.</p>
<h2>Precedent</h2>
<ul>
<li><strong>GTA IV:</strong> reached PC about seven months after consoles (April and December 2008).</li>
<li><strong>GTA V:</strong> about 19 months later.</li>
<li><strong>Red Dead Redemption 2:</strong> October 2018 on consoles, PC on November 5, 2019, about a year later.</li>
</ul>
<p>That isn't a prediction, just how Rockstar has handled it before.</p>
<h2>Watch out for scams</h2>
<p>There is no PC version. Any download claiming otherwise is fake and may contain malware.</p>
<h2>Change log</h2>
<p>Nov 20, 2026: added Take-Two's official availability release, which names only PS5 and Xbox Series X|S. Nov 19, 2026: the game launches on PS5 and Xbox Series only.</p>
<p>Meanwhile, see <a href="../issues/ps5-pro-vs-ps5-vs-xbox.html">which console runs it best</a>.</p>""",
 sources=[("https://www.take2games.com/ir/news/rockstar-games-announces-grand-theft-auto-vi-now-available", "Take-Two: Rockstar Games announces Grand Theft Auto VI is now available (Nov 19, 2026)"),
          (NW_LAUNCH, "Rockstar Newswire: Grand Theft Auto VI Now Available (Nov 19, 2026)"),
          ("https://wccftech.com/gta-6-november-19-date-holds-take-two-beats-earnings-zelnick-pc-port/", "Wccftech: Take-Two holds the date; Zelnick on PC"),
          ("https://www.digitalcitizen.life/gta-6-keeps-november-19-release-date-as-take-two-stays-quiet-on-pc-version/", "Digital Citizen: Take-Two stays quiet on a PC version"),
          ("https://www.gamespot.com/articles/red-dead-redemption-2-coming-to-pc-google-stadia-s/1100-6470338", "GameSpot: Red Dead Redemption 2 is coming to PC")],
 related=["pc-online/mods.html", "pc-online/gta-6-online.html", "issues/ps5-pro-vs-ps5-vs-xbox.html"]),

dict(es="novedades/precio-ediciones.html", en="pc-online/price-editions.html",
 title="GTA 6 Price: Standard $79.99 vs Ultimate Edition $99.99",
 h1="How much is GTA 6? Standard vs Ultimate Edition",
 desc="GTA 6 costs $79.99 for the Standard Edition and $99.99 for the Ultimate Edition. What Ultimate adds, the physical copy and pre-order bonuses.",
 chip=OK,
 answer="In the US, the Standard Edition is $79.99 and the Ultimate Edition is $99.99, according to Take-Two's pre-order announcement.",
 body="""<h2>Editions</h2>
<ul>
<li><strong>Standard ($79.99):</strong> the game. Sold digitally and as a physical box with a download code (no disc).</li>
<li><strong>Ultimate ($99.99):</strong> digital only. Standard owners can buy the Ultimate Edition Upgrade separately at any time.</li>
</ul>
<h2>What the Ultimate Edition adds</h2>
<p>Rockstar lists, among other items: the '95 Grotti Cheetah, the Hawk &amp; Little Morgan revolvers, personalized weapon variants, Jason's safehouse vehicles, the '67 Vapid Dominator Buggy, the Shitzu Squalo speedboat, the Rideout Customs and One-Eyed Willie's mod shops, Sara's Unisex Salon, the Stock 305 clothing store, the Electric Fang tattoo parlor, the PTT Youngin$ compound and a classic car collection. Rockstar says the bonuses are spread across the story, with new items in each chapter.</p>
<h2>Pre-order bonuses</h2>
<p>Digital purchases before November 20, 2026 included the Vintage Vice City Pack ('55 Vapid Stanier sedan and garage, outfits and hairstyles, an exclusive weapon pattern) and a month of GTA+. Physical pre-orders included the Vintage Vice City Pack but not GTA+. Rockstar's launch post called November 19 the last day.</p>
<h2>Rating</h2>
<p>Rockstar's posts list these content descriptors: Blood and Gore, Intense Violence, Mature Humor, Nudity, Strong Language, Strong Sexual Content, Use of Drugs and Alcohol, plus In-Game Purchases. In Europe it's rated PEGI 18.</p>
<p>Prices can change with sales. Always check the current price in the store.</p>""",
 sources=[("https://ir.take2games.com/node/32311", "Take-Two: Grand Theft Auto VI pre-orders announcement (June 24, 2026)"),
          (RS_ED, "Rockstar Support: GTA VI platforms, editions and versions"),
          (NW_LAUNCH, "Rockstar Newswire: Grand Theft Auto VI Now Available (Nov 19, 2026)"),
          ("https://store.playstation.com/es-es/product/EP1004-PPSA01547_00-GTAVISTANDARD001/", "PlayStation Store listing for GTA VI (Spain, PEGI rating)")],
 related=["pc-online/gta-plus.html", "issues/physical-edition-no-disc.html", "money/fastest-car.html"]),

dict(es="novedades/gta-plus.html", en="pc-online/gta-plus.html",
 title="GTA+ in GTA 6: What the Membership Includes",
 h1="What does GTA+ include in GTA 6?",
 desc="What the GTA+ membership gives you in GTA 6: an exclusive Elegy, a Crosstown garage, Scooter Bros Premium, free transit and discounts.",
 chip=OK,
 answer="Rockstar confirmed GTA+ now includes GTA 6 bonuses. According to Vandal's launch coverage, they include an exclusive Elegy, a Crosstown garage with an armory, Scooter Bros Premium, free public transit and 10% off vehicle sales.",
 body="""<h2>Member benefits, per Vandal</h2>
<ul>
<li>An exclusive '90 Annis Elegy with custom bodywork.</li>
<li>A Crosstown garage with an armory and a place to sell stolen goods directly.</li>
<li>Scooter Bros Premium.</li>
<li>Free rides on Leonida's public transit.</li>
<li>10% on vehicle sales, plus similar discounts at several Leonida stores (Vandal doesn't say which).</li>
</ul>
<p>Rockstar's November 19 launch post confirms GTA+ “now contains GTAVI bonuses for Members” but doesn't list them, so the details above rely on Vandal.</p>
<h2>The free month with purchase</h2>
<p>According to Rockstar, digital purchases before November 20, 2026 included one month of GTA+. On Xbox, the store listing we checked gives 180 days from the pre-order to redeem it. After that it renews as a paid membership, so check auto-renewal in your account if you don't want to keep it.</p>
<h2>Is it worth it?</h2>
<p>You don't need it for the story. It saves time with the garage and getting around. If you're unsure, start without it and see <a href="../money/make-money.html">how to make money early</a>.</p>""",
 sources=[(NW_LAUNCH, "Rockstar Newswire: Grand Theft Auto VI Now Available (Nov 19, 2026)"),
          (RS_ED, "Rockstar Support: GTA VI platforms, editions and versions"),
          (VANDAL_LIVE, "Vandal (Spanish): GTA 6 launch live coverage, GTA+ details"),
          ("https://www.xbox.com/es-es/games/store/grand-theft-auto-vi/9p3h4968grsm", "Xbox Store listing for GTA VI (Spain)")],
 related=["pc-online/price-editions.html", "questions/buy-houses.html", "money/make-money.html"]),

dict(es="novedades/actualizaciones-parches.html", en="pc-online/patch-notes-updates.html",
 title="GTA 6 Patch Notes: What We Know About Update 1.002",
 h1="Are there GTA 6 patches? What we know about update 1.002",
 desc="Update 1.002.000 arrived before launch. Its size on PS5 and Xbox, whether it's mandatory, and why nobody knows what it changes.",
 chip=PART,
 answer="Yes. Update 1.002.000 arrived before launch, marked as mandatory on PS5 (about 1.07 GB) and about 2.18 GB on Xbox. Rockstar hasn't published patch notes, so what it changes is unknown.",
 body="""<h2>What we know</h2>
<ul>
<li><strong>Version:</strong> 1.002.000, cited for PS5.</li>
<li><strong>Size:</strong> about 1.07 GB on PS5 and about 2.18 GB on Xbox Series X|S.</li>
<li><strong>Mandatory:</strong> KeenGamer calls it a mandatory download, and it's flagged as such on PS5.</li>
<li><strong>Patch notes:</strong> Rockstar hasn't published any or confirmed it as a “day-one patch.”</li>
</ul>
<h2>Other updates</h2>
<p>Gaming press reported a later update, 01.002.001, in mid-November, smaller on PS5. Its changes aren't known either. If you see detailed “fix lists,” be skeptical: they're guesses, not Rockstar's notes.</p>
<h2>What to do</h2>
<p>Install pending updates before you play. If the game won't start, see <a href="../issues/not-loading-fixes.html">GTA 6 won't load</a>, and for space, <a href="../issues/download-size.html">GTA 6 download size</a>.</p>""",
 sources=[("https://www.keengamer.com/articles/news/gta-6-update-1-002-starts-rolling-out-on-ps5-and-xbox-ahead-of-launch/", "KeenGamer: GTA 6 update 1.002 rolls out on PS5 and Xbox (Nov 13, 2026)"),
          ("https://mp1st.com/?p=318409", "MP1st: GTA 6 update 1.002"),
          ("https://www.ggrecon.com/articles/gta-6-update-1-002-before-launch/", "GGRecon: GTA 6 gets a 1 GB update before launch"),
          ("https://beatcopgame.com/gta-6-patch-notes-and-updates-tracker/", "BeatCop: GTA 6 patch notes tracker")],
 related=["issues/download-size.html", "issues/not-loading-fixes.html", "pc-online/gta-6-online.html"]),

dict(es="novedades/mods.html", en="pc-online/mods.html",
 title="Will GTA 6 Have Mods? Rockstar's Mod Rules Explained",
 h1="Will GTA 6 have mods? What Rockstar's rules say",
 desc="Rockstar published mod guidelines for all its games. What they allow, what they restrict and why no official GTA 6 mod tools exist.",
 chip=PART,
 answer="Rockstar has published mod guidelines for all of its games, GTA 6 included: they tolerate single-player, offline, non-commercial mods and restrict expanding the story, porting games or mixing titles. There's no PC version or official mod tools announced.",
 body="""<h2>What's allowed</h2>
<p>According to press coverage, the guidelines accept single-player, offline, non-commercial projects that respect third-party intellectual property. Take-Two has said that, in general, it doesn't take legal action against that kind of project in its PC games.</p>
<h2>What's restricted</h2>
<ul>
<li>Expanding or replacing official missions and story.</li>
<li>Unofficial ports and mash-ups between games in the series.</li>
<li>Paid and multiplayer mods, which are steered toward the official creator platform built on FiveM.</li>
</ul>
<h2>And GTA 6?</h2>
<p>The guidelines are company-wide and aren't an announcement of mod tools for GTA 6. The game is only on PS5 and Xbox Series X|S; for PC, see <a href="gta-6-pc.html">when GTA 6 is coming to PC</a>. We haven't found a Rockstar text specific to GTA 6 mods.</p>""",
 sources=[("https://www.invenglobal.com/articles/26384/no-exception-for-gta-6-rockstar-releases-mod-guidelines-across-all-titles", "Inven Global: No exception for GTA 6, Rockstar releases mod guidelines across all titles"),
          ("https://games.gg/news/rockstar-tightens-mod-rules-gta-6/", "games.gg: Rockstar tightens mod rules"),
          ("https://www.pcgamer.com/au/rockstar-is-talking-with-openiv-developer-issues-new-statement-on-mods", "PC Gamer: Rockstar talks with the OpenIV developer, issues new statement on mods")],
 related=["pc-online/gta-6-pc.html", "questions/cheats.html", "pc-online/gta-6-online.html"]),

# ---------------------------------------------------------------- LEONIDA
dict(es="lugares/protagonistas.html", en="leonida/characters.html",
 title="Jason Duval and Lucia Caminos: Who Are GTA 6's Protagonists?",
 h1="Who are Jason and Lucia, GTA 6's protagonists?",
 desc="Who Jason Duval and Lucia Caminos are according to Rockstar, and the other official characters in GTA 6.",
 chip=OK,
 answer="Jason Duval is a military veteran doing jobs for drug runners in the Keys; Lucia Caminos is fresh out of prison. Together they try to get ahead in Leonida.",
 body="""<h2>Jason Duval</h2>
<ul>
<li><strong>Background:</strong> grew up around grifters and crooks.</li>
<li><strong>Past:</strong> served in the military.</li>
<li><strong>Now:</strong> lives in the Leonida Keys, working for local drug runners.</li>
<li><strong>What he wants:</strong> a quiet life, which he never gets.</li>
</ul>
<p>Rockstar frames meeting Lucia as a turn that could be the best or worst thing to happen to him.</p>
<h2>Lucia Caminos</h2>
<ul>
<li><strong>Background:</strong> her family is from Liberty City; her father taught her to fight as a kid.</li>
<li><strong>Past:</strong> ended up in prison in Leonida for protecting her family, and got out by sheer luck.</li>
<li><strong>What she wants:</strong> the better life she and her mother hoped for. She sees a way out in Jason.</li>
</ul>
<p>How they get along during the game partly depends on you: see <a href="../questions/endings-choices.html">endings and choices</a>.</p>
<h2>Other official characters</h2>
<p>Rockstar also introduces Cal Hampton, Boobie Ike, Dre'Quan Priest, Real Dimez, Raul Bautista and Brian Heder.</p>""",
 sources=[("https://www.rockstargames.com/VI/only-in-leonida", "Rockstar Games: Only in Leonida (official site)"),
          ("https://www.gamesradar.com/games/grand-theft-auto/gta-6s-lucia-and-jason-get-full-names-and-backstories-as-trailer-2-drops-and-rockstar-shares-loads-more-details-about-its-protagonists", "GamesRadar: Lucia and Jason get full names and backstories")],
 related=["leonida/map-leonida.html", "questions/switch-characters.html", "questions/endings-choices.html"]),

dict(es="lugares/mapa-leonida.html", en="leonida/map-leonida.html",
 title="GTA 6 Map: The Six Regions of Leonida and Vice City",
 h1="What is the GTA 6 map like? The regions of Leonida",
 desc="GTA 6 is set in Leonida, a fictional state inspired by Florida. Its six official regions and the real places the press compares them to.",
 chip=OK,
 answer="GTA 6 is set in Leonida, a fictional state inspired by Florida. Rockstar presents six regions: Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia and Mount Kalaga.",
 body="""<h2>The six official regions</h2>
<p>Rockstar's descriptions, as reported by Game Informer in May 2025, summarized:</p>
<ul>
<li><strong>Vice City:</strong> the big city, where luxury, hustle and greed come together.</li>
<li><strong>Leonida Keys:</strong> islands with dangerous waters.</li>
<li><strong>Grassrivers:</strong> wetlands with predators deadlier than gators.</li>
<li><strong>Port Gellhorn:</strong> parking lots fueled by cheap beer, painkillers and gas-station energy drinks.</li>
<li><strong>Ambrosia:</strong> the heartland of Leonida, with old-fashioned values.</li>
<li><strong>Mount Kalaga:</strong> a national park for hunting, fishing and off-roading.</li>
</ul>
<h2>What the official map shows</h2>
<p>The map poster Rockstar published on the official GTA VI site divides Leonida into five counties: Lummox, Kelly, Leonard, Vice-Dale and Mariana. According to that map:</p>
<ul>
<li><strong>Vice City</strong> sits on the east coast in Vice-Dale County, with Vice Beach across the bay.</li>
<li><strong>Port Gellhorn</strong> is on the west coast.</li>
<li><strong>Ambrosia</strong> is in the middle of the state.</li>
<li><strong>Mount Kalaga National Park</strong> covers the north, in Lummox County.</li>
<li><strong>Grassrivers</strong> lies to the south, between Kelly and Mariana counties.</li>
<li><strong>Leonida Keys</strong>: the island chain to the south, including Key Lento.</li>
</ul>
<h2>Is Vice City Miami?</h2>
<p>Rockstar never names Florida. Outlets such as PC Gamer compare Vice City to Miami, the Leonida Keys to the Florida Keys and Grassrivers to the Everglades, but those are the press's comparisons. We haven't found reliable equivalents for Port Gellhorn, Ambrosia or Mount Kalaga.</p>
<p>GTA 6's Vice City is set in the present day, not the 1980s of 2002's Vice City. Want to know who lives here? Meet the <a href="characters.html">protagonists</a>.</p>""",
 sources=[("https://www.rockstargames.com/VI/only-in-leonida", "Rockstar Games: Only in Leonida (official site)"),
          ("https://www.rockstargames.com/VI/media", "Rockstar Games: official Leonida map poster (Media & Artwork)"),
          ("https://gameinformer.com/2025/05/06/rockstar-shows-off-six-major-areas-of-vice-city-in-grand-theft-auto-vi", "Game Informer: Rockstar shows off six major areas in GTA VI"),
          ("https://www.pcgamer.com/games/grand-theft-auto/gta6-map", "PC Gamer: GTA 6 map")],
 related=["leonida/characters.html", "leonida/radio-stations.html", "money/fastest-car.html"]),

dict(es="lugares/emisoras-radio.html", en="leonida/radio-stations.html",
 title="GTA 6 Radio Stations: The Six Rockstar Has Revealed",
 h1="What radio stations are in GTA 6?",
 desc="Rockstar revealed six GTA 6 radio stations on October 8, 2026. Genres, hosts, podcasts and what's still unconfirmed.",
 chip=PART,
 answer="Rockstar has officially revealed six stations: Flash FM, Cocoteo FM, Back Country Radio, AfroBank FM, The Chamber 106.6 and Dirty South Classics. The full lineup hasn't been confirmed.",
 body="""<h2>The six revealed stations</h2>
<p>Announced on Rockstar Newswire on October 8, 2026:</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Table (scroll for more)"><table><thead><tr><th>Station</th><th>Genre</th><th>Hosts</th></tr></thead><tbody>
<tr><td>Flash FM</td><td>Pop</td><td>Robyn and Alex</td></tr>
<tr><td>Cocoteo FM</td><td>Modern Latin</td><td>El Martillo and La Gata</td></tr>
<tr><td>Back Country Radio</td><td>Country</td><td>MW and Delta Dawne</td></tr>
<tr><td>AfroBank FM</td><td>African music</td><td>Burna and Palmsy</td></tr>
<tr><td>The Chamber 106.6</td><td>Metal</td><td>DJ Kerry and DJ Tom</td></tr>
<tr><td>Dirty South Classics</td><td>Southern rap and hip-hop</td><td>Trick and Trina</td></tr>
</tbody></table></div>
<p>Rockstar also says GTA 6 adds on-demand podcasts for the first time, playable in vehicles or on foot through in-game headphones and earbuds, and that <em>Grand Theft Auto VI: The Album</em> has 34 original tracks.</p>
<h2>What isn't confirmed</h2>
<p>Lists of more than 20 stations come from leaks. GTABase's database lists 21, but it says the full soundtrack and per-station tracklists haven't been officially revealed, and it doesn't separate confirmed names from leaked ones. So we don't count the rest until a reliable source confirms them.</p>""",
 sources=[("https://www.rockstargames.com/newswire/article/o3982oa93a23k4/the-music-of-grand-theft-auto-vi-in-game-radio-stations", "Rockstar Newswire: The Music of Grand Theft Auto VI, In-Game Radio Stations (Oct 8, 2026)"),
          ("https://www.gtabase.com/gta-6/radio-stations/", "GTABase: GTA 6 radio stations (checked Nov 20, 2026; undated)"),
          ("https://www.dexerto.com/gta/gta-6-radio-stations-revealed-and-you-can-listen-to-them-now-3417185/", "Dexerto: GTA 6 radio stations revealed"),
          ("https://shacknews.com/article/150944/gta-6-radio-stations", "Shacknews: GTA 6 radio stations")],
 related=["leonida/map-leonida.html", "leonida/characters.html", "pc-online/price-editions.html"]),
]

# ---------------------------------------------------------------- actualización 20/11/2026 (tarde)
import trucos_datos as _T

_A = {a["en"]: a for a in ARTICULOS}

_A["questions/cheats.html"].update(
 title="GTA 6 Cheats for PS5 and Xbox: All Codes and How to Unlock Them",
 h1="Does GTA 6 have cheats? All codes and how to unlock them",
 desc=f"All 61 GTA 6 cheats with their unlock requirements, plus the {_T.CONOCIDOS} codes found so far for PS5 and Xbox: money, infinite ammo, body armor and more.",
 chip=PART,
 answer=f"Yes, 61 of them, with the same codes on PS5 and Xbox. They only work after you beat the story and meet each cheat's own requirement. As of November 20, {_T.CONOCIDOS} codes are known; all 61 cheats and their requirements are below.",
 body=f"""<p>This is the big change from earlier GTA games: cheats aren't available from the start. PowerPyx, Red Bull and Vandal agree that they unlock after you complete the main story and that each one also has its own requirement, listed under Progress &gt; Cheats. Enter a code before that and nothing happens.</p>
<p>According to Red Bull, the game counts what you've already done during the story, so some cheats may be ready the moment the credits roll. It pays to work on the requirements as you play.</p>
<h2>How to enter a cheat</h2>
<ol>
<li>Press up on the d-pad to pull out your phone.</li>
<li>Hold L1 and press R1 (on Xbox, hold LB and press RB).</li>
<li>Enter the cheat's d-pad sequence.</li>
</ol>
<p>Codes only use the d-pad, so they're identical on PS5 and Xbox. Several look alike (the ammo cheats share an opening, and vehicle spawns all start with ← ↑ → ↓): one wrong press gets you a different cheat or none.</p>
<h2>What you give up</h2>
<ul>
<li>Trophies and achievements are disabled.</li>
<li>Saving is disabled until you quit and reload (see <a href="how-to-save.html">how to save</a>). Save before you use them.</li>
</ul>
<h2>All 61 cheats and how to unlock each one</h2>
<p>There are 10 player cheats, 11 combat cheats, 21 vehicle spawns, 3 environment cheats and 16 screen filters. All three guides agree on the requirements; as of November 20, {_T.CONOCIDOS} codes are known. Unless noted, a code appears in all three. “Not found yet” means the requirement is official but nobody has published the sequence.</p>
{_T.tablas("en")}
<h2>Watch out for fake lists</h2>
<ul>
<li><strong>There are no phone-number cheats.</strong> Red Bull says “GTA 6 cheat phone numbers” lists are GTA V codes with a new label; they don't work in GTA 6.</li>
<li><strong>Safe combinations aren't cheats and aren't fixed.</strong> GameSpot says they're randomized per playthrough, even if you rob the same store twice, so online “safe code” lists won't help. See how to find them in <a href="../money/make-money.html">how to make money</a>.</li>
</ul>
<p>We'll add the missing codes as reliable sources publish them.</p>""",
 sources=[("https://www.powerpyx.com/gta-6-all-cheats/", "PowerPyx: All GTA 6 cheats (Nov 18, 2026)"),
          ("https://www.redbull.com/int-en/gta-6-cheat-codes", "Red Bull: GTA 6 cheats, all the codes and how to unlock them (Nov 18, 2026)"),
          ("https://vandal.elespanol.com/guias/guia-grand-theft-auto-vi-trucos-consejos-y-secretos/trucos", "Vandal (Spanish): GTA 6 cheats (Nov 20, 2026)"),
          ("https://www.gamespot.com/articles/gta-6-safe-codes-and-robberies-guide/", "GameSpot: GTA 6 safe codes and robberies guide (Nov 18, 2026)")])

_RADIO = [
 ("Flash FM", "Pop", "Robyn and Alex Consani", True), ("Emotion 98.3", "Soft rock (back from 2002's Vice City)", "—", False),
 ("Vice City FM", "'80s pop", "“Weird Al” Yankovic and Brigitte Nielsen", False), ("Stockyard FM", "Indie and dance", "PinkPantheress and The Dare", False),
 ("Dirty South Classics", "Southern rap", "Trick Daddy and Trina", True), ("VCRR", "Modern rap", "JT and DJ Stevie J", False),
 ("Honey FM", "'90s R&amp;B and soul", "Chilli and T-Boz", False), ("Cocoteo FM", "Modern Latin: reggaeton, dembow, bachata", "Bad Bunny (El Martillo) and RaiNao (La Gata)", True),
 ("Radio La Ola", "Latin classics", "Gloria and Emilio Estefan", False), ("Radio On-U", "Laid-back rock", "—", False),
 ("V-Rock", "Classic rock", "Lindsey Buckingham and Michael McDonald", False), ("The Chamber 106.6", "Metal", "Kerry King and Tom Araya", True),
 ("Back Country Radio", "Country", "Morgan Wallen (MW) and Delta Dawne", True), ("Gloriana Blues Radio", "Blues", "Keith Richards and Buddy Guy", False),
 ("Leonida Jazz Radio", "'70s jazz fusion", "—", False), ("Symphony FM", "Classical", "Yuja Wang", False),
 ("Worldwide FM", "World music and jazz (back from GTA V)", "Gilles Peterson", False), ("CircoLoco Records Radio", "Club music", "Seth Troxler and Antonio Carbonaro", False),
 ("AfroBank FM", "African music", "Burna Boy and Palms Trax", True), ("Kaleidoscope FM", "Covers, global pop, Finnish disco", "Jeremy Irons", False),
 ("WKTT", "Talk radio (back from GTA IV)", "Stavros Halkias", False), ("The Wipe", "Talk show about Leonida's oddities", "—", False)]
_rows = "".join(f"<tr><td>{n}{' ★' if o else ''}</td><td>{g}</td><td>{h}</td></tr>" for n, g, h, o in _RADIO)
_A["leonida/radio-stations.html"].update(
 title="GTA 6 Radio Stations: All 22 and the Secret Vault Radio",
 h1="What radio stations are in GTA 6? All 22 and the secret one",
 desc="GTA 6 has 22 radio stations, according to GameSpot, plus the secret Vault Radio. Genres, hosts and how to unlock the hidden station.",
 answer="GameSpot counts 22 stations from playing the game, plus a secret one, The Vault Radio. Rockstar officially revealed six: Flash FM, Cocoteo FM, Back Country Radio, AfroBank FM, The Chamber 106.6 and Dirty South Classics.",
 body=f"""<h2>All 22 stations</h2>
<p>GameSpot, which has been listening in-game since launch, counts 22 stations, the most in the series, plus a secret one. Stations marked ★ are the six Rockstar officially revealed on October 8, 2026; the rest come from GameSpot, so they rest on a single source.</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Table (scroll for more)"><table><thead><tr><th>Station</th><th>Style</th><th>Hosts (per GameSpot)</th></tr></thead><tbody>{_rows}</tbody></table></div>
<h2>The secret station: The Vault Radio</h2>
<p>According to GameSpot, it unlocks once you reach Vice City: go to The Vault nightclub, roughly in the middle of the city, find a poster with a pink gas mask inside and scan it with your phone. You can then listen to the club's dance and electronic tracks.</p>
<h2>What Rockstar announced</h2>
<p>In its October 8 reveal, Rockstar detailed six stations and their hosts, and said GTA 6 adds on-demand podcasts for the first time, playable in vehicles or on foot through earbuds connected to the in-game phone, plus an official album, <em>Grand Theft Auto VI: The Album</em>, with 34 tracks.</p>
<p>GTABase listed 21 stations before launch without separating confirmed names from leaks; GameSpot's list comes from the released game.</p>""",
 sources=[("https://www.gamespot.com/articles/all-gta-6-radio-stations-and-songs/", "GameSpot: All GTA 6 radio stations and songs (Nov 19, 2026)"),
          ("https://www.rockstargames.com/newswire/article/o3982oa93a23k4/the-music-of-grand-theft-auto-vi-in-game-radio-stations", "Rockstar Newswire: The Music of Grand Theft Auto VI, In-Game Radio Stations (Oct 8, 2026)"),
          ("https://www.gtabase.com/gta-6/radio-stations/", "GTABase: GTA 6 radio stations")])

_m = _A["money/make-money.html"]
_m["body"] = _m["body"].replace("<h2>Other options</h2>", """<h2>How to rob a store without tripping the alarm</h2>
<p>Tips from GameSpot's robbery guide:</p>
<ul>
<li><strong>Check the map first:</strong> every business has a Low, Medium or High security level. Nearly all have an employee, an alarm and cameras.</li>
<li><strong>Crowd first, then the alarm:</strong> smashing displays or doors sets it off. Disable it at a white wall panel, usually in a back room; Focus mode (click both sticks) highlights it.</li>
<li><strong>Cameras:</strong> if you're recorded, find the security room and destroy the footage, or police will identify you when you leave. Or shoot cameras first, ideally with a suppressor.</li>
<li><strong>Use the back door:</strong> the Snap Gun, unlocked through the story, picks locks without tripping the alarm. Your map shows back entrances while you're inside a building.</li>
<li><strong>Safes:</strong> codes are randomized every robbery; look for the code on a guard or nearby. Smaller safes can be picked.</li>
<li><strong>Banks and loan stores:</strong> they pay in marked bills you must sell to a fence, and dye packs explode if you get too far away unless you have a jammer.</li>
<li><strong>Rob as a pair:</strong> in bigger places, the character you're not controlling handles crowd control.</li>
</ul>
<h2>Other options</h2>""", 1)
_m["sources"] = _m["sources"] + [("https://www.gamespot.com/articles/gta-6-safe-codes-and-robberies-guide/", "GameSpot: GTA 6 safe codes and robberies guide (Nov 18, 2026)")]

_CAPS = [("2", "Paradise Lost", ["What's in the Bag?", "Ambulance Chaser", "Play Nurse", "Overnight Charges", "Just Moved In", "Girls' Trip (optional)", "Moses", "New Look", "How Do I Look?", "Got Pills?", "Daily Driver", "Behind on Payments", "Slam Dunk", "Breakfast Run", "Coffee Break (optional)", "Prepare for Vice City", "Afternoon Delight", "Checking Out"]),
 ("3", "Tits Ass Drug Money", ["Welcome to Vice City", "Dealer's Choice", "Meet the Heders", "Dubious Provenance", "Mami Knows Best (optional)", "South Leonida Real Estate", "Tyrone", "Here, Kitty Kitty", "Send Money to Lorena", "Encrypted Hard Drive", "Car Service", "Send More Money to Lorena", "Top Billing", "Boobie Time (optional)", "First Impressions", "Caught Slipping", "Crosstown Traffic", "Credit Check", "Steal the Zorrusso for Randy", "Raul's Next Job (optional, missable)", "Sinfrontera National Bank", "Security Expert", "Heist Planning", "Ride or Die", "Company Property", "The Missing Link", "Safe Word", "Cooties", "Bricked Up", "Hidden Charges", "The Cartel Heist"]),
 ("4", "Vice City, Baby", ["Ocean Beach", "Another Life", "Pool Day", "Company Cars", "Lawyer Up", "It's a Date!", "Party Hard", "Heavy Lifting", "Pay Abe's Fee", "Photo/Shoot (optional)", "Making Gainz", "Blood Sweat and Gear", "Watch It", "Call Nate", "Cash Injections", "Amateur Hour", "Dirty Work", "Nate Will Be in Touch", "Too Much Baggage", "Adventures in Babysitting", "Rafa", "Fresh Evidence", "Power Play", "Child's Play (optional, missable)", "Headliners", "Close Surveillance", "Delivery Method", "Team Building", "Fully Catered", "Heist Plans in Place", "VCIA Takedown", "Tie Up Loose Ends (optional)", "Call Valentina Back", "Sunset", "Starting From Zero"]),
 ("5", "Top of the World, Ma", ["Bird in the Hand", "Taking Liberties", "VC Baby", "Doggie Bag", "Operation Savage Glory", "Honest Abe", "Unfinished Business", "Pay Abe's Fee", "Protective Custody", "The End of the Road"])]
_caps = "\n".join(f"<details><summary>Chapter {n}: {nm.replace('&', '&amp;')} ({len(ms)} missions)</summary><ol>" + "".join(f"<li>{x.replace('&', '&amp;')}</li>" for x in ms) + "</ol></details>" for n, nm, ms in _CAPS)
_c = _A["questions/chapter-1-missions.html"]
_c.update(title="GTA 6 Missions List by Chapter (Spoiler-Light) and Missables",
          h1="What are the missions in GTA 6? Full list by chapter and missables",
          desc="Every GTA 6 mission by chapter, per GTABase, including the four optional missions you can miss. Chapters 2 to 5 are collapsed to avoid spoilers.",
          answer="The story has a Prologue and five chapters. GTABase numbers 122 missions including optional ones, 27 of them in Chapter 1, from “Gone Fishing” to “Discharge Time.” Four optional missions can be missed: two in Chapter 1, one in Chapter 3 and one in Chapter 4.")
_c["body"] = _c["body"] + f"""
<h2>Chapters 2 to 5</h2>
<p class="note">Contains mission titles from later chapters. Expand a chapter only if you want to see them.</p>
<p>From GTABase's list, which names each chapter and flags two more optional missions as missable: “Raul's Next Job” (Chapter 3) and “Child's Play” (Chapter 4).</p>
{_caps}"""

ARTICULOS.append(dict(es="preguntas/secretos-easter-eggs.html", en="questions/secrets-easter-eggs.html",
 title="GTA 6 Secrets and Easter Eggs Found So Far: Aliens, Bigfoot and More",
 h1="What secrets and Easter eggs are in GTA 6? Everything found so far",
 desc="GTA 6 secrets found in the first days: the alien abduction and its trophy, the Easter egg atop Vice City's tallest tower, Bigfoot, Dexter's apartment and more.",
 chip=PART,
 answer="In the first two days, players found an alien abduction with its own trophy, a literal Easter egg atop Vice City's tallest tower, Bigfoot, Dexter Morgan's apartment and nods to Red Dead Redemption, among others. Rockstar doesn't confirm secrets: all of this comes from press coverage and players.",
 body="""<p>Rockstar doesn't confirm secrets, so everything below comes from outlets that checked it or from player videos they reported on. When only one source has it, we say so.</p>
<h2>Alien abduction (with a trophy)</h2>
<p>According to GameSpot, which lays out the steps, and The Tab:</p>
<ol>
<li>Finish Chapter 1.</li>
<li>Alone and after 2 a.m. in-game, head northwest of the Starlet Motel in Kelly County (near Port Gellhorn).</li>
<li>Look for a stranded car with flashing headlights: it points to a trail into the woods, where you'll see a blue light.</li>
<li>Offer to help the woman being abducted and fetch her car. Then you get abducted.</li>
</ol>
<p>It unlocks the “The truth is out there” trophy or achievement.</p>
<h2>The follow-up: the secret base</h2>
<p>According to GameSpot, some time later the abducted character has a dream with clues to a rescue mission at South Point Airfield in Hamlet: you get into the radio tower building through the roof and use a keypad. GameSpot says the code is “usually” 2134 and is shown in the dream; other sites give a different combination, so watch the dream in your own game. There's radiation and toxic gas inside, so move fast.</p>
<h2>A literal Easter egg</h2>
<p>There's a nest at the top of the tallest tower in Vice City. GameSpot and GamingBible say the player who found it took about seven minutes to climb; up top you can grab an egg and throw it, and we won't spoil what happens next. GamingBible describes it as a communications tower, so the exact spot depends on who's telling it.</p>
<h2>Bigfoot</h2>
<p>GameSpot places him in Gullet Marsh and says he's tied to a mission, so he's hard to miss. The Tab points to the wetlands south of Hamlet.</p>
<h2>Dexter Morgan's apartment</h2>
<p>It's on Washington Island in Vice City, near the Top Fun Drones shop in Vice Beach, per GameSpot. You can't go inside. Some players think the boat docked nearby looks like the show's Slice of Life.</p>
<h2>Nods to Red Dead and Liberty City</h2>
<ul>
<li>A Western novel about a cowboy from New Austin, a Red Dead Redemption region; GameSpot spotted it in Jacob's Tavern in Millport.</li>
<li>On the table in Jason's house early in Chapter 1, a former Liberty City mobster's memoir references 2008, the year GTA IV is set.</li>
</ul>
<p>You can read excerpts from books and magazines in the game.</p>
<h2>The secret radio station</h2>
<p>The Vault Radio unlocks by scanning a poster inside The Vault nightclub in Vice City. Details in <a href="../leonida/radio-stations.html">GTA 6 radio stations</a>.</p>
<h2>Unconfirmed</h2>
<ul>
<li><strong>A lifeguard dog:</strong> a dog in sunglasses on a jet ski that rescues stranded swimmers, around Partridge Bay and Gambit Bay according to Playday. GameSpot has also reported on the dog.</li>
<li><strong>Michael's boat:</strong> some players think a boat parked by Jason's house is Michael's from GTA V, per Game Rant. Rockstar hasn't confirmed it.</li>
</ul>
<p>This is a living page: we'll add more secrets as sources confirm them.</p>""",
 sources=[("https://www.gamespot.com/articles/gta-6-has-aliens-and-heres-how-to-find-them/", "GameSpot: GTA 6 has aliens, and here's how to find them (Nov 20, 2026)"),
          ("https://www.gamespot.com/articles/gta-6-easter-eggs-list-and-locations/", "GameSpot: GTA 6 Easter eggs and where to find them (Nov 18, 2026)"),
          ("https://www.gamingbible.com/news/gta-6-secret-cutscene-seven-minute-tower-easter-egg-795530-20261119", "GamingBible: secret cutscene behind a seven-minute climb (Nov 19, 2026)"),
          ("https://thetab.com/2026/11/20/bigfoot-and-ufos-all-the-weird-and-wonderful-things-people-are-stumbling-upon-in-gta-6", "The Tab: Bigfoot, UFOs and other weird finds in GTA 6 (Nov 20, 2026)"),
          ("https://gamerant.com/grand-theft-auto-6-gta-5-easter-egg-michael-boat/", "Game Rant: players think they found Michael's boat"),
          ("https://playday.one/2026/11/19/gta-6-cool-dog-easter-egg/", "Playday: the jet ski dog Easter egg (Nov 19, 2026)")],
 related=["questions/cheats.html", "leonida/map-leonida.html", "leonida/radio-stations.html"]))

# ---------------------------------------------------------------- SEO 20/11/2026: búsquedas reales (Trends y autocompletado)
_A = {a["en"]: a for a in ARTICULOS}
_CREDITS = ("https://www.rockstargames.com/VI/credits", "Rockstar Games: official GTA VI credits")
_CAST = [("Jason Duval", "Dylan Rourke"), ("Lucia Caminos", "Manni L. Perez"), ("Cal Hampton", "Bobby Moynihan"),
         ("Brian Heder", "Stephen Root"), ("Lori Heder", "Orlagh Cassidy"), ("Donnie", "Brad Carter"), ("Mandy", "Lexie Shoaibi"),
         ("Boobie Ike", "Mike Forbs"), ("Dre'Quan", "Naiqui Macabroad"), ("Raul Bautista", "Manny Perez"),
         ("Mia Caminos", "Roselyn Sanchez"), ("Bret Vogel", "Jariko Denman"), ("Moses “Mo” Watkins", "Aaron Morton"),
         ("Randy Kozlov", "Serge Didenko"), ("Pilot Pete", "Carl Palmer"), ("Vicki", "Taryn Manning"),
         ("Kordell Grant", "Michael Jai White"), ("DWNPLY", "Denzel Curry"), ("Arnold", "Caesar Samayoa"),
         ("Shirley Baker", "Carolee Carmello"), ("The Hitman", "Michael Hollick")]
_cast_rows = "".join(f"<tr><td>{p}</td><td>{a}</td></tr>" for p, a in _CAST)

ARTICULOS.append(dict(es="lugares/personajes-actores.html", en="leonida/voice-actors-cast.html",
 title="GTA 6 Voice Actors and Cast: Who Plays Jason, Lucia and Mandy",
 h1="Who voices Jason and Lucia? GTA 6 voice actors and cast",
 desc="GTA 6's cast from the official credits: Dylan Rourke plays Jason, Manni L. Perez plays Lucia and Lexie Shoaibi plays Mandy. Plus: is Niko Bellic in GTA 6?",
 chip=OK,
 answer="According to Rockstar's official credits, Jason Duval is played by Dylan Rourke and Lucia Caminos by Manni L. Perez. The cast also includes Stephen Root (Brian Heder), Bobby Moynihan (Cal) and Lexie Shoaibi (Mandy). Michael Hollick, who played Niko Bellic in GTA IV, is credited as “The Hitman.”",
 body=f"""<p>Rockstar published GTA 6's full credits on its official site at launch. The same performers handled voice and motion capture, according to Screen Rant.</p>
<h2>Jason and Lucia</h2>
<ul>
<li><strong>Jason Duval: Dylan Rourke.</strong> Screen Rant says it's his video game debut; he's had TV guest spots on <em>Station 19</em>, <em>Modern Family</em> and <em>9-1-1: Lone Star</em>.</li>
<li><strong>Lucia Caminos: Manni L. Perez.</strong> Not her first GTA: per Screen Rant, she appeared as a clubgoer in GTA V and GTA Online, and has guest-starred on <em>The Blacklist</em>, <em>Jessica Jones</em> and <em>Chicago P.D.</em></li>
</ul>
<p>Who they are in the story: <a href="characters.html">Jason and Lucia, the protagonists</a>.</p>
<h2>Main cast</h2>
<p>A selection from the official credits, covering characters mentioned on this site:</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Table (scroll for more)"><table><thead><tr><th>Character</th><th>Actor</th></tr></thead><tbody>{_cast_rows}</tbody></table></div>
<p>The credits also include music cameos such as Kodak Black, who plays himself.</p>
<h2>Is Niko Bellic in GTA 6?</h2>
<p>Not confirmed. What we do know: the official credits list <strong>Michael Hollick</strong>, the actor who played Niko Bellic in GTA IV, in the role of “The Hitman.” Rockstar doesn't say that character is Niko, so we don't assume it. GameSpot also found an in-game memoir by a former Liberty City mobster that references 2008, the year GTA IV is set.</p>
<h2>What about Mandy?</h2>
<p>She's played by Lexie Shoaibi. Who she is and whether you can date her: <a href="../questions/mandy.html">Mandy in GTA 6</a>.</p>""",
 sources=[_CREDITS, ("https://screenrant.com/gta-6-cast-voice-actors/", "Screen Rant: GTA 6 full cast and voice list (Nov 19, 2026)"),
          ("https://www.gamespot.com/articles/gta-6-easter-eggs-list-and-locations/", "GameSpot: GTA 6 Easter eggs (Nov 18, 2026)")],
 related=["leonida/characters.html", "questions/mandy.html", "questions/endings-choices.html"]))

ARTICULOS.append(dict(es="preguntas/mandy.html", en="questions/mandy.html",
 title="Who Is Mandy in GTA 6? Can You Romance Her?",
 h1="Who is Mandy in GTA 6, and can you romance her?",
 desc="Mandy is Brian's tenant in Key Lento whom Jason meets in the Pipework mission. You can't romance her. Who plays her and what's known about her.",
 chip=OK,
 answer="Mandy is one of Brian Heder's tenants in Key Lento: Jason meets her in “Pipework,” a Chapter 1 mission where he collects her rent. She flirts with Jason, but you can't romance her. She's played by Lexie Shoaibi.",
 body="""<h2>Who she is</h2>
<p>She's one of Brian Heder's tenants in Key Lento, in the Leonida Keys. Jason meets her in “Pipework,” a Chapter 1 mission where Brian sends him to collect overdue rent and he ends up fixing her pipes, according to GTABase and GameSpot. The official credits list Lexie Shoaibi as Mandy.</p>
<h2>Can you romance Mandy?</h2>
<p>No. According to GameSpot, Mandy flirts with Jason throughout the mission, but the dialogue never lets you steer things toward romance, and at the end Jason leaves without the player getting a choice. You can drop by her house later and pick things back up, but that doesn't make her a romance option.</p>
<p>The game's only relationship is Jason and Lucia's, and Rockstar has said it's optional: if you want it to work, you have to nurture it. More in <a href="endings-choices.html">endings and choices</a>.</p>
<h2>Is Mandy a serial killer?</h2>
<p>That's a player theory based on items in her home and car. It isn't confirmed. GameSpot mentions Jason pulls a “curious item” out of her pipes, but nothing more.</p>""",
 sources=[("https://www.gamespot.com/articles/can-you-romance-mandy-in-gta-6/", "GameSpot: Can you romance Mandy in GTA 6? (Nov 18, 2026)"),
          ("https://www.gtabase.com/gta-6/missions/", "GTABase: GTA 6 missions list (Pipework)"), _CREDITS,
          ("https://www.techradar.com/gaming/rockstar-says-if-you-want-gta-6s-romance-between-jason-and-lucia-to-flourish-you-have-to-nurture-it-but-its-completely-optional-its-not-something-that-we-want-to-foist-upon-players", "TechRadar: Rockstar says Jason and Lucia's romance is optional"),
          ("https://beebom.com/gta-6-mandy-serial-killer/", "Beebom: the Mandy serial killer theory")],
 related=["leonida/voice-actors-cast.html", "questions/fix-jasons-house.html", "questions/endings-choices.html"]))

ARTICULOS.append(dict(es="preguntas/arreglos-casa-jason.html", en="questions/fix-jasons-house.html",
 title="How to Fix the Railing in GTA 6: All 4 Jason's House Projects",
 h1="How to fix the railing and Jason's house in GTA 6",
 desc="All four Jason's house projects in GTA 6 (steps, roof, railing and wall), where to find them, and why you must finish them before picking up Lucia.",
 chip=OK,
 answer="There are four projects at Jason's Key Lento house: the steps, the roof, the railing and the bedroom wall. Do them before you pick up Lucia, because you can't finish them afterward. The railing is behind the house, by the outdoor gym.",
 body="""<p>Early in the story, Jason lives in a waterfront house in Key Lento that Brian Heder lends him. It's a fixer-upper, and you have limited time to fix it up before Lucia gets out and moves in, according to GameSpot. Finishing the projects makes Lucia happier and strengthens their relationship.</p>
<h2>The four projects</h2>
<ol>
<li><strong>Steps:</strong> next to the stairs closest to the mailbox and driveway are some 2x4s; interact with them (Triangle / Y).</li>
<li><strong>Leaky roof:</strong> climb the yellow ladder on the front porch and interact with the shingles.</li>
<li><strong>Railing:</strong> the hardest to find. Go out the back door and down to the outdoor gym; facing the house, you'll see a gap in the railing next to a ladder. Interact with the gap.</li>
<li><strong>Wall:</strong> in the bedroom, the wall opposite the bed is half-built. Interact with the wood frame: Jason hangs drywall and paints it, and you pick the color.</li>
</ol>
<p class="note">Important: once you decide to go pick up Lucia, you can't come back to these projects.</p>
<h2>Other tasks before Lucia arrives</h2>
<p>GTABase and GameSpot list more optional Chapter 1 tasks: picking up groceries, buying flowers, buying Lucia a necklace, collecting her clothes from her friend Andy and getting a haircut. Push Square adds that Lucia reacts differently depending on whether the house was ready in time.</p>
<p>To be safe, save to another slot first: <a href="how-to-save.html">how to save</a>. Full list in <a href="chapter-1-missions.html">GTA 6 missions</a>.</p>""",
 sources=[("https://www.gamespot.com/articles/how-to-fix-all-projects-at-jasons-house-in-gta-6/", "GameSpot: How to fix all projects at Jason's house in GTA 6 (Nov 18, 2026)"),
          ("https://www.gtabase.com/gta-6/missions/", "GTABase: Chapter 1 missions (Feng Shui and optional tasks)"),
          (PSQ, "Push Square: Grand Theft Auto 6 review")],
 related=["questions/chapter-1-missions.html", "questions/mandy.html", "questions/endings-choices.html"]))

ARTICULOS.append(dict(es="dinero/codigos-cajas-fuertes.html", en="money/safe-codes.html",
 title="GTA 6 Safe Codes: Why Online Lists Don't Work",
 h1="GTA 6 safe codes: why online lists don't work",
 desc="GTA 6 safe codes are randomized: they change every playthrough and every robbery. How to find yours, including at Brooks Boatworks and Kingpin Bowling.",
 chip=ONE,
 answer="No list will work: according to GameSpot, GTA 6 safe codes are randomized, changing every playthrough and even if you rob the same store twice. The code is on a guard or somewhere nearby, and smaller safes can be picked.",
 body="""<h2>How to find the code</h2>
<ul>
<li>Some safes need a code. According to GameSpot, a guard usually carries it or it's written down nearby; Focus mode (click both sticks) helps you spot it.</li>
<li>If you can't find it, smaller safes can be picked and lockboxes snapped open.</li>
<li>Most safes can be forced open, but that usually trips the alarm.</li>
</ul>
<h2>What about Brooks Boatworks or Kingpin Bowling?</h2>
<p>They're among the most searched safe codes right now. GameSpot doesn't mention any exceptions to codes being randomized, so a code you find online probably won't match your game: search the location itself.</p>
<h2>Before you open the safe</h2>
<p>Handle the crowd, disable the alarm and destroy the camera footage first. Every step is in <a href="make-money.html">how to rob a store without tripping the alarm</a>.</p>
<p>Safe codes aren't cheats: <a href="../questions/cheats.html">GTA 6 cheats</a> are entered on the phone and only work after the story.</p>""",
 sources=[("https://www.gamespot.com/articles/gta-6-safe-codes-and-robberies-guide/", "GameSpot: GTA 6 safe codes and robberies guide (Nov 18, 2026)")],
 related=["money/make-money.html", "questions/cheats.html", "money/buckme-bank.html"]))

# Títulos alineados con lo que se busca
_A["questions/how-to-save.html"].update(title="Does GTA 6 Autosave? How to Save Your Game (15 Slots)",
    h1="Does GTA 6 autosave? How to save your game",
    desc="Yes, GTA 6 autosaves, and it has 15 manual save slots. How to save, when you can't, and why cheats block saving.")
_A["pc-online/gta-6-pc.html"].update(title="Is GTA 6 on PC or Steam? Release Date and What Take-Two Says",
    h1="Is GTA 6 on PC? When it's coming to PC and Steam",
    desc="GTA 6 isn't on PC or Steam and has no PC date. What Take-Two has said, and how long GTA V and Red Dead Redemption 2 took to reach PC.")
_A["leonida/map-leonida.html"].update(title="GTA 6 Map: Leonida's Regions, Counties and Vice City")
_A["questions/chapter-1-missions.html"].update(title="GTA 6 Missions List: How Many Chapters and Every Mission")
_A["pc-online/price-editions.html"].update(title="How Much Is GTA 6? Standard $79.99 vs Ultimate $99.99")

_ps = _A["issues/ps5-pro-vs-ps5-vs-xbox.html"]
_ps["body"] = _ps["body"].replace("<h2>Is a PS5 Pro worth it just for this?</h2>", """<h2>Why does GTA 6 look blurry?</h2>
<p>Internal resolution. Per Digital Foundry's analysis, the game renders internally at 1440p on PS5 and upscales, while Series S starts from 720p to reach 1080p, so it can look softer than on PS5 Pro, which upscales with PSSR. No in-game setting changes that, since every console runs at 30fps.</p>
<h2>Is a PS5 Pro worth it just for this?</h2>""", 1)
_x = _A["issues/ps4-xbox-one.html"]
_x["body"] = _x["body"] + """
<h2>What about Nintendo Switch 2, Steam or Game Pass?</h2>
<p>Rockstar has only released GTA 6 on PS5 and Xbox Series X|S. There's no Nintendo Switch 2 or PC version, so it isn't on Steam either (more in <a href="../pc-online/gta-6-pc.html">GTA 6 on PC</a>). Rockstar hasn't announced GTA 6 for Game Pass.</p>"""
_c = _A["leonida/characters.html"]
_c["body"] = _c["body"].replace("<h2>Other official characters</h2>", """<h2>Who voices them</h2>
<p>According to the official credits, Jason is played by Dylan Rourke and Lucia by Manni L. Perez. The full cast is in <a href="voice-actors-cast.html">GTA 6 voice actors and cast</a>.</p>
<h2>Other official characters</h2>""", 1)
_c["sources"] = _c["sources"] + [_CREDITS]

# Páginas que no son artículos: equivalencias para hreflang y el selector.
OTRAS = {
    "index.html": "en/",
    "guia-inicio.html": "en/beginners-guide.html",
    "sobre.html": "en/about.html",
    "aviso-legal.html": "en/legal-notice.html",
    "privacidad.html": "en/privacy.html",
    "cookies.html": "en/cookies.html",
    "buscar.html": "en/search.html",
    "404.html": "en/404.html",
}

MAPA = {a["es"]: "en/" + a["en"] for a in ARTICULOS}
MAPA.update({f'{v["es"]}/index.html': f"en/{k}/" for k, v in SECCIONES_EN.items()})
MAPA.update(OTRAS)
