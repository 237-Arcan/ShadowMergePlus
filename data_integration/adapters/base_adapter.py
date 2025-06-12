from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    @abstractmethod
    def fetch_data(self, match_id: str) -> dict:
        """
        Récupère les données brutes de la source.
        """
        pass
