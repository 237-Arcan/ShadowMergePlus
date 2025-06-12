import pytest
from data_integration.orchestrator import DataOrchestrator

def test_data_orchestrator_basic():
    orchestrator = DataOrchestrator()
    
    # On simule une source connue (doit exister dans tes adaptateurs fonctionnels)
    source = "openapi"
    match_id = "12345"

    try:
        result = orchestrator.fuse(source, match_id=match_id)
        assert isinstance(result, dict), "Le résultat devrait être un dictionnaire"
        print(f"[Test] Fusion réussie : {result}")
    except NotImplementedError:
        pytest.skip("Méthode 'fuse' non encore implémentée pour cette source.")
    except Exception as e:
        pytest.fail(f"Erreur inattendue : {e}")
