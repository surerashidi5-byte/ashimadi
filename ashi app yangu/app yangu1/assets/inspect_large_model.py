import os

target_dir = "model"
if os.path.exists(target_dir):
    print(("[+] Inachunguza mafaili ndani ya folda ya model..."))
    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        if os.path.isfile(filepath):
            size_mb = os.path.getsize(filepath) / (1024 * 1024)
            print(f"\n[FILE]: {filename}")
            print(f"[SIZE]: {size_mb:.2f} MB")
            
            # Kusoma bafu za mwanzo (header) ili kujua aina ya faili
            with open(filepath, "rb") as f:
                header_bytes = f.read(32)
                print(f"[HEADER BYTES]: {header_bytes}")
else:
    print("[-] Folda ya model haipatikani kwenye njia hii!")
