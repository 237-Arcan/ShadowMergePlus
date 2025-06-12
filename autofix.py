import os
import ast
import astor

ADAPTERS_PATH = "data_integration/adapters"

class SuperInitFixer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        if node.name == "__init__":
            has_super = any(
                isinstance(stmt, ast.Expr)
                and isinstance(stmt.value, ast.Call)
                and isinstance(stmt.value.func, ast.Attribute)
                and isinstance(stmt.value.func.value, ast.Name)
                and stmt.value.func.value.id == "super"
                for stmt in node.body
            )

            if not has_super:
                # Créer l'appel super().__init__()
                super_call = ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Call(func=ast.Name(id="super", ctx=ast.Load()), args=[], keywords=[]),
                            attr="__init__",
                            ctx=ast.Load(),
                        ),
                        args=[],
                        keywords=[],
                    )
                )
                node.body.insert(0, super_call)
        return node

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        source = file.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"{filepath} → ❌ Erreur de parsing : {e}")
        return

    fixer = SuperInitFixer()
    new_tree = fixer.visit(tree)
    fixed_code = astor.to_source(new_tree)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(fixed_code)
        print(f"{filepath} → ✅ super().__init__() ajouté")

def fix_all_adapters():
    for filename in os.listdir(ADAPTERS_PATH):
        if filename.endswith(".py") and not filename.startswith("__"):
            filepath = os.path.join(ADAPTERS_PATH, filename)
            fix_file(filepath)

if __name__ == "__main__":
    fix_all_adapters()
