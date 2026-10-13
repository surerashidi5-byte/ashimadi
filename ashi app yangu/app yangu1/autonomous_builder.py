import os
import json

base_dir = "/sdcard/app yangu1"
config_dir = os.path.join(base_dir, "assets", "config")
shaders_dir = os.path.join(base_dir, "shaders")

# Kutengeneza folda husika kwa usalama kama hazipo, bila kugusa zilizopo
os.makedirs(config_dir, exist_ok=True)
os.makedirs(shaders_dir, exist_ok=True)

print("="*60)
print("[*] AUTONOMOUS ARCHITECTURE ENGINE: Inachunguza na kuunda kisasa...")
print("="*60)

# 1. Kuunda kigezo cha Modern UI Theme kwenye assets/config/
modern_ui_file = os.path.join(config_dir, "modern_ui_theme.json")
if not os.path.exists(modern_ui_file):
    modern_ui_config = {
        "version": "2026.1_MODERN_CORE",
        "theme_style": "NEUMORPHIC_3D_GLASS",
        "animations": {
            "card_hover": "DEPTH_PARALLAX_3D",
            "screen_transition": "SMOOTH_SMOOTH_ACCEL",
            "fps_target": 60
        },
        "lighting": {
            "ambient_light": "#FFFFFF",
            "shadow_quality": "HIGH_DEFINED_MAPS"
        },
        "auto_generated_by": "Autonomous Builder Engine"
    }
    with open(modern_ui_file, 'w', encoding='utf-8') as f:
        json.dump(modern_ui_config, f, indent=4)
    print(f"[+] Kimeingia kwenye mpangilio sahihi: assets/config/modern_ui_theme.json")

# 2. Kuunda Shader ya kisasa kwenye shaders/
modern_shader_file = os.path.join(shaders_dir, "modern_3d_render.glsl")
if not os.path.exists(modern_shader_file):
    shader_code = """// Auto-Generated Modern 3D Shader Core
#version 300 es
precision highp float;
in vec3 vNormal;
out vec4 fragColor;
void main() {
    float intensity = dot(vNormal, vec3(0.0, 0.0, 1.0));
    fragColor = vec4(vec3(intensity) * vec3(0.2, 0.6, 1.0), 1.0);
}
"""
    with open(modern_shader_file, 'w', encoding='utf-8') as f:
        f.write(shader_code)
    print(f"[+] Kimeingia kwenye mpangilio sahihi: shaders/modern_3d_render.glsl")

# 3. Kuingiza usajili kwenye catalog kuu bila kuharibu mfumo
catalog_file = os.path.join(config_dir, "system_master_catalog.json")
if os.path.exists(catalog_file):
    try:
        with open(catalog_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        registry = data.get("protected_system_registry", {})
        
        # Kuongeza vipengele vipya kwenye usajili kwa nidhamu
        registry["assets/config/modern_ui_theme.json"] = {
            "type": "JSON_CONFIG",
            "status": "PROTECTED_AND_ALIGNED"
        }
        registry["shaders/modern_3d_render.glsl"] = {
            "type": "SHADER_SOURCE",
            "status": "PROTECTED_AND_ALIGNED"
        }
        
        data["protected_system_registry"] = registry
        
        with open(catalog_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"[✔] Katalogi kuu imesasishwa na kusajili vipengele vipya bila kuharibu vilivyopo!")
    except Exception as e:
        print(f"[!] Hitilafu ya usasishaji: {e}")

print("="*60)
print("[✔] Kazi imekamilika! Vipengele vimeingia sehemu zake sahihi salama kabisa.")
print("="*60)
