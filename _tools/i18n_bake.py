# -*- coding: utf-8 -*-
"""
i18n_bake.py — «ψήνει» τις μεταφράσεις του i18n.js μέσα στο στατικό HTML.

    python3 _tools/i18n_bake.py            # index.html (ελληνικά) + en/index.html (αγγλικά)

Γιατί: τα ρομπότ των ChatGPT/Claude/Perplexity δεν εκτελούν JavaScript, και η Google
ευρετηριάζει μία γλώσσα ανά διεύθυνση. Άρα:
  - το index.html πρέπει να έχει ΗΔΗ μέσα του το ελληνικό κείμενο του λεξικού,
  - τα αγγλικά χρειάζονται δική τους διεύθυνση (/en/) με στατικό αγγλικό κείμενο.

Πηγή αλήθειας για τα κείμενα της αρχικής = το λεξικό του i18n.js.
Αλλάζεις κείμενο στο i18n.js → ξανατρέχεις αυτό. Το en/index.html είναι ΠΑΡΑΓΩΓΟ: μη το διορθώνεις με το χέρι.
Το _tools/ δεν δημοσιεύεται (το GitHub Pages/Jekyll αγνοεί φακέλους που αρχίζουν με _).
"""
import html, json, re, subprocess, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import entity as E  # noqa: E402
import navmenu as N  # noqa: E402

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def load_dict():
    js = r"""
    global.document={readyState:'complete',querySelectorAll:()=>[],documentElement:{lang:'el'},addEventListener(){}};
    global.window=global; global.localStorage={setItem(){},getItem(){return null}};
    require(process.argv[1]); process.stdout.write(JSON.stringify(window.I18n.translations));
    """
    out = subprocess.run(["node", "-e", js, str(ROOT / "i18n.js")], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


class Locator(HTMLParser):
    """Βρίσκει θέσεις (offsets) για στοιχεία με data-i18n / data-i18n-html."""

    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.lines = [0]
        for m in re.finditer("\n", text):
            self.lines.append(m.end())
        self.open = []    # [tag, depth, inner_start, key, mode]
        self.found = []   # (inner_start, inner_end, key, mode)

    def off(self):
        ln, col = self.getpos()
        return self.lines[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        start = self.off()
        end = start + len(self.get_starttag_text())
        for o in self.open:
            if o[0] == tag and tag not in VOID:
                o[1] += 1
        a = dict(attrs)
        mode = "html" if "data-i18n-html" in a else ("text" if "data-i18n" in a else None)
        if mode and tag not in VOID:
            self.open.append([tag, 1, end, a.get("data-i18n-html") or a.get("data-i18n"), mode])

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pos = self.off()
        for o in list(self.open):
            if o[0] == tag:
                o[1] -= 1
                if o[1] == 0:
                    self.found.append((o[2], pos, o[3], o[4]))
                    self.open.remove(o)


def bake(text, t, lang):
    loc = Locator(text)
    loc.feed(text)
    missing = set()
    for start, end, key, mode in sorted(loc.found, key=lambda x: -x[0]):
        if key not in t or lang not in t[key]:
            missing.add(key)
            continue
        val = t[key][lang]
        if val == "" and lang == "el":
            continue
        new = val if mode == "html" else html.escape(val, quote=False)
        # κρατά ίδια εσοχή/αλλαγές γραμμής γύρω από κείμενο που ήταν σε δική του γραμμή
        old = text[start:end]
        lead = re.match(r"\s*", old).group(0)
        trail = re.search(r"\s*$", old).group(0)
        if "\n" not in lead:
            lead, trail = "", ""
        text = text[:start] + lead + new + trail + text[end:]

    def attr(m, name):
        key = m.group(2)
        if key in t and lang in t[key]:
            return m.group(0)  # ο κανόνας εφαρμόζεται στο επόμενο βήμα
        missing.add(key)
        return m.group(0)

    # attributes: alt / title / placeholder, με το κλειδί στο data-i18n-*
    for a in ("alt", "title", "placeholder"):
        def rep(m, a=a):
            tag = m.group(0)
            key = re.search(r'data-i18n-%s="([^"]+)"' % a, tag).group(1)
            if key not in t or lang not in t[key]:
                missing.add(key)
                return tag
            val = html.escape(t[key][lang], quote=True)
            if re.search(r'\s%s="[^"]*"' % a, tag):
                return re.sub(r'(\s)%s="[^"]*"' % a, r'\1%s="%s"' % (a, val), tag, count=1)
            return tag.replace(" data-i18n-%s=" % a, ' %s="%s" data-i18n-%s=' % (a, val, a), 1)
        text = re.sub(r"<[a-zA-Z][^<>]*data-i18n-%s=\"[^\"]+\"[^<>]*>" % a, rep, text)
    return text, missing


# ── αγγλική έκδοση ──────────────────────────────────────────────────────────
EN_LINKS = {
    "texnikos-asfaleias/": "safety-technician-greece/",
    "geek-grapti-ektimisi-kindynou/": "risk-assessment-greece/",
    "ekpaideuseis-ygeias-asfaleias/": "health-safety-training/",
    "diereynisi-ergatikou-atyximatos/": "accident-investigation/",
    "schedia-diafygis-ekkenosis/": "evacuation-plans/",
    "elegxos-epitheorisis-ergasias/": "labour-inspection-readiness/",
    "kataskeves-ergotaxia/": "construction-sites/",
    "viomixania-logistics/": "industry-logistics/",
    "mikres-epixeiriseis/": "small-businesses/",
    "omada/": "team/",
    "odigoi/": "guides/",
    "odigoi/ores-texnikou-asfaleias/": "guides/safety-technician-hours/",
    "odigoi/ergodotis-texnikos-asfaleias/": "guides/employer-as-safety-technician/",
    "odigoi/ergatiko-atyxima-ti-kanei-o-ergodotis/": "guides/workplace-accident-employer-steps/",
    "aporrito/": "privacy/",
    "en/foreign-companies-greece/": "foreign-companies-greece/",
}


def refresh_dd(text, t, lang):
    """Βάζει/ανανεώνει τα υπομενού «Υπηρεσίες» και «Τομείς» της μπάρας (δείκτες <!--dd:…-->)."""
    for key in ("services", "sectors"):
        block = N.home_block(key, lang, t["nav." + key][lang])
        pat = re.compile(r"<!--dd:%s-->.*?<!--/dd:%s-->" % (key, key), re.S)
        if pat.search(text):
            text = pat.sub(lambda m: block, text, count=1)
        else:
            old = re.compile(r'<a href="#%s" data-i18n="nav\.%s">[^<]*</a>' % (key, key))
            text, n = old.subn(lambda m: block, text, count=1)
            if not n:
                raise SystemExit("δεν βρέθηκε ο σύνδεσμος #%s στη μπάρα" % key)
    return text


def to_en(text, t):
    D = E.DOMAIN
    text = refresh_dd(text, t, "en")
    text = text.replace('id="hamburger" role="button" tabindex="0" aria-label="Μενού"', 'id="hamburger" role="button" tabindex="0" aria-label="Menu"')
    title = "Malliaris & Partners | Occupational Health & Safety, Athens"
    desc = ("Safety technician, written risk assessment, staff training, evacuation plans and labour "
            "inspection readiness for companies in Athens and Attica, Greece.")
    text = text.replace('<html lang="el">', '<html lang="en">', 1)
    text = re.sub(r"<title>.*?</title>", "<title>%s</title>" % html.escape(title, quote=False), text, count=1)
    text = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, text, count=1)
    text = text.replace('<link rel="canonical" href="%s/">' % D, '<link rel="canonical" href="%s/en/">' % D)
    text = text.replace('<meta property="og:url" content="%s/">' % D, '<meta property="og:url" content="%s/en/">' % D)
    text = text.replace('<meta property="og:site_name" content="Μάλλιαρης &amp; Συνεργάτες">', '<meta property="og:site_name" content="Malliaris &amp; Partners">')
    text = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % html.escape(title), text)
    text = re.sub(r'<meta name="twitter:title" content="[^"]*">', '<meta name="twitter:title" content="%s">' % html.escape(title), text)
    text = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % desc, text)
    text = re.sub(r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="%s">' % desc, text)
    text = re.sub(r'<meta property="og:image:alt" content="[^"]*">', '<meta property="og:image:alt" content="Malliaris &amp; Partners — health and safety training on a construction site">', text)
    text = text.replace('<meta property="og:locale" content="el_GR">', '<meta property="og:locale" content="en_GB">')
    text = text.replace('<meta property="og:locale:alternate" content="en_GB">', '<meta property="og:locale:alternate" content="el_GR">')

    faq = [(t["faq.q%d" % i]["en"], t["faq.a%d" % i]["en"]) for i in range(1, 6)]
    nodes = [E.org("en"), *E.PEOPLE, E.website(),
             {"@type": "WebPage", "@id": D + "/en/#webpage", "url": D + "/en/", "name": title, "description": desc,
              "isPartOf": {"@id": E.SITE_ID}, "about": {"@id": E.ORG_ID}, "inLanguage": "en", "dateModified": "2026-09-25"},
             {"@type": "FAQPage", "@id": D + "/en/#faq", "inLanguage": "en",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    text = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: E.graph(nodes), text, count=1, flags=re.S)

    # γλωσσικοί σύνδεσμοι
    text = text.replace('class="lang-btn active" data-lang="el" href="./"', 'class="lang-btn" data-lang="el" href="../"')
    text = text.replace('class="lang-btn" data-lang="en" href="en/"', 'class="lang-btn active" data-lang="en" href="./"')

    # εσωτερικοί σύνδεσμοι προς σελίδες με αγγλική εκδοχή
    def link(m):
        attr, url = m.group(1), m.group(2)
        if url in EN_LINKS:
            return '%s="%s"' % (attr, EN_LINKS[url])
        return m.group(0)
    text = re.sub(r'(href)="([a-z0-9\-/]+/)"', link, text)

    # σχετικές διαδρομές → ../ (εκτός από τις αγγλικές σελίδες που μόλις αντιστοιχίσαμε)
    en_targets = set(EN_LINKS.values()) | {"./"}
    def rel(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|tel:|#|/|data:|\.\./|javascript:)", url) or url in en_targets:
            return m.group(0)
        return '%s="../%s"' % (attr, url)
    text = re.sub(r'\b(src|href)="([^"]*)"', rel, text)
    text = re.sub(r"url\('(?!https?:|data:|\.\./)([^']+)'\)", r"url('../\1')", text)
    return text


def main():
    t = load_dict()
    src = refresh_dd((ROOT / "index.html").read_text(encoding="utf-8"), t, "el")
    el, miss_el = bake(src, t, "el")
    (ROOT / "index.html").write_text(el, encoding="utf-8")
    en, miss_en = bake(el, t, "en")
    en = to_en(en, t)
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(en, encoding="utf-8")
    miss = sorted(miss_el | miss_en)
    print("ok: index.html + en/index.html", ("· χωρίς κλειδί: " + ", ".join(miss)) if miss else "")


if __name__ == "__main__":
    main()
