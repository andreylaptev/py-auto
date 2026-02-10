"""ExpressToll sign-in form (after clicking Sign In)."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ExpressTollLoginPage(BasePage):
    """Sign-in form: account number and password."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, url_path="/")

    # Common patterns for account/password - adjust if site uses different ids/names
    ACCOUNT_NUMBER_INPUT = "input[name='accountNumber'], input[id*='account'], input[placeholder*='account' i]"
    PASSWORD_INPUT = "input[name='password'], input[type='password'], input[id*='password']"
    SIGN_IN_SUBMIT = "button:has-text('Sign In'), input[type='submit'][value*='Sign' i], button[type='submit']"

    def fill_account_number(self, value: str) -> "ExpressTollLoginPage":
        """Fill account number. Uses first matching input if multiple selectors."""
        locator = self.page.locator(self.ACCOUNT_NUMBER_INPUT).first
        locator.fill(value, timeout=self.timeout)
        return self

    def fill_password(self, value: str) -> "ExpressTollLoginPage":
        """Fill password."""
        self.page.locator(self.PASSWORD_INPUT).first.fill(value, timeout=self.timeout)
        return self

    def click_sign_in_submit(self) -> "ExpressTollLoginPage":
        """Click the Sign In submit button."""
        self.page.locator(self.SIGN_IN_SUBMIT).first.click(timeout=self.timeout)
        return self

    def sign_in(self, account_number: str, password: str) -> "ExpressTollLoginPage":
        """Fill credentials and submit."""
        self.fill_account_number(account_number)
        self.fill_password(password)
        self.click_sign_in_submit()
        return self
