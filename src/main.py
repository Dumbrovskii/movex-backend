import uvicorn

from src.config.logging import setup_logging
from src.app import app


def main() -> None:
    setup_logging()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )

if __name__ == "__main__":
    main()