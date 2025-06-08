class NumerologyEngine:
    """
    Analyse numérologique.
    """

    def __init__(self):
        pass

    def compute_vibration(self, match_date):
        """
        Calcule la vibration numérologique du jour.
        """
        return (int(match_date.strftime("%Y%m%d")) % 9) + 1
