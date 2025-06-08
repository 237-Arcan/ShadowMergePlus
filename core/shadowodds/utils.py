import csv
import json
import yaml
from typing import List, Dict, Any


def load_csv(filepath: str) -> List[Dict[str, str]]:
    """Charge un fichier CSV en liste de dictionnaires."""
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def load_json(filepath: str) -> Any:
    """Charge un fichier JSON en objet Python."""
    with open(filepath, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)


def load_yaml(filepath: str) -> Any:
    """Charge un fichier YAML en objet Python."""
    with open(filepath, 'r', encoding='utf-8') as yamlfile:
        return yaml.safe_load(yamlfile)


def filter_by_odds_range(data: List[Dict[str, Any]], lower: float, upper: float) -> List[Dict[str, Any]]:
    """
    Filtre les entrées dont la cote ('odds') est dans [lower, upper].
    """
    filtered = []
    for entry in data:
        try:
            odds = float(entry.get('odds', 0))
            if lower <= odds <= upper:
                filtered.append(entry)
        except (ValueError, TypeError):
            continue
    return filtered


def print_summary_stats(data: List[Dict[str, Any]]) -> None:
    """
    Affiche un résumé statistique du nombre de 'win' dans les résultats.
    """
    total = len(data)
    win_count = sum(1 for x in data if x.get('result') == 'win')
    win_pct = (win_count / total * 100) if total else 0.0
    print(f"Total entries: {total}")
    print(f"Wins: {win_count} ({win_pct:.2f}%)")
