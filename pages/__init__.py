"""Page Object Model - page classes for test automation."""

from pages.base_page import BasePage
from pages.expresstoll_account_page import ExpressTollAccountPage
from pages.expresstoll_home_page import ExpressTollHomePage
from pages.expresstoll_login_page import ExpressTollLoginPage

__all__ = [
    "BasePage",
    "ExpressTollAccountPage",
    "ExpressTollHomePage",
    "ExpressTollLoginPage",
]
