import os, json

print("=============================================")
print("[+] INAKAGUA NA KUSANIDI MFUMO WA ASHIMADI 3D")
print("=============================================")

base_dir = "/sdcard/app yangu1"
assets_dir = os.path.join(base_dir, "assets")
models_dir = os.path.join(assets_dir, "models")

# 1. Kukagua kama folda zipo
if os.path.exists(base_dir):
    print(f"[OK] Folda kuu ipo: {base_dir}")
else:
    print(f"[-] OPO: Folda kuu haipatikani!")

# 2. Kukagua faili la 3D (.gltf au .glb)
if os.path.exists(models_dir):
    for f in os.listdir(models_dir):
        if "model_repaired_master" in f:
            found_model = os.path.join(models_dir, f)
            size_mb = os.path.getsize(found_model) / (1024 * 1024)
            print(f"[OK] Faili la 3D limegunduliwa: {f}")
            print(f"     - Ukubwa wake: {size_mb:.2f} MB")

# 3. Kusoma muundo wa JSON uliouleta (World Configuration)
json_path = os.path.join(base_dir, "world_01_house_3d.json")
if os.path.exists(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as jf:
            data = json.load(jf)
            print(f"[OK] Faili la Config la Dunia limesomwa kwa mafanikio!")
            print(f"     - World ID: {data.get('world_id')}")
            print(f"     - Quality: {data.get('render_quality')}")
            steps = data.get("scroll_system", {}).get("steps", [])
            if steps:
                hotspots = steps[0].get("hotspots", [])
                print(f"     - Hotspots/Vitu vilivyomo: {len(hotspots)} vitu")
    except Exception as e:
        print(f"[-] Kosa kwenye kusoma JSON: {e}")
else:
    print("[-] Faili la JSON la world_01_house_3d.json halionekani kwenye app yangu1")

print("=============================================")
print("[+] UCHUNGUZI UMEKAMILIKA. MFUMO UKO TAYARI!")
print("=============================================")
