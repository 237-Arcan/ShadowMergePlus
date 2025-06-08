class ChronoEcho:
    """
    Analyse des échos historiques.
    """

    def __init__(self, historical_memory):
        self.memory = historical_memory

    def analyze_echo(self, current_match):
        """
        Retourne un écho historique pertinent pour un match courant.
        """
        return self.memory.get(current_match, "Aucun écho pertinent trouvé")
