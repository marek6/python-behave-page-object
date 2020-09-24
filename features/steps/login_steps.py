from behave import *

from features.pages.login_page import LoginPage


# class LoginSteps(BaseTest):
#
#     @Given("Login page is opened")
#     def step_impl(self):
#         context.pages.get_login_page.check_page_is_opened()
#


@Given("Login page is opened")
def step_impl(context):
    assert context.page_manager.get_login_page().check_page_is_opened() is True


@When("I enter invalid login and password and click login button")
def step_impl(context):
    context.page_manager.get_login_page().login_to_portal('bad_login', 'bad_password')


@Then("A popup should appears")
def step_impl(context):
    assert context.page_manager.get_login_page().invalid_login_msg()


@When("I enter valid login and password and click login button")
def step_impl(context):
    context.page_manager.get_login_page().login_to_portal('standard_user', 'secret_sauce')


@Then("I should be logged into portal")
def step_impl(context):
    assert context.page_manager.get_login_page().is_valid_login
