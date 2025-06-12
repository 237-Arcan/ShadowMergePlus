import os
import ast

ADAPTERS_PATH = "data_integration/adapters"

def check_missing_super_init():
    results = []

    for filename in os.listdir(ADAPTERS_PATH):
        if not filename.endswith(".py") or filename.startswith("__"):
            continue

        filepath = os.path.join(ADAPTERS_PATH, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            try:
                tree = ast.parse(file.read(), filename=filename)
            except SyntaxError as e:
                results.append((filename, f"❌ Erreur de parsing : {e}"))
                continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                init_found = False
                super_called = False

                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                        init_found = True
                        for stmt in ast.walk(item):
                            if isinstance(stmt, ast.Call) and isinstance(stmt.func, ast.Attribute):
                                if stmt.func.attr == "__init__":
                                    if isinstance(stmt.func.value, ast.Name) and stmt.func.value.id == "super":
                                        super_called = True

                if init_found and not super_called:
                    results.append((filename, f"⚠️ Classe '{node.name}' a un __init__() mais sans super().__init__()"))

    return results

if __name__ == "__main__":
    warnings = check_missing_super_init()
    if not warnings:
        print("✅ Tous les adaptateurs appellent bien super().__init__()")
    else:
        for filename, msg in warnings:
            print(f"{filename} → {msg}")
