from features.base.webdriver_factory import WebDriverFactory
from features.managers.page_manager import PageManager
from features.utilities.screenshot_helper import ScreenshotHelper


def before_scenario(context, scenario):
    context.webdriver_factory = WebDriverFactory()
    context.driver = context.webdriver_factory.get_webdriver_instance()
    context.driver.maximize_window()

    context.page_manager = PageManager(context.driver)


def after_scenario(context, scenario):
    context.screenshot_helper = ScreenshotHelper()
    context.screenshot_helper = context.screenshot_helper.make_screenshot_when_test_failed(context.driver, scenario)
    context.driver.quit()
