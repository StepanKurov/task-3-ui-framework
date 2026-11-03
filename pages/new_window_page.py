from playwright.sync_api import Page

from ui.web_element import WebElement


class NewWindowPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_window_title = WebElement(
            self.page.locator(".example h3"),
            description="New window"
        )

    def get_title(self):
        return self.new_window_title.get_text_content().strip()
