# tests/test_adapters_loading.py

import pytest
import os
from data_integration.data_integration_hub import DataIntegrationHub

ADAPTERS_DIR = "data_integration/adapters"

def expected_adapters():
    """Génère une liste de noms d’adaptateurs à partir des fichiers *_adapter.py"""
    names = []
    for fname in os.listdir(ADAPTERS_DIR):
        if fname.endswith("_adapter.py") and not fname.startswith("__"):
            base = fname.replace("_adapter.py", "")
            names.append(base)
    return names

def test_all_adapters_are_loaded():
    hub = DataIntegrationHub()
    expected = expected_adapters()

    loaded = list(hub.adapters.keys())

    for name in expected:
        assert name in loaded, f"❌ Adaptateur '{name}' manquant dans hub.adapters"

    print("\n✅ Tous les adaptateurs sont correctement chargés.")
