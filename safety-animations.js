/**
 * safety-animations.js  v1
 * Safety & H&S themed animations — modular, reusable, drop-in.
 * Each feature activates only if its HTML hook exists.
 *
 * Features:
 *   A. ComplianceGauge   — semi-circular SVG gauge sweeps to target %
 *   B. ChecklistTicker   — checklist items tick off one by one on scroll
 *   C. HelmetWidget      — animated SVG safety hard hat, gentle bob + tilt
 *   D. CraneWidget       — SVG construction crane with swinging jib arm
 *
 * Required HTML hooks (all optional — animation skips if element absent):
 *   #complianceGauge [data-target]  → contains #gaugeArcFill, #gaugeNeedle, #gaugeValue
 *   [data-checklist-container]      → contains .cl-item children
 *   #helmetWrap                     → contains a <svg> element
 *   #craneWrap                      → contains SVG with #craneArm group
 *
 * Usage:
 *   <script src="safety-animations.js"></script>
 *   (no configuration needed — drop in and go)
 *
 * Public API:
 *   window.SafetyAnimations.refresh()     — re-trigger IntersectionObserver checks
 *   window.SafetyAnimations.resetGauge()  — reset gauge to 0 and re-animate
 */

(function () {
    'use strict';

    /* ─── HELPERS ────────────────────────────────────────────────────────── */
    function $(id) { return document.getElementById(id); }

    function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
    }

    /* Run fn when DOM is ready */
    function onReady(fn) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fn);
        } else {
            fn();
        }
    }

    /* Create a simple IntersectionObserver that fires once per element */
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

    /* ─── A. COMPLIANCE GAUGE ────────────────────────────────────────────── */
    /*
     * Semi-circular SVG gauge. HTML hook: #complianceGauge with data-target="92"
     * Children: #gaugeArcFill (path), #gaugeNeedle (line), #gaugeValue (text)
     *
     * Geometry:
     *   cx=100, cy=100, r=72  →  half-circle arc from 9 o'clock (180°) to 3 o'clock (0°)
     *   Arc path: M 28 100 A 72 72 0 0 1 172 100
     *   Full arc length = π * r = π * 72 ≈ 226.2px  (half of circumference)
     *   stroke-dasharray: <filled> <gap>  where filled = (pct/100) * 226.2
     *
     * Needle:
     *   At 0%  → points left  (rotate(-90 100 100) → -90°)
     *   At 50% → points up    (rotate(  0 100 100) →   0°)
     *   At 100%→ points right (rotate( 90 100 100) → +90°)
     *   angle  = -90 + (pct / 100) * 180
     */

    var GAUGE_ARC_LENGTH = Math.PI * 72; /* ≈ 226.195 */

    var gaugeEl    = null;
    var gaugeArc   = null;
    var gaugeNeedle= null;
    var gaugeValue = null;
    var gaugeTarget= 0;
    var gaugeAnimId= null;

    function initGauge() {
        gaugeEl = $('complianceGauge');
        if (!gaugeEl) return;

        gaugeArc    = $('gaugeArcFill');
        gaugeNeedle = $('gaugeNeedle');
        gaugeValue  = $('gaugeValue');
        gaugeTarget = parseInt(gaugeEl.getAttribute('data-target') || '92', 10);

        /* Reset to 0 */
        applyGaugeValue(0);

        onceVisible(gaugeEl, animateGauge, 0.3);
    }

    function applyGaugeValue(pct) {
        var filled = (pct / 100) * GAUGE_ARC_LENGTH;
        var gap    = GAUGE_ARC_LENGTH - filled;

        if (gaugeArc) {
            gaugeArc.style.strokeDasharray  = filled + ' ' + gap;
            gaugeArc.style.strokeDashoffset = '0';
        }
        if (gaugeNeedle) {
            var angle = -90 + (pct / 100) * 180;
            gaugeNeedle.setAttribute('transform', 'rotate(' + angle + ' 100 100)');
        }
        if (gaugeValue) {
            gaugeValue.textContent = Math.round(pct) + '%';
        }
    }

    function animateGauge() {
        if (gaugeAnimId) cancelAnimationFrame(gaugeAnimId);
        var DURATION = 2000; /* ms */
        var start    = null;

        function step(ts) {
            if (!start) start = ts;
            var elapsed = ts - start;
            var progress = Math.min(elapsed / DURATION, 1);
            var eased    = easeOutCubic(progress);
            var current  = eased * gaugeTarget;

            applyGaugeValue(current);

            if (progress < 1) {
                gaugeAnimId = requestAnimationFrame(step);
            } else {
                applyGaugeValue(gaugeTarget);
                gaugeAnimId = null;
            }
        }

        gaugeAnimId = requestAnimationFrame(step);
    }

    /* ─── B. CHECKLIST TICKER ────────────────────────────────────────────── */
    /*
     * HTML hook: element with data-checklist-container attribute.
     * Children: .cl-item  (CSS handles visual: opacity 0 → 1, translateX(-10px) → 0)
     * On scroll entry, adds .cl-done to each item with 280ms stagger.
     */

    var CHECKLIST_STAGGER = 280; /* ms between items */

    function initChecklist() {
        var containers = document.querySelectorAll('[data-checklist-container]');
        if (!containers.length) return;

        containers.forEach(function (container) {
            var items = container.querySelectorAll('.cl-item');
            if (!items.length) return;

            onceVisible(container, function () {
                items.forEach(function (item, idx) {
                    setTimeout(function () {
                        item.classList.add('cl-done');
                    }, idx * CHECKLIST_STAGGER);
                });
            }, 0.2);
        });
    }

    /* ─── C. HELMET WIDGET ───────────────────────────────────────────────── */
    /*
     * HTML hook: #helmetWrap containing a <svg> element.
     * Animation: gentle sin-wave vertical bob (amplitude 4px, period 3000ms)
     *            + slight ±3deg rotation synchronized with bob.
     * Uses requestAnimationFrame. Starts only when element enters viewport.
     */

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

        var BOB_AMPLITUDE = 4;    /* px */
        var BOB_PERIOD    = 3000; /* ms */
        var TILT_DEGREES  = 3;    /* max degrees */
        var startTime     = null;

        function step(ts) {
            if (!helmetActive) return;
            if (!startTime) startTime = ts;
            var elapsed = ts - startTime;
            var phase   = (elapsed / BOB_PERIOD) * Math.PI * 2;
            var sinVal  = Math.sin(phase);

            var translateY = sinVal * BOB_AMPLITUDE;
            var rotate     = sinVal * TILT_DEGREES;

            svg.style.transform = 'translateY(' + translateY.toFixed(2) + 'px) rotate(' + rotate.toFixed(2) + 'deg)';

            helmetAnimId = requestAnimationFrame(step);
        }

        helmetAnimId = requestAnimationFrame(step);
    }

    /* ─── D. CRANE WIDGET ────────────────────────────────────────────────── */
    /*
     * HTML hook: #craneWrap containing SVG with #craneArm group.
     * Animation: jib swings pendulum-style ±18° around tower top with 6s period.
     * The craneArm group has transform-origin at the tower top (cx=93, cy=68 in SVG coords).
     * Uses requestAnimationFrame. Starts when element enters viewport.
     */

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

        var SWING_DEGREES = 18;   /* ± degrees */
        var SWING_PERIOD  = 6000; /* ms — full cycle */
        var startTime     = null;

        /* Pivot point in SVG local coordinates (tower top / mast base) */
        var PIVOT_X = 93;
        var PIVOT_Y = 68;

        function step(ts) {
            if (!craneActive) return;
            if (!startTime) startTime = ts;
            var elapsed = ts - startTime;
            var phase   = (elapsed / SWING_PERIOD) * Math.PI * 2;

            /* sin-wave swing */
            var angle = Math.sin(phase) * SWING_DEGREES;

            /* SVG transform: rotate around the pivot point */
            craneArm.setAttribute(
                'transform',
                'rotate(' + angle.toFixed(3) + ' ' + PIVOT_X + ' ' + PIVOT_Y + ')'
            );

            craneAnimId = requestAnimationFrame(step);
        }

        craneAnimId = requestAnimationFrame(step);
    }

    /* ─── INIT ───────────────────────────────────────────────────────────── */
    onReady(function () {
        initGauge();
        initChecklist();
        initHelmet();
        initCrane();
    });

    /* ─── PUBLIC API ─────────────────────────────────────────────────────── */
    window.SafetyAnimations = {
        /** Re-run all IntersectionObserver setups (call if DOM changed) */
        refresh: function () {
            initGauge();
            initChecklist();
            initHelmet();
            initCrane();
        },

        /** Reset and re-animate the compliance gauge */
        resetGauge: function () {
            if (!gaugeEl) return;
            if (gaugeAnimId) cancelAnimationFrame(gaugeAnimId);
            applyGaugeValue(0);
            setTimeout(animateGauge, 100);
        },

        /** Stop all rAF animations */
        stop: function () {
            helmetActive = false;
            craneActive  = false;
            if (helmetAnimId) { cancelAnimationFrame(helmetAnimId); helmetAnimId = null; }
            if (craneAnimId)  { cancelAnimationFrame(craneAnimId);  craneAnimId  = null; }
            if (gaugeAnimId)  { cancelAnimationFrame(gaugeAnimId);  gaugeAnimId  = null; }
        },
    };

})();
