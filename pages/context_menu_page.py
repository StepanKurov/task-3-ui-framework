from playwright.sync_api import Page

from ui.web_element import WebElement


class ContextMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.context_area = WebElement(
            self.page.locator("#hot-spot"),
            description="Context area"
        )

    def right_click_context_area(self):
        self.context_area.right_click()
