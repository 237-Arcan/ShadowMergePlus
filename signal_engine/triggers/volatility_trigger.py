from .base_trigger import BaseTrigger
from utils.logger import StructuredLogger

class VolatilityTrigger(BaseTrigger):
    def __init__(self, threshold=0.15):
        self.threshold = threshold
        self.logger = StructuredLogger(__name__)

    def evaluate(self, match_data: dict) -> dict:
        odds = match_data.get("odds", [])
        if len(odds) < 2:
            self.logger.debug(
                "VolatilityTrigger : pas assez d'historique de cotes",
                odds=odds
            )
            return {"triggered": False, "reason": "Pas assez d'historique de cotes"}
        diff = abs(odds[-1] - odds[0])
        self.logger.debug(
            "VolatilityTrigger : calcul de volatilité",
            odds=odds,
            diff=diff,
            threshold=self.threshold
        )
        if diff > self.threshold:
            self.logger.info(
                "VolatilityTrigger déclenché",
                diff=diff,
                threshold=self.threshold
            )
            return {"triggered": True, "reason": f"Volatilité détectée : écart de cote de {diff:.2f}"}
        self.logger.debug(
            "VolatilityTrigger non déclenché",
            diff=diff,
            threshold=self.threshold
        )
        return {"triggered": False, "reason": "Variation de cote normale"}
