import os
import re
from pathlib import Path

INIT_FILE = Path("data_integration/__init__.py")
ADAPTERS_DIR = Path("data_integration/adapters")
ROOT_DIR = Path("data_integration")

def extract_imports(file_path):
    """
    Extrait tous les imports du fichier __init__.py
    et détecte si l'import vient du sous-dossier 'adapters' ou de la racine.
    """
    imports = []
    pattern = re.compile(r"from\s+\.(adapters\.)?(\w+)_adapter\s+import\s+(\w+)")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                is_adapter_subdir, module_name, class_name = match.groups()
                location = "adapters" if is_adapter_subdir else "root"
                imports.append((module_name, class_name, location))
    return imports

def find_mismatched_files(imports):
    """
    Vérifie que le nom des fichiers correspond à la casse des modules importés.
    """
    mismatches = []
    for module, _, location in imports:
        expected_name = f"{module}_adapter.py"
        base_dir = ADAPTERS_DIR if location == "adapters" else ROOT_DIR
        files = list(base_dir.glob(f"*{module}_adapter.py"))

        if not files:
            mismatches.append((location, module, "missing"))
        elif files[0].name != expected_name:
            mismatches.append((location, module, files[0].name))
    return mismatches

def fix_case_conflicts(mismatches):
    for location, module, found in mismatches:
        if found == "missing":
            print(f"[⚠️] Fichier manquant pour le module '{module}' dans {location}")
            continue
        correct_name = f"{module}_adapter.py"
        base_dir = ADAPTERS_DIR if location == "adapters" else ROOT_DIR
        src = base_dir / found
        dst = base_dir / correct_name
        print(f"[🔁] Renommage : {found} → {correct_name} dans {location}")
        os.rename(src, dst)

if __name__ == "__main__":
    print("🔍 Analyse des imports dans __init__.py...")
    imports = extract_imports(INIT_FILE)

    print("🧠 Vérification des correspondances avec les fichiers...")
    mismatches = find_mismatched_files(imports)

    if not mismatches:
        print("✅ Tous les noms de fichiers correspondent à la casse des imports.")
    else:
        print("❗ Conflits détectés :")
        for location, module, found in mismatches:
            print(f"   → {module}_adapter (attendu) ≠ {found} (trouvé dans {location})")
        fix = input("\nSouhaites-tu corriger automatiquement ces conflits ? (oui/non) ").strip().lower()
        if fix == "oui":
            fix_case_conflicts(mismatches)
            print("✅ Correction effectuée.")
        else:
            print("⛔ Aucune modification n’a été faite.")
