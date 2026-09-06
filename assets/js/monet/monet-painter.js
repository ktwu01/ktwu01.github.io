import { createMonetMarks } from './monet-scene.js';
import { MONET_FRAGMENT, MONET_VERTEX } from './monet-shaders.js';

export function createMonetPainter(canvas) {
  const gl = canvas.getContext('webgl', {
    alpha: false,
    antialias: false,
    depth: false,
    powerPreference: 'low-power',
  });
  if (!gl) return null;
  const shaders = [];
  const program = gl.createProgram();
  const buffer = gl.createBuffer();
  const dispose = () => {
    if (buffer) gl.deleteBuffer(buffer);
    if (program) gl.deleteProgram(program);
    shaders.forEach(shader => gl.deleteShader(shader));
  };
  if (!program || !buffer) { dispose(); return null; }
  for (const [type, source] of [[gl.VERTEX_SHADER, MONET_VERTEX], [gl.FRAGMENT_SHADER, MONET_FRAGMENT]]) {
    const shader = gl.createShader(type);
    if (!shader) { dispose(); return null; }
    shaders.push(shader);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) { dispose(); return null; }
    gl.attachShader(program, shader);
  }
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) { dispose(); return null; }
  gl.useProgram(program);
  gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
  let vertexCount = 0;
  let compact;
  let offset = 0;
  for (const [name, size] of [['a_corner', 2], ['a_center', 2], ['a_size', 2], ['a_angle', 1], ['a_pigment', 4], ['a_seed', 1]]) {
    const location = gl.getAttribLocation(program, name);
    gl.enableVertexAttribArray(location);
    gl.vertexAttribPointer(location, size, gl.FLOAT, false, 48, offset * 4);
    offset += size;
  }
  const uniforms = Object.fromEntries(
    ['u_time', 'u_scroll', 'u_aspect', 'u_pointer'].map(name => [name, gl.getUniformLocation(program, name)])
  );
  gl.enable(gl.BLEND);
  gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
  gl.clearColor(0.69, 0.76, 0.77, 1);

  const resize = () => {
    const bounds = canvas.getBoundingClientRect();
    const nextCompact = bounds.width < 780;
    const ratio = Math.min(window.devicePixelRatio || 1, nextCompact ? 1 : 1.25);
    // Bound the drawing buffer even on a large or high-density display.
    const scale = Math.min(ratio, 1920 / Math.max(bounds.width, 1));
    canvas.width = Math.max(1, Math.round(bounds.width * scale));
    canvas.height = Math.max(1, Math.round(bounds.height * scale));
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.uniform1f(uniforms.u_aspect, bounds.width / Math.max(bounds.height, 1));
    if (nextCompact !== compact) {
      compact = nextCompact;
      const marks = createMonetMarks(compact);
      vertexCount = marks.length / 12;
      gl.bufferData(gl.ARRAY_BUFFER, marks, gl.STATIC_DRAW);
    }
  };
  resize();
  return {
    resize,
    draw({ time, scroll, pointer }) {
      gl.clear(gl.COLOR_BUFFER_BIT);
      gl.uniform1f(uniforms.u_time, time);
      gl.uniform1f(uniforms.u_scroll, scroll);
      gl.uniform2f(uniforms.u_pointer, ...pointer);
      gl.drawArrays(gl.TRIANGLES, 0, vertexCount);
    },
    dispose,
  };
}
