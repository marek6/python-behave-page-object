from selenium import webdriver
from features.managers.page_manager import PageManager


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get('https://www.saucedemo.com/')
    context.page_manager = PageManager(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()
