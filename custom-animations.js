/**
 * custom-animations.js — Malliaris H&S
 * Infinite-scroll strips, 3D tilt, magnetic buttons, cursor glow, stagger reveals
 */
(function () {
    'use strict';

    /* ─── UTILITY ──────────────────────────────────────────────────────── */
    function qs(sel, ctx) { return (ctx || document).querySelector(sel); }
    function qsa(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }

    /* ─── 1. INFINITE STRIP — Sectors ─────────────────────────────────── */
    (function () {
        var wrap  = qs('#sectorsWrap');
        var track = qs('#sectorsTrack');
        if (!wrap || !track) return;

        /* Pause on hover */
        wrap.addEventListener('mouseenter', function () {
            track.style.animationPlayState = 'paused';
        });
        wrap.addEventListener('mouseleave', function () {
            track.style.animationPlayState = 'running';
        });

        /* Touch swipe: speed up briefly on swipe */
        var tx = 0;
        wrap.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
        wrap.addEventListener('touchend', function (e) {
            var diff = tx - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 30) {
                track.style.animationPlayState = 'running';
            }
        }, { passive: true });
    })();

    /* ─── 2. INFINITE STRIP — In Action ───────────────────────────────── */
    (function () {
        var wrap  = qs('#actionStripWrap');
        var strip = qs('#actionStrip');
        if (!wrap || !strip) return;

        wrap.addEventListener('mouseenter', function () {
            strip.style.animationPlayState = 'paused';
        });
        wrap.addEventListener('mouseleave', function () {
            strip.style.animationPlayState = 'running';
        });

        /* Touch pause on press */
        wrap.addEventListener('touchstart', function () {
            strip.style.animationPlayState = 'paused';
        }, { passive: true });
        wrap.addEventListener('touchend', function () {
            strip.style.animationPlayState = 'running';
        }, { passive: true });
    })();

    /* ─── 3. 3D TILT — Sector carousel cards ──────────────────────────── */
    qsa('[data-tilt]').forEach(function (card) {
        card.addEventListener('mousemove', function (e) {
            var rect = card.getBoundingClientRect();
            var cx   = rect.left + rect.width  / 2;
            var cy   = rect.top  + rect.height / 2;
            var dx   = (e.clientX - cx) / (rect.width  / 2);   /* -1 … +1 */
            var dy   = (e.clientY - cy) / (rect.height / 2);
            var rotX =  dy * -6;   /* tilt range ±6° */
            var rotY =  dx *  6;
            card.style.transform = 'perspective(700px) rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg) scale(1.03)';
            card.style.transition = 'transform 0.08s linear';
        });
        card.addEventListener('mouseleave', function () {
            card.style.transform = '';
            card.style.transition = 'transform 0.45s var(--ease, cubic-bezier(0.16,1,0.3,1))';
        });
    });

    /* ─── 4. SERVICE CARDS — 3D tilt lite ─────────────────────────────── */
    qsa('.service-card').forEach(function (card) {
        card.addEventListener('mousemove', function (e) {
            var rect = card.getBoundingClientRect();
            var dx = (e.clientX - rect.left - rect.width  / 2) / (rect.width  / 2);
            var dy = (e.clientY - rect.top  - rect.height / 2) / (rect.height / 2);
            card.style.transform = 'perspective(600px) rotateX(' + (dy * -3) + 'deg) rotateY(' + (dx * 3) + 'deg) translateY(-4px)';
            card.style.transition = 'transform 0.08s linear';
        });
        card.addEventListener('mouseleave', function () {
            card.style.transform = '';
            card.style.transition = 'transform 0.4s cubic-bezier(0.16,1,0.3,1)';
        });
    });

    /* ─── 5. MAGNETIC BUTTONS ──────────────────────────────────────────── */
    qsa('.btn-accent, .nav-cta, .calendly-cta, .back-to-top').forEach(function (btn) {
        btn.addEventListener('mousemove', function (e) {
            var rect = btn.getBoundingClientRect();
            var dx = e.clientX - rect.left - rect.width  / 2;
            var dy = e.clientY - rect.top  - rect.height / 2;
            btn.style.transform = 'translate(' + dx * 0.22 + 'px, ' + dy * 0.22 + 'px)';
            btn.style.transition = 'transform 0.15s linear';
        });
        btn.addEventListener('mouseleave', function () {
            btn.style.transform = '';
            btn.style.transition = 'transform 0.5s cubic-bezier(0.16,1,0.3,1)';
        });
    });

    /* ─── 6. HERO CURSOR GLOW ──────────────────────────────────────────── */
    (function () {
        var hero = qs('.hero');
        if (!hero) return;
        var glow = document.createElement('div');
        glow.id = 'heroCursorGlow';
        glow.style.cssText = [
            'position:absolute', 'pointer-events:none', 'z-index:4',
            'width:320px', 'height:320px', 'border-radius:50%',
            'background:radial-gradient(circle,rgba(45,170,110,0.12) 0%,transparent 70%)',
            'transform:translate(-50%,-50%)',
            'transition:opacity 0.4s', 'opacity:0', 'will-change:transform'
        ].join(';');
        hero.appendChild(glow);

        hero.addEventListener('mousemove', function (e) {
            var rect = hero.getBoundingClientRect();
            glow.style.left = (e.clientX - rect.left) + 'px';
            glow.style.top  = (e.clientY - rect.top)  + 'px';
            glow.style.opacity = '1';
        });
        hero.addEventListener('mouseleave', function () {
            glow.style.opacity = '0';
        });
    })();

    /* ─── 7. STAGGER REVEAL — service + resource cards ────────────────── */
    (function () {
        var cards = qsa('.service-card, .resource-card, .sector-carousel-card, .action-strip-item');
        cards.forEach(function (c, i) {
            c.style.transitionDelay = (i % 6) * 60 + 'ms';
        });
    })();

    /* ─── 8. COUNTER ANIMATION — hero stat1 (7+) ─────────────────────── */
    (function () {
        var el = qs('[data-countup]');
        if (!el) return; /* eng-animations handles this; skip if already handled */
    })();

    /* ─── 9. SCROLL PROGRESS GLOW ──────────────────────────────────────── */
    (function () {
        var prog = document.getElementById('progress');
        if (!prog) return;
        window.addEventListener('scroll', function () {
            var total = document.documentElement.scrollHeight - window.innerHeight;
            var pct   = total > 0 ? (window.scrollY / total) * 100 : 0;
            prog.style.width = pct + '%';
            prog.style.boxShadow = pct > 5 ? '0 0 8px rgba(45,170,110,0.5)' : '';
        }, { passive: true });
    })();

    /* ─── 10. FLOATING LABEL on scroll-hint ─────────────────────────────── */
    (function () {
        var hints = qsa('.scroll-hint-label');
        if (!hints.length) return;
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                e.target.style.opacity = e.isIntersecting ? '1' : '0';
            });
        }, { threshold: 0.5 });
        hints.forEach(function (h) {
            h.style.transition = 'opacity 0.5s';
            io.observe(h);
        });
    })();

})();
