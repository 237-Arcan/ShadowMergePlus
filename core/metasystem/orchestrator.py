import logging
from .fusion_engine import FusionEngine
from .logbook import Logbook

class Orchestrator:
    """
    Orchestration du cycle de prédiction :
    Agrège les sorties des modules, les fusionne, journalise les résultats.
    """
    def __init__(self, modules: dict):
        self.modules = modules
        self.fusion_engine = FusionEngine()
        self.logbook = Logbook()

    def run_prediction_cycle(self, match_data: dict):
        """
        Lance un cycle de prédiction sur les modules fournis.

        Args:
            match_data (dict): Données d'entrée du match.

        Returns:
            float: Score final fusionné.
        """
        outputs = {}
        for name, module in self.modules.items():
            outputs[name] = module.predict(match_data)
            self.logbook.log_module_output(name, outputs[name])
        merged = self.fusion_engine.merge(outputs)
        self.logbook.log_merged_output(merged)
        return merged
