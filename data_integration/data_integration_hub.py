import os
import importlib.util
import inspect

class DataIntegrationHub:
    def __init__(self):
        self.adapters = {}
        self.load_adapters()

    def load_adapters(self):
        """
        Charge dynamiquement tous les adaptateurs du dossier adapters
        et les enregistre dans le dictionnaire self.adapters
        """
        adapters_dir = os.path.join(os.path.dirname(__file__), "adapters")

        for filename in os.listdir(adapters_dir):
            if filename.endswith("_adapter.py"):
                module_name = filename[:-3]  # Exemple: bet365_adapter
                repo_name = module_name.replace("_adapter", "")  # Exemple: bet365
                class_name = ''.join([part.capitalize() for part in module_name.split('_')])

                file_path = os.path.join(adapters_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                adapter_class = getattr(module, class_name, None)
                if adapter_class:
                    try:
                        sig = inspect.signature(adapter_class.__init__)
                        params = list(sig.parameters.values())[1:]  # on saute 'self'
                        if any(p.name == 'repo_path' for p in params):
                            instance = adapter_class(repo_path=f"./data_sources/{repo_name}")
                        else:
                            instance = adapter_class()
                        self.adapters[repo_name] = instance
                    except Exception as e:
                        print(f"[ERREUR] Instanciation échouée pour {class_name}: {e}")

def get_adapter(self, name):
        """
        Retourne l'instance d'adaptateur correspondant au nom donné
        """
        adapter = self.adapters.get(name)
        if not adapter:
            raise ValueError(f"Aucun adaptateur trouvé pour la source : {name}")
        return adapter
