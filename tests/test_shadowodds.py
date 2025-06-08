from core.shadowodds.engine import ShadowOddsEngine

class DummyAnalyzer:
    def analyze_behavior(self, odds, market): return {}

class DummyTriggerSet:
    def identify_triggers(self, odds): return []

class DummyValidator:
    def validate(self, signals, triggers): return True

def test_shadow_odds_engine_instantiation():
    engine = ShadowOddsEngine(DummyAnalyzer(), DummyTriggerSet(), DummyValidator())
    assert isinstance(engine, ShadowOddsEngine)
