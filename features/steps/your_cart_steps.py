from behave import *


@Given("User is logged into portal")
def step_impl(context):
    context.page_manager.get_login_page().login_to_portal('standard_user', 'secret_sauce')
    assert context.page_manager.get_login_page().is_valid_login()


@Step("Product is added to the cart from main products list")
def step_impl(context):
    context.page_manager.get_your_cart_page().add_product_to_cart_from_main_products_list()


@When("I open cart")
def step_impl(context):
    context.page_manager.get_your_cart_page().open_your_cart()


@Then("There is added product")
def step_impl(context):
    assert context.page_manager.get_your_cart_page().check_is_product_in_basket()


@Step("There is continue shopping button")
def step_impl(context):
    assert context.page_manager.get_your_cart_page().check_is_continue_shopping_button_visible()
