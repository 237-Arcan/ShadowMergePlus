from core.shared.helpers import TriggerSet  # Modifie l'import selon l'emplacement réel de TriggerSet

def test_trigger_set_identify_triggers():
    trigger_set = TriggerSet()
    odds_data = [
        {"match": "A vs B", "odds": 1.5},
        {"match": "C vs D", "odds": 1.8},
        {"match": "E vs F", "odds": 1.75},
        {"match": "G vs H", "odds": 2.0},
        {"match": "I vs J", "odds": 4.75},
    ]
    triggers = trigger_set.identify_triggers(odds_data)
    triggered_matches = [t["match"] for t in triggers if t["triggered"]]
    # On attend A vs B, E vs F, I vs J (car 1.5, 1.75, 4.75 sont triggers)
    assert "A vs B" in triggered_matches
    assert "E vs F" in triggered_matches
    assert "I vs J" in triggered_matches
    # On vérifie qu'il n'y a pas de faux positif
    assert "C vs D" not in triggered_matches
    assert "G vs H" not in triggered_matches
