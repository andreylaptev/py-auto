"""ExpressToll home page - links and sign-in entry point."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ExpressTollHomePage(BasePage):
    """ExpressToll home page. Verifies main links and provides sign-in navigation."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, url_path="/")

    def are_home_links_displayed(self) -> bool:
        """Return True if PAY YOUR TOLL, CREATE ACCOUNT and SIGN IN are visible (title case on site)."""
        return (
            self.page.get_by_text("Pay Your Toll", exact=False).first.is_visible(timeout=self.timeout)
            and self.page.get_by_text("Create Account", exact=False).first.is_visible(timeout=self.timeout)
            and self.page.get_by_text("Sign In", exact=False).first.is_visible(timeout=self.timeout)
        )

    def click_sign_in(self) -> "ExpressTollHomePage":
        """Click the SIGN IN link (navigates to /sign-in)."""
        self.page.get_by_role("link", name="Sign In").click(timeout=self.timeout)
        return self
