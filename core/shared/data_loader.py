import pandas as pd
import json

class DataLoader:
    """
    Gestionnaire d'accès aux données (CSV, JSON, ...).
    """
    def __init__(self, source_path: str):
        self.source_path = source_path

    def load_csv(self):
        return pd.read_csv(self.source_path)

    def load_json(self):
        with open(self.source_path, 'r') as f:
            return json.load(f)
