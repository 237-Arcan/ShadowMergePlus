# scripts/patch_adapters_init.py

import os
import re

ADAPTERS_DIR = "data_integration/adapters"

def patch_adapter_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    class_name = None
    inside_init = False
    indent = ""
    modified = False
    new_lines = []

    for i, line in enumerate(lines):
        class_match = re.match(r"class\s+(\w+)BaseAdapter:", line)
        if class_match:
            class_name = class_match.group(1)

        if class_name and re.match(r"\s+def __init__.*:", line):
            inside_init = True
            indent = re.match(r"(\s+)", line).group(1)

        if inside_init and "super().__init__()" in line:
            return  # déjà patché

        if inside_init and re.match(rf"{indent}self\.", line):
            # insérer super().__init__() juste avant la première ligne de self.*
            new_lines.append(f"{indent}super().__init__()\n")
            modified = True
            inside_init = False  # une seule insertion
            break

    if modified:
        print(f"✅ Patch appliqué à {filepath}")
        # Fusionner les nouvelles lignes dans le fichier
        patched_content = []
        inserted = False
        for line in lines:
            if not inserted and re.match(rf"{indent}self\.", line):
                patched_content.append(f"{indent}super().__init__()\n")
                inserted = True
            patched_content.append(line)

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(patched_content)

def run_patch():
    print("🔧 Patching des adaptateurs...")
    for filename in os.listdir(ADAPTERS_DIR):
        if filename.endswith("_adapter.py") and filename != "base_adapter.py":
            filepath = os.path.join(ADAPTERS_DIR, filename)
            patch_adapter_file(filepath)

if __name__ == "__main__":
    run_patch()
