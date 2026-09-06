/* Manual coverflow: no autoplay, external dependencies, or hidden archive links. */
(function () {
  'use strict';
  const deck = document.querySelector('.media-deck');
  if (!deck) return;
  const stage = deck.querySelector('.media-deck__stage');
  const cards = Array.from(stage.querySelectorAll('.media-card'));
  if (cards.length < 2) return;
  const controls = deck.querySelector('.media-deck__controls');
  const status = deck.querySelector('.media-deck__status');
  let active = 0;
  let width = 310;
  let pointer = null;
  let suppressClickUntil = 0;

  function place() {
    cards.forEach(function (card, index) {
      let offset = (index - active + cards.length) % cards.length;
      if (offset > cards.length / 2) offset -= cards.length;
      const distance = Math.abs(offset);
      card.style.transform = 'translateX(-50%) translateX(' + (offset * width * .65) + 'px) translateZ(' + (-distance * 85) + 'px) rotateY(' + (offset ? -Math.sign(offset) * 27 : 0) + 'deg)';
      card.style.opacity = distance > 2 ? '0' : String(1 - distance * .28);
      card.style.zIndex = String(cards.length - distance);
      card.style.visibility = distance > 2 ? 'hidden' : 'visible';
      card.classList.toggle('is-active', index === active);
      card.tabIndex = index === active ? 0 : -1;
      card.setAttribute('aria-hidden', index === active ? 'false' : 'true');
    });
    status.textContent = (active + 1) + ' / ' + cards.length + ' · ' + cards[active].querySelector('.media-card__outlet').textContent;
  }
  function go(index) {
    const cardHadFocus = cards.includes(document.activeElement);
    active = (index + cards.length) % cards.length;
    place();
    if (cardHadFocus) cards[active].focus({ preventScroll: true });
  }
  function measure() {
    width = Math.min(310, stage.clientWidth - 48);
    stage.style.setProperty('--media-card-width', width + 'px');
    stage.style.height = (Math.max.apply(null, cards.map(card => card.offsetHeight)) + 60) + 'px';
    place();
  }
  controls.hidden = false;
  deck.classList.add('is-ready');
  deck.querySelector('[data-media-prev]').addEventListener('click', () => go(active - 1));
  deck.querySelector('[data-media-next]').addEventListener('click', () => go(active + 1));
  deck.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      go(active + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
  cards.forEach(function (card, index) {
    card.addEventListener('click', function (event) {
      if (Date.now() < suppressClickUntil) { event.preventDefault(); return; }
      if (index !== active) { event.preventDefault(); go(index); }
    });
    card.addEventListener('dragstart', event => event.preventDefault());
  });
  stage.addEventListener('pointerdown', function (event) {
    if (!event.isPrimary || event.button !== 0) return;
    pointer = { id: event.pointerId, x: event.clientX, y: event.clientY };
  });
  window.addEventListener('pointerup', function (event) {
    if (!pointer || pointer.id !== event.pointerId) return;
    const dx = event.clientX - pointer.x;
    const dy = event.clientY - pointer.y;
    pointer = null;
    if (Math.abs(dx) > 35 && Math.abs(dx) > Math.abs(dy)) {
      suppressClickUntil = Date.now() + 400;
      go(active + (dx < 0 ? 1 : -1));
    }
  });
  window.addEventListener('pointercancel', () => { pointer = null; });
  if (window.ResizeObserver) new ResizeObserver(measure).observe(stage);
  else window.addEventListener('resize', measure);
  measure();
})();
