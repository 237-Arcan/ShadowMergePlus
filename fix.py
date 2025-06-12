import os

ADAPTERS_DIR = "data_integration/adapters"
IMPORT_LINE_TO_REPLACE = "from .base_adapter import BaseAdapter"
NEW_IMPORT_LINE = "from data_integration.adapters.base_adapter import BaseAdapter"

# Fichiers à exclure
EXCLUDE_FILES = {"base_adapter.py", "__init__.py"}

def fix_imports():
    for filename in os.listdir(ADAPTERS_DIR):
        if filename.endswith(".py") and filename not in EXCLUDE_FILES:
            filepath = os.path.join(ADAPTERS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if IMPORT_LINE_TO_REPLACE in content:
                print(f"🔧 Mise à jour : {filename}")
                new_content = content.replace(IMPORT_LINE_TO_REPLACE, NEW_IMPORT_LINE)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
            else:
                print(f"✅ Déjà correct ou pas concerné : {filename}")

if __name__ == "__main__":
    fix_imports()
