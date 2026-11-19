/* 6 Estrellas: buscador interno. Sin dependencias, sin cookies, sin enviar nada a ningún servidor.
   Carga assets/search-index.json (generado por herramientas/mantenimiento.py) y filtra en el navegador. */
(function () {
  "use strict";
  var form = document.getElementById("search-form"), input = document.getElementById("q"),
      out = document.getElementById("search-results"), status = document.getElementById("search-status");
  if (!form || !input || !out) return;

  // Sinónimos habituales en España y Latinoamérica (todos ya normalizados).
  var SIN = {
    coche: ["carro", "auto", "vehiculo", "vehiculos"], carro: ["coche", "auto"], auto: ["coche", "carro"],
    vehiculo: ["coche"], ordenador: ["pc", "computadora"], computadora: ["ordenador", "pc"], pc: ["ordenador"],
    dinero: ["plata", "efectivo", "cash"], plata: ["dinero"], trucos: ["codigos", "cheats", "claves"],
    codigos: ["trucos"], policia: ["wanted", "estrellas", "busqueda"], trofeos: ["logros", "platino"],
    logros: ["trofeos"], online: ["multijugador", "multiplayer"], multijugador: ["online"],
    errores: ["fallo", "problema", "bug"], problema: ["errores", "fallo"], precio: ["cuesta", "costo", "coste"],
    descargar: ["descarga", "instalar", "peso", "tamano", "gb"], tamano: ["peso", "gb", "ocupa"]
  };
  var data = null, loading = null;

  function norm(s) {
    return (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9ñ ]+/g, " ").replace(/\s+/g, " ").trim();
  }
  function esc(s) { return s.replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function load() {
    if (data) return Promise.resolve(data);
    if (!loading) {
      loading = fetch("assets/search-index.json").then(function (r) { return r.json(); }).then(function (j) {
        data = j.map(function (x) { x._t = norm(x.t); x._r = norm(x.r + " " + x.d); x._c = norm(x.c); return x; });
        return data;
      });
    }
    return loading;
  }
  function score(item, tokens) {
    var total = 0;
    for (var i = 0; i < tokens.length; i++) {
      var alts = [tokens[i]].concat(SIN[tokens[i]] || []), best = 0;
      for (var j = 0; j < alts.length; j++) {
        var w = alts[j], pts = (j === 0 ? 1 : 0.7);
        var v = (item._t.indexOf(w) > -1 ? 6 : 0) + (item._r.indexOf(w) > -1 ? 3 : 0) + (item._c.indexOf(w) > -1 ? 1 : 0);
        if (v * pts > best) best = v * pts;
      }
      if (!best) return 0;      // todas las palabras deben aparecer (en ella o en un sinónimo)
      total += best;
    }
    return total;
  }
  function render(items, q) {
    if (!items.length) {
      out.innerHTML = "";
      status.textContent = "No hay resultados para «" + q + "». Prueba con otra palabra o mira las secciones del menú.";
      return;
    }
    status.textContent = items.length + (items.length === 1 ? " resultado" : " resultados") + " para «" + q + "»";
    out.innerHTML = items.slice(0, 20).map(function (x) {
      return '<li class="result"><a href="' + esc(x.u) + '"><span class="card-t">' + esc(x.t) + '</span>' +
             '<span class="card-d">' + esc(x.r.length > 170 ? x.r.slice(0, 167) + "…" : x.r) + '</span>' +
             '<span class="result-s">' + esc(x.s) + '</span></a></li>';
    }).join("");
  }
  function run() {
    var q = input.value.trim(), n = norm(q);
    if (n.length < 2) { out.innerHTML = ""; status.textContent = ""; return; }
    status.textContent = "Buscando…";
    load().then(function (d) {
      var tokens = n.split(" ").filter(function (t) { return t.length > 1; });
      var res = d.map(function (x) { return { x: x, s: score(x, tokens) }; })
                 .filter(function (r) { return r.s > 0; })
                 .sort(function (a, b) { return b.s - a.s; })
                 .map(function (r) { return r.x; });
      render(res, q);
    }).catch(function () { status.textContent = "No se pudo cargar el buscador. Inténtalo de nuevo o usa el menú."; });
  }
  var timer;
  input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(run, 120); });
  form.addEventListener("submit", function (e) { e.preventDefault(); run(); });
  var m = /[?&]q=([^&]*)/.exec(location.search);
  if (m) { try { input.value = decodeURIComponent(m[1].replace(/\+/g, " ")); } catch (e) {} run(); }
})();
