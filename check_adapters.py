# check_adapters.py
import os
import re

ADAPTER_DIR = "data_integration/adapters"
errors = []

for filename in os.listdir(ADAPTER_DIR):
    if filename.endswith("_adapter.py"):
        filepath = os.path.join(ADAPTER_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        base = filename.replace("_adapter.py", "")
        expected_class_name = "".join(word.capitalize() for word in base.split("_")) + "Adapter"

        if expected_class_name not in content:
            errors.append((filename, expected_class_name))

print("🔍 Résultat de la vérification des adaptateurs :\n")
if not errors:
    print("✅ Tous les adaptateurs contiennent leur classe correspondante.")
else:
    for filename, class_name in errors:
        print(f"❌ {filename} → Classe attendue absente : {class_name}")
