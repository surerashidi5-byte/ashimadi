import os
import json

base_dir = "/sdcard/app yangu1"
print("="*50)
print("[*] TMAX ENGINE INSPECTOR: Inaanza kuchambua mfumo wako...")
print("="*50)

total_files = 0
configs_found = []
models_found = []
scripts_found = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        total_files += 1
        fp = os.path.join(root, file)
        
        # Tambua mafaili ya JSON na Configs
        if file.endswith('.json'):
            configs_found.append(file)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"\n[CONFIG] {file}:")
                    print(f"   -> Vipengele vyake: {list(data.keys())[:5]}")
            except:
                pass
                
        # Tambua mafaili ya Model au Assets kubwa
        elif file.endswith(('.g', '.gltf', '.obj', '.bin', '.zip')) or "model" in file.lower():
            size_mb = os.path.getsize(fp) / (1024 * 1024)
            models_found.append(f"{file} ({size_mb:.2f} MB)")
            
        # Tambua script za Python au JS
        elif file.endswith(('.py', '.js')):
            scripts_found.append(file)

print("\n" + "="*50)
print("       RIPOTI YA RAMANI YA INJINI YA 3D")
print("="*50)
print(f"[*] Jumla ya mafaili yaliyochunguzwa: {total_files}")
print(f"[*] Mafaili ya Mipangilio (JSON Configs): {len(configs_found)}")
for c in configs_found:
    print(f"    - {c}")

print(f"\n[*] Mafaili ya Model & 3D Assets: {len(models_found)}")
for m in models_found:
    print(f"    - {m}")

print(f"\n[*] Script za Uendeshaji (Python/JS): {len(scripts_found)}")
for s in scripts_found:
    print(f"    - {s}")

print("\n[✔] Uchambuzi wa Tmax umekamilika kikamilifu!")
print("="*50)
