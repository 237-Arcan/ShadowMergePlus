import os

def ensure_init_py(directories):
    """
    Ajoute un fichier __init__.py vide dans chaque dossier de la liste s'il n'existe pas déjà.
    """
    for directory in directories:
        init_path = os.path.join(directory, "__init__.py")
        if not os.path.exists(directory):
            print(f"Le dossier '{directory}' n'existe pas. Création...")
            os.makedirs(directory)
        if not os.path.exists(init_path):
            with open(init_path, "w", encoding="utf-8") as f:
                pass  # Fichier vide
            print(f"Créé : {init_path}")
        else:
            print(f"Déjà présent : {init_path}")

if __name__ == "__main__":
    # Liste des dossiers à traiter à la racine du projet
    target_dirs = ["fusion", "triggers", "insights"]
    ensure_init_py(target_dirs)
