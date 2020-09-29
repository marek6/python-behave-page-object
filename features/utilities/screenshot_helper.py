import allure
from allure_commons.types import AttachmentType
import os


class ScreenshotHelper:

    @classmethod
    def make_screenshot_when_test_failed(cls, browser, scenario):
        print("scenario status: " + scenario.status.name)
        if scenario.status.name == "failed":
            if not os.path.exists("failed_scenarios_screenshots"):
                os.makedirs("failed_scenarios_screenshots")
            os.chdir("failed_scenarios_screenshots")
            browser.save_screenshot(scenario.name + "_failed.png")
            allure.attach(browser.get_screenshot_as_png(),
                          name=scenario.name + "_failed.png", attachment_type=AttachmentType.PNG)
