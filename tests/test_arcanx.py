from core.arcanx.astro import AstroEngine

def test_astro_engine_instantiation():
    engine = AstroEngine()
    assert isinstance(engine, AstroEngine)
