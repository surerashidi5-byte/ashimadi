import os
import json

modules_dir = "/sdcard/app yangu1/modules"
target_file = None

if os.path.exists(modules_dir):
    for f in os.listdir(modules_dir):
        if "model_repaired_master" in f:
            target_file = os.path.join(modules_dir, f)
            break

print("="*85)
print("[*] TMAX DETAILED MODULE LIST & TASK VIEWER")
print("="*85)

if target_file and os.path.exists(target_file):
    try:
        with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Jaribu kutafuta JSON data au vipengele vyake
        data = json.loads(content)
        print(f"[✔] Faili limefikiwa kwa mafanikio: {os.path.basename(target_file)}")
        
        # Kuangalia kama lina orodha ya faili zilizosajiliwa ndani
        files_list = []
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict) and 'file_name' in item:
                            files_list.append(item)
                elif isinstance(v, dict):
                    for sub_k, sub_v in v.items():
                        if isinstance(sub_v, dict) and 'file_name' in sub_v:
                            files_list.append(sub_v)
                            
        # Kama hakuna list ya moja kwa moja, tutachimbua muundo wake
        print(f"\n--- ORODHA YA MAFAILI NA KAZI ZAKE NDANI YA MODULI ---")
        if files_list:
            for idx, file_obj in enumerate(files_list, 1):
                fname = file_obj.get('file_name', f'Module_{idx}')
                status = file_obj.get('status', 'ACTIVE')
                print(f"{idx}. 📄 Majina: {fname}")
                print(f"   ⚙️ Hali/Kazi: {status}")
                if 'data' in file_obj:
                    print(f"   📊 Maelezo: {file_obj['data']}")
                print("-" * 50)
        else:
            print("[i] Faili hili lina miundo ya ndani ya 3D/JSON. Hapa kuna muhtasari wa funguo zake kuu:")
            for key in data.keys():
                print(f"   - Kipengele: {key}")
                
    except json.JSONDecodeError:
        print("[!] Faili lina muundo wa binary au linahitaji usomaji maalum wa JSON chunks.")
    except Exception as e:
        print(f"[!] Hitilafu: {e}")
else:
    print("[!] Faili kubwa la moduli halikuonekana kwenye folda ya modules.")

print("="*85)
