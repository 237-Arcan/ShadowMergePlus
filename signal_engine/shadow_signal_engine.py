from .triggers.volatility_trigger import VolatilityTrigger
from .triggers.freeze_trigger import FreezeTrigger
from .triggers.betflow_trigger import BetflowTrigger
from .triggers.base_trigger import BaseTrigger
from utils.logger import StructuredLogger
from utils.signal_output import make_signal_output

class ShadowSignalEngine:
    """
    Orchestrates behavioral analysis by applying a set of triggers to match data.
    Produces a confidence score and detailed signal justifications.
    """

    def __init__(self):
        self.logger = StructuredLogger(__name__)
        self.triggers = [
            VolatilityTrigger(threshold=0.15),
            FreezeTrigger(volume_threshold=10000, freeze_window=3),
            BetflowTrigger(ratio_threshold=6000),
            # BaseTrigger can be used as a placeholder, but is not meant to be used directly.
        ]

    def analyze(self, match_data: dict) -> dict:
        self.logger.info("Analyse d'un match", match_id=match_data.get("match_id"))
        signals = []
        for trigger in self.triggers:
            result = trigger.evaluate(match_data)
            self.logger.debug(
                "Résultat du trigger",
                trigger=trigger.__class__.__name__,
                status=result["triggered"],
                reason=result["reason"],
            )
            signals.append({
                "trigger": trigger.__class__.__name__,
                "status": result["triggered"],
                "reason": result["reason"]
            })
        confidence_score = (
            sum(sig["status"] for sig in signals) / len(signals) if signals else 0.0
        )
        self.logger.info(
            "Fin d'analyse",
            match_id=match_data.get("match_id"),
            confidence_score=confidence_score,
        )
        # Utilisation centralisée du helper pour garantir la conformité du signal_output
        return make_signal_output(match_data.get("match_id"), confidence_score, signals)
