import logging
from data_integration.github_adapter import GithubAdapter

class DataIntegrationHub:
    def __init__(self):
        self.adapters = {}
        self._initialize_adapters()

    def _initialize_adapters(self):
        try:
            self.adapters['github'] = GithubAdapter(
                repo_path="data_sources/soccerdata"  # Exemple, à adapter selon les dépôts
            )
            logging.info("Adaptateur Github initialisé.")
        except Exception as e:
            logging.error(f"Erreur lors de l'initialisation de GithubAdapter : {e}")

    def get_adapter(self, name):
        return self.adapters.get(name, None)

    def list_all_files(self):
        results = {}
        for name, adapter in self.adapters.items():
            try:
                results[name] = adapter.list_files(adapter.repo_path)
            except Exception as e:
                logging.warning(f"Erreur lors de la lecture via {name} : {e}")
        return results
