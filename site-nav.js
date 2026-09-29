/* site-nav.js - υπομενού της μπάρας (Υπηρεσίες / Τομείς) */
(function () {
    'use strict';

    /* ── Υπομενού ── */
    var dds = Array.prototype.slice.call(document.querySelectorAll('.nav-dd'));
    function closeAll(except) {
        dds.forEach(function (d) {
            if (d === except) return;
            d.classList.remove('dd-open');
            var b = d.querySelector('.nav-dd-toggle');
            if (b) b.setAttribute('aria-expanded', 'false');
        });
    }
    dds.forEach(function (d) {
        var btn = d.querySelector('.nav-dd-toggle');
        if (!btn) return;
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            var open = !d.classList.contains('dd-open');
            closeAll(d);
            d.classList.toggle('dd-open', open);
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        /* το ποντίκι φεύγει από το υπομενού: κλείνει και η «ανοιχτή» κατάσταση που άνοιξε με κλικ */
        d.addEventListener('mouseleave', function () {
            if (window.matchMedia('(hover: hover) and (min-width: 901px)').matches) closeAll();
        });
    });
    document.addEventListener('click', function (e) {
        if (!e.target.closest || !e.target.closest('.nav-dd')) closeAll();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
})();
