import logging

from data_integration.adapters.openapi_adapter import OpenAPIAdapter
from data_integration.adapters.soccerdata_adapter import SoccerDataAdapter
from data_integration.adapters.sports_betting_adapter import SportsBettingAdapter
from data_integration.adapters.bet365_adapter import Bet365Adapter
from data_integration.adapters.sportsbook_adapter import SportsBookAdapter
from data_integration.adapters.whoscored_adapter import WhoScoredAdapter

class DataIntegrationHub:
    def __init__(self):
        self.adapters = {}
        self.init_adapters()
        logging.info(f"[Hub] Adaptateurs chargés : {list(self.adapters.keys())}")

    def init_adapters(self):
        try:
            self.adapters['openapi'] = OpenAPIAdapter()
        except Exception as e:
            logging.warning(f"[Hub] Échec OpenAPIAdapter : {e}")

        try:
            self.adapters['soccerdata'] = SoccerDataAdapter()
        except Exception as e:
            logging.warning(f"[Hub] Échec SoccerDataAdapter : {e}")

        try:
            self.adapters['sportsbetting'] = SportsBettingAdapter()
        except Exception as e:
            logging.warning(f"[Hub] Échec SportsBettingAdapter : {e}")

        try:
            self.adapters['bet365'] = Bet365Adapter()
        except Exception as e:
            logging.warning(f"[Hub] Échec Bet365Adapter : {e}")

        try:
            self.adapters['sportsbook'] = SportsBookAdapter()
        except Exception as e:
            logging.warning(f"[Hub] Échec SportsBookAdapter : {e}")

        try:
            self.adapters['whoscored'] = WhoScoredAdapter()
        except Exception as e:
            logging.warning(f"[Hub] Échec WhoScoredAdapter : {e}")

    def get_available_adapters(self):
        return {
            name: adapter.is_available()
            for name, adapter in self.adapters.items()
        }

    def fetch_data(self, source, *args, **kwargs):
        adapter = self.adapters.get(source)
        if adapter and adapter.is_available():
            try:
                return adapter.fetch_data(*args, **kwargs)
            except Exception as e:
                logging.error(f"[Hub] Erreur lors de fetch_data depuis {source} : {e}")
        else:
            logging.warning(f"[Hub] Source {source} indisponible ou invalide.")
        return None
