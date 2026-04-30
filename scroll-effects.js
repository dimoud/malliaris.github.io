/**
 * scroll-effects.js — Smooth scroll animations, NO skew, NO heavy effects
 */
(function () {
    'use strict';

    var io = 'IntersectionObserver' in window;
    var reducedMotion = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

    function once(el, fn, opts) {
        if (!io || reducedMotion) { fn(el); return; }
        var obs = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) { fn(e.target); obs.unobserve(e.target); }
            });
        }, opts || { threshold: 0.12 });
        obs.observe(el);
    }
    function qAll(sel, ctx) { return Array.prototype.slice.call((ctx||document).querySelectorAll(sel)); }
    function q(sel) { return document.querySelector(sel); }
    function rAF(fn) { requestAnimationFrame(fn); }

    /* ── A. HERO LOAD SEQUENCE — staggered fade-up ── */
    (function() {
        var items = [
            { sel: '.hero-credential',  delay: 60  },
            { sel: '.hero-name .line1', delay: 160 },
            { sel: '.hero-name .line2', delay: 280 },
            { sel: '.hero-eyebrow',     delay: 400 },
            { sel: '.btn-accent',       delay: 520 },
            { sel: '.hero-stats',       delay: 640 },
            { sel: '.live-badge',       delay: 760 },
            { sel: '.hero-scroll-hint', delay: 960 },
        ];
        items.forEach(function(item) {
            var el = q(item.sel);
            if (!el) return;
            el.classList.add('sx-load');
            setTimeout(function() { el.classList.add('sx-load-in'); }, item.delay);
        });
        var photo = q('.hero-photo-wrap');
        if (photo) {
            photo.classList.add('sx-load');
            setTimeout(function() { photo.classList.add('sx-load-in'); }, 100);
        }
    })();

    /* ── B. SCROLL PROGRESS BAR ── */
    (function() {
        var bar = document.createElement('div');
        bar.className = 'sx-progress-bar';
        bar.setAttribute('aria-hidden', 'true');
        document.body.appendChild(bar);
        window.addEventListener('scroll', function() {
            var total = document.documentElement.scrollHeight - window.innerHeight;
            bar.style.width = (total > 0 ? window.scrollY / total * 100 : 0) + '%';
        }, { passive: true });
    })();

    /* ── C. GENERAL FADE-UP for all [data-sx] elements ── */
    (function() {
        qAll('[data-sx]').forEach(function(el) {
            var delay = parseInt(el.getAttribute('data-sx-delay') || '0', 10);
            el.classList.add('sx-up');
            once(el, function(t) {
                setTimeout(function() { t.classList.add('sx-up-go'); }, delay);
            });
        });
    })();

    /* ── D. FEATURE ROWS — staggered slide-in ── */
    (function() {
        qAll('.feature-row').forEach(function(row, i) {
            row.classList.add('sx-feature');
            once(row, function(el) {
                setTimeout(function() { el.classList.add('sx-feature-go'); }, i * 100);
            });
        });
    })();

    /* ── E. RESOURCE CARDS — staggered fade-up ── */
    (function() {
        qAll('.resources-grid .resource-card').forEach(function(card, i) {
            card.classList.add('sx-card');
            once(card, function(el) {
                setTimeout(function() { el.classList.add('sx-card-go'); }, (i % 4) * 70 + Math.floor(i / 4) * 50);
            });
        });
    })();

    /* ── F. EYEBROW WIPE ── */
    (function() {
        qAll('.eyebrow').forEach(function(el) {
            el.classList.add('sx-eyebrow');
            once(el, function(t) { t.classList.add('sx-eyebrow-go'); });
        });
    })();

    /* ── G. SECTION HEADINGS — fade+rise ── */
    (function() {
        qAll('.section-heading').forEach(function(el) {
            el.classList.add('sx-heading');
            once(el, function(t) { t.classList.add('sx-heading-go'); }, { threshold: 0.1 });
        });
    })();

    /* ── H. GOAL SHIELD SVG DRAW ── */
    (function() {
        var shield = q('.goal-shield-outer');
        var check  = q('.goal-check');
        if (!shield) return;
        var slen = shield.getTotalLength ? shield.getTotalLength() : 300;
        shield.style.strokeDasharray  = slen;
        shield.style.strokeDashoffset = slen;
        shield.style.transition = 'stroke-dashoffset 1.3s cubic-bezier(.4,0,.2,1) 0.1s';
        if (check) {
            var clen = check.getTotalLength ? check.getTotalLength() : 60;
            check.style.strokeDasharray  = clen;
            check.style.strokeDashoffset = clen;
            check.style.transition = 'stroke-dashoffset 0.6s cubic-bezier(.4,0,.2,1) 1.3s';
        }
        var wrap = q('.goal-section') || q('#goalSection');
        if (wrap) {
            once(wrap, function() {
                shield.style.strokeDashoffset = '0';
                if (check) check.style.strokeDashoffset = '0';
                qAll('.goal-stat-num[data-goal-count]').forEach(function(el) {
                    var target = parseInt(el.getAttribute('data-goal-count'), 10);
                    var suffix = el.getAttribute('data-goal-suffix') || '';
                    var dur = 1600, start = null;
                    function ease(t) { return 1 - Math.pow(1 - t, 3); }
                    (function step(ts) {
                        if (!start) start = ts;
                        var p = Math.min((ts - start) / dur, 1);
                        el.textContent = Math.round(ease(p) * target) + suffix;
                        if (p < 1) rAF(step);
                    })(performance.now());
                });
            }, { threshold: 0.3 });
        }
    })();

    /* ── I. CONTACT SECTION slide from sides ── */
    (function() {
        var info = q('.contact-info');
        var form = q('.contact-form-wrap');
        if (info) {
            info.classList.add('sx-from-left');
            once(info, function(t) { t.classList.add('sx-from-left-go'); });
        }
        if (form) {
            form.classList.add('sx-from-right');
            once(form, function(t) { setTimeout(function() { t.classList.add('sx-from-right-go'); }, 100); });
        }
    })();

    /* ── J. STAT COUNTUP ── */
    (function() {
        qAll('[data-countup]').forEach(function(el) {
            once(el, function(t) {
                var target = parseFloat(t.getAttribute('data-countup'));
                var suffix = t.getAttribute('data-suffix') || '';
                var dur = 1600, start = null;
                function ease(p) { return 1 - Math.pow(1 - p, 3); }
                (function step(ts) {
                    if (!start) start = ts;
                    var p = Math.min((ts - start) / dur, 1);
                    t.textContent = Math.round(ease(p) * target) + suffix;
                    if (p < 1) rAF(step);
                })(performance.now());
            }, { threshold: 0.5 });
        });
    })();

    /* ── K. MAGNETIC BUTTON (subtle) ── */
    (function() {
        if (window.matchMedia('(hover:none)').matches) return;
        qAll('.btn-accent').forEach(function(btn) {
            btn.addEventListener('mousemove', function(e) {
                var r = btn.getBoundingClientRect();
                var x = (e.clientX - r.left - r.width  / 2) * 0.18;
                var y = (e.clientY - r.top  - r.height / 2) * 0.18;
                btn.style.transform = 'translate(' + x + 'px,' + y + 'px)';
            });
            btn.addEventListener('mouseleave', function() {
                btn.style.transform = '';
            });
        });
    })();

    /* ── L. RESOURCE ICON SPIN on hover ── */
    (function() {
        qAll('.resource-card .resource-icon').forEach(function(icon) {
            var card = icon.closest('.resource-card');
            if (!card) return;
            card.addEventListener('mouseenter', function() {
                icon.classList.add('sx-spin');
            });
            icon.addEventListener('animationend', function() {
                icon.classList.remove('sx-spin');
            });
        });
    })();

    /* ── M. MARQUEE speed burst on scroll ── */
    (function() {
        var track = q('.marquee-track');
        if (!track) return;
        var base = 28, current = base, lastY = window.scrollY;
        window.addEventListener('scroll', function() {
            var dy = Math.abs(window.scrollY - lastY);
            lastY = window.scrollY;
            current = Math.max(8, base - dy * 0.5);
            track.style.animationDuration = current + 's';
        }, { passive: true });
    })();

    /* ── N. SECTORS HEADER in-view for CSS underline ── */
    (function() {
        var hdr = q('.sectors-header');
        if (!hdr) return;
        once(hdr, function(t) { t.classList.add('in-view'); }, { threshold: 0.2 });
    })();

})();
