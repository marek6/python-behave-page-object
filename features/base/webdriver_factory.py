from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver

from features.config import BASE_URL, CURRENT_BROWSER


class WebDriverFactory:
    def __init__(self):
        self.current_browser = CURRENT_BROWSER

    def get_webdriver_instance(self):
        if self.current_browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.current_browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.current_browser == "ie":
            driver = webdriver.Ie(IEDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(BASE_URL)
        return driver
