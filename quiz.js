/**
 * quiz.js — Safety Self-Assessment Quiz
 * Step-by-step Yes/No questionnaire with image, progress bar, and result.
 */

(function () {
    'use strict';

    var QUESTIONS = [
        {
            el: 'Έχετε εκπονήσει Γραπτή Εκτίμηση Επαγγελματικού Κινδύνου (ΓΕΕΚ);',
            en: 'Do you have a Written Occupational Risk Assessment (GEEK)?',
            img: 'Risk Assessment.png',
            pts: 20
        },
        {
            el: 'Εκπαιδεύονται τακτικά οι εργαζόμενοι σε θέματα Υγείας & Ασφάλειας;',
            en: 'Are employees regularly trained on Health & Safety topics?',
            img: 'Training.jpg',
            pts: 20
        },
        {
            el: 'Διαθέτουν οι εργαζόμενοι κατάλληλα ΜΑΠ (Μέσα Ατομικής Προστασίας);',
            en: 'Do employees have appropriate PPE (Personal Protective Equipment)?',
            img: 'PPE.jpg',
            pts: 20
        },
        {
            el: 'Υπάρχει σήμανση ασφαλείας σε όλους τους χώρους εργασίας;',
            en: 'Is safety signage displayed throughout all work areas?',
            img: 'Signage.jpg',
            pts: 20
        },
        {
            el: 'Γνωρίζετε τις υποχρεώσεις σας βάσει του Ν. 3850/2010;',
            en: 'Are you aware of your obligations under Law N.3850/2010?',
            img: 'N.3850.png',
            pts: 20
        }
    ];

    var RESULTS = {
        el: [
            { min: 0,   max: 20,  verdict: 'Υψηλός Κίνδυνος',          color: '#E8541A', msg: 'Η επιχείρησή σας εκτίθεται σε σημαντικό νομικό και λειτουργικό κίνδυνο. Χρειάζεστε άμεση υποστήριξη.' },
            { min: 21,  max: 40,  verdict: 'Χρειάζεται Βελτίωση',        color: '#F09030', msg: 'Υπάρχουν σοβαρά κενά στην ασφάλειά σας. Ένα πλάνο δράσης μπορεί να αλλάξει τα πράγματα γρήγορα.' },
            { min: 41,  max: 60,  verdict: 'Μέτρια Συμμόρφωση',          color: '#F09030', msg: 'Έχετε κάνει βήματα προς τη σωστή κατεύθυνση, αλλά υπάρχουν ακόμα σημαντικά κενά.' },
            { min: 61,  max: 80,  verdict: 'Καλή Πρόοδος',               color: '#2DAA6E', msg: 'Η επιχείρησή σας είναι σε καλό δρόμο. Μικρές βελτιώσεις μπορούν να σας φέρουν σε πλήρη συμμόρφωση.' },
            { min: 81,  max: 100, verdict: 'Εξαιρετική Συμμόρφωση!',     color: '#2DAA6E', msg: 'Μπράβο! Η ασφάλεια είναι προτεραιότητά σας. Επικοινωνήστε μαζί μας για να διατηρήσετε αυτό το επίπεδο.' }
        ],
        en: [
            { min: 0,   max: 20,  verdict: 'High Risk',                  color: '#E8541A', msg: 'Your business faces significant legal and operational risk. You need immediate support.' },
            { min: 21,  max: 40,  verdict: 'Needs Improvement',           color: '#F09030', msg: 'There are serious gaps in your safety compliance. An action plan can change things quickly.' },
            { min: 41,  max: 60,  verdict: 'Moderate Compliance',         color: '#F09030', msg: 'You\'ve taken steps in the right direction, but significant gaps remain.' },
            { min: 61,  max: 80,  verdict: 'Good Progress',               color: '#2DAA6E', msg: 'Your business is on the right track. Small improvements can bring you to full compliance.' },
            { min: 81,  max: 100, verdict: 'Excellent Compliance!',       color: '#2DAA6E', msg: 'Well done! Safety is your priority. Contact us to maintain this level.' }
        ]
    };

    var YES_LABEL = { el: 'Ναι', en: 'Yes' };
    var NO_LABEL  = { el: 'Όχι', en: 'No'  };
    var STEP_OF   = { el: 'Ερώτηση', en: 'Question' };
    var OF_LABEL  = { el: 'από', en: 'of' };

    var current = 0;
    var answers = []; // true = yes, false = no

    function getLang() {
        if (window.I18n && typeof window.I18n.getLang === 'function') return window.I18n.getLang();
        return 'el';
    }

    function $(id) { return document.getElementById(id); }

    function getScore() {
        var total = 0;
        answers.forEach(function (a, i) {
            if (a && QUESTIONS[i]) total += QUESTIONS[i].pts;
        });
        return Math.min(total, 100);
    }

    function getResult(score, lang) {
        var list = RESULTS[lang] || RESULTS.el;
        for (var i = list.length - 1; i >= 0; i--) {
            if (score >= list[i].min) return list[i];
        }
        return list[0];
    }

    function animateRing(circleEl, pct, circumference) {
        var offset = circumference * (1 - pct / 100);
        circleEl.style.strokeDashoffset = offset;
    }

    function updateProgressSteps() {
        var steps = document.querySelectorAll('.sqz-step-dot');
        steps.forEach(function (dot, i) {
            dot.classList.remove('done-yes', 'done-no', 'active');
            if (i < answers.length) {
                dot.classList.add(answers[i] ? 'done-yes' : 'done-no');
                dot.textContent = answers[i] ? '✓' : '✗';
            } else if (i === current) {
                dot.classList.add('active');
                dot.textContent = i + 1;
            } else {
                dot.textContent = i + 1;
            }
        });
    }

    function updateScorePreview() {
        var score = getScore();
        var ringFill = $('sqzRingFill');
        var pctEl = $('sqzScorePct');
        if (ringFill) animateRing(ringFill, score, 201.06);
        if (pctEl) pctEl.textContent = score + '%';

        var color = score >= 60 ? '#2DAA6E' : score >= 40 ? '#F09030' : '#E8541A';
        if (ringFill) ringFill.style.stroke = color;
    }

    function renderQuestion(idx) {
        var lang = getLang();
        var q = QUESTIONS[idx];
        var total = QUESTIONS.length;

        /* Step label */
        var stepEl = $('sqzStepLabel');
        if (stepEl) stepEl.textContent = STEP_OF[lang] + ' ' + (idx + 1) + ' ' + OF_LABEL[lang] + ' ' + total;

        /* Image */
        var img = $('sqzQImg');
        if (img) {
            img.onload = null;
            img.style.transition = 'none';
            img.style.opacity = '0';
            img.style.objectPosition = (idx === 2) ? 'center center' : 'top center';
            img.src = q.img;
            img.alt = q[lang];
            setTimeout(function () {
                img.style.transition = 'opacity 0.3s ease';
                img.style.opacity = '1';
            }, 50);
        }

        /* Question text */
        var textEl = $('sqzQText');
        if (textEl) textEl.textContent = q[lang];

        /* Options */
        var opts = $('sqzOptions');
        if (opts) {
            opts.innerHTML = '';
            var btnYes = document.createElement('button');
            btnYes.className = 'sqz-option-btn';
            btnYes.textContent = '✔  ' + YES_LABEL[lang];
            btnYes.onclick = function () { answer(true); };

            var btnNo = document.createElement('button');
            btnNo.className = 'sqz-option-btn';
            btnNo.textContent = '✘  ' + NO_LABEL[lang];
            btnNo.onclick = function () { answer(false); };

            opts.appendChild(btnYes);
            opts.appendChild(btnNo);
        }

        /* Progress bar */
        var fill = $('sqzProgressFill');
        var label = $('sqzProgressLabel');
        var answered = answers.length;
        if (fill) fill.style.width = (answered / total * 100) + '%';
        if (label) label.textContent = answered + ' ' + OF_LABEL[lang] + ' ' + total;

        updateProgressSteps();
        updateScorePreview();
    }

    function answer(isYes) {
        answers[current] = isYes;

        /* Flash selection */
        var opts = $('sqzOptions');
        if (opts) {
            var btns = opts.querySelectorAll('.sqz-option-btn');
            btns[isYes ? 0 : 1].classList.add(isYes ? 'selected-yes' : 'selected-no');
        }

        updateScorePreview();
        updateProgressSteps();

        setTimeout(function () {
            current++;
            if (current < QUESTIONS.length) {
                renderQuestion(current);
            } else {
                showResult();
            }
        }, 400);
    }

    function buildProgressDots() {
        var container = $('sqzProgressSteps');
        if (!container) return;
        container.innerHTML = '';
        QUESTIONS.forEach(function (_, i) {
            var dot = document.createElement('div');
            dot.className = 'sqz-step-dot' + (i === 0 ? ' active' : '');
            dot.textContent = i + 1;
            container.appendChild(dot);
        });
    }

    function showResult() {
        var lang = getLang();
        var score = getScore();
        var res = getResult(score, lang);

        /* Progress bar to 100% */
        var fill = $('sqzProgressFill');
        var label = $('sqzProgressLabel');
        var total = QUESTIONS.length;
        if (fill) fill.style.width = '100%';
        if (label) label.textContent = total + ' ' + OF_LABEL[lang] + ' ' + total;
        updateProgressSteps();

        setTimeout(function () {
            $('sqzGame').style.display = 'none';

            var resultEl = $('sqzResult');
            resultEl.style.display = 'flex';

            $('sqzResultPct').textContent = score + '%';
            $('sqzResultVerdict').textContent = res.verdict;
            $('sqzResultVerdict').style.color = res.color;
            $('sqzResultMsg').textContent = res.msg;

            var ring = $('sqzResultRing');
            if (ring) {
                ring.style.stroke = res.color;
                setTimeout(function () {
                    animateRing(ring, score, 314.16);
                }, 100);
            }
        }, 300);
    }

    window.SQZ = {
        start: function () {
            current = 0;
            answers = [];

            var intro = $('sqzIntro');
            var game  = $('sqzGame');

            intro.style.opacity = '0';
            intro.style.transform = 'translateY(-8px)';

            setTimeout(function () {
                intro.style.display = 'none';
                buildProgressDots();
                renderQuestion(0);
                game.style.display = 'grid';
            }, 350);
        },

        restart: function () {
            current = 0;
            answers = [];

            $('sqzResult').style.display = 'none';

            buildProgressDots();
            renderQuestion(0);
            $('sqzGame').style.display = 'grid';
        }
    };
}());
