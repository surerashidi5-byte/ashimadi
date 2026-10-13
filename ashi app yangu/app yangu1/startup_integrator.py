import os
import json
import shutil

base_dir = "/sdcard/app yangu1"
assets_dir = os.path.join(base_dir, "assets")
config_dir = os.path.join(assets_dir, "config")

print("="*50)
print("[*] TMAX WELCOME & LOADING INTEGRATOR: Inasanisi Skrini ya Kwanza...")
print("="*50)

# 1. Kusaka na kuhamisha picha ya ukaribisho (ashimadi.png)
source_img = os.path.join(assets_dir, "ashimadi.png")
target_img_dir = os.path.join(assets_dir, "intro")
os.makedirs(target_img_dir, exist_ok=True)
target_img_path = os.path.join(target_img_dir, "welcome_splash.png")

if os.path.exists(source_img):
    shutil.copy2(source_img, target_img_path)
    print(f"[+] Picha ya ukaribisho imepangwa rasmi: intro/welcome_splash.png")
else:
    print("[!] Tahadhari: Faili la ashimadi.png halikuonekana kwenye assets/.")

# 2. Kuunda/Kusasisha mfumo wa Startup Intro na 3D Loading Bar kwenye Config
startup_config_path = os.path.join(config_dir, "startup_intro.json")
os.makedirs(config_dir, exist_ok=True)

startup_data = {
    "splash_image": "assets/intro/welcome_splash.png",
    "title": "ASHIMADI 3D LAUNCHER",
    "subtitle": "WELCOME",
    "loading_bar": {
        "style": "3D_ROAD_PROGRESS",
        "min_value": 0,
        "max_value": 100,
        "animation_speed": "smooth_accelerated",
        "trigger_engine_on_complete": True
    },
    "next_runtime": "engine_core_runtime.json"
}

with open(startup_config_path, 'w', encoding='utf-8') as f:
    json.dump(startup_data, f, indent=4)

print("[+] Mipangilio ya Skrini ya Ukaribisho na 3D Loading Bar imerekebishwa kikamilifu!")
print("[✔] Tmax imekamilisha uunganishaji wa mafanikio bila kugusa injini kuu!")
print("="*50)
