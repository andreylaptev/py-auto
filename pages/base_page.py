"""Base page class with common actions for all page objects."""

from typing import Optional

from playwright.sync_api import Page

from config.settings import settings


class BasePage:
    """Base class for all page objects. Provides common navigation and interaction methods."""

    def __init__(self, page: Page, url_path: str = "") -> None:
        self.page = page
        self.url = f"{settings.BASE_URL}{url_path}"
        self.timeout = settings.DEFAULT_TIMEOUT

    def navigate(self) -> "BasePage":
        """Navigate to the page URL."""
        self.page.goto(self.url, timeout=self.timeout)
        return self

    def get_title(self) -> str:
        """Return the page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Return the current page URL."""
        return self.page.url

    def wait_for_load_state(self, state: str = "domcontentloaded") -> "BasePage":
        """Wait for the page to reach the given load state."""
        self.page.wait_for_load_state(state, timeout=self.timeout)
        return self

    def take_screenshot(self, name: Optional[str] = None) -> bytes:
        """Take a screenshot and return bytes. Optional name for file."""
        return self.page.screenshot(path=name)

    def click(self, selector: str) -> "BasePage":
        """Click an element by selector."""
        self.page.click(selector, timeout=self.timeout)
        return self

    def fill(self, selector: str, value: str) -> "BasePage":
        """Fill an input by selector."""
        self.page.fill(selector, value, timeout=self.timeout)
        return self

    def get_text(self, selector: str) -> str:
        """Get text content of an element."""
        return self.page.locator(selector).text_content(timeout=self.timeout) or ""
