"""
Anomaly Detector : Détection d'événements anormaux en live.
"""

def detect_anomalies(data: dict) -> list:
    """
    Détecte des anomalies dans le déroulement live du match.

    Args:
        data (dict): Données normalisées du match.

    Returns:
        list: Liste d'anomalies détectées.
    """
    anomalies = []
    events = data.get('events', [])
    minute = data.get('minute', 0)

    if 'red_card' in events:
        anomalies.append('Red Card Detected')
    if 'goal' in events and minute < 5:
        anomalies.append('Early Goal')
    return anomalies
