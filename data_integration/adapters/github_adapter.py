import os
import logging

class GithubAdapter:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.logger = logging.getLogger(__name__)

    def is_available(self):
        return os.path.isdir(self.repo_path)

    def fetch_data(self, relative_path=None):
        try:
            path = os.path.join(self.repo_path, relative_path) if relative_path else self.repo_path
            if os.path.isfile(path):
                return self.read_file(path)
            elif os.path.isdir(path):
                return self.list_files(path)
            else:
                raise FileNotFoundError(f"Chemin invalide : {path}")
        except Exception as e:
            self.logger.error(f"Erreur dans fetch_data : {e}")
            return None

    def list_files(self, dir_path, ext_filter=None):
        result = []
        for root, _, files in os.walk(dir_path):
            for file in files:
                if not ext_filter or file.endswith(ext_filter):
                    full_path = os.path.join(root, file)
                    result.append(full_path)
        return result

    def search_files_by_type(self, extension):
        return [
            os.path.join(root, file)
            for root, _, files in os.walk(self.repo_path)
            for file in files if file.endswith(extension)
        ]

    def search_files_by_keyword(self, keyword):
        results = []
        for root, _, files in os.walk(self.repo_path):
            for file in files:
                try:
                    full_path = os.path.join(root, file)
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        if keyword in f.read():
                            results.append(full_path)
                except Exception:
                    continue
        return results

    def read_file(self, filepath, preview=False, max_lines=100):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                if preview:
                    return ''.join([next(f) for _ in range(max_lines)])
                return f.read()
        except Exception as e:
            self.logger.error(f"Erreur lecture fichier {filepath} : {e}")
            return None
