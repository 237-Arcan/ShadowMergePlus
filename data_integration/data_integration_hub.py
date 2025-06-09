# data_integration/data_integration_hub.py

import logging

from data_integration.adapters.bet365_adapter import Bet365Adapter
from data_integration.adapters.github_adapter import GithubAdapter
from data_integration.adapters.openapi_adapter import OpenAPIAdapter
from data_integration.adapters.soccerdata_adapter import SoccerDataAdapter
from data_integration.adapters.sports_betting_adapter import SportsBettingAdapter
from data_integration.adapters.sportsbook_adapter import SportsBookAdapter
from data_integration.adapters.whoscored_adapter import WhoscoredAdapter

ADAPTERS_CATALOG = {
    "Bet365Adapter": Bet365Adapter,
    "GithubAdapter": GithubAdapter,
    "OpenAPIAdapter": OpenAPIAdapter,
    "SoccerDataAdapter": SoccerDataAdapter,
    "SportsBettingAdapter": SportsBettingAdapter,
    "SportsBookAdapter": SportsBookAdapter,
    "WhoscoredAdapter": WhoscoredAdapter,
}

REPO_BASE_PATH = "./data_sources/"

class DataIntegrationHub:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.adapters = self.get_available_adapters()

    def get_available_adapters(self):
        available_adapters = {}

        for name, adapter_cls in ADAPTERS_CATALOG.items():
            try:
                instance = adapter_cls(repo_path=f"{REPO_BASE_PATH}{name}")
                if instance.is_available():
                    available_adapters[name] = instance
                    self.logger.info(f"[Hub] Adaptateur disponible : {name}")
            except Exception as e:
                self.logger.warning(f"[Hub] Échec {name} : {e}")

        return available_adapters

    def fetch_data(self, source_name, **kwargs):
        adapter = self.adapters.get(source_name)
        if not adapter:
            raise ValueError(f"Source inconnue : {source_name}")
        return adapter.fetch_data(**kwargs)
