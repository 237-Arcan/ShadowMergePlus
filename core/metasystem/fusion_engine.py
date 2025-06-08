class FusionEngine:
    """
    Moteur de fusion des prédictions issues des modules du système.
    """
    def __init__(self):
        self.weights = {
            "shadowodds": 0.3,
            "arcanx": 0.25,
            "arcan_sentinel_live": 0.25,
            "arcanpocs": 0.2
        }

    def merge(self, predictions: dict) -> float:
        """
        Fusionne les scores/prédictions selon les poids attribués.

        Args:
            predictions (dict): {module_name: score}

        Returns:
            float: Score global pondéré.
        """
        final_score = 0.0
        for module, score in predictions.items():
            weight = self.weights.get(module, 0)
            final_score += score * weight
        return final_score
