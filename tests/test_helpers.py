from core.shared.helpers import safe_divide, normalize

def test_safe_divide_basic():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) == 0

def test_normalize_basic():
    values = [1, 2, 3]
    norm = normalize(values)
    assert abs(sum(norm) - 1) < 1e-8
