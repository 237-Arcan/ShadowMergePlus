from core.shadowodds.khawatim import KhawatimEngine

def test_khawatim_engine_instantiation():
    engine = KhawatimEngine()
    assert isinstance(engine, KhawatimEngine)

def test_detect_final_signals_cycle_change():
    engine = KhawatimEngine()
    # Cas : Fin de cycle détectée
    result = engine.detect_final_signals([10, 8])
    assert result == "Fin de cycle suspectée"
    # Cas : Cycle stable
    result = engine.detect_final_signals([8, 10])
    assert result == "Cycle stable"
