/**
 * i18n.js — Greek / English translation toggle
 * Malliaris H&S Engineer — Σταύρος Μάλλιαρης
 * Modular & reusable. Drop into any page that uses data-i18n attributes.
 *
 * Attributes recognised:
 *   data-i18n="key"             → replaces element.textContent
 *   data-i18n-html="key"        → replaces element.innerHTML
 *   data-i18n-placeholder="key" → replaces element.placeholder
 *
 * Public API:
 *   window.I18n.setLang('el' | 'en')
 *   window.I18n.getLang()
 *   window.setLang(lang)           ← shorthand for onclick="setLang('el')"
 */

(function () {
    'use strict';

    /* ─── TRANSLATIONS ───────────────────────────────────────────────────── */
    const t = {

        /* NAV */
        'nav.title':    { el: 'Σύμβουλοι Υγείας και Ασφάλειας - Τεχνικοί Ασφαλείας', en: 'Health and Safety consultants -<br>Safety Technician services' },
        'nav.about':    { el: 'ΠΟΙΟΙ ΕΙΜΑΣΤΕ',                en: 'WHO WE ARE' },
        'nav.services': { el: 'Υπηρεσίες',                    en: 'Services' },
        'nav.sectors':  { el: 'Τομείς',                       en: 'Sectors' },
        'nav.team':     { el: 'Η ΟΜΑΔΑ ΜΑΣ',                   en: 'OUR TEAM' },
        'nav.action':   { el: 'ΣΤΗΝ ΔΡΑΣΗ',                    en: 'IN ACTION' },
        'nav.contact':  { el: 'Επικοινωνία',                  en: 'Contact' },

        /* HERO CREDENTIAL */
        'cred.studies':     { el: 'ΜΕΛΕΤΕΣ',       en: 'STUDIES' },
        'cred.training':    { el: 'ΕΚΠΑΙΔΕΥΣΕΙΣ',  en: 'TRAINING' },
        'cred.inspections': { el: 'ΕΠΙΘΕΩΡΗΣΕΙΣ',  en: 'INSPECTIONS' },

        /* HERO */
        'hero.name1':    { el: 'ΜΑΛΛΙΑΡΗΣ &amp;',                             en: 'MALLIARIS &amp;' },
        'hero.name2':    { el: '<span style="color:#E8541A;">ΣΥΝΕΡΓΑΤΕΣ</span>', en: '<span style="color:#E8541A;">PARTNERS</span>' },
        'hero.eyebrow':  { el: 'ΥΠΗΡΕΣΙΕΣ ΥΓΕΙΑΣ ΚΑΙ ΑΣΦΑΛΕΙΑΣ ΣΤΗΝ ΕΡΓΑΣΙΑ', en: 'OCCUPATIONAL HEALTH AND SAFETY SERVICES' },
        'hero.cta':      { el: 'ΠΑΡΕ ΠΡΟΣΦΟΡΑ',                                en: 'GET A QUOTE' },
        'hero.stat1.num':{ el: '10+',                                           en: '10+' },
        'hero.stat1.lbl':{ el: 'χρόνια εμπειρίας',                             en: 'years experience' },
        'hero.stat2.num':{ el: '24H/7',                                         en: '24H/7' },
        'hero.stat2.lbl':{ el: 'ΚΑΘΕ ΤΥΠΟΣ ΕΠΙΧΕΙΡΗΣΗΣ',                      en: 'EVERY TYPE OF BUSINESS' },
        'hero.stat3.num':{ el: '360°',                                          en: '360°' },
        'hero.stat3.lbl':{ el: 'ΠΛΗΡΗΣ ΚΑΛΥΨΗ ΣΕ ΘΕΜΑΤΑ Υ&Α',               en: 'FULL H&S COVERAGE' },

        /* MARQUEE */
        'marquee.m1': { el: 'Τεχνικός Ασφαλείας',                              en: 'Safety Technician' },
        'marquee.m2': { el: 'ΓΡΑΠΤΗ Εκτίμηση Επαγγελματικού Κινδύνου',        en: 'WRITTEN Risk Assessment (ΓΕΕΚ)' },
        'marquee.m3': { el: 'Σχέδια Διαφυγής',                                en: 'Escape Plans' },
        'marquee.m4': { el: 'Εκπαιδεύσεις Υ&Α',                              en: 'H&S Training' },
        'marquee.m7': { el: 'ΔΙΕΡΕΥΝΗΣΗ ΕΡΓΑΤΙΚΩΝ ΑΤΥΧΗΜΑΤΩΝ',                en: 'WORKPLACE ACCIDENT INVESTIGATION' },
        'marquee.m8': { el: 'ΣΧΕΔΙΑ ΕΚΚΕΝΩΣΗΣ',                              en: 'EVACUATION PLANS' },
        'marquee.m9': { el: 'ΠΡΟΣΟΜΟΙΩΣΗ ΕΠΙΘΕΩΡΗΣΗΣ ΣΕΠΕ',                  en: 'LABOUR INSPECTORATE SIMULATION' },

        /* TEAM */
        'team.eyebrow':        { el: 'Η ΟΜΑΔΑ ΜΑΣ',                                            en: 'OUR TEAM' },
        'team.heading':        { el: 'Γνωρίστε μας',                                            en: 'Meet the Team' },
        'team.badge':          { el: 'ΙΔΡΥΤΗΣ',                                                 en: 'FOUNDER' },
        'team.role':           { el: 'ΙΔΡΥΤΗΣ & ΕΠΙΚΕΦΑΛΗΣ ΜΗΧΑΝΙΚΟΣ',                        en: 'FOUNDER & LEAD ENGINEER' },
        'team.name':           { el: 'Σταύρος Μάλλιαρης',                                       en: 'Stavros Malliaris' },
        'team.bio':            { el: 'Διπλωματούχος Πολιτικός Μηχανικός ΑΠΘ με εξειδίκευση στην Υγεία και Ασφάλεια στην εργασία. 10+ χρόνια εμπειρίας σε εργοτάξια, βιομηχανίες και επιχειρήσεις κάθε τύπου σε Ελλάδα και εξωτερικό. Κάτοχος διεθνούς πιστοποίησης ASP® (BCSP) και Εσωτερικός Επιθεωρητής ISO 9001, 14001, και 45001. Συνδυάζει υψηλή τεχνική κατάρτιση με ρεαλιστικές και εφαρμόσιμες λύσεις στο πεδίο, που δίνουν αποτελέσματα χωρίς να εκτοξεύουν τον προϋπολογισμό. Οι 3 λέξεις που μας χαρακτηρίζουν;', en: 'Civil Engineer (AUTH) specialising in Health & Safety at Work. 10+ years of experience in construction sites, industrial facilities and all types of businesses in Greece and abroad. Holder of the ASP® (BCSP) certification and Internal Auditor for ISO 9001, 14001, and 45001. Combines high technical expertise with realistic, field-ready solutions that deliver results without blowing the budget. The 3 words that define us?' },
        'team.pill.exp':       { el: '10+ Χρόνια Εμπειρίας',                                   en: '10+ Years Experience' },
        'team.pill.exp.text':  { el: 'Διεθνής εμπειρία σε απαιτητικά έργα υποδομών και επιχειρήσεις κάθε τύπου', en: 'International experience in demanding infrastructure projects and every type of business' },
        'team.pill.cert':      { el: 'ASP® Πιστοποιημένος',                                    en: 'ASP® Certified' },
        'team.pill.cert.text': { el: 'Πιστοποίηση Board of Certified Safety Professionals (BCSP) — το υψηλότερο διεθνές πρότυπο', en: 'Board of Certified Safety Professionals (BCSP) certification — the highest international standard' },
        'team.pill.cov':       { el: 'Πανελλαδική Κάλυψη',                                     en: 'Nationwide Coverage' },
        'team.pill.cov.text':  { el: 'Εξυπηρέτηση επιχειρήσεων σε όλη την Ελλάδα — Αττική, Θεσσαλονίκη, Πανελλαδικά', en: 'Serving businesses across Greece — Attica, Thessaloniki, Nationwide' },

        /* ABOUT */
        'about.eyebrow': { el: 'ΠΟΙΟΙ ΕΙΜΑΣΤΕ', en: 'WHO WE ARE' },
        'about.heading': {
            el: 'Το Προφίλ της Εταιρείας',
            en: 'Company Profile',
        },
        'about.bio.p1': {
            el: 'Ο Σταύρος Μάλλιαρης και οι συνεργάτες του παρέχουν εξειδικευμένες υπηρεσίες <strong>Υγείας &amp; Ασφάλειας στην Εργασία</strong>, από κάλυψη Τεχνικού Ασφαλείας μέχρι Εκπαιδεύσεις Προσωπικού και Σύνταξη ΓΕΕΚ.<br><br>Η εταιρεία μας ιδρύθηκε το 2026, συσπειρώνοντας μηχανικούς με πάνω από μια δεκαετία εμπειρία στις κατασκευές, την βιομηχανία και τις υπηρεσίες. Αφορμή ήταν οι αυξανόμενες ανάγκες για <strong>ουσιαστική ασφάλεια</strong> στους χώρους εργασίας των ελληνικών επιχειρήσεων. Ο στόχος ξεκάθαρος: κάθε εργαζόμενος να επιστρέφει σπίτι του ασφαλής.<br><br>Πιστεύουμε ότι η ασφάλεια δεν θα \'πρεπε να κοστίζει ακριβά, αντιθέτως θα \'πρεπε να βοηθάει την παραγωγή και την βιωσιμότητα της επιχείρησης. Σεβόμαστε τον προϋπολογισμό σας, δίνουμε βάρος στην πρόληψη και προτείνουμε πρακτικές λύσεις με μεγάλο αντίκρεισμα.<br><br>Γιατί η πραγματική ασφάλεια ξεκινά πάντα από τις σωστές βάσεις.',
            en: 'Stavros Malliaris and his partners provide specialised <strong>Occupational Health &amp; Safety</strong> services, from Safety Technician coverage to Staff Training and Written Risk Assessment (ΓΕΕΚ).<br><br>Our company was founded in 2026, bringing together engineers with over a decade of experience in construction, industry and services. The driving force was the growing need for meaningful safety in Greek workplaces. The goal is clear: every employee returns home safe.<br><br>We believe safety should not be expensive — on the contrary, it should support production and business sustainability. We respect each company\'s budget, focus on prevention and propose practical, high-impact solutions.<br><br>Because real safety always starts from the right foundations.',
        },
        'about.bio.p2': {
            el: '',
            en: '',
        },
        'about.bio.p3': {
            el: '',
            en: '',
        },
        'about.bio.p4': {
            el: '',
            en: '',
        },
        'about.tl.m1': { el: 'ΜΑΡ 2026', en: 'MAR 2026' },
        'about.tl.n1': { el: 'Ίδρυση',   en: 'Founded' },
        'about.tl.m2': { el: 'ΑΠΡ 2026', en: 'APR 2026' },
        'about.tl.n2.l1': { el: 'Πρώτοι', en: 'First' },
        'about.tl.n2.l2': { el: 'Πελάτες', en: 'Clients' },
        'about.tl.m3': { el: 'ΜΑΙ 2026', en: 'MAY 2026' },
        'about.tl.n3.l1': { el: 'Επέκταση', en: 'Service' },
        'about.tl.n3.l2': { el: 'Υπηρεσιών', en: 'Expansion' },
        'about.tl.m4': { el: 'ΣΗΜΕΡΑ', en: 'TODAY' },
        'about.tl.n4': { el: 'Εν εξελίξει', en: 'Ongoing' },
        'about.lead': {
            el: '<ul class="about-bullets"><li><span class="hi-num">5+</span> χρόνια <span class="hi-key">διεθνούς εμπειρίας</span> στην Υγεία &amp; Ασφάλεια</li><li>Πιστοποιημένος <span class="hi-badge">ASP®</span> &middot; Πολιτικός Μηχανικός <span class="hi-badge">ΑΠΘ</span></li><li>Εξυπηρέτηση <span class="hi-key">κάθε τύπου επιχείρησης</span> — εστιατόρια, γραφεία, εργοτάξια, βιομηχανίες</li><li>Εκατοντάδες ώρες εκπαίδευσης — <span class="hi-key">πρακτικές λύσεις</span> κατευθείαν στο πεδίο</li><li>Πλήρης <span class="hi-green">νομική κάλυψη</span> &amp; προστασία του ανθρώπινου δυναμικού σας</li></ul>',
            en: '<ul class="about-bullets"><li><span class="hi-num">5+</span> years of <span class="hi-key">international H&amp;S experience</span></li><li>Certified <span class="hi-badge">ASP®</span> &middot; Civil Engineer <span class="hi-badge">AUTH</span></li><li>Supporting <span class="hi-key">every business type</span> — restaurants, offices, construction sites, industry</li><li>Hundreds of training hours — <span class="hi-key">practical solutions</span> directly in the field</li><li>Full <span class="hi-green">legal compliance</span> &amp; protection of your most valuable asset: your people</li></ul>',
        },
        'about.dim': { el: 'Ελλάδα — Διεθνώς', en: 'Greece — International' },

        /* FEATURES — Γιατί να μας επιλέξετε */
        'feature.risk.label':        { el: 'Πολυετής Εμπειρία', en: 'Safety Expertise' },
        'feature.risk.text':         { el: 'Αναγνωρίζουμε έγκαιρα κινδύνους και προτείνουμε πρακτικές λύσεις που λειτουργούν στην πράξη και βοηθούν την παραγωγή', en: 'We identify risks early and propose practical solutions that work in the field and support production' },
        'feature.custom.label':      { el: 'Στοχευμένη Εξυπηρέτηση',    en: 'Targeted Service' },
        'feature.custom.text':       { el: 'Εξατομικευμένη αξιολόγηση και σαφείς προτάσεις προσαρμοσμένες στο μέγεθος και τον χαρακτήρα της επιχείρησης', en: 'Individual assessment with clear, specific proposals adapted to the size and nature of each business' },
        'feature.compliance.label':  { el: 'Άρτια Επικοινωνία', en: 'Clear Communication' },
        'feature.compliance.text':   { el: 'Διαχειριζόμαστε κάθε πληροφορία με εχεμύθεια και δίνουμε ιδιαίτερη έμφαση στη σαφή επικοινωνία με τη διοίκηση και το προσωπικό', en: 'We handle all information with confidentiality and place special emphasis on clear communication with management and staff' },

        /* SERVICES */
        'services.eyebrow': { el: 'ΥΠΗΡΕΣΙΕΣ', en: 'SERVICES' },
        'services.heading': {
            el: 'Παρέχουμε ένα <span class="hi-orange">πλήρες πακέτο</span> <em class="hi-white">Υπηρεσιών Υ&amp;Α</em>',
            en: 'We provide a <span class="hi-orange">complete package</span> of <em class="hi-white">H&amp;S Services</em>',
        },
        'services.legal': {
            el: 'Σύμφωνα με το Ν. 3850/2010, ακόμα και για ένα άτομο προσωπικό <strong>η επιχείρηση πρέπει να έχει Τεχνικό Ασφαλείας και ΓΕΕΚ</strong> — Νόμος 3850/2010, Άρθρο 8 &amp; 43',
            en: 'Under Law 3850/2010, even a single employee business is required to have a declared Safety Technician and a Risk Assessment — Law 3850/2010, Articles 8 &amp; 43',
        },

        'services.measlabel': { el: '6 ΥΠΗΡΕΣΙΕΣ - 100% ΙΚΑΝΟΠΟΙΗΣΗ', en: '6 SERVICES - 100% SATISFACTION' },

        's1.title': { el: 'Κάλυψη Τεχνικού Ασφαλείας', en: 'Safety Technician Services' },
        's1.text':  {
            el: 'Υποχρεωτική για κάθε εταιρεία σύμφωνα με το Νόμο 3850/2010, Άρθρο 8. Μηνιαίες επισκέψεις Τεχνικού Ασφαλείας στο χώρο σας για αναγνώριση κινδύνων, επίβλεψη συνθηκών εργασίας και στοχευμένες προτάσεις. Full-time ή Part-time.',
            en: 'Mandatory for every business under Law 3850/2010, Article 8. Monthly Safety Technician visits for hazard identification, supervision of working conditions, and targeted recommendations. Full-time or Part-time.',
        },

        's2.title': { el: 'Σύνταξη ΓΕΕΚ', en: 'Written Occupational Risk Assessment (GEEK)' },
        's2.text':  {
            el: 'Υποχρεωτική για κάθε εταιρεία σύμφωνα με το Νόμο 3850/2010, Άρθρο 43. Εκπόνηση μελέτης εκτίμησης επαγγελματικού κινδύνου ανάλογα με τη δραστηριότητα και τις θέσεις εργασίας.',
            en: 'Mandatory under Law 3850/2010, Article 43. We prepare the occupational risk assessment study based on your activity and job positions.',
        },

        's3.title': { el: 'Εκπαιδεύσεις Υγείας & Ασφάλειας', en: 'H&S Training Programmes' },
        's3.text':  {
            el: 'Ανάλογα με τις ανάγκες κάθε επιχείρησης, παρέχουμε ευρύ φάσμα εκπαιδεύσεων για εργαζόμενους σύμφωνα με Νόμο 3850/2010, Άρθρο 48.',
            en: 'Tailored to each business needs, we provide a wide range of employee training programmes under Law 3850/2010, Article 48.',
        },

        's4.title': { el: 'Διερεύνηση Εργατικών Ατυχημάτων', en: 'Workplace Accident Investigation' },
        's4.text':  {
            el: 'Διερεύνηση κάθε είδους εργατικού ατυχήματος με εχεμύθεια και πλήρη επαγγελματισμό. Root Cause Analysis, προτάσεις διορθωτικών ενεργειών και σύνταξη έκθεσης ατυχήματος.',
            en: 'We investigate all types of workplace accidents with full confidentiality, including Root Cause Analysis, corrective action recommendations, and accident report preparation.',
        },

        's5.title': { el: 'Εκπόνηση Σχεδίων Διαφυγής', en: 'Escape Plan Design' },
        's5.text':  {
            el: 'Μελέτη, σχεδιασμός και αποτύπωση Σχεδίων Διαφυγής και Εκκένωσης — βασικό εργαλείο συμμόρφωσης με Πυροσβεστική Υπηρεσία και εργατική νομοθεσία.',
            en: 'Study, design and documentation of Escape and Evacuation Plans — a key compliance tool for Fire Service and labour legislation.',
        },

        's6.title': { el: 'Προετοιμασία για Επιθεώρηση ΣΕΠΕ', en: 'Labour Inspectorate (SEPE) Audit Prep' },
        's6.text':  {
            el: 'Έλεγχος συνθηκών εργασίας και φακέλου Υγείας & Ασφάλειας της επιχείρησης για διαπίστωση βαθμού συμμόρφωσης με την ισχύουσα νομοθεσία και πρόταση διορθωτικών ενεργειών.',
            en: 'Review of working conditions and the business H&S file to determine compliance level with current legislation and propose necessary corrective actions.',
        },

        /* SECTORS */
        'sectors.eyebrow': { el: 'ΤΟΜΕΙΣ', en: 'SECTORS' },
        'sectors.heading': {
            el: 'Τομείς <em>Δραστηριότητας</em>',
            en: 'Sectors of <em>Activity</em>',
        },
        'sectors.lead': {
            el: 'Μετά από πολυετή εμπειρία σε απαιτητικά έργα υποδομών και επιχειρήσεις κάθε είδους, ο Σταύρος Μάλλιαρης και η ομάδα του μπορούν να συμβουλέψουν πελάτες από κάθε τομέα δραστηριότητας.',
            en: 'With years of experience across demanding infrastructure projects and businesses of all kinds, Stavros Malliaris and his team can advise clients from every sector of activity.',
        },

        /* RESOURCES */
        'resources.eyebrow': { el: 'Γνώση & Πόροι',                      en: 'Knowledge & Resources' },
        'resources.heading': {
            el: 'Άρθρα &amp; <em>Χρήσιμοι Σύνδεσμοι</em>',
            en: 'Articles &amp; <em>Useful Links</em>',
        },

        /* CONTACT */
        'contact.eyebrow': { el: 'Επικοινωνία', en: 'Contact' },
        'contact.heading': {
            el: 'Μιλήστε <em>μαζί μας</em>',
            en: 'Let\'s <em>talk</em>',
        },
        'contact.role':    { el: 'Σύμβουλος Υγείας και Ασφάλειας', en: 'Health & Safety Consultant' },
        'contact.role2':   { el: 'Πολιτικός Μηχανικός, MEng, ASP®', en: 'Civil Engineer, MEng, ASP®' },
        'contact.calendly':{ el: 'ΚΛΕΙΣΤΕ ΡΑΝΤΕΒΟΥ',                  en: 'BOOK APPOINTMENT' },

        /* FORM */
        'form.title':          { el: 'Φόρμα επικοινωνίας',        en: 'Contact Form' },
        'form.label.name':     { el: 'Ονοματεπώνυμο',            en: 'Full Name' },
        'form.ph.name':        { el: 'Το όνομά σας',              en: 'Your name' },
        'form.label.phone':    { el: 'Τηλέφωνο',                 en: 'Phone' },
        'form.label.email':    { el: 'Email',                     en: 'Email' },
        'form.ph.email':       { el: 'email@example.gr',          en: 'email@example.com' },
        'form.label.subject':  { el: 'Αντικείμενο',              en: 'Subject' },
        'form.select.default': { el: 'Επιλέξτε υπηρεσία',        en: 'Select a service' },
        'form.opt.1':          { el: 'Κάλυψη Τεχνικού Ασφαλείας',                             en: 'Safety Technician Services' },
        'form.opt.2':          { el: 'ΓΕΕΚ - Γραπτή Εκτίμηση Επαγγελματικού Κινδύνου',      en: 'Occupational Risk Assessment Study (GEEK)' },
        'form.opt.3':          { el: 'Εκπαιδεύσεις Υ&Α',                                     en: 'H&S Training' },
        'form.opt.4':          { el: 'Διερεύνηση Εργατικού Ατυχήματος',                       en: 'Accident Investigation' },
        'form.opt.5':          { el: 'Σχέδια Διαφυγής',                                        en: 'Escape Plans' },
        'form.opt.6':          { el: 'Προετοιμασία για Επιθεώρηση ΣΕΠΕ',                      en: 'Labour Inspectorate (SEPE) Audit Prep' },
        'form.opt.7':          { el: 'Άλλο',                                                  en: 'Other' },
        'form.label.message':  { el: 'Μήνυμα',                   en: 'Message' },
        'form.ph.message':     { el: 'Περιγράψτε σύντομα το αίτημά σας...', en: 'Briefly describe your request...' },
        'form.submit':         { el: 'Αποστολή Μηνύματος ✉️',    en: 'Send Message ✉️' },

        /* GAUGE */
        'gauge.label': { el: 'Συμμόρφωση', en: 'Compliance' },

        /* CHECKLIST */
        'cl.item1': { el: 'ΓΕΕΚ εκπονημένο',              en: 'Risk assessment completed' },
        'cl.item2': { el: 'Εκπαίδευση εργαζομένων',       en: 'Employee training done' },
        'cl.item3': { el: 'Σχέδιο εκκένωσης',             en: 'Evacuation plan in place' },
        'cl.item4': { el: 'Σήμανση ασφαλείας',            en: 'Safety signage installed' },
        'cl.item5': { el: 'Ν.3850/2010 συμμόρφωση',       en: 'Law 3850/2010 compliant' },

        /* SECTOR CARDS */
        'sec1.title': { el: 'Εστίαση και Τουρισμός', en: 'Hospitality & Tourism' },
        'sec1.text':  {
            el: '<li>Εργονομία &amp; Θέσεις Εργασίας</li><li>Πυρασφάλεια &amp; Σχέδια Εκκένωσης</li><li>Αναγνώριση Κινδύνων Υγειονομικών Χώρων</li><li>Εκπαίδευση Προσωπικού σε Θέματα Υ&amp;Α</li><li>Σχέδια Έκτακτης Ανάγκης για Επισκέπτες</li>',
            en: '<li>Ergonomics &amp; Workstations</li><li>Fire Safety &amp; Evacuation Plans</li><li>Hazard Identification in Catering Areas</li><li>Staff H&amp;S Training</li><li>Emergency Plans for Guests</li>',
        },
        'sec2.title': { el: 'Εμπόριο και Υπηρεσίες', en: 'Retail & Services' },
        'sec2.text':  {
            el: '<li>Αξιολόγηση Κινδύνου Γραφείου ή Καταστήματος</li><li>Έλεγχος Ηλεκτρολογικών Εγκαταστάσεων</li><li>Εκπαίδευση Βασικών Πρώτων Βοηθειών</li><li>Μελέτη Φωτισμού και Αερισμού Χώρων</li><li>Διαχείριση Επαγγελματικού Άγχους &amp; Κόπωσης</li>',
            en: '<li>Office or Shop Risk Assessment</li><li>Electrical Installations Inspection</li><li>Basic First Aid Training</li><li>Lighting and Ventilation Study</li><li>Occupational Stress &amp; Fatigue Management</li>',
        },
        'sec3.title': { el: 'Κατασκευές και Υποδομές', en: 'Construction & Infrastructure' },
        'sec3.text':  {
            el: '<li>Σχέδιο Ασφάλειας και Υγείας (ΣΑΥ/ΦΑΥ)</li><li>Πρόληψη Πτώσεων &amp; Μέτρα Προστασίας</li><li>Επιθεώρηση Εργοταξίου — Έλεγχος εξοπλισμού</li><li>Ασφαλής Χρήση Μηχανημάτων Έργου</li><li>Οργάνωση Πυροπροστασίας Εργοταξίου</li>',
            en: '<li>Safety &amp; Health Plan (SAY/FAY)</li><li>Fall Prevention &amp; Protection Measures</li><li>Site Inspection — Equipment Check</li><li>Safe Use of Construction Machinery</li><li>Site Fire Safety Organisation</li>',
        },
        'sec4.title': { el: 'Μεταφορές και Logistics', en: 'Transport & Logistics' },
        'sec4.text':  {
            el: '<li>Ασφαλής Αποθήκευση &amp; Στοίβαξη</li><li>Κυκλοφορία Εντός Εγκαταστάσεων</li><li>Χειρωνακτική Διακίνηση Φορτίων</li><li>Έλεγχος Κατάστασης Εξοπλισμού Φόρτωσης</li><li>Σεμινάρια Ασφαλούς Κίνησης Εντός Αποθηκών</li>',
            en: '<li>Safe Storage &amp; Stacking</li><li>Traffic Management Within Premises</li><li>Manual Handling of Loads</li><li>Loading Equipment Condition Check</li><li>Safe Movement in Warehouses Seminars</li>',
        },
        'sec5.title': { el: 'Ενέργεια και Περιβάλλον', en: 'Energy & Environment' },
        'sec5.text':  {
            el: '<li>Διαχείριση Ηλεκτρικού Κινδύνου</li><li>Ασφάλεια σε Ανανεώσιμες Πηγές</li><li>Περιβαλλοντική Πρόληψη</li><li>Εργασία σε Περιορισμένους Χώρους</li><li>Πρωτόκολλα Συντήρησης Υψηλής Τάσης</li>',
            en: '<li>Electrical Risk Management</li><li>Safety in Renewable Energy</li><li>Environmental Prevention</li><li>Confined Space Work</li><li>High Voltage Maintenance Protocols</li>',
        },
        'sec6.title': { el: 'Βιομηχανία και Παραγωγή', en: 'Industry & Production' },
        'sec6.text':  {
            el: '<li>Ασφαλής Χειρισμός Μηχανημάτων</li><li>Διαχείριση Χημικών Παραγόντων</li><li>Μελέτες ATEX</li><li>Σήμανση Ασφάλειας Χώρων Εργασίας</li><li>Τακτικοί Έλεγχοι Συστημάτων Ασφαλείας</li>',
            en: '<li>Safe Machine Operation</li><li>Chemical Agents Management</li><li>ATEX Studies</li><li>Workplace Safety Signage</li><li>Regular Safety System Inspections</li>',
        },

        /* IN ACTION */
        'action.eyebrow': { el: 'Στη Δράση',       en: 'In the Field' },
        'action.heading': {
            el: 'Επί το <em>Έργω</em>',
            en: 'IN <em>ACTION</em>',
        },
        'action.cap1': { el: 'Παρουσίαση Επικίνδυνων Ενεργειών',                            en: 'Presentation of Hazardous Energies' },
        'action.cap2': { el: 'Εκπαίδευση Εργασίας σε Ύψος',                                en: 'Working at Height Training' },
        'action.cap3': { el: 'Μηνιαία Συγκέντρωση Υ&Α Εργαζομένων',                        en: 'Monthly H&S Townhall Meeting' },
        'action.cap4': { el: 'Εκπαίδευση για Χρήση ΜΑΠ',                                   en: 'Use of PPE Training' },
        'action.cap5': { el: 'Εκπαίδευση για Περιορισμένους Χώρους',                        en: 'Confined Space Entry Training' },
        'action.cap6': { el: 'Καθημερινός Έλεγχος Ασφάλειας Χειριστών Αναβατορίου',        en: 'Daily Safety Check for Hoist Operators' },
        'action.cap7': { el: 'Πρωινή Συνάντηση Υγείας και Ασφάλειας',                      en: 'Morning Health & Safety Toolbox' },

        /* GOAL SECTION */
        'goal.eyebrow':   { el: 'ΣΤΟΧΟΣ ΜΑΣ',     en: 'OUR GOAL' },
        'goal.stat2.lbl': { el: 'κάλυψη Υ&Α',      en: 'H&S coverage' },
        'goal.stat3.lbl': { el: 'ικανοποίηση',      en: 'satisfaction' },

        /* QUOTE */
        'quote.text': {
            el: '«Στόχος μας είναι η μετατροπή της ασφάλειας από τυπική υποχρέωση σε ουσιαστικό πλεονέκτημα για την επιχείρησή σας»',
            en: '"Our goal is to transform safety from a formal obligation into a real competitive advantage for your business."',
        },
        'quote.author': { el: 'Σταύρος Μάλλιαρης - Πολιτικός Μηχανικός ΑΠΘ, MEng, ASP®', en: 'Stavros Malliaris - Civil Engineer AUTh, MEng, ASP®' },

        /* RESOURCES */
        'res1.title': { el: 'ΕΛΙΝΥΑΕ', en: 'ELINYAE' },
        'res1.text':  { el: 'Ελληνικό Ινστιτούτο Υγιεινής και Ασφάλειας της Εργασίας — νέες εκδόσεις, μελέτες, εκπαιδευτικό υλικό και ενημέρωση για την Υ&Α.', en: 'Hellenic Institute for Occupational Health & Safety — new publications, studies, training material and H&S updates.' },
        'res2.title': { el: 'Νόμος 3850/2010', en: 'Law 3850/2010' },
        'res2.text':  { el: 'Κωδικοποιημένο κείμενο του Ν. 3850/2010 — ο βασικός νόμος για την Υγεία και Ασφάλεια στην Εργασία στην Ελλάδα.', en: 'Consolidated text of Law 3850/2010 — the primary Greek H&S at Work legislation.' },
        'res3.title': { el: 'Επιθεώρηση Εργασίας', en: 'Labour Inspectorate' },
        'res3.text':  { el: 'Επίσημος φορέας ελέγχου εφαρμογής της εργατικής νομοθεσίας — Υποχρεώσεις εργοδότη, Ο ρόλος του Τεχνικού Ασφαλείας, Έντυπα.', en: 'Official enforcement body for labour legislation — Employer obligations, The Safety Technician role, Official forms.' },
        'res4.title': { el: 'OiRA — Εκτίμηση Κινδύνου', en: 'OiRA — Risk Assessment' },
        'res4.text':  { el: 'Διαδραστικά εργαλεία εκτίμησης επαγγελματικού κινδύνου ανά κλάδο, εκδοθέντα από το Υπ. Εργασίας & την EU-OSHA.', en: 'Interactive sector-specific occupational risk assessment tools published by the Ministry of Labour & EU-OSHA.' },
        'res5.title': { el: 'Αναγγελία Εργατικού Ατυχήματος', en: 'Workplace Accident Reporting' },
        'res5.text':  { el: 'Επίσημη διαδικασία αναγγελίας εργατικού ατυχήματος μέσω gov.gr — υποχρεώσεις εργοδότη και βήματα υποβολής.', en: 'Official workplace accident reporting process via gov.gr — employer obligations and submission steps.' },
        'res6.title': { el: 'sepenet.gr', en: 'sepenet.gr' },
        'res6.text':  { el: 'Πλατφόρμα για την online αναγγελία Τεχνικού Ασφαλείας στο ΣΕΠΕ — γρήγορη και εύκολη ηλεκτρονική διαδικασία.', en: 'Platform for online registration of Safety Technicians with SEPE — quick and easy process.' },
        'res7.title': { el: 'EU-OSHA', en: 'EU-OSHA' },
        'res7.text':  { el: 'Ευρωπαϊκός Οργανισμός για την Ασφάλεια & Υγεία στην Εργασία — οδηγοί, εκστρατείες και βέλτιστες πρακτικές.', en: 'European Agency for Safety & Health at Work — guides, campaigns and best practices.' },
        'res8.title': { el: 'ILO — Διεθνής Εργασία', en: 'ILO — International Labour' },
        'res8.text':  { el: 'Διεθνής Οργανισμός Εργασίας — πρότυπα, εργαλεία και εκπαιδευτικό υλικό για Υ&Α παγκοσμίως.', en: 'International Labour Organization — global H&S standards, tools and training resources.' },
        'res9.title': { el: 'ΙΚΑ — Εργατικά Ατυχήματα', en: 'IKA — Occupational Accidents' },
        'res9.text':  { el: 'Οδηγός αποζημίωσης εργατικών ατυχημάτων και επαγγελματικών ασθενειών μέσω ΕΦΚΑ/ΙΚΑ.', en: 'Guide to compensation for workplace accidents and occupational diseases via EFKA/IKA.' },
        'res10.title': { el: 'ΚΕΕΛΠΝΟ / ΕΟΔΥ', en: 'EODY — Public Health' },
        'res10.text':  { el: 'Εθνικός Οργανισμός Δημόσιας Υγείας — πρωτόκολλα υγιεινής και ασφάλειας για εργασιακούς χώρους.', en: 'National Public Health Organisation — workplace hygiene and safety protocols.' },
        'res11.title': { el: 'ΑΣΕΠ — Τεχνικός Ασφαλείας', en: 'ASEP — Safety Technician' },
        'res11.text':  { el: 'Επίσημος κατάλογος πιστοποιημένων Τεχνικών Ασφαλείας και προϋποθέσεις αναγνώρισης προσόντων.', en: 'Official registry of certified Safety Technicians and qualification recognition requirements.' },
        'res.visit':  { el: 'Επίσκεψη', en: 'Visit' },

        /* CONTACT */
        'contact.location': { el: 'Ελλάδα & Διεθνώς', en: 'Greece & Abroad' },

        /* NAME */
        'name.stavros':  { el: 'ΜΑΛΛΙΑΡΗΣ ΣΤΑΥΡΟΣ',      en: 'MALLIARIS STAVROS' },
        'name.company':  { el: 'ΜΑΛΛΙΑΡΗΣ & ΣΥΝΕΡΓΑΤΕΣ', en: 'MALLIARIS & PARTNERS' },

        /* HOVER HINT */
        'hint.hover': { el: 'HOVER ΓΙΑ ΠΑΥΣΗ', en: 'HOVER TO PAUSE' },

        /* FOOTER */
        'footer.title': { el: 'Υπηρεσίες Υγείας και Ασφάλειας - Τεχνικοί Ασφαλείας', en: 'Health and Safety consultants -<br>Safety Technician services' },
    };

    /* ─── STATE ──────────────────────────────────────────────────────────── */
    let currentLang = 'el';

    /* ─── APPLY TRANSLATIONS ─────────────────────────────────────────────── */
    function applyLang(lang) {
        currentLang = lang;
        localStorage.setItem('lang', lang);

        /* text content */
        document.querySelectorAll('[data-i18n]').forEach(function (el) {
            var key = el.getAttribute('data-i18n');
            if (t[key] && t[key][lang] !== undefined) {
                el.textContent = t[key][lang];
            }
        });

        /* innerHTML (for keys with HTML tags) */
        document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
            var key = el.getAttribute('data-i18n-html');
            if (t[key] && t[key][lang] !== undefined) {
                el.innerHTML = t[key][lang];
            }
        });

        /* placeholder attribute */
        document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
            var key = el.getAttribute('data-i18n-placeholder');
            if (t[key] && t[key][lang] !== undefined) {
                el.placeholder = t[key][lang];
            }
        });

        /* update <html lang> attribute */
        document.documentElement.lang = lang;

        /* update toggle button states */
        document.querySelectorAll('.lang-btn').forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
        });
    }

    /* ─── PUBLIC API ─────────────────────────────────────────────────────── */
    window.I18n = {
        setLang: applyLang,
        getLang: function () { return currentLang; },
        translations: t,
    };

    /* Global shorthand used by onclick="setLang('en')" buttons */
    window.setLang = applyLang;

    /* ─── INIT ───────────────────────────────────────────────────────────── */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () { applyLang(currentLang); });
    } else {
        applyLang(currentLang);
    }

})();
