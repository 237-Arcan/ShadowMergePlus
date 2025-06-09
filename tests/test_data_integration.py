import pytest
from data_integration.data_integration_hub import DataIntegrationHub

def test_available_adapters():
    hub = DataIntegrationHub()
    adapters = hub.get_available_adapters()
    assert isinstance(adapters, list)
    assert "openapi" in adapters
    assert "soccerdata" in adapters
    assert "sportsbetting" in adapters
    assert "bet365" in adapters
    assert "sportsbook" in adapters
    assert "whoscored" in adapters

def test_fetch_data_openapi():
    hub = DataIntegrationHub()
    result = hub.fetch_data("openapi", match_id="12345")
    assert isinstance(result, dict) or result is None

def test_invalid_adapter():
    hub = DataIntegrationHub()
    result = hub.fetch_data("invalid_source", match_id="12345")
    assert result is None
