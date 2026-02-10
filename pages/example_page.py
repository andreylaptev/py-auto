"""Example page object - replace with your application pages."""

from pages.base_page import BasePage
from playwright.sync_api import Page


class ExamplePage(BasePage):
    """Example page for demo. Adapt selectors and methods to your app."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, url_path="/")

    # Define locators as class attributes for reuse
    HEADING = "h1"
    SEARCH_INPUT = 'input[name="q"]'
    SEARCH_BUTTON = 'button[type="submit"]'

    def get_heading_text(self) -> str:
        """Get the main heading text."""
        return self.get_text(self.HEADING)

    def search(self, query: str) -> None:
        """Perform a search (example interaction)."""
        self.fill(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
