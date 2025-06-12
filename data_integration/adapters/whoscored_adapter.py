from .base_adapter import BaseAdapter

class WhoscoredAdapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # Simulation de données WhoScored
        return {"source": "whoscored", "match_id": match_id, "players": []}
