from .base_adapter import BaseAdapter

class GithubAdapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # Simulation d'une interrogation GitHub locale
        return {"source": "github", "match_id": match_id, "info": "github repo data"}
