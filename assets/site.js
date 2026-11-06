// codex magna: notebook filter. Works without it; this only hides entries.
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
