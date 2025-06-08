"""
Sentinel Core : Coordination du système live.
"""

from .live_parser import parse_live_data
from .scoring_model import calculate_live_scores
from .anomaly_detector import detect_anomalies


class ArcanSentinelLive:
    """
    Coordonne l'analyse live d'un match en intégrant parsing, scoring et détection d'anomalies.
    """

    def __init__(self):
        self.events = []
        self.predictions = []

    def monitor_game(self, raw_feed: dict) -> dict:
        """
        Analyse un flux brut de match et stocke les résultats.

        Args:
            raw_feed (dict): Données brutes du match.

        Returns:
            dict: Dernière prédiction calculée.
        """
        live_data = parse_live_data(raw_feed)
        score_prediction = calculate_live_scores(live_data)
        anomalies = detect_anomalies(live_data)

        self.events.append(live_data)
        self.predictions.append({
            'score_prediction': score_prediction,
            'anomalies': anomalies
        })
        return self.predictions[-1]
