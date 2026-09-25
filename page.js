/* page.js — μενού κινητού και «συμπαγές» μενού στην κύλιση, για τις εσωτερικές σελίδες */
(function () {
    'use strict';
    var nav = document.getElementById('nav');
    var links = document.getElementById('navLinks');
    var hbg = document.getElementById('hamburger');
    function close() { if (links) links.classList.remove('open'); if (hbg) { hbg.classList.remove('open'); hbg.setAttribute('aria-expanded', 'false'); } }
    if (hbg && links) {
        hbg.addEventListener('click', function () {
            var open = links.classList.toggle('open');
            hbg.classList.toggle('open', open);
            hbg.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        hbg.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); hbg.click(); } });
        links.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });
    }
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    function onScroll() {
        if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
        if (links) links.classList.toggle('nav-scrolled', window.scrollY > 60);
        var hero = document.querySelector('.page-hero'), logoText = document.querySelector('.logo-text');
        if (hero && logoText) logoText.classList.toggle('logo-text--visible', window.scrollY >= hero.offsetHeight * 0.85);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
})();

/* Δίκτυο κόμβων στην επάνω ζώνη — ίδιο με το hero της αρχικής, πυκνότητα ανάλογη με το εμβαδόν */
(function () {
    'use strict';
    var canvas = document.getElementById('heroNet');
    if (!canvas || !canvas.getContext) return;
    var ctx = canvas.getContext('2d');
    var MAX_DIST = 190, NODE_R = 3.5, SPEED = 0.38, COLOR = '210,230,220', EDGE_ALPHA = 0.36, NODE_ALPHA = 0.55, REPEL_R = 120, REPEL_F = 1.8;
    var W, H, nodes = [], mouse = { x: -9999, y: -9999 }, visible = true, host = canvas.parentElement;
    function resize() { W = canvas.width = host.offsetWidth; H = canvas.height = host.offsetHeight; }
    function mk() { var a = Math.random() * Math.PI * 2, v = SPEED * (0.5 + Math.random()); return { x: Math.random() * W, y: Math.random() * H, vx: Math.cos(a) * v, vy: Math.sin(a) * v }; }
    function init() { resize(); var n = Math.max(30, Math.round(110 * (W * H) / (1440 * 900))); nodes = []; for (var i = 0; i < n; i++) nodes.push(mk()); }
    function tick() {
        if (visible) {
            ctx.clearRect(0, 0, W, H);
            var i, j, n;
            for (i = 0; i < nodes.length; i++) {
                n = nodes[i];
                var mdx = n.x - mouse.x, mdy = n.y - mouse.y, md = Math.sqrt(mdx * mdx + mdy * mdy);
                if (md < REPEL_R && md > 0) { var f = (1 - md / REPEL_R) * REPEL_F; n.vx += (mdx / md) * f * 0.05; n.vy += (mdy / md) * f * 0.05; }
                n.vx *= 0.985; n.vy *= 0.985;
                if (Math.sqrt(n.vx * n.vx + n.vy * n.vy) < SPEED * 0.3) { n.vx += (Math.random() - 0.5) * 0.12; n.vy += (Math.random() - 0.5) * 0.12; }
                n.x += n.vx; n.y += n.vy;
                if (n.x < -20) n.x = W + 20; else if (n.x > W + 20) n.x = -20;
                if (n.y < -20) n.y = H + 20; else if (n.y > H + 20) n.y = -20;
            }
            for (i = 0; i < nodes.length; i++) for (j = i + 1; j < nodes.length; j++) {
                var a = nodes[i], b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = Math.sqrt(dx * dx + dy * dy);
                if (d < MAX_DIST) { ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.strokeStyle = 'rgba(' + COLOR + ',' + ((1 - d / MAX_DIST) * EDGE_ALPHA) + ')'; ctx.lineWidth = 1.4; ctx.stroke(); }
            }
            for (i = 0; i < nodes.length; i++) { ctx.beginPath(); ctx.arc(nodes[i].x, nodes[i].y, NODE_R, 0, Math.PI * 2); ctx.fillStyle = 'rgba(' + COLOR + ',' + NODE_ALPHA + ')'; ctx.fill(); }
        }
        requestAnimationFrame(tick);
    }
    host.addEventListener('mousemove', function (e) { var r = canvas.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; }, { passive: true });
    host.addEventListener('mouseleave', function () { mouse.x = -9999; mouse.y = -9999; });
    window.addEventListener('resize', resize);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(host);
    init(); tick();
})();

