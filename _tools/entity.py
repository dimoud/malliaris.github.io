# -*- coding: utf-8 -*-
"""Κοινά στοιχεία οντότητας (NAP, πρόσωπα, υπηρεσίες) για JSON-LD όλων των σελίδων.
Μία πηγή αλήθειας: αν αλλάξει τηλέφωνο/διεύθυνση/email, αλλάζει ΕΔΩ και ξανατρέχει το _tools/build.py."""
import json

DOMAIN = "https://malliarisandpartners.gr"
ORG_ID = DOMAIN + "/#organization"
SITE_ID = DOMAIN + "/#website"
PHONE_E164 = "+302110040193"
PHONE_DISPLAY = "+30 211 0040 193"
EMAIL = "info@stavrosmalliaris.gr"
MAP_URL = "https://share.google/xxk94ucxrcYaLiCtk"
ADDRESS = {"@type": "PostalAddress", "streetAddress": "Δωδεκανήσου 16", "addressLocality": "Άλιμος",
           "postalCode": "17456", "addressRegion": "Αττική", "addressCountry": "GR"}
ADDRESS_EN = {"@type": "PostalAddress", "streetAddress": "Dodekanisou 16", "addressLocality": "Alimos",
              "postalCode": "17456", "addressRegion": "Attica", "addressCountry": "GR"}

PEOPLE = [
    {"@type": "Person", "@id": DOMAIN + "/#stavros-malliaris", "name": "Σταύρος Μάλλιαρης",
     "alternateName": "Stavros Malliaris", "jobTitle": "Ιδρυτής & επικεφαλής μηχανικός υγείας και ασφάλειας",
     "image": DOMAIN + "/img/stavros-malliaris.webp", "worksFor": {"@id": ORG_ID},
     "alumniOf": {"@type": "CollegeOrUniversity", "name": "Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης"},
     "hasCredential": [
         {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree",
          "name": "Δίπλωμα Πολιτικού Μηχανικού ΑΠΘ",
          "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης"}},
         {"@type": "EducationalOccupationalCredential", "credentialCategory": "certification",
          "name": "ASP® — Associate Safety Professional",
          "recognizedBy": {"@type": "Organization", "name": "Board of Certified Safety Professionals (BCSP)"}}],
     "knowsAbout": ["Υγεία και ασφάλεια στην εργασία", "Τεχνικός ασφαλείας", "Γραπτή εκτίμηση επαγγελματικού κινδύνου",
                    "Διερεύνηση εργατικών ατυχημάτων", "ISO 45001", "Occupational health and safety"],
     "knowsLanguage": ["el", "en"]},
    {"@type": "Person", "@id": DOMAIN + "/#dimitrios-moudiotis", "name": "Δημήτριος Μουδιώτης",
     "alternateName": "Dimitrios Moudiotis", "jobTitle": "Υπεύθυνος μηχανολογικών", "worksFor": {"@id": ORG_ID},
     "image": DOMAIN + "/img/dimitrios-moudiotis.webp",
     "alumniOf": {"@type": "CollegeOrUniversity", "name": "Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης"},
     "sameAs": ["https://www.moudiotis.gr/"]},
    {"@type": "Person", "@id": DOMAIN + "/#vaios-liapis", "name": "Βάιος Λιάπης",
     "alternateName": "Vaios Liapis", "jobTitle": "Υπεύθυνος μελετών", "worksFor": {"@id": ORG_ID},
     "image": DOMAIN + "/img/vaios-liapis.webp",
     "alumniOf": {"@type": "CollegeOrUniversity", "name": "Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης"},
     "sameAs": ["https://www.vaiosliapis.gr/"]},
    {"@type": "Person", "@id": DOMAIN + "/#eleftherios-adam", "name": "Ελευθέριος Αδάμ",
     "alternateName": "Eleftherios Adam", "jobTitle": "HSE Officer", "worksFor": {"@id": ORG_ID},
     "image": DOMAIN + "/img/eleftherios-adam.webp",
     "alumniOf": {"@type": "CollegeOrUniversity", "name": "Πανεπιστήμιο Πατρών"}},
]

SERVICES = [
    ("Τεχνικός Ασφαλείας", "Safety technician services", "/texnikos-asfaleias/"),
    ("Γραπτή Εκτίμηση Επαγγελματικού Κινδύνου (ΓΕΕΚ)", "Written occupational risk assessment", "/geek-grapti-ektimisi-kindynou/"),
    ("Προετοιμασία για έλεγχο της Επιθεώρησης Εργασίας", "Labour inspection readiness", "/elegxos-epitheorisis-ergasias/"),
    ("Εκπαιδεύσεις υγείας και ασφάλειας", "Health and safety training", "/ekpaideuseis-ygeias-asfaleias/"),
    ("Σχέδια διαφυγής και εκκένωσης", "Escape and evacuation plans", "/schedia-diafygis-ekkenosis/"),
    ("Διερεύνηση εργατικών ατυχημάτων", "Workplace accident investigation", "/diereynisi-ergatikou-atyximatos/"),
]

def org(lang="el"):
    el = lang == "el"
    return {
        "@type": "ProfessionalService", "@id": ORG_ID,
        "name": "Μάλλιαρης & Συνεργάτες" if el else "Malliaris & Partners",
        "alternateName": ["Malliaris & Partners", "ΜΑΛΛΙΑΡΗΣ & ΣΥΝΕΡΓΑΤΕΣ"] if el else ["Μάλλιαρης & Συνεργάτες"],
        "description": ("Ομάδα μηχανικών που καλύπτει επιχειρήσεις στην Αττική σε θέματα υγείας και ασφάλειας στην εργασία: "
                        "τεχνικός ασφαλείας, ΓΕΕΚ, εκπαιδεύσεις, σχέδια διαφυγής, διερεύνηση ατυχημάτων.") if el else
                       ("Engineering team providing occupational health and safety services to companies in Athens and Attica: "
                        "safety technician, written risk assessment, training, evacuation plans, accident investigation."),
        "disambiguatingDescription": "Σύμβουλοι υγείας και ασφάλειας στην εργασία, Άλιμος Αττικής" if el else
                                     "Occupational health and safety consultancy based in Alimos, Attica, Greece",
        "url": DOMAIN + ("/" if el else "/en/"),
        "logo": DOMAIN + "/img/logo-malliaris-synergates.webp",
        "image": DOMAIN + "/img/og-malliaris-synergates.jpg",
        "telephone": PHONE_E164, "email": EMAIL,
        "address": ADDRESS if el else ADDRESS_EN,
        "hasMap": MAP_URL,
        "areaServed": {"@type": "AdministrativeArea", "name": "Αττική" if el else "Attica, Greece"},
        "knowsLanguage": ["el", "en"],
        "foundingDate": "2026-03",
        "founder": {"@id": DOMAIN + "/#stavros-malliaris"},
        "employee": [{"@id": p["@id"]} for p in PEOPLE],
        "hasOfferCatalog": {"@type": "OfferCatalog",
                            "name": "Υπηρεσίες υγείας και ασφάλειας στην εργασία" if el else "Occupational health and safety services",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {
                                "@type": "Service", "name": (n if el else e), "url": DOMAIN + u,
                                "provider": {"@id": ORG_ID}, "areaServed": {"@type": "AdministrativeArea", "name": "Αττική"}}}
                                for n, e, u in SERVICES]},
    }

def website():
    return {"@type": "WebSite", "@id": SITE_ID, "url": DOMAIN + "/", "name": "Μάλλιαρης & Συνεργάτες",
            "alternateName": "Malliaris & Partners", "inLanguage": ["el", "en"], "publisher": {"@id": ORG_ID}}

def graph(nodes):
    return '<script type="application/ld+json">\n' + json.dumps({"@context": "https://schema.org", "@graph": nodes},
                                                               ensure_ascii=False, indent=1) + '\n</script>'
