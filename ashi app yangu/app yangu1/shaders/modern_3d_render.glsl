// Auto-Generated Modern 3D Shader Core
#version 300 es
precision highp float;
in vec3 vNormal;
out vec4 fragColor;
void main() {
    float intensity = dot(vNormal, vec3(0.0, 0.0, 1.0));
    fragColor = vec4(vec3(intensity) * vec3(0.2, 0.6, 1.0), 1.0);
}
