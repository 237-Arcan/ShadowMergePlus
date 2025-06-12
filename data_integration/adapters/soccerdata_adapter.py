from .base_adapter import BaseAdapter

class SoccerdataAdapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # Simulation d'intégration soccerdata
        return {"source": "soccerdata", "match_id": match_id, "stats": {"shots": 10, "corners": 5}}
