class MarketBehaviorAnalyzer:
    """
    Analyse comportementale des marchés pour les cotes.
    """

    def __init__(self):
        pass

    def analyze_behavior(self, odds_data, market_data):
        """
        Détecte les mouvements suspects sur la base du volume et des variations de cotes.
        """
        signals = []
        for entry in odds_data:
            volume = entry.get('volume', 0)
            odds_change = entry.get('odds_change', 0)
            if volume > 10000 and odds_change >= 0:
                signals.append({
                    "match": entry.get('match'),
                    "signal": "suspicious movement"
                })
        return signals
