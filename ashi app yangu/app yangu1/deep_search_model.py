import os

target_filename = "model_repaired_master"
found_path = None

print("[+] Inatafuta faili la 3D kwa kina kuanzia kwenye mizizi ya app yangu1...")

for root, dirs, files in os.walk("."):
    for file in files:
        if "model_repaired" in file or file.endswith(".glb") or file.endswith(".gltf") or file.endswith(".obj"):
            full_path = os.path.abspath(os.path.join(root, file))
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            print(f"\n[!] LIMEGUNDULIWA:")
            print(f" - Jina: {file}")
            print(f" - Njia kamili: {full_path}")
            print(f" - Ukubwa: {size_mb:.2f} MB")
            
            # Kusoma saini ya mwanzo (Header) ili kuhakikisha ubora wake
            with open(full_path, "rb") as f:
                header = f.read(16)
                print(f" - Saini (Hex): {header.hex()}")

