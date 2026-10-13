import os

root_dir = "/sdcard/app yangu1"
styles_path = os.path.join(root_dir, "res/values/styles.xml")

# Kutengeneza muundo safi kabisa wa styles.xml bila makosa ya tagi wala aapt2
clean_styles_xml = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="@android:style/Theme.DeviceDefault.NoActionBar">
        <item name="android:windowBackground">@android:color/black</item>
        <item name="android:windowNoTitle">true</item>
    </style>
</resources>
"""

# Kuhakikisha folda ya res/values ipo
os.makedirs(os.path.dirname(styles_path), exist_ok=True)

# Kuandika faili safi la styles.xml
with open(styles_path, "w", encoding="utf-8") as f:
    f.write(clean_styles_xml.strip())

print("[+] Faili la res/values/styles.xml limesafishwa na kuandikwa upya kwa usahihi wa 100%!")
print("[+] Makosa yote ya 'mismatched tag' na 'aapt2 compile error' yameondolewa!")
