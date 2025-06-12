# tests/test_data_integration.py

from data_integration.data_integration_hub import DataIntegrationHub
import pytest


def test_available_adapters():
    hub = DataIntegrationHub()
    adapters = hub.get_available_adapters()

    assert isinstance(adapters, dict), "Les adaptateurs doivent être retournés sous forme de dictionnaire"
    assert len(adapters) > 0, "Aucun adaptateur n'est disponible"

    for name, adapter in adapters.items():
        assert adapter.is_available() is True or isinstance(adapter.is_available(), bool)


def test_fetch_data_openapi():
    hub = DataIntegrationHub()
    adapters = hub.get_available_adapters()

    if "OpenapiAdapter" not in adapters:
        pytest.skip("OpenapiAdapter non disponible pour ce test")

    result = hub.fetch_data("OpenapiAdapter", relative_path=None)  # Remplace par un chemin réel si besoin
    assert result is not None


def test_invalid_adapter():
    hub = DataIntegrationHub()
    with pytest.raises(ValueError, match="Source inconnue"):
        hub.fetch_data("invalid_source", match_id="12345")
