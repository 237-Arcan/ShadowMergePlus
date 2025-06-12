# fix_adapters.py
import os

ADAPTER_DIR = "data_integration/adapters"

for filename in os.listdir(ADAPTER_DIR):
    if filename.endswith("_adapter.py"):
        filepath = os.path.join(ADAPTER_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        base = filename.replace("_adapter.py", "")
        class_name = "".join(word.capitalize() for word in base.split("_")) + "Adapter"

        if class_name not in content:
            print(f"⚠️ Classe {class_name} absente dans {filename}. Insertion en cours...")
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(f"\n\nclass {class_name}(BaseAdapter):\n    pass\n")

print("✅ Correction terminée.")
