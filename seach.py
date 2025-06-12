import os
import re

ADAPTERS_DIR = "./data_integration/adapters"

def check_fetch_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    matches = re.findall(r"def fetch_dataself(.*?):", content)
    if matches:
        for sig in matches:
            print(f"[Found] fetch_data signature in {file_path}: (self{sig})")
    else:
        print(f"[Missing] Pas de méthode fetch_data dans {file_path}")

def main():
    for fname in os.listdir(ADAPTERS_DIR):
        if fname.endswith(".py"):
            path = os.path.join(ADAPTERS_DIR, fname)
            check_fetch_data(path)

if __name__ == "__main__":
    main()
