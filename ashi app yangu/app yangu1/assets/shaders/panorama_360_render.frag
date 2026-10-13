#version 300 es
precision highp float;

in vec2 vTexCoord;
out vec4 fragColor;

uniform sampler2D uPanoramaTexture;
uniform float uYawAngle;
uniform float uPitchAngle;
uniform float uTime;
uniform vec3 uColorFilter;
uniform float uWindIntensity;
uniform float uBloomThreshold;
uniform float uFogDensity;

void main() {
    vec2 uv = vTexCoord;

    // Wind wave effect
    float windEffect = sin(uv.y * 25.0 + uTime * 4.0) * 0.004 * uWindIntensity;
    float windWave = cos(uv.x * 15.0 + uTime * 2.5) * 0.002 * uWindIntensity;
    uv.x += windEffect;
    uv.y += windWave;

    // 360 Panorama Movement
    uv.x = fract(uv.x + uYawAngle / 360.0);
    uv.y = clamp(uv.y + uPitchAngle / 180.0, 0.0, 1.0);

    vec4 texColor = texture(uPanoramaTexture, uv);
    vec3 color = texColor.rgb * uColorFilter;

    // God Rays / Dynamic Sun Effect
    float sunRay = max(0.0, sin(uv.x * 3.14159 * 4.0 + uTime * 0.5));
    color += vec3(0.12, 0.10, 0.08) * sunRay * uWindIntensity;

    // HDR Bloom
    float brightness = dot(color, vec3(0.2126, 0.7152, 0.0722));
    if (brightness > uBloomThreshold) {
        color += color * 0.35;
    }

    // Atmospheric Fog
    float fogFactor = smoothstep(0.2, 0.9, abs(uv.y - 0.5)) * uFogDensity;
    color = mix(color, vec3(0.05, 0.08, 0.12), fogFactor);

    fragColor = vec4(color, texColor.a);
}
