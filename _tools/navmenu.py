# -*- coding: utf-8 -*-
"""
navmenu.py — υπομενού «Υπηρεσίες» / «Τομείς» στην κεντρική μπάρα.

Μία πηγή για: αρχική (index.html, ανάμεσα σε <!--dd:services--> … <!--/dd:services-->),
en/index.html (το i18n_bake.py βάζει την αγγλική εκδοχή) και τις εσωτερικές σελίδες (build_pages.py).
Οι διαδρομές είναι σχετικές με τη ρίζα του ιστότοπου· το pre δίνει το «../» που χρειάζεται κάθε σελίδα.
"""

SERVICES_EL = [
    ("texnikos-asfaleias/", "Τεχνικός Ασφαλείας"),
    ("geek-grapti-ektimisi-kindynou/", "Γραπτή Εκτίμηση Κινδύνου (ΓΕΕΚ)"),
    ("ekpaideuseis-ygeias-asfaleias/", "Εκπαιδεύσεις Υγείας &amp; Ασφάλειας"),
    ("diereynisi-ergatikou-atyximatos/", "Διερεύνηση Εργατικού Ατυχήματος"),
    ("schedia-diafygis-ekkenosis/", "Σχέδια Διαφυγής &amp; Εκκένωσης"),
    ("elegxos-epitheorisis-ergasias/", "Προετοιμασία για Έλεγχο ΣΕΠΕ"),
]
SERVICES_EL_MORE = [
    ("odigoi/", "Οδηγοί για εργοδότες"),
    ("odigoi/ores-texnikou-asfaleias/", "Υπολογιστής ωρών Τεχνικού Ασφαλείας"),
    ("odigoi/ergodotis-texnikos-asfaleias/", "Ο εργοδότης ως Τεχνικός Ασφαλείας"),
    ("odigoi/ergatiko-atyxima-ti-kanei-o-ergodotis/", "Εργατικό ατύχημα: πρώτα βήματα"),
]

SECTORS_EL = [
    ("kataskeves-ergotaxia/", "Κατασκευές &amp; Εργοτάξια"),
    ("viomixania-logistics/", "Βιομηχανία &amp; Logistics"),
    ("mikres-epixeiriseis/", "Καταστήματα, Εστίαση, Γραφεία"),
    ("en/foreign-companies-greece/", "Ξένες εταιρείες (στα αγγλικά)"),
]

SERVICES_EN = [
    ("en/safety-technician-greece/", "Safety technician"),
    ("en/risk-assessment-greece/", "Written risk assessment (GEEK)"),
    ("en/health-safety-training/", "Health &amp; safety training"),
    ("en/accident-investigation/", "Accident investigation"),
    ("en/evacuation-plans/", "Escape &amp; evacuation plans"),
    ("en/labour-inspection-readiness/", "Labour Inspectorate readiness"),
]
SERVICES_EN_MORE = [
    ("en/guides/", "Guides for employers"),
    ("en/guides/safety-technician-hours/", "Safety technician hours calculator"),
    ("en/guides/employer-as-safety-technician/", "Employer as safety technician"),
    ("en/guides/workplace-accident-employer-steps/", "Workplace accident: first steps"),
]

SECTORS_EN = [
    ("en/construction-sites/", "Construction sites"),
    ("en/industry-logistics/", "Industry &amp; logistics"),
    ("en/small-businesses/", "Shops, restaurants, offices"),
    ("en/foreign-companies-greece/", "Foreign companies in Greece"),
]


def dd(key, trigger_href, trigger_label, items, pre, lang="el", i18n_key=None, more=None):
    """Ένα αναπτυσσόμενο στοιχείο της μπάρας: σύνδεσμος + κουμπί-βέλος + λίστα."""
    el = lang == "el"
    aria = {"services": ("Υπομενού υπηρεσιών", "Services submenu"),
            "sectors": ("Υπομενού τομέων", "Sectors submenu")}[key][0 if el else 1]
    di = f' data-i18n="{i18n_key}"' if i18n_key else ""
    rows = "".join(f'<a href="{pre}{h}">{t}</a>' for h, t in items)
    if more:
        rows += '<span class="nav-dd-sep" aria-hidden="true"></span>'
        rows += "".join(f'<a href="{pre}{h}">{t}</a>' for h, t in more)
    return (f'<div class="nav-dd">'
            f'<a href="{trigger_href}"{di}>{trigger_label}</a>'
            f'<button class="nav-dd-toggle" type="button" aria-expanded="false" aria-controls="dd-{key}" aria-label="{aria}"></button>'
            f'<div class="nav-dd-menu" id="dd-{key}">{rows}</div>'
            f'</div>')


def home_block(key, lang, label, pre=""):
    """Το μπλοκ της αρχικής (με τους δείκτες), για index.html και en/index.html."""
    if lang == "el":
        if key == "services":
            inner = dd("services", "#services", label, SERVICES_EL, pre, "el", "nav.services", SERVICES_EL_MORE)
        else:
            inner = dd("sectors", "#sectors", label, SECTORS_EL, pre, "el", "nav.sectors")
    else:
        # στην /en/ οι σύνδεσμοι γράφονται σχετικά με τη ρίζα της /en/
        strip = lambda items: [(h[len("en/"):], t) for h, t in items]
        if key == "services":
            inner = dd("services", "#services", label, strip(SERVICES_EN), "", "en", "nav.services", strip(SERVICES_EN_MORE))
        else:
            inner = dd("sectors", "#sectors", label, strip(SECTORS_EN), "", "en", "nav.sectors")
    return f"<!--dd:{key}-->{inner}<!--/dd:{key}-->"
