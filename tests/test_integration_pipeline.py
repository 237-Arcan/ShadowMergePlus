import os
import json
import shutil
import tempfile

from signal_engine.signal_orchestrator import SignalOrchestrator

def test_pipeline_end_to_end_and_output_format():
    # Prépare un répertoire temporaire pour l'entrée et la sortie
    tmp_in = tempfile.mkdtemp(prefix="input_")
    tmp_out = tempfile.mkdtemp(prefix="output_")

    try:
        # Crée un fichier match_data.json avec la structure attendue
        match_data = {
            "match_id": "TESTMATCH001",
            "odds": [1.75, 2.10],
            "volumes": [12000, 8500],
            "players": ["Player A", "Player B"],
            "ratings": {"Player A": 7.2}
        }
        in_path = os.path.join(tmp_in, "match_data.json")
        with open(in_path, "w") as f:
            json.dump(match_data, f)

        # Lance l'orchestrateur (pipeline complet)
        orchestrator = SignalOrchestrator(input_dir=tmp_in, output_dir=tmp_out)
        orchestrator.run()

        # Cherche le fichier de sortie
        out_files = [f for f in os.listdir(tmp_out) if f.startswith("signal_") and f.endswith(".json")]
        assert len(out_files) == 1, f"Un seul fichier de sortie attendu, trouvé: {out_files}"

        # Charge le fichier de sortie
        out_path = os.path.join(tmp_out, out_files[0])
        with open(out_path, "r") as f:
            signal_output = json.load(f)

        # Valide la structure du signal_output.json
        assert "match_id" in signal_output
        assert signal_output["match_id"] == match_data["match_id"]
        assert "confidence_score" in signal_output
        assert isinstance(signal_output["confidence_score"], float)
        assert "signals" in signal_output
        assert isinstance(signal_output["signals"], list)
        for signal in signal_output["signals"]:
            assert "trigger" in signal
            assert "status" in signal
            assert isinstance(signal["status"], bool)
            assert "reason" in signal
            assert isinstance(signal["reason"], str)
    finally:
        shutil.rmtree(tmp_in)
        shutil.rmtree(tmp_out)
