"""
POCMatrix : Centralise les points d'observation critiques issus des modules.
"""

class POCMatrix:
    def __init__(self):
        self.points = []

    def add_point(self, label: str, value: float):
        """
        Ajoute un point à la matrice POC.

        Args:
            label (str): Nom ou identifiant du signal.
            value (float): Valeur/poids du signal.
        """
        self.points.append((label, value))

    def summarize(self) -> dict:
        """
        Résume la matrice des points.

        Returns:
            dict: Compte et liste des points.
        """
        return {
            'count': len(self.points),
            'data': self.points
        }
