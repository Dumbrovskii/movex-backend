from src.config.logging import setup_logging
from .app import run


setup_logging()

def main() -> None:
    run()

if __name__ == "__main__":
    main()