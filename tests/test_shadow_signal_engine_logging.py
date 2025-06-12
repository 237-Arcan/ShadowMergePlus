import json
from signal_engine.shadow_signal_engine import ShadowSignalEngine

class MockLogger:
    def __init__(self, *args, **kwargs):
        self.logs = []

    def info(self, message, **fields):
        self.logs.append(('INFO', message, fields))

    def warning(self, message, **fields):
        self.logs.append(('WARNING', message, fields))

    def error(self, message, **fields):
        self.logs.append(('ERROR', message, fields))

    def debug(self, message, **fields):
        self.logs.append(('DEBUG', message, fields))

def test_shadow_signal_engine_logging(monkeypatch):
    # Patch all trigger loggers AND the engine logger
    import signal_engine.triggers.volatility_trigger as volatility_trigger_mod
    import signal_engine.triggers.freeze_trigger as freeze_trigger_mod
    import signal_engine.triggers.betflow_trigger as betflow_trigger_mod
    import signal_engine.triggers.base_trigger as base_trigger_mod
    import signal_engine.shadow_signal_engine as shadow_signal_engine_mod

    mock_logger = MockLogger()

    monkeypatch.setattr(volatility_trigger_mod, "StructuredLogger", lambda *a, **k: mock_logger)
    monkeypatch.setattr(freeze_trigger_mod, "StructuredLogger", lambda *a, **k: mock_logger)
    monkeypatch.setattr(betflow_trigger_mod, "StructuredLogger", lambda *a, **k: mock_logger)
    monkeypatch.setattr(base_trigger_mod, "StructuredLogger", lambda *a, **k: mock_logger)
    monkeypatch.setattr(shadow_signal_engine_mod, "StructuredLogger", lambda *a, **k: mock_logger)

    engine = ShadowSignalEngine()
    match_data = {
        "match_id": "LOGTEST01",
        "odds": [1.5, 1.8, 2.0],
        "volumes": [5000, 12000, 8000]
    }
    result = engine.analyze(match_data)

    # Vérifier que des logs structurés ont bien été produits à chaque étape clé
    assert any(l[0] == "INFO" and "Analyse d'un match" in l[1] for l in mock_logger.logs)
    assert any(l[0] == "INFO" and "Fin d'analyse" in l[1] for l in mock_logger.logs)
    # Vérifie qu'au moins un log d'un trigger est présent
    assert any("trigger" in l[2] or "status" in l[2] or "reason" in l[2] for l in mock_logger.logs if l[0] == "DEBUG" or l[0] == "INFO")
    # Vérifier que le résultat final contient les bons champs
    assert "match_id" in result and "confidence_score" in result and "signals" in result
