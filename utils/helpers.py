"""Helper utilities for test automation."""

import logging
from datetime import datetime
from pathlib import Path

from config.settings import settings


def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for test runs."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_timestamp() -> str:
    """Return a timestamp string for reports and screenshots."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def ensure_reports_dir() -> Path:
    """Create reports directory if it does not exist. Return path."""
    settings.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    settings.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    return settings.REPORTS_DIR
