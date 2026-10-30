from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class WindowsPage:
    WINDOWS_PATH = "/windows"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.click_here_link = WebElement(
            self.page.locator(".example a"),
            description="Click Here"
        )

    def open(self):
        self.page_actions.goto(self.WINDOWS_PATH)

    def click_link(self):
        self.click_here_link.click()

    def open_new_window(self):
        with self.page_actions.expect_new_page() as new_page_info:
            self.click_link()
        new_page = new_page_info.value
        return new_page

    def switch_to_main_page(self):
        self.page_actions.bring_to_front()

    def get_open_pages_count(self):
        return self.page_actions.get_pages_count()