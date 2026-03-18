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
        'nav.title':    { el: 'Τεχνικός Ασφαλείας',          en: 'Safety Officer' },
        'nav.about':    { el: 'Σχετικά',                      en: 'About' },
        'nav.services': { el: 'Υπηρεσίες',                    en: 'Services' },
        'nav.sectors':  { el: 'Τομείς',                       en: 'Sectors' },
        'nav.contact':  { el: 'Επικοινωνία',                  en: 'Contact' },

        /* HERO */
        'hero.name1':    { el: 'ΣΤΑΥΡΟΣ',                                      en: 'STAVROS' },
        'hero.name2':    { el: 'ΜΑΛΛΙΑΡΗΣ',                                    en: 'MALLIARIS' },
        'hero.eyebrow':  { el: 'Μηχανικός Υγείας & Ασφάλειας ΑΠΘ',            en: 'H&S Engineer — AUTH' },
        'hero.cta':      { el: 'Επικοινωνία',                                  en: 'Get in Touch' },
        'hero.stat1.num':{ el: '7+',                                            en: '7+' },
        'hero.stat1.lbl':{ el: 'χρόνια εμπειρίας',                             en: 'years experience' },
        'hero.stat2.num':{ el: 'ASP®',                                          en: 'ASP®' },
        'hero.stat2.lbl':{ el: 'πιστοποίηση',                                  en: 'certification' },
        'hero.stat3.num':{ el: 'ΑΠΘ',                                          en: 'AUTH' },
        'hero.stat3.lbl':{ el: 'πολ. μηχανικός',                               en: 'civil engineer' },

        /* MARQUEE */
        'marquee.m1': { el: 'Τεχνικός Ασφαλείας',                    en: 'Safety Officer' },
        'marquee.m2': { el: 'Εκτίμηση Επαγγελματικού Κινδύνου',      en: 'Risk Assessment (ΓΕΕΚ)' },
        'marquee.m3': { el: 'Σχέδια Εκκένωσης',                      en: 'Evacuation Plans' },
        'marquee.m4': { el: 'Εκπαιδεύσεις Υ&Α',                     en: 'H&S Training' },
        'marquee.m5': { el: 'ASP® Certified',                        en: 'ASP® Certified' },
        'marquee.m6': { el: 'Πολιτικός Μηχανικός ΑΠΘ',              en: 'Civil Engineer AUTH' },

        /* ABOUT */
        'about.eyebrow': { el: 'Σχετικά με εμένα',  en: 'About Me' },
        'about.heading': {
            el: 'Εμπειρία &amp; <em>Εξειδίκευση</em>',
            en: 'Experience &amp; <em>Expertise</em>',
        },
        'about.lead': {
            el: 'Πιστοποιημένος Επαγγελματίας Υγείας και Ασφάλειας στην Εργασία, με σπουδές Πολιτικού Μηχανικού ΑΠΘ και πάνω από 7 χρόνια διεθνούς εμπειρίας, παρέχοντας ολοκληρωμένες υπηρεσίες πρόληψης και συμμόρφωσης σε επιχειρήσεις κάθε μεγέθους.<br><br>Αποτελεσματική υποστήριξη κάθε τύπου επιχείρησης, από εστιατόρια, καταστήματα και γραφεία, μέχρι εταιρείες παροχής υπηρεσιών, βιομηχανικές εγκαταστάσεις και εργοτάξια.',
            en: 'Certified Occupational Health & Safety professional, with a Civil Engineering background from AUTH and over 7 years of international experience delivering comprehensive prevention and compliance services to businesses of every size.<br><br>Effective support for all business types — from restaurants, shops and offices to service companies, industrial facilities and construction sites.',
        },
        'about.dim': { el: 'Ελλάδα — Διεθνώς', en: 'Greece — International' },

        /* FEATURES */
        'feature.risk.label':        { el: 'Αξιολόγηση Κινδύνου',          en: 'Risk Assessment' },
        'feature.risk.text':         { el: 'Αναγνώριση κινδύνων & πρακτικές λύσεις που λειτουργούν στην πράξη', en: 'Hazard identification & practical solutions that work in the field' },
        'feature.custom.label':      { el: 'Εξατομικευμένη Προσέγγιση',    en: 'Tailored Approach' },
        'feature.custom.text':       { el: 'Εξατομικευμένη αξιολόγηση, προσαρμοσμένες λύσεις ανά μέγεθος επιχείρησης', en: 'Individual assessment, solutions adapted to your business size' },
        'feature.compliance.label':  { el: 'Νομική Κάλυψη',                en: 'Legal Compliance' },
        'feature.compliance.text':   { el: 'Εχεμύθεια, σαφής επικοινωνία με διοίκηση και προσωπικό', en: 'Confidentiality, clear communication with management and staff' },

        /* SERVICES */
        'services.eyebrow': { el: 'Τι προσφέρω',  en: 'What I offer' },
        'services.heading': {
            el: 'Οι <em>Υπηρεσίες</em> μου',
            en: 'My <em>Services</em>',
        },

        's1.title': { el: 'Κάλυψη Τεχνικού Ασφαλείας',         en: 'Safety Officer Coverage' },
        's1.text':  {
            el: 'Υποχρεωτική κατά Ν. 3850/2010, Άρθρο 8. Μηνιαίες επισκέψεις για αναγνώριση κινδύνων, επίβλεψη συνθηκών εργασίας και στοχευμένες προτάσεις.',
            en: 'Mandatory under Law 3850/2010, Article 8. Monthly visits for hazard identification, supervision of working conditions, and targeted recommendations.',
        },

        's2.title': { el: 'ΓΕΕΚ',                               en: 'Risk Assessment Study' },
        's2.text':  {
            el: 'Υποχρεωτική κατά Ν. 3850/2010, Άρθρο 43. Εκπόνηση μελέτης για την εκτίμηση επαγγελματικού κινδύνου ανάλογα με τη δραστηριότητα και τις θέσεις εργασίας.',
            en: 'Mandatory under Law 3850/2010, Article 43. Preparation of the occupational risk assessment study based on the activity and job positions.',
        },

        's3.title': { el: 'Εκπαιδεύσεις Υ&Α',                  en: 'H&S Training' },
        's3.text':  {
            el: 'Ανάλογα με τις ανάγκες της κάθε επιχείρησης, παρέχουμε ευρύ φάσμα εκπαιδεύσεων για εργαζόμενους κατά Ν. 3850/2010, Άρθρο 48.',
            en: 'Tailored to the needs of each business, we provide a wide range of employee training programmes under Law 3850/2010, Article 48.',
        },

        's4.title': { el: 'Διερεύνηση Εργατικών Ατυχημάτων',   en: 'Workplace Accident Investigation' },
        's4.text':  {
            el: 'Root Cause Analysis, προτάσεις διορθωτικών ενεργειών και σύνταξη έκθεσης ατυχήματος με εχεμύθεια και επαγγελματισμό.',
            en: 'Root Cause Analysis, corrective action recommendations and accident report preparation with full confidentiality and professionalism.',
        },

        's5.title': { el: 'Σχέδια Εκκένωσης',                  en: 'Evacuation Plans' },
        's5.text':  {
            el: 'Μελέτη, σχεδιασμός και αποτύπωση Σχεδίων Διαφυγής και Εκκένωσης για συμμόρφωση με την Πυροσβεστική Υπηρεσία.',
            en: 'Study, design and documentation of Escape and Evacuation Plans for compliance with the Fire Service requirements.',
        },

        's6.title': { el: 'Προετοιμασία ΣΕΠΕ',                 en: 'Labour Inspectorate Preparation' },
        's6.text':  {
            el: 'Έλεγχος του φακέλου Υ&Α για διαπίστωση συμμόρφωσης με την ισχύουσα νομοθεσία και πρόταση διορθωτικών ενεργειών.',
            en: 'Review of the H&S file to verify compliance with current legislation and proposal of corrective actions.',
        },

        /* SECTORS */
        'sectors.eyebrow': { el: 'Κλάδοι δραστηριότητας',  en: 'Activity Sectors' },
        'sectors.heading': {
            el: 'Τομείς <em>Εξειδίκευσης</em>',
            en: 'Sectors of <em>Specialisation</em>',
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
            el: 'Μιλήστε <em>μαζί μου</em>',
            en: 'Let\'s <em>talk</em>',
        },
        'contact.lead': {
            el: 'Είμαι εδώ για κάθε ερώτηση ή ανάγκη. Επικοινωνήστε σήμερα για δωρεάν αρχική ενημέρωση ή κλείστε ραντεβού 15 λεπτών.',
            en: 'I\'m here for any question or need. Get in touch today for a free initial consultation or book a 15-minute appointment.',
        },
        'contact.role':    { el: 'Μηχανικός Υγείας & Ασφάλειας ΑΠΘ, MEng, ASP®', en: 'H&S Engineer AUTH, MEng, ASP®' },
        'contact.calendly':{ el: 'Κλείστε Ραντεβού',                               en: 'Book an Appointment' },

        /* FORM */
        'form.title':          { el: 'Στείλτε μήνυμα',           en: 'Send a Message' },
        'form.label.name':     { el: 'Ονοματεπώνυμο',            en: 'Full Name' },
        'form.ph.name':        { el: 'Το όνομά σας',              en: 'Your name' },
        'form.label.phone':    { el: 'Τηλέφωνο',                 en: 'Phone' },
        'form.label.email':    { el: 'Email',                     en: 'Email' },
        'form.ph.email':       { el: 'email@example.gr',          en: 'email@example.com' },
        'form.label.subject':  { el: 'Αντικείμενο',              en: 'Subject' },
        'form.select.default': { el: 'Επιλέξτε υπηρεσία',        en: 'Select a service' },
        'form.opt.1':          { el: 'Κάλυψη Τεχνικού Ασφαλείας',               en: 'Safety Officer Coverage' },
        'form.opt.2':          { el: 'ΓΕΕΚ — Εκτίμηση Επαγγελματικού Κινδύνου', en: 'Risk Assessment Study (ΓΕΕΚ)' },
        'form.opt.3':          { el: 'Εκπαιδεύσεις Υ&Α',                        en: 'H&S Training' },
        'form.opt.4':          { el: 'Διερεύνηση Εργατικού Ατυχήματος',          en: 'Accident Investigation' },
        'form.opt.5':          { el: 'Σχέδια Εκκένωσης',                         en: 'Evacuation Plans' },
        'form.opt.6':          { el: 'Προετοιμασία ΣΕΠΕ',                        en: 'Labour Inspectorate Prep' },
        'form.opt.7':          { el: 'Άλλο',                                     en: 'Other' },
        'form.label.message':  { el: 'Μήνυμα',                   en: 'Message' },
        'form.ph.message':     { el: 'Περιγράψτε σύντομα το αίτημά σας...', en: 'Briefly describe your request...' },
        'form.submit':         { el: 'Αποστολή Μηνύματος',       en: 'Send Message' },

        /* GAUGE */
        'gauge.label': { el: 'Συμμόρφωση', en: 'Compliance' },

        /* CHECKLIST */
        'cl.item1': { el: 'ΓΕΕΚ εκπονημένο',              en: 'Risk assessment completed' },
        'cl.item2': { el: 'Εκπαίδευση εργαζομένων',       en: 'Employee training done' },
        'cl.item3': { el: 'Σχέδιο εκκένωσης',             en: 'Evacuation plan in place' },
        'cl.item4': { el: 'Σήμανση ασφαλείας',            en: 'Safety signage installed' },
        'cl.item5': { el: 'Ν.3850/2010 συμμόρφωση',       en: 'Law 3850/2010 compliant' },

        /* SECTOR CARDS */
        'sec1.title': { el: 'Κατασκευές',             en: 'Construction' },
        'sec1.text':  { el: 'Εργοτάξια, ανακαινίσεις, τεχνικά έργα — πλήρης Υ&Α κάλυψη.', en: 'Construction sites, renovations, infrastructure — full H&S coverage.' },
        'sec2.title': { el: 'Βιομηχανία',             en: 'Industry' },
        'sec2.text':  { el: 'Εργοστάσια, αποθήκες, παραγωγικές μονάδες υψηλού κινδύνου.', en: 'Factories, warehouses, high-risk production units.' },
        'sec3.title': { el: 'Λιανικό Εμπόριο',       en: 'Retail' },
        'sec3.text':  { el: 'Καταστήματα, εμπορικά κέντρα, logistics — ασφάλεια πελατών & προσωπικού.', en: 'Shops, shopping centres, logistics — customer & staff safety.' },
        'sec4.title': { el: 'Φιλοξενία',             en: 'Hospitality' },
        'sec4.text':  { el: 'Ξενοδοχεία, εστιατόρια, τουριστικές εγκαταστάσεις — HACCP & πυρασφάλεια.', en: 'Hotels, restaurants, tourist facilities — HACCP & fire safety.' },
        'sec5.title': { el: 'Υγειονομικές Μονάδες', en: 'Healthcare' },
        'sec5.text':  { el: 'Κλινικές, ιατρεία, εργαστήρια — βιολογικοί & χημικοί κίνδυνοι.', en: 'Clinics, practices, labs — biological & chemical hazards.' },
        'sec6.title': { el: 'Ναυτιλία & Λιμάνια',   en: 'Maritime & Ports' },
        'sec6.text':  { el: 'Πλοία, λιμενικές εγκαταστάσεις — διεθνή πρότυπα ISM & ISPS.', en: 'Vessels, port facilities — international ISM & ISPS standards.' },

        /* IN ACTION */
        'action.eyebrow': { el: 'Στη Δράση',       en: 'In the Field' },
        'action.heading': {
            el: 'Εικόνες <em>Πεδίου</em>',
            en: 'Field <em>Photos</em>',
        },
        'action.cap1': { el: 'Επιθεώρηση Ασφαλείας Εργοταξίου', en: 'Construction Site Safety Inspection' },
        'action.cap2': { el: 'Εκπαίδευση &amp; Αξιολόγηση Κινδύνου', en: 'Training &amp; Risk Assessment' },

        /* QUOTE */
        'quote.text': {
            el: '"Η ασφάλεια δεν είναι δαπάνη — είναι επένδυση στους ανθρώπους σας."',
            en: '"Safety is not a cost — it is an investment in your people."',
        },

        /* RESOURCES */
        'res1.title': { el: 'Οδηγός ΓΕΕΚ',                    en: 'Risk Assessment Guide' },
        'res1.text':  { el: 'Βήμα-βήμα οδηγίες για εκπόνηση Γραπτής Εκτίμησης Επαγγελματικού Κινδύνου.', en: 'Step-by-step guide for preparing a Written Occupational Risk Assessment.' },
        'res2.title': { el: 'Checklist Ασφαλείας Εργοταξίου', en: 'Construction Site Safety Checklist' },
        'res2.text':  { el: 'Πρακτική λίστα ελέγχου για εβδομαδιαίες επιθεωρήσεις εργοταξίου.', en: 'Practical checklist for weekly construction site inspections.' },
        'res3.title': { el: 'Εγχειρίδιο Εκπαίδευσης ΜΑΠ',   en: 'PPE Training Manual' },
        'res3.text':  { el: 'Πλήρες εγχειρίδιο επιλογής & ορθής χρήσης Μέσων Ατομικής Προστασίας.', en: 'Complete manual for selecting & correctly using Personal Protective Equipment.' },
        'res.soon':   { el: 'Σύντομα', en: 'Coming Soon' },

        /* CONTACT */
        'contact.location': { el: 'Ελλάδα & Διεθνώς', en: 'Greece & International' },

        /* FOOTER */
        'footer.title': { el: 'Μηχανικός Υγείας & Ασφάλειας ΑΠΘ', en: 'H&S Engineer AUTH' },
    };

    /* ─── STATE ──────────────────────────────────────────────────────────── */
    let currentLang = localStorage.getItem('lang') || 'el';

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
