import os
import re

manifest_path = "AndroidManifest.xml"
print("="*85)
print("[*] TMAX AUTONOMOUS MANIFEST ENGINE: Inakagua na kurekebisha AndroidManifest.xml...")
print("="*85)

if os.path.exists(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # 1. Hakikisha namespace kuu ya android ipo kwenye manifest tag
    if 'xmlns:android' not in content:
        content = content.replace('<manifest', '<manifest xmlns:android="http://schemas.android.com/apk/res/android"', 1)
        print("[✔] Imeongeza namespace sahihi ya android kwenye manifest.")
        
    # 2. Rekebisha migongano ya <uses-feature> ambapo android:name na android:glEsVersion viko pamoja
    # Tutagawanya ili zikae kwa usahihi kisheria ya aapt2
    def fix_uses_feature(match):
        tag_content = match.group(0)
        if 'glEsVersion' in tag_content and 'name' in tag_content:
            # Tenganisha ziwe tags mbili tofauti au safisha iliyo sahihi
            return '<uses-feature android:glEsVersion="0x00020000" android:required="true" />'
        return tag_content

    content = re.sub(r'<uses-feature[^>]+>', fix_uses_feature, content)
    
    # 3. Hakikisha sifa za msingi za app hazina upungufu wa namba au majina
    if 'android:versionCode' not in content:
        content = content.replace('<manifest', '<manifest android:versionCode="1" android:versionName="1.0"', 1)
        print("[✔] Imeongeza versionCode na versionName zilizokosekana.")

    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("[✔] MAFANIKIO: Faili la AndroidManifest.xml limetakaswa na kusanifiwa kikamilifu na Tmax!")
else:
    print("[!] Hitilafu: Faili la AndroidManifest.xml halikuonekana katika saraka ya sasa.")

print("="*85)
