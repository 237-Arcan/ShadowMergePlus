import logging

def setup_logger(name: str) -> logging.Logger:
    """
    Initialise un logger standard pour le module donné.

    Args:
        name (str): Nom du logger.

    Returns:
        logging.Logger: Instance configurée.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
