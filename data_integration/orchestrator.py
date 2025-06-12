# data_integration/orchestrator.py

from data_integration.data_integration_hub import DataIntegrationHub

class DataOrchestrator:
    def __init__(self):
        self.hub = DataIntegrationHub()

    def fuse(self, source: str, match_id: str) -> dict:
        """
        Orchestration simple : appelle un seul adaptateur via le Hub
        """
        adapter = self.hub.get_adapter(source)
        if adapter is None:
            raise ValueError(f"Adaptateur introuvable pour la source : {source}")
        
        # Appelle la méthode fetch_data sur l’adaptateur
        data = adapter.fetch_data(match_id=match_id)
        
        return {
            "source": source,
            "match_id": match_id,
            "data": data
        }
