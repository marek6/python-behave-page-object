from features.base.webdriver_factory import WebDriverFactory
from features.managers.page_manager import PageManager


def before_scenario(context, scenario):
    context.webdriver_factory = WebDriverFactory()
    context.browser = context.webdriver_factory.get_webdriver_instance()
    context.browser.maximize_window()

    context.page_manager = PageManager(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()
