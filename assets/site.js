// codex magna: theme switch (the eclipse) and notebook filter. The site works without either.
(function () {
  var root = document.documentElement, btn = document.querySelector('.eclipse');
  if (!btn) return;
  function label() {
    var light = root.getAttribute('data-theme') === 'light';
    btn.setAttribute('aria-label', light ? 'switch to dark mode' : 'switch to light mode');
  }
  btn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    root.classList.add('theming');
    btn.classList.remove('turning');
    void btn.offsetWidth;
    btn.classList.add('turning');
    clearTimeout(btn._t);
    btn._t = setTimeout(function () { root.classList.remove('theming'); btn.classList.remove('turning'); }, 1900);
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('cm-theme', next); } catch (e) {}
    label();
  });
  label();
})();
(function () {
  var bar = document.querySelector('.filters');
  if (!bar) return;
  var links = bar.querySelectorAll('a');
  var ents = document.querySelectorAll('.entries .ent');
  function apply(k) {
    links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('data-k') === k); });
    ents.forEach(function (e) { e.classList.toggle('hide', !!k && e.getAttribute('data-kind') !== k); });
  }
  function fromHash() {
    var h = decodeURIComponent(location.hash.slice(1));
    var k = '';
    links.forEach(function (a) { if (a.getAttribute('href') === '#' + h) k = a.getAttribute('data-k'); });
    apply(k);
  }
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
// lightbox: click a photo to look at it up close. Esc / click closes, ← → move.
(function () {
  var imgs = Array.prototype.slice.call(document.querySelectorAll('.photo-full img, .photo-grid img'));
  if (!imgs.length) return;
  var box = document.createElement('div');
  box.className = 'lb';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'photograph');
  box.innerHTML = '<button class="lb-x" type="button" aria-label="close">×</button>' +
    '<button class="lb-prev" type="button" aria-label="previous photograph">←</button>' +
    '<figure class="lb-fig"><img alt=""><figcaption class="lb-cap"></figcaption></figure>' +
    '<button class="lb-next" type="button" aria-label="next photograph">→</button>';
  document.body.appendChild(box);
  var big = box.querySelector('img'), cap = box.querySelector('.lb-cap'), i = 0, last = null;
  function caption(el) {
    var f = el.closest('figure, a');
    var t = f && f.querySelector('.t, strong'), d = f && f.querySelector('.d');
    if (t) return (t.textContent + (d ? ' · ' + d.textContent : '')).trim();
    var c = f && f.querySelector('figcaption');
    return c ? c.textContent.trim() : el.alt;
  }
  function show(n) {
    i = (n + imgs.length) % imgs.length;
    var el = imgs[i];
    big.src = el.currentSrc || el.src;
    big.alt = el.alt;
    cap.textContent = caption(el);
  }
  function open(n) {
    last = document.activeElement;
    show(n);
    box.classList.add('on');
    document.documentElement.classList.add('lb-open');
    box.querySelector('.lb-x').focus();
  }
  function close() {
    box.classList.remove('on');
    document.documentElement.classList.remove('lb-open');
    if (last && last.focus) last.focus();
  }
  imgs.forEach(function (el, n) {
    el.classList.add('zoomable');
    var host = el.closest('a') || el;
    if (!el.closest('a')) { el.setAttribute('tabindex', '0'); el.setAttribute('role', 'button'); }
    host.addEventListener('click', function (e) { e.preventDefault(); open(n); });
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(n); } });
  });
  box.addEventListener('click', function (e) {
    if (e.target.closest('.lb-prev')) return show(i - 1);
    if (e.target.closest('.lb-next')) return show(i + 1);
    close();
  });
  document.addEventListener('keydown', function (e) {
    if (!box.classList.contains('on')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(i - 1);
    else if (e.key === 'ArrowRight') show(i + 1);
    else if (e.key === 'Tab') { e.preventDefault(); box.querySelector('.lb-x').focus(); }
  });
})();
// search the stacks: loads /vault/search.json on first use, matches every word, titles first
(function () {
  var q = document.getElementById('q');
  if (!q) return;
  var out = document.getElementById('qr'), cnt = document.getElementById('qn'), wrap = q.closest('.s');
  var data = null, loading = null, t = null;
  function load() {
    if (!loading) loading = fetch('/vault/search.json').then(function (r) { return r.json(); }).then(function (d) {
      data = d.map(function (x) { return { t: x[0], id: x[1], h: x[2], f: x[3], d: x[4], b: x[5], tl: x[0].toLowerCase(), bl: x[5].toLowerCase() }; });
    });
    return loading;
  }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function mark(s, words) {
    var h = esc(s);
    words.forEach(function (w) { h = h.replace(new RegExp('(' + esc(w).replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); });
    return h;
  }
  function snip(n, words) {
    var i = -1;
    for (var k = 0; k < words.length && i < 0; k++) i = n.bl.indexOf(words[k]);
    if (i < 0) return n.b.slice(0, 140) + (n.b.length > 140 ? ' …' : '');
    var a = Math.max(0, i - 60), b = Math.min(n.b.length, i + 120);
    return (a > 0 ? '… ' : '') + n.b.slice(a, b) + (b < n.b.length ? ' …' : '');
  }
  function run() {
    var v = q.value.trim().toLowerCase();
    wrap.classList.toggle('searching', !!v);
    if (!v) { out.innerHTML = ''; cnt.textContent = ''; return; }
    if (!data) { cnt.textContent = 'loading the stacks …'; load().then(run); return; }
    var words = v.split(/\s+/).filter(Boolean);
    var hits = [];
    data.forEach(function (n) {
      var score = 0;
      for (var k = 0; k < words.length; k++) {
        var w = words[k], inT = n.tl.indexOf(w) >= 0 || n.id.indexOf(w) === 0, inB = n.bl.indexOf(w) >= 0;
        if (!inT && !inB) return;
        score += inT ? 10 : 1;
      }
      if (n.tl === v) score += 50; else if (n.tl.indexOf(v) === 0) score += 20;
      hits.push([score, n]);
    });
    hits.sort(function (a, b) { return b[0] - a[0] || a[1].tl.localeCompare(b[1].tl); });
    cnt.textContent = hits.length ? hits.length + (hits.length === 1 ? ' note' : ' notes') : 'nothing in the stacks for that';
    out.innerHTML = hits.slice(0, 60).map(function (h) {
      var n = h[1];
      return '<a href="' + n.h + '"><span class="n">' + n.id + '</span><span class="rt">' + mark(n.t, words) + '</span><span class="rm">' + esc(n.f) + (n.d ? ' · ' + n.d : '') + '</span><span class="sn">' + mark(snip(n, words), words) + '</span></a>';
    }).join('') + (hits.length > 60 ? '<p class="quiet">' + (hits.length - 60) + ' more. Add a word to narrow it.</p>' : '');
  }
  q.addEventListener('focus', load, { once: true });
  q.addEventListener('input', function () { clearTimeout(t); t = setTimeout(run, 80); });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== q && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); q.focus(); }
    if (e.key === 'Escape' && document.activeElement === q) { q.value = ''; run(); }
  });
  var m = location.hash.match(/^#q=(.+)/);
  if (m) { q.value = decodeURIComponent(m[1]); run(); }
})();
