import os

from features.base.webdriver_factory import WebDriverFactory
from features.managers.page_manager import PageManager


def before_scenario(context, scenario):
    context.webdriver_factory = WebDriverFactory()
    context.browser = context.webdriver_factory.get_webdriver_instance()
    context.browser.maximize_window()

    context.page_manager = PageManager(context.browser)


def after_scenario(context, scenario):
    print("scenario status: " + scenario.status.name)
    if scenario.status.name == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")

    context.browser.quit()
