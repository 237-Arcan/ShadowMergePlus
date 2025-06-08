"""
Module : arcan_sentinel_live
Description : Système d'analyse en temps réel des matchs pour détecter des dynamiques
              décisives, anomalies comportementales et signaux live cruciaux.
"""

from .sentinel_core import ArcanSentinelLive
from .live_parser import parse_live_data
from .scoring_model import calculate_live_scores
from .anomaly_detector import detect_anomalies

__all__ = [
    "ArcanSentinelLive",
    "parse_live_data",
    "calculate_live_scores",
    "detect_anomalies",
    "analyze_live_match"
]


def analyze_live_match(feed_raw: dict) -> dict:
    """
    Fonction d'analyse complète d'un match live à partir de données brutes.

    Args:
        feed_raw (dict): Données brutes du match (API, JSON live, etc.)

    Returns:
        dict: Résultat structuré de l'analyse temps réel
    """
    parsed_data = parse_live_data(feed_raw)
    score_prediction = calculate_live_scores(parsed_data)
    anomalies = detect_anomalies(parsed_data)

    return {
        "parsed": parsed_data,
        "score_prediction": score_prediction,
        "anomalies": anomalies
    }
