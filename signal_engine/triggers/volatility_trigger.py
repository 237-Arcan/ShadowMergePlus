from .base_trigger import BaseTrigger

class VolatilityTrigger(BaseTrigger):
    def __init__(self, threshold=0.15):
        self.threshold = threshold

    def evaluate(self, match_data: dict) -> dict:
        odds = match_data.get("odds", [])
        if len(odds) < 2:
            return {"triggered": False, "reason": "Pas assez d'historique de cotes"}
        diff = abs(odds[-1] - odds[0])
        if diff > self.threshold:
            return {"triggered": True, "reason": f"Volatilité détectée : écart de cote de {diff:.2f}"}
        return {"triggered": False, "reason": "Variation de cote normale"}
