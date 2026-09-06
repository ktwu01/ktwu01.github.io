// Adapted from AmberLJC/AmberLJC.github.io@6e229f2; see README for source.
/* News deck — a coverflow, not a carousel.
   The card in the middle is the one being read; its neighbours turn away and
   step back, so the deck reads like flipping through movie posters. Cards are
   plain links in the HTML; this file only positions them, which keeps the
   section readable and clickable when the script never runs. */
(function () {
  var deck = document.querySelector('.news-deck');
  if (!deck) return;

  var stage = deck.querySelector('.news-stage');
  var track = deck.querySelector('.news-track');
  var cards = Array.prototype.slice.call(deck.querySelectorAll('.news-card'));
  if (cards.length < 2) return;

  var CARD_MAX = 330;
  var ANGLE = 26;      // degrees each step out from the centre turns away
  var DEPTH = 90;      // px pushed back per step, capped a few steps out
  // Neighbours drawn per side. The deck wraps, so this stays under half the
  // cards — otherwise the far card would show up on both sides at once.
  var settled = 0;
  var VISIBLE = Math.min(3, Math.max(1, Math.floor((cards.length - 1) / 2)));
  var DWELL = 4200;    // ms a card holds the middle before the deck moves on
  var active = 0;
  var step = 200;
  var drag = null;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var timer = 0;
  var held = true;    // the reader is on the deck, so it waits for them
  var holds = { pointer: false, focus: false, hidden: false, offscreen: true, paused: false };

  document.documentElement.classList.add('js-news');
  var pause = document.createElement('button');
  pause.type = 'button';
  pause.className = 'news-pause';
  pause.textContent = 'Pause motion';
  pause.hidden = reduced.matches;
  pause.setAttribute('aria-pressed', 'false');
  pause.addEventListener('click', function () {
    hold('paused', !holds.paused);
    pause.textContent = holds.paused ? 'Resume motion' : 'Pause motion';
    pause.setAttribute('aria-pressed', String(holds.paused));
  });
  deck.parentNode.appendChild(pause);


  // Arrows and dots only exist for a reader who has this script.
  var prev = document.createElement('button');
  prev.className = 'news-nav news-nav--prev';
  prev.type = 'button';
  prev.setAttribute('aria-label', 'Previous news item');
  prev.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M15 5 8 12l7 7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var next = prev.cloneNode(true);
  next.className = 'news-nav news-nav--next';
  next.setAttribute('aria-label', 'Next news item');
  next.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  deck.appendChild(prev);
  deck.appendChild(next);

  var dots = document.createElement('div');
  dots.className = 'news-dots';
  cards.forEach(function (card, i) {
    var dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('aria-label', 'Show news item ' + (i + 1));
    dot.addEventListener('click', function () { go(i); });
    dots.appendChild(dot);
  });
  deck.parentNode.insertBefore(dots, deck.nextSibling);
  var dotList = Array.prototype.slice.call(dots.children);

  function measure() {
    var w = stage.clientWidth;
    var card = Math.round(Math.min(w - 40, CARD_MAX, Math.max(230, w * 0.44)));
    step = Math.round(card * 0.64);
    stage.style.setProperty('--news-card-w', card + 'px');
    // The stage is as tall as the tallest card — notes differ in length, and a
    // deck that resized as you slid through it would jitter the page.
    var tallest = 0;
    cards.forEach(function (c) { tallest = Math.max(tallest, c.offsetHeight); });
    stage.style.height = (tallest + 30) + 'px';
    place();
  }

  // Shortest way round the ring: the deck loops, so the card five slots ahead
  // is really one slot behind, and both sides stay filled at every position.
  function offset(i) {
    var n = cards.length;
    var d = i - active;
    if (d > n / 2) d -= n;
    if (d < -n / 2) d += n;
    return d;
  }

  function place() {
    cards.forEach(function (card, i) {
      var d = offset(i);
      var far = Math.min(Math.abs(d), VISIBLE);
      var dir = d < 0 ? -1 : 1;
      // Spacing tightens the further out a card sits, the way a stack of
      // posters foreshortens, instead of marching off at an even pitch.
      var x = dir * (far * step - far * (far - 1) * step * 0.12);
      var hidden = Math.abs(d) >= VISIBLE + 1;
      card.style.transform =
        'translate(-50%, -50%) translateX(' + x + 'px) translateZ(' + (-far * DEPTH) + 'px) ' +
        'rotateY(' + (far === 0 ? 0 : -dir * (ANGLE + (far - 1) * 4)) + 'deg) ' +
        'scale(' + (1 - far * 0.09) + ')';
      card.style.opacity = hidden ? 0 : 1 - far * 0.26;
      card.style.zIndex = 50 - far;
      card.style.pointerEvents = hidden ? 'none' : 'auto';
      card.classList.toggle('is-active', d === 0);
      card.setAttribute('aria-hidden', hidden ? 'true' : 'false');
      card.tabIndex = hidden ? -1 : 0;
    });
    dotList.forEach(function (dot, i) { dot.classList.toggle('is-active', i === active); dot.setAttribute('aria-pressed', String(i === active)); });
    settled = Date.now();
  }

  function go(i) {
    var hadCardFocus = cards.indexOf(document.activeElement) !== -1;
    var n = cards.length;
    active = ((i % n) + n) % n;
    place();
    if (hadCardFocus) cards[active].focus({ preventScroll: true });
    schedule();
  }

  // The deck moves on its own, so nothing has to be clicked to read it; it
  // holds still while the pointer is on it, or while a card has keyboard
  // focus, so it never slides out from under someone mid-sentence.
  function schedule() {
    clearTimeout(timer);
    if (held || reduced.matches) return;
    timer = setTimeout(function () { go(active + 1); }, DWELL);
  }

  // Several things independently want the deck to wait — the pointer resting on
  // it, a focused card, a hidden tab, the section being scrolled past. They are
  // tracked separately so the last one to change its mind cannot speak for the
  // rest and start the deck moving under someone's cursor.
  function hold(reason, on) {
    holds[reason] = on;
    held = Object.keys(holds).some(function (k) { return holds[k]; });
    if (held) clearTimeout(timer);
    else schedule();
  }

  reduced.addEventListener('change', function () { pause.hidden = reduced.matches; schedule(); });
  deck.addEventListener('pointerenter', function () { hold('pointer', true); });
  deck.addEventListener('pointerleave', function () { hold('pointer', false); });
  deck.addEventListener('focusin', function () { hold('focus', true); });
  deck.addEventListener('focusout', function () { hold('focus', false); });
  document.addEventListener('visibilitychange', function () { hold('hidden', document.hidden); });

  prev.addEventListener('click', function () { go(active - 1); });
  next.addEventListener('click', function () { go(active + 1); });

  // A click on a neighbour brings it to the middle rather than following its
  // link — the reader is picking, not opening. A click on the middle card
  // opens it, but only once it has settled: while the deck is still sliding,
  // the card under the cursor is not the one the reader aimed at.
  cards.forEach(function (card, i) {
    card.addEventListener('click', function (e) {
      if (i !== active || Date.now() - settled < 450) {
        e.preventDefault();
        if (i !== active) go(active + offset(i));
      }
    });
    card.addEventListener('focus', function () { if (i !== active) go(active + offset(i)); });
  });

  deck.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { go(active - 1); e.preventDefault(); }
    if (e.key === 'ArrowRight') { go(active + 1); e.preventDefault(); }
  });

  // Drag / swipe: the deck follows the pointer, then settles on whichever card
  // the release landed nearest.
  function down(e) {
    if (e.button) return;
    drag = { x: e.clientX, moved: 0 };
    track.style.transition = 'none';
  }
  function move(e) {
    if (!drag) return;
    drag.moved = e.clientX - drag.x;
    track.style.transform = 'translateX(' + drag.moved * 0.55 + 'px)';
  }
  function up() {
    if (!drag) return;
    track.style.transition = '';
    track.style.transform = '';
    if (Math.abs(drag.moved) > 30) go(active - Math.round(drag.moved / step));
    // Suppress the click that follows a real drag, so a swipe never opens a link.
    var moved = Math.abs(drag.moved);
    drag = null;
    if (moved > 8) {
      deck.addEventListener('click', function swallow(e) {
        e.preventDefault();
        e.stopPropagation();
        deck.removeEventListener('click', swallow, true);
      }, true);
    }
  }
  // Trackpad: a two-finger sideways swipe slides the deck. Only horizontal
  // intent is taken — a swipe that is mostly vertical is the reader scrolling
  // the page past the section, and the page keeps it.
  var wheelSum = 0;
  var wheelIdle = 0;
  var wheelLock = 0;
  stage.addEventListener('wheel', function (e) {
    if (Math.abs(e.deltaX) <= Math.abs(e.deltaY)) return;
    e.preventDefault();
    clearTimeout(wheelIdle);
    // One flick should move one card, not race through the deck, so the
    // accumulator is spent on the first threshold crossing and then ignores
    // the tail of the same gesture.
    wheelIdle = setTimeout(function () { wheelSum = 0; wheelLock = 0; }, 220);
    if (wheelLock) return;
    wheelSum += e.deltaX;
    if (Math.abs(wheelSum) > 40) {
      wheelLock = 1;
      wheelSum = 0;
      go(active + (e.deltaX > 0 ? 1 : -1));
    }
  }, { passive: false });

  stage.addEventListener('pointerdown', down);
  window.addEventListener('pointermove', move);
  window.addEventListener('pointerup', up);
  window.addEventListener('pointercancel', up);

  // Nothing should be cycling in a part of the page nobody is looking at.
  if (window.IntersectionObserver) {
    new IntersectionObserver(function (entries) {
      hold('offscreen', !entries[0].isIntersecting);
    }, { threshold: 0.25 }).observe(deck);
  }

  if (!window.IntersectionObserver) hold('offscreen', false);
  if (window.ResizeObserver) new ResizeObserver(measure).observe(deck);
  window.addEventListener('resize', measure);
  measure();
  schedule();
  // Artwork loading late changes a card's height; remeasure once it settles.
  window.addEventListener('load', measure);
})();
