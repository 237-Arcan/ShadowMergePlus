import os
import re

ADAPTERS_DIR = "./data_integration/adapters"

def fix_fetch_data_signature(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex pour trouver la méthode fetch_data avec sa signature
    pattern = re.compile(r"(def fetch_dataself(?:, *[^]*)?:)")

    def replacer(match):
        signature = match.group(1)
        # Si 'match_id' ou '**kwargs' est déjà dans la signature, on ne change rien
        if 'match_id' in signature or '**kwargs' in signature:
            return signature
        # Sinon on remplace par une signature acceptant **kwargs
        return "def fetch_data(self, **kwargs):"

    new_content, count = pattern.subn(replacer, content)

    if count > 0:
        print(f"[+] Correction appliquée dans {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"[-] Pas de méthode fetch_data à corriger dans {file_path}")

def main():
    for fname in os.listdir(ADAPTERS_DIR):
        if fname.endswith(".py"):
            path = os.path.join(ADAPTERS_DIR, fname)
            fix_fetch_data_signature(path)

if __name__ == "__main__":
    main()
