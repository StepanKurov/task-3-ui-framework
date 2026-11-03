from playwright.sync_api import Page

from ui.web_element import WebElement


class BasicAuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.result_text = WebElement(
            self.page.locator(".example p"),
            description="Result text"
        )

    def get_result_text(self):
        return self.result_text.get_text_content().strip()
