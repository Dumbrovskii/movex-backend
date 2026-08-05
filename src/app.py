import logging


logger = logging.getLogger(__name__)

def run() -> None:
    logger.info("Application started")
    logger.warning("Redis unavailable")
    logger.error("Database connection failed")