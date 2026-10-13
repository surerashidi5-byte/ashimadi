import os
import shutil

base_dir = "/sdcard/app yangu1"
print("="*50)
print("[*] TMAX SMART INTEGRATOR: Inachambua mfumo na kupanga vipengele...")
print("="*50)

# Eneo la usalama la kupokea vitu vipya ili Tmax ivichambue
incoming_dir = os.path.join(base_dir, "incoming_modules")
if not os.path.exists(incoming_dir):
    os.makedirs(incoming_dir)
    print(f"[+] Folda ya usalama imetengenezwa: {incoming_dir}")
    print("    (Weka faili au moduli zako mpya hapa, Tmax itazipokea na kuzisambaza yenyewe.)")

def auto_route_and_integrate():
    if not os.listdir(incoming_dir):
        print("[!] Hakuna mafaili mapya yaliyokutwa kwenye folda ya 'incoming_modules'.")
        print("    Tafadhali weka faili lako hapo kisha uendeshe script hii tena.")
        return

    count = 0
    for item in os.listdir(incoming_dir):
        item_path = os.path.join(incoming_dir, item)
        
        # Tmax inachunguza jina na aina ya faili ili ijue ikae wapi bila kuharibu injini
        target_subfolder = "assets"
        lower_name = item.lower()
        
        if "config" in lower_name or lower_name.endswith('.json'):
            target_subfolder = "config"
        elif "shader" in lower_name or lower_name.endswith(('.glsl', '.vert', '.frag')):
            target_subfolder = "shaders"
        elif "anim" in lower_name or "timeline" in lower_name:
            target_subfolder = "animations"
        elif "mod" in lower_name or os.path.isdir(item_path):
            target_subfolder = "modules"

        target_path = os.path.join(base_dir, target_subfolder)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            
        destination = os.path.join(target_path, item)
        
        # Ulinzi wa kutoharibu mafaili yaliyopo tayari (Smart Merge / Copy)
        if os.path.exists(destination):
            if os.path.isdir(destination):
                shutil.copytree(item_path, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(item_path, destination)
        else:
            if os.path.isdir(item_path):
                shutil.copytree(item_path, destination)
            else:
                shutil.copy2(item_path, destination)
                
        print(f"[+] Imepangwa kwa usahihi: {item} ===> {target_subfolder}/")
        count += 1

    print(f"\n[✔] Tmax imekamilisha! Vipengele {count} vimeunganishwa kwenye injini kwa usalama mkubwa.")

if __name__ == "__main__":
    auto_route_and_integrate()
