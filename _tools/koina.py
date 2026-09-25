#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
koina.py — ΙΔΙΟ μενού ναυσιπλοΐας και ΙΔΙΟ υποσέλιδο σε ΟΛΕΣ τις σελίδες

    python3 koina.py <φάκελος-site> [--check]

Πηγή αλήθειας: η αρχική (index.html για την κύρια γλώσσα, en/index.html για
την άλλη). Από εκεί παίρνει το <nav id="nav"> (ή το <header> που το περιέχει)
και το <footer>, και τα γράφει σε κάθε υποσελίδα (φάκελος/index.html,
en/φάκελος/index.html, …) με:
  - διαδρομές ξαναϋπολογισμένες για το βάθος της υποσελίδας
    (#about → ../#about, styles.css → ../styles.css, …)
  - διακόπτη γλώσσας που δείχνει στο ΑΝΤΙΣΤΟΙΧΟ της υποσελίδας (hreflang),
    όχι στην αρχική
  - aria-current="page" στον σύνδεσμο της τρέχουσας σελίδας

Τρέχει ΑΥΤΟΜΑΤΑ στο τέλος του prerender.py. Μόνο του: μετά από χειροκίνητη
αλλαγή σε υποσελίδα, ή σε ιστότοπο χωρίς index.src.html (παλιάς γενιάς).

--check : δεν γράφει· κωδικός 1 αν κάποια σελίδα έχει άλλο μενού/υποσέλιδο.

Κανόνας: references/04-stoixeia.md §15α. Έλεγχος: elegxos.py (N5).
"""
import argparse, posixpath, re, sys
from pathlib import Path
from urllib.parse import urljoin, urlsplit

SKIP_DIRS = {".git", "node_modules", "_to_delete", ".claude", "kinito-anafora", "glossa-anafora", "assets"}
URL_ATTRS = ("href", "src", "poster")


# ── εύρεση μπλοκ ────────────────────────────────────────────────────────────
def _block(html, tag, start):
    """(αρχή, τέλος) του στοιχείου <tag> που ξεκινά στο start, με ένθεση."""
    pat = re.compile(r"<(/?)%s\b[^>]*>" % tag, re.I)
    depth = 0
    for m in pat.finditer(html, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return start, m.end()
    return None


def _mask(html):
    """Σχόλια → κενά ίδιου μήκους: οι θέσεις μένουν ίδιες, αλλά ένα «<nav id="nav">»
    μέσα σε σχόλιο (π.χ. οδηγία στον σκελετό) δεν μπερδεύει την αναζήτηση."""
    return re.sub(r"(?s)<!--.*?-->", lambda m: " " * len(m.group(0)), html)


def find_nav(html):
    html = _mask(html)
    m = re.search(r'<nav\b[^>]*\bid="nav"', html, re.I)
    if m:
        return _block(html, "nav", m.start())
    for h in re.finditer(r"<header\b", html, re.I):
        b = _block(html, "header", h.start())
        if b and re.search(r"<nav\b", html[b[0]:b[1]], re.I):
            return b
    m = re.search(r"<nav\b", html, re.I)
    return _block(html, "nav", m.start()) if m else None


def find_footer(html):
    html = _mask(html)
    ms = list(re.finditer(r"<footer\b", html, re.I))
    return _block(html, "footer", ms[-1].start()) if ms else None


# ── σελίδες ─────────────────────────────────────────────────────────────────
def primary_lang(site):
    cfg = site / "config.js"
    if cfg.exists():
        m = re.search(r"meta\s*:\s*\{[^}]*?\blang\s*:\s*'(el|en)'", cfg.read_text(encoding="utf-8", errors="replace"), re.S)
        if m:
            return m.group(1)
    h = site / "index.html"
    if h.exists():
        m = re.search(r'<html[^>]*\blang="(el|en)', h.read_text(encoding="utf-8", errors="replace"))
        if m:
            return m.group(1)
    return "el"


def pages(site):
    """{'home': {lang: Path}, 'subs': [(Path, lang)]} — υποσελίδες = κάθε άλλο index.html."""
    prim = primary_lang(site)
    other = "en" if prim == "el" else "el"
    homes = {prim: site / "index.html"}
    if (site / other / "index.html").exists():
        homes[other] = site / other / "index.html"
    subs = []
    for p in sorted(site.rglob("index.html")):
        rel = p.relative_to(site).parts
        if p in homes.values() or len(rel) > 5:
            continue
        if any(x in SKIP_DIRS or x.startswith((".", "_")) for x in rel[:-1]):
            continue
        subs.append((p, other if rel[0] == other and other in homes else prim))
    return {"primary": prim, "other": other, "home": homes, "subs": subs}


def url_path(site, p):
    """Διαδρομή URL της σελίδας: index.html → '/', en/x/index.html → '/en/x/'."""
    rel = p.parent.relative_to(site).as_posix()
    return "/" if rel == "." else "/" + rel + "/"


# ── διαδρομές ───────────────────────────────────────────────────────────────
ABS = re.compile(r"^(?:[a-z][a-z0-9+.\-]*:|//|data:)", re.I)


def rel_from(target, here_dir):
    """Σχετική διαδρομή από τον φάκελο here_dir ('/en/x/') προς το target ('/en/#about')."""
    sp = urlsplit(target)
    path = sp.path or "/"
    tail = ("?" + sp.query if sp.query else "") + ("#" + sp.fragment if sp.fragment else "")
    if path.endswith("/"):
        r = posixpath.relpath(path, here_dir)
        r = "./" if r == "." else r + "/"
    else:
        r = posixpath.relpath(path, here_dir)
    return r + tail


def rebase(block, src_dir, dst_dir):
    """Ξαναγράφει κάθε σχετική διαδρομή του μπλοκ από src_dir σε dst_dir."""
    def fix(u):
        # εξωτερική, data:, tel:, mailto:, ή απόλυτη στον τομέα ('/…') → μένει ως έχει
        if not u or ABS.match(u) or u.startswith("/"):
            return u
        return rel_from(urljoin("http://h" + src_dir, u)[len("http://h"):], dst_dir)

    def attr(m):
        return '%s="%s"' % (m.group(1), fix(m.group(2)))
    block = re.sub(r'\b(%s)="([^"]*)"' % "|".join(URL_ATTRS), attr, block)
    block = re.sub(r'\bsrcset="([^"]*)"', lambda m: 'srcset="%s"' % ", ".join(
        (lambda parts: " ".join([fix(parts[0])] + parts[1:]))(c.strip().split()) for c in m.group(1).split(",") if c.strip()), block)
    block = re.sub(r"url\((['\"]?)([^'\")]+)\1\)", lambda m: "url(%s%s%s)" % (m.group(1), fix(m.group(2)), m.group(1)), block)
    # τα data-href-el/-en χρειάζονται μόνο στη σελίδα ανάπτυξης (αλλαγή γλώσσας επί τόπου)
    block = re.sub(r'\s+data-href-(?:el|en)="[^"]*"', "", block)
    return block


def alt_paths(html):
    """hreflang → διαδρομή URL, από τα <link rel=alternate> της σελίδας."""
    out = {}
    for tag in re.findall(r"<link\b[^>]*>", html, re.I):
        if 'rel="alternate"' not in tag:
            continue
        hl = re.search(r'hreflang="([^"]+)"', tag)
        hr = re.search(r'href="([^"]+)"', tag)
        if hl and hr:
            out[hl.group(1)[:2]] = urlsplit(hr.group(1)).path or "/"
    return out


def lang_links(block, sub_html, sub_path, lang, info, site):
    """Ο διακόπτης γλώσσας της υποσελίδας δείχνει στο αντίστοιχό της."""
    alts = alt_paths(sub_html)

    def target(l):
        if l == lang:
            return "./"
        p = alts.get(l)
        if not p:                                    # χωρίς hreflang: μάντεψε από τη δομή φακέλων
            slug = sub_path.strip("/").split("/")
            if lang == info["other"]:
                slug = slug[1:]
            else:
                slug = [info["other"]] + slug
            cand = "/" + "/".join(slug) + "/"
            p = cand if (site / cand.strip("/") / "index.html").exists() else ("/" if l == info["primary"] else "/%s/" % l)
        return rel_from(p, sub_path)

    def fix(m):
        tag = m.group(0)
        if "lang-btn" not in tag:
            return tag
        dl = re.search(r'data-lang="([^"]+)"', tag)
        if not dl or not re.search(r'\bhref="', tag):
            return tag
        return re.sub(r'\bhref="[^"]*"', 'href="%s"' % target(dl.group(1)), tag, 1)
    return re.sub(r"<a\b[^>]*>", fix, block)


def mark_current(block, sub_path):
    block = re.sub(r'\s+aria-current="page"', "", block)

    def fix(m):
        tag = m.group(0)
        h = re.search(r'\bhref="([^"]*)"', tag)
        if not h or "lang-btn" in tag:
            return tag
        full = urljoin("http://h" + sub_path, h.group(1))[len("http://h"):]
        if urlsplit(full).path == sub_path and not urlsplit(full).fragment:
            return tag[:-1] + ' aria-current="page">'
        return tag
    return re.sub(r"<a\b[^>]*>", fix, block)


def build(site, sub, lang, info):
    """Επιστρέφει (νέο_html, [σημειώσεις]) για μία υποσελίδα."""
    home = info["home"].get(lang) or info["home"][info["primary"]]
    hh = home.read_text(encoding="utf-8")
    sh = sub.read_text(encoding="utf-8")
    src_dir, dst_dir = url_path(site, home), url_path(site, sub)
    notes = []
    for name, finder in (("nav", find_nav), ("footer", find_footer)):
        hb = finder(hh)
        if not hb:
            continue
        block = rebase(hh[hb[0]:hb[1]], src_dir, dst_dir)
        if name == "nav":
            block = lang_links(block, sh, dst_dir, lang, info, site)
        block = mark_current(block, dst_dir)
        sb = finder(sh)
        if sb:
            if sh[sb[0]:sb[1]] != block:
                sh = sh[:sb[0]] + block + sh[sb[1]:]
                notes.append(name)
        else:
            if name == "nav":
                m = re.search(r"<body\b[^>]*>", sh, re.I)
                skip = re.search(r'<a\b[^>]*class="skip-link"[^>]*>.*?</a>', sh[m.end():] if m else "", re.S)
                at = (m.end() + skip.end()) if (m and skip) else (m.end() if m else 0)
            else:
                mm = list(re.finditer(r"</main>", sh, re.I))
                at = mm[-1].end() if mm else sh.lower().rfind("</body>")
            sh = sh[:at] + "\n" + block + "\n" + sh[at:]
            notes.append(name + " (νέο)")
    return sh, notes


def sync(site, check=False, quiet=False):
    info = pages(site)
    if not info["home"][info["primary"]].exists():
        print("ΣΦΑΛΜΑ: δεν υπάρχει index.html στο %s" % site, file=sys.stderr)
        return 2
    changed = []
    for sub, lang in info["subs"]:
        new, notes = build(site, sub, lang, info)
        if notes:
            changed.append((sub, notes))
            if not check:
                sub.write_text(new, encoding="utf-8")
    if not quiet:
        for sub, notes in changed:
            print("  %-40s %s %s" % (sub.relative_to(site).as_posix(), "διαφέρει:" if check else "ενημερώθηκε:", ", ".join(notes)))
        n = len(info["subs"])
        if not changed:
            print("  κοινά μέρη: μενού + υποσέλιδο ίδια σε %d υποσελίδες" % n)
        elif not check:
            print("  κοινά μέρη: %d/%d υποσελίδες πήραν το μενού/υποσέλιδο της αρχικής" % (len(changed), n))
    return 1 if (check and changed) else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    site = Path(a.site).expanduser().resolve()
    return sync(site, a.check)


if __name__ == "__main__":
    sys.exit(main())
