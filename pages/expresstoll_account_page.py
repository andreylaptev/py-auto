"""ExpressToll Account Overview and Payments (after login)."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ExpressTollAccountPage(BasePage):
    """Account Overview: greeting, navigation to Payments, balance."""

    def __init__(self, page: Page) -> None:
        super().__init__(page, url_path="/")

    GREETING_TEXT = "text=HELLO, TESTFIRST!"
    PAYMENT_SUMMARY_HEADING = "text=PAYMENT SUMMARY"
    POPUP_HEADING = "text=ADD ADDITIONAL FUNDS TO MY ACCOUNT"
    FUND_AMOUNT_INPUT = "input[name*='amount' i], input[id*='amount' i], input[placeholder*='amount' i]"
    POPUP_ADD_FUNDS_BUTTON = "[role='dialog'] button:has-text('Add Additional Funds'), .modal button:has-text('Add')"

    def is_greeting_displayed(self) -> bool:
        """Return True if 'HELLO, TESTFIRST!' is visible."""
        return self.is_visible(self.GREETING_TEXT)

    def go_to_payments(self) -> "ExpressTollAccountPage":
        """Navigate to Payments page (link or menu)."""
        self.page.get_by_text("Payments", exact=False).or_(self.page.get_by_text("PAYMENTS")).first.click(
            timeout=self.timeout
        )
        return self

    def is_payment_summary_displayed(self) -> bool:
        """Return True if PAYMENT SUMMARY is visible."""
        return self.is_visible(self.PAYMENT_SUMMARY_HEADING)

    def click_add_additional_funds(self) -> "ExpressTollAccountPage":
        """Click Add Additional Funds button."""
        self.page.get_by_text("Add Additional Funds", exact=False).first.click(timeout=self.timeout)
        return self

    def is_add_funds_popup_visible(self) -> bool:
        """Return True if ADD ADDITIONAL FUNDS TO MY ACCOUNT popup is visible."""
        return self.is_visible(self.POPUP_HEADING)

    def fill_fund_amount(self, amount: str) -> "ExpressTollAccountPage":
        """Enter fund amount in popup (e.g. '6' or '$6')."""
        # Try common input in dialog
        dialog = self.page.locator("[role='dialog'], .modal, [class*='modal']").first
        input_el = dialog.locator("input").first
        input_el.fill(amount, timeout=self.timeout)
        return self

    def click_popup_add_funds(self) -> "ExpressTollAccountPage":
        """Click Add Additional Funds in the popup."""
        dialog = self.page.locator("[role='dialog'], .modal, [class*='modal']").first
        dialog.get_by_text("Add Additional Funds", exact=False).or_(dialog.get_by_role("button", name="Add")).first.click(
            timeout=self.timeout
        )
        return self

    def get_available_balance(self) -> str:
        """Return the available balance text (to compare before/after)."""
        balance_label = self.page.get_by_text("Available Balance", exact=False).or_(
            self.page.get_by_text("Available balance", exact=False)
        ).first
        try:
            parent = balance_label.locator("xpath=..")
            return (parent.text_content(timeout=self.timeout) or "").strip()
        except Exception:
            return (balance_label.text_content(timeout=self.timeout) or "").strip()
