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
