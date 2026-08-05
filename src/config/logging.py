from pathlib import Path
import logging.config
from src.config import settings

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": settings.LOG_LEVEL,
        },

        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "movex.log",
            "formatter": "default",
            "level": settings.LOG_LEVEL,
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },

    "root": {
        "handlers": [
            "console",
            "file",
        ],
        "level": settings.LOG_LEVEL,
    },
}


def setup_logging() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)