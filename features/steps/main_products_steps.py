from behave import *


@Given("After valid login main products page is opened")
def step_impl(context):
    context.page_manager.get_login_page().login_to_portal('standard_user', 'secret_sauce')
    assert context.page_manager.get_login_page().is_valid_login()


@Then("There are 6 products on main page")
def step_impl(context):
    assert context.page_manager.get_main_products_page().get_number_of_products() == 6


@When("I open products details")
def step_impl(context):
    context.page_manager.get_main_products_page().open_product_details()


@When("I add product to cart")
def step_impl(context):
    context.page_manager.get_main_products_page().add_product_to_cart()


@Then("Remove button appears, which means product is added to the cart")
def step_impl(context):
    assert 3 == 2
    #assert context.page_manager.get_main_products_page().check_remove_button_appear()
