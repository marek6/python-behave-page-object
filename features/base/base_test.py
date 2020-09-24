from features.managers.page_manager import PageManager


class BaseTest:
    pages: PageManager = None

    def __init__(self, browser, context):
        context.pages = PageManager(browser)
