class KhawatimEngine:
    """
    Analyse des signes de fin de cycle.
    """

    def __init__(self):
        pass

    def detect_final_signals(self, team_trends):
        """
        Détecte la fin d’un cycle sur la base des tendances.
        """
        if len(team_trends) >= 2 and team_trends[-1] < team_trends[-2]:
            return "Fin de cycle suspectée"
        return "Cycle stable"
