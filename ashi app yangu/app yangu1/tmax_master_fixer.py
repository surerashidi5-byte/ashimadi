import os
import re

print("="*85)
print("[*] TMAX MASTER ENGINE: Inasafisha na kujipangia kila kitu upya kiotomatiki...")
print("="*85)

project_dir = "/sdcard/app yangu1"
res_dir = os.path.join(project_dir, "res")
values_dir = os.path.join(res_dir, "values")

# 1. Futa public.xml ya zamani iliyokuwa inaleta mgongano wa ID
public_xml_path = os.path.join(values_dir, "public.xml")
if os.path.exists(public_xml_path):
    os.remove(public_xml_path)
    print("[✔] Imeondoa faili lenye mgongano la public.xml.")

# 2. Safisha au tengeneza AndroidManifest.xml safi isiyo na makosa
manifest_path = os.path.join(project_dir, "AndroidManifest.xml")
clean_manifest = '''<?xml version="1.0" encoding="utf-8"?>
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

with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(clean_manifest.strip())

print("[✔] Tmax imekamilisha kusawazisha na kupanga kila kitu kwa usahihi kabisa!")
print("="*85)
