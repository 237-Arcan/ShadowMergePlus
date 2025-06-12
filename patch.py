import os
import re
import shutil

TARGET_PATH = "data_integration/data_integration_hub.py"
BACKUP_PATH = TARGET_PATH + ".bak"
PATCH_SIGNATURE = "# PATCHED_BY_DYNAMIC_LOADER_PATCH"

PATCHED_FUNC = f'''
    {PATCH_SIGNATURE}
    def load_adapters(self):
        \"\"\"
        Charge dynamiquement tous les adaptateurs du dossier adapters
        et les enregistre dans le dictionnaire self.adapters
        \"\"\"
        import importlib.util
        import os
        import inspect

        adapters_dir = os.path.join(os.path.dirname(__file__), "adapters")
        for filename in os.listdir(adapters_dir):
            if filename.endswith("_adapter.py"):
                module_name = filename[:-3]  # ex: bet365_adapter
                repo_name = module_name.replace("_adapter", "")  # ex: bet365
                class_name = ''.join([part.capitalize() for part in module_name.split('_')])

                file_path = os.path.join(adapters_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                adapter_class = getattr(module, class_name, None)
                if adapter_class:
                    try:
                        sig = inspect.signature(adapter_class.__init__)
                        params = list(sig.parameters.values())[1:]  # skip 'self'
                        if any(p.name == 'repo_path' for p in params):
                            instance = adapter_class(repo_path=f"./data_sources/{repo_name}")
                        else:
                            instance = adapter_class()
                        self.adapters[repo_name] = instance
                    except Exception as e:
                        print(f"[ERREUR] Instanciation échouée pour {{class_name}}: {{e}}")
'''

def patch_loader():
    if not os.path.exists(TARGET_PATH):
        print(f"[❌] Fichier introuvable : {TARGET_PATH}")
        return

    with open(TARGET_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    if PATCH_SIGNATURE in content:
        print("[ℹ️] Patch déjà appliqué.")
        return

    shutil.copy(TARGET_PATH, BACKUP_PATH)
    print(f"[✔️] Sauvegarde créée : {BACKUP_PATH}")

    # Remplace l'ancienne version de load_adapters()
    new_content = re.sub(
        r'def load_adaptersself:.*?(?=^\s+def |\Z)',
        PATCHED_FUNC,
        content,
        flags=re.DOTALL | re.MULTILINE
    )

    with open(TARGET_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("[✅] Patch appliqué avec succès.")

if __name__ == "__main__":
    patch_loader()
