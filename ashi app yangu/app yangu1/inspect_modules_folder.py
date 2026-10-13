import os

modules_dir = "/sdcard/app yangu1/modules"
print("="*85)
print("[*] TMAX DIRECT MODULES INSPECTOR: Inachunguza ndani ya folda ya modules...")
print("="*85)

if os.path.exists(modules_dir):
    items = os.listdir(modules_dir)
    print(f"[✔] Jumla ya vitu vilivyomo kwenye folda ya modules: {len(items)}\n")
    
    for item in items:
        item_path = os.path.join(modules_dir, item)
        if os.path.isfile(item_path):
            size_mb = os.path.getsize(item_path) / (1024 * 1024)
            print(f"   📄 [FAILI] {item} ({size_mb:.2f} MB)")
        elif os.path.isdir(item_path):
            sub_items = os.listdir(item_path)
            print(f"   📁 [FOLDA] {item}/ (Ina vitu {len(sub_items)} ndani)")
            
    print("\n--- UCHAMBUZI WA KINA WA FAILI KUBWA ---")
    for item in items:
        if "model" in item.lower() or "master" in item.lower():
            target_file = os.path.join(modules_dir, item)
            sz = os.path.getsize(target_file) / (1024 * 1024)
            print(f"[*] Inasoma muundo wa mwanzo wa {item}...")
            try:
                with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
                    snippet = f.read(600)
                print(f"   -> Vipengele vya mwanzo:\n{snippet}\n")
            except Exception as e:
                print(f"   -> Imesoma kama binary au data maalum ya 3D. (Hitilafu ndogo: {e})")
else:
    print(f"[!] Folda ya modules haikuonekana katika njia hii: {modules_dir}")

print("="*85)
