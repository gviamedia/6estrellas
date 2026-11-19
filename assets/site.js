/* 6 Estrellas: consentimiento de cookies y formulario de correo. Sin dependencias.
   IMPORTANTE: si añades un proveedor nuevo (anuncios, estadísticas), sube CONSENT_VERSION
   para que todo el mundo vuelva a ver el aviso. Para AdSense en el EEE hace falta además
   una CMP certificada por Google (TCF v2.2); este banner no la sustituye. */
(function () {
  "use strict";
  var KEY = "seisestrellas_consent", CONSENT_VERSION = 2, MAX_AGE = 365 * 24 * 3600 * 1000;

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
    if (prev && ((prev.analytics && !c.analytics) || (prev.ads && !c.ads))) { location.reload(); return; }
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
        if (!box.firstChild) box.innerHTML = '<a class="ad-house" href="' + a.dataset.house + '">Guía de inicio gratis de GTA 6 →</a>';
        return;
      }
      function load() {
        if (a.dataset.done) return;
        a.dataset.done = "1";
        adQueue.push(function (next) {
          box.innerHTML = "";
          window.atOptions = { key: a.dataset.ad, format: "iframe", height: +a.dataset.h, width: +a.dataset.w, params: {} };
          var s = document.createElement("script");
          s.src = a.dataset.src; s.async = false;
          var house = function () {
            if (!box.querySelector("iframe, ins, a, img")) box.insertAdjacentHTML("beforeend", '<a class="ad-house" href="' + a.dataset.house + '">Guía de inicio gratis de GTA 6 →</a>');
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
  function close() { box.hidden = true; setPad(); }
  function toggleOpts(on) {
    document.getElementById("consent-opts").hidden = !on;
    box.querySelector('[data-consent="save"]').hidden = !on;
    box.querySelector('[data-consent="config"]').hidden = on;
    setPad();
  }
  function open(showOpts) {
    if (!box) return;
    var c = read() || {};
    var a = document.getElementById("c-analytics"), d = document.getElementById("c-ads");
    if (a) a.checked = !!c.analytics;
    if (d) d.checked = !!c.ads;
    box.hidden = false;
    toggleOpts(!!showOpts);
  }
  if (box) {
    box.addEventListener("click", function (e) {
      var b = e.target.closest("[data-consent]"); if (!b) return;
      var k = b.getAttribute("data-consent");
      if (k === "accept") { close(); save({ analytics: true, ads: true }); }
      else if (k === "reject") { close(); save({ analytics: false, ads: false }); }
      else if (k === "config") { toggleOpts(true); }
      else if (k === "save") {
        var c = { analytics: document.getElementById("c-analytics").checked, ads: document.getElementById("c-ads").checked };
        close(); save(c);
      }
    });
    var cur = read();
    if (cur) apply(cur); else { open(false); fillAds({}); }
    window.addEventListener("resize", function () { if (!box.hidden) setPad(); });
  }
  document.querySelectorAll("[data-open-consent]").forEach(function (b) {
    b.addEventListener("click", function () { open(true); });
  });

  /* Formulario de correo. Para activarlo con Brevo: crea el formulario en Brevo con doble
     opt-in y pon su URL de acción en BREVO_ACTION al ejecutar build.py. */
  document.querySelectorAll(".email-form").forEach(function (f) {
    var msg = f.querySelector(".form-msg"), mail = f.querySelector('input[type="email"]'), ok = f.querySelector('input[name="OPT_IN"]'), age = f.querySelector('input[name="AGE_OK"]');
    function err(el, t) {
      msg.textContent = t; msg.classList.add("is-error");
      el.setAttribute("aria-invalid", "true"); el.setAttribute("aria-describedby", msg.id); el.focus();
    }
    function clear(el) { el.removeAttribute("aria-invalid"); msg.classList.remove("is-error"); }
    mail.addEventListener("input", function () { clear(mail); });
    ok.addEventListener("change", function () { clear(ok); });
    if (age) age.addEventListener("change", function () { clear(age); });
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!mail.value.trim()) return err(mail, "Escribe tu correo.");
      if (!mail.checkValidity()) return err(mail, "Al correo le falta algo (ej.: nombre@gmail.com).");
      if (!ok.checked) return err(ok, "Marca la casilla para recibir la guía.");
      if (age && !age.checked) return err(age, "Confirma que tienes 18 años o más.");
      msg.classList.remove("is-error");
      var action = f.getAttribute("data-brevo-action");
      if (!action) { msg.textContent = "La suscripción todavía no está activa. Mientras tanto, puedes leer la guía en la página Guía gratis."; return; }
      fetch(action, { method: "POST", body: new FormData(f), mode: "no-cors" })
        .then(function () { msg.textContent = "Listo. Revisa tu correo para confirmar la suscripción."; f.reset(); })
        .catch(function () { msg.classList.add("is-error"); msg.textContent = "No se pudo enviar. Comprueba tu conexión e inténtalo de nuevo."; });
    });
  });
})();
