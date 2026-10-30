from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class BasicAuthPage:
    BASIC_AUTH_PATH = "/basic_auth"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.result_text = WebElement(
            self.page.locator(".example p"),
            description="Result text"
        )

    def get_result_text(self):
        return self.result_text.get_text_content().strip()

    def open(self):
        self.page_actions.goto(self.BASIC_AUTH_PATH)
