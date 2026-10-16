/* ores-calc.js - ενδεικτικός υπολογισμός ετήσιων ωρών Τεχνικού Ασφαλείας / Ιατρού Εργασίας
   Συντελεστές: άρθρο 21 ν. 3850/2010 (όπως κωδικοποιήθηκε στο ΠΔ 62/2025). Ελάχιστο: 25 / 50 / 75 ώρες. */
(function () {
    'use strict';
    var CATS = ['A', 'B', 'C'], inp = {};
    CATS.forEach(function (c) { inp[c] = document.getElementById('calc' + c); });
    if (!inp.A || !inp.B || !inp.C) return;
    function coefTA(c, n) {
        if (c === 'A') return n <= 500 ? 3.5 : n <= 1000 ? 3.0 : n <= 5000 ? 2.5 : 2.0;
        if (c === 'B') return n <= 1000 ? 2.5 : n <= 5000 ? 1.5 : 1.0;
        return 0.4;
    }
    function coefIE(c) { return c === 'A' ? 0.8 : c === 'B' ? 0.6 : 0.4; }
    function min(n) { return n <= 20 ? 25 : n <= 50 ? 50 : 75; }
    var EN = (document.documentElement.lang || '').indexOf('en') === 0;
    var T = EN ? { yr: ' per year', min: ' → minimum ', mo: ' · about ', pm: ' a month', h1: ' hour', h: ' hours', m1: ' minute', m: ' minutes', and: ' ', ie: 'As a rule, required from 50 employees upwards.',
                     ta: 'Safety technician', iep: 'Occupational physician', d1: ' day', d: ' days', fr: ' for ', dh: 'Pick the contract start and end dates for a pro-rata calculation of the hours.', bad: 'The end date must be on or after the start date.',
                     cat: { A: 'A', B: 'B', C: 'C' }, none: 'Enter the number of employees in at least one category.' }
               : { yr: ' ετησίως', min: ' → ελάχιστο ', mo: ' · περίπου ', pm: ' τον μήνα', h1: ' ώρα', h: ' ώρες', m1: ' λεπτό', m: ' λεπτά', and: ' και ', ie: 'Κατά κανόνα απαιτείται από 50 εργαζόμενους και πάνω.',
                     ta: 'Τεχνικός Ασφαλείας', iep: 'Ιατρός Εργασίας', d1: ' ημέρα', d: ' ημέρες', fr: ' για ', dh: 'Επιλέξτε έναρξη και λήξη της σύμβασης για αναλογικό υπολογισμό των ωρών.', bad: 'Η ημερομηνία λήξης πρέπει να είναι ίδια ή μεταγενέστερη της έναρξης.',
                     cat: { A: 'Α΄', B: 'Β΄', C: 'Γ΄' }, none: 'Συμπληρώστε εργαζόμενους σε τουλάχιστον μία κατηγορία.' };
    var dFrom = document.getElementById('calcFrom'), dTo = document.getElementById('calcTo'), daysOut = document.getElementById('calcDaysOut');
    /* "YYYY-MM-DD" σε ms (UTC, ώστε η αλλαγή ώρας να μη χαλάει τη διαφορά ημερών) */
    function ymd(v) { var p = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v || ''); return p ? Date.UTC(+p[1], p[2] - 1, +p[3]) : 0; }
    function fmt(x) { return (Math.round(x * 10) / 10).toLocaleString(EN ? 'en-GB' : 'el-GR'); }
    /* ώρες σε "Χ ώρες και Υ λεπτά", ποτέ δεκαδικές ώρες */
    function hm(x) {
        var t = Math.round(x * 60), h = Math.floor(t / 60), m = t % 60;
        var hs = h.toLocaleString(EN ? 'en-GB' : 'el-GR') + (h === 1 ? T.h1 : T.h), ms = m + (m === 1 ? T.m1 : T.m);
        return !m ? hs : !h ? ms : hs + T.and + ms;
    }
    function count(el) { return Math.max(0, Math.min(100000, parseInt(el.value, 10) || 0)); }
    var sent = false;
    function run() {
        /* μικτή επιχείρηση: κάθε κατηγορία με τους δικούς της εργαζόμενους και συντελεστή,
           άθροισμα ωρών, ελάχιστο και υποχρέωση Ιατρού Εργασίας με βάση το σύνολο των εργαζομένων */
        var groups = [], n = 0, ta = 0, ie = 0;
        CATS.forEach(function (c) {
            var k = count(inp[c]);
            if (!k) return;
            groups.push({ c: c, k: k });
            n += k; ta += k * coefTA(c, k); ie += k * coefIE(c);
        });
        var taEl = document.getElementById('calcTA'), taSub = document.getElementById('calcTAsub'),
            ieEl = document.getElementById('calcIE'), ieSub = document.getElementById('calcIEsub');
        if (!n) {
            taEl.textContent = ieEl.textContent = '-';
            taSub.textContent = T.none; ieSub.textContent = '';
            if (daysOut) daysOut.textContent = T.dh;
            return;
        }
        function calc(coef) {
            return groups.map(function (g) { return (groups.length > 1 ? T.cat[g.c] + ' ' : '') + g.k + ' × ' + fmt(coef(g.c, g.k)); }).join(' + ');
        }
        var taH = Math.max(ta, min(n));
        taEl.textContent = hm(taH) + T.yr;
        taSub.textContent = calc(coefTA) + ' = ' + hm(ta) + (ta < min(n) ? T.min + hm(min(n)) : '') + T.mo + hm(taH / 12) + T.pm;
        var ieH = 0;
        if (n >= 50) {
            ieH = Math.max(ie, min(n));
            ieEl.textContent = hm(ieH) + T.yr;
            ieSub.textContent = calc(coefIE) + ' = ' + hm(ie) + (ie < min(n) ? T.min + hm(min(n)) : '');
        } else {
            ieEl.textContent = '-';
            ieSub.textContent = T.ie;
        }
        /* αναλογικός υπολογισμός βάσει σύμβασης: ετήσιες ώρες × ημέρες (Από-Μέχρι, και οι δύο μετράνε) / 365 */
        if (dFrom && dTo && daysOut) {
            var a = ymd(dFrom.value), b = ymd(dTo.value), d = a && b ? Math.round((b - a) / 864e5) + 1 : 0;
            if (a && b && d < 1) {
                daysOut.textContent = T.bad;
            } else if (d > 0) {
                var out = T.ta + ': <strong>' + hm(taH * d / 365) + '</strong>';
                if (ieH) out += ' · ' + T.iep + ': <strong>' + hm(ieH * d / 365) + '</strong>';
                daysOut.innerHTML = out + T.fr + d + (d === 1 ? T.d1 : T.d);
            } else {
                daysOut.textContent = T.dh;
            }
        }
        if (!sent && window.ccEvent) { sent = true; window.ccEvent('calc_use', { category: groups.length > 1 ? 'mixed' : groups[0].c }); }
    }
    CATS.forEach(function (c) { inp[c].addEventListener('input', run); });
    if (dFrom && dTo) {
        dFrom.addEventListener('input', function () { dTo.min = dFrom.value; run(); });
        dTo.addEventListener('input', run);
    }
    run();
})();
