"""
Live Parser : Normalisation des données live.
"""

def parse_live_data(feed: dict) -> dict:
    """
    Convertit le flux live brut en format structuré exploitable.

    Args:
        feed (dict): Données live brutes.

    Returns:
        dict: Données normalisées.
    """
    return {
        'minute': feed.get('minute'),
        'home_team': feed.get('home'),
        'away_team': feed.get('away'),
        'score': feed.get('score'),
        'events': feed.get('events', [])
    }
