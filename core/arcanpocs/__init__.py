"""
ArcanPOCS - Points of Convergence System
----------------------------------------
Ce module initialise le système ArcanPOCS, responsable de l'identification
des points de convergence entre signaux statistiques, ésotériques et comportementaux.
Il constitue une des briques stratégiques du moteur prédictif ShadowMerge+.

Contenu exposé :
- load_poc_matrix()
- find_convergences()
- apply_filters()
- generate_scenarios()
"""

from .poc_matrix import load_poc_matrix
from .convergence_finder import find_convergences
from .filters import apply_filters
from .scenarios import generate_scenarios

__all__ = [
    "load_poc_matrix",
    "find_convergences",
    "apply_filters",
    "generate_scenarios"
]
