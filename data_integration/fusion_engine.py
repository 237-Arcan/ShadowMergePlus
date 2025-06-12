from typing import List, Dict
from .orchestrator import DataOrchestrator

class FusionEngine:
    def __init__(self):
        self.orchestrator = DataOrchestrator()

    def fuse_all(self, match_id: str, sources: List[str]) -> dict:
        all_data = self.orchestrator.fuse_multiple(sources, match_id)
        # Exemple de logique de fusion : priorité à la première source, fusion naïve
        fused = {}
        for source, data in all_data.items():
            if isinstance(data, dict):
                fused.update(data)
        return fused
