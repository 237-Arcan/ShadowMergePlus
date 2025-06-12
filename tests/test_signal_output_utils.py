from utils.signal_output import make_signal_output

def test_make_signal_output_basic():
    match_id = "XYZ123"
    confidence_score = 0.87654
    signals = [
        {"trigger": "FreezeTrigger", "status": True, "reason": "Blocage détecté"},
        {"trigger": "VolatilityTrigger", "status": False, "reason": "Pas de volatilité"}
    ]
    output = make_signal_output(match_id, confidence_score, signals)
    assert output["match_id"] == "XYZ123"
    assert isinstance(output["confidence_score"], float)
    assert round(output["confidence_score"], 2) == 0.88
    assert isinstance(output["signals"], list)
    assert output["signals"][0]["trigger"] == "FreezeTrigger"
    assert output["signals"][0]["status"] is True
    assert isinstance(output["signals"][0]["reason"], str)
    assert output["signals"][1]["status"] is False

def test_make_signal_output_formatting_and_defaults():
    # Vérifie robustesse si certains champs sont manquants ou de mauvais type
    signals = [
        {"trigger": "BetflowTrigger"},  # missing status & reason
        {"trigger": None, "status": "yes", "reason": 42}
    ]
    out = make_signal_output("MID", 1, signals)
    assert out["signals"][0]["status"] is False
    assert isinstance(out["signals"][0]["reason"], str)
    assert out["signals"][1]["trigger"] is None
    assert out["signals"][1]["status"] is True  # bool("yes") == True
    assert isinstance(out["signals"][1]["reason"], str)
