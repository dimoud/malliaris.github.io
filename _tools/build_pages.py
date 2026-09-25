# -*- coding: utf-8 -*-
"""
build_pages.py — παράγει τις εσωτερικές σελίδες (υπηρεσίες, κλάδοι, ομάδα, οδηγοί, απόρρητο) σε ΕΛ/ΕΝ.

    python3 _tools/build_pages.py

Περιεχόμενο: _tools/pages_el.py και _tools/pages_en.py (κείμενα σε HTML).
Πρότυπο: αυτό το αρχείο (μενού, υποσέλιδο, ζώνη επικοινωνίας, JSON-LD, sitemap.xml).
Τα παραγόμενα */index.html είναι στατικά και διαβάζονται χωρίς JavaScript.
Μετά από αλλαγή κειμένου: ξανατρέχεις αυτό και το _tools/i18n_bake.py.
"""
import html, json, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import entity as E  # noqa: E402
import navmenu as N  # noqa: E402

TODAY = "2026-09-25"
D = E.DOMAIN
esc = lambda s: html.escape(s, quote=True)


def prefix_for(path):
    depth = path.strip("/").count("/") + 1 if path.strip("/") else 0
    return "../" * depth


def head(p, pre, alt):
    el = p["lang"] == "el"
    url = D + p["path"]
    links = [f'<link rel="canonical" href="{url}">']
    if alt:
        el_url = url if el else D + alt
        en_url = D + alt if el else url
        links += [f'<link rel="alternate" hreflang="el" href="{el_url}">',
                  f'<link rel="alternate" hreflang="en" href="{en_url}">',
                  f'<link rel="alternate" hreflang="x-default" href="{el_url}">']
    img = D + p.get("og_image", "/img/og-malliaris-synergates.jpg")
    site = "Μάλλιαρης &amp; Συνεργάτες" if el else "Malliaris &amp; Partners"
    return f'''<!DOCTYPE html>
<html lang="{p["lang"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{esc(p["title"])}</title>
    <meta name="description" content="{esc(p["desc"])}">
    {chr(10).join("    " + l if i else l for i, l in enumerate(links))}
    <meta name="theme-color" content="#0F1929">
    <meta name="format-detection" content="telephone=no">
    <link rel="icon" type="image/x-icon" href="{pre}favicon.ico">
    <link rel="icon" type="image/svg+xml" href="{pre}favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="{pre}apple-touch-icon.png">
    <meta property="og:type" content="{p.get("og_type", "website")}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="{site}">
    <meta property="og:title" content="{esc(p["title"])}">
    <meta property="og:description" content="{esc(p["desc"])}">
    <meta property="og:image" content="{img}">
    <meta property="og:locale" content="{"el_GR" if el else "en_GB"}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(p["title"])}">
    <meta name="twitter:description" content="{esc(p["desc"])}">
    <meta name="twitter:image" content="{img}">
    <script src="{pre}consent.js"></script>
    {E.graph(jsonld(p, alt))}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="{pre}styles.css">
    <link rel="stylesheet" href="{pre}page.css">
    <link rel="stylesheet" href="{pre}expertease-credit.css">
</head>'''


def jsonld(p, alt):
    el = p["lang"] == "el"
    url = D + p["path"]
    home = D + ("/" if el else "/en/")
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Αρχική" if el else "Home", "item": home}]
    for i, (name, path) in enumerate(p.get("crumbs", []), 2):
        crumbs.append({"@type": "ListItem", "position": i, "name": name, "item": D + path})
    crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": p["crumb"], "item": url})
    org = {"@type": "ProfessionalService", "@id": E.ORG_ID, "name": "Μάλλιαρης & Συνεργάτες" if el else "Malliaris & Partners",
           "url": home, "telephone": E.PHONE_E164, "address": E.ADDRESS if el else E.ADDRESS_EN}
    page = {"@type": p.get("page_type", "WebPage"), "@id": url + "#webpage", "url": url, "name": p["title"],
            "description": p["desc"], "inLanguage": p["lang"], "isPartOf": {"@id": E.SITE_ID},
            "about": {"@id": E.ORG_ID}, "dateModified": p.get("updated", TODAY),
            "breadcrumb": {"@id": url + "#breadcrumb"}}
    if p.get("author", True):
        page["author"] = {"@id": D + "/#stavros-malliaris"}
        page["reviewedBy"] = {"@id": D + "/#stavros-malliaris"}
    nodes = [org, page, {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": crumbs}]
    if p.get("service"):
        nodes.append({"@type": "Service", "@id": url + "#service", "name": p["service"], "serviceType": p["service"],
                      "url": url, "provider": {"@id": E.ORG_ID},
                      "areaServed": {"@type": "AdministrativeArea", "name": "Αττική" if el else "Attica, Greece"},
                      "availableLanguage": ["el", "en"], "description": p["desc"]})
    if p.get("people"):
        nodes += [x for x in E.PEOPLE]
    if p.get("faq"):
        nodes.append({"@type": "FAQPage", "@id": url + "#faq", "inLanguage": p["lang"],
                      "mainEntity": [{"@type": "Question", "name": q,
                                      "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in p["faq"]]})
    return nodes


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def nav(p, pre, alt):
    el = p["lang"] == "el"
    home = pre if el else pre + "en/"
    if el:
        drops = [N.dd("services", home + "#services", "Υπηρεσίες", N.SERVICES_EL, pre, "el", more=N.SERVICES_EL_MORE),
                 N.dd("sectors", home + "#sectors", "Τομείς", N.SECTORS_EL, pre, "el")]
        items = [("omada/", "Η ομάδα", pre), ("odigoi/", "Οδηγοί", pre)]
        cta = (home + "#contact", "Επικοινωνία")
    else:
        drops = [N.dd("services", home + "#services", "Services", N.SERVICES_EN, pre, "en")]
        items = [("team/", "Team", pre + "en/")]
        cta = (home + "#contact", "Contact")
    if el:
        el_href, en_href = "./", (pre + alt.lstrip("/")) if alt else pre + "en/"
    else:
        en_href, el_href = "./", (pre + alt.lstrip("/")) if alt else pre

    def lang_links():
        a_el = "active" if el else ""
        a_en = "" if el else "active"
        return (f'<a class="lang-btn {a_el}" data-lang="el" href="{el_href}" hreflang="el" lang="el"><img src="{pre}img/flag-gr.svg" alt="" class="flag-icon" width="20" height="14"> <span class="lcode">ΕΛ</span></a>'
                f'<div class="lang-sep"></div>'
                f'<a class="lang-btn {a_en}" data-lang="en" href="{en_href}" hreflang="en" lang="en"><img src="{pre}img/flag-gb.svg" alt="" class="flag-icon" width="20" height="10"> <span class="lcode">EN</span></a>')
    links = "\n".join(["                " + d for d in drops] + [f'                <a href="{base}{h}">{t}</a>' for h, t, base in items])
    name = "ΜΑΛΛΙΑΡΗΣ &amp; ΣΥΝΕΡΓΑΤΕΣ" if el else "MALLIARIS &amp; PARTNERS"
    title = "Σύμβουλοι Υγείας και Ασφάλειας - Τεχνικοί Ασφαλείας" if el else "Health &amp; Safety Consultants - Safety Technicians"
    alt_logo = "Μάλλιαρης &amp; Συνεργάτες — αρχική σελίδα" if el else "Malliaris &amp; Partners — home"
    menu = "Μενού" if el else "Menu"
    return f'''    <nav id="nav" aria-label="{"Κύριο μενού" if el else "Main menu"}">
        <div class="nav-logo-group">
            <a href="{home}" class="nav-logo">
                <div class="logo-rect"><img decoding="async" width="300" height="200" src="{pre}img/logo-malliaris-synergates.webp" alt="{alt_logo}"></div>
                <div class="logo-text">
                    <span class="name">{name}</span>
                    <span class="title">{title}</span>
                </div>
            </a>
            <div class="nav-logo-lang-sep"></div>
            <div class="nav-logo-lang">{lang_links()}</div>
        </div>
        <div class="nav-right">
            <div class="nav-links" id="navLinks">
{links}
                <a href="{cta[0]}" class="nav-cta">{cta[1]}</a>
            </div>
            <div class="lang-toggle">{lang_links()}</div>
        </div>
        <div class="mobile-nav-right">
            <div class="mobile-lang">{lang_links()}</div>
            <div class="mobile-nav-sep"></div>
            <div class="hamburger" id="hamburger" role="button" tabindex="0" aria-label="{menu}" aria-controls="navLinks" aria-expanded="false">
                <span></span><span></span><span></span>
            </div>
        </div>
    </nav>'''


def hero(p, pre):
    el = p["lang"] == "el"
    home = pre if el else pre + "en/"
    crumbs = [f'<li><a href="{home}">{"Αρχική" if el else "Home"}</a></li>']
    for name, path in p.get("crumbs", []):
        crumbs.append(f'<li><a href="{pre}{path.lstrip("/")}">{esc(name)}</a></li>')
    crumbs.append(f'<li aria-current="page">{esc(p["crumb"])}</li>')
    ctas = p.get("ctas", True)
    cta_html = ""
    if ctas:
        if el:
            cta_html = (f'<div class="page-cta"><a href="{home}#contact" class="btn-accent">ΖΗΤΗΣΤΕ ΠΡΟΣΦΟΡΑ</a>'
                        f'<a href="tel:{E.PHONE_E164}" class="btn-ghost"><i class="fa-solid fa-phone" aria-hidden="true"></i> {E.PHONE_DISPLAY}</a></div>')
        else:
            cta_html = (f'<div class="page-cta"><a href="{home}#contact" class="btn-accent">REQUEST A QUOTE</a>'
                        f'<a href="tel:{E.PHONE_E164}" class="btn-ghost"><i class="fa-solid fa-phone" aria-hidden="true"></i> {E.PHONE_DISPLAY}</a></div>')
    upd = p.get("updated", TODAY)
    d = date.fromisoformat(upd)
    meta = ""
    if p.get("author", True):
        if el:
            meta = f'<p class="page-meta">Σύνταξη και έλεγχος: <a href="{pre}omada/">Σταύρος Μάλλιαρης</a>, Πολιτικός Μηχανικός ΑΠΘ, ASP® · Τελευταία ενημέρωση: <time datetime="{upd}">{d.day}/{d.month}/{d.year}</time></p>'
        else:
            meta = f'<p class="page-meta">Written and reviewed by <a href="{pre}en/team/">Stavros Malliaris</a>, Civil Engineer (AUTh), ASP® · Last updated: <time datetime="{upd}">{d.strftime("%d %B %Y")}</time></p>'
    return f'''    <header class="page-hero">
        <div class="page-hero-inner">
            <div class="breadcrumbs" role="navigation" aria-label="{"Διαδρομή" if el else "Breadcrumb"}"><ol>{"".join(crumbs)}</ol></div>
            <div class="eyebrow"><span>{p["eyebrow"]}</span></div>
            <h1 class="page-h1">{p["h1"]}</h1>
            <p class="page-lead">{p["lead"]}</p>
            {cta_html}
            {meta}
        </div>
    </header>'''


def faq_block(p):
    if not p.get("faq"):
        return ""
    el = p["lang"] == "el"
    items = "".join(f'''
                <details class="faq-item">
                    <summary>{esc(q)}</summary>
                    <div class="faq-answer"><p>{a}</p></div>
                </details>''' for q, a in p["faq"])
    return f'''
    <section class="page-section" aria-labelledby="h-faq">
        <div class="page-section-inner">
            <div class="eyebrow"><span>{"Συχνές ερωτήσεις" if el else "FAQ"}</span></div>
            <h2 id="h-faq" class="section-heading">{"Ερωτήσεις που μας κάνουν" if el else "Questions we are asked"}</h2>
            <div class="faq-list">{items}
            </div>
        </div>
    </section>'''


def related_block(p, pre):
    rel = p.get("related")
    if not rel:
        return ""
    el = p["lang"] == "el"
    cards = "".join(f'''
                <a class="resource-card" href="{pre}{href.lstrip("/")}">
                    <div class="resource-icon"><i class="fa-solid {icon}" aria-hidden="true"></i></div>
                    <h3>{esc(t)}</h3>
                    <p>{esc(txt)}</p>
                </a>''' for href, icon, t, txt in rel)
    return f'''
    <section class="page-section" aria-labelledby="h-related">
        <div class="page-section-inner">
            <div class="eyebrow"><span>{"Δείτε επίσης" if el else "See also"}</span></div>
            <h2 id="h-related" class="section-heading">{"Σχετικές υπηρεσίες και οδηγοί" if el else "Related pages"}</h2>
            <div class="related-grid">{cards}
            </div>
        </div>
    </section>'''


def author_box(p, pre):
    if not p.get("author", True):
        return ""
    el = p["lang"] == "el"
    if el:
        return f'''<aside class="author-box" aria-label="Ποιος υπογράφει">
                <img src="{pre}img/stavros-malliaris.webp" alt="Σταύρος Μάλλιαρης" width="72" height="72" loading="lazy" decoding="async">
                <div><div class="ab-role">Ποιος υπογράφει</div><div class="ab-name">Σταύρος Μάλλιαρης</div>
                <div class="ab-text">Πολιτικός Μηχανικός ΑΠΘ, MEng, ASP® (BCSP), εσωτερικός επιθεωρητής ISO 45001. <a href="{pre}omada/">Η ομάδα μας</a></div></div>
            </aside>'''
    return f'''<aside class="author-box" aria-label="Author">
                <img src="{pre}img/stavros-malliaris.webp" alt="Stavros Malliaris" width="72" height="72" loading="lazy" decoding="async">
                <div><div class="ab-role">Written by</div><div class="ab-name">Stavros Malliaris</div>
                <div class="ab-text">Civil Engineer (AUTh), MEng, ASP® (BCSP), ISO 45001 internal auditor. <a href="{pre}en/team/">Our team</a></div></div>
            </aside>'''


def contact_band(p, pre):
    el = p["lang"] == "el"
    home = pre if el else pre + "en/"
    if el:
        h, txt, form = "Μιλήστε <em>μαζί μας</em>", "Πείτε μας τι κάνει η επιχείρησή σας και πόσους εργαζόμενους έχει. Σας απαντάμε με συγκεκριμένη πρόταση.", "Φόρμα επικοινωνίας"
        addr, book = "Δωδεκανήσου 16, 174 56 Άλιμος", "Κλείστε ραντεβού 15′"
    else:
        h, txt, form = "Talk <em>to us</em>", "Tell us what your company does and how many people it employs. We reply with a concrete proposal, in English.", "Contact form"
        addr, book = "Dodekanisou 16, 174 56 Alimos, Athens", "Book a 15′ call"
    return f'''
    <section class="page-contact" aria-labelledby="h-contact">
        <div class="page-contact-inner">
            <div>
                <div class="eyebrow"><span>{"Επικοινωνία" if el else "Contact"}</span></div>
                <h2 id="h-contact" class="section-heading">{h}</h2>
                <p>{txt}</p>
            </div>
            <div class="pc-list">
                <a href="tel:{E.PHONE_E164}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {E.PHONE_DISPLAY}</a>
                <a href="mailto:{E.EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i> {E.EMAIL}</a>
                <a href="{home}#contact"><i class="fa-solid fa-pen-to-square" aria-hidden="true"></i> {form}</a>
                <a href="https://calendly.com/stamalliaris2/15min" target="_blank" rel="noopener"><i class="fa-regular fa-calendar-check" aria-hidden="true"></i> {book}</a>
                <a href="{E.MAP_URL}" target="_blank" rel="noopener"><i class="fa-solid fa-location-dot" aria-hidden="true"></i> {addr}</a>
            </div>
        </div>
    </section>'''


def footer(p, pre):
    el = p["lang"] == "el"
    if el:
        cols = [("Υπηρεσίες", [("texnikos-asfaleias/", "Τεχνικός Ασφαλείας"), ("geek-grapti-ektimisi-kindynou/", "Γραπτή Εκτίμηση Κινδύνου (ΓΕΕΚ)"),
                               ("ekpaideuseis-ygeias-asfaleias/", "Εκπαιδεύσεις Υ&Α"), ("diereynisi-ergatikou-atyximatos/", "Διερεύνηση ατυχημάτων"),
                               ("schedia-diafygis-ekkenosis/", "Σχέδια διαφυγής"), ("elegxos-epitheorisis-ergasias/", "Έλεγχος Επιθεώρησης Εργασίας")]),
                ("Κλάδοι", [("kataskeves-ergotaxia/", "Κατασκευές & εργοτάξια"), ("viomixania-logistics/", "Βιομηχανία & logistics"),
                            ("mikres-epixeiriseis/", "Μικρές επιχειρήσεις"), ("en/foreign-companies-greece/", "Ξένες εταιρείες (EN)")]),
                ("Η εταιρεία", [("omada/", "Η ομάδα"), ("odigoi/", "Οδηγοί"), ("odigoi/ores-texnikou-asfaleias/", "Υπολογιστής ωρών ΤΑ"),
                                ("aporrito/", "Πολιτική απορρήτου"), ("#cookies", "Ρυθμίσεις cookies")])]
        brand, sub, contact = "ΜΑΛΛΙΑΡΗΣ &amp; ΣΥΝΕΡΓΑΤΕΣ", "Υπηρεσίες Υγείας και Ασφάλειας - Τεχνικοί Ασφαλείας", "Επικοινωνία"
        addr = "Δωδεκανήσου 16, 174 56 Άλιμος"
    else:
        cols = [("Services", [("en/safety-technician-greece/", "Safety technician"), ("en/risk-assessment-greece/", "Written risk assessment"),
                              ("en/foreign-companies-greece/", "Foreign companies in Greece"), ("en/", "All services")]),
                ("Company", [("en/team/", "Our team"), ("en/privacy/", "Privacy policy"), ("#cookies", "Cookie settings"), ("", "Greek version")]),
                ("Greek guides", [("odigoi/", "Guides (in Greek)"), ("odigoi/ores-texnikou-asfaleias/", "Hours calculator (GR)")])]
        brand, sub, contact = "MALLIARIS &amp; PARTNERS", "Health &amp; Safety Consultants - Safety Technicians", "Contact"
        addr = "Dodekanisou 16, 174 56 Alimos, Athens"

    def a(h, t):
        if h == "#cookies":
            return f'<a href="#" data-cc-open>{esc(t)}</a>'
        return f'<a href="{pre}{h}">{esc(t)}</a>'
    colhtml = "".join(f'''
            <div class="footer-nav-col">
                <p class="footer-nav-title">{t}</p>
                {"".join(a(h, x) for h, x in links)}
            </div>''' for t, links in cols)
    return f'''    <footer>
        <div class="footer-top">
            <div class="footer-brand">
                <div class="footer-logo-rect"><img src="{pre}img/logo-malliaris-synergates.webp" alt="" width="300" height="200" loading="lazy" decoding="async"></div>
                <div class="footer-brand-text"><p class="fname">{brand}</p><p class="ftitle">{sub}</p></div>
            </div>
        </div>
        <div class="footer-nav">{colhtml}
            <div class="footer-nav-col">
                <p class="footer-nav-title">{contact}</p>
                <a href="tel:{E.PHONE_E164}">{E.PHONE_DISPLAY}</a>
                <a href="mailto:{E.EMAIL}">{E.EMAIL}</a>
                <a href="{E.MAP_URL}" target="_blank" rel="noopener">{addr}</a>
            </div>
        </div>
        <hr class="ec-rule">
        <div class="expertease-credit">
          <div class="ec-layer ec-layer--credit">
            <span class="ec-copy">© 2026 · All Rights Reserved</span>
            <span class="ec-divider"></span>
            <a href="https://expertease.eu/webdesign" target="_blank" rel="noopener" class="ec-brand">
              <span class="ec-label">Designed by</span>
              <img src="{pre}img/logo-expertease.webp" alt="Expertease Designs" class="ec-logo" width="96" height="95" loading="lazy" decoding="async">
              <span class="ec-name">Expertease Designs</span>
            </a>
          </div>
        </div>
    </footer>'''


def render(p, alt):
    pre = prefix_for(p["path"])
    body = p["body"].replace("{PRE}", pre)
    skip = "Μετάβαση στο περιεχόμενο" if p["lang"] == "el" else "Skip to content"
    extra_js = "".join(f'\n    <script src="{pre}{s}" defer></script>' for s in p.get("scripts", []))
    out = f'''{head(p, pre, alt)}
<body>
    <a class="skip-link" href="#main">{skip}</a>
{nav(p, pre, alt)}

    <main id="main">
{hero(p, pre)}
{body}
{faq_block(p)}
{related_block(p, pre).replace("{PRE}", pre)}
{contact_band(p, pre)}
    </main>

{footer(p, pre)}
    <script src="{pre}page.js" defer></script>
    <script src="{pre}site-nav.js" defer></script>{extra_js}
</body>
</html>
'''
    out = re.sub(r'(<a [^>]*?) hreflang="(?:el|en)"', r"\1", out)
    return out.replace("{PRE}", pre)


def author_html(p):
    return author_box(p, prefix_for(p["path"]))


def main():
    import pages_el, pages_en
    pages = pages_el.PAGES + pages_en.PAGES
    by_path = {p["path"]: p for p in pages}
    for p in pages:
        alt = p.get("alt")
        if alt and alt not in by_path and alt not in ("/", "/en/"):
            alt = None
        p["body"] = p["body"].replace("{AUTHOR}", author_html(p))
        out = ROOT / p["path"].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p, alt), encoding="utf-8")
    write_sitemap(pages)
    print("σελίδες:", len(pages))


def write_sitemap(pages):
    urls = [("/", "/en/", TODAY), ("/en/", "/", TODAY)]
    for p in pages:
        urls.append((p["path"], p.get("alt"), p.get("updated", TODAY)))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, alt, lm in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{D}{path}</loc>")
        lines.append(f"    <lastmod>{lm}</lastmod>")
        if alt:
            is_en = path.startswith("/en/")
            el_p, en_p = (alt, path) if is_en else (path, alt)
            lines.append(f'    <xhtml:link rel="alternate" hreflang="el" href="{D}{el_p}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{D}{en_p}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{D}{el_p}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
