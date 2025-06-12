import os
import json
from utils.logger import StructuredLogger
from .shadow_signal_engine import ShadowSignalEngine

class SignalOrchestrator:
    def __init__(self, input_dir="outputs/match_data/", output_dir="outputs/signals/"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.engine = ShadowSignalEngine()
        self.logger = StructuredLogger(__name__)

    def run(self):
        self.logger.info("Début de l'orchestration des signaux")
        for fname in os.listdir(self.input_dir):
            if fname.endswith(".json"):
                in_path = os.path.join(self.input_dir, fname)
                try:
                    with open(in_path, "r") as fin:
                        match_data = json.load(fin)
                    self.logger.info("Analyse d'un match", match_id=match_data.get("match_id"), file=fname)
                    result = self.engine.analyze(match_data)
                    out_path = os.path.join(self.output_dir, f"signal_{match_data['match_id']}.json")
                    with open(out_path, "w") as fout:
                        json.dump(result, fout, indent=2)
                    self.logger.info("Signal généré", match_id=match_data.get("match_id"), output=out_path)
                except Exception as e:
                    self.logger.error(
                        "Erreur lors du traitement du match",
                        file=fname,
                        error=str(e)
                    )
        self.logger.info("Fin de l'orchestration des signaux")
