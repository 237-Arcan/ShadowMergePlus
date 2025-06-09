import os
import re

BASE_DIR = "data_integration"
ADAPTERS_DIR = os.path.join(BASE_DIR, "adapters")
INIT_FILE = os.path.join(BASE_DIR, "__init__.py")

def find_adapters():
    adapters = []
    for root, _, files in os.walk(ADAPTERS_DIR):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                path = os.path.join(root, file)
                with open(path, encoding="utf-8") as f:
                    content = f.read()
                matches = re.findall(r"class\s+(\w+Adapter)\b", content)
                for match in matches:
                    rel_path = os.path.relpath(path, BASE_DIR).replace(os.sep, ".")[:-3]
                    adapters.append((match, rel_path))
    return adapters

def update_init(adapters):
    header = "# Auto-generated imports - Ne pas modifier manuellement\n\n"
    footer = "\n# Fin des imports auto-générés\n"
    lines = [header]
    for class_name, rel_path in adapters:
        lines.append(f"from .{rel_path} import {class_name}\n")
    lines.append(footer)

    with open(INIT_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Fichier {INIT_FILE} mis à jour avec {len(adapters)} adaptateurs.")

if __name__ == "__main__":
    adapters = find_adapters()
    update_init(adapters)
