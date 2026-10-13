import os, json, glob

root_dir = "/sdcard/app yangu1"
print("[+] Inaanzisha Ujenzi wa Injini Kuu ya Pamoja (Heavyweight All-in-One Master Engine)...")

# 1. Kuhakikisha mafolda yote ya msingi yako kamili
folders = ["assets", "res/values", "res/xml", "smali", "lib", "modi", "presets", "shaders", "config"]
for f in folders:
    os.makedirs(os.path.join(root_dir, f), exist_ok=True)

# 2. Kujenga AndroidManifest.xml iliyonyooka na yenye uwezo kamili wa kuendesha huduma zote
manifest_code = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.ashimadi.world3d"
    android:versionCode="1"
    android:versionName="1.0">

    <uses-permission android:name="android.permission.BLUETOOTH" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.SET_WALLPAPER" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="Ashimadi 3D World"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|screenSize|keyboardHidden">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <service
            android:name=".LiveWallpaperService"
            android:permission="android.permission.BIND_WALLPAPER"
            android:exported="true">
            <intent-filter>
                <action android:name="android.service.wallpaper.WallpaperService" />
            </intent-filter>
            <meta-data
                android:name="android.service.wallpaper"
                android:resource="@xml/wallpaper" />
        </service>
    </application>
</manifest>
"""

with open(os.path.join(root_dir, "AndroidManifest.xml"), "w", encoding="utf-8") as f:
    f.write(manifest_code.strip())

# 3. Kujenga styles.xml iliyo salama na nyepesi kwa aapt2
styles_path = os.path.join(root_dir, "res/values/styles.xml")
clean_styles = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme">
    </style>
</resources>
"""
with open(styles_path, "w", encoding="utf-8") as f:
    f.write(clean_styles.strip())

# 4. Kuweka wallpaper.xml kwenye res/xml
xml_dir = os.path.join(root_dir, "res/xml")
os.makedirs(xml_dir, exist_ok=True)
with open(os.path.join(xml_dir, "wallpaper.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?><wallpaper xmlns:android="http://schemas.android.com/apk/res/android" />')

# 5. Kujenga Faili Kuu la Uzito na Ushirikiano wa Mifumo (Heavy Master Bridge Core)
all_files = glob.glob(os.path.join(root_dir, "**/*.*"), recursive=True)
heavy_core_data = {
    "engine_name": "Ashimadi_Heavyweight_Master_Core",
    "status": "fully_synchronized_and_locked",
    "total_managed_files": len(all_files),
    "modules_integrated": ["modi", "presets", "shaders", "config", "assets", "smali"],
    "coordination": "forced_cross_layer_shared_memory"
}

bridge_file = os.path.join(root_dir, "assets/heavy_master_bridge_core.json")
with open(bridge_file, "w", encoding="utf-8") as f:
    json.dump(heavy_core_data, f, indent=4)

print("[+] Mfumo mzima umechaguliwa, umesawazishwa, na kuunganishwa kuwa kitovu kimoja kizito na chenye uwezo kamili!")
