def make_signal_output(match_id, confidence_score, signals):
    """
    Construit un dictionnaire structuré pour l'output signal.
    """
    # Arrondi le score à 2 décimales pour la lisibilité
    score = round(float(confidence_score), 2)
    # Nettoie les signaux pour ne garder que les champs attendus, au cas où
    clean_signals = [
        {
            "trigger": s.get("trigger"),
            "status": bool(s.get("status", False)),
            "reason": str(s.get("reason", ""))
        }
        for s in signals
    ]
    return {
        "match_id": match_id,
        "confidence_score": score,
        "signals": clean_signals
    }
