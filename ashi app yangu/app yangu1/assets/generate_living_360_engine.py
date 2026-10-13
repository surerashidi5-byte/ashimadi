import json
import os

# ============================================================
DIRECTORY SETUP & CONFIGURATION
# ============================================================
base_dir = "assets"
dirs = [
    os.path.join(base_dir, "worlds"),
    os.path.join(base_dir, "shaders"),
    os.path.join(base_dir, "locales"),
    os.path.join(base_dir, "config"),
    os.path.join(base_dir, "presets"),
    "docs"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

print("Folders initialized successfully.")
