from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.multi_web_element import MultiWebElement


class ScrollPage:
    SCROLL_PATH = "/infinite_scroll"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(self.page)

        self.paragraphs = MultiWebElement(
            self.page.locator(".jscroll-added"),
            description="Scroll"
        )

    def open(self):
        self.page_actions.goto(self.SCROLL_PATH)

    def get_paragraph_count(self):
        return self.paragraphs.count()

    def scroll_to_last_paragraph(self):
        paragraph_count = self.get_paragraph_count()
        last_index = paragraph_count - 1
        last_paragraph = self.paragraphs.nth(last_index)
        last_paragraph.scroll_into_view_if_needed()