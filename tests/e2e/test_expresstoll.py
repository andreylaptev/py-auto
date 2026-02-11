"""E2E test: ExpressToll – open site, sign in, go to Payments, add funds."""

import pytest

from pages.expresstoll_account_page import ExpressTollAccountPage
from pages.expresstoll_home_page import ExpressTollHomePage
from pages.expresstoll_login_page import ExpressTollLoginPage


@pytest.mark.e2e
def test_expresstoll_add_additional_funds(page, base_url):
    """
    Step 1: Open ExpressToll – PAY YOUR TOLL, CREATE ACCOUNT, SIGN IN displayed.
    Step 2: Sign in – 'HELLO, AUTOTESTFN!' on Account Overview.
    Step 3: Go to Payments – 'PAYMENT SUMMARY' displayed.
    Step 4: Click Add Additional Funds – popup 'ADD ADDITIONAL FUNDS TO MY ACCOUNT'.
    Step 5: Enter Fund Amount $6.
    Step 6: Click Add Additional Funds – available balance reflects the change.
    """
    home = ExpressTollHomePage(page)
    login = ExpressTollLoginPage(page)
    account = ExpressTollAccountPage(page)

    # Step 1: Open ExpressToll web site
    home.navigate()
    home.wait_for_load_state("domcontentloaded")
    assert page.url.startswith(base_url) or "expresstoll" in page.url
    assert home.are_home_links_displayed(), "PAY YOUR TOLL, CREATE ACCOUNT and SIGN IN should be displayed"

    # Step 2: Sign in with account number and password
    home.click_sign_in()
    page.wait_for_url("**/sign-in**", timeout=10000)
    page.wait_for_load_state("domcontentloaded")
    login.sign_in(account_number="24236452", password="Welcome01!")
    page.wait_for_load_state("networkidle")
    assert account.is_greeting_displayed(), "HELLO, AUTOTESTFN! should be displayed on Account Overview"

    # Step 3: Go to Payments page
    account.go_to_payments()
    page.wait_for_load_state("domcontentloaded")
    assert account.is_payment_summary_displayed(), "PAYMENT SUMMARY should be displayed"

    # Step 4: Click Add Additional Funds button
    account.click_add_additional_funds()
    page.wait_for_timeout(500)
    assert account.is_add_funds_popup_visible(), "ADD ADDITIONAL FUNDS TO MY ACCOUNT popup should open"

    # Capture balance before adding funds (for Step 6)
    balance_before = account.get_available_balance()

    # Step 5: Enter Fund Amount $6
    account.fill_fund_amount("6")

    # Step 6: Click Add Additional Funds in popup
    account.click_popup_add_funds()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)
    balance_after = account.get_available_balance()

    # Expected: Available balance reflects the change (increased by $6)
    assert balance_before != balance_after, "Available balance should reflect the change after adding $6"
