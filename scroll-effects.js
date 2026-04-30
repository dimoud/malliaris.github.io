/**
 * scroll-effects.js — Rich scroll & load animation layer for malliaris site
 *
 * Effects:
 *  A. Hero load sequence  — staggered fade-up for name, eyebrow, CTA, stats
 *  B. Eyebrow line wipe   — [data-eyebrow-anim] orange underline draws across
 *  C. Heading blur-in     — [data-heading-anim] letters unblur + rise
 *  D. Section divider     — [data-line-draw] horizontal rule draws left→right
 *  E. Stat counters       — [data-countup] elements count up when visible
 *  F. Feature row pop     — .feature-row staggered slide+scale with icon spin
 *  G. Card cascade        — .resource-card perspective flip-in stagger
 *  H. Floating particles  — hero background subtle drifting dots
 *  I. Section bg parallax — section backgrounds shift at 0.15× scroll speed
 *  J. Tilt on hover       — [data-tilt] cards follow mouse in 3D
 *  K. Marquee speed burst — marquee speeds up when scrolling past it
 *  L. Magnetic buttons    — .btn-accent follows cursor slightly
 *  M. Scroll-triggered    — general [data-sx] with stagger, scale, rotate, clip variants
 *  N. Number ticker       — hero stat numbers animate on load
 *  O. Goal shield draw    — SVG stroke-dashoffset draw when visible
 *  P. Typewriter quote    — goal quote types letter by letter
 */

(function () {
    'use strict';

    var io = 'IntersectionObserver' in window;

    /* ─── HELPERS ─────────────────────────────────────────────────────────── */
    function observe(els, fn, opts) {
        if (!io) { els.forEach(function(el){ fn(el, true); }); return; }
        var obs = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) { fn(e.target, e.isIntersecting, obs); });
        }, opts || { threshold: 0.12 });
        els.forEach(function(el) { obs.observe(el); });
        return obs;
    }
    function once(el, fn, opts) {
        if (!io) { fn(el); return; }
        var obs = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) { fn(e.target); obs.unobserve(e.target); }
            });
        }, opts || { threshold: 0.15 });
        obs.observe(el);
    }
    function qAll(sel, ctx) { return Array.prototype.slice.call((ctx||document).querySelectorAll(sel)); }
    function q(sel, ctx) { return (ctx||document).querySelector(sel); }
    function rAF(fn) { requestAnimationFrame(fn); }
    function clamp(v,a,b) { return Math.max(a, Math.min(b, v)); }
    function lerp(a,b,t) { return a + (b-a)*t; }

    /* ─── A. HERO LOAD SEQUENCE ───────────────────────────────────────────── */
    (function heroLoad() {
        var els = [
            { sel: '.hero-credential',   delay: 80 },
            { sel: '.hero-name .line1',  delay: 180 },
            { sel: '.hero-name .line2',  delay: 300 },
            { sel: '.hero-eyebrow',      delay: 440 },
            { sel: '.btn-accent',        delay: 580 },
            { sel: '.hero-stats',        delay: 720 },
            { sel: '.hero-scroll-hint',  delay: 1100 },
            { sel: '.live-badge',        delay: 900 },
        ];
        els.forEach(function(item) {
            var el = q(item.sel);
            if (!el) return;
            el.classList.add('sx-hero-hidden');
            setTimeout(function() { el.classList.add('sx-hero-in'); }, item.delay);
        });
        /* Hero photo */
        var photo = q('.hero-photo-wrap');
        if (photo) {
            photo.classList.add('sx-photo-hidden');
            setTimeout(function() { photo.classList.add('sx-photo-in'); }, 200);
        }
    })();

    /* ─── B. EYEBROW LINE WIPE ────────────────────────────────────────────── */
    qAll('[data-eyebrow-anim]').forEach(function(el) {
        once(el, function(t) { t.classList.add('sx-eyebrow-go'); });
    });

    /* ─── C. HEADING BLUR-IN ──────────────────────────────────────────────── */
    qAll('[data-heading-anim]').forEach(function(el) {
        once(el, function(t) { t.classList.add('sx-heading-go'); });
    });

    /* ─── D. LINE DRAW ────────────────────────────────────────────────────── */
    qAll('[data-line-draw]').forEach(function(el) {
        once(el, function(t) { t.classList.add('sx-line-go'); });
    });

    /* ─── E. STAT COUNT-UP (reusable, targets [data-countup]) ────────────── */
    function runCount(el) {
        var target  = parseFloat(el.getAttribute('data-countup'));
        var suffix  = el.getAttribute('data-suffix') || '';
        var dec     = String(target).includes('.') ? 1 : 0;
        var dur     = 1600;
        var start   = null;
        function ease(t) { return 1 - Math.pow(1-t, 3); }
        function step(ts) {
            if (!start) start = ts;
            var p = Math.min((ts-start)/dur, 1);
            el.textContent = (ease(p)*target).toFixed(dec) + suffix;
            if (p < 1) rAF(step);
        }
        rAF(step);
    }
    qAll('[data-countup]').forEach(function(el) {
        once(el, runCount, { threshold: 0.5 });
    });

    /* ─── F. FEATURE ROW POP ──────────────────────────────────────────────── */
    (function() {
        var rows = qAll('.feature-row');
        if (!rows.length) return;
        rows.forEach(function(row, i) {
            row.classList.add('sx-feature');
            once(row, function(el) {
                setTimeout(function() { el.classList.add('sx-feature-go'); }, i * 110);
            });
        });
    })();

    /* ─── G. RESOURCE CARD PERSPECTIVE CASCADE ────────────────────────────── */
    (function() {
        var cards = qAll('.resources-grid .resource-card');
        cards.forEach(function(card, i) {
            card.classList.add('sx-card-flip');
            once(card, function(el) {
                var col = i % 4; /* 4-col grid */
                setTimeout(function() { el.classList.add('sx-card-flip-go'); }, col * 80 + Math.floor(i/4)*60);
            });
        });
    })();

    /* ─── H. HERO FLOATING PARTICLES ─────────────────────────────────────── */
    (function() {
        var hero = q('.hero-section, header');
        if (!hero) return;
        var canvas = document.createElement('canvas');
        canvas.className = 'sx-particles';
        canvas.setAttribute('aria-hidden','true');
        hero.insertBefore(canvas, hero.firstChild);
        var ctx = canvas.getContext('2d');
        var W, H, pts = [];
        function resize() {
            W = canvas.width  = hero.offsetWidth;
            H = canvas.height = hero.offsetHeight;
        }
        resize();
        window.addEventListener('resize', resize, {passive:true});

        var COUNT = window.innerWidth < 600 ? 28 : 55;
        var accent = [232,84,26];
        for (var i=0; i<COUNT; i++) {
            pts.push({
                x: Math.random()*W, y: Math.random()*H,
                r: Math.random()*1.8 + 0.4,
                vx: (Math.random()-0.5)*0.22,
                vy: (Math.random()-0.5)*0.22,
                a: Math.random()*0.4 + 0.08,
                col: Math.random() < 0.3 ? accent : [200,210,225]
            });
        }
        function draw() {
            ctx.clearRect(0,0,W,H);
            pts.forEach(function(p) {
                p.x += p.vx; p.y += p.vy;
                if (p.x < 0) p.x = W; if (p.x > W) p.x = 0;
                if (p.y < 0) p.y = H; if (p.y > H) p.y = 0;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, 6.283);
                ctx.fillStyle = 'rgba('+p.col[0]+','+p.col[1]+','+p.col[2]+','+p.a+')';
                ctx.fill();
            });
            rAF(draw);
        }
        draw();
    })();

    /* ─── I. SECTION BG PARALLAX ──────────────────────────────────────────── */
    (function() {
        var els = qAll('[data-parallax-bg]');
        if (!els.length) return;
        function update() {
            var sy = window.scrollY;
            els.forEach(function(el) {
                var rect = el.getBoundingClientRect();
                var factor = parseFloat(el.getAttribute('data-parallax-bg')) || 0.15;
                var off = (rect.top + sy) * factor - sy * factor;
                el.style.backgroundPositionY = (50 + off * 0.04) + '%';
            });
        }
        window.addEventListener('scroll', update, {passive:true});
        update();
    })();

    /* ─── J. TILT ON HOVER (3D card follow) ──────────────────────────────── */
    (function() {
        var cards = qAll('[data-tilt]');
        var isMob = window.matchMedia('(hover:none)').matches;
        if (isMob) return;
        cards.forEach(function(card) {
            card.addEventListener('mousemove', function(e) {
                var r = card.getBoundingClientRect();
                var x = (e.clientX - r.left) / r.width  - 0.5;
                var y = (e.clientY - r.top)  / r.height - 0.5;
                card.style.transform = 'perspective(700px) rotateY('+x*10+'deg) rotateX('+(-y*8)+'deg) scale(1.02)';
            });
            card.addEventListener('mouseleave', function() {
                card.style.transform = '';
            });
        });
    })();

    /* ─── K. GENERAL [data-sx] SCROLL TRIGGERS ───────────────────────────── */
    (function() {
        var els = qAll('[data-sx]');
        els.forEach(function(el) {
            var type  = el.getAttribute('data-sx') || 'up';
            var delay = parseInt(el.getAttribute('data-sx-delay') || '0', 10);
            el.classList.add('sx-' + type);
            once(el, function(t) {
                setTimeout(function() { t.classList.add('sx-' + type + '-go'); }, delay);
            });
        });
    })();

    /* ─── L. MAGNETIC BUTTON ──────────────────────────────────────────────── */
    (function() {
        var btns = qAll('.btn-accent');
        if (window.matchMedia('(hover:none)').matches) return;
        btns.forEach(function(btn) {
            btn.addEventListener('mousemove', function(e) {
                var r = btn.getBoundingClientRect();
                var x = (e.clientX - r.left - r.width/2)  * 0.25;
                var y = (e.clientY - r.top  - r.height/2) * 0.25;
                btn.style.transform = 'translate('+x+'px,'+y+'px) scale(1.04)';
            });
            btn.addEventListener('mouseleave', function() {
                btn.style.transform = '';
            });
        });
    })();

    /* ─── M. SECTION HEADINGS — split-char on [data-char-split] ──────────── */
    (function() {
        qAll('[data-char-split]').forEach(function(el) {
            var text = el.textContent;
            el.textContent = '';
            text.split('').forEach(function(ch, i) {
                var span = document.createElement('span');
                span.className = 'sx-char';
                span.textContent = ch === ' ' ? ' ' : ch;
                span.style.transitionDelay = (i * 28) + 'ms';
                el.appendChild(span);
            });
            once(el, function(t) { t.classList.add('sx-char-go'); });
        });
    })();

    /* ─── N. GOAL SHIELD STROKE DRAW ─────────────────────────────────────── */
    (function() {
        var shield = q('.goal-shield-outer');
        if (!shield) return;
        var len = shield.getTotalLength ? shield.getTotalLength() : 300;
        shield.style.strokeDasharray  = len;
        shield.style.strokeDashoffset = len;
        shield.style.transition = 'stroke-dashoffset 1.4s cubic-bezier(.4,0,.2,1) 0.2s';
        var check = q('.goal-check');
        if (check) {
            var clen = check.getTotalLength ? check.getTotalLength() : 60;
            check.style.strokeDasharray  = clen;
            check.style.strokeDashoffset = clen;
            check.style.transition = 'stroke-dashoffset 0.7s cubic-bezier(.4,0,.2,1) 1.4s';
        }
        var wrap = q('.goal-section, #goalSection');
        if (wrap) {
            once(wrap, function() {
                shield.style.strokeDashoffset = '0';
                if (check) check.style.strokeDashoffset = '0';
                /* also trigger goal stat count-up */
                qAll('.goal-stat-num[data-goal-count]').forEach(function(el) {
                    var target = parseInt(el.getAttribute('data-goal-count'), 10);
                    var suffix = el.getAttribute('data-goal-suffix') || '';
                    var dur = 1800, start = null;
                    function ease(t){ return 1-Math.pow(1-t,3); }
                    function step(ts) {
                        if (!start) start = ts;
                        var p = Math.min((ts-start)/dur,1);
                        el.textContent = Math.round(ease(p)*target)+suffix;
                        if (p<1) rAF(step);
                    }
                    setTimeout(function(){ rAF(step); }, 400);
                });
            }, { threshold: 0.3 });
        }
    })();

    /* ─── O. STAGGER EYEBROWS inside sections ─────────────────────────────── */
    (function() {
        qAll('.eyebrow').forEach(function(el) {
            el.classList.add('sx-eyebrow');
            once(el, function(t) { t.classList.add('sx-eyebrow-go'); });
        });
    })();

    /* ─── P. SERVICES HEADER legal text reveal ────────────────────────────── */
    (function() {
        var el = q('.services-legal');
        if (!el) return;
        el.classList.add('sx-up');
        once(el, function(t) {
            setTimeout(function() { t.classList.add('sx-up-go'); }, 200);
        });
    })();

    /* ─── Q. CONTACT GRID slide in ────────────────────────────────────────── */
    (function() {
        var info = q('.contact-info');
        var form = q('.contact-form-wrap');
        if (info) { info.classList.add('sx-left'); once(info, function(t){ t.classList.add('sx-left-go'); }); }
        if (form) { form.classList.add('sx-right'); once(form, function(t){ setTimeout(function(){ t.classList.add('sx-right-go'); },120); }); }
    })();

    /* ─── R. FOOTER links stagger ─────────────────────────────────────────── */
    (function() {
        qAll('.footer-links a').forEach(function(a, i) {
            a.classList.add('sx-up');
            once(a, function(t) { setTimeout(function(){ t.classList.add('sx-up-go'); }, i*60); });
        });
    })();

    /* ─── S. SECTION NUMBER BADGES (service cards) ────────────────────────── */
    (function() {
        qAll('.service-num').forEach(function(el, i) {
            el.classList.add('sx-num');
            once(el, function(t) { setTimeout(function(){ t.classList.add('sx-num-go'); }, i*90); }, {threshold:0.1});
        });
    })();

    /* ─── T. SCROLL-DRIVEN SKEW on sections ──────────────────────────────── */
    (function() {
        if (window.matchMedia('(prefers-reduced-motion:reduce)').matches) return;
        if (window.matchMedia('(max-width:600px)').matches) return;
        var sections = qAll('section:not(.contact-section)');
        var lastY = window.scrollY, skewAmount = 0;
        function updateSkew() {
            var dy = window.scrollY - lastY;
            lastY = window.scrollY;
            skewAmount = clamp(skewAmount + dy * 0.004, -1.8, 1.8);
            skewAmount *= 0.9;
            sections.forEach(function(s) {
                s.style.transform = 'skewY(' + skewAmount.toFixed(3) + 'deg)';
            });
        }
        window.addEventListener('scroll', updateSkew, {passive:true});
    })();

    /* ─── U. IN-VIEW CLASS for CSS animations ─────────────────────────────── */
    (function() {
        var els = qAll('[data-inview]');
        observe(els, function(el, isIn, obs) {
            if (isIn) {
                el.classList.add('in-view');
                if (obs) obs.unobserve(el);
            }
        });
    })();

    /* ─── V. RESOURCE ICON SPIN on hover ─────────────────────────────────── */
    (function() {
        qAll('.resource-icon').forEach(function(el) {
            el.parentElement.addEventListener('mouseenter', function() {
                el.classList.add('sx-icon-spin');
            });
            el.parentElement.addEventListener('animationend', function() {
                el.classList.remove('sx-icon-spin');
            }, {once: true});
        });
    })();

    /* ─── W. SCROLL PROGRESS ACCENT LINE (top of page) ───────────────────── */
    (function() {
        var bar = document.createElement('div');
        bar.className = 'sx-scroll-bar';
        bar.setAttribute('aria-hidden','true');
        document.body.appendChild(bar);
        function update() {
            var total = document.documentElement.scrollHeight - window.innerHeight;
            bar.style.width = (total > 0 ? (window.scrollY/total*100) : 0) + '%';
        }
        window.addEventListener('scroll', update, {passive:true});
    })();

    /* ─── X. MARQUEE speed burst when scrolling fast ─────────────────────── */
    (function() {
        var track = q('.marquee-track');
        if (!track) return;
        var baseSpeed = 1, currentSpeed = 1, lastY = window.scrollY;
        function update() {
            var dy = Math.abs(window.scrollY - lastY);
            lastY = window.scrollY;
            currentSpeed = clamp(1 + dy * 0.08, 1, 4);
        }
        function anim() {
            currentSpeed = lerp(currentSpeed, baseSpeed, 0.04);
            track.style.animationPlayState = 'running';
            track.style.animationDuration  = (28 / currentSpeed) + 's';
            rAF(anim);
        }
        window.addEventListener('scroll', update, {passive:true});
        anim();
    })();

})();
