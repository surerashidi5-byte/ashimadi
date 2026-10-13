import os
import shutil
import re

print("="*85)
print("[*] TMAX ISOLATED PROXY ENGINE: Inatengeneza folda maalum ya kiunganishi kwa ajili ya aapt2...")
print("="*85)

source_project_dir = "/sdcard/app yangu1"
isolated_build_dir = os.path.join(source_project_dir, "tmax_build_workspace")

# 1. Tengeneza au safisha folda maalum ya kujengea (Isolated Workspace)
if os.path.exists(isolated_build_dir):
    shutil.rmtree(isolated_build_dir)
os.makedirs(isolated_build_dir, exist_ok=True)

print(f"[✔] Folda maalum ya kiunganishi imetengenezwa hapa: {isolated_build_dir}")

# 2. Nakili rasilimali muhimu na moduli kwenda kwenye folda maalum ya proxy
for item in ["res", "assets", "AndroidManifest.xml"]:
    src_path = os.path.join(source_project_dir, item)
    if os.path.exists(src_path):
        if os.path.isdir(src_path):
            shutil.copytree(src_path, os.path.join(isolated_build_dir, item))
        else:
            shutil.copy2(src_path, os.path.join(isolated_build_dir, item))

print("[✔] Rasilimali zote zimewekwa kwenye mfumo wa kusoma wa kando (Proxy Layer).")

# 3. Safisha na ujenge public.xml ya kipekee ndani ya folda maalum ili aapt2 isome bila migongano
isolated_res_dir = os.path.join(isolated_build_dir, "res")
isolated_values_dir = os.path.join(isolated_res_dir, "values")
os.makedirs(isolated_values_dir, exist_ok=True)

public_xml_path = os.path.join(isolated_values_dir, "public.xml")
public_content = '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'

seen_names = set()
resource_counter = 0

if os.path.exists(isolated_res_dir):
    for root, dirs, files in os.walk(isolated_res_dir):
        for file in files:
            if file.endswith(".xml") and file != "public.xml":
                folder_name = os.path.basename(root)
                if folder_name.startswith("values"):
                    res_type = "string"
                elif folder_name.startswith("drawable") or folder_name.startswith("mipmap"):
                    res_type = "drawable"
                elif folder_name.startswith("layout"):
                    res_type = "layout"
                else:
                    res_type = "id"
                
                res_name = os.path.splitext(file)[0]
                clean_res_name = re.sub(r'[^a-zA-Z0-9_]', '_', res_name).lower()
                
                if clean_res_name not in seen_names and len(clean_res_name) > 0:
                    seen_names.add(clean_res_name)
                    unique_id = f"0x7f01{resource_counter:04x}"
                    public_content += f'    <public type="{res_type}" name="{clean_res_name}" id="{unique_id}" />\n'
                    resource_counter += 1

public_content += '</resources>'

with open(public_xml_path, 'w', encoding='utf-8') as f:
    f.write(public_content)

print(f"[✔] Jedwali la public.xml la kiunganishi limeundwa na rasilimali {resource_counter} zimesawazishwa!")

# 4. Hakikisha AndroidManifest.xml ya kwenye folda maalum iko safi kabisa
isolated_manifest_path = os.path.join(isolated_build_dir, "AndroidManifest.xml")
proxy_manifest = '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.ashmali.launcher3d"
    android:versionCode="1"
    android:versionName="1.0">

    <uses-sdk
        android:minSdkVersion="21"
        android:targetSdkVersion="34" />

    <uses-feature
        android:glEsVersion="0x00020000"
        android:required="true" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="Ashmali 3D Launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen">
        
        <activity
            android:name=".HomeActivity"
            android:exported="true"
            android:screenOrientation="sensor">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
    </application>
</manifest>
'''

with open(isolated_manifest_path, 'w', encoding='utf-8') as f:
    f.write(proxy_manifest.strip())

print("[✔] Kila kitu kimekamilika! Sasa aapt2 inaweza kusoma folda hii maalum bila kukwama.")
print("="*85)
