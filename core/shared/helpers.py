def safe_divide(a, b):
    """
    Division protégée contre la division par zéro.
    """
    return a / b if b else 0

def normalize(values):
    """
    Normalise une liste de valeurs pour que leur somme fasse 1.
    """
    total = sum(values)
    return [v / total for v in values] if total else values
