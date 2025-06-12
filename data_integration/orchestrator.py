from typing import List, Dict
from .data_integration_hub import DataIntegrationHub

class DataOrchestrator:
    def __init__(self):
        self.hub = DataIntegrationHub()

    def fuse(self, source: str, match_id: str) -> dict:
        adapter = self.hub.get_adapter(source)
        if not adapter:
            raise ValueError(f"Adapter not found for source '{source}'")
        return adapter.fetch_data(match_id=match_id)

    def fuse_multiple(self, sources: List[str], match_id: str) -> Dict[str, dict]:
        results = {}
        for source in sources:
            try:
                results[source] = self.fuse(source, match_id)
            except Exception as e:
                results[source] = {"error": str(e)}
        return results
