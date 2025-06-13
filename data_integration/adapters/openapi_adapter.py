from .base_adapter import BaseAdapter

class OpenapiAdapter(BaseAdapter):
    def fetch_data(self, match_id: str) -> dict:
        # À compléter pour requêter l'OpenAPI Directory ou des APIs déclarées dynamiquement
        return {"source": "openapi", "match_id": match_id, "data": "openapi data"}
