/* ores-calc.js — ενδεικτικός υπολογισμός ετήσιων ωρών Τεχνικού Ασφαλείας / Ιατρού Εργασίας
   Συντελεστές: άρθρο 21 ν. 3850/2010 (όπως κωδικοποιήθηκε στο ΠΔ 62/2025). Ελάχιστο: 25 / 50 / 75 ώρες. */
(function () {
    'use strict';
    var cat = document.getElementById('calcCat'), emp = document.getElementById('calcEmp');
    if (!cat || !emp) return;
    function coefTA(c, n) {
        if (c === 'A') return n <= 500 ? 3.5 : n <= 1000 ? 3.0 : n <= 5000 ? 2.5 : 2.0;
        if (c === 'B') return n <= 1000 ? 2.5 : n <= 5000 ? 1.5 : 1.0;
        return 0.4;
    }
    function coefIE(c) { return c === 'A' ? 0.8 : c === 'B' ? 0.6 : 0.4; }
    function min(n) { return n <= 20 ? 25 : n <= 50 ? 50 : 75; }
    function fmt(x) { return (Math.round(x * 10) / 10).toLocaleString('el-GR'); }
    var sent = false;
    function run() {
        var c = cat.value, n = Math.max(1, Math.min(100000, parseInt(emp.value, 10) || 0));
        var ta = n * coefTA(c, n), taH = Math.max(ta, min(n));
        document.getElementById('calcTA').textContent = fmt(taH) + ' ώρες/έτος';
        document.getElementById('calcTAsub').textContent = n + ' × ' + fmt(coefTA(c, n)) + ' = ' + fmt(ta) + (ta < min(n) ? ' → ελάχιστο ' + min(n) + ' ώρες' : '') + ' · περίπου ' + fmt(taH / 12) + ' ώρες τον μήνα';
        if (n >= 50) {
            var ie = n * coefIE(c), ieH = Math.max(ie, min(n));
            document.getElementById('calcIE').textContent = fmt(ieH) + ' ώρες/έτος';
            document.getElementById('calcIEsub').textContent = n + ' × ' + fmt(coefIE(c)) + ' = ' + fmt(ie) + (ie < min(n) ? ' → ελάχιστο ' + min(n) + ' ώρες' : '');
        } else {
            document.getElementById('calcIE').textContent = '—';
            document.getElementById('calcIEsub').textContent = 'Κατά κανόνα απαιτείται από 50 εργαζόμενους και πάνω.';
        }
        if (!sent && window.ccEvent) { sent = true; window.ccEvent('calc_use', { category: c }); }
    }
    cat.addEventListener('change', run);
    emp.addEventListener('input', run);
    run();
})();
