from .base_trigger import BaseTrigger
from utils.logger import StructuredLogger

class BetflowTrigger(BaseTrigger):
    def __init__(self, ratio_threshold=6000):
        self.ratio_threshold = ratio_threshold
        self.logger = StructuredLogger(__name__)

    def evaluate(self, match_data: dict) -> dict:
        odds = match_data.get("odds", [])
        volumes = match_data.get("volumes", [])

        if not odds or not volumes or len(odds) != len(volumes):
            self.logger.warning(
                "BetflowTrigger : données de cotes/volumes insuffisantes ou incohérentes",
                odds=odds,
                volumes=volumes
            )
            return {"triggered": False, "reason": "Données de cotes/volumes insuffisantes ou incohérentes"}

        ratios = []
        for o, v in zip(odds, volumes):
            if o > 0:
                ratios.append(v / o)
            else:
                ratios.append(0)
        max_ratio = max(ratios)
        self.logger.debug(
            "BetflowTrigger : calcul des ratios",
            ratios=ratios,
            max_ratio=max_ratio,
            threshold=self.ratio_threshold
        )
        if max_ratio > self.ratio_threshold:
            idx = ratios.index(max_ratio)
            self.logger.info(
                "BetflowTrigger déclenché",
                max_ratio=max_ratio,
                volume=volumes[idx],
                cote=odds[idx]
            )
            return {
                "triggered": True,
                "reason": f"Ratio volume/cote anormal détecté : {max_ratio:.2f} (volume {volumes[idx]} / cote {odds[idx]})"
            }
        self.logger.debug(
            "BetflowTrigger non déclenché",
            max_ratio=max_ratio,
            threshold=self.ratio_threshold
        )
        return {"triggered": False, "reason": "Aucune anomalie betflow détectée"}
