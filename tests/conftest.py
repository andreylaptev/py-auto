"""Pytest fixtures for Playwright and test configuration."""

import pytest

from config.settings import settings
from utils.helpers import ensure_reports_dir


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Launch args for browser (headed, slow_mo)."""
    return {
        "headless": not settings.HEADED,
        "slow_mo": settings.SLOW_MO,
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """Default context args (viewport, base_url)."""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "base_url": settings.BASE_URL,
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def base_url():
    """Base URL for navigation."""
    return settings.BASE_URL


@pytest.fixture(scope="function", autouse=True)
def set_page_timeout(page):
    """Set default timeout on every page."""
    page.set_default_timeout(settings.DEFAULT_TIMEOUT)
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    if rep.when == "call" and rep.failed and "page" in item.funcargs:
        try:
            ensure_reports_dir()
            path = settings.SCREENSHOTS_DIR / f"{item.name}.png"
            item.funcargs["page"].screenshot(path=str(path))
        except Exception:
            pass
