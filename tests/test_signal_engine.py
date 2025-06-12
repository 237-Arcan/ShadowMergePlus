from signal_engine.shadow_signal_engine import ShadowSignalEngine

def test_shadow_signal_engine_all_triggers():
    engine = ShadowSignalEngine()

    # Cas 1 : Volatilité (odds fluctuants), freeze sur volume, betflow anormal
    match_data = {
        "match_id": "TEST1",
        "odds": [1.80, 1.95, 2.10],
        "volumes": [8000, 12000, 13000]
    }
    result = engine.analyze(match_data)
    assert result["match_id"] == "TEST1"
    assert isinstance(result["confidence_score"], float)
    assert len(result["signals"]) == 3  # 3 triggers attendus

    # Vérifie que chaque trigger renvoie bien un booléen et une raison
    for signal in result["signals"]:
        assert "trigger" in signal
        assert "status" in signal
        assert isinstance(signal["status"], bool)
        assert "reason" in signal

    # Cas 2 : Aucun trigger ne se déclenche (tout faible)
    match_data2 = {
        "match_id": "TEST2",
        "odds": [1.50, 1.51, 1.52],
        "volumes": [100, 120, 90]
    }
    result2 = engine.analyze(match_data2)
    assert result2["confidence_score"] == 0.0
    assert all(signal["status"] is False for signal in result2["signals"])

    # Cas 3 : FreezeTrigger déclenché (cote figée, gros volume)
    match_data3 = {
        "match_id": "TEST3",
        "odds": [1.77, 1.77, 1.77],
        "volumes": [8000, 12000, 16000]
    }
    result3 = engine.analyze(match_data3)
    freeze_signal = next(s for s in result3["signals"] if s["trigger"] == "FreezeTrigger")
    assert freeze_signal["status"] is True

    # Cas 4 : BetflowTrigger déclenché (volume/cote anormal)
    match_data4 = {
        "match_id": "TEST4",
        "odds": [2.0, 2.0, 1.95],
        "volumes": [1000, 20000, 8000]
    }
    result4 = engine.analyze(match_data4)
    betflow_signal = next(s for s in result4["signals"] if s["trigger"] == "BetflowTrigger")
    assert betflow_signal["status"] is True
