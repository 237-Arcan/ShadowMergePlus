from .base_adapter import BaseAdapter

class SportsBettingAdapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # Simulation d'historique de paris sportifs
        return {"source": "sports_betting", "match_id": match_id, "bets": []}
