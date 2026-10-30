from playwright.sync_api import Page

from ui.web_element import WebElement
from ui.page_actions import PageActions


class NewWindowPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.new_window_title = WebElement(
            self.page.locator(".example h3"),
            description="New window"
        )

    def get_title(self):
        return self.new_window_title.get_text_content()

    def close(self):
        self.page_actions.close_page()
