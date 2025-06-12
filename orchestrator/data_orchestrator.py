from data_integration.data_integration_hub import DataIntegrationHub

class DataOrchestrator:
    def __init__(self):
        self.hub = DataIntegrationHub()

    def collect_match_data(self, match_id: str) -> dict:
        """
        Collecte les données issues de tous les adaptateurs disponibles pour un match donné.

        :param match_id: identifiant unique du match
        :return: dictionnaire unifié contenant les données par source
        """
        all_data = {}
        adapters = self.hub.get_available_adapters()
        for name, adapter in adapters.items():
            try:
                data = adapter.fetch_data(match_id)
                all_data[name] = data
            except Exception as e:
                all_data[name] = {"error": str(e)}
        return all_data
