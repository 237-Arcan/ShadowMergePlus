import os
import re
import importlib.util

INIT_PATH = "data_integration/__init__.py"
ADAPTERS_PATH = "data_integration/adapters"

def extract_imports(init_file):
    with open(init_file, "r") as f:
        lines = f.readlines()
    
    pattern = re.compile(r"from \.adapters\.(\w+)_adapter import (\w+)")
    imports = []

    for line in lines:
        match = pattern.search(line)
        if match:
            module, class_name = match.groups()
            imports.append((module, class_name))
    return imports

def check_class_in_module(module_file, expected_class):
    path = os.path.join(ADAPTERS_PATH, f"{module_file}_adapter.py")
    if not os.path.exists(path):
        return f"❌ Fichier manquant : {path}"
    
    with open(path, "r") as f:
        content = f.read()

    # Cherche une définition de classe avec le nom attendu
    class_pattern = re.compile(rf"class\s+{expected_class}\b")
    if class_pattern.search(content):
        return f"✅ {expected_class} bien défini dans {module_file}_adapter.py"
    else:
        # Suggestion : retrouve une classe proche si possible
        class_names = re.findall(r"class\s+(\w+)\b", content)
        if class_names:
            suggestion = f"⚠️ Classe définie : {class_names[0]}, attendu : {expected_class}"
        else:
            suggestion = "⚠️ Aucune classe détectée"
        return f"❌ Mauvaise casse ou nom pour {expected_class} dans {module_file}_adapter.py – {suggestion}"

def main():
    print("🔍 Vérification des imports dans __init__.py...\n")
    imports = extract_imports(INIT_PATH)
    
    for module_name, class_name in imports:
        result = check_class_in_module(module_name, class_name)
        print(result)

if __name__ == "__main__":
    main()
