# -*- coding: utf-8 -*-
"""Content of inner pages — ENGLISH. One English page for every Greek page (same legal basis as pages_el.py).
Rule: no Greek characters on English pages (transliterate: GEEK, SEPE, e-EFKA, KAD).
"""
from pages_el import S, HLI_TA, HLI_GEEK, GOV_ACC, OIRA

LAW = "Law 3850/2010, now codified in the Greek Labour Code (Presidential Decree 62/2025)"

REL = [
    ("en/safety-technician-greece/", "fa-file-shield", "Safety technician", "Appointment, site visits, written recommendations."),
    ("en/risk-assessment-greece/", "fa-file-lines", "Written risk assessment (GEEK)", "Hazards per job position and prevention measures."),
    ("en/labour-inspection-readiness/", "fa-clipboard-check", "Labour Inspectorate readiness", "Mock inspection and a list of fixes."),
    ("en/health-safety-training/", "fa-person-chalkboard", "Health & safety training", "Work at height, PPE, fire safety, CPR."),
    ("en/evacuation-plans/", "fa-person-running", "Escape & evacuation plans", "Floor plans, routes, roles and drills."),
    ("en/accident-investigation/", "fa-magnifying-glass-chart", "Accident investigation", "Causes, report and corrective actions."),
    ("en/guides/safety-technician-hours/", "fa-calculator", "Hours calculator", "Indicative yearly safety technician hours."),
    ("en/guides/employer-as-safety-technician/", "fa-user-tie", "Employer as safety technician", "When it is allowed after 1 January 2026."),
    ("en/guides/workplace-accident-employer-steps/", "fa-triangle-exclamation", "Workplace accident", "The employer's first steps."),
    ("en/foreign-companies-greece/", "fa-earth-europe", "Foreign companies in Greece", "Your health and safety obligations, in plain English."),
    ("en/small-businesses/", "fa-store", "Small businesses", "Shops, restaurants, offices."),
    ("en/team/", "fa-users", "Our team", "Engineers from Aristotle University of Thessaloniki."),
]


def rel(*keys):
    by = {r[0]: r for r in REL}
    return [by[k] for k in keys]


PAGES = []

# ─────────────────────────────────────────────────────────────── P1 SAFETY TECHNICIAN
PAGES.append(dict(
    lang="en", path="/en/safety-technician-greece/", alt="/texnikos-asfaleias/",
    title="Safety Technician Services in Athens, Greece",
    desc="Mandatory safety technician (technikos asfaleias) services for companies in Athens and Attica: appointment, site visits, written recommendations, in English.",
    crumb="Safety technician", eyebrow="Service", service="Safety technician services",
    h1="Safety technician services <em>in Athens, Greece</em>",
    lead=("In Greece, every employer with at least one employee needs a safety technician (technikos asfaleias). "
          "We take on the role formally, visit your premises on a schedule, give written recommendations and keep your "
          "health and safety file up to date. Hours and cost depend on your risk category and headcount. We work in English and Greek."),
    faq=[
        ("Do I need a safety technician with only one employee?",
         f"Yes. The obligation applies from the first employee ({LAW}). In small category B and C businesses the law allows, under conditions, the employer or one of the employees to take on the duties. See our <a href=\"{{PRE}}en/guides/employer-as-safety-technician/\">guide on the employer as safety technician</a>."),
        ("How many hours per year must the safety technician attend?",
         "It depends on your risk category (A, B or C, based on your activity code) and on your headcount. Our <a href=\"{PRE}en/guides/safety-technician-hours/\">hours calculator</a> gives a first estimate; we confirm the exact category before we send an offer."),
        ("Do we also need an occupational physician?",
         "As a rule, from 50 employees upwards. We check this at the start, together with your category, and work with the occupational physician where required."),
        ("What about the recommendations book?",
         "The safety technician's recommendations are given in writing. Law 5239/2025 moves the recommendations book to electronic form in the Labour Inspectorate's information system (Article 504 of P.D. 62/2025). Until that is fully in operation, we keep the book as currently required."),
        ("Do you cover companies with several shops or sites?",
         "Yes. We plan visits per site, so each location covers its own hours and has its own file."),
        ("Can you report to a head office abroad?",
         "Yes. We write visit reports and action plans in English, while the legally required records are kept in Greek. See also <a href=\"{PRE}en/foreign-companies-greece/\">health and safety for foreign companies</a>."),
    ],
    related=rel("en/risk-assessment-greece/", "en/guides/safety-technician-hours/", "en/guides/employer-as-safety-technician/",
                "en/labour-inspection-readiness/", "en/health-safety-training/", "en/accident-investigation/"),
    body=S("Who needs a safety technician", f"""
<p>An employer must use a safety technician from the moment they employ even one person, whatever the activity. The legal basis is {LAW}, as amended in 2025.</p>
<p>The safety technician advises the employer. They identify hazards, propose measures in writing and follow up on whether they are applied. Responsibility for taking the measures stays with the employer; our job is to show clearly what is needed and in what order.</p>
<div class="facts"><strong>In one sentence:</strong> from the first employee you need a safety technician and a written occupational risk assessment. The hours follow from your risk category and headcount.</div>
<p class="src">Source: <a href="{HLI_TA}" target="_blank" rel="noopener">Labour Inspectorate: safety technician (in Greek)</a></p>
""", "Obligation", "h-who") + S("Risk categories and hours", """
<p>Businesses fall into three categories: <strong>A</strong> (high risk), <strong>B</strong> (medium) and <strong>C</strong> (low). The category follows from the activity code (KAD) of the business, under the new table of Article 500 of P.D. 62/2025, as replaced by Law 5239/2025.</p>
<p>The category and the number of employees set the minimum yearly time of the safety technician. Because the new table changed the category of quite a few activities, we re-check it for every new client, even if you already had a safety technician.</p>
<p><a href="{PRE}en/guides/safety-technician-hours/">Estimate the hours for your business →</a></p>
""", "Hours", "h-hours") + S("What the service includes", """
<ul class="check-grid">
<li>Formal appointment and notification in the Labour Inspectorate's information system</li>
<li>Scheduled site visits, based on the hours your category requires</li>
<li>Written recommendations after each visit, with priorities</li>
<li>Preparing or updating the written occupational risk assessment</li>
<li>Staff training and briefings, with attendance records for the file</li>
<li>Checks of fire safety, escape routes and first-aid equipment</li>
<li>Reminders of employer duties, e.g. reporting accidents within 24 hours and CPR training</li>
<li>Coordination with the occupational physician, where required</li>
</ul>
""", "Scope", "h-incl") + S("How we start", """
<ol class="steps">
<li><strong>Short call</strong>You tell us your activity, activity code, headcount and premises. Ten minutes on the phone is enough.</li>
<li><strong>Category, hours, offer</strong>We check your classification, calculate the hours and send a written offer.</li>
<li><strong>Appointment</strong>The appointment is made and notified, so the business is formally covered.</li>
<li><strong>First site survey</strong>We walk the premises, review the existing file and note what is missing.</li>
<li><strong>Regular visits</strong>Recommendations, training and follow-up of corrections, with the same contact person.</li>
</ol>
{AUTHOR}
""", "Process", "h-steps") + S("Sectors we work in", """
<p>We work with construction sites, industry and warehouses, shops and restaurants, offices, and foreign companies with staff in Greece. For what each type of workplace needs:</p>
<ul>
<li><a href="{PRE}en/construction-sites/">Construction sites</a>: work at height, scaffolding, construction machinery, safety plans</li>
<li><a href="{PRE}en/industry-logistics/">Industry, warehouses and logistics</a>: forklifts, racking, shift work</li>
<li><a href="{PRE}en/small-businesses/">Small businesses</a>: shops, restaurants, offices</li>
<li><a href="{PRE}en/foreign-companies-greece/">Foreign companies in Greece</a></li>
</ul>
""", "Sectors", "h-sectors"),
))

# ─────────────────────────────────────────────────────────────── P2 GEEK
PAGES.append(dict(
    lang="en", path="/en/risk-assessment-greece/", alt="/geek-grapti-ektimisi-kindynou/",
    title="Written Occupational Risk Assessment in Greece",
    desc="We prepare and update the written occupational risk assessment (GEEK) required from every employer in Greece, after a site survey of each job position.",
    crumb="Written risk assessment", eyebrow="Service", service="Written occupational risk assessment",
    h1="Written occupational <em>risk assessment (GEEK)</em>",
    lead=("The written occupational risk assessment, known in Greek as GEEK, records the hazards of every job position and "
          "the measures that control them. Every employer in Greece must have one, whatever the number of employees. "
          "We prepare it after visiting your premises, so it describes your actual work and not a generic business."),
    faq=[
        ("Is the risk assessment mandatory for a small business?",
         "Yes. The employer must have a written assessment of the risks regardless of the number of employees (Article 534 of P.D. 62/2025, formerly Article 43 of Law 3850/2010)."),
        ("If I act as safety technician myself, can I also write the assessment?",
         "Not necessarily. Even when the employer carries out the safety technician duties, the written risk assessment must be prepared by a person holding the safety technician qualifications set by law and the right specialisation for the activity."),
        ("How often is it updated?",
         "Whenever working conditions change materially: new equipment, new processes or positions, a move, after an accident, or when the Labour Inspectorate asks. We also recommend a yearly review."),
        ("What is a MEEK?",
         "\"Occupational risk assessment study\" (MEEK) is often used for the same document. What matters is the content: hazards per position, assessment, measures, owners and a timetable."),
        ("Can we reuse our group's risk assessment?",
         "It is a useful starting point, but the Greek assessment has to reflect the local premises, positions and legal requirements, and be available in Greek."),
        ("How much does it cost?",
         "It depends on the job positions, the premises and the level of risk. After a short call we send you a written offer."),
    ],
    related=rel("en/safety-technician-greece/", "en/labour-inspection-readiness/", "en/health-safety-training/",
                "en/accident-investigation/", "en/evacuation-plans/", "en/guides/employer-as-safety-technician/"),
    body=S("What it is and who needs it", f"""
<p>The employer must have a written assessment of the risks to employees' safety and health, together with the prevention measures that follow from it (Article 534 of P.D. 62/2025, formerly Article 43 of Law 3850/2010). The duty does not depend on size: it applies to a business with a single employee.</p>
<p>In practice the risk assessment is the reference point for everything else: which training is needed, which personal protective equipment, what changes on the premises and in what order.</p>
<p class="src">Sources: <a href="{HLI_GEEK}" target="_blank" rel="noopener">Labour Inspectorate: written risk assessment (in Greek)</a> · <a href="https://oira.osha.europa.eu/en/what-is-risk-assessment" target="_blank" rel="noopener">OiRA (EU-OSHA)</a></p>
""", "Definition", "h-what") + S("What a proper assessment contains", """
<ul>
<li>A description of the business, the premises and the equipment</li>
<li>Each job position, one by one, with the tasks each person performs</li>
<li>The hazards of each position (mechanical, electrical, chemical, ergonomic, fire, psychosocial) and their assessment</li>
<li>Measures already in place and those to be added, by priority</li>
<li>Who is responsible for each measure and by when</li>
<li>The resulting personal protective equipment and training needs</li>
</ul>
<div class="note">Law 5239/2025 explicitly added weight to psychosocial risks and to reasonable adjustments for employees with disabilities or chronic conditions (Article 533 of P.D. 62/2025). We cover both in the assessment.</div>
""", "Contents", "h-contents") + S("How we prepare it", """
<ol class="steps">
<li><strong>Data and drawings</strong>Floor plan, equipment list, organisation chart, previous assessment if there is one.</li>
<li><strong>Site survey</strong>We see each position during working hours and talk to the employees.</li>
<li><strong>Assessment</strong>We rate likelihood and severity for each hazard, with justification.</li>
<li><strong>Action plan</strong>Practical measures with cost and timetable, starting with those that reduce risk the most.</li>
<li><strong>Delivery and briefing</strong>A signed assessment and a short briefing for management and employees.</li>
</ol>
{AUTHOR}
""", "Method", "h-method"),
))

# ─────────────────────────────────────────────────────────────── P3 LABOUR INSPECTION READINESS
PAGES.append(dict(
    lang="en", path="/en/labour-inspection-readiness/", alt="/elegxos-epitheorisis-ergasias/",
    title="Labour Inspectorate Readiness in Greece (SEPE)",
    desc="What the Greek Labour Inspectorate checks on health and safety and how to prepare: mock inspection, document checklist and a plan of corrections.",
    crumb="Labour Inspectorate readiness", eyebrow="Service", service="Preparation for a Labour Inspectorate inspection",
    h1="Getting ready for <em>a Labour Inspectorate visit</em>",
    lead=("We carry out at your business the check a health and safety inspector would make, before the inspector comes. "
          "We review documents and premises, give you a written list of what is missing and help you close the gaps. "
          "It is useful before an expected inspection, after an accident, or when you change safety technician."),
    faq=[
        ("Is the Labour Inspectorate the old SEPE?",
         "Yes. The authority is now the independent Labour Inspectorate (Epitheorisi Ergasias), but many people still call it SEPE, and its information system is still referred to as OPS-SEPE."),
        ("What penalties apply?",
         "Sanctions depend on the breach and on the size of the business. For the most common breaches (personal protective equipment, unlicensed machinery operators, lifting equipment) the Labour Code provides administrative sanctions for directly provable breaches (Article 572 of P.D. 62/2025). We do not quote amounts without seeing the specific case."),
        ("Can you be present during the inspection?",
         "When we act as your safety technician, yes, provided we are told in time. We prepare with you the documents that will be requested."),
        ("Do you run mock inspections for businesses that already have a safety technician?",
         "Yes. A second look from outside often finds gaps that day-to-day work hides. We do not replace your current partner unless you want us to."),
    ],
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/health-safety-training/",
                "en/guides/workplace-accident-employer-steps/", "en/evacuation-plans/", "en/guides/safety-technician-hours/"),
    body=S("What a health and safety inspection usually covers", """
<p>Every inspection is different. On health and safety, the documents and points checked most often are these:</p>
<ul class="check-grid">
<li>Appointment of the safety technician (and occupational physician, where required) and its notification</li>
<li>Written occupational risk assessment, up to date for the current positions</li>
<li>Safety technician's recommendations book</li>
<li>Accident book and list of accidents with more than three working days of incapacity (Article 534(2))</li>
<li>Records of staff training and briefings</li>
<li>Personal protective equipment: selection, issue, use</li>
<li>Fire safety, escape routes, signage, first-aid equipment (Article 535)</li>
<li>CPR and Heimlich training, mandatory since 1 January 2026</li>
<li>Licences of machinery and lifting equipment operators, where relevant</li>
<li>Installations: electrical, racking, machinery, guards</li>
</ul>
<p class="src">Legal basis: P.D. 62/2025 (Greek Labour Code), as amended by Laws 5239/2025 and 5297/2026.</p>
""", "Checklist", "h-check") + S("What we do", """
<ol class="steps">
<li><strong>File review</strong>We go through every document in the order an inspector would ask for it.</li>
<li><strong>Site survey</strong>We check premises, equipment, signage, PPE and practices during working hours.</li>
<li><strong>Written report</strong>Each finding with a photo, legal basis and proposal, in order of priority.</li>
<li><strong>Closing the gaps</strong>We prepare what is missing (risk assessment, training, plans) and check again.</li>
</ol>
{AUTHOR}
""", "Service", "h-service"),
))

# ─────────────────────────────────────────────────────────────── P4 TRAINING
PAGES.append(dict(
    lang="en", path="/en/health-safety-training/", alt="/ekpaideuseis-ygeias-asfaleias/",
    title="Health and Safety Training for Employees in Greece",
    desc="On-site employee training in Athens: work at height, PPE, confined spaces, fire safety, evacuation, CPR. Delivered in English or Greek.",
    crumb="Health & safety training", eyebrow="Service", service="Health and safety training for employees",
    h1="Health and safety training <em>for your staff</em>",
    lead=("We train employees on your own premises, on your own equipment and on the hazards recorded in your risk "
          "assessment. Every session leaves an attendance record and material for the file. Training is delivered in "
          "English or Greek, and can be adapted for staff who do not speak Greek well."),
    faq=[
        ("Is CPR training mandatory?",
         "Since 1 January 2026 the employer must provide CPR and Heimlich manoeuvre training. With up to 50 employees on one site, this is done with the free training material of the Ministry of Labour; with more, through courses by certified first-aid providers for at least half the staff every three years (Article 535 of P.D. 62/2025)."),
        ("How long does a session last?",
         "From half an hour for a morning safety briefing to several hours for subjects such as work at height or confined spaces. The programme follows from the hazards of each position."),
        ("Can training be delivered in English?",
         "Yes. We deliver training in English for foreign companies and mixed teams."),
    ],
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/evacuation-plans/",
                "en/labour-inspection-readiness/", "en/accident-investigation/", "en/guides/workplace-accident-employer-steps/"),
    body=S("Training topics", """
<ul class="check-grid">
<li>Work at height, scaffolding, ladders, harnesses and fall arrest</li>
<li>Selection, use and care of personal protective equipment (PPE)</li>
<li>Work in confined spaces</li>
<li>Fire safety, use of extinguishers, building evacuation</li>
<li>First aid, CPR and the Heimlich manoeuvre</li>
<li>Manual handling and ergonomics</li>
<li>Safe use of machinery and tools</li>
<li>Induction of new employees</li>
<li>Morning toolbox talks on construction sites</li>
<li>Briefings on dangerous practices with real examples</li>
</ul>
<figure class="page-figure"><img src="{PRE}img/ekpaideusi-ergasia-se-ypsos.webp" alt="Work at height training on a construction site" width="619" height="1100" loading="lazy" decoding="async" style="max-height:520px;object-fit:cover"><figcaption>Work at height training, from our work in the field.</figcaption></figure>
""", "Programmes", "h-topics") + S("How it is organised", """
<p>Training is not a generic lecture. We start from the hazards recorded in the written occupational risk assessment and from what we see during visits. We use photos from your own premises, show the right way on the actual equipment and close with short questions.</p>
<p>For the company file we deliver a signed attendance sheet, the training material and a short certificate. For training that requires a certified provider (e.g. CPR on sites with more than 50 employees), we coordinate with the provider.</p>
{AUTHOR}
""", "Method", "h-how"),
))

# ─────────────────────────────────────────────────────────────── P5 EVACUATION PLANS
PAGES.append(dict(
    lang="en", path="/en/evacuation-plans/", alt="/schedia-diafygis-ekkenosis/",
    title="Escape and Evacuation Plans for Businesses in Greece",
    desc="Escape and evacuation plans: floor plans with routes, exits, extinguishers and assembly point, plus roles, procedures and evacuation drills.",
    crumb="Escape & evacuation plans", eyebrow="Service", service="Escape and evacuation plans",
    h1="Escape <em>and evacuation plans</em>",
    lead=("An escape plan shows at a glance where you are, how to get out and where to gather. We draw it on the real "
          "floor plan, place it at the right points and combine it with an evacuation procedure, roles and a drill "
          "for your staff."),
    faq=[
        ("Is an escape plan mandatory?",
         "The employer must take the measures needed for first aid, fire safety and evacuation, according to the size and nature of the business (Article 535 of P.D. 62/2025). In addition, fire safety rules require posted plans and an organised evacuation for many building uses. We check what applies to your premises during the site survey."),
        ("How often should an evacuation drill take place?",
         "We recommend at least one drill a year, and after changes to the premises or staff, unless the building use requires something stricter."),
    ],
    related=rel("en/health-safety-training/", "en/risk-assessment-greece/", "en/safety-technician-greece/",
                "en/labour-inspection-readiness/"),
    body=S("What is included", """
<ul class="check-grid">
<li>Survey of the premises or work on the existing floor plan</li>
<li>Escape routes, emergency exits and assembly point</li>
<li>Locations of extinguishers, first-aid kits, electrical panels and switches</li>
<li>A \"You are here\" plan for each posting point</li>
<li>Evacuation procedure and appointment of responsible persons</li>
<li>Staff training and an evacuation drill with a report</li>
</ul>
<figure class="page-figure"><img src="{PRE}img/schedio-diafygis-ekkenosis.webp" alt="Emergency exit sign" width="784" height="900" loading="lazy" decoding="async" style="max-height:420px;object-fit:cover"></figure>
{AUTHOR}
""", "Deliverables", "h-incl"),
))

# ─────────────────────────────────────────────────────────────── P6 ACCIDENT INVESTIGATION
PAGES.append(dict(
    lang="en", path="/en/accident-investigation/", alt="/diereynisi-ergatikou-atyximatos/",
    title="Workplace Accident Investigation in Greece",
    desc="Workplace accident investigation with site survey, interviews and root-cause analysis: accident report, corrective actions and an updated risk assessment.",
    crumb="Accident investigation", eyebrow="Service", service="Workplace accident investigation",
    h1="Workplace <em>accident investigation</em>",
    lead=("After an accident you need to understand what really happened, not only who got hurt. We survey the site, "
          "talk to those who were there, analyse the causes and give you a written report with measures, so it does "
          "not happen again. The investigation is handled discreetly."),
    faq=[
        ("How soon must a workplace accident be reported?",
         "Within 24 hours, to the Labour Inspectorate and e-EFKA. In case of serious injury or death, also to the police (Article 534(2) of P.D. 62/2025). See the <a href=\"{PRE}en/guides/workplace-accident-employer-steps/\">employer's first steps</a>."),
        ("What counts as a serious injury?",
         "Under the law, an injury is serious when it requires transfer to a healthcare facility and admission to hospital."),
        ("Do you investigate incidents without injury?",
         "Yes, and we recommend it. A near miss often shows the same problem as a serious accident, without the cost."),
    ],
    related=rel("en/guides/workplace-accident-employer-steps/", "en/risk-assessment-greece/", "en/safety-technician-greece/",
                "en/health-safety-training/", "en/labour-inspection-readiness/"),
    body=S("How the investigation works", """
<ol class="steps">
<li><strong>Immediate contact</strong>We tell you what to leave unchanged at the scene and which reports are due.</li>
<li><strong>Site survey</strong>Photos, measurements, checks of equipment and conditions as they were at the time.</li>
<li><strong>Interviews</strong>With the employee, the witnesses and the shift supervisor, separately and calmly.</li>
<li><strong>Root-cause analysis</strong>From the immediate cause we move to the deeper ones: organisation, training, equipment, time pressure.</li>
<li><strong>Report and measures</strong>Written report, corrective actions with owners and deadlines, entry in the accident book and an updated risk assessment.</li>
</ol>
<p>The law requires the employer to record the causes and description of every accident in a special book, and the measures taken in the recommendations book. Our report is written to cover both.</p>
{AUTHOR}
""", "Method", "h-method"),
))

# ─────────────────────────────────────────────────────────────── P8 CONSTRUCTION
PAGES.append(dict(
    lang="en", path="/en/construction-sites/", alt="/kataskeves-ergotaxia/",
    title="Health and Safety on Construction Sites in Greece",
    desc="Site safety technician, safety coordinator, safety and health plan and file, work at height training and inspections for construction companies in Attica.",
    crumb="Construction sites", eyebrow="Sector",
    h1="Health and safety <em>on construction sites</em>",
    lead=("Construction sites are where we started. We provide the safety technician and the safety coordinator, "
          "prepare the safety and health plan (SAY) and file (FAY), train crews in the field and check scaffolding, "
          "machinery and guards before a mistake happens."),
    faq=[
        ("Can the safety coordinator also be the safety technician?",
         "Yes, the coordinator can also be given the safety technician duties. Since 1 January 2026, however, the coordinator's time is not offset against the safety technician's time; it is calculated separately and the coordinator's minimum time is written explicitly in their contract (Article 6 of P.D. 305/1996, as amended by Law 5239/2025)."),
        ("What applies to construction machinery operators without a licence?",
         "The Labour Code expressly provides sanctions for an employer who assigns work to persons without the required licence (Article 572(6A) of P.D. 62/2025, added by Law 5297/2026). We check licences during our visits."),
    ],
    related=rel("en/safety-technician-greece/", "en/health-safety-training/", "en/accident-investigation/",
                "en/risk-assessment-greece/", "en/labour-inspection-readiness/", "en/guides/workplace-accident-employer-steps/"),
    body=S("The hazards we see most often", """
<ul>
<li>Falls from height: scaffolding without full guardrails, openings, roofs</li>
<li>Construction machinery and lifting equipment, with operators who do not always hold a licence</li>
<li>Excavations and slopes, live cables, falling objects</li>
<li>Several crews working at the same time without coordination</li>
</ul>
<figure class="page-figure"><img src="{PRE}img/miniaia-synantisi-ygeias-asfaleias.webp" alt="Monthly health and safety meeting with construction site workers" width="1100" height="821" loading="lazy" decoding="async"><figcaption>Monthly health and safety meeting on a construction site.</figcaption></figure>
""", "Hazards", "h-risks") + S("What we take on", """
<ul class="check-grid">
<li>Site safety technician</li>
<li>Health and safety coordinator during the works</li>
<li>Safety and health plan (SAY) and file (FAY)</li>
<li>Work at height training and morning briefings</li>
<li>Inspections of scaffolding, machinery and guards</li>
<li>Investigation of accidents and near misses</li>
</ul>
{AUTHOR}
""", "Services", "h-services"),
))

# ─────────────────────────────────────────────────────────────── P9 INDUSTRY
PAGES.append(dict(
    lang="en", path="/en/industry-logistics/", alt="/viomixania-logistics/",
    title="Health and Safety in Industry and Logistics, Greece",
    desc="Safety technician and risk assessment for factories, warehouses and logistics companies in Attica: forklifts, racking, machinery, shift work, training.",
    crumb="Industry & logistics", eyebrow="Sector",
    h1="Industry, warehouses <em>and logistics</em>",
    lead=("In a warehouse or a production plant, the hazards change with the shift, the volume and the staff. We work "
          "along the flow of the work: forklift and pedestrian traffic, racking, machinery, manual handling, and "
          "training that reaches the night shifts too."),
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/health-safety-training/",
                "en/labour-inspection-readiness/", "en/accident-investigation/", "en/guides/safety-technician-hours/"),
    body=S("What we look at in a warehouse or plant", """
<ul>
<li>Forklift and pedestrian traffic, aisles, markings, mirrors</li>
<li>Racking: loads, anchoring, protection, impact damage</li>
<li>Machinery: guards, emergency stops, lockout during maintenance</li>
<li>Manual handling and ergonomics at packing stations</li>
<li>Noise, dust, chemicals, heat stress in summer</li>
<li>Shift work, fatigue and psychosocial risks, which Law 5239/2025 explicitly requires to be taken into account</li>
</ul>
""", "Hazards", "h-risks") + S("How we help", """
<p>We act as safety technician with a visit schedule that covers all shifts, prepare the risk assessment per position and organise training for operators, warehouse staff and packing staff. On sites with more than 50 employees we also coordinate CPR training by a certified provider, as the law requires from 2026.</p>
{AUTHOR}
""", "Services", "h-help"),
))

# ─────────────────────────────────────────────────────────────── P10 SMALL BUSINESSES
PAGES.append(dict(
    lang="en", path="/en/small-businesses/", alt="/mikres-epixeiriseis/",
    title="Safety Technician for Shops, Restaurants and Offices",
    desc="Health and safety for small businesses in Attica: safety technician, written risk assessment and training for shops, restaurants and offices.",
    crumb="Small businesses", eyebrow="Sector",
    h1="Shops, restaurants <em>and offices</em>",
    lead=("Even with one employee, a business needs a safety technician and a written occupational risk assessment. "
          "For small businesses we keep things simple: a few targeted visits, a clean file ready for inspection and "
          "training that fits the shop's opening hours."),
    faq=[
        ("Can I act as safety technician myself?",
         "In category B and C businesses with up to 20 employees, the law allows it under conditions and with training, as applies from 1 January 2026. The written risk assessment, however, must be prepared by a person with safety technician qualifications. See the <a href=\"{PRE}en/guides/employer-as-safety-technician/\">detailed guide</a>."),
        ("What is needed for CPR training in a small shop?",
         "With up to 50 employees on one site, the training is done with the free training material of the Ministry of Labour. We make sure it is recorded properly in the file."),
    ],
    related=rel("en/safety-technician-greece/", "en/guides/employer-as-safety-technician/", "en/risk-assessment-greece/",
                "en/guides/safety-technician-hours/", "en/labour-inspection-readiness/", "en/evacuation-plans/"),
    body=S("Common hazards", """
<h3>Restaurants and cafes</h3>
<p>Burns and cuts in the kitchen, slips on wet floors, LPG and fryers, cold rooms, carrying heavy crates from the storeroom.</p>
<h3>Shops</h3>
<p>Ladders and high shelving, goods deliveries, electrical installations in old buildings, emergency exits blocked by boxes.</p>
<h3>Offices</h3>
<p>Ergonomics at screen workstations, lighting, ventilation, cables on the floor, fire safety in shared areas.</p>
""", "Hazards", "h-risks") + S("What you get", """
<ul class="check-grid">
<li>Safety technician appointment with the hours that apply</li>
<li>A risk assessment written for your own premises</li>
<li>A file ready for a Labour Inspectorate inspection</li>
<li>Staff training and CPR with the Ministry's material</li>
<li>Checks of fire safety and emergency exits</li>
<li>Phone support when something comes up</li>
</ul>
{AUTHOR}
""", "Services", "h-give"),
))

# ─────────────────────────────────────────────────────────────── FOREIGN COMPANIES (English only)
PAGES.append(dict(
    lang="en", path="/en/foreign-companies-greece/", alt=None,
    title="Health & Safety for Foreign Companies in Greece",
    desc="Plain-English guide to health and safety duties for foreign companies with staff in Greece: safety technician, risk assessment, accident reporting.",
    crumb="Foreign companies in Greece", eyebrow="Sector",
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
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/labour-inspection-readiness/",
                "en/health-safety-training/", "en/guides/safety-technician-hours/", "en/team/"),
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

# ─────────────────────────────────────────────────────────────── TEAM
PAGES.append(dict(
    lang="en", path="/en/team/", alt="/omada/", people=True, page_type="AboutPage", author=False,
    title="Our Team | Malliaris & Partners",
    desc="Meet the engineers of Malliaris & Partners: Stavros Malliaris (ASP®), Dimitrios Moudiotis, Vaios Liapis and Eleftherios Adam.",
    crumb="Team", eyebrow="About us",
    h1="The team at <em>Malliaris &amp; Partners</em>",
    lead=("We are engineers with experience on construction sites, in industry and in services, in Greece and abroad. "
          "The company was founded in March 2026 and is based in Alimos, Athens, to give businesses real safety through "
          "practical solutions and clear communication."),
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/health-safety-training/"),
    body=S("People", """
<div class="team-grid">
  <article class="team-card"><img src="{PRE}img/stavros-malliaris.webp" alt="Stavros Malliaris" width="591" height="588" loading="lazy" decoding="async">
    <div><div class="tc-role">Founder &amp; lead engineer</div><h3>Stavros Malliaris</h3>
    <p>Civil Engineer (Aristotle University of Thessaloniki) specialising in occupational health and safety (MEng). Over ten years of experience on construction sites, industrial facilities and all types of businesses in Greece and abroad. ASP® certified by the Board of Certified Safety Professionals (BCSP) and internal auditor for ISO 9001, 14001 and 45001.</p></div></article>
  <article class="team-card"><img src="{PRE}img/dimitrios-moudiotis.webp" alt="Dimitrios Moudiotis" width="400" height="400" loading="lazy" decoding="async">
    <div><div class="tc-role">Mechanical engineering lead</div><h3>Dimitrios Moudiotis</h3>
    <p>Mechanical Engineer (AUTh). Covers mechanical matters: machinery, work equipment, lifting equipment and vehicles. <a href="https://www.moudiotis.gr/" target="_blank" rel="noopener">moudiotis.gr</a></p></div></article>
  <article class="team-card"><img src="{PRE}img/vaios-liapis.webp" alt="Vaios Liapis" width="347" height="400" loading="lazy" decoding="async">
    <div><div class="tc-role">Engineering studies lead</div><h3>Vaios Liapis</h3>
    <p>Civil Engineer (AUTh). Responsible for studies and drawings: floor plans, escape plans, technical studies. <a href="https://www.vaiosliapis.gr/" target="_blank" rel="noopener">vaiosliapis.gr</a></p></div></article>
  <article class="team-card"><img src="{PRE}img/eleftherios-adam.webp" alt="Eleftherios Adam" width="400" height="400" loading="lazy" decoding="async">
    <div><div class="tc-role">HSE officer</div><h3>Eleftherios Adam</h3>
    <p>BSc Materials Science, University of Patras. Supports the team in the field, in inspections and in training.</p></div></article>
</div>
""", "Team", "h-people") + S("How we work", """
<p>Three words describe us: <strong>honesty, method, technical knowledge</strong>. We say clearly what is needed and what is not, give priority to the measures that really reduce risk and respect the company's budget.</p>
<p>Every client has one contact person from the team who knows the premises and the staff. Where specialist knowledge is needed (mechanical, structural, drawings), the relevant engineer joins the work.</p>
<p class="src">Malliaris &amp; Partners · Dodekanisou 16, 174 56 Alimos, Athens · +30 211 0040 193</p>
""", "Approach", "h-how"),
))

# ─────────────────────────────────────────────────────────────── GUIDES — hub
PAGES.append(dict(
    lang="en", path="/en/guides/", alt="/odigoi/", page_type="CollectionPage", author=False, ctas=False,
    title="Health and Safety Guides for Employers in Greece",
    desc="Practical guides for employers in Greece: safety technician hours, the employer as safety technician, what to do after a workplace accident.",
    crumb="Guides", eyebrow="Guides",
    h1="Guides <em>for employers</em>",
    lead=("Short, practical guides to the questions businesses ask us most often. Each guide cites the legal basis by "
          "article number and is updated when the law changes."),
    body=S("All guides", """
<div class="related-grid">
  <a class="resource-card" href="{PRE}en/guides/safety-technician-hours/"><div class="resource-icon"><i class="fa-solid fa-calculator" aria-hidden="true"></i></div><h3>Safety technician hours calculator</h3><p>How many hours a year apply to your business, by category and headcount.</p></a>
  <a class="resource-card" href="{PRE}en/guides/employer-as-safety-technician/"><div class="resource-icon"><i class="fa-solid fa-user-tie" aria-hidden="true"></i></div><h3>The employer as safety technician</h3><p>What changed on 1 January 2026 and when it is allowed.</p></a>
  <a class="resource-card" href="{PRE}en/guides/workplace-accident-employer-steps/"><div class="resource-icon"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i></div><h3>Workplace accident: first steps</h3><p>Reporting within 24 hours, evidence, accident book.</p></a>
  <a class="resource-card" href="{PRE}en/labour-inspection-readiness/"><div class="resource-icon"><i class="fa-solid fa-clipboard-check" aria-hidden="true"></i></div><h3>What the Labour Inspectorate checks</h3><p>Documents and points for a health and safety inspection.</p></a>
  <a class="resource-card" href="{PRE}en/foreign-companies-greece/"><div class="resource-icon"><i class="fa-solid fa-earth-europe" aria-hidden="true"></i></div><h3>Health &amp; safety for foreign companies</h3><p>Your obligations in Greece, in plain English.</p></a>
  <a class="resource-card" href="{PRE}en/#resources"><div class="resource-icon"><i class="fa-solid fa-book" aria-hidden="true"></i></div><h3>Official resources</h3><p>ELINYAE, Labour Inspectorate, EU-OSHA, e-EFKA.</p></a>
</div>
""", "Guides", "h-guides"),
))

# ─────────────────────────────────────────────────────────────── G1 HOURS CALCULATOR
CALC = """
<form class="calc" id="taCalc" onsubmit="return false" aria-label="Safety technician hours calculator">
  <div class="calc-row">
    <div><label for="calcCat">Risk category</label>
      <select id="calcCat"><option value="A">A: high</option><option value="B" selected>B: medium</option><option value="C">C: low</option></select></div>
    <div><label for="calcEmp">Number of employees</label>
      <input id="calcEmp" type="number" min="1" max="100000" value="10" inputmode="numeric"></div>
  </div>
  <div class="calc-out" aria-live="polite">
    <div class="calc-box"><div class="cb-label">Safety technician</div><div class="cb-num" id="calcTA">—</div><div class="cb-sub" id="calcTAsub"></div></div>
    <div class="calc-box"><div class="cb-label">Occupational physician</div><div class="cb-num" id="calcIE">—</div><div class="cb-sub" id="calcIEsub"></div></div>
  </div>
  <p class="calc-note">Indicative calculation for a single site. The exact category follows from the activity code of the business (Article 500 of P.D. 62/2025), and special cases may change the result.</p>
</form>
"""
PAGES.append(dict(
    lang="en", path="/en/guides/safety-technician-hours/", alt="/odigoi/ores-texnikou-asfaleias/", page_type="WebPage",
    title="Safety Technician Hours in Greece: Calculator",
    desc="Estimate the yearly hours of the safety technician and occupational physician for category A, B and C businesses in Greece.",
    crumbs=[("Guides", "/en/guides/")], crumb="Safety technician hours", eyebrow="Guide · Tool", ctas=False,
    h1="Safety technician hours: <em>calculator</em>",
    lead=("The minimum yearly time of the safety technician follows from the risk category and the number of employees: "
          "multiply the employees by the category's coefficient, subject to a minimum number of hours. "
          "Enter your figures for a first estimate."),
    scripts=["ores-calc.js"],
    faq=[
        ("Which category is my business?",
         "Category A, B or C follows from the activity code (KAD), using the table of Article 500 of P.D. 62/2025, as replaced by Law 5239/2025. Because the table changed, we check it with every offer."),
        ("Do the hours apply to each site separately?",
         "The calculation is made for the business and allocated to its sites according to the staff and hazards of each one. For several sites, ask us for a detailed calculation."),
        ("When do I also need an occupational physician?",
         "As a rule, from 50 employees upwards. Below that it may be required in special cases. This is why the calculator shows physician hours only from 50 employees."),
    ],
    related=rel("en/safety-technician-greece/", "en/guides/employer-as-safety-technician/", "en/small-businesses/"),
    body=S("Calculate the hours", CALC + """
<p>The calculation uses the coefficients of Article 21 of Law 3850/2010, as in force after codification in the Greek Labour Code (P.D. 62/2025):</p>
<div class="table-wrap"><table class="data-table">
<caption>Hours per employee per year</caption>
<thead><tr><th>Category</th><th>Employees</th><th>Safety technician</th><th>Occupational physician</th></tr></thead>
<tbody>
<tr><td>A</td><td>up to 500</td><td>3.5</td><td>0.8</td></tr>
<tr><td>A</td><td>501–1,000</td><td>3.0</td><td>0.8</td></tr>
<tr><td>A</td><td>1,001–5,000</td><td>2.5</td><td>0.8</td></tr>
<tr><td>A</td><td>over 5,000</td><td>2.0</td><td>0.8</td></tr>
<tr><td>B</td><td>up to 1,000</td><td>2.5</td><td>0.6</td></tr>
<tr><td>B</td><td>1,001–5,000</td><td>1.5</td><td>0.6</td></tr>
<tr><td>B</td><td>over 5,000</td><td>1.0</td><td>0.6</td></tr>
<tr><td>C</td><td>all</td><td>0.4</td><td>0.4</td></tr>
</tbody></table></div>
<p>The time cannot fall below a yearly minimum: <strong>25 hours</strong> for up to 20 employees, <strong>50 hours</strong> for 21–50 and <strong>75 hours</strong> for more than 50.</p>
<div class="note">Example: a category B business with 30 employees → 30 × 2.5 = 75 hours a year for the safety technician (above the minimum of 50).</div>
<p>The hours and their monthly allocation are recorded in the staff details, and any change is notified to the Labour Inspectorate.</p>
{AUTHOR}
""", "Tool", "h-calc"),
))

# ─────────────────────────────────────────────────────────────── G2 EMPLOYER AS SAFETY TECHNICIAN
PAGES.append(dict(
    lang="en", path="/en/guides/employer-as-safety-technician/", alt="/odigoi/ergodotis-texnikos-asfaleias/", page_type="WebPage",
    title="Employer as Safety Technician in Greece: 2026 Rules",
    desc="When can the employer or an employee take on safety technician duties after Law 5239/2025: headcount limits, categories, training.",
    crumbs=[("Guides", "/en/guides/")], crumb="Employer as safety technician", eyebrow="Guide", ctas=True,
    h1="Can the employer <em>be the safety technician?</em>",
    lead=("In small category B and C businesses, yes, under conditions. Since 1 January 2026 the limit has dropped to 20 "
          "employees (from fewer than 50) and training is required. In category A the business needs a safety technician "
          "with full qualifications, and the risk assessment is always written by a qualified person."),
    faq=[
        ("I have 25 employees in category C. Can I carry on by myself?",
         "Not after 1 January 2026. The limit for the employer or an employee to take on the duties is now up to 20 employees. You need to appoint a safety technician with the qualifications set by law."),
        ("Is the training enough for me to write the risk assessment too?",
         "No. The written risk assessment is prepared by a person with safety technician qualifications and the right specialisation for the activity."),
    ],
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/guides/safety-technician-hours/"),
    body=S("What applies from 1 January 2026", """
<p>Law 5239/2025 amended Article 502 of the Greek Labour Code (formerly Article 12 of Law 3850/2010). The changes apply from 1 January 2026:</p>
<div class="table-wrap"><table class="data-table">
<thead><tr><th>Category</th><th>Employees</th><th>Who may carry out the safety technician duties</th></tr></thead>
<tbody>
<tr><td>A</td><td>up to 50</td><td>A safety technician with the qualifications set by law (Article 501)</td></tr>
<tr><td>B</td><td>up to 20</td><td>A qualified safety technician, or a full-time employee with training; the employer personally only up to 5 employees, with specific formal qualifications or ten years in the activity, plus training</td></tr>
<tr><td>C</td><td>up to 20</td><td>A safety technician, or the employer or an employee after training</td></tr>
<tr><td>B / C</td><td>over 20</td><td>A safety technician with the qualifications set by law</td></tr>
</tbody></table></div>
<p class="src">Legal basis: Article 502 of P.D. 62/2025, as amended by Article 30 of Law 5239/2025 (Government Gazette A' 178/2025). The table is simplified; the exact conditions are examined case by case.</p>
""", "Changes", "h-rules") + S("What it means in practice", """
<p>Many employers with 21 to 49 employees who had taken on the duties themselves until 2025 must now appoint a safety technician. If this is your case, it is worth sorting out before an inspection.</p>
<p>Even where the employer may take on the role, two things remain: the written occupational risk assessment must be prepared by a qualified person, and the employer carries full responsibility for applying the measures. That is exactly where we can help without taking on the whole contract.</p>
{AUTHOR}
""", "In practice", "h-practice"),
))

# ─────────────────────────────────────────────────────────────── G4 WORKPLACE ACCIDENT
PAGES.append(dict(
    lang="en", path="/en/guides/workplace-accident-employer-steps/", alt="/odigoi/ergatiko-atyxima-ti-kanei-o-ergodotis/",
    title="Workplace Accident in Greece: Employer Steps in 24h",
    desc="Workplace accident in Greece: report within 24 hours to the Labour Inspectorate and e-EFKA, when to inform the police, accident book and investigation.",
    crumbs=[("Guides", "/en/guides/")], crumb="Workplace accident", eyebrow="Guide", ctas=True,
    h1="Workplace accident: <em>what the employer does</em>",
    lead=("First, care for the injured person. Then, within 24 hours, report to the Labour Inspectorate and e-EFKA, and "
          "in case of serious injury or death to the police as well. Meanwhile, the evidence at the scene stays as it was, "
          "so the causes can be found."),
    faq=[
        ("Where is the accident reported?",
         "To the competent services of the Labour Inspectorate and e-EFKA. The official procedure is described on <a href=\"" + GOV_ACC + "\" target=\"_blank\" rel=\"noopener\">gov.gr</a> (in Greek)."),
        ("What about occupational diseases?",
         "The employer reports a work-related disease to the Labour Inspectorate and e-EFKA within 5 days of being informed by the occupational physician or of a diagnosis by a public health system doctor."),
    ],
    related=rel("en/accident-investigation/", "en/safety-technician-greece/", "en/labour-inspection-readiness/"),
    body=S("Step by step", """
<ol class="steps">
<li><strong>Care and safety</strong>First aid, call the ambulance (166 or 112) and move others away from the danger.</li>
<li><strong>Preserve the evidence</strong>The employer must keep unchanged everything that can help establish the causes. Take photos before anything changes.</li>
<li><strong>Report within 24 hours</strong>To the Labour Inspectorate and e-EFKA for every workplace accident. For serious injury (transfer and hospital admission) or death, also to the nearest police authority.</li>
<li><strong>Record it</strong>Causes and description in the accident book; accidents with more than three working days of incapacity in the relevant list.</li>
<li><strong>Investigate and act</strong>The measures to prevent a repeat are recorded in the recommendations book, and the risk assessment is updated.</li>
</ol>
<p class="src">Legal basis: Article 534(2) of P.D. 62/2025 (formerly Article 43 of Law 3850/2010), as amended by Article 38 of Law 5239/2025.</p>
<div class="facts"><strong>Need help now?</strong> Call us on <a href="tel:+302110040193">+30 211 0040 193</a>. If we act as your safety technician, we come for a site survey and investigation.</div>
{AUTHOR}
""", "Steps", "h-steps"),
))

# ─────────────────────────────────────────────────────────────── PRIVACY
PAGES.append(dict(
    lang="en", path="/en/privacy/", alt="/aporrito/", author=False, ctas=False, noindex=True,
    title="Privacy and Cookie Policy | Malliaris & Partners",
    desc="How Malliaris & Partners uses the details you send through the contact form, and how Google Analytics cookies work on this website.",
    crumb="Privacy policy", eyebrow="Information",
    h1="Privacy <em>and cookies</em>",
    lead="This page explains what data the website collects, why, and how you can exercise your rights.",
    body=S("Controller", """
<p>The controller is Malliaris &amp; Partners, Dodekanisou 16, 174 56 Alimos, Greece, tel. +30 211 0040 193, email <a href="mailto:info@malliarisandpartners.gr">info@malliarisandpartners.gr</a>.</p>
""", "", "h-ctrl") + S("Contact form", """
<p>When you use the contact form we receive your name, email, phone (if given), subject and message. We use them only to reply and to prepare an offer. The form is sent through a Google service (Apps Script) to our mailbox.</p>
<p>We keep the correspondence as long as needed for your request and any resulting cooperation, and delete it when no longer needed or when you ask us to.</p>
""", "", "h-form") + S("Cookies and Google Analytics", """
<p>Google Analytics 4 runs only if you click “Accept” in the cookie banner; without consent the script is not loaded at all. We measure, anonymously, which pages are read and whether the contact buttons are used, so we can improve the website. We do not use advertising cookies.</p>
<p>You can change your choice at any time via <a href="#" data-cc-open>Cookie settings</a>.</p>
<p>The map on the contact section and the web fonts are loaded from Google services, which may log your IP address under their own policies.</p>
""", "", "h-cookies") + S("Your rights", """
<p>You have the right of access, rectification, erasure, restriction, portability and objection. Write to <a href="mailto:info@malliarisandpartners.gr">info@malliarisandpartners.gr</a>. If you believe we have not complied with the law, you may lodge a complaint with the Hellenic Data Protection Authority (<a href="https://www.dpa.gr/" target="_blank" rel="noopener">dpa.gr</a>).</p>
<p class="src">Last updated: 25 September 2026</p>
""", "", "h-rights"),
))
