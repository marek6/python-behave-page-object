from behave import *
from features.pages.login_page import LoginPage


@Given("Login page is opened")
def step_impl(context):
    opened_page = LoginPage(context.browser)
    assert opened_page.check_page_is_opened() is True


@When("I enter invalid login and password and click login button")
def step_impl(context):
    invalid_login = LoginPage(context.browser)
    invalid_login.login_to_portal('bad_login', 'bad_password')


@Then("A popup should appears")
def step_impl(context):
    invalid_login = LoginPage(context.browser)
    assert invalid_login.invalid_login_msg()


@When("I enter valid login and password and click login button")
def step_impl(context):
    valid_login = LoginPage(context.browser)
    valid_login.login_to_portal('standard_user', 'secret_sauce')


@Then("I should be logged into portal")
def step_impl(context):
    valid_login = LoginPage(context.browser)
    assert valid_login.is_valid_login()
