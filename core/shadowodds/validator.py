class OddsValidator:
    """
    Validation par historique et logique des signaux.
    """

    def __init__(self):
        pass

    def validate(self, behavior_signals, triggers):
        """
        Valide les triggers selon la présence de signaux comportementaux.
        """
        results = []
        for trigger in triggers:
            match = trigger.get('match')
            valid = False
            reason = None
            for signal in behavior_signals:
                if signal.get('match') == match:
                    valid = True
                    reason = signal.get('signal')
                    break
            results.append({
                "match": match,
                "valid": valid,
                "reason": reason
            })
        return results
