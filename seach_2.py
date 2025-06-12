import os
import re

ADAPTERS_DIR = "./data_integration/adapters"

def add_or_fix_fetch_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Trouver la classe principale (on suppose qu'il y a une classe par fichier)
    class_line_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("class "):
            class_line_index = i
            break
    if class_line_index is None:
        print(f"[Skip] Pas de classe dans {file_path}")
        return

    # Vérifier si fetch_data existe déjà
    fetch_data_index = None
    fetch_data_signature_line = None
    for i, line in enumerate(lines):
        if re.match(r"\s+def fetch_dataself.*:", line):
            fetch_data_index = i
            fetch_data_signature_line = line
            break

    if fetch_data_index is None:
        # Pas de fetch_data, on va l'ajouter juste après le __init__ si possible, sinon après la classe
        insert_index = None
        for i in range(class_line_index + 1, len(lines)):
            if re.match(r"\s+def __init__self.*:", lines[i]):
                insert_index = i + 1
                break
        if insert_index is None:
            # pas de __init__, on insère après la déclaration de classe (ligne de classe +1)
            insert_index = class_line_index + 1

        indent = " " * 4  # 4 espaces d'indentation standard

        fetch_data_code = [
            f"{indent}def fetch_data(self, **kwargs):\n",
            f"{indent*2}\"\"\"Méthode fetch_data ajoutée automatiquement.\"\"\"\n",
            f"{indent*2}raise NotImplementedError('fetch_data doit être implémentée dans cet adaptateur')\n",
            "\n"
        ]

        lines[insert_index:insert_index] = fetch_data_code
        print(f"[Add] Ajout de fetch_data dans {file_path} à la ligne {insert_index + 1}")

    else:
        # fetch_data existe, vérifier la signature pour **kwargs
        if "**kwargs" not in fetch_data_signature_line:
            # modifier la signature pour ajouter **kwargs
            new_signature = fetch_data_signature_line.rstrip("\n").rstrip("):") + ", **kwargs):\n"
            lines[fetch_data_index] = new_signature
            print(f"[Fix] Modifié la signature de fetch_data dans {file_path} à la ligne {fetch_data_index + 1}")

    # Réécrire le fichier avec la modification
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def main():
    for fname in os.listdir(ADAPTERS_DIR):
        if fname.endswith(".py"):
            path = os.path.join(ADAPTERS_DIR, fname)
            add_or_fix_fetch_data(path)

if __name__ == "__main__":
    main()
