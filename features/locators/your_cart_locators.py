from selenium.webdriver.common.by import By


class YourCartLocators:
    cart_icon = (By.CSS_SELECTOR, '.shopping_cart_badge')
    continue_shopping_button = (By.CSS_SELECTOR, '.btn_secondary')
    product_in_cart = (By.CSS_SELECTOR, '.inventory_item_name')
    add_to_cart_button = (By.CSS_SELECTOR, '.btn_inventory')

