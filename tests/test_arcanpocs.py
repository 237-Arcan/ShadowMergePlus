from core.arcanpocs.filters import apply_filters

def test_apply_filters_basic():
    points = [("A", 0.6), ("B", 0.3), ("C", 0.8)]
    filtered = apply_filters(points, threshold=0.5)
    assert filtered == [("A", 0.6), ("C", 0.8)]
