class ShadowMergePlus:
    def fuse(self, triggers, context_insights, raw_data) -> dict:
        """
        Fusionne tous les signaux pour générer un score de confiance ou priorisation.
        :return: dict (score, tags, etc.)
        """
        result = {
            "score": 0.0,
            "tags": [],
            "details": {
                "triggers": triggers,
                "context": context_insights
            }
        }
        # ... logique de fusion à compléter
        return result
