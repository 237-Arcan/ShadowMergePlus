from signal_engine.triggers.volatility_trigger import VolatilityTrigger
from signal_engine.triggers.freeze_trigger import FreezeTrigger
from signal_engine.triggers.betflow_trigger import BetflowTrigger
from signal_engine.triggers.base_trigger import BaseTrigger

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

def test_volatility_trigger_logging(monkeypatch):
    mock_logger = MockLogger()
    monkeypatch.setattr("signal_engine.triggers.volatility_trigger.StructuredLogger", lambda *a, **k: mock_logger)
    trigger = VolatilityTrigger(threshold=0.1)
    data = {"odds": [1.5, 1.8]}
    result = trigger.evaluate(data)
    assert any("VolatilityTrigger" in log[1] or "volatilité" in log[1].lower() for log in mock_logger.logs)
    assert isinstance(result, dict)

def test_freeze_trigger_logging(monkeypatch):
    mock_logger = MockLogger()
    monkeypatch.setattr("signal_engine.triggers.freeze_trigger.StructuredLogger", lambda *a, **k: mock_logger)
    trigger = FreezeTrigger(volume_threshold=9000, freeze_window=2)
    data = {"odds": [1.7, 1.7], "volumes": [9500, 11000]}
    result = trigger.evaluate(data)
    assert any("FreezeTrigger" in log[1] or "freeze" in log[1].lower() for log in mock_logger.logs)
    assert isinstance(result, dict)

def test_betflow_trigger_logging(monkeypatch):
    mock_logger = MockLogger()
    monkeypatch.setattr("signal_engine.triggers.betflow_trigger.StructuredLogger", lambda *a, **k: mock_logger)
    trigger = BetflowTrigger(ratio_threshold=8000)
    data = {"odds": [2.0, 2.0, 1.95], "volumes": [1000, 20000, 8000]}
    result = trigger.evaluate(data)
    assert any("BetflowTrigger" in log[1] or "betflow" in log[1].lower() for log in mock_logger.logs)
    assert isinstance(result, dict)

def test_base_trigger_logging(monkeypatch):
    mock_logger = MockLogger()
    monkeypatch.setattr("signal_engine.triggers.base_trigger.StructuredLogger", lambda *a, **k: mock_logger)
    trigger = BaseTrigger()
    caught = False
    try:
        trigger.evaluate({"foo": "bar"})
    except NotImplementedError:
        caught = True
    assert caught
    assert any("BaseTrigger" in log[1] or "non prévu" in log[1].lower() for log in mock_logger.logs)
