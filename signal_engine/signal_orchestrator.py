import os
import json
from utils.logger import StructuredLogger
from utils.signal_output import make_signal_output
from .shadow_signal_engine import ShadowSignalEngine

class SignalOrchestrator:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.engine = ShadowSignalEngine()
        self.logger = StructuredLogger(__name__)

    def run(self):
        self.logger.info("Démarrage de l'orchestration")
        for file in os.listdir(self.input_dir):
            if file.endswith(".json"):
                path = os.path.join(self.input_dir, file)
                with open(path, "r") as f:
                    match_data = json.load(f)
                signal = self.engine.analyze(match_data)
                # Centralisation de la structure de sortie
                output = make_signal_output(
                    match_data.get("match_id"),
                    signal.get("confidence_score"),
                    signal.get("signals")
                )
                output_path = os.path.join(self.output_dir, f"signal_{match_data['match_id']}.json")
                with open(output_path, "w") as out:
                    json.dump(output, out, indent=2)
                self.logger.info("Signal produit", match_id=match_data["match_id"], output=output_path)
        self.logger.info("Orchestration terminée")
