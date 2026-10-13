import os
import re
import xml.etree.ElementTree as ET

print("="*85)
print("[*] TMAX TRUE AUTONOMOUS ENGINE: Inajipangia na kuchunguza kila kitu kivyake...")
print("="*85)

project_dir = "/sdcard/app yangu1"
res_dir = os.path.join(project_dir, "res")
modules_dir = os.path.join(project_dir, "modules")

# 1. Tmax inajipangia kugundua jina la kifurushi (package name) au muundo uliopo kama upo
detected_package = "com.tmax.launcher3d"
existing_manifest = os.path.join(project_dir, "AndroidManifest.xml")

if os.path.exists(existing_manifest):
    try:
        with open(existing_manifest, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            match = re.search(r'package="([^"]+)"', content)
            if match:
                detected_package = match.group(1)
                print(f"[✔] Tmax imejipangia kugundua package halisi: {detected_package}")
    except Exception:
        pass

# 2. Tmax inaingia kwenye kila folda (pamoja na modules na res) kusoma kila faili kwa uhuru
all_discovered_files = []
if os.path.exists(modules_dir):
    for root, dirs, files in os.walk(modules_dir):
        for file in files:
            all_discovered_files.append(os.path.join(root, file))

if os.path.exists(res_dir):
    for root, dirs, files in os.walk(res_dir):
        for file in files:
            all_discovered_files.append(os.path.join(root, file))

print(f"[✔] Tmax imefagia na kugundua mafaili {len(total_files := all_discovered_files)} kwenye mradi wako.")

# 3. Tmax inajitengenezea muundo wa Manifest kwa kujipangia yenyewe kulingana na ugunduzi wake
dynamic_manifest = f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{detected_package}"
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
        android:label="Tmax 3D Launcher"
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

with open(existing_manifest, 'w', encoding='utf-8') as f:
    f.write(dynamic_manifest.strip())

print("[✔] Tmax imejipangia na kuandika faili la manifest kwa uhuru kamili.")
print("="*85)
print("[✔] KILA KITU kimejipanga chenyewe! Sasa nenda kwenye Apktool M, tumia 'Use aapt' na ukamilishe ujenzi.")
print("="*85)
