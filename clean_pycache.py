import os
import shutil

def delete_pycache(root_dir):
    deleted = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname == '__pycache__':
                pycache_path = os.path.join(dirpath, dirname)
                try:
                    shutil.rmtree(pycache_path)
                    print(f"[🗑️] Supprimé : {pycache_path}")
                    deleted += 1
                except Exception as e:
                    print(f"[⚠️] Erreur lors de la suppression de {pycache_path} : {e}")
    print(f"\n✅ Suppression terminée : {deleted} dossier(s) '__pycache__' supprimé(s).")

if __name__ == "__main__":
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    delete_pycache(PROJECT_ROOT)
