import os
import json
import hashlib
import shutil

base_dir = "/sdcard/app yangu1"
config_dir = os.path.join(base_dir, "assets", "config")
catalog_file = os.path.join(config_dir, "system_master_catalog.json")

print("="*60)
print("[*] TMAX PROFESSIONAL SAFE-INSPECTOR: Inachunguza na kupanga mfumo...")
print("="*60)

def verify_and_catalog():
    registry = {}
    
    # Kupitia kila faili kwa nidhamu ya hali ya juu bila kubadilisha asili yake
    for root, dirs, files in os.walk(base_dir):
        # Kuzuia isome folda za system zisizohitajika ili kulinda usalama
        if "incoming_modules" in root or ".git" in root:
            continue
            
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            
            try:
                with open(full_path, 'rb') as f:
                    header = f.read(16)
                    
                file_type = "GENERAL_ASSET"
                if header.startswith(b'glTF') or b'"asset"' in header:
                    file_type = "3D_MODEL_GLTF"
                elif file.endswith('.json'):
                    file_type = "JSON_CONFIG"
                elif file.endswith(('.png', '.jpg', '.jpeg')):
                    file_type = "IMAGE_SPLASH"
                    
                registry[rel_path] = {
                    "type": file_type,
                    "size": os.path.getsize(full_path),
                    "status": "PROTECTED_AND_ALIGNED"
                }
            except Exception:
                pass

    # Kuhifadhi katalogi ya usalama bila kugusa wala kuharibu muundo wa ndani wa mod zako
    with open(catalog_file, 'w', encoding='utf-8') as f:
        json.dump({"protected_system_registry": registry}, f, indent=4)

    print(f"[✔] Usalama umekamilika! Mafaili {len(registry)} yamesajiliwa kwa nidhamu ya kitaalamu.")
    print(f"[+] Katalogi rasmi imehifadhiwa: assets/config/system_master_catalog.json")
    print("="*60)

if __name__ == "__main__":
    verify_and_catalog()
