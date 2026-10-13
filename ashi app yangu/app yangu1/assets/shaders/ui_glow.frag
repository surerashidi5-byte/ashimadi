#version 300 es
precision highp float;
in vec2 vTexCoord;
out vec4 fragColor;
uniform float uTime;
uniform vec3 uGlowColor;
uniform float uIntensity;
void main() {
    float d = length(vTexCoord - 0.5);
    float glow = 1.0 - smoothstep(0.0, 0.75, d);
    float pulse = 0.85 + 0.15 * sin(uTime * 2.0);
    fragColor = vec4(uGlowColor, glow * uIntensity * pulse);
}
