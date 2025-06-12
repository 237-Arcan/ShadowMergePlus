from signal_engine.triggers.volatility_trigger import VolatilityTrigger

def test_volatility_trigger():
    trigger = VolatilityTrigger(threshold=0.10)
    # Cas déclenché
    data = {"odds": [1.50, 1.80]}
    result = trigger.evaluate(data)
    assert result["triggered"] is True
    # Cas non déclenché
    data = {"odds": [1.50, 1.55]}
    result = trigger.evaluate(data)
    assert result["triggered"] is False
