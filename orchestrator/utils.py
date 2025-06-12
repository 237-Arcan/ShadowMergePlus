def extract_odds(sources: dict) -> dict:
    """
    Agrège et normalise les cotes issues des adaptateurs (bet365, sportsbook, etc.)
    :param sources: dict des données sources pour un match (clé = nom adaptateur)
    :return: dict normalisé des cotes par source
    """
    odds = {}
    for src, data in sources.items():
        if "odds" in data:
            odds[src] = data["odds"]
    return odds
