from .base_adapter import BaseAdapter

class SportsbookAdapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # Simulation pour plateformes type Betfair, Pinnacle
        return {"source": "sportsbook", "match_id": match_id, "markets": []}
