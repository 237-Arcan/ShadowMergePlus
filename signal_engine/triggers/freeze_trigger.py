from .base_trigger import BaseTrigger
from utils.logger import StructuredLogger

class FreezeTrigger(BaseTrigger):
    def __init__(self, volume_threshold=10000, freeze_window=3):
        self.volume_threshold = volume_threshold
        self.freeze_window = freeze_window
        self.logger = StructuredLogger(__name__)

    def evaluate(self, match_data: dict) -> dict:
        odds = match_data.get("odds", [])
        volumes = match_data.get("volumes", [])
        if len(odds) < self.freeze_window or len(volumes) < self.freeze_window:
            self.logger.debug("Pas assez d'historique pour FreezeTrigger", odds=odds, volumes=volumes)
            return {"triggered": False, "reason": "Pas assez d'historique pour le freeze"}

        recent_odds = odds[-self.freeze_window:]
        recent_volumes = volumes[-self.freeze_window:]
        is_frozen = all(o == recent_odds[0] for o in recent_odds)
        large_volume = max(recent_volumes) >= self.volume_threshold

        self.logger.debug("Vérification freeze", recent_odds=recent_odds, recent_volumes=recent_volumes, is_frozen=is_frozen, large_volume=large_volume)

        if is_frozen and large_volume:
            return {
                "triggered": True,
                "reason": f"Cote figée à {recent_odds[0]} malgré un volume max de {max(recent_volumes)} sur {self.freeze_window} ticks"
            }
        return {"triggered": False, "reason": "Pas de freeze détecté (cote variable ou faibles volumes)"}
