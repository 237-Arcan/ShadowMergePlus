class WeightAdapter:
    """
    Ajuste dynamiquement les poids des modules selon les feedbacks.
    """
    def __init__(self, weights: dict):
        self.weights = weights

    def adjust_weights(self, feedback: dict):
        """
        Ajuste les poids selon les résultats.

        Args:
            feedback (dict): {module: {'success': bool}}
        """
        for module, result in feedback.items():
            if result.get('success'):
                self.weights[module] = min(1.0, self.weights.get(module, 0) + 0.01)
            else:
                self.weights[module] = max(0.0, self.weights.get(module, 0) - 0.01)
