import yaml

class Config:
    """
    Gestion centralisée de la configuration du système.
    """
    def __init__(self, filepath="config.yaml"):
        with open(filepath, 'r') as f:
            self.settings = yaml.safe_load(f)

    def get(self, key, default=None):
        return self.settings.get(key, default)
