import traceback
import pytest

def test_data_integration():
    print("=== TEST DATA INTEGRATION ===")
    try:
        from data_integration.data_integration_hub import DataIntegrationHub
        from data_integration.orchestrator import DataOrchestrator
        from data_integration.fusion_engine import FusionEngine

        hub = DataIntegrationHub()

        # 1. Vérification des adaptateurs disponibles
        adapters = list(hub.adapters.keys())
        print(f"Adaptateurs disponibles : {adapters}")
        assert len(adapters) > 0, "Aucun adaptateur détecté !"

        # 2. Test de chaque adaptateur
        for name, adapter in hub.adapters.items():
            print(f"Test fetch_data pour adaptateur '{name}'…")
            try:
                data = adapter.fetch_data("test_match_001")
                assert isinstance(data, dict), f"fetch_data de {name} ne retourne pas un dict"
                print(f"  OK - Réponse: {data}")
            except Exception as e:
                print(f"  ERREUR dans {name}: {e}")
                traceback.print_exc()
                raise

        # 3. Test de l'Orchestrator
        orchestrator = DataOrchestrator()
        test_source = adapters[0]
        print(f"Test Orchestrator fuse() avec source '{test_source}'")
        data = orchestrator.fuse(test_source, "test_match_001")
        print(f"  Réponse Orchestrator: {data}")
        assert isinstance(data, dict), "Orchestrator n'a pas retourné un dict"

        # 4. Test de la fusion multi-source
        fusion_engine = FusionEngine()
        sources_multi = adapters[:3] if len(adapters) >= 3 else adapters
        print(f"Test FusionEngine fuse_all() avec sources {sources_multi}")
        fusion_result = fusion_engine.fuse_all("test_match_001", sources_multi)
        print(f"  Fusion multi-source: {fusion_result}")
        assert isinstance(fusion_result, dict), "FusionEngine n'a pas retourné un dict"

        print("=== TOUT EST OK ===")

        # 5. ERREUR VOLONTAIRE : test d'une source inexistante
        print("Test ERREUR VOLONTAIRE avec source inexistante…")
        with pytest.raises(Exception):
            orchestrator.fuse("source_inconnue", "test_match_001")
        print("=== ERREUR VOLONTAIRE DÉTECTÉE ===")

    except Exception:
        print("=== ECHEC DU TEST DATA INTEGRATION ===")
        traceback.print_exc()
        assert False, "Erreur inattendue dans le test data integration"
