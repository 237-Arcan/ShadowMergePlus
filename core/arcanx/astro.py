class AstroEngine:
    """
    Analyse astrologique des influences planétaires.
    """

    def __init__(self):
        self.influences = {
            "mars": "agressivité",
            "venus": "harmonie",
            "mercure": "communication",
        }

    def evaluate(self, date_of_match):
        """
        Pseudo-analyse astrologique pour une date donnée.
        À remplacer par une vraie logique plus tard.
        """
        return {
            "dominant_planet": "mars",
            "effect": self.influences["mars"]
        }
