/**
 * i18n.js — Greek / English translation toggle
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
        'nav.title':    { el: 'Πολιτικός Μηχανικός',   en: 'Civil Engineer' },
        'nav.about':    { el: 'Σχετικά',                en: 'About' },
        'nav.services': { el: 'Υπηρεσίες',              en: 'Services' },
        'nav.projects': { el: 'Έργα',                   en: 'Projects' },
        'nav.contact':  { el: 'Επικοινωνία',            en: 'Contact' },

        /* HERO */
        'hero.name1':   { el: 'ΒΑΪΟΣ',                   en: 'VAIOS' },
        'hero.name2':   { el: 'ΛΙΑΠΗΣ',                  en: 'LIAPIS' },
        'hero.eyebrow': { el: 'Πολιτικός Μηχανικός ΑΠΘ', en: 'Civil Engineer — AUTH' },
        'hero.cta':     { el: 'Επικοινωνία',              en: 'Get in Touch' },

        /* MARQUEE */
        'marquee.m1': { el: 'Άμεση Αυτοψία',                    en: 'Immediate Site Inspection' },
        'marquee.m2': { el: 'Ηλεκτρονική Ταυτότητα Κτιρίου',   en: 'Building e-Identity' },
        'marquee.m3': { el: 'Νομιμοποίηση Αυθαιρέτων',         en: 'Unauthorized Structure Legalization' },
        'marquee.m4': { el: 'Ενεργειακά Πιστοποιητικά ΠΕΑ',    en: 'Energy Performance Certificates' },
        'marquee.m5': { el: 'Οικοδομικές Άδειες',               en: 'Building Permits' },
        'marquee.m6': { el: 'Διπλωματούχος Μηχανικός ΑΠΘ',     en: 'Graduate Engineer AUTH' },

        /* ABOUT */
        'about.heading': {
            el: '<em>Εμπειρία &amp; <em>Εξειδίκευση</em>',
            en: 'Experience &amp; <em>Expertise</em>',
        },
        'about.lead': {
            el: 'Διπλωματούχος Πολιτικός Μηχανικός του Αριστοτέλειου Πανεπιστημίου Θεσσαλονίκης, με <span class="years-exp"></span>+ χρόνια εμπειρία στην αντιμετώπιση πολεοδομικών, κτηματολογικών και κατασκευαστικών θεμάτων για ιδιώτες και επαγγελματίες σε όλη την Αττική.',
            en: 'Licensed Civil Engineer from the Aristotle University of Thessaloniki, with <span class="years-exp"></span>+ years of experience in urban planning, cadastral, and construction matters for individuals and professionals throughout Attica.',
        },
        'about.dim': { el: 'Αθήνα — Αττική', en: 'Athens — Attica' },

        /* FEATURES */
        'feature.timeline.label':     { el: 'Χρονοδιάγραμμα', en: 'Timeline' },
        'feature.timeline.text':      { el: 'Γρήγορη ανταπόκριση & τήρηση προθεσμιών', en: 'Fast response & strict deadline compliance' },
        'feature.transparency.label': { el: 'Διαφάνεια',       en: 'Transparency' },
        'feature.transparency.text':  { el: 'Σαφής ενημέρωση σε κάθε στάδιο',          en: 'Clear updates at every stage' },
        'feature.direct.label':       { el: 'Άμεση',           en: 'Direct' },
        'feature.direct.text':        { el: 'Εξυπηρέτηση σε ολόκληρη την Αττική',      en: 'Service across all of Attica' },

        /* SERVICES */
        'services.eyebrow': { el: 'Τι προσφέρουμε',  en: 'What we offer' },
        'services.heading': {
            el: 'Οι <em>Υπηρεσίες</em> μας',
            en: 'Our <em>Services</em>',
        },
        'service.more': { el: 'Μάθε Περισσότερα', en: 'Learn More' },

        's1.title': { el: 'Δήλωση στο Κτηματολόγιο',              en: 'Land Registry Declaration' },
        's1.text':  { el: 'Αναλαμβάνουμε την ηλεκτρονική υποβολή της δήλωσής σας ώστε η διαδικασία να ολοκληρωθεί με ορθότητα και να κατοχυρώσετε την ιδιοκτησία σας.', en: 'We handle the electronic submission of your declaration to ensure the process is completed correctly and your property ownership is fully secured.' },

        's2.title': { el: 'Πολεοδομικές Άδειες',                  en: 'Urban Planning Permits' },
        's2.text':  { el: 'Οι πολεοδομικές άδειες εκδίδονται ηλεκτρονικά. Ο μηχανικός, εξουσιοδοτημένος από τον κύριο του έργου, αναλαμβάνει ως πιστοποιημένος χρήστης όλη τη διαδικασία.', en: 'Urban planning permits are issued electronically. The engineer, authorized by the project owner, manages the entire process as a certified user.' },

        's3.title': { el: 'Μεταφορά Αυθαιρέτων στο Ν.4495/17',   en: 'Transfer of Unauthorized Structures (Law 4495/17)' },
        's3.text':  { el: 'Σύμφωνα με την ισχύουσα νομοθεσία (άρθρο 88, Ν.4495/2017), αναλαμβάνουμε τη μεταφορά αυθαίρετων κατασκευών που έχουν υπαχθεί σε παλαιότερους νόμους.', en: 'Under current legislation (Article 88, Law 4495/2017), we handle the transfer of unauthorized constructions previously registered under earlier laws.' },

        's4.title': { el: 'Βεβαιώσεις Μηχανικού Ν.4495/2017',    en: 'Engineer Certificates (Law 4495/2017)' },
        's4.text':  { el: 'Σε συμβολαιογραφικές πράξεις επί ακινήτων όπως αγοραπωλησία, μεταβίβαση, γονική παροχή, απαιτείται η βεβαίωση του μηχανικού που αναλαμβάνουμε άμεσα.', en: 'For notarial acts on properties such as sales, transfers, or parental grants, an engineer\'s certificate is required — we handle this promptly.' },

        's5.title': { el: 'Επίβλεψη Κατασκευών & Έργων',         en: 'Construction & Project Supervision' },
        's5.text':  { el: 'Ως φυσικό επακόλουθο μιας οικοδομικής άδειας, αναλαμβάνουμε την επίβλεψη της κατασκευής για την ομαλή λειτουργία του εργοταξίου.', en: 'As a natural follow-up to a building permit, we take on the supervision of the construction for smooth and efficient site operation.' },

        's6.title': { el: 'Νομιμοποίηση & Τακτοποίηση Αυθαιρέτων', en: 'Legalization & Regularization of Unauthorized Structures' },
        's6.text':  { el: 'Αναλαμβάνουμε την τακτοποίηση αυθαίρετων κατασκευών και χρήσεων σύμφωνα με τον ισχύοντα νόμο 4495/2017.', en: 'We handle the regularization of unauthorized constructions and uses in accordance with the current Law 4495/2017.' },

        's7.title': { el: 'Ηλεκτρονική Ταυτότητα Κτιρίων',       en: 'Electronic Building Identity' },
        's7.text':  { el: 'Στόχος της ΗΤΚ είναι η λεπτομερής αποτύπωση της υφιστάμενης κατάστασης κάθε κτιρίου και των οικοδομικών αδειών του για ασφαλείς μεταβιβάσεις.', en: 'The BEI aims to provide a detailed record of each building\'s current status and building permits, ensuring secure property transfers.' },

        's8.title': { el: 'Υπηρεσία Μιας Στάσης',                 en: 'One-Stop Service' },
        's8.text':  { el: 'Το γραφείο μας και οι συνεργάτες αναλαμβάνουν κάθε υπόθεση από την αρχή μέχρι το τέλος, εξασφαλίζοντας πλήρη συνέπεια και αποτελεσματικότητα.', en: 'Our office and partners handle every case from start to finish, ensuring full consistency and effectiveness.' },

        's9.title': { el: 'Ανακαινίσεις & Επισκευές & Μονώσεις',  en: 'Renovations, Repairs & Insulation' },
        's9.text':  { el: 'Η ανακαίνιση εξασφαλίζει κάλυψη λειτουργικών αναγκών και εκσυγχρονισμό των υφιστάμενων κατασκευών σύμφωνα με τις σύγχρονες απαιτήσεις.', en: 'Renovation ensures functional coverage and modernization of existing structures in line with contemporary requirements.' },

        's10.title': { el: 'Ενεργειακά Πιστοποιητικά',            en: 'Energy Performance Certificates' },
        's10.text':  { el: 'Αναλαμβάνουμε την ενεργειακή επιθεώρηση σε κτίρια κάθε χρήσης (κατοικίες, καταστήματα, ξενοδοχεία) σύμφωνα με τη νεώτερη νομοθεσία.', en: 'We carry out energy inspections for buildings of all types (residences, shops, hotels) in accordance with current legislation.' },

        's11.title': { el: 'Άδειες Λειτουργίας',                  en: 'Operating Licences' },
        's11.text':  { el: 'Αναλαμβάνουμε όλη τη διαδικασία για την επιτυχή έκδοση της άδειας λειτουργίας της επιχείρησής σας σε κάθε τύπο εμπορικής δραστηριότητας.', en: 'We handle the entire process for successfully obtaining the operating licence for your business across all commercial activity types.' },

        's12.title': { el: 'Τοπογραφικά Διαγράμματα',             en: 'Topographic Diagrams' },
        's12.text':  { el: 'Σχέδιο που αναπαριστά το περίγραμμα του κτιρίου και τα όρια του οικοπέδου με ακριβείς συντεταγμένες στο Ελληνικό Γεωδαιτικό Σύστημα Αναφοράς.', en: 'A plan depicting the building outline and plot boundaries with precise coordinates in the Greek Geodetic Reference System.' },

        /* PROJECTS */
        'projects.eyebrow': { el: 'Το χαρτοφυλάκιό μας',   en: 'Our Portfolio' },
        'projects.heading': {
            el: 'Επιλεγμένα <em>Έργα</em>',
            en: 'Selected <em>Projects</em>',
        },
        'p1.cat':   { el: 'Ηλεκτρονική Ταυτότητα',      en: 'Electronic Identity' },
        'p1.title': { el: 'Κατοικία Αθήνα',              en: 'Residence Athens' },
        'p1.desc':  { el: 'Πλήρης ΗΤΚ & βεβαίωση μηχανικού για μεταβίβαση', en: 'Full BEI & engineer\'s certificate for property transfer' },

        'p2.cat':   { el: 'Οικοδομική Άδεια',            en: 'Building Permit' },
        'p2.title': { el: 'Νέα Κατασκευή Πειραιάς',      en: 'New Construction Piraeus' },
        'p2.desc':  { el: 'Αρχιτεκτονική μελέτη & αδειοδότηση', en: 'Architectural study & permit approval' },

        'p3.cat':   { el: 'Τακτοποίηση Αυθαίρετου',     en: 'Unauthorized Structure Settlement' },
        'p3.title': { el: 'Μονοκατοικία Γλυφάδα',        en: 'Detached House Glyfada' },
        'p3.desc':  { el: 'Νομιμοποίηση κατά Ν.4495/2017', en: 'Legalization under Law 4495/2017' },

        'p4.cat':   { el: 'Ενεργειακό Πιστοποιητικό',   en: 'Energy Certificate' },
        'p4.title': { el: 'Εμπορικό Κτίριο Μαρούσι',    en: 'Commercial Building Maroussi' },
        'p4.desc':  { el: 'ΠΕΑ & ενεργειακή αναβάθμιση', en: 'EPC & energy upgrade' },

        'p5.cat':   { el: 'Scan to BIM',                 en: 'Scan to BIM' },
        'p5.title': { el: 'Βιομηχανικό Κτίριο Ελαιώνας', en: 'Industrial Building Eleonas' },
        'p5.desc':  { el: '3D Laser Scanning & ψηφιακή αποτύπωση', en: '3D Laser Scanning & digital survey' },

        'p6.cat':   { el: 'Ανακαίνιση',                  en: 'Renovation' },
        'p6.title': { el: 'Διαμέρισμα Κολωνάκι',         en: 'Apartment Kolonaki' },
        'p6.desc':  { el: 'Πλήρης ανακαίνιση & επίβλεψη', en: 'Full renovation & supervision' },

        /* CONTACT */
        'contact.eyebrow': { el: 'Επικοινωνία', en: 'Contact' },
        'contact.heading': {
            el: 'Μιλήστε <em>μαζί μας</em>',
            en: 'Let\'s <em>talk</em>',
        },
        'contact.lead': {
            el: 'Είμαστε εδώ για κάθε ερώτηση ή ανάγκη. Επικοινωνήστε μαζί μας σήμερα για δωρεάν αρχική ενημέρωση.',
            en: 'We\'re here for any question or need. Get in touch today for a free initial consultation.',
        },
        'contact.role': { el: 'Πολιτικός Μηχανικός ΑΠΘ', en: 'Civil Engineer AUTH' },

        /* FORM */
        'form.title':          { el: 'Στείλτε μήνυμα',        en: 'Send a Message' },
        'form.label.name':     { el: 'Ονοματεπώνυμο',         en: 'Full Name' },
        'form.ph.name':        { el: 'Το όνομά σας',           en: 'Your name' },
        'form.label.phone':    { el: 'Τηλέφωνο',              en: 'Phone' },
        'form.label.email':    { el: 'Email',                  en: 'Email' },
        'form.ph.email':       { el: 'email@example.gr',       en: 'email@example.com' },
        'form.label.subject':  { el: 'Αντικείμενο',           en: 'Subject' },
        'form.select.default': { el: 'Επιλέξτε υπηρεσία',     en: 'Select a service' },
        'form.opt.1':          { el: 'Ηλεκτρονική Ταυτότητα Κτιρίου', en: 'Building e-Identity' },
        'form.opt.2':          { el: 'Νομιμοποίηση Αυθαιρέτων',       en: 'Unauthorized Structure Legalization' },
        'form.opt.3':          { el: 'Ενεργειακό Πιστοποιητικό (ΠΕΑ)', en: 'Energy Performance Certificate (EPC)' },
        'form.opt.4':          { el: 'Οικοδομική Άδεια',               en: 'Building Permit' },
        'form.opt.5':          { el: 'Άλλο',                           en: 'Other' },
        'form.label.message':  { el: 'Μήνυμα',                en: 'Message' },
        'form.ph.message':     { el: 'Περιγράψτε σύντομα το αίτημά σας...', en: 'Briefly describe your request...' },
        'form.submit':         { el: 'Αποστολή Μηνύματος',    en: 'Send Message' },

        /* FOOTER */
        'footer.title': { el: 'Διπλωματούχος Πολιτικός Μηχανικός ΑΠΘ', en: 'Graduate Civil Engineer AUTH' },
        'footer.copy': {
            el: '&copy; 2026 Βάϊος Λιάπης &mdash; Πολιτικός Μηχανικός Αθήνα',
            en: '&copy; 2026 Vaios Liapis &mdash; Civil Engineer Athens',
        },
        'footer.design': {
            el: 'Σχεδιασμός <span class="design-brand">Design Expertease</span>',
            en: 'Designed by <span class="design-brand">Design Expertease</span>',
        },
    };

    /* ─── STATE ──────────────────────────────────────────────────────────── */
    let currentLang = localStorage.getItem('lang') || 'el';

    /* ─── YEARS OF EXPERIENCE (dynamic) ─────────────────────────────────── */
    const EXP_START_YEAR = 2019;
    function fillYearsExp() {
        var years = new Date().getFullYear() - EXP_START_YEAR;
        document.querySelectorAll('.years-exp').forEach(function (el) {
            el.textContent = years;
        });
    }

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

        /* re-fill dynamic years after innerHTML replacement */
        fillYearsExp();
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
    /* Apply on DOM ready — handles page reload with saved preference */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () { applyLang(currentLang); });
    } else {
        applyLang(currentLang);
    }

})();
