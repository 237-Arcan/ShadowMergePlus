from orchestrator.data_orchestrator import DataOrchestrator

def test_collect_match_data():
    orchestrator = DataOrchestrator()
    result = orchestrator.collect_match_data("match123")

    # Vérifie que le résultat est bien un dictionnaire non vide
    assert isinstance(result, dict)
    assert len(result) > 0

    # Pour chaque adaptateur, on vérifie que la valeur est un dict (soit les données, soit l'erreur)
    for adapter_name, data in result.items():
        assert isinstance(data, dict)
        # Optionnel : si erreur, il doit y avoir la clé "error"
        if "error" in data:
            assert isinstance(data["error"], str)

    # Optionnel : Affiche le résultat pour debug si besoin
    print("Résultat collect_match_data :", result)
