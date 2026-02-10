"""ExpressToll sign-in form at /sign-in."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ExpressTollLoginPage(BasePage):
    """Sign-in form: account number and password (from playwright-cli snapshot)."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, url_path="/sign-in")

    def fill_account_number(self, value: str) -> "ExpressTollLoginPage":
        """Fill account number (placeholder: Account Number or Email Address)."""
        self.page.get_by_placeholder("Account Number or Email Address").fill(
            value, timeout=self.timeout
        )
        return self

    def fill_password(self, value: str) -> "ExpressTollLoginPage":
        """Fill password."""
        self.page.get_by_placeholder("Password").fill(value, timeout=self.timeout)
        return self

    def click_sign_in_submit(self) -> "ExpressTollLoginPage":
        """Click the Sign In submit button."""
        self.page.get_by_role("button", name="Sign In").click(timeout=self.timeout)
        return self

    def sign_in(self, account_number: str, password: str) -> "ExpressTollLoginPage":
        """Fill credentials and submit."""
        self.fill_account_number(account_number)
        self.fill_password(password)
        self.click_sign_in_submit()
        return self
