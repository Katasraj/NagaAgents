import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

class Logging:
    def log(self,name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        # add the file handler only once, even if log() is called many times
        if not logger.handlers:
            handler = logging.FileHandler(LOG_DIR / "logFile1.log", mode="w")
            handler.setFormatter(logging.Formatter(
                '%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%y %I:%M:%S %p'
            ))
            logger.addHandler(handler)
        return logger
