import os
import importlib
from typing import Optional, Dict, Type
from .adapters.base_adapter import BaseAdapter

class DataIntegrationHub:
    def __init__(self):
        self.adapters: Dict[str, BaseAdapter] = {}
        self._load_adapters()

    def _load_adapters(self):
        adapters_dir = os.path.join(os.path.dirname(__file__), "adapters")
        for file in os.listdir(adapters_dir):
            if file.endswith("_adapter.py") and file != "base_adapter.py":
                module_name = f"data_integration.adapters.{file[:-3]}"
                class_name = ''.join(word.capitalize() for word in file.replace("_adapter.py", "").split("_")) + "Adapter"
                module = importlib.import_module(module_name)
                adapter_cls: Type[BaseAdapter] = getattr(module, class_name, None)
                if adapter_cls:
                    self.adapters[class_name.replace("Adapter", "").lower()] = adapter_cls()

    def get_adapter(self, name: str) -> Optional[BaseAdapter]:
        return self.adapters.get(name.lower())
