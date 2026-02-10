"""Application and test run settings loaded from environment."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path)


class Settings:
    """Centralized settings for test execution."""

    BASE_URL: str = os.getenv("BASE_URL", "https://uat.expresstoll.com").rstrip("/")
    BROWSER: str = os.getenv("BROWSER", "chromium")
    HEADED: bool = os.getenv("HEADED", "false").lower() == "true"
    SLOW_MO: int = int(os.getenv("SLOW_MO", "0"))
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "30000"))

    # Paths
    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
    REPORTS_DIR: Path = PROJECT_ROOT / "reports"
    SCREENSHOTS_DIR: Path = REPORTS_DIR / "screenshots"


settings = Settings()
