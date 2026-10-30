from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class ContextMenuPage:
    CONTEXT_MENU_PATH = "/context_menu"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)
        self.context_area = WebElement(
            self.page.locator("#hot-spot"),
            description="Context area"
        )

    def open(self):
        self.page_actions.goto(self.CONTEXT_MENU_PATH)

    def accept_context_menu(self):
        return self.page_actions.run_and_accept_alert(
            self.context_area.right_click
        )
    