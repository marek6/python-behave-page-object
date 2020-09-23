from behave import *
from features.pages.main_products_page import MainProductsPage
from features.pages.login_page import LoginPage


@Given("After valid login main products page is opened")
def step_impl(context):
    valid_login = LoginPage(context.browser)
    valid_login.login_to_portal('standard_user', 'secret_sauce')
    assert valid_login.is_valid_login()


@Then("There are 6 products on main page")
def step_impl(context):
    main_products = MainProductsPage(context.browser)
    assert main_products.get_number_of_products() == 6


@When("I open products details")
def step_impl(context):
    product_details = MainProductsPage(context.browser)
    product_details.open_product_details()


@When("I add product to cart")
def step_impl(context):
    add_product = MainProductsPage(context.browser)
    add_product.add_product_to_cart()


@Then("Remove button appears, which means product is added to the cart")
def step_impl(context):
    remove_button = MainProductsPage(context.browser)
    assert remove_button.check_remove_button_appear()
