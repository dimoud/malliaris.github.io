/**
 * consent.js — συγκατάθεση cookies (Consent Mode v2) + Google Analytics 4 + συμβάντα
 * Μάλλιαρης & Συνεργάτες
 *
 * - Προεπιλογή: άρνηση και στα 4 σήματα. Το gtag.js ΔΕΝ κατεβαίνει πριν από το «Αποδοχή».
 * - Η «Αποδοχή» δίνει μόνο analytics_storage (η μπάρα μιλά μόνο για cookies ανάλυσης).
 * - Ανάκληση: κάθε στοιχείο με data-cc-open ξανανοίγει τη μπάρα (άρθρο 7§3 GDPR).
 * - window.ccEvent(name, params): πριν τη συγκατάθεση τα συμβάντα μπαίνουν σε ουρά,
 *   μετά από άρνηση πετιούνται.
 * - Αυτόματα συμβάντα: click_tel, click_email, book_call (Calendly).
 *   Τα generate_lead / quiz_complete / quiz_cta τα στέλνουν contact-form.js και quiz.js.
 */
(function () {
    'use strict';

    var GA_ID = 'G-W7HGV18VNJ';
    var KEY = 'cookie_consent';          /* ίδιο κλειδί με την παλιά μπάρα: κρατά τις επιλογές που έχουν ήδη γίνει */

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    gtag('consent', 'default', {
        analytics_storage: 'denied',
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied'
    });

    function sget() { try { return window.localStorage.getItem(KEY); } catch (e) { return null; } }
    function sset(v) { try { window.localStorage.setItem(KEY, v); } catch (e) { /* ιδιωτική περιήγηση */ } }

    var queue = [];
    var gaLoaded = false;

    function loadGA() {
        if (gaLoaded) return;
        gaLoaded = true;
        gtag('consent', 'update', { analytics_storage: 'granted' });
        var s = document.createElement('script');
        s.async = true;
        s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
        document.head.appendChild(s);
        gtag('js', new Date());
        gtag('config', GA_ID);
        while (queue.length) { var ev = queue.shift(); gtag('event', ev.name, ev.params); }
    }

    window.ccEvent = function (name, params) {
        var st = sget();
        if (st === 'accepted') { loadGA(); gtag('event', name, params || {}); }
        else if (st !== 'rejected') { queue.push({ name: name, params: params || {} }); }
    };

    var TXT = {
        el: {
            text: 'Χρησιμοποιούμε cookies του Google Analytics μόνο για να καταλαβαίνουμε πώς χρησιμοποιείται ο ιστότοπος. Δεν μοιραζόμαστε δεδομένα σας με τρίτους για διαφήμιση.',
            more: 'Πολιτική απορρήτου',
            accept: 'Αποδοχή',
            reject: 'Απόρριψη',
            aria: 'Ρυθμίσεις cookies'
        },
        en: {
            text: 'We use Google Analytics cookies only to understand how the website is used. We do not share your data with third parties for advertising.',
            more: 'Privacy policy',
            accept: 'Accept',
            reject: 'Reject',
            aria: 'Cookie settings'
        }
    };

    function lang() { return (document.documentElement.lang || 'el').slice(0, 2) === 'en' ? 'en' : 'el'; }

    /* διαδρομή προς τη ρίζα του ιστότοπου, από τη θέση του consent.js */
    var ROOT = (document.currentScript && document.currentScript.src || '').replace(/[^\/]*$/, '');

    function buildBanner() {
        var b = document.getElementById('cookie-banner');
        if (b) return b;
        var t = TXT[lang()];
        var privacy = ROOT + (lang() === 'en' ? 'en/privacy/' : 'aporrito/');
        b = document.createElement('div');
        b.id = 'cookie-banner';
        b.setAttribute('role', 'region');
        b.setAttribute('aria-label', t.aria);
        b.innerHTML =
            '<p>' + t.text + ' <a href="' + privacy + '">' + t.more + '</a></p>' +
            '<div class="cookie-buttons">' +
            '<button type="button" id="cookie-accept">' + t.accept + '</button>' +
            '<button type="button" id="cookie-reject">' + t.reject + '</button>' +
            '</div>';
        document.body.appendChild(b);
        b.querySelector('#cookie-accept').addEventListener('click', function () {
            sset('accepted'); b.style.display = 'none'; loadGA();
        });
        b.querySelector('#cookie-reject').addEventListener('click', function () {
            sset('rejected'); b.style.display = 'none'; queue.length = 0;
        });
        return b;
    }

    function init() {
        var st = sget();
        if (st === 'accepted') loadGA();
        else if (st !== 'rejected') buildBanner().style.display = 'flex';

        document.addEventListener('click', function (e) {
            var el = e.target.closest ? e.target.closest('a, [data-cc-open]') : null;
            if (!el) return;
            if (el.hasAttribute('data-cc-open')) {
                e.preventDefault();
                buildBanner().style.display = 'flex';
                return;
            }
            var href = el.getAttribute('href') || '';
            if (href.indexOf('tel:') === 0) window.ccEvent('click_tel', { link_url: href, page_path: location.pathname });
            else if (href.indexOf('mailto:') === 0) window.ccEvent('click_email', { page_path: location.pathname });
            else if (href.indexOf('calendly.com') !== -1) window.ccEvent('book_call', { page_path: location.pathname });
        }, { passive: false });
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
})();
