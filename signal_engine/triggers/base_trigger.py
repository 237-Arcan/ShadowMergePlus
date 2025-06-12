class BaseTrigger:
    def evaluate(self, match_data: dict) -> dict:
        """
        Retourne un dict {'triggered': bool, 'reason': str}
        """
        raise NotImplementedError("Chaque trigger doit implémenter la méthode evaluate.")
