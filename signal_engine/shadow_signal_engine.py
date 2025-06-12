from .triggers.volatility_trigger import VolatilityTrigger

class ShadowSignalEngine:
    def __init__(self):
        self.triggers = [
            VolatilityTrigger(threshold=0.15),
            # Ajouter d’autres triggers ici (FreezeTrigger, etc.)
        ]

    def analyze(self, match_data: dict) -> dict:
        signals = []
        for trigger in self.triggers:
            result = trigger.evaluate(match_data)
            signals.append({
                "trigger": trigger.__class__.__name__,
                "status": result["triggered"],
                "reason": result["reason"]
            })
        confidence_score = sum(sig["status"] for sig in signals) / len(signals) if signals else 0
        return {
            "match_id": match_data.get("match_id"),
            "confidence_score": confidence_score,
            "signals": signals
        }
