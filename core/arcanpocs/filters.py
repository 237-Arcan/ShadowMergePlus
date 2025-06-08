"""
POC Filters : Nettoyage des signaux faibles.
"""

def apply_filters(points: list, threshold: float = 0.5) -> list:
    """
    Filtre les points sous un certain seuil.

    Args:
        points (list): Liste de tuples (label, value).
        threshold (float): Seuil minimal d'acceptation.

    Returns:
        list: Points filtrés.
    """
    return [(label, val) for label, val in points if val >= threshold]
