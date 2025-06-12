from .base_adapter import BaseAdapter

class Bet365Adapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # Simulation d'appel à une API Bet365
        return {"source": "bet365", "match_id": match_id, "odds": {"home": 1.8, "draw": 3.2, "away": 4.5}}
