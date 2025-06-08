"""
Package shared - Modules partagés, configuration globale, logger, gestion de fichiers, helpers et constantes.
"""

from .config import Config
from .logger import setup_logger
from .data_loader import DataLoader
from .helpers import safe_divide, normalize
from .constants import MODULES, DEFAULT_WEIGHTS, CONFIG_PATH

__all__ = [
    "Config",
    "setup_logger",
    "DataLoader",
    "safe_divide",
    "normalize",
    "MODULES",
    "DEFAULT_WEIGHTS",
    "CONFIG_PATH",
]
