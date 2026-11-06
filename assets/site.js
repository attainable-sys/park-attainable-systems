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
