from playwright.sync_api import Page

from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page: Page):
        self.page = page

        self.click_here_link = WebElement(
            self.page.locator(".example a"),
            description="Click Here"
        )

    def click_link(self):
        self.click_here_link.click()
