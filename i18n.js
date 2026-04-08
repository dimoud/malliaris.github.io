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
 *   window.setLang(lang)          ← shorthand for onclick="setLang('el')"
 */

(function () {
    'use strict';

    /* ─── TRANSLATIONS ───────────────────────────────────────────────────── */
    const t = {

        /* NAV */
        'nav.title':    { el: 'Τεχνικός Ασφαλείας - Σύμβουλος Υγείας και Ασφάλειας', en: 'Safety Officer - H&S Consultant' },
        'nav.about':    { el: 'Σχετικά',                      en: 'About' },
        'nav.services': { el: 'Υπηρεσίες',                    en: 'Services' },
        'nav.sectors':  { el: 'Τομείς',                       en: 'Sectors' },
        'nav.action':   { el: 'ΣΤΗΝ ΔΡΑΣΗ',                    en: 'IN ACTION' },
        'nav.contact':  { el: 'Επικοινωνία',                  en: 'Contact' },

        /* HERO */
        'hero.name1':    { el: 'ΣΤΑΥΡΟΣ',                                      en: 'STAVROS' },
        'hero.name2':    { el: 'ΜΑΛΛΙΑΡΗΣ',                                    en: 'MALLIARIS' },
        'hero.eyebrow':  { el: 'ΠΙΣΤΟΠΟΙΗΜΕΝΟΣ ΜΗΧΑΝΙΚΟΣ ΥΓΕΙΑΣ ΚΑΙ ΑΣΦΑΛΕΙΑΣ ΑΠΘ', en: 'CERTIFIED H&S ENGINEER - AUTH' },
        'hero.cta':      { el: 'ΠΑΡΕ ΠΡΟΣΦΟΡΑ',                                en: 'GET A QUOTE' },
        'hero.stat1.num':{ el: '7+',                                            en: '7+' },
        'hero.stat1.lbl':{ el: 'χρόνια εμπειρίας',                             en: 'years experience' },
        'hero.stat2.num':{ el: '24Η/7',                                         en: '24H/7' },
        'hero.stat2.lbl':{ el: 'ΚΑΘΕ ΤΥΠΟΣ ΕΠΙΧΕΙΡΗΣΗΣ',                      en: 'EVERY TYPE OF BUSINESS' },
        'hero.stat3.num':{ el: '360°',                                          en: '360°' },
        'hero.stat3.lbl':{ el: 'ΠΛΗΡΗΣ ΚΑΛΥΨΗ ΣΕ ΘΕΜΑΤΑ Υ&Α',               en: 'FULL H&S COVERAGE' },

        /* MARQUEE */
        'marquee.m1': { el: 'Τεχνικός Ασφαλείας',                              en: 'Safety Officer' },
        'marquee.m2': { el: 'ΓΡΑΠΤΗ Εκτίμηση Επαγγελματικού Κινδύνου',        en: 'WRITTEN Risk Assessment (ΓΕΕΚ)' },
        'marquee.m3': { el: 'Σχέδια Εκκένωσης',                               en: 'Evacuation Plans' },
        'marquee.m4': { el: 'Εκπαιδεύσεις Υ&Α',                              en: 'H&S Training' },
        'marquee.m7': { el: 'ΔΙΕΡΕΥΝΗΣΗ ΕΡΓΑΤΙΚΩΝ ΑΤΥΧΗΜΑΤΩΝ',                en: 'WORKPLACE ACCIDENT INVESTIGATION' },
        'marquee.m8': { el: 'ΣΧΕΔΙΑ ΕΚΚΕΝΩΣΗΣ',                              en: 'EVACUATION PLANS' },
        'marquee.m9': { el: 'ΠΡΟΣΟΜΟΙΩΣΗ ΕΠΙΘΕΩΡΗΣΗΣ ΣΕΠΕ',                  en: 'LABOUR INSPECTORATE SIMULATION' },

        /* ABOUT */
        'about.eyebrow': { el: 'ΠΟΙΟΙ ΕΙΜΑΣΤΕ', en: 'WHO WE ARE' },
        'about.heading': {
            el: 'Σταύρος Μάλλιαρης',
            en: 'Stavros Malliaris',
        },
        'about.lead': {
            el: '<ul class="about-bullets"><li><span class="hi-num">5+</span> χρόνια <span class="hi-key">διεθνούς εμπειρίας</span> στην Υγεία &amp; Ασφάλεια</li><li>Πιστοποιημένος <span class="hi-badge">ASP®</span> &middot; Πολιτικός Μηχανικός <span class="hi-badge">ΑΠΘ</span></li><li>Εξυπηρέτηση <span class="hi-key">κάθε τύπου επιχείρησης</span> — εστιατόρια, γραφεία, εργοτάξια, βιομηχανίες</li><li>Εκατοντάδες ώρες εκπαίδευσης — <span class="hi-key">πρακτικές λύσεις</span> κατευθείαν στο πεδίο</li><li>Πλήρης <span class="hi-green">νομική κάλυψη</span> &amp; προστασία του ανθρώπινου δυναμικού σας</li></ul>',
            en: '<ul class="about-bullets"><li><span class="hi-num">5+</span> years of <span class="hi-key">international H&amp;S experience</span></li><li>Certified <span class="hi-badge">ASP®</span> &middot; Civil Engineer <span class="hi-badge">AUTH</span></li><li>Supporting <span class="hi-key">every business type</span> — restaurants, offices, construction sites, industry</li><li>Hundreds of training hours — <span class="hi-key">practical solutions</span> directly in the field</li><li>Full <span class="hi-green">legal compliance</span> &amp; protection of your most valuable asset: your people</li></ul>',
        },
        'about.dim': { el: 'Ελλάδα — Διεθνώς', en: 'Greece — International' },

        /* FEATURES — Γιατί να μας επιλέξετε */
        'feature.risk.label':        { el: 'Πολυετής Εμπειρία σε Θέματα Ασφάλειας', en: 'Safety Expertise' },
        'feature.risk.text':         { el: 'Αναγνωρίζουμε έγκαιρα κινδύνους και προτείνουμε πρακτικές λύσεις που λειτουργούν στην πράξη', en: 'We identify risks early and propose practical solutions that work in the field' },
        'feature.custom.label':      { el: 'Στοχευμένη Εξυπηρέτηση',    en: 'Targeted Service' },
        'feature.custom.text':       { el: 'Εξατομικευμένη αξιολόγηση και σαφείς προτάσεις προσαρμοσμένες στο μέγεθος και τον χαρακτήρα της επιχείρησης', en: 'Individual assessment with clear, specific proposals adapted to the size and nature of each business' },
        'feature.compliance.label':  { el: 'Διακριτικότητα & Άρτια Επικοινωνία', en: 'Discretion & Clear Communication' },
        'feature.compliance.text':   { el: 'Διαχειριζόμαστε κάθε πληροφορία με απόλυτη εχεμύθεια και δίνουμε ιδιαίτερη έμφαση στη σαφή επικοινωνία με τη διοίκηση και το προσωπικό', en: 'We handle all information with full confidentiality and place special emphasis on clear communication with management and staff' },

        /* SERVICES */
        'services.eyebrow': { el: 'ΥΠΗΡΕΣΙΕΣ', en: 'SERVICES' },
        'services.heading': {
            el: 'Παρέχουμε ένα <span class="hi-orange">πλήρες πακέτο</span> <em class="hi-white">Υπηρεσιών Υ&amp;Α</em>',
            en: 'We provide a <span class="hi-orange">complete package</span> of <em class="hi-white">H&amp;S Services</em>',
        },
        'services.lead': {
            el: 'Από την ικανοποίηση των νομικών απαιτήσεων έως την διαμόρφωση κουλτούρας πρόληψης, ο Σταύρος Μάλλιαρης και η ομάδα του έχουν την τεχνογνωσία για να εξασφαλίσουν κορυφαίες συνθήκες Υγείας και Ασφάλειας στην επιχείρησή σας.',
            en: 'From legal compliance to building a strong prevention culture, Stavros Malliaris and his team deliver the right solutions.',
        },
        'services.legal': {
            el: 'Σύμφωνα με το Ν. 3850/2010, ακόμα και για ένα άτομο προσωπικό <strong>η επιχείρηση πρέπει να έχει Τεχνικό Ασφαλείας και ΓΕΕΚ</strong> — Νόμος 3850/2010, Άρθρο 8 &amp; 43',
            en: 'Under Law 3850/2010, even a single employee business is required to have a declared Safety Officer and a Risk Assessment — Law 3850/2010, Articles 8 &amp; 43',
        },

        'services.measlabel': { el: '6 ΥΠΗΡΕΣΙΕΣ - 100% ΙΚΑΝΟΠΟΙΗΣΗ', en: '6 SERVICES - 100% SATISFACTION' },

        's1.title': { el: 'Κάλυψη Τεχνικού Ασφαλείας', en: 'Safety Officer Coverage' },
        's1.text':  {
            el: 'Υποχρεωτική για κάθε εταιρεία σύμφωνα με το Νόμο 3850/2010, Άρθρο 8. Μηνιαίες επισκέψεις Τεχνικού Ασφαλείας στο χώρο σας για αναγνώριση κινδύνων, επίβλεψη συνθηκών εργασίας και στοχευμένες προτάσεις.',
            en: 'Mandatory for every business under Law 3850/2010, Article 8. Monthly Safety Officer visits for hazard identification, supervision of working conditions, and targeted recommendations.',
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

        's5.title': { el: 'Εκπόνηση Σχεδίων Εκκένωσης', en: 'Evacuation Plan Design' },
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
        'contact.lead': {
            el: 'Είμαστε διαθέσιμοι για κάθε ερώτηση ή ανάγκη σας. Επικοινωνήστε σήμερα συμπληρώνοντας τη φόρμα ή κλείνοντας ένα τηλεφωνικό ραντεβού 15 λεπτών.',
            en: 'We are available for any question or need. Contact us today by filling in the form or booking a 15-minute phone appointment.',
        },
        'contact.role':    { el: 'Τεχνικός Ασφαλείας — MEng, ASP®', en: 'Safety Officer — MEng, ASP®' },
        'contact.calendly':{ el: 'ΚΛΕΙΣΤΕ 📞 ΡΑΝΤΕΒΟΥ',              en: 'BOOK 📞 APPOINTMENT' },

        /* FORM */
        'form.title':          { el: 'Φόρμα επικοινωνίας',        en: 'Contact Form' },
        'form.label.name':     { el: 'Ονοματεπώνυμο',            en: 'Full Name' },
        'form.ph.name':        { el: 'Το όνομά σας',              en: 'Your name' },
        'form.label.phone':    { el: 'Τηλέφωνο',                 en: 'Phone' },
        'form.label.email':    { el: 'Email',                     en: 'Email' },
        'form.ph.email':       { el: 'email@example.gr',          en: 'email@example.com' },
        'form.label.subject':  { el: 'Αντικείμενο',              en: 'Subject' },
        'form.select.default': { el: 'Επιλέξτε υπηρεσία',        en: 'Select a service' },
        'form.opt.1':          { el: 'Κάλυψη Τεχνικού Ασφαλείας',                             en: 'Safety Officer Coverage' },
        'form.opt.2':          { el: 'ΓΕΕΚ - Γραπτή Εκτίμηση Επαγγελματικού Κινδύνου',      en: 'Occupational Risk Assessment Study (GEEK)' },
        'form.opt.3':          { el: 'Εκπαιδεύσεις Υ&Α',                                     en: 'H&S Training' },
        'form.opt.4':          { el: 'Διερεύνηση Εργατικού Ατυχήματος',                       en: 'Accident Investigation' },
        'form.opt.5':          { el: 'Σχέδια Εκκένωσης',                                      en: 'Evacuation Plans' },
        'form.opt.6':          { el: 'Προετοιμασία για Επιθεώρηση ΣΕΠΕ',                      en: 'Labour Inspectorate (SEPE) Audit Prep' },
        'form.opt.7':          { el: 'Άλλο',                                                  en: 'Other' },
        'form.label.message':  { el: 'Μήνυμα',                   en: 'Message' },
        'form.ph.message':     { el: 'Περιγράψτε σύντομα το αίτημά σας...', en: 'Briefly describe your request...' },
        'form.submit':         { el: 'Αποστολή Μηνύματος 📨',    en: 'Send Message 📨' },

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

        /* QUOTE */
        'quote.text': {
            el: '«Στόχος μας είναι η μετατροπή της ασφάλειας από τυπική υποχρέωση σε ουσιαστικό πλεονέκτημα για την επιχείρησή σας»',
            en: '"Our goal is to transform safety from a formal obligation into a real competitive advantage for your business."',
        },
        'quote.author': { el: 'Σταύρος Μάλλιαρης — Μηχανικός Υγείας και Ασφάλειας, MEng, ASP®', en: 'Stavros Malliaris — H&S Engineer, MEng, ASP®' },

        /* RESOURCES */
        'res1.title': { el: 'ΕΛΙΝΥΑΕ', en: 'ELINYAE' },
        'res1.text':  { el: 'Ελληνικό Ινστιτούτο Υγιεινής και Ασφάλειας της Εργασίας — νέες εκδόσεις, μελέτες, εκπαιδευτικό υλικό και ενημέρωση για την Υ&Α.', en: 'Hellenic Institute for Occupational Health & Safety — new publications, studies, training material and H&S updates.' },
        'res2.title': { el: 'Νόμος 3850/2010', en: 'Law 3850/2010' },
        'res2.text':  { el: 'Κωδικοποιημένο κείμενο του Ν. 3850/2010 — ο βασικός νόμος για την Υγεία και Ασφάλεια στην Εργασία στην Ελλάδα.', en: 'Consolidated text of Law 3850/2010 — the primary Greek H&S at Work legislation.' },
        'res3.title': { el: 'Επιθεώρηση Εργασίας', en: 'Labour Inspectorate' },
        'res3.text':  { el: 'Επίσημος φορέας ελέγχου εφαρμογής της εργατικής νομοθεσίας — Υποχρεώσεις εργοδότη, Ο ρόλος του Τεχνικού Ασφαλείας, Έντυπα.', en: 'Official enforcement body for labour legislation — Employer obligations, The Safety Officer role, Official forms.' },
        'res4.title': { el: 'OiRA — Εκτίμηση Κινδύνου', en: 'OiRA — Risk Assessment' },
        'res4.text':  { el: 'Διαδραστικά εργαλεία εκτίμησης επαγγελματικού κινδύνου ανά κλάδο, εκδοθέντα από το Υπ. Εργασίας & την EU-OSHA.', en: 'Interactive sector-specific occupational risk assessment tools published by the Ministry of Labour & EU-OSHA.' },
        'res5.title': { el: 'Αναγγελία Εργατικού Ατυχήματος', en: 'Workplace Accident Reporting' },
        'res5.text':  { el: 'Επίσημη διαδικασία αναγγελίας εργατικού ατυχήματος μέσω gov.gr — υποχρεώσεις εργοδότη και βήματα υποβολής.', en: 'Official workplace accident reporting process via gov.gr — employer obligations and submission steps.' },
        'res6.title': { el: 'sepenet.gr', en: 'sepenet.gr' },
        'res6.text':  { el: 'Πλατφόρμα για την online αναγγελία Τεχνικού Ασφαλείας στο ΣΕΠΕ — γρήγορη και εύκολη ηλεκτρονική διαδικασία.', en: 'Platform for online registration of Safety Officers with SEPE — quick and easy process.' },
        'res.visit':  { el: 'Επίσκεψη', en: 'Visit' },

        /* CONTACT */
        'contact.location': { el: 'Ελλάδα & Διεθνώς', en: 'Greece & Abroad' },

        /* NAME */
        'name.stavros': { el: 'Σταύρος Μάλλιαρης', en: 'Stavros Malliaris' },

        /* HOVER HINT */
        'hint.hover': { el: 'HOVER ΓΙΑ ΠΑΥΣΗ', en: 'HOVER TO PAUSE' },

        /* FOOTER */
        'footer.title': { el: 'Τεχνικός Ασφαλείας - Σύμβουλος Υγείας και Ασφάλειας', en: 'Safety Officer - H&S Consultant' },
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
