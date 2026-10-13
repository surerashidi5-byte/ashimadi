// Tmax Pure Autonomous Generated Shader (OpenGL ES 3.0)
#version 300 es
precision highp float;

in vec2 vTexCoord;
in vec3 vNormal;
in vec3 vViewDir;
out vec4 fragColor;

uniform sampler2D uBackgroundTexture;
uniform float uBlurStrength;

void main() {
    vec2 texelSize = 1.0 / vec2(textureSize(uBackgroundTexture, 0));
    vec4 colorSum = vec4(0.0);
    
    // Advanced Multi-Pass Blur for Glass
    for(int x = -3; x <= 3; x++) {
        for(int y = -3; y <= 3; y++) {
            vec2 offset = vec2(float(x), float(y)) * texelSize * uBlurStrength;
            colorSum += texture(uBackgroundTexture, vTexCoord + offset);
        }
    }
    vec4 blurred = colorSum / 49.0;
    vec3 glassTint = vec3(0.82, 0.90, 1.0) * 0.4;
    vec3 finalColor = mix(blurred.rgb, glassTint, 0.5);
    
    fragColor = vec4(finalColor, 0.88);
}
