from orchestrator.batch_orchestrator import BatchDataOrchestrator

# Squelettes modulaires à compléter selon ta logique métier
from orchestrator.utils import extract_odds
from triggers.trigger_set import TriggerSet
from insights.context_insight_manager import ContextInsightManager
from fusion.shadow_merge_plus import ShadowMergePlus

def orchestrate_multi_match_analysis(match_ids):
    batch = BatchDataOrchestrator()
    aggregated_data = batch.collect_all_for_matches(match_ids)

    triggers = {}
    context_insights = {}

    for match_id, sources in aggregated_data.items():
        # Extraction des cotes multi-sources (bet365, sportsbook, etc.)
        odds_data = extract_odds(sources)
        triggers[match_id] = TriggerSet().detect_anomalies(odds_data)

        # Analyse contextuelle (forme, absences, etc.)
        context_insights[match_id] = ContextInsightManager().analyze(
            sources.get("whoscored"), sources.get("soccerdata")
        )

    # Fusion finale (score hybride, priorisation, etc.)
    results = {}
    for match_id in match_ids:
        results[match_id] = ShadowMergePlus().fuse(
            triggers=triggers[match_id],
            context_insights=context_insights[match_id],
            raw_data=aggregated_data[match_id]
        )

    return results

if __name__ == "__main__":
    # Exemple d’appel
    match_ids = ["match1", "match2", "match3"]
    output = orchestrate_multi_match_analysis(match_ids)
    print(output)
