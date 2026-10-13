import os
import re

# Njia kuu ya mradi
base_dir = "/sdcard/app yangu1"
print("[*] Tmax inaanza uchambuzi wa kina wa mfumo wako...")

# --- 1. Uchambuzi wa Mfumo (System Analysis) ---
package_name = "com.ashimadi.launcher3d"
main_activity = "MainActivity"
required_permissions = set()
features_required = set()
screens_fullscreen = False

print("[*] Inachambua mafaili yote ili kuelewa utendaji...")

total_files_scanned = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        total_files_scanned += 1
        file_path = os.path.join(root, file)
        
        # Uchambuzi wa mafaili ya msimbo (mfano: .smali, .py, .java, .json)
        # ili kugundua ruhusa (permissions) zinazohitajika na vipengele vinavyotumiwa.
        if file.endswith(('.smali', '.py', '.java', '.json', '.xml')):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    # Gundua matumizi ya Internet
                    if re.search(r'HttpURLConnection|HttpClient|connect|socket', content, re.IGNORECASE):
                        required_permissions.add("android.permission.INTERNET")
                    
                    # Gundua matumizi ya Hifadhi ya Nje
                    if re.search(r'getExternalStorage|sdcard|writeStream|readStream', content, re.IGNORECASE):
                        required_permissions.add("android.permission.WRITE_EXTERNAL_STORAGE")
                        required_permissions.add("android.permission.READ_EXTERNAL_STORAGE")

                    # Gundua matumizi ya Kamera
                    if re.search(r'Camera|takePicture|openCamera', content, re.IGNORECASE):
                        required_permissions.add("android.permission.CAMERA")
                        features_required.add("android.hardware.camera")
                    
                    # Gundua matumizi ya OpenGL/Injini ya 3D
                    if re.search(r'GLES|GLSurfaceView|Shader|render|OpenGLES', content, re.IGNORECASE):
                        features_required.add("android.hardware.opengles.version")

                    # Gundua mahitaji ya kioo kizima (Fullscreen)
                    if re.search(r'FLAG_FULLSCREEN|windowFullscreen|NoActionBar', content, re.IGNORECASE):
                        screens_fullscreen = True

                    # Jaribu kugundua jina la package na Main Activity
                    if "package" in file.lower() and file.endswith('.json'):
                        import json
                        try:
                            data = json.loads(content)
                            if "package" in data: package_name = data["package"]
                            if "main_activity" in data: main_activity = data["main_activity"]
                        except: pass

            except:
                pass

print(f"[+] Uchambuzi umekamilika. Mafaili {total_files_scanned} yamekaguliwa.")
print(f"    - Ruhusa zilizogunduliwa: {list(required_permissions)}")
print(f"    - Vipengele vilivyogunduliwa: {list(features_required)}")
print(f"    - Mahitaji ya Kioo Kizima (Fullscreen): {screens_fullscreen}")

# --- 2. Ujenzi wa Manifest (Manifest Construction) ---
print("[*] Tmax inaanza kujenga AndroidManifest.xml kulingana na uchambuzi...")

manifest_path = os.path.join(base_dir, "AndroidManifest.xml")

# Jenga orodha ya ruhusa (permissions)
permissions_xml = ""
for perm in sorted(required_permissions):
    permissions_xml += f'    <uses-permission android:name="{perm}" />\n'

# Jenga orodha ya vipengele (features)
features_xml = ""
for feat in sorted(features_required):
    if feat == "android.hardware.opengles.version":
        features_xml += '    <uses-feature android:name="android.hardware.opengles.version" android:required="true" android:glEsVersion="0x00020000" />\n'
    else:
        features_xml += f'    <uses-feature android:name="{feat}" android:required="false" />\n'

# Jenga muundo kamili wa Manifest kulingana na data iliyokusanywa
manifest_content = f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{package_name}"
    android:versionCode="1"
    android:versionName="1.0" >

    <uses-sdk
        android:minSdkVersion="21"
        android:targetSdkVersion="33" />

    <!-- Ruhusa zilizogunduliwa kupitia uchambuzi -->
{permissions_xml}
    <!-- Vipengele vilivyogunduliwa kupitia uchambuzi -->
{features_xml}
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="Launcher 3D"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme" >
        
        <!-- Shughuli Kuu iliyogunduliwa -->
        <activity
            android:name="{package_name}.{main_activity}"
            android:exported="true"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:theme="@style/AppTheme" >
            <intent-filter>
                <action android:name="android:intent.action.MAIN" />
                <category android:name="android:intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
        <!-- Mipangilio ya ziada ya kulingana na uchambuzi -->
        <meta-data android:name="android.max_aspect" android:value="2.1" />
    </application>

</manifest>
"""

with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(manifest_content)
print("[+] AndroidManifest.xml imetengenezwa upya kikamilifu kulingana na mfumo wako na uchambuzi wa Tmax.")

print("\n[✔] Tmax imekamilisha uchambuzi na ujenzi upya wa Manifest!")
print("Sasa unaweza kurudi kwenye Apktool M na kujaribu kujenga (Build) tena.")
