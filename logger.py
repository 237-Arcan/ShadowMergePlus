# scripts/patch_adapters_init_with_logger.py

import os
import re

ADAPTERS_DIR = "data_integration/adapters"

def ensure_logging_import(lines):
    for line in lines:
        if "import logging" in line:
            return lines  # déjà présent
    # Ajouter en haut du fichier
    return ["import logging\n"] + lines

def patch_adapter_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    class_name = None
    inside_init = False
    indent = ""
    modified = False
    injected_lines = []
    patched_lines = []
    inserted = False

    # Chercher nom de classe principale
    for line in lines:
        match = re.match(r"class\s+(\w+)BaseAdapter:", line)
        if match:
            class_name = match.group(1)
            break

    if not class_name:
        return  # pas une classe héritée de BaseAdapter

    # Ajouter import logging si nécessaire
    lines = ensure_logging_import(lines)

    for i, line in enumerate(lines):
        if f"class {class_name}(BaseAdapter):" in line:
            patched_lines.append(line)
            continue

        # Détecter __init__
        if re.match(r"\s+def __init__.*:", line):
            inside_init = True
            indent_match = re.match(r"(\s+)", line)
            indent = indent_match.group(1) if indent_match else "    "
            patched_lines.append(line)
            continue

        if inside_init:
            if not inserted and re.match(rf"{indent}self\.", line):
                patched_lines.append(f"{indent}super().__init__()\n")
                patched_lines.append(f'{indent}self.logger = logging.getLogger("{class_name}")\n')
                inserted = True
                modified = True

        patched_lines.append(line)

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(patched_lines)
        print(f"✅ Patch appliqué à {filepath}")

def run_patch():
    print("🔧 Patching des adaptateurs avec logger...")
    for filename in os.listdir(ADAPTERS_DIR):
        if filename.endswith("_adapter.py") and filename != "base_adapter.py":
            filepath = os.path.join(ADAPTERS_DIR, filename)
            patch_adapter_file(filepath)

if __name__ == "__main__":
    run_patch()
