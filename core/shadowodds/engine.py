class ShadowOddsEngine:
    """
    Moteur principal d'analyse des cotes.
    Orchestration de l'analyse comportementale, des triggers et de la validation.
    """

    def __init__(self, behavior_analyzer, trigger_set, validator):
        self.behavior_analyzer = behavior_analyzer
        self.trigger_set = trigger_set
        self.validator = validator

    def analyze(self, odds_data, market_data):
        """
        Exécute l’analyse complète : comportement, triggers, validation.
        """
        behavior_signals = self.behavior_analyzer.analyze_behavior(odds_data, market_data)
        triggers = self.trigger_set.identify_triggers(odds_data)
        validated = self.validator.validate(behavior_signals, triggers)
        return validated
