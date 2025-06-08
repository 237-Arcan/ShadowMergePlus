from core.shared.config import Config

def test_config_loading(tmp_path):
    # Création d'un fichier YAML temporaire
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text("param: value\n")
    cfg = Config(str(cfg_file))
    assert cfg.get("param") == "value"
