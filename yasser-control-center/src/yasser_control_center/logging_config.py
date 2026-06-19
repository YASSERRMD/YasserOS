"""Logging setup for Yasser Control Center."""

import logging
import os
from pathlib import Path

_LOG_DIR = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "yasser-control-center"
_LOG_FILE = _LOG_DIR / "ycc.log"


def setup_logging(debug: bool = False) -> None:
    level = logging.DEBUG if debug else logging.INFO
    _LOG_DIR.mkdir(parents=True, exist_ok=True)

    fmt = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    handlers = [logging.StreamHandler()]
    try:
        handlers.append(logging.FileHandler(_LOG_FILE))
    except OSError:
        pass

    logging.basicConfig(level=level, format=fmt, datefmt=datefmt, handlers=handlers)
    logging.getLogger("gi").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"ycc.{name}")
