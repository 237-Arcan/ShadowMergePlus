from orchestrator.data_orchestrator import DataOrchestrator

class BatchDataOrchestrator:
    def __init__(self):
        self.single_orchestrator = DataOrchestrator()

    def collect_all_for_matches(self, match_ids: list[str]) -> dict:
        """
        Collecte les données pour une liste de matchs via DataOrchestrator.

        :param match_ids: liste d'identifiants de matchs
        :return: dict structuré par match_id → source → données
        """
        aggregated_data = {}

        for match_id in match_ids:
            try:
                aggregated_data[match_id] = self.single_orchestrator.collect_match_data(match_id)
            except Exception as e:
                aggregated_data[match_id] = {"error": str(e)}

        return aggregated_data
