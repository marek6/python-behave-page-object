from features.pages.login_page import LoginPage
from features.pages.main_products_page import MainProductsPage


class PageManager:
    def __init__(self, browser):
        self.browser = browser

    def get_login_page(self) -> LoginPage:
        return LoginPage(self.browser)

    def get_main_products_page(self) -> MainProductsPage:
        return MainProductsPage(self.browser)
