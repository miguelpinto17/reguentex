/* Reguentex — shared behaviour: EN/PT toggle, lightbox, reveal, menu, request form. No dependencies. */
(function () {
  var D = window.RGX_I18N || { c: {}, alt: {} };
  var doc = document, root = doc.documentElement;
  var LS = 'rgx-lang';

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) {} }
  function pick(pair, lang) { return pair ? pair[lang === 'pt' ? 1 : 0] : null; }

  /* ---------- language ---------- */
  var lang = store(LS) || ((navigator.language || '').toLowerCase().indexOf('pt') === 0 ? 'pt' : 'en');
  function t(key) { return pick(D.c[key], lang); }

  function applyLang(l) {
    lang = l; root.lang = l === 'pt' ? 'pt-PT' : 'en';
    doc.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = t(el.getAttribute('data-i18n')); if (v != null) el.textContent = v;
    });
    doc.querySelectorAll('img[data-alt]').forEach(function (img) {
      var v = pick(D.alt[img.getAttribute('data-alt')], l); if (v) img.alt = v;
    });
    doc.querySelectorAll('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(',').forEach(function (pair) {
        var p = pair.split(':'), v = t(p[1]); if (v != null) el.setAttribute(p[0], v);
      });
    });
    var tk = root.getAttribute('data-title-key'); if (tk && t(tk)) doc.title = t(tk);
    doc.querySelectorAll('[data-lang-set]').forEach(function (b) {
      var on = b.getAttribute('data-lang-set') === l;
      b.setAttribute('aria-pressed', on); b.classList.toggle('is-on', on);
    });
    store(LS, l);
  }
  doc.addEventListener('click', function (e) {
    var b = e.target.closest('[data-lang-set]'); if (b) applyLang(b.getAttribute('data-lang-set'));
  });

  /* ---------- menu / header ---------- */
  var body = doc.body;
  doc.addEventListener('click', function (e) {
    if (e.target.closest('[data-menu-toggle]')) {
      var open = body.classList.toggle('menu-open');
      doc.querySelectorAll('[data-menu-toggle]').forEach(function (b) { b.setAttribute('aria-expanded', open); });
    } else if (e.target.closest('[data-nav] a') && body.classList.contains('menu-open')) {
      body.classList.remove('menu-open');
    }
  });
  function onScroll() { body.classList.toggle('is-scrolled', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- scroll reveal ---------- */
  var rv = doc.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- lightbox ---------- */
  var lb, items = [], idx = 0, lastFocus;
  function build() {
    lb = doc.createElement('div'); lb.className = 'rgx-lb'; lb.hidden = true;
    lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true');
    lb.innerHTML = '<button class="rgx-lb-x" aria-label="Close">&times;</button>' +
      '<button class="rgx-lb-p" aria-label="Previous">&#8592;</button>' +
      '<figure><img alt=""><figcaption></figcaption></figure>' +
      '<button class="rgx-lb-n" aria-label="Next">&#8594;</button>';
    body.appendChild(lb);
    lb.addEventListener('click', function (e) {
      if (e.target.closest('.rgx-lb-p')) go(-1);
      else if (e.target.closest('.rgx-lb-n')) go(1);
      else if (!e.target.closest('img')) close();
    });
  }
  function show() {
    var a = items[idx], img = lb.querySelector('img'), src = a.getAttribute('href');
    img.src = src; img.alt = a.querySelector('img') ? a.querySelector('img').alt : '';
    lb.querySelector('figcaption').textContent = (idx + 1) + ' / ' + items.length + (img.alt ? '  ·  ' + img.alt : '');
  }
  function go(d) { idx = (idx + d + items.length) % items.length; show(); }
  function close() { lb.hidden = true; body.classList.remove('lb-open'); if (lastFocus) lastFocus.focus(); }
  doc.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-lb]'); if (!a) return;
    e.preventDefault(); if (!lb) build();
    var g = a.getAttribute('data-lb') || 'all';
    items = Array.prototype.slice.call(doc.querySelectorAll('a[data-lb="' + g + '"]'));
    idx = items.indexOf(a); lastFocus = a; show(); lb.hidden = false; body.classList.add('lb-open');
    lb.querySelector('.rgx-lb-x').focus();
  });
  doc.addEventListener('keydown', function (e) {
    if (!lb || lb.hidden) return;
    if (e.key === 'Escape') close(); else if (e.key === 'ArrowRight') go(1); else if (e.key === 'ArrowLeft') go(-1);
  });
  var sx = 0;
  doc.addEventListener('touchstart', function (e) { sx = e.changedTouches[0].clientX; }, { passive: true });
  doc.addEventListener('touchend', function (e) {
    if (!lb || lb.hidden) return; var dx = e.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1);
  }, { passive: true });

  /* ---------- request form ----------
     Set data-endpoint on the <form> (Formspree, Netlify, your own API…) to POST there.
     Without it, the form opens the visitor's email app addressed to geral@reguentex.pt. */
  doc.querySelectorAll('form[data-request]').forEach(function (f) {
    var status = f.querySelector('[data-status]');
    f.addEventListener('submit', function (e) {
      e.preventDefault(); if (!f.reportValidity()) return;
      var data = new FormData(f), ep = f.getAttribute('data-endpoint');
      if (ep) {
        fetch(ep, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (r) { if (!r.ok) throw 0; f.reset(); say('f_ok', 'ok'); })
          .catch(function () { say('f_err', 'err'); });
      } else {
        var msg = (data.get('message') || t('f_msg_default')) + '\n\n' + data.get('name') + '\n' + (data.get('company') || '') + '\n' + data.get('email');
        location.href = 'mailto:' + f.getAttribute('data-mailto') + '?subject=' +
          encodeURIComponent('Virtual Showroom — ' + data.get('name')) + '&body=' + encodeURIComponent(msg);
        say('f_mail', 'ok');
      }
    });
    function say(k, cls) { if (!status) return; status.setAttribute('data-i18n', k); status.textContent = t(k); status.className = 'form-status ' + cls; }
  });

  /* ---------- slide-in panels: [data-open="x"] / [data-close="x"] toggle body.x-open on #x ---------- */
  function panel(name, open) {
    body.classList.toggle(name + '-open', open);
    var p = doc.getElementById(name); if (!p) return;
    p.setAttribute('aria-hidden', !open);
    if (open) { var i = p.querySelector('input'); if (i) setTimeout(function () { i.focus(); }, 350); }
  }
  doc.addEventListener('click', function (e) {
    var o = e.target.closest('[data-open]'), c = e.target.closest('[data-close]');
    if (o) panel(o.getAttribute('data-open'), true); else if (c) panel(c.getAttribute('data-close'), false);
  });
  doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') panel('enq', false); });

  /* ---------- gentle parallax: [data-parallax] > img drifts against the scroll ---------- */
  var par = Array.prototype.slice.call(doc.querySelectorAll('[data-parallax]'));
  if (par.length && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var tick = false;
    var run = function () {
      tick = false; var vh = window.innerHeight;
      par.forEach(function (el) {
        var r = el.getBoundingClientRect(); if (r.bottom < -100 || r.top > vh + 100) return;
        var im = el.querySelector('img'); if (!im) return;
        im.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - vh / 2) * -0.12).toFixed(1) + 'px,0) scale(1.18)';
      });
    };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true });
    window.addEventListener('resize', run); run();
  }

  applyLang(lang);
})();
