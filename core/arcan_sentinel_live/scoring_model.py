"""
Scoring Model : Prédiction basée sur la dynamique live.
"""

def calculate_live_scores(data: dict) -> dict:
    """
    Calcule des scores et une confiance à partir des événements live.

    Args:
        data (dict): Données normalisées du match.

    Returns:
        dict: Prédictions sur le score final, momentum, confiance.
    """
    score = data.get('score')
    events = data.get('events', [])
    minute = data.get('minute', 0)

    momentum = sum(1 for event in events if event in ['attack', 'corner'])
    confidence = min(1.0, 0.1 + 0.02 * momentum)

    return {
        'expected_final_score': score,
        'momentum': momentum,
        'confidence': confidence
    }
