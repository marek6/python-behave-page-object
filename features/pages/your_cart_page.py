from features.locators.your_cart_locators import YourCartLocators
from features.base.base_page import BasePage


class YourCartPage(BasePage):
    def add_product_to_cart_from_main_products_list(self):
        self.click_element(YourCartLocators.add_to_cart_button)

    def open_your_cart(self):
        self.click_element(YourCartLocators.cart_icon)

    def check_is_product_in_basket(self):
        product = self.is_element_visible(YourCartLocators.product_in_cart)
        return product

    def check_is_continue_shopping_button_visible(self):
        button = self.is_element_visible(YourCartLocators.continue_shopping_button)
        return button
