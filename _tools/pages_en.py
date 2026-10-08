# -*- coding: utf-8 -*-
"""Content of inner pages - ENGLISH. One English page for every Greek page (same legal basis as pages_el.py).
Rule: no Greek characters on English pages (transliterate: GEEK, SEPE, e-EFKA, KAD).
"""
from pages_el import S, HLI_TA, HLI_GEEK, GOV_ACC, OIRA

LAW = "Law 3850/2010, now codified in the Greek Labour Code (Presidential Decree 62/2025)"

REL = [
    ("en/safety-technician-greece/", "fa-file-shield", "Safety technician", "Appointment, site visits, written recommendations."),
    ("en/risk-assessment-greece/", "fa-file-lines", "Written risk assessment (GEEK)", "Hazards per job position and prevention measures."),
    ("en/labour-inspection-readiness/", "fa-clipboard-check", "Labour Inspectorate readiness", "Mock inspection and a list of fixes."),
    ("en/health-safety-training/", "fa-person-chalkboard", "Health & safety training", "Work at height, PPE, fire safety, CPR."),
    ("en/evacuation-plans/", "fa-compass-drafting", "Engineering Studies", "Fire protection, escape plans, SAY-FAY, H&S plans."),
    ("en/safety-coordinator/", "fa-helmet-safety", "Safety coordinator", "Coordinating contractors and the H&S plan on site."),
    ("en/guides/safety-technician-hours/", "fa-calculator", "Hours calculator", "Indicative yearly safety technician hours."),
    ("en/guides/employer-as-safety-technician/", "fa-user-tie", "Employer as safety technician", "When it is allowed after 1 January 2026."),
    ("en/guides/workplace-accident-employer-steps/", "fa-triangle-exclamation", "Workplace accident", "The employer's first steps."),
    ("en/foreign-companies-greece/", "fa-earth-europe", "Foreign companies in Greece", "Your health and safety obligations, in plain English."),
    ("en/shops-restaurants-tourism/", "fa-store", "Shops, restaurants, tourism", "Discreet, targeted visits and a clean file."),
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
                "en/labour-inspection-readiness/", "en/health-safety-training/", "en/safety-coordinator/"),
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
<li>Reminders of employer duties, e.g. reporting accidents within 24 hours and CPR training</li>
<li>Written recommendations in the Safety Technician's Recommendations Book, after each visit</li>
<li>Regular briefing of staff on occupational health and safety matters</li>
<li>Scheduled visits to your premises, based on the hours your category requires</li>
<li>Coordination with the occupational physician, where required</li>
<li>Updating the Accident Book (if needed)</li>
<li>Investigation of workplace accidents (if needed)</li>
</ul>
""", "Scope", "h-incl") + S("How we start", """
<ol class="steps">
<li><strong>Short call</strong>You tell us your activity, activity code, headcount and premises. Ten minutes on the phone is enough.</li>
<li><strong>Category, hours, offer</strong>We check your classification, calculate the hours and send a written offer.</li>
<li><strong>Appointment</strong>The appointment is made and notified, so the business is formally covered.</li>
<li><strong>First site survey</strong>We walk the premises, review the existing file and note what is missing.</li>
<li><strong>Regular visits</strong>Recommendations, briefings and follow-up of corrections, with the same person on our side.</li>
</ol>
{AUTHOR}
""", "Process", "h-steps") + S("Sectors we work in", """
<p>We work with energy projects, industry and warehouses, construction sites, offices, shops, restaurants and tourism, and foreign companies with staff in Greece. For what each type of workplace needs:</p>
<ul>
<li><a href="{PRE}en/energy-environment/">Energy and environment</a>: electrical hazards, work at height, confined spaces</li>
<li><a href="{PRE}en/industry-logistics/">Industry, warehouses and logistics</a>: forklifts, racking, shift work</li>
<li><a href="{PRE}en/construction-sites/">Construction sites</a>: work at height, scaffolding, construction machinery, safety plans</li>
<li><a href="{PRE}en/offices-services/">Offices and services</a>: ergonomics, fire safety, staff training</li>
<li><a href="{PRE}en/shops-restaurants-tourism/">Shops, restaurants, tourism</a></li>
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
        ("What is a GEEK (or MEEK)?",
         "\"Written occupational risk assessment\" (GEEK) or \"occupational risk assessment study\" (MEEK) often refer to the same document. What matters is the content: hazards per position, assessment, measures, owners and personal protective equipment."),
        ("Can we reuse our group's risk assessment?",
         "It is a useful starting point, but the Greek assessment has to reflect the local premises, positions and legal requirements, and be available in Greek."),
        ("How much does it cost?",
         "It depends on the job positions, the premises and the level of risk. After a short call we send you a written offer."),
    ],
    related=rel("en/safety-technician-greece/", "en/labour-inspection-readiness/", "en/health-safety-training/",
                "en/safety-coordinator/", "en/evacuation-plans/", "en/guides/employer-as-safety-technician/"),
    body=S("What it is and who needs it", f"""
<p>The employer must have a written assessment of the risks to employees' safety and health, together with the prevention measures that follow from it (Article 534 of P.D. 62/2025, formerly Article 43 of Law 3850/2010). The duty does not depend on size: it applies to a business with a single employee.</p>
<p>In practice the risk assessment is the reference point for everything else: which training is needed, which personal protective equipment, what changes on the premises and in what order.</p>
<p class="src">Sources: <a href="{HLI_GEEK}" target="_blank" rel="noopener">Labour Inspectorate: written risk assessment (in Greek)</a> · <a href="https://oira.osha.europa.eu/en/what-is-risk-assessment" target="_blank" rel="noopener">OiRA (EU-OSHA)</a></p>
""", "Definition", "h-what") + S("What a proper assessment contains", """
<ul>
<li>A description of the business, the premises and the equipment</li>
<li>Each job position, one by one</li>
<li>The hazards of each position (mechanical, electrical, chemical, ergonomic, fire, psychosocial, etc.)</li>
<li>The assessment of likelihood, severity and risk level</li>
<li>The appropriate measures to prevent the risks</li>
<li>Who is responsible for each measure and by when (if not already clear)</li>
<li>The resulting personal protective equipment and training needs (where they go beyond the standard ones)</li>
</ul>
<div class="note">Law 5239/2025 explicitly added weight to psychosocial risks and to reasonable adjustments for employees with disabilities or chronic conditions (Article 533 of P.D. 62/2025). We cover both in the assessment.</div>
""", "Contents", "h-contents") + S("How we prepare it", """
<ol class="steps">
<li><strong>Data and drawings</strong>Floor plan, equipment list, organisation chart, previous assessment if there is one.</li>
<li><strong>Site survey</strong>We see each position during working hours and talk to the employees.</li>
<li><strong>Assessment</strong>We rate likelihood and severity for each hazard, with justification.</li>
<li><strong>Action plan</strong>Appropriate risk prevention measures, starting with those that reduce risk the most.</li>
<li><strong>Delivery and briefing</strong>A signed assessment, in PDF format, for the management to be informed.</li>
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
         "When we act as your safety technician, we do everything we can to be present at the inspection, provided we are told in time. We also help you organise the documents that will be requested."),
        ("Do you run mock inspections for businesses that already have a safety technician?",
         "Yes. A second look from outside often finds gaps that day-to-day work hides. We do not replace your current partner unless you want us to."),
    ],
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/health-safety-training/",
                "en/guides/workplace-accident-employer-steps/", "en/evacuation-plans/", "en/guides/safety-technician-hours/"),
    body=S("What a health and safety inspection usually covers", """
<p>Every inspection is different. On health and safety, the documents and points checked most often are these:</p>
<ul class="check-grid">
<li>Appointment of the safety technician (and occupational physician, where required) and its notification</li>
<li>Accident book and list of accidents with more than three working days of incapacity (Article 534(2))</li>
<li>Safety technician's recommendations book, with numbered and stamped pages</li>
<li>Written occupational risk assessment, up to date for the current positions</li>
<li>Records of staff training and briefings</li>
<li>Personal protective equipment: selection, issue, use and maintenance</li>
<li>Fire safety, escape routes, signage, first-aid equipment (Article 535)</li>
<li>CPR and Heimlich training, mandatory since 1 January 2026</li>
<li>Licences of machinery and lifting equipment operators, where relevant</li>
<li>Installations: electrical, plumbing, machinery, hazard signage</li>
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
          "assessment. Every session leaves an attendance record for the file. Training is delivered in "
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
                "en/labour-inspection-readiness/", "en/safety-coordinator/", "en/guides/workplace-accident-employer-steps/"),
    body=S("Training topics", """
<ul class="check-grid">
<li>Work at height, scaffolding, ladders, using a fall arrest harness or other equipment</li>
<li>Selection, use and care of personal protective equipment (PPE)</li>
<li>First aid, CPR and the Heimlich manoeuvre, using the Ministry of Labour material</li>
<li>Fire safety, use of extinguishers, building evacuation</li>
<li>Work in confined spaces</li>
<li>Manual handling and ergonomics</li>
<li>Safe use of machinery and tools</li>
<li>Induction of new employees</li>
<li>Morning toolbox talks on construction sites</li>
<li>Briefings on dangerous practices with real examples</li>
</ul>
""", "Programmes", "h-topics") + S("How it is organised", """
<p>Training is not a generic lecture. We start from the hazards recorded in the written occupational risk assessment and from what we see during visits. We use photos from your own premises, show the right way to use the equipment and close with short questions.</p>
<p>For the company file we deliver a signed attendance sheet. For training that requires a certified provider (e.g. CPR on sites with more than 50 employees), we coordinate with the provider.</p>
{AUTHOR}
""", "Method", "h-how"),
))

# ─────────────────────────────────────────────────────────────── P5 STUDIES
PAGES.append(dict(
    lang="en", path="/en/evacuation-plans/", alt="/schedia-diafygis-ekkenosis/",
    title="Fire Protection Studies, Escape Plans, SAY-FAY and H&S Plans in Greece",
    desc="Fire protection studies, escape and evacuation plans, Health and Safety Plan and File (SAY-FAY) and subcontractor H&S Plans, by engineers from Aristotle University.",
    crumb="Engineering Studies", eyebrow="Service", service="Fire protection studies, escape plans, SAY-FAY and H&S plans",
    h1="Fire protection <em>and safety studies</em>",
    lead=("We prepare the studies required by the Fire Service, labour legislation and main contractors: fire protection "
          "studies, escape and evacuation plans, SAY-FAY for construction projects and H&amp;S Plans for subcontractors. "
          "Every study is based on a survey of the actual premises or site and is delivered ready to submit or post."),
    faq=[
        ("Is an escape plan mandatory?",
         "The employer must take the measures needed for first aid, fire safety and evacuation, according to the size and nature of the business (Article 535 of P.D. 62/2025). In addition, fire safety rules require posted plans and an organised evacuation for many building uses. We check what applies to your premises during the site survey."),
        ("When is a fire protection study needed?",
         "It depends on the use, floor area and occupancy of the premises. For many businesses the study is a prerequisite for the Fire Safety Certificate or the operating licence. We check what applies to your premises during the site survey."),
        ("When is a SAY-FAY needed?",
         "The Health and Safety Plan (SAY) and Health and Safety File (FAY) are required for construction projects under P.D. 305/1996 and usually accompany the building permit application. The SAY is updated as construction progresses and the FAY is handed to the project owner at the end."),
        ("What is a subcontractor H&S Plan?",
         "It is the document in which a subcontractor shows the main contractor how it will carry out its scope of work safely: hazards, work methods, equipment, staff and emergency procedures. Large contractors usually ask for it before site access."),
        ("How often should an evacuation drill take place?",
         "We recommend at least one drill a year, and after changes to the premises or staff, unless the building use requires something stricter."),
    ],
    related=rel("en/health-safety-training/", "en/risk-assessment-greece/", "en/safety-technician-greece/",
                "en/labour-inspection-readiness/"),
    body=S("Studies we prepare", """
<h3>Fire protection study</h3>
<ul class="check-grid">
<li>Classification of the building use and the requirements that apply to your premises</li>
<li>Active and passive fire protection measures</li>
<li>Floor plans with firefighting, detection and alarm equipment</li>
<li>File for the Fire Safety Certificate</li>
</ul>
<h3>Escape and evacuation plans</h3>
<ul class="check-grid">
<li>Survey of the premises or work on the existing floor plan</li>
<li>Escape routes, emergency exits and assembly point</li>
<li>Locations of extinguishers, first-aid kits, electrical panels and switches</li>
<li>A \"You are here\" plan for each posting point</li>
<li>Evacuation procedure and appointment of responsible persons</li>
<li>Staff training and an evacuation drill with a report</li>
</ul>
<h3>Health and Safety Plan and File (SAY-FAY)</h3>
<ul class="check-grid">
<li>Health and Safety Plan (SAY) for every phase of the project</li>
<li>Health and Safety File (FAY) for future maintenance work</li>
<li>Work schedule and risk assessment per phase</li>
<li>Updates to the SAY-FAY as the project progresses</li>
</ul>
<h3>Subcontractor H&amp;S Plans</h3>
<ul class="check-grid">
<li>Health &amp; Safety Plan for the subcontractor's scope of work</li>
<li>Method statements and risk assessments (RAMS)</li>
<li>Equipment, certificates and staff qualifications</li>
<li>Written in English or Greek, in the main contractor's template</li>
</ul>
<figure class="page-figure"><img src="{PRE}img/schedio-diafygis-ekkenosis.webp" alt="Emergency exit sign" width="784" height="900" loading="lazy" decoding="async" style="max-height:420px;object-fit:cover"></figure>
{AUTHOR}
""", "Deliverables", "h-incl"),
))

# ─────────────────────────────────────────────────────────────── P6 SAFETY COORDINATOR
PAGES.append(dict(
    lang="en", path="/en/safety-coordinator/", alt="/syntonistis-asfaleias/",
    title="Health and Safety Coordinator for Construction in Greece",
    desc="Health and safety coordinator for construction projects in Athens and Attica: contractor coordination, H&S plan and file (SAY-FAY), site checks under P.D. 305/1996.",
    crumb="Safety coordinator", eyebrow="Service", service="Health and safety coordinator for construction projects",
    h1="Health and safety <em>coordinator</em> for construction projects",
    lead=("When more than one contractor or subcontractor works on a site, the client must appoint a health and safety "
          "coordinator. We take on the role from design to handover: we coordinate the trades, keep the H&amp;S plan "
          "and file (SAY-FAY) up to date and check on site that the measures are applied."),
    faq=[
        ("When is a safety coordinator required?",
         "Under P.D. 305/1996, when more than one company will work on the site, e.g. a main contractor with subcontractors "
         "or self-employed tradespeople. The client appoints the coordinator for the design stage and for the construction stage."),
        ("How is this different from a safety technician?",
         "The <a href=\"{PRE}en/safety-technician-greece/\">safety technician</a> advises each employer about its own staff. "
         "The coordinator looks at the project as a whole: how all the trades work together, in what order and with which shared measures. "
         "Many projects need both roles."),
        ("Does appointing a coordinator relieve the client of responsibility?",
         "No. Appointing a coordinator does not relieve the client or the employers of their duties. "
         "It helps them meet those duties in an organised and safe way."),
        ("Is a prior notice to the Labour Inspectorate needed?",
         "Yes, when the work lasts more than 30 working days and has more than 20 workers on site at the same time, "
         "or when the total volume exceeds 500 person-days. The notice also names the project's coordinators."),
        ("Do you also prepare the SAY-FAY?",
         "Yes. The health and safety plan (SAY) and file (FAY) are part of the coordinator's duties at the design stage. "
         "See also our <a href=\"{PRE}en/evacuation-plans/\">engineering studies</a>."),
        ("When must the coordinator be on site full time?",
         "Since 1 January 2026, under Law 5239/2025, the coordinator must be present for the whole duration of the works on public works "
         "that require a class 4 or higher contractor, and on special (mainly non-residential) buildings with a footprint of 4,000 m² or more. "
         "On all other projects the coordinator must be present at least at the start of each critical phase."),
    ],
    related=rel("en/evacuation-plans/", "en/safety-technician-greece/", "en/risk-assessment-greece/",
                "en/health-safety-training/", "en/labour-inspection-readiness/"),
    body=S("What the coordinator does", """
<h3>At the design stage</h3>
<ul class="check-grid">
<li>Applying the general principles of prevention to architectural, technical and organisational choices</li>
<li>Preparing the health and safety plan (SAY)</li>
<li>Preparing the health and safety file (FAY) for future work on the building</li>
<li>Estimating the duration of each phase and the work done at the same time</li>
</ul>
<h3>At the construction stage</h3>
<ul class="check-grid">
<li>Coordinating contractors, subcontractors and self-employed workers on site</li>
<li>Checking that the SAY and the work procedures are applied</li>
<li>Updating the SAY-FAY when the work or its sequence changes</li>
<li>Organising cooperation and information between the trades</li>
<li>Measures so that only authorised persons enter the site</li>
<li>Regular visits with written observations to the client</li>
</ul>
<div class="note"><strong>New since 1 January 2026: full-time presence on large projects.</strong> Law 5239/2025 (Article 40) amended Article 6 of P.D. 305/1996 and set a minimum on-site presence for the coordinator:
<ul>
<li><strong>For the whole duration of the works</strong> on public works that require a class 4 or higher contractor (P.D. 71/2019), and on special buildings under Law 4067/2012 (main use other than housing) with a footprint of 4,000 m² or more according to the building permit.</li>
<li><strong>At least at the start</strong> of the works, the load-bearing structure, the shell and interior layout, and the electrical and mechanical installations, on all other public or private projects.</li>
</ul>
The coordinator's minimum time is written explicitly in their contract and is not offset against the safety technician's time.</div>
<p class="src">Legal basis: P.D. 305/1996, Article 6 as amended by Article 40 of Law 5239/2025 (Government Gazette A 178/2025).</p>
{AUTHOR}
""", "Duties", "h-duties"),
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
    related=rel("en/safety-technician-greece/", "en/health-safety-training/", "en/safety-coordinator/",
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
                "en/labour-inspection-readiness/", "en/safety-coordinator/", "en/guides/safety-technician-hours/"),
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
    lang="en", path="/en/shops-restaurants-tourism/", alt="/katastimata-estiasi-tourismos/",
    title="Safety Technician for Shops, Restaurants and Tourism",
    desc="Health and safety for shops, restaurants and tourist accommodation in Attica: safety technician, written risk assessment and staff training.",
    crumb="Shops, restaurants, tourism", eyebrow="Sector",
    h1="Shops, restaurants <em>and tourism</em>",
    lead=("Even with one employee, a business needs a safety technician and a written occupational risk assessment. "
          "We keep things simple: discreet, targeted visits during your business hours, a clean file ready for inspection and "
          "staff training on what the law requires."),
    faq=[
        ("Can I act as safety technician myself?",
         "In category B and C businesses with up to 20 employees, the law allows it under conditions and with training, as applies from 1 January 2026. The written risk assessment, however, must be prepared by a person with safety technician qualifications. See the <a href=\"{PRE}en/guides/employer-as-safety-technician/\">detailed guide</a>."),
        ("What applies to CPR training in shops, restaurants and hotels?",
         "With up to 50 employees on one site, the training is done with the free training material of the Ministry of Labour. We make sure it is recorded properly in the file."),
    ],
    related=rel("en/safety-technician-greece/", "en/guides/employer-as-safety-technician/", "en/risk-assessment-greece/",
                "en/guides/safety-technician-hours/", "en/labour-inspection-readiness/", "en/evacuation-plans/"),
    body=S("Common hazards", """
<h3>Restaurants and cafes</h3>
<p>Burns and cuts in the kitchen, slips on wet floors, LPG and fryers, cold rooms, carrying heavy crates from the storeroom.</p>
<h3>Shops</h3>
<p>Ladders and high shelving, goods deliveries, electrical installations in old buildings, emergency exits blocked by boxes.</p>
<h3>Tourism and accommodation</h3>
<p>Room cleaning with chemicals and repetitive movements, laundries and linen rooms, pools and plant rooms, seasonal staff that changes every year, evacuation with guests who do not know the building.</p>
<p>For offices and service companies, see <a href="{PRE}en/offices-services/">Offices and services</a>.</p>
""", "Hazards", "h-risks") + S("Where we can help", """
<ul class="check-grid">
<li>Safety technician appointment and visits with the hours that apply</li>
<li>A risk assessment written for your own premises</li>
<li>A file ready for a Labour Inspectorate inspection</li>
<li>Staff training and CPR with the Ministry's material</li>
<li>Checks of fire safety and emergency exits</li>
<li>Phone support when something comes up</li>
</ul>
{AUTHOR}
""", "Services", "h-give"),
))

# ─────────────────────────────────────────────────────────────── P11 OFFICES AND SERVICES
PAGES.append(dict(
    lang="en", path="/en/offices-services/", alt="/grafeia-ypiresies/",
    title="Safety Technician for Offices and Service Companies",
    desc="Health and safety for offices and service companies in Attica: safety technician, written risk assessment, ergonomics, fire safety and staff training.",
    crumb="Offices and services", eyebrow="Sector",
    h1="Offices <em>and services</em>",
    lead=("An office looks like a safe place, and it usually is. The duties still apply: a safety technician and a written "
          "occupational risk assessment, even with one employee. We work discreetly, during your business hours, and "
          "focus on what actually matters in an office: ergonomics, fire safety and staff training."),
    faq=[
        ("Does an office with a few employees need a safety technician?",
         "Yes. Even with one employee, a business must have a safety technician and a written occupational risk assessment (Law 3850/2010, now codified in the Greek Labour Code, Presidential Decree 62/2025). The hours depend on the category and the headcount; see the <a href=\"{PRE}en/guides/safety-technician-hours/\">hours calculator</a>."),
        ("Can I act as safety technician myself?",
         "In category B and C businesses with up to 20 employees, the law allows it under conditions and with training, as applies from 1 January 2026. The written risk assessment, however, must be prepared by a person with safety technician qualifications. See the <a href=\"{PRE}en/guides/employer-as-safety-technician/\">detailed guide</a>."),
    ],
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/health-safety-training/",
                "en/evacuation-plans/", "en/guides/safety-technician-hours/", "en/guides/employer-as-safety-technician/"),
    body=S("Common hazards", """
<ul>
<li>Ergonomics at screen workstations: chairs, screen height, long hours of sitting</li>
<li>Lighting, ventilation and room temperature</li>
<li>Electrical: extension leads, cables on the floor, old installations</li>
<li>Fire safety and emergency exits, especially in the shared areas of multi-storey buildings</li>
<li>Slips and falls on stairs, in corridors and in archive rooms</li>
<li>Work-related stress, fatigue and psychosocial risks, which Law 5239/2025 explicitly requires to be taken into account</li>
</ul>
<p>For shops, restaurants and accommodation, see <a href="{PRE}en/shops-restaurants-tourism/">Shops, restaurants, tourism</a>.</p>
""", "Hazards", "h-risks") + S("Where we can help", """
<ul class="check-grid">
<li>Safety technician appointment and visits with the hours that apply</li>
<li>A risk assessment written for your own premises</li>
<li>Ergonomic assessment of screen workstations</li>
<li>Fire safety checks, escape plans and evacuation drills</li>
<li>Staff training and basic first aid</li>
<li>A file ready for a Labour Inspectorate inspection</li>
</ul>
{AUTHOR}
""", "Services", "h-give"),
))

# ─────────────────────────────────────────────────────────────── P12 ENERGY AND ENVIRONMENT
PAGES.append(dict(
    lang="en", path="/en/energy-environment/", alt="/energeia-perivallon/",
    title="Health and Safety in Energy and Environmental Projects, Greece",
    desc="Safety technician, risk assessment and training for solar and wind farms, substations and environmental facilities: electrical hazards, work at height, confined spaces.",
    crumb="Energy and environment", eyebrow="Sector",
    h1="Energy <em>and environment</em>",
    lead=("On energy projects the hazard is not always visible: voltage that remains after isolation, work at height far "
          "from help, spaces with little oxygen. We act as safety technician and prepare risk assessments for solar and "
          "wind farms, substations and environmental facilities, from construction to maintenance."),
    related=rel("en/safety-technician-greece/", "en/risk-assessment-greece/", "en/labour-inspection-readiness/",
                "en/health-safety-training/", "en/safety-coordinator/", "en/guides/workplace-accident-employer-steps/"),
    body=S("The hazards that stand out", """
<ul>
<li>Electrical hazards: work near or on low, medium and high voltage installations</li>
<li>Work at height: roofs with solar panels, wind turbine towers, poles</li>
<li>Confined spaces: tanks, manholes, ducts, with a risk from gases or lack of oxygen</li>
<li>Isolated work locations, far from immediate help</li>
<li>Weather: heat, wind, lightning</li>
<li>Chemicals, waste and the risk of pollution during operation and maintenance</li>
</ul>
""", "Hazards", "h-risks") + S("What we take on", """
<ul class="check-grid">
<li>Safety technician during construction and operation</li>
<li>Risk assessment per facility and per maintenance task</li>
<li>Isolation and lockout procedures before any intervention</li>
<li>Permits to work for height, confined spaces and hot work</li>
<li>Crew training and emergency plans</li>
<li>Safety coordination when several contractors work together</li>
</ul>
{AUTHOR}
""", "Services", "h-services"),
))

# ─────────────────────────────────────────────────────────────── FOREIGN COMPANIES
PAGES.append(dict(
    lang="en", path="/en/foreign-companies-greece/", alt="/xenes-etaireies-ellada/",
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
<li><strong>Safety technician</strong>Required from the first employee ({LAW}). Small businesses (up to 20 employees) of risk category B and C may, under conditions, use the employer or a trained employee as a Safety Technician.</li>
<li><strong>Occupational physician</strong>As a rule, required from 50 employees upwards.</li>
<li><strong>Written risk assessment (GEEK)</strong>Mandatory for every employer (Article 534 of P.D. 62/2025), prepared by a qualified person and kept up to date.</li>
<li><strong>Accident reporting</strong>Every workplace accident must be reported within 24 hours to the Labour Inspectorate and e-EFKA, and to the police for serious injury or death. Evidence must be kept unchanged.</li>
<li><strong>Occupational disease</strong>Reported within 5 days of being informed by the occupational physician or a public health system doctor.</li>
<li><strong>CPR and Heimlich training</strong>Required since 1 January 2026: through free video material provided by the Ministry of Labor for up to 50 employees per site; above that, courses by certified providers for at least half the staff every three years.</li>
<li><strong>Records</strong>Recommendations book, accident book and list of accidents with more than three working days of incapacity.</li>
</ol>
<p class="src">Legal basis: Greek Labour Code (P.D. 62/2025), as amended by Law 5239/2025 (Government Gazette A' 178/2025). This summary is for orientation and does not replace advice for your specific case.</p>
""", "Checklist", "h-duties") + S("How we help", """
<p>We act as your safety technician in Greece, prepare the risk assessment, run training in English or Greek and keep the Greek records in order. You get one English-speaking engineer as contact, and reports that your management can easily understand.</p>
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
    body=S("The people who support you", """
<div class="team-profile-card">
  <div class="team-profile-photo-wrap"><div class="about-photo-wrap" style="width:200px;height:200px;"><img src="{PRE}img/stavros-malliaris.webp" alt="Stavros Malliaris" width="591" height="588" class="about-photo" loading="lazy" decoding="async"></div></div>
  <div class="team-profile-body">
    <div class="team-profile-role">Founder &amp; lead engineer</div>
    <h3 class="team-profile-name">Stavros Malliaris</h3>
    <p class="team-profile-bio">Civil Engineer (Aristotle University of Thessaloniki) specialising in occupational health and safety (MEng). Over ten years of experience on construction sites, industrial facilities and all types of businesses in Greece and abroad. ASP® certified by the Board of Certified Safety Professionals (BCSP) and internal auditor for ISO 9001, 14001 and 45001.</p>
  </div>
</div>
<div class="team-sub-cards">
  <div class="team-sub-card">
    <div class="team-sub-photo-wrap"><div class="team-sub-photo-circle"><img src="{PRE}img/dimitrios-moudiotis.webp" alt="Dimitrios Moudiotis" width="400" height="400" class="about-photo" loading="lazy" decoding="async"></div></div>
    <div class="team-sub-body">
      <div class="team-profile-role">Mechanical engineering lead</div>
      <h4 class="team-sub-name">Dimitrios Moudiotis</h4>
      <p class="team-sub-bio">Mechanical Engineer (AUTh). Covers mechanical matters: machinery, work equipment, lifting equipment and vehicles. <a href="https://www.moudiotis.gr/" target="_blank" rel="noopener">moudiotis.gr</a></p>
    </div>
  </div>
  <div class="team-sub-card">
    <div class="team-sub-photo-wrap"><div class="team-sub-photo-circle"><img src="{PRE}img/vaios-liapis.webp" alt="Vaios Liapis" width="347" height="400" class="about-photo" loading="lazy" decoding="async"></div></div>
    <div class="team-sub-body">
      <div class="team-profile-role">Engineering studies lead</div>
      <h4 class="team-sub-name">Vaios Liapis</h4>
      <p class="team-sub-bio">Civil Engineer (AUTh). Responsible for studies and drawings: floor plans, escape plans, technical studies. <a href="https://www.vaiosliapis.gr/" target="_blank" rel="noopener">vaiosliapis.gr</a></p>
    </div>
  </div>
  <div class="team-sub-card">
    <div class="team-sub-photo-wrap"><div class="team-sub-photo-circle"><img src="{PRE}img/eleftherios-adam.webp" alt="Eleftherios Adam" width="400" height="400" class="about-photo" loading="lazy" decoding="async"></div></div>
    <div class="team-sub-body">
      <div class="team-profile-role">HSE officer</div>
      <h4 class="team-sub-name">Eleftherios Adam</h4>
      <p class="team-sub-bio">BSc Materials Science, University of Patras. Supports the team in the field, in inspections and in training.</p>
    </div>
  </div>
</div>
""", "Team", "h-people") + S("How we work", """
<p>Three words describe us: <strong>honesty, method, technical knowledge</strong>. We say clearly what is needed and what is not, give priority to the measures that really reduce risk and respect the company's budget.</p>
<p>Every client has one contact person from the team who knows the premises and the staff. Where specialist knowledge is needed (mechanical, structural, drawings), the relevant engineer joins the work.</p>
<p class="src">Malliaris &amp; Partners · Patmou 3, 174 56 Alimos, Athens · +30 211 00 40 193</p>
""", "Approach", "h-how"),
))

# ─────────────────────────────────────────────────────────────── GUIDES - hub
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
    <div class="calc-box"><div class="cb-label">Safety technician</div><div class="cb-num" id="calcTA">-</div><div class="cb-sub" id="calcTAsub"></div></div>
    <div class="calc-box"><div class="cb-label">Occupational physician</div><div class="cb-num" id="calcIE">-</div><div class="cb-sub" id="calcIEsub"></div></div>
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
    related=rel("en/safety-technician-greece/", "en/guides/employer-as-safety-technician/", "en/shops-restaurants-tourism/"),
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
    related=rel("en/risk-assessment-greece/", "en/safety-technician-greece/", "en/labour-inspection-readiness/"),
    body=S("Step by step", """
<ol class="steps">
<li><strong>Care and safety</strong>First aid, call the ambulance (166 or 112) and move others away from the danger.</li>
<li><strong>Preserve the evidence</strong>The employer must keep unchanged everything that can help establish the causes. Take photos before anything changes.</li>
<li><strong>Report within 24 hours</strong>To the Labour Inspectorate and e-EFKA for every workplace accident. For serious injury (transfer and hospital admission) or death, also to the nearest police authority.</li>
<li><strong>Record it</strong>Causes and description in the accident book; accidents with more than three working days of incapacity in the relevant list.</li>
<li><strong>Investigate and act</strong>The measures to prevent a repeat are recorded in the recommendations book, and the risk assessment is updated.</li>
</ol>
<p class="src">Legal basis: Article 534(2) of P.D. 62/2025 (formerly Article 43 of Law 3850/2010), as amended by Article 38 of Law 5239/2025.</p>
<div class="facts"><strong>Need help now?</strong> Call us on <a href="tel:+302110040193">+30 211 00 40 193</a>. If we act as your safety technician, we come for a site survey and investigation.</div>
{AUTHOR}
""", "Steps", "h-steps"),
))

# ─────────────────────────────────────────────────────────────── PRIVACY
PAGES.append(dict(
    lang="en", path="/en/privacy/", alt="/aporrito/", author=False, ctas=False, noindex=True,
    title="Terms of Use, Privacy and Cookies | Malliaris & Partners",
    desc="The terms of use of this website, the limits of the information we publish, how we handle personal data and which cookies we use.",
    crumb="Terms and privacy", eyebrow="Information",
    h1="Terms of use, <em>privacy and cookies</em>",
    lead="The rules for using this website, what the information we publish does and does not mean, and how we handle your personal data and cookies.",
    body=S("Contents", """
<div class="facts"><strong>In short:</strong> The information on this website is general and for information only; it does not replace advice on your own situation. We collect only what you send us and, if you accept, pseudonymised visit statistics. We do not use advertising cookies.</div>
<ol>
<li><a href="#h-terms">Terms of use</a></li>
<li><a href="#h-disclaimer">Legal disclaimer</a></li>
<li><a href="#h-accuracy">Currency and accuracy of information</a></li>
<li><a href="#h-liability">Limitation of liability</a></li>
<li><a href="#h-ip">Intellectual property</a></li>
<li><a href="#h-privacy">Personal data</a></li>
<li><a href="#h-cookies">Cookies</a></li>
<li><a href="#h-third">Third-party services</a></li>
<li><a href="#h-rights">Your rights</a></li>
<li><a href="#h-changes">Changes to these terms</a></li>
<li><a href="#h-reach">Contact</a></li>
<li><a href="#h-updated">Last updated</a></li>
</ol>
<p class="src">This is a translation of the <a href="../../aporrito/">Greek text</a>. If the two differ, the Greek version prevails.</p>
""", "", "h-toc") + S("Terms of use", """
<h3>Who we are</h3>
<p>The website malliarisandpartners.gr belongs to Stavros Malliaris, trading as “Malliaris &amp; Partners”, tax ID (AFM) 104740278, Civil Engineer (professional title awarded in Greece), member of the Technical Chamber of Greece (TEE), registration no. 158581, Patmou 3, 174 56 Alimos, Greece, tel. <a href="tel:+302110040193">+30 211 00 40 193</a>, email <a href="mailto:info@malliarisandpartners.gr">info@malliarisandpartners.gr</a> (“we”). As an engineer, Stavros Malliaris is subject to the rules governing the engineering profession in Greece and to the regulations of the <a href="https://web.tee.gr/" target="_blank" rel="noopener">TEE</a>.</p>
<h3>Acceptance of the terms</h3>
<p>Using the website is free and requires no registration. By using it, you accept these terms. If you do not agree, please do not use the website.</p>
<h3>Permitted use</h3>
<p>You may read and print our pages and share links to them for personal or professional information. You may not:</p>
<ul>
<li>use the website in a way that breaks the law or offends public morals;</li>
<li>attempt unauthorised access, interfere with its operation or introduce malicious code;</li>
<li>copy the content in bulk by automated means (scraping) for republication or commercial use;</li>
<li>send through the contact form unlawful or offensive content, unsolicited advertising, or third-party data you have no right to share.</li>
</ul>
<h3>No professional relationship</h3>
<p>Reading the website, using its tools or sending a message does not create a professional relationship or engagement. Cooperation begins only once we have agreed its scope and terms in writing. Please do not send sensitive information through the form, such as health data of employees, before we have spoken.</p>
<h3>Tools and calculators</h3>
<p>The website’s tools, such as the Safety Technician hours calculator and the short quizzes, give indicative results based on what you enter and on general rules. They do not take account of your business’s specific circumstances and do not replace a review by a competent professional.</p>
<h3>Links to other websites</h3>
<p>We often link to official sources, such as gov.gr, the Labour Inspectorate, e-EFKA and ELINYAE, and to other websites. We choose them carefully, but we do not control their content or privacy policies. Where the text of this website differs from an official legal text or an announcement by a competent authority, the official text prevails.</p>
<h3>Availability</h3>
<p>We aim to keep the website running without interruption, but there may be interruptions for maintenance or for reasons beyond our control. We may change, add or remove content without prior notice.</p>
<h3>Governing law</h3>
<p>These terms are governed by Greek law. The courts of Athens have jurisdiction over disputes, without prejudice to mandatory rules that protect consumers, such as their right to bring proceedings in the courts of their place of residence. If any term is held invalid, the remaining terms continue to apply.</p>
""", "", "h-terms") + S("Legal disclaimer", """
<p>We publish guides, summaries of obligations and references to the legislation on occupational health and safety, because good information helps businesses prevent accidents. We write carefully and draw on our experience. It is important, however, to be clear about the limits of this information:</p>
<ul>
<li><strong>For information only.</strong> The content is provided solely for general information.</li>
<li><strong>Not individual advice.</strong> It is not legal advice, a legal opinion or a technical study for a specific case, and it does not replace the advice of a lawyer, Safety Technician, Occupational Physician, accountant or other competent professional.</li>
<li><strong>Every case is different.</strong> How the law applies depends on the facts: the sector, the number of employees and their roles, the premises, the decisions of the competent authorities. Two businesses that look alike may have different obligations.</li>
<li><strong>Not the sole basis for decisions.</strong> Please do not rely solely on the information on this website for important legal, business or financial decisions.</li>
<li><strong>When to ask a professional.</strong> Where obligations, deadlines, fines or people’s safety are at stake, consult a suitable professional, whether us or anyone else you trust, or the competent authority.</li>
</ul>
<p>When we provide services to a client, what we agree in writing and what the law provides apply; this section concerns only the public content of the website.</p>
""", "", "h-disclaimer") + S("Currency and accuracy of information", """
<p>We make every effort to keep the content accurate and up to date: we follow changes in the legislation and review our pages. Occupational health and safety legislation changes regularly, however, through new laws, codifications, ministerial decisions and circulars. We therefore cannot guarantee that every piece of information always reflects the latest legislation, case law, administrative practice or regulatory amendments. In particular:</p>
<ul>
<li>the law may change after an article or piece of information is published;</li>
<li>some time may pass before the relevant content on the website is updated;</li>
<li>some information may have been published before a recent legislative change;</li>
<li>the “last updated” date of a page or article, where shown, is indicative: it shows when the page was last reviewed and does not guarantee that all of its content remains fully current.</li>
</ul>
<p>For the texts in force, consult the Government Gazette (FEK) and the announcements of the competent authorities, to which we usually link. If you spot something inaccurate or out of date, we would appreciate it if you wrote to us at <a href="mailto:info@malliarisandpartners.gr">info@malliarisandpartners.gr</a> so we can correct it.</p>
""", "", "h-accuracy") + S("Limitation of liability", """
<p>We provide the website with care, as a free source of general information. To the extent permitted by law, we are not liable for loss arising:</p>
<ul>
<li>from decisions taken solely on the basis of general information on the website, without a competent professional examining the specific case;</li>
<li>from temporary unavailability or a technical fault of the website;</li>
<li>from the content or operation of third-party websites and services to which we link.</li>
</ul>
<p>Nothing in these terms excludes or limits any liability or right that cannot lawfully be excluded or limited under applicable law. In particular, it does not limit our liability for intent or gross negligence (Article 332 of the Greek Civil Code), or your rights as a consumer under Law 2251/1994 or as a data subject under the GDPR.</p>
""", "", "h-liability") + S("Intellectual property", """
<p>The texts, guides, graphics, photographs, tools, design and distinctive signs of the website (name, logo) belong to us or to those who have licensed them to us, and are protected by Greek Law 2121/1993 and EU law.</p>
<ul>
<li><strong>You may</strong> read the pages, print them for your own use, share links and quote short extracts with clear attribution and a link to the page.</li>
<li><strong>Our written permission is required</strong> to republish whole texts or substantial parts of them, to modify them, for commercial use and to use our logo.</li>
</ul>
<p>The official legal texts we link to do not belong to us; they are not protected as works (Article 2(5) of Law 2121/1993) and are freely available from the official sources.</p>
""", "", "h-ip") + S("Personal data", """
<h3>Controller</h3>
<p>The controller under the General Data Protection Regulation (EU) 2016/679 (“GDPR”) and Greek Law 4624/2019 is Stavros Malliaris (“Malliaris &amp; Partners”), with the details given under <a href="#h-terms">Terms of use</a>.</p>
<h3>What data we collect</h3>
<ul>
<li><strong>What you send us:</strong> through the contact form, your name, email, phone number (if given), subject and message; similar details when you email us, call us or book an appointment through Calendly.</li>
<li><strong>Usage statistics, only with your consent:</strong> through Google Analytics 4, which pages you visit and for how long, device and browser type, approximate region, and whether you click the contact buttons or use our tools (for example, the category in the hours calculator or the total score of a quiz). This data is linked to a pseudonymous identifier, not to your name.</li>
<li><strong>Technical connection data:</strong> as with any website, the hosting provider and the services that deliver fonts, icons and the map necessarily receive your IP address and browser details in order to send you the page.</li>
</ul>
<p>We do not ask for special categories of data (such as health data) through the website, and we do not take decisions about you based solely on automated processing or profiling. The website is aimed at businesses and professionals, not at minors.</p>
<h3>Why we use it and on what legal basis</h3>
<div class="table-wrap"><table class="data-table">
<caption>Purposes, legal basis and retention</caption>
<thead><tr><th>Purpose</th><th>Legal basis (GDPR)</th><th>How long we keep it</th></tr></thead>
<tbody>
<tr><td>Replying to your request, sending a quote, scheduling an appointment</td><td>Article 6(1)(b) (steps prior to a contract, at your request); for general questions, Article 6(1)(f) (legitimate interest in replying to those who contact us)</td><td>As long as needed for the request and, if no cooperation follows, up to 24 months from the last contact</td></tr>
<tr><td>Performing work for clients, invoicing</td><td>Article 6(1)(b) (contract) and 6(1)(c) (tax and other legal obligations)</td><td>For the duration of the cooperation and thereafter as required by tax and other legislation, or as needed to establish or defend legal claims</td></tr>
<tr><td>Visit statistics to improve the website</td><td>Article 6(1)(a) (consent), together with Article 4(5) of Greek Law 3471/2006</td><td>In Google Analytics, detailed visit data for 2 months and data linked to your identifier for 14 months from your last visit; aggregated statistics that do not identify you may be kept longer. Cookies as shown in the Cookies table</td></tr>
<tr><td>Storing your cookie and language choices</td><td>Article 6(1)(f) (legitimate interest in running the website as you asked)</td><td>Only on your device, until you delete them</td></tr>
<tr><td>Security and technical operation of the website</td><td>Article 6(1)(f) (legitimate interest in secure operation)</td><td>As set by each provider (see <a href="#h-third">Third-party services</a>)</td></tr>
</tbody>
</table></div>
<p>Providing data is optional, but without a name and email we cannot reply to a message sent through the form. Where we rely on legitimate interest, you may object (see <a href="#h-rights">Your rights</a>).</p>
<h3>Who has access</h3>
<p>Your data is seen only by those in our team who need to handle your request. We do not sell data or share it for advertising. We use providers that supply the technical infrastructure or process data on our behalf (see <a href="#h-third">Third-party services</a>). Data may be disclosed to public authorities only where the law requires it.</p>
<h3>Transfers outside the European Economic Area</h3>
<p>Some of these providers are established in, or process data in, the United States. Transfers rely on the European Commission’s adequacy decision for the EU-U.S. Data Privacy Framework, for certified providers, or on standard contractual clauses (Article 46 GDPR).</p>
<h3>Security</h3>
<p>The website runs over an encrypted connection (HTTPS) and keeps no database of its own with visitor data; form messages go straight to our mailbox. The form has anti-abuse measures, and access to our accounts is limited to those who need it. No system on the internet is completely secure; if a breach affecting you occurs, we will act as required by Articles 33 and 34 GDPR.</p>
""", "", "h-privacy") + S("Cookies", """
<p>Cookies are small files stored on your device. We treat similar technologies, such as your browser’s local storage (localStorage), in the same way. Under Article 4(5) of Greek Law 3471/2006, we need your consent for any storage that is not strictly necessary to provide the service you asked for.</p>
<h3>Strictly necessary</h3>
<p>These remember your choices so that we do not ask you again on every page. They do not require consent and are not used for tracking.</p>
<h3>Statistics (analytics)</h3>
<p>Google Analytics 4 runs only if you click “Accept”. Before that, its code is not loaded at all. We use Google’s Consent Mode with all advertising signals switched off.</p>
<h3>Advertising and marketing</h3>
<p>We do not use advertising, remarketing or social media cookies. If this changes, we will update this page first and ask for your consent separately.</p>
<div class="table-wrap"><table class="data-table">
<caption>Cookies and local storage used by the website</caption>
<thead><tr><th>Name</th><th>Category</th><th>Provider</th><th>Purpose</th><th>Duration</th></tr></thead>
<tbody>
<tr><td><code>cookie_consent</code> (localStorage)</td><td>Strictly necessary</td><td>Us</td><td>Remembers whether you accepted or rejected statistics</td><td>Until you delete the website’s data from your browser</td></tr>
<tr><td><code>lang</code> (localStorage)</td><td>Strictly necessary</td><td>Us</td><td>Remembers the language you chose</td><td>As above</td></tr>
<tr><td><code>_ga</code></td><td>Statistics</td><td>Google</td><td>Distinguishes visitors with a pseudonymous identifier</td><td>2 years</td></tr>
<tr><td><code>_ga_W7HGV18VNJ</code></td><td>Statistics</td><td>Google</td><td>Keeps the state of the visit</td><td>2 years</td></tr>
</tbody>
</table></div>
<h3>How to change your choices</h3>
<ul>
<li>On your first visit a banner appears with two equal buttons, “Accept” and “Reject”.</li>
<li>You can change or withdraw your consent at any time via <a href="#" data-cc-open>Cookie settings</a>, also found at the bottom of every page. Withdrawal does not affect the lawfulness of processing carried out before it.</li>
<li>You can also delete or block cookies in your browser settings. <code>_ga</code> cookies already stored are removed there, or expire on their own.</li>
<li>Google also offers a <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">Google Analytics opt-out browser add-on</a> for all websites.</li>
</ul>
<h3>Third-party content with its own cookies</h3>
<p>The Google Maps map in the contact section of the home page is loaded from Google, which may set its own cookies and log your IP address under its own policy. If you follow a link to another website, such as Calendly, that website’s cookies and policy apply.</p>
""", "", "h-cookies") + S("Third-party services", """
<p>We use the following services to run the website. Each provider also processes data under its own privacy policy.</p>
<div class="table-wrap"><table class="data-table">
<caption>Providers and what they receive</caption>
<thead><tr><th>Service</th><th>Use</th><th>Data received</th></tr></thead>
<tbody>
<tr><td><a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub Pages</a> (GitHub, Inc.)</td><td>Hosting the website</td><td>IP address, browser details, page requested (log files)</td></tr>
<tr><td><a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Analytics 4</a> (Google)</td><td>Visit statistics, only with consent</td><td>Pseudonymous identifier, usage data, approximate region</td></tr>
<tr><td>Google Apps Script and Gmail (Google)</td><td>Delivering form messages to our mailbox and sending a copy to your email</td><td>The form details</td></tr>
<tr><td>Google Maps (Google)</td><td>Map on the home page</td><td>IP address, browser details, possibly Google cookies</td></tr>
<tr><td>Google Fonts (Google)</td><td>Web fonts</td><td>IP address, browser details</td></tr>
<tr><td><a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cdnjs</a> (Cloudflare, Inc.)</td><td>Icons (Font Awesome)</td><td>IP address, browser details</td></tr>
<tr><td><a href="https://calendly.com/legal/privacy-notice" target="_blank" rel="noopener">Calendly</a> (Calendly LLC)</td><td>Booking appointments, only if you follow the link</td><td>What you enter in the Calendly form (name, email, appointment time)</td></tr>
</tbody>
</table></div>
""", "", "h-third") + S("Your rights", """
<p>Under Articles 15 to 22 GDPR, you have the right to:</p>
<ul>
<li><strong>access</strong> your data and receive a copy;</li>
<li><strong>rectification</strong> of inaccurate or incomplete data;</li>
<li><strong>erasure</strong>, where there is no longer a reason to keep it;</li>
<li><strong>restriction</strong> of processing;</li>
<li><strong>portability</strong>, that is, to receive the data you gave us in a structured, commonly used format, where processing is based on consent or contract;</li>
<li><strong>object</strong> to processing based on legitimate interest;</li>
<li><strong>withdraw your consent</strong> at any time, without affecting the lawfulness of processing before the withdrawal.</li>
</ul>
<h3>How to make a request</h3>
<p>Write to us at <a href="mailto:info@malliarisandpartners.gr">info@malliarisandpartners.gr</a> or at our postal address, stating which right you wish to exercise. We may ask for details to confirm your identity, only as far as necessary. We reply without undue delay and at the latest within one month; for complex or numerous requests this may be extended by two further months, and we will explain why. Exercising your rights is free of charge, unless requests are manifestly unfounded or excessive (Article 12 GDPR).</p>
<h3>Complaint to the supervisory authority</h3>
<p>If you believe that the processing of your data breaches the law, you have the right to lodge a complaint with the <a href="https://www.dpa.gr/" target="_blank" rel="noopener">Hellenic Data Protection Authority</a>. If you wish, contact us first and we will try to resolve the matter promptly.</p>
""", "", "h-rights") + S("Changes to these terms", """
<p>We review this page when the law, the way the website works or the services we use change. The version published here, with its last updated date, always applies. If a change materially affects how we use your personal data, we will highlight it clearly on the website and, where required, ask for your consent again.</p>
""", "", "h-changes") + S("Contact", """
<p>For questions about these terms, requests concerning your personal data, or to point out an inaccuracy:</p>
<ul>
<li>Email: <a href="mailto:info@malliarisandpartners.gr">info@malliarisandpartners.gr</a> (for data requests, put “Personal data” in the subject line)</li>
<li>Phone: <a href="tel:+302110040193">+30 211 00 40 193</a></li>
<li>Post: Malliaris &amp; Partners, Patmou 3, 174 56 Alimos, Greece</li>
</ul>
""", "", "h-reach") + S("Last updated", """
<p>These terms were last updated on 8 October 2026.</p>
""", "", "h-updated"),
))
