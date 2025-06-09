# data_integration/adapters/base_adapter.py
import logging
from functools import wraps

class BaseAdapter:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def safe_run(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            try:
                self.logger.debug(f"Appel de {method.__name__} avec args={args}, kwargs={kwargs}")
                return method(self, *args, **kwargs)
            except Exception as e:
                self.logger.error(f"Erreur dans {method.__name__}: {e}")
                return None
        return wrapper
