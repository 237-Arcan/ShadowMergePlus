import json

class Logbook:
    """
    Journalisation des sorties des modules et des fusions.
    """
    def __init__(self):
        self.logs = []

    def log_module_output(self, module_name: str, output):
        self.logs.append({"module": module_name, "output": output})

    def log_merged_output(self, merged):
        self.logs.append({"merged_output": merged})

    def export(self, filepath="metasystem_logs.json"):
        with open(filepath, 'w') as f:
            json.dump(self.logs, f, indent=2)
