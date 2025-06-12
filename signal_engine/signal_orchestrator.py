import os
import json
from .shadow_signal_engine import ShadowSignalEngine

class SignalOrchestrator:
    def __init__(self, input_dir="outputs/match_data/", output_dir="outputs/signals/"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.engine = ShadowSignalEngine()

    def run(self):
        for fname in os.listdir(self.input_dir):
            if fname.endswith(".json"):
                with open(os.path.join(self.input_dir, fname), "r") as fin:
                    match_data = json.load(fin)
                result = self.engine.analyze(match_data)
                out_path = os.path.join(self.output_dir, f"signal_{match_data['match_id']}.json")
                with open(out_path, "w") as fout:
                    json.dump(result, fout, indent=2)
