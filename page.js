/* page.js — μενού κινητού και «συμπαγές» μενού στην κύλιση, για τις εσωτερικές σελίδες */
(function () {
    'use strict';
    var nav = document.getElementById('nav');
    var links = document.getElementById('navLinks');
    var hbg = document.getElementById('hamburger');
    function close() { if (links) links.classList.remove('open'); if (hbg) { hbg.classList.remove('open'); hbg.setAttribute('aria-expanded', 'false'); } }
    if (hbg && links) {
        hbg.addEventListener('click', function () {
            var open = links.classList.toggle('open');
            hbg.classList.toggle('open', open);
            hbg.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        hbg.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); hbg.click(); } });
        links.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });
    }
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    function onScroll() {
        if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
        if (links) links.classList.toggle('nav-scrolled', window.scrollY > 60);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
})();
