import pytest
from orchestrator.intelligent_orchestration import orchestrate_multi_match_analysis

# Dummies pour patcher les dépendances de l'orchestrateur intelligent
class DummyBatchOrchestrator:
    def collect_all_for_matches(self, match_ids):
        # Retourne des données simulées multi-sources
        return {
            mid: {
                "bet365": {"odds": [1.5, 2.1]},
                "whoscored": {"ratings": {"player1": 7.1}},
                "soccerdata": {"stats": {}}
            }
            for mid in match_ids
        }

class DummyTriggerSet:
    def detect_anomalies(self, odds_data): return {"trigger": "ok"}

class DummyContextInsightManager:
    def analyze(self, whoscored, soccerdata): return {"insight": "context"}

class DummyShadowMergePlus:
    def fuse(self, triggers, context_insights, raw_data): return {"score": 99, "details": {"triggers": triggers}}

def dummy_extract_odds(sources): return sources["bet365"]["odds"]

@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    import orchestrator.intelligent_orchestration as io
    monkeypatch.setattr(io, "BatchDataOrchestrator", DummyBatchOrchestrator)
    monkeypatch.setattr(io, "TriggerSet", DummyTriggerSet)
    monkeypatch.setattr(io, "ContextInsightManager", DummyContextInsightManager)
    monkeypatch.setattr(io, "ShadowMergePlus", DummyShadowMergePlus)
    monkeypatch.setattr(io, "extract_odds", dummy_extract_odds)

def test_orchestrate_multi_match_analysis():
    match_ids = ["matchA", "matchB"]
    results = orchestrate_multi_match_analysis(match_ids)
    assert isinstance(results, dict)
    for mid in match_ids:
        assert "score" in results[mid]
        assert isinstance(results[mid]["score"], int)
