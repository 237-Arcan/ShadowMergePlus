"""
Scenarios : Génération de scénarios à partir des points POC.
"""

def generate_scenarios(points: list) -> list:
    """
    Produit des scénarios à partir des points d'observation.

    Args:
        points (list): Points retenus après filtrage/convergence.

    Returns:
        list: Scénarios textuels ou recommandations.
    """
    if not points:
        return ['No viable scenario']
    return [
        f"Scenario {i+1}: {label} with confidence {val}"
        for i, (label, val) in enumerate(points)
    ]
