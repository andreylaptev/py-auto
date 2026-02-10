"""ExpressToll home page - links and sign-in entry point."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ExpressTollHomePage(BasePage):
    """ExpressToll home page. Verifies main links and provides sign-in navigation."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, url_path="/")

    # Home page links (text-based locators)
    LINK_PAY_YOUR_TOLL = "text=PAY YOUR TOLL"
    LINK_CREATE_ACCOUNT = "text=CREATE ACCOUNT"
    LINK_SIGN_IN = "text=SIGN IN"

    def are_home_links_displayed(self) -> bool:
        """Return True if PAY YOUR TOLL, CREATE ACCOUNT and SIGN IN are visible."""
        return (
            self.is_visible(self.LINK_PAY_YOUR_TOLL)
            and self.is_visible(self.LINK_CREATE_ACCOUNT)
            and self.is_visible(self.LINK_SIGN_IN)
        )

    def click_sign_in(self) -> "ExpressTollHomePage":
        """Click the SIGN IN link."""
        self.click(self.LINK_SIGN_IN)
        return self
