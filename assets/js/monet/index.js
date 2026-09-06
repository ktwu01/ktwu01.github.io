import { createMonetPainter } from './monet-painter.js';

// The page remains readable without JavaScript or WebGL. CSS provides the base
// color field; data-ready only reveals a canvas after it has painted a frame.
export function initializeMonetBackground(canvas) {
  if (!canvas) return () => {};
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let painter = null;
  let frame = 0;
  let lastTick = 0;
  let lastPaint = 0;
  let elapsed = 0;
  let resizeNeeded = false;
  let contextLost = false;
  const pointer = [-2, -2];
  const target = [-2, -2];
  let scroll = 0;

  const draw = () => {
    if (resizeNeeded) { painter?.resize(); resizeNeeded = false; }
    painter?.draw({
      time: reducedMotion.matches ? 0 : elapsed,
      scroll: reducedMotion.matches ? 0 : scroll,
      pointer: reducedMotion.matches ? [-2, -2] : pointer,
    });
  };
  const tick = now => {
    if (!painter || document.hidden || reducedMotion.matches || contextLost) return;
    const delta = now - lastTick;
    if (delta >= 1000 / 30) {
      elapsed += Math.min(now - lastPaint, 80) / 1000;
      lastPaint = now;
      // Retain fractional frame time for an even 30 fps on 60 Hz displays.
      lastTick = now - (delta % (1000 / 30));
      pointer[0] += (target[0] - pointer[0]) * 0.045;
      pointer[1] += (target[1] - pointer[1]) * 0.045;
      draw();
    }
    frame = requestAnimationFrame(tick);
  };
  const syncMotion = () => {
    cancelAnimationFrame(frame);
    if (!painter || contextLost || document.hidden) return;
    draw();
    canvas.dataset.ready = 'true';
    if (!reducedMotion.matches) {
      lastTick = lastPaint = performance.now();
      frame = requestAnimationFrame(tick);
    }
  };
  const initialize = () => {
    try { painter = createMonetPainter(canvas); } catch { painter = null; }
    canvas.dataset.ready = 'false';
    syncMotion();
  };
  const onPointerMove = event => {
    if (event.pointerType === 'touch' || reducedMotion.matches) return;
    target[0] = event.clientX / Math.max(window.innerWidth, 1);
    target[1] = event.clientY / Math.max(window.innerHeight, 1);
  };
  const onPointerLeave = () => { target[0] = -2; target[1] = -2; };
  const onScroll = () => { scroll = Math.min(window.scrollY / Math.max(window.innerHeight, 1), 12); };
  const onResize = () => {
    resizeNeeded = true;
    if (reducedMotion.matches && !document.hidden && !contextLost) draw();
  };
  const onContextLost = event => {
    event.preventDefault();
    contextLost = true;
    cancelAnimationFrame(frame);
    canvas.dataset.ready = 'false';
  };
  const onContextRestored = () => {
    painter?.dispose();
    contextLost = false;
    initialize();
  };

  onScroll();
  initialize();
  const observer = typeof ResizeObserver === 'function' ? new ResizeObserver(onResize) : null;
  observer?.observe(canvas);
  if (!observer) window.addEventListener('resize', onResize, { passive: true });
  document.addEventListener('visibilitychange', syncMotion);
  document.addEventListener('pointermove', onPointerMove, { passive: true });
  document.documentElement.addEventListener('pointerleave', onPointerLeave);
  window.addEventListener('scroll', onScroll, { passive: true });
  // Safari versions predating MediaQueryList's EventTarget support use listeners.
  if (reducedMotion.addEventListener) reducedMotion.addEventListener('change', syncMotion);
  else reducedMotion.addListener(syncMotion);
  canvas.addEventListener('webglcontextlost', onContextLost);
  canvas.addEventListener('webglcontextrestored', onContextRestored);

  return () => {
    cancelAnimationFrame(frame);
    observer?.disconnect();
    window.removeEventListener('resize', onResize);
    document.removeEventListener('visibilitychange', syncMotion);
    document.removeEventListener('pointermove', onPointerMove);
    document.documentElement.removeEventListener('pointerleave', onPointerLeave);
    window.removeEventListener('scroll', onScroll);
    if (reducedMotion.removeEventListener) reducedMotion.removeEventListener('change', syncMotion);
    else reducedMotion.removeListener(syncMotion);
    canvas.removeEventListener('webglcontextlost', onContextLost);
    canvas.removeEventListener('webglcontextrestored', onContextRestored);
    painter?.dispose();
    canvas.dataset.ready = 'false';
  };
}

// Module scripts are deferred, so the shared layout's canvas is available here.
const canvas = document.querySelector('.monet-background canvas');
initializeMonetBackground(canvas);
