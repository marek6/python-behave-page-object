from features.pages.login_page import LoginPage
from features.pages.main_products_page import MainProductsPage
from features.pages.your_cart_page import YourCartPage


class PageManager:
    def __init__(self, browser):
        self.browser = browser

    def get_login_page(self) -> LoginPage:
        return LoginPage(self.browser)

    def get_main_products_page(self) -> MainProductsPage:
        return MainProductsPage(self.browser)

    def get_your_cart_page(self) -> YourCartPage:
        return YourCartPage(self.browser)
