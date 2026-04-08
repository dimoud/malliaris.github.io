/**
 * safety-animations.js  v2
 * Safety & H&S themed animations — modular, reusable, drop-in.
 *
 * Features:
 *   A. ComplianceGauge   — quiz-driven SVG gauge (replaces auto-animate)
 *   B. SafetyQuiz        — interactive H&S self-assessment game
 *   C. HelmetWidget      — animated SVG hard hat (bob + tilt)
 *   D. CraneWidget       — SVG crane with swinging jib arm
 *
 * HTML hooks:
 *   #complianceGauge     → contains #gaugeArcFill, #gaugeNeedle, #gaugeValue
 *   #sqQuestions         → empty div — quiz questions injected here
 *   #sqGaugeTitle        → title text node (updated on lang change)
 *   #sqStatus            → status message node
 *   #helmetWrap          → contains a <svg> element
 *   #craneWrap           → contains SVG with #craneArm group
 */

(function () {
    'use strict';

    /* ─── HELPERS ────────────────────────────────────────────────────────── */
    function $(id) { return document.getElementById(id); }

    function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
    }

    function onReady(fn) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fn);
        } else {
            fn();
        }
    }

    function onceVisible(el, callback, threshold) {
        if (!el) return;
        if (!('IntersectionObserver' in window)) { callback(); return; }
        var obs = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    obs.unobserve(entry.target);
                    callback();
                }
            });
        }, { threshold: threshold || 0.2 });
        obs.observe(el);
    }

    function getLang() {
        if (window.I18n && typeof window.I18n.getLang === 'function') {
            return window.I18n.getLang();
        }
        return 'el';
    }

    /* ─── A. COMPLIANCE GAUGE (quiz-driven) ──────────────────────────────── */
    /*
     * Semi-circular SVG gauge driven by quiz answers.
     * Arc: M 28 100 A 72 72 0 0 1 172 100  (half-circle, length ≈ 226.2px)
     * Needle: rotate(-90..+90 deg) around cx=100 cy=100
     */
    var GAUGE_ARC_LENGTH = Math.PI * 72; /* ≈ 226.195 */

    var gaugeArc        = null;
    var gaugeNeedle     = null;
    var gaugeValue      = null;
    var gaugeAnimId     = null;
    var gaugeCurrentPct = 0;

    function getScoreColor(pct) {
        if (pct >= 84) return '#2DAA6E';   /* green  — great / perfect */
        if (pct >= 42) return '#F09030';   /* amber  — good / medium   */
        return '#E8541A';                  /* orange — low             */
    }

    function applyGaugeValue(pct) {
        var filled = (pct / 100) * GAUGE_ARC_LENGTH;
        var gap    = GAUGE_ARC_LENGTH - filled;

        if (gaugeArc) {
            gaugeArc.style.strokeDasharray = filled + ' ' + gap;
            gaugeArc.style.stroke = pct > 0 ? getScoreColor(pct) : '#E8541A';
        }
        if (gaugeNeedle) {
            var angle = -90 + (pct / 100) * 180;
            gaugeNeedle.setAttribute('transform', 'rotate(' + angle + ' 100 100)');
        }
        if (gaugeValue) {
            gaugeValue.textContent = Math.round(pct) + '%';
        }
    }

    function animateGaugeTo(target) {
        if (gaugeAnimId) cancelAnimationFrame(gaugeAnimId);
        var DURATION = 550;
        var start    = null;
        var from     = gaugeCurrentPct;

        function step(ts) {
            if (!start) start = ts;
            var p = Math.min((ts - start) / DURATION, 1);
            var e = easeOutCubic(p);
            applyGaugeValue(from + (target - from) * e);
            if (p < 1) {
                gaugeAnimId = requestAnimationFrame(step);
            } else {
                applyGaugeValue(target);
                gaugeCurrentPct = target;
                gaugeAnimId = null;
            }
        }
        gaugeAnimId = requestAnimationFrame(step);
    }

    function initGauge() {
        var gaugeEl = $('complianceGauge');
        if (!gaugeEl) return;
        gaugeArc    = $('gaugeArcFill');
        gaugeNeedle = $('gaugeNeedle');
        gaugeValue  = $('gaugeValue');
        applyGaugeValue(0);
    }

    /* ─── B. SAFETY QUIZ ─────────────────────────────────────────────────── */
    /*
     * Self-assessment game. 6 real H&S questions × 14 pts + 1 Stavros × 16 pts = 100%.
     * Only by working with Stavros Malliaris can the user reach 100%.
     * Gauge animates on each checkbox change. Status message & color update live.
     */

    var QUIZ_QUESTIONS = [
        {
            el: 'Έχετε εκπονήσει Γραπτή Εκτίμηση Επαγγελματικού Κινδύνου (ΓΕΕΚ);',
            en: 'Do you have a Written Occupational Risk Assessment (GEEK)?',
            pts: 14
        },
        {
            el: 'Εκπαιδεύονται τακτικά οι εργαζόμενοι σε θέματα Υγείας & Ασφάλειας;',
            en: 'Are employees regularly trained on Health & Safety topics?',
            pts: 14
        },
        {
            el: 'Υπάρχει σχέδιο εκκένωσης και γίνονται ασκήσεις ετοιμότητας;',
            en: 'Do you have an evacuation plan with regular emergency drills?',
            pts: 14
        },
        {
            el: 'Διαθέτουν οι εργαζόμενοι κατάλληλα ΜΑΠ (Μέσα Ατομικής Προστασίας);',
            en: 'Do employees have appropriate PPE (Personal Protective Equipment)?',
            pts: 14
        },
        {
            el: 'Υπάρχει σήμανση ασφαλείας σε όλους τους χώρους εργασίας;',
            en: 'Is safety signage displayed throughout all work areas?',
            pts: 14
        },
        {
            el: 'Γνωρίζετε τις υποχρεώσεις σας βάσει του Ν. 3850/2010;',
            en: 'Are you aware of your obligations under Law N.3850/2010?',
            pts: 14
        },
        {
            el: 'Συνεργάζεστε με τον Σταύρο Μάλλιαρη;',
            en: 'Do you work with Stavros Malliaris?',
            pts: 16,
            stavros: true
        }
    ];

    var QUIZ_STATUS = {
        empty:   { el: '',                                                          en: '' },
        low:     { el: 'Υψηλός κίνδυνος — απαιτείται άμεση δράση',                en: 'High risk — immediate action required' },
        medium:  { el: 'Χρειάζεται βελτίωση',                                      en: 'Needs improvement' },
        good:    { el: 'Καλή πρόοδος — υπάρχουν ακόμα κενά',                       en: 'Good progress — some gaps remain' },
        great:   { el: 'Εξαιρετική συμμόρφωση!',                                   en: 'Excellent compliance!' },
        perfect: { el: '🛡️ Πλήρης κάλυψη — μαζί με τον Σταύρο Μάλλιαρη!',        en: '🛡️ Full coverage — with Stavros Malliaris!' }
    };

    var QUIZ_TITLE = {
        el: 'ΤΟ ΕΠΙΠΕΔΟ ΑΣΦΑΛΕΙΑΣ ΣΑΣ',
        en: 'YOUR SAFETY LEVEL'
    };

    function getStatusKey(pct) {
        if (pct === 0)   return 'empty';
        if (pct === 100) return 'perfect';
        if (pct >= 70)   return 'great';
        if (pct >= 42)   return 'good';
        if (pct >= 14)   return 'medium';
        return 'low';
    }

    function updateQuizStatus(pct) {
        var statusEl = $('sqStatus');
        if (!statusEl) return;
        var key  = getStatusKey(pct);
        var lang = getLang();
        statusEl.textContent = QUIZ_STATUS[key][lang];
        statusEl.className   = 'sq-status sq-status--' + key;
    }

    function getCheckedScore() {
        var total = 0;
        var checks = document.querySelectorAll('.sq-check:checked');
        checks.forEach(function (cb) {
            var idx = parseInt(cb.getAttribute('data-idx'), 10);
            if (!isNaN(idx) && QUIZ_QUESTIONS[idx]) {
                total += QUIZ_QUESTIONS[idx].pts;
            }
        });
        return Math.min(total, 100);
    }

    function onQuizChange() {
        var score = getCheckedScore();
        animateGaugeTo(score);
        updateQuizStatus(score);
    }

    function makeBadgeHtml(lang) {
        return '<span class="sq-stavros-badge">' + (lang === 'el' ? '⭐ Κλειδί' : '⭐ Key') + '</span>';
    }

    function buildQuiz() {
        var container = $('sqQuestions');
        if (!container) return;
        var lang = getLang();
        container.innerHTML = '';

        QUIZ_QUESTIONS.forEach(function (q, i) {
            var label = document.createElement('label');
            label.className = 'sq-item' + (q.stavros ? ' sq-item--stavros' : '');
            label.innerHTML =
                '<input type="checkbox" class="sq-check" data-idx="' + i + '">' +
                '<span class="sq-checkmark"></span>' +
                '<span class="sq-text">' + q[lang] + (q.stavros ? makeBadgeHtml(lang) : '') + '</span>';
            container.appendChild(label);
        });

        container.querySelectorAll('.sq-check').forEach(function (cb) {
            cb.addEventListener('change', onQuizChange);
        });

        /* Set gauge title */
        var titleEl = $('sqGaugeTitle');
        if (titleEl) titleEl.innerHTML = '<strong>' + QUIZ_TITLE[lang] + '</strong>';
    }

    function rebuildQuizTexts() {
        /* Update question text while preserving checkbox states */
        var lang = getLang();
        var items = document.querySelectorAll('.sq-item');
        items.forEach(function (item, i) {
            var q = QUIZ_QUESTIONS[i];
            if (!q) return;
            var textEl = item.querySelector('.sq-text');
            if (!textEl) return;
            textEl.innerHTML = q[lang] + (q.stavros ? makeBadgeHtml(lang) : '');
        });
        var titleEl = $('sqGaugeTitle');
        if (titleEl) titleEl.innerHTML = '<strong>' + QUIZ_TITLE[lang] + '</strong>';
        updateQuizStatus(gaugeCurrentPct);
    }

    function initQuiz() {
        var container = $('sqQuestions');
        if (!container) return;
        buildQuiz();

        /* Hook into language switcher */
        var _origSetLang = window.setLang;
        if (typeof _origSetLang === 'function') {
            window.setLang = function (lang) {
                _origSetLang.apply(this, arguments);
                setTimeout(rebuildQuizTexts, 20);
            };
        }
    }

    /* ─── C. HELMET WIDGET ───────────────────────────────────────────────── */
    var helmetAnimId = null;
    var helmetActive = false;

    function initHelmet() {
        var helmetWrap = $('helmetWrap');
        if (!helmetWrap) return;
        var svg = helmetWrap.querySelector('svg');
        if (!svg) return;
        onceVisible(helmetWrap, function () {
            helmetActive = true;
            animateHelmet(svg);
        }, 0.3);
    }

    function animateHelmet(svg) {
        if (!helmetActive) return;
        var BOB_AMPLITUDE = 4;
        var BOB_PERIOD    = 3000;
        var TILT_DEGREES  = 3;
        var startTime     = null;

        function step(ts) {
            if (!helmetActive) return;
            if (!startTime) startTime = ts;
            var sinVal = Math.sin(((ts - startTime) / BOB_PERIOD) * Math.PI * 2);
            svg.style.transform =
                'translateY(' + (sinVal * BOB_AMPLITUDE).toFixed(2) + 'px) ' +
                'rotate(' + (sinVal * TILT_DEGREES).toFixed(2) + 'deg)';
            helmetAnimId = requestAnimationFrame(step);
        }
        helmetAnimId = requestAnimationFrame(step);
    }

    /* ─── D. CRANE WIDGET ────────────────────────────────────────────────── */
    var craneAnimId = null;
    var craneActive = false;

    function initCrane() {
        var craneWrap = $('craneWrap');
        if (!craneWrap) return;
        var craneArm = $('craneArm');
        if (!craneArm) return;
        onceVisible(craneWrap, function () {
            craneActive = true;
            animateCrane(craneArm);
        }, 0.2);
    }

    function animateCrane(craneArm) {
        if (!craneActive) return;
        var SWING_DEGREES = 18;
        var SWING_PERIOD  = 6000;
        var PIVOT_X       = 93;
        var PIVOT_Y       = 68;
        var startTime     = null;

        function step(ts) {
            if (!craneActive) return;
            if (!startTime) startTime = ts;
            var angle = Math.sin(((ts - startTime) / SWING_PERIOD) * Math.PI * 2) * SWING_DEGREES;
            craneArm.setAttribute('transform',
                'rotate(' + angle.toFixed(3) + ' ' + PIVOT_X + ' ' + PIVOT_Y + ')');
            craneAnimId = requestAnimationFrame(step);
        }
        craneAnimId = requestAnimationFrame(step);
    }

    /* ─── INIT ───────────────────────────────────────────────────────────── */
    onReady(function () {
        initGauge();
        initQuiz();
        initHelmet();
        initCrane();
    });

    /* ─── PUBLIC API ─────────────────────────────────────────────────────── */
    window.SafetyAnimations = {
        refresh: function () {
            initGauge();
            initQuiz();
            initHelmet();
            initCrane();
        },
        resetGauge: function () {
            gaugeCurrentPct = 0;
            applyGaugeValue(0);
        },
        stop: function () {
            helmetActive = false;
            craneActive  = false;
            if (helmetAnimId) { cancelAnimationFrame(helmetAnimId); helmetAnimId = null; }
            if (craneAnimId)  { cancelAnimationFrame(craneAnimId);  craneAnimId  = null; }
            if (gaugeAnimId)  { cancelAnimationFrame(gaugeAnimId);  gaugeAnimId  = null; }
        }
    };

})();
