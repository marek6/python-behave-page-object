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
            browser = webdriver.Chrome(ChromeDriverManager().install())
        elif self.current_browser == "firefox":
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.current_browser == "ie":
            browser = webdriver.Ie(IEDriverManager().install())
        else:
            browser = webdriver.Chrome(ChromeDriverManager().install())

        browser.get(BASE_URL)
        return browser
