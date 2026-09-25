# -*- coding: utf-8 -*-
"""Content of inner pages — ENGLISH. Same legal basis as pages_el.py."""
from pages_el import S

LAW = "Law 3850/2010, now codified in the Greek Labour Code (Presidential Decree 62/2025)"

REL = [
    ("en/safety-technician-greece/", "fa-file-shield", "Safety technician", "Appointment, site visits, written recommendations."),
    ("en/risk-assessment-greece/", "fa-file-lines", "Written risk assessment", "Hazards per job position and prevention measures."),
    ("en/foreign-companies-greece/", "fa-earth-europe", "Foreign companies in Greece", "Your health and safety obligations, in plain English."),
    ("en/team/", "fa-users", "Our team", "Engineers from Aristotle University of Thessaloniki."),
]


def rel(*keys):
    return [r for r in REL if r[0] in keys]


PAGES = []

PAGES.append(dict(
    lang="en", path="/en/safety-technician-greece/", alt="/texnikos-asfaleias/",
    title="Safety Technician Services in Athens, Greece",
    desc="Mandatory safety technician (technikos asfaleias) services for companies in Athens and Attica: appointment, site visits, written recommendations, in English.",
    crumb="Safety technician", eyebrow="Service", service="Safety technician services",
    h1="Safety technician services <em>in Athens, Greece</em>",
    lead=("In Greece, every employer with at least one employee must use a safety technician (technikos asfaleias). "
          "We take on the role formally, visit your premises on a schedule, give written recommendations and keep your "
          "health and safety file up to date. We work in English and Greek."),
    faq=[
        ("Is a safety technician mandatory for a small office?",
         f"Yes. The obligation applies from the first employee, whatever the activity ({LAW}). In small category B and C businesses the law allows, under conditions, the employer or a trained employee to take on the duties."),
        ("How many hours per year are required?",
         "It depends on the risk category of your activity (A, B or C, based on the activity code) and on your headcount. We confirm the category and calculate the hours before we send an offer."),
        ("Do we also need an occupational physician?",
         "As a rule, from 50 employees upwards. We check this at the start and work with the occupational physician where required."),
        ("Can you report to a head office abroad?",
         "Yes. We write visit reports and action plans in English, while the legally required records are kept in Greek."),
    ],
    related=rel("en/risk-assessment-greece/", "en/foreign-companies-greece/", "en/team/"),
    body=S("What the role covers", """
<ul class="check-grid">
<li>Formal appointment and notification to the Labour Inspectorate system</li>
<li>Scheduled site visits, based on the hours your category requires</li>
<li>Written recommendations after each visit, with priorities</li>
<li>Preparing or updating the written occupational risk assessment</li>
<li>Staff training and briefings, with attendance records</li>
<li>Fire safety, escape routes and first-aid checks</li>
<li>Reminders of employer duties, e.g. reporting accidents within 24 hours and CPR training</li>
<li>Coordination with the occupational physician where needed</li>
</ul>
""", "Scope", "h-scope") + S("Risk categories and hours", """
<p>Businesses fall into three categories: <strong>A</strong> (high risk), <strong>B</strong> (medium) and <strong>C</strong> (low), according to their activity code (Article 500 of P.D. 62/2025, table replaced by Law 5239/2025). The category and headcount set the minimum yearly hours of the safety technician.</p>
<p>Because the classification table changed in 2025, we re-check it for every new client, even if you already had a safety technician. Our <a href="{PRE}odigoi/ores-texnikou-asfaleias/" hreflang="el">hours calculator</a> (in Greek) gives a first estimate.</p>
{AUTHOR}
""", "Hours", "h-hours"),
))

PAGES.append(dict(
    lang="en", path="/en/risk-assessment-greece/", alt="/geek-grapti-ektimisi-kindynou/",
    title="Written Occupational Risk Assessment in Greece",
    desc="We prepare and update the written occupational risk assessment (GEEK) required from every employer in Greece, after a site survey of each job position.",
    crumb="Written risk assessment", eyebrow="Service", service="Written occupational risk assessment",
    h1="Written occupational <em>risk assessment</em>",
    lead=("Every employer in Greece must have a written assessment of the risks to employees' safety and health, "
          "known in Greek as GEEK, whatever the number of employees. We prepare it after visiting your premises, so it "
          "describes your actual work and the measures that make sense for it."),
    faq=[
        ("Which article requires it?",
         "Article 534 of the Greek Labour Code (P.D. 62/2025), formerly Article 43 of Law 3850/2010."),
        ("Can we reuse our group's risk assessment?",
         "It is a useful starting point, but the Greek assessment has to reflect the local premises, positions and legal requirements, and be available in Greek."),
    ],
    related=rel("en/safety-technician-greece/", "en/foreign-companies-greece/", "en/team/"),
    body=S("What a proper assessment contains", """
<ul>
<li>Description of the premises, equipment and activities</li>
<li>Each job position and the tasks performed</li>
<li>Hazards per position (mechanical, electrical, chemical, ergonomic, fire, psychosocial) and their assessment</li>
<li>Existing and additional measures, prioritised, with owners and deadlines</li>
<li>Resulting PPE and training needs</li>
</ul>
<p>Even when an employer is allowed to act as safety technician, the written risk assessment must be prepared by a person holding the safety technician qualifications set by law.</p>
{AUTHOR}
""", "Contents", "h-contents"),
))

PAGES.append(dict(
    lang="en", path="/en/foreign-companies-greece/", alt=None,
    title="Health & Safety for Foreign Companies in Greece",
    desc="Plain-English guide to health and safety duties for foreign companies with staff in Greece: safety technician, risk assessment, accident reporting.",
    crumb="Foreign companies in Greece", eyebrow="Guide", service="Health and safety support for foreign companies in Greece",
    h1="Health &amp; safety in Greece <em>for foreign companies</em>",
    lead=("If your company employs people in Greece, Greek health and safety law applies from the first employee. "
          "You need a safety technician, a written risk assessment in Greek, and a few specific procedures such as "
          "24-hour accident reporting. Here is what that means in practice, and how we can take it off your hands."),
    faq=[
        ("We only have two sales staff in Athens. Does this apply?",
         "Yes. The duties apply from the first employee. For a small office the effort is modest, but the appointment and the risk assessment are still required."),
        ("Who is the authority?",
         "The Labour Inspectorate (Epitheorisi Ergasias), still often called SEPE. Accidents are also reported to e-EFKA, the social security body."),
        ("Can you work with our regional EHS team?",
         "Yes. We align with your group standards and report in English, while keeping the Greek records the law asks for."),
    ],
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/team/"),
    body=S("Your main obligations", f"""
<ol class="steps">
<li><strong>Safety technician</strong>Required from the first employee ({LAW}). Small category B and C businesses (up to 20 employees) may, under conditions, use the employer or a trained employee.</li>
<li><strong>Occupational physician</strong>As a rule, required from 50 employees upwards.</li>
<li><strong>Written risk assessment (GEEK)</strong>Mandatory for every employer (Article 534 of P.D. 62/2025), prepared by a qualified person and kept up to date.</li>
<li><strong>Accident reporting</strong>Every workplace accident must be reported within 24 hours to the Labour Inspectorate and e-EFKA, and to the police for serious injury or death. Evidence must be kept unchanged.</li>
<li><strong>Occupational disease</strong>Reported within 5 days of being informed by the occupational physician or a public health system doctor.</li>
<li><strong>CPR and Heimlich training</strong>Required since 1 January 2026: through free ministry video material for up to 50 employees per site; above that, courses by certified providers for at least half the staff every three years.</li>
<li><strong>Records</strong>Recommendations book, accident book and list of accidents with more than three working days of incapacity.</li>
</ol>
<p class="src">Legal basis: Greek Labour Code (P.D. 62/2025), as amended by Law 5239/2025 (Government Gazette A' 178/2025). This summary is for orientation and does not replace advice for your specific case.</p>
""", "Checklist", "h-duties") + S("How we help", """
<p>We act as your safety technician in Attica, prepare the risk assessment, run training in English or Greek and keep the Greek records in order. You get one English-speaking engineer as contact, and reports your head office can read.</p>
{AUTHOR}
""", "Service", "h-help"),
))

PAGES.append(dict(
    lang="en", path="/en/team/", alt="/omada/", people=True, page_type="AboutPage", author=False,
    title="Our Team | Malliaris & Partners",
    desc="Meet the engineers of Malliaris & Partners: Stavros Malliaris (ASP®), Dimitrios Moudiotis, Vaios Liapis and Eleftherios Adam.",
    crumb="Team", eyebrow="About us",
    h1="The team at <em>Malliaris &amp; Partners</em>",
    lead=("We are engineers with experience on construction sites, in industry and in services, in Greece and abroad. "
          "The company was founded in March 2026 and is based in Alimos, Athens."),
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/foreign-companies-greece/"),
    body=S("People", """
<div class="team-grid">
  <article class="team-card"><img src="{PRE}img/stavros-malliaris.webp" alt="Stavros Malliaris" width="591" height="588" loading="lazy" decoding="async">
    <div><div class="tc-role">Founder &amp; lead engineer</div><h3>Stavros Malliaris</h3>
    <p>Civil Engineer (Aristotle University of Thessaloniki) specialising in occupational health and safety (MEng). Over ten years of experience on construction sites, industrial facilities and all types of businesses in Greece and abroad. ASP® certified by the Board of Certified Safety Professionals (BCSP) and internal auditor for ISO 9001, 14001 and 45001.</p></div></article>
  <article class="team-card"><img src="{PRE}img/dimitrios-moudiotis.webp" alt="Dimitrios Moudiotis" width="400" height="400" loading="lazy" decoding="async">
    <div><div class="tc-role">Mechanical engineering lead</div><h3>Dimitrios Moudiotis</h3>
    <p>Mechanical Engineer (AUTh). Machinery, work equipment, lifting equipment and vehicles. <a href="https://www.moudiotis.gr/" target="_blank" rel="noopener">moudiotis.gr</a></p></div></article>
  <article class="team-card"><img src="{PRE}img/vaios-liapis.webp" alt="Vaios Liapis" width="347" height="400" loading="lazy" decoding="async">
    <div><div class="tc-role">Engineering studies lead</div><h3>Vaios Liapis</h3>
    <p>Civil Engineer (AUTh). Studies and drawings: floor plans, escape plans, technical studies. <a href="https://www.vaiosliapis.gr/" target="_blank" rel="noopener">vaiosliapis.gr</a></p></div></article>
  <article class="team-card"><img src="{PRE}img/eleftherios-adam.webp" alt="Eleftherios Adam" width="400" height="400" loading="lazy" decoding="async">
    <div><div class="tc-role">HSE officer</div><h3>Eleftherios Adam</h3>
    <p>BSc Materials Science, University of Patras. Field support, inspections and training.</p></div></article>
</div>
""", "Team", "h-people"),
))

PAGES.append(dict(
    lang="en", path="/en/privacy/", alt="/aporrito/", author=False, ctas=False,
    title="Privacy and Cookie Policy | Malliaris & Partners",
    desc="How Malliaris & Partners uses the details you send through the contact form, and how Google Analytics cookies work on this website.",
    crumb="Privacy policy", eyebrow="Information",
    h1="Privacy <em>and cookies</em>",
    lead="This page explains what data the website collects, why, and how you can exercise your rights.",
    body=S("Controller", """
<p>Malliaris &amp; Partners, Dodekanisou 16, 174 56 Alimos, Greece · +30 211 0040 193 · <a href="mailto:info@stavrosmalliaris.gr">info@stavrosmalliaris.gr</a></p>
""", "", "h-ctrl") + S("Contact form", """
<p>When you use the contact form we receive your name, email, phone (if given), subject and message. We use them only to reply and to prepare an offer. The form is sent through a Google service (Apps Script) to our mailbox. We keep the correspondence as long as needed for your request and any resulting cooperation, and delete it when no longer needed or when you ask us to.</p>
""", "", "h-form") + S("Cookies and Google Analytics", """
<p>Google Analytics 4 runs only if you click “Accept” in the cookie banner; without consent the script is not loaded at all. We measure, anonymously, which pages are read and whether the contact buttons are used. We do not use advertising cookies. You can change your choice at any time via <a href="#" data-cc-open>Cookie settings</a>. The map and web fonts are loaded from Google services, which may log your IP address under their own policies.</p>
""", "", "h-cookies") + S("Your rights", """
<p>You have the right of access, rectification, erasure, restriction, portability and objection. Write to <a href="mailto:info@stavrosmalliaris.gr">info@stavrosmalliaris.gr</a>. You may also lodge a complaint with the Hellenic Data Protection Authority (<a href="https://www.dpa.gr/" target="_blank" rel="noopener">dpa.gr</a>).</p>
<p class="src">Last updated: 25 September 2026</p>
""", "", "h-rights"),
))
