class TrainingFeedback:
    """
    Historique des prédictions et feedback pour ajustement des modèles.
    """
    def __init__(self):
        self.history = []

    def record(self, prediction, actual):
        self.history.append({"prediction": prediction, "actual": actual})

    def evaluate(self) -> float:
        correct = sum(1 for entry in self.history if round(entry['prediction']) == entry['actual'])
        return correct / len(self.history) if self.history else 0.0
