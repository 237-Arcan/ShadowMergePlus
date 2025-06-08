class TeamInsight:
    """
    Gestion des insights d’équipe.
    """

    def __init__(self, team_profiles):
        self.team_profiles = team_profiles

    def generate_insight(self, team_name):
        """
        Retourne l’insight associé à une équipe.
        """
        return self.team_profiles.get(team_name, "Insight inconnu")
