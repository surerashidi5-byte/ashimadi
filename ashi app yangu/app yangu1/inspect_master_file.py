import os
import json

print("="*85)
print("[*] TMAX ADVANCED CONTENT INSPECTOR: Inatafuta na kuchambua faili kubwa...")
print("="*85)

target_file = None
# Kutafuta faili lenye jina la model_repaired au kubwa kuliko 100MB
for root, dirs, files in os.walk("/sdcard"):
    for f in files:
        if "model_repaired" in f or "master" in f:
            f_path = os.path.join(root, f)
            try:
                size_mb = os.path.getsize(f_path) / (1024 * 1024)
                if size_mb > 50:
                    target_file = f_path
                    print(f"[✔] Limekutwa Faili: {target_file} ({size_mb:.2f} MB)")
                    break
            except:
                pass
    if target_file:
        break

if target_file:
    print("\n[*] Inasoma muundo na yaliyomo ndani ya faili hili...")
    try:
        with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
            # Kusoma vipande vya mwanzo na katikati ili kuona vitu vilivyomo
            head_content = f.read(4000)
            
        print("\n--- SEHEMU YA KWANZA YA YALIYOMO (STRUCTURE PREVIEW) ---")
        print(head_content[:1500])
        print("\n... [Imekatwa sehemu ndogo kuonyesha mfumo wa ndani] ...")
        
        # Jaribu kuchambua kama ni JSON
        try:
            with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
                data = json.load(f)
            print("\n--- UCHAMBUZI WA VITU VILIVYOMO (JSON KEYS) ---")
            if isinstance(data, dict):
                print(f"Vifungu Vikuu (Keys) Ndani ya Faili Hili: {list(data.keys())}")
                for key, val in data.items():
                    if isinstance(val, (dict, list)):
                        print(f" - [{key}]: Ina vipengele {len(val)} ndani yake.")
                    else:
                        print(f" - [{key}]: {str(val)[:50]}")
            elif isinstance(data, list):
                print(f"Faili hili ni Orodha (List) yenye vitu {len(data)} kwa ujumla.")
        except json.JSONDecodeError:
            print("\n[i] KUMBUKA: Hili ni faili la binary au lina mchanganyiko wa 3D mesh / binary streams ambazo zinabeba michoro na takwimu za launcher.")
            
    except Exception as e:
        print(f"[!] Hitilafu katika kusoma faili: {e}")
else:
    print("[!] Hatujapata faili kubwa linalofanana na hilo kwenye njia kuu. Tafadhali hakikisha lipo kwenye folda husika.")

print("="*85)
