# fusion_engine.py

import logging

logger = logging.getLogger(__name__)


class FusionEngine:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def fuse_match_insight(self, match_id):
        """
        Fusionne les données de match + cotes + signaux dans une structure homogène.
        """
        try:
            match_data = self.orchestrator.get_match_data(match_id)
            odds_data = self.orchestrator.get_odds_for_match(match_id)
            # Placeholder pour signaux live à venir
            signals = []

            fused_result = {
                "match_id": match_id,
                "teams": self._extract_teams(match_data),
                "match_info": match_data,
                "odds": odds_data,
                "signals": signals,
                "confidence_score": self._calculate_confidence(match_data, odds_data),
            }

            return fused_result

        except Exception as e:
            logger.error(f"[FusionEngine] Erreur pendant la fusion pour le match {match_id}: {e}")
            return None

    def _extract_teams(self, match_data):
        teams = []
        for adapter_name, data in match_data.items():
            if isinstance(data, dict):
                home = data.get("home_team") or data.get("team1")
                away = data.get("away_team") or data.get("team2")
                if home and away:
                    teams.append((home, away))
        return teams[0] if teams else ("Unknown", "Unknown")

    def _calculate_confidence(self, match_data, odds_data):
        """
        Donne un score naïf basé sur le nombre de sources et la consistance des cotes.
        """
        if not match_data or not odds_data:
            return 0.0

        num_sources = len(match_data) + len(odds_data)
        odds_values = [o["odd"] for source in odds_data.values() if isinstance(o := source, dict) and "odd" in o]

        if not odds_values:
            return 0.2

        avg_odd = sum(odds_values) / len(odds_values)
        variance = sum((x - avg_odd) ** 2 for x in odds_values) / len(odds_values)
        normalized_variance = min(1.0, variance / 4.0)

        return round(min(1.0, 0.5 + (num_sources / 10.0) - normalized_variance), 3)
