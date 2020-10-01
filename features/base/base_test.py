from features.managers.page_manager import PageManager


class BaseTest:
    pages: PageManager = None

    def __init__(self, driver, context):
        context.pages = PageManager(driver)
