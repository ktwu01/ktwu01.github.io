export const MONET_VERTEX = `
attribute vec2 a_corner;
attribute vec2 a_center;
attribute vec2 a_size;
attribute float a_angle;
attribute vec4 a_pigment;
attribute float a_seed;
uniform float u_time;
uniform float u_scroll;
uniform float u_aspect;
uniform vec2 u_pointer;
varying vec2 v_brush;
varying vec4 v_color;
varying float v_seed;

void main() {
  vec2 p = a_center;
  float t = u_time;
  // Neighbouring marks move together, like reflections on a single surface.
  float wave = sin(p.y * 19.0 + p.x * 5.0 + t * 0.32);
  p.x += 0.008 * wave + 0.004 * sin(p.y * 37.0 - t * 0.19);
  p.y += 0.0035 * sin(p.x * 12.0 + t * 0.22) + sin(u_scroll * 0.3) * 0.025;
  vec2 delta = p - u_pointer;
  float wake = exp(-dot(delta, delta) * 18.0);
  p.x += wake * 0.006 * sin(length(delta) * 40.0 - t * 0.75);
  float angle = a_angle + wave * 0.035;
  mat2 rotation = mat2(cos(angle), -sin(angle), sin(angle), cos(angle));
  vec2 brush = rotation * (a_corner * a_size);
  brush.x *= clamp(1.6 / u_aspect, 0.8, 1.6);
  vec2 point = p + brush;
  gl_Position = vec4(point.x * 2.0 - 1.0, 1.0 - point.y * 2.0, 0.0, 1.0);
  v_brush = a_corner;
  v_color = a_pigment;
  v_color.rgb += 0.018 * sin(t * 0.15 + a_center.x * 4.0 + a_center.y * 3.0);
  v_seed = a_seed;
}`;

export const MONET_FRAGMENT = `
precision mediump float;
varying vec2 v_brush;
varying vec4 v_color;
varying float v_seed;
float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
void main() {
  vec2 p = v_brush;
  // Uneven edges, bristle grooves, and translucent pigment accumulation.
  float bristle = sin(p.y * 29.0 + v_seed * 72.0) * 0.045
    + sin(p.y * 67.0 + p.x * 3.0) * 0.025;
  float edge = pow(abs(p.x + bristle * 1.5), 4.0) + pow(abs(p.y + bristle), 4.0);
  float opacity = (1.0 - smoothstep(0.66, 1.02, edge)) * v_color.a;
  float dry = 0.77 + 0.23 * hash(floor(p * vec2(85.0, 24.0)) + v_seed * 120.0);
  float groove = 0.96 + 0.04 * sin(p.y * 80.0 + v_seed * 50.0);
  gl_FragColor = vec4(v_color.rgb * groove, opacity * dry);
}`;
