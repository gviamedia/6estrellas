/* 6 Estrellas / Six Stars: consentimiento de cookies y huecos de anuncio. Sin dependencias.
   IMPORTANTE: si añades un proveedor nuevo (anuncios, estadísticas), sube CONSENT_VERSION
   para que todo el mundo vuelva a ver el aviso. Para AdSense en el EEE hace falta además
   una CMP certificada por Google (TCF v2.2); este banner no la sustituye. */
(function () {
  "use strict";
  var KEY = "seisestrellas_consent", CONSENT_VERSION = 3, MAX_AGE = 365 * 24 * 3600 * 1000;
  // Texto del anuncio propio que se muestra cuando no hay consentimiento (o el anuncio no carga).
  var HOUSE = document.documentElement.lang === "en" ? "Free GTA 6 beginner's guide →" : "Guía de inicio gratis de GTA 6 →";

  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY));
      if (v && v.v === CONSENT_VERSION && Date.now() - v.t < MAX_AGE) return v;
    } catch (e) {}
    return null;
  }
  function save(c) {
    var prev = read();
    c.t = Date.now(); c.v = CONSENT_VERSION;
    try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {}
    // Si se retira un permiso ya concedido, recargamos para no dejar scripts en marcha.
    if (prev && prev.ads && !c.ads) { location.reload(); return; }
    apply(c);
  }
  /* Carga diferida de scripts de terceros. Añade en el HTML:
     <script type="text/plain" data-consent="ads" data-src="https://..."></script>
     y solo se ejecutará si el usuario acepta esa categoría. */
  function apply(c) {
    window.GL_CONSENT = c;
    document.querySelectorAll('script[type="text/plain"][data-consent]').forEach(function (s) {
      if (!c[s.getAttribute("data-consent")] || s.dataset.loaded) return;
      var n = document.createElement("script");
      if (s.dataset.src) { n.src = s.dataset.src; n.async = true; } else { n.text = s.text; }
      s.dataset.loaded = "1"; document.head.appendChild(n);
    });
    fillAds(c);
  }

  /* Huecos de anuncio. Cada <aside class="ad" data-ad="CLAVE" data-w data-h data-src-base> se
     rellena con un iframe aislado SOLO si el usuario acepta publicidad. Si no, se muestra un
     anuncio propio del mismo tamaño para que no haya saltos de maquetación. */
  /* atOptions es global en el código de Adsterra: cargamos los huecos de uno en uno. */
  var adQueue = [], adBusy = false;
  function runQueue() {
    if (adBusy || !adQueue.length) return;
    adBusy = true;
    adQueue.shift()(function () { adBusy = false; runQueue(); });
  }
  function fillAds(c) {
    document.querySelectorAll(".ad[data-ad]").forEach(function (a) {
      if (a.dataset.done) return;
      var box = a.querySelector(".ad-box");
      if (!c.ads || !a.dataset.ad || !a.dataset.src) {
        if (!box.firstChild) box.innerHTML = '<a class="ad-house" href="' + a.dataset.house + '">' + HOUSE + '</a>';
        return;
      }
      function load() {
        if (a.dataset.done) return;
        a.dataset.done = "1";
        adQueue.push(function (next) {
          box.innerHTML = "";
          window.atOptions = { key: a.dataset.ad, format: "iframe", height: +a.dataset.h, width: +a.dataset.w, params: {} };
          var s = document.createElement("script");
          s.src = a.dataset.src; s.async = false; s.setAttribute("data-cfasync", "false");
          var house = function () {
            if (!box.querySelector("iframe, ins, a, img")) box.insertAdjacentHTML("beforeend", '<a class="ad-house" href="' + a.dataset.house + '">' + HOUSE + '</a>');
          };
          s.onload = function () { setTimeout(function () { house(); next(); }, 3000); };
          s.onerror = function () { house(); setTimeout(next, 300); };
          box.appendChild(s);
        });
        runQueue();
      }
      if ("IntersectionObserver" in window) {
        var io = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { io.disconnect(); load(); } }, { rootMargin: "300px" });
        io.observe(a);
      } else load();
    });
  }

  var box = document.getElementById("consent");
  var root = document.documentElement;
  function setPad() { root.style.setProperty("--consent-h", box.hidden ? "0px" : (box.offsetHeight + 16) + "px"); }
  var opener = null;
  function close() {
    box.hidden = true; setPad();
    // Devolver el foco a donde estaba (p. ej. el botón «Configurar cookies» del pie).
    if (opener && document.contains(opener)) { try { opener.focus(); } catch (e) {} }
    opener = null;
  }
  function toggleOpts(on) {
    document.getElementById("consent-opts").hidden = !on;
    box.querySelector('[data-consent="save"]').hidden = !on;
    box.querySelector('[data-consent="config"]').hidden = on;
    setPad();
  }
  function open(showOpts, from) {
    if (!box) return;
    var c = read() || {};
    var d = document.getElementById("c-ads");
    if (d) d.checked = !!c.ads;
    if (from) opener = from;
    box.hidden = false;
    toggleOpts(!!showOpts);
    if (from) { var f = box.querySelector("input:not([disabled]), button"); if (f) f.focus(); }
  }
  if (box) {
    box.addEventListener("click", function (e) {
      var b = e.target.closest("[data-consent]"); if (!b) return;
      var k = b.getAttribute("data-consent");
      if (k === "accept") { close(); save({ ads: true }); }
      else if (k === "reject") { close(); save({ ads: false }); }
      else if (k === "config") {
        toggleOpts(true);
        var f = document.getElementById("c-ads"); if (f) f.focus();   // no perder el foco al ocultar «Configurar»
      }
      else if (k === "save") {
        var c = { ads: document.getElementById("c-ads").checked };
        close(); save(c);
      }
    });
    // Escape cierra el aviso sin guardar elección (equivale a no consentir: no se cargan anuncios).
    box.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !box.hidden) { close(); }
    });
    var cur = read();
    if (cur) apply(cur); else { open(false); fillAds({}); }
    window.addEventListener("resize", function () { if (!box.hidden) setPad(); });
  }
  document.querySelectorAll("[data-open-consent]").forEach(function (b) {
    b.addEventListener("click", function () { open(true, b); });
  });

})();
