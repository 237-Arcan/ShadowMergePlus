from utils.logger import StructuredLogger

class BaseTrigger:
    def __init__(self):
        self.logger = StructuredLogger(__name__)

    def evaluate(self, match_data: dict) -> dict:
        self.logger.warning(
            "BaseTrigger appelé directement, ce qui est non prévu.",
            match_data=match_data
        )
        raise NotImplementedError("Chaque trigger doit implémenter la méthode evaluate.")
