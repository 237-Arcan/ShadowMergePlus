TRIGGER_ODDS = [1.5, 1.6, 1.7, 1.75, 1.92, 4.75]
TRIGGER_RANGE = (1.5, 1.7)

class TriggerSet:
    """
    Déclencheurs basés sur les cotes gagnantes.
    """

    def __init__(self):
        self.static_odds = TRIGGER_ODDS
        self.range = TRIGGER_RANGE

    def identify_triggers(self, odds_data):
        """
        Identifie les triggers selon les cotes définies et la plage.
        """
        triggers = []
        for entry in odds_data:
            odd = entry.get('odds')
            if odd in self.static_odds or (self.range[0] <= odd <= self.range[1]):
                triggers.append({
                    "match": entry.get('match'),
                    "triggered": True,
                    "odds": odd
                })
        return triggers
