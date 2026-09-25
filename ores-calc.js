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
    var EN = (document.documentElement.lang || '').indexOf('en') === 0;
    var T = EN ? { yr: ' hours/year', min: ' → minimum ', hrs: ' hours', mo: ' · about ', pm: ' hours a month', ie: 'As a rule, required from 50 employees upwards.' }
               : { yr: ' ώρες/έτος', min: ' → ελάχιστο ', hrs: ' ώρες', mo: ' · περίπου ', pm: ' ώρες τον μήνα', ie: 'Κατά κανόνα απαιτείται από 50 εργαζόμενους και πάνω.' };
    function fmt(x) { return (Math.round(x * 10) / 10).toLocaleString(EN ? 'en-GB' : 'el-GR'); }
    var sent = false;
    function run() {
        var c = cat.value, n = Math.max(1, Math.min(100000, parseInt(emp.value, 10) || 0));
        var ta = n * coefTA(c, n), taH = Math.max(ta, min(n));
        document.getElementById('calcTA').textContent = fmt(taH) + T.yr;
        document.getElementById('calcTAsub').textContent = n + ' × ' + fmt(coefTA(c, n)) + ' = ' + fmt(ta) + (ta < min(n) ? T.min + min(n) + T.hrs : '') + T.mo + fmt(taH / 12) + T.pm;
        if (n >= 50) {
            var ie = n * coefIE(c), ieH = Math.max(ie, min(n));
            document.getElementById('calcIE').textContent = fmt(ieH) + T.yr;
            document.getElementById('calcIEsub').textContent = n + ' × ' + fmt(coefIE(c)) + ' = ' + fmt(ie) + (ie < min(n) ? T.min + min(n) + T.hrs : '');
        } else {
            document.getElementById('calcIE').textContent = '—';
            document.getElementById('calcIEsub').textContent = T.ie;
        }
        if (!sent && window.ccEvent) { sent = true; window.ccEvent('calc_use', { category: c }); }
    }
    cat.addEventListener('change', run);
    emp.addEventListener('input', run);
    run();
})();
