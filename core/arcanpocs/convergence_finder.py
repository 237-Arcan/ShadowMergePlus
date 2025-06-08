"""
Convergence Finder : Recherche des points de convergence forts.
"""

def find_convergences(points: list) -> dict:
    """
    Cherche les valeurs hautes récurrentes dans la matrice.

    Args:
        points (list): Liste de tuples (label, value).

    Returns:
        dict: Indique s'il y a convergence et détaille les valeurs élevées.
    """
    values = [v for _, v in points]
    high_values = [v for v in values if v > 0.75]
    return {
        'converged': len(high_values) > 2,
        'high_values': high_values
    }
