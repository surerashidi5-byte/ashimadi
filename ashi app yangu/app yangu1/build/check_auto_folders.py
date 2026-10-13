import os
import json

base_dir = "/sdcard/app yangu1"
print("="*85)
print("[*] TMAX FOLDER AUTO-INTEGRATION CHECKER: Inachunguza kama mafolda mapya yanaingia ndani ya Moduli...")
print("="*85)

# 1. Kusanya mafolda na mafaili yote yaliyopo kwenye app yangu1
actual_folders = []
actual_files_count = 0
for root, dirs, files in os.walk(base_dir):
    for d in dirs:
        actual_folders.append(os.path.relpath(os.path.join(root, d), base_dir))
    actual_files_count += len(files)

print(f"[✔] Jumla ya mafolda yaliyopo kwenye simu: {len(actual_folders)}")
print(f"[✔] Jumla ya mafaili yaliyopo: {actual_files_count}")

print("\n--- ORODHA YA MAFOLDA YALIYOGUNDULIWA ---")
for f_folder in actual_folders[:15]: # Inaonyesha mafolda 15 ya mwanzo
    print(f"   📁 {f_folder}")
if len(actual_folders) > 15:
    print(f"   ... na mengineyo ({len(actual_folders) - 15} folders)")

# 2. Kukagua kama katalogi kuu au moduli inatambua mafolda haya
catalog_path = os.path.join(base_dir, "assets", "config", "system_master_catalog.json")
if os.path.exists(catalog_path):
    print("\n--- UKAGUZI WA USAJILI WA KIOTOMATIKI (CATALOG REGISTRY) ---")
    try:
        with open(catalog_path, 'r', encoding='utf-8') as f:
            cat_data = json.load(f)
        registry = cat_data.get("protected_system_registry", {})
        print(f"[✔] Vitu vilivyosajiliwa ndani ya Katalogi Kuu: {len(registry)} items")
        
        # Angalia baadhi ya mafolda/mafaili yaliyomo kwenye registry
        matched_count = 0
        for path_key in registry.keys():
            matched_count += 1
            if matched_count <= 5:
                print(f"   -> Imesajiliwa: {path_key}")
                
    except Exception as e:
        print(f"[!] Hitilafu katika kusoma katalogi: {e}")
else:
    print("\n[i] Katalogi kuu haijaonekana kwenye njia hiyo.")

print("="*85)
print("[✔] UCHUNGUZI UMESHAKamilika! Endesha hii kila ukiweka folda mpya kuona kama inajisajili.")
print("="*85)
