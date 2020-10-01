import allure
from allure_commons.types import AttachmentType
import os


class ScreenshotHelper:

    @classmethod
    def make_screenshot_when_test_failed(cls, driver, scenario):
        print("scenario status: " + scenario.status.name)
        if scenario.status.name == "failed":
            if not os.path.exists("failed_scenarios_screenshots"):
                os.makedirs("failed_scenarios_screenshots")
            os.chdir("failed_scenarios_screenshots")
            driver.save_screenshot(scenario.name + "_failed.png")
            allure.attach(driver.get_screenshot_as_png(),
                          name=scenario.name + "_failed.png", attachment_type=AttachmentType.PNG)
