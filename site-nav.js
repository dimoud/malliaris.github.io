/* site-nav.js — υπομενού της μπάρας (Υπηρεσίες / Τομείς) και κάρτες υπηρεσιών που ανοίγουν τη σελίδα τους */
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

    /* ── Κάρτες υπηρεσιών (αρχική): κλικ σε όλη την κάρτα → σελίδα υπηρεσίας ──
       Σε οθόνη αφής το πρώτο πάτημα ανοίγει το κείμενο (όπως πριν), το δεύτερο ανοίγει τη σελίδα. */
    var touch = window.matchMedia('(hover: none)').matches;
    document.addEventListener('click', function (e) {
        var card = e.target.closest && e.target.closest('.service-card');
        if (!card || e.target.closest('a')) return;
        var link = card.querySelector('.sc-link');
        if (!link) return;
        if (touch && !card.classList.contains('touched')) return;
        if (e.ctrlKey || e.metaKey || e.button === 1) { window.open(link.href, '_blank'); return; }
        window.location.href = link.href;
    }, true);
})();
