# data_integration/adapters/openapi_adapter.py
from .base_adapter import BaseAdapter
import os

class OpenAPIAdapter(BaseAdapter):
    def __init__(self, repo_path):
        super().__init__()
        self.repo_path = repo_path

    @BaseAdapter.safe_run
    def is_available(self):
        return os.path.isdir(self.repo_path)

    @BaseAdapter.safe_run
    def fetch_data(self, relative_path=None):
        path = os.path.join(self.repo_path, relative_path) if relative_path else self.repo_path
        if os.path.isfile(path):
            return self.read_file(path)
        elif os.path.isdir(path):
            return self.list_files(path)
        else:
            self.logger.warning(f"Chemin invalide: {path}")
            return None

    @BaseAdapter.safe_run
    def list_files(self, dir_path):
        result = []
        for root, _, files in os.walk(dir_path):
            for file in files:
                result.append(os.path.join(root, file))
        return result

    @BaseAdapter.safe_run
    def read_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
