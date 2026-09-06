// Adapted from Tacite's living Monet concept. All pigment is generated in code;
// no painting, photograph, texture, or other image asset is loaded.
const COLORS = [
  [0.57, 0.70, 0.74], [0.43, 0.60, 0.66], [0.64, 0.64, 0.75],
  [0.50, 0.64, 0.56], [0.74, 0.77, 0.69], [0.88, 0.84, 0.68],
];

function noise(x, y) {
  return Math.sin(x * 3.1 + Math.sin(y * 3.7)) * 0.5
    + Math.sin(y * 5.3 - x * 1.8) * 0.3 + Math.sin(x * 11 + y * 7) * 0.2;
}

export function createMonetMarks(compact) {
  let seed = 1906;
  const random = () => {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    return seed / 4294967296;
  };
  const data = [];
  const corners = [[-1, -1], [1, -1], [-1, 1], [-1, 1], [1, -1], [1, 1]];
  const addMark = (x, y, w, h, angle, color, alpha) => {
    const variation = random();
    for (const [cx, cy] of corners) {
      data.push(cx, cy, x, y, w, h, angle, ...color, alpha, variation);
    }
  };

  // Broad underpainting binds the fine marks into one continuous water surface.
  for (let i = 0; i < 1000; i++) {
    const x = random() * 1.12 - 0.06;
    const y = random() * 1.12 - 0.06;
    const n = noise(x * 2.3, y * 1.8);
    const color = COLORS[n > 0.50 ? 3 : n < -0.42 ? 2 : n > 0.05 ? 0 : 1];
    addMark(x, y, 0.028 + random() * 0.045, 0.009 + random() * 0.021,
      (random() - 0.5) * 0.7, color, 0.20);
  }
  const count = compact ? 6800 : 15000;
  for (let i = 0; i < count; i++) {
    const x = random() * 1.12 - 0.06;
    const y = random() * 1.12 - 0.06;
    const n = noise(x * 2.3, y * 1.8);
    const colorIndex = n > 0.50 ? 3 : n < -0.42 ? 2 : n > 0.05 ? 0 : 1;
    const base = random() > 0.84 ? COLORS[4] : COLORS[colorIndex];
    const light = (random() - 0.5) * 0.19;
    const color = base.map(c => Math.min(1, Math.max(0, c + light)));
    // A few vertical reflections interrupt the horizontal water strokes.
    const reflection = y < 0.6 && Math.sin(x * 24 + noise(x, y) * 2) > 0.45;
    const size = compact ? 1.25 : 1;
    addMark(x, y,
      (0.005 + random() ** 2 * 0.020) * size,
      (0.0018 + random() * 0.005) * size,
      reflection ? 0.6 + random() * 0.75 : (random() - 0.5) * 0.6,
      color, 0.35 + random() * 0.36);
  }

  // Lily pads are loose groups of marks, with broken edges and rare flowers.
  const islands = [[0.84, 0.25, 0.19], [0.68, 0.72, 0.23], [0.16, 0.86, 0.18], [0.96, 0.91, 0.17], [0.32, 0.08, 0.12]];
  for (const [ix, iy, spread] of islands) {
    for (let pad = 0; pad < 24; pad++) {
      const x = ix + (random() - 0.5) * spread * 2;
      const y = iy + (random() - 0.5) * spread * 0.63;
      const radius = 0.008 + random() * 0.024;
      const flower = random() > 0.81;
      for (let mark = 0; mark < (compact ? 12 : 20); mark++) {
        const theta = random() * Math.PI * 2;
        const r = Math.sqrt(random());
        const px = x + Math.cos(theta) * radius * r;
        const py = y + Math.sin(theta) * radius * 0.38 * r;
        const base = mark < 5 ? [0.30, 0.49, 0.43] : mark < 13 ? [0.51, 0.65, 0.48] : [0.73, 0.76, 0.56];
        const lift = random() * 0.13;
        addMark(px, py, 0.003 + random() * radius * 0.34, 0.0015 + random() * 0.002,
          (random() - 0.5) * 0.55, base.map(c => c + lift), 0.68);
      }
      if (flower) {
        for (let petal = 0; petal < 8; petal++) {
          const color = petal < 3 ? [0.69, 0.44, 0.58] : [0.94, 0.80 + random() * 0.12, 0.79];
          addMark(x + (random() - 0.5) * 0.009, y - random() * 0.006,
            0.002 + random() * 0.003, 0.0014 + random() * 0.0025,
            (random() - 0.5) * 1.6, color, 0.88);
        }
      }
    }
  }
  return new Float32Array(data);
}
