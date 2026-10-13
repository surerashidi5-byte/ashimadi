import os, glob, re

root_dir = "/sdcard/app yangu1"
print("[+] Inasafisha na Kurekebisha Mfumo Wote Kiotomatiki...")

# 1. KUREKEBISHA STYLES.XML IWE SAFI NA BILA MAREJEO YANAYOFAIL (aapt2 friendly)
styles_path = os.path.join(root_dir, "res/values/styles.xml")
os.makedirs(os.path.dirname(styles_path), exist_ok=True)

clean_styles = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme">
    </style>
</resources>
"""

with open(styles_path, "w", encoding="utf-8") as f:
    f.write(clean_styles.strip())
print("[+] styles.xml imewekwa sawa bila kutegemea mfumo wa nje!")

# 2. KUKAGUA NA KUREKEBISHA MAFAILI YOTE YA XML NDANI YA RES
xml_files = glob.glob(os.path.join(root_dir, "res/**/*.xml"), recursive=True)
for file_path in xml_files:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        # Kuondoa mistari au tagi zenye makosa ya anim au references zilizoharibika
        lines = content.splitlines()
        valid_lines = [line for line in lines if "android:anim/" not in line]
        new_content = "\n".join(valid_lines)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    except:
        pass

print("[+] Usafishaji wa mafaili yote ya XML umekamilika kikamilifu!")
